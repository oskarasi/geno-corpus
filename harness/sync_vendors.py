#!/usr/bin/env python3
"""Re-vendor all apps in manifest.json from GitHub remotes (oskarasi/<id>).

For each app: resolve main SHA via gh api, download tarball at that commit,
copy Main.geno / geno.toml / *.geno / README / LICENSE into apps/<id>/,
write SOURCE.json with {repo, commit, vendored_at}.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"
APPS_DIR = ROOT / "apps"

KEEP_NAMES = {"Main.geno", "geno.toml", "README.md", "README", "LICENSE", "LICENSE.md"}


def load_manifest() -> list[dict]:
    return json.loads(MANIFEST.read_text())["apps"]


def gh_api_text(path: str, jq: str | None = None) -> str:
    cmd = ["gh", "api", path]
    if jq:
        cmd.extend(["--jq", jq])
    for attempt in range(6):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            return proc.stdout.strip()
        err = (proc.stderr or proc.stdout or "").strip()
        if attempt < 5 and ("rate limit" in err.lower() or "403" in err or "502" in err):
            time.sleep(min(2 ** attempt, 30))
            continue
        raise RuntimeError(f"gh api {path} failed (rc={proc.returncode}): {err[:500]}")
    raise RuntimeError(f"gh api {path} failed after retries")


def gh_api_bytes(path: str) -> bytes:
    cmd = ["gh", "api", path]
    for attempt in range(6):
        proc = subprocess.run(cmd, capture_output=True)
        if proc.returncode == 0:
            return proc.stdout
        err = (proc.stderr or b"").decode(errors="replace")
        if attempt < 5 and ("rate limit" in err.lower() or "403" in err or "502" in err):
            time.sleep(min(2 ** attempt, 30))
            continue
        raise RuntimeError(f"gh api {path} failed (rc={proc.returncode}): {err[:500]}")
    raise RuntimeError(f"gh api {path} failed after retries")


def parse_geno_files(toml_text: str) -> list[str]:
    m = re.search(r"files\s*=\s*\[(.*?)\]", toml_text, re.S)
    if not m:
        return []
    names = re.findall(r'["\']([^"\']+)["\']', m.group(1))
    out = []
    for n in names:
        out.append(n if n.endswith(".geno") else f"{n}.geno")
    return out


def extract_wanted(tar_bytes: bytes) -> dict[str, bytes]:
    """Map basename -> content for root-level wanted files from a GitHub tarball."""
    wanted: dict[str, bytes] = {}
    with tarfile.open(fileobj=BytesIO(tar_bytes), mode="r:gz") as tf:
        members = [m for m in tf.getmembers() if m.isfile()]
        # tarball paths look like: oskarasi-repo-<sha>/filename
        for m in members:
            parts = Path(m.name).parts
            if len(parts) != 2:
                # skip nested dirs for now (corpus apps are flat)
                continue
            name = parts[1]
            if name in KEEP_NAMES or name.endswith(".geno"):
                f = tf.extractfile(m)
                if f is not None:
                    wanted[name] = f.read()
    return wanted


def vendor_app(app_id: str) -> dict:
    repo = f"oskarasi/{app_id}"
    sha = gh_api_text(f"repos/{repo}/commits/main", jq=".sha")
    if not sha or len(sha) < 7:
        raise RuntimeError(f"No main SHA for {repo}: {sha!r}")

    tar_bytes = gh_api_bytes(f"repos/{repo}/tarball/{sha}")
    files = extract_wanted(tar_bytes)
    if not files:
        raise RuntimeError(f"Empty extract for {repo}@{sha[:12]}")

    # Ensure geno.toml-listed modules are present (warn if missing from tarball)
    if "geno.toml" in files:
        listed = parse_geno_files(files["geno.toml"].decode("utf-8", errors="replace"))
        missing = [f for f in listed if f not in files]
        if missing:
            raise RuntimeError(f"{repo}: geno.toml lists missing files: {missing}")

    if "Main.geno" not in files and "geno.toml" not in files:
        raise RuntimeError(f"{repo}: no Main.geno or geno.toml")

    dest_dir = APPS_DIR / app_id
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Remove previous vendored files (keep SOURCE.json until we overwrite)
    for p in list(dest_dir.iterdir()):
        if p.is_file() and p.name != "SOURCE.json":
            p.unlink()

    for name, content in files.items():
        (dest_dir / name).write_bytes(content)

    vendored_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source = {
        "repo": f"https://github.com/{repo}",
        "commit": sha,
        "vendored_at": vendored_at,
    }
    (dest_dir / "SOURCE.json").write_text(json.dumps(source, indent=2) + "\n")
    return {"id": app_id, "commit": sha, "files": sorted(files), "ok": True}


def main() -> int:
    apps = load_manifest()
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    results = []
    failures = []
    total = len([a for a in apps if not only or a["id"] in only])
    print(f"Vendoring {total} apps from GitHub remotes into {APPS_DIR} ...", flush=True)
    i = 0
    for app in apps:
        app_id = app["id"]
        if only and app_id not in only:
            continue
        i += 1
        print(f"[{i}/{total}] {app_id} ...", flush=True)
        try:
            r = vendor_app(app_id)
            print(f"  ok {r['commit'][:12]} ({len(r['files'])} files)", flush=True)
            results.append(r)
        except Exception as e:
            print(f"  FAIL: {e}", flush=True)
            failures.append({"id": app_id, "error": str(e)})
            time.sleep(1)

    print(f"\nDone: {len(results)} ok, {len(failures)} failed", flush=True)
    if failures:
        for f in failures:
            print(f"  - {f['id']}: {f['error']}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
