#!/usr/bin/env python3
"""Run the geno-corpus conformance suite against a pinned geno-lang."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"
PIN = ROOT / "pin.json"
RESULTS_DIR = ROOT / "results"
SUMMARY_TEMPLATE = Path(__file__).parent / "summary.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def resolve_geno(geno_bin: str | None) -> str:
    if geno_bin:
        p = Path(geno_bin)
        if p.exists():
            return str(p.resolve())
        # allow bare name on PATH
        found = shutil.which(geno_bin)
        if found:
            return found
        raise SystemExit(f"geno binary not found: {geno_bin}")

    preferred = Path("/workspace/geno-venv/bin/geno")
    if preferred.exists():
        return str(preferred)

    found = shutil.which("geno")
    if found:
        return found

    # CI / local bootstrap from pin.json
    pin = load_json(PIN)
    venv_dir = ROOT / ".venv"
    geno_path = venv_dir / "bin" / "geno"
    if not geno_path.exists():
        print(f"Creating venv at {venv_dir} and installing {pin['pip']} ...")
        venv.create(venv_dir, with_pip=True)
        pip = venv_dir / "bin" / "pip"
        subprocess.check_call([str(pip), "install", "-U", "pip"])
        subprocess.check_call([str(pip), "install", pin["pip"]])
    if not geno_path.exists():
        raise SystemExit("Failed to install geno into .venv")
    return str(geno_path)


def select_apps(tier: str) -> list[dict]:
    apps = load_json(MANIFEST)["apps"]
    if tier == "all":
        return apps
    selected = [a for a in apps if a["tier"] == tier]
    if not selected:
        raise SystemExit(f"No apps for tier={tier!r}")
    return selected


def run_cmd(cmd: list[str], cwd: Path) -> tuple[int, str, float]:
    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=120,
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, out.strip(), time.perf_counter() - t0
    except subprocess.TimeoutExpired as e:
        out = ((e.stdout or b"") if isinstance(e.stdout, (bytes, bytearray)) else (e.stdout or ""))  # type: ignore
        if isinstance(out, bytes):
            out = out.decode(errors="replace")
        err = ((e.stderr or b"") if isinstance(e.stderr, (bytes, bytearray)) else (e.stderr or ""))  # type: ignore
        if isinstance(err, bytes):
            err = err.decode(errors="replace")
        return 124, (str(out) + str(err) + "\nTIMEOUT").strip(), time.perf_counter() - t0


def run_app(geno: str, app: dict) -> dict:
    path = ROOT / app["path"]
    main = path / "Main.geno"
    toml = path / "geno.toml"

    if not path.is_dir():
        return {
            "id": app["id"],
            "tier": app["tier"],
            "ok": False,
            "seconds": 0.0,
            "error": f"missing path {app['path']}",
            "test_ok": False,
            "run_ok": False,
        }

    # geno test: prefer project dir when geno.toml exists, else Main.geno
    if toml.exists():
        test_target = [geno, "test", "."]
        test_cwd = path
    elif main.exists():
        test_target = [geno, "test", str(main)]
        test_cwd = path
    else:
        return {
            "id": app["id"],
            "tier": app["tier"],
            "ok": False,
            "seconds": 0.0,
            "error": "no Main.geno or geno.toml",
            "test_ok": False,
            "run_ok": False,
        }

    test_rc, test_out, test_s = run_cmd(test_target, test_cwd)
    test_ok = test_rc == 0

    # geno run: Main.geno if present, else project dir
    if main.exists():
        run_target = [geno, "run", str(main.name)]
        run_cwd = path
    else:
        run_target = [geno, "run", "."]
        run_cwd = path

    run_rc, run_out, run_s = run_cmd(run_target, run_cwd)
    run_ok = run_rc == 0

    ok = test_ok and run_ok
    error = ""
    if not test_ok:
        error += f"test failed (rc={test_rc}): {test_out[-800:]}"
    if not run_ok:
        if error:
            error += " | "
        error += f"run failed (rc={run_rc}): {run_out[-800:]}"

    return {
        "id": app["id"],
        "tier": app["tier"],
        "ok": ok,
        "seconds": round(test_s + run_s, 3),
        "error": error,
        "test_ok": test_ok,
        "run_ok": run_ok,
    }


def write_results(results: list[dict], tier: str, geno: str) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    pin = load_json(PIN)
    payload = {
        "tier": tier,
        "geno": geno,
        "pin": pin,
        "passed": sum(1 for r in results if r["ok"]),
        "failed": sum(1 for r in results if not r["ok"]),
        "total": len(results),
        "apps": results,
    }
    out = RESULTS_DIR / "latest.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")

    # summary.md from template
    template = SUMMARY_TEMPLATE.read_text() if SUMMARY_TEMPLATE.exists() else (
        "# Corpus results\n\n"
        "Tier: {tier} | geno: {geno} | pin: {pin}\n\n"
        "Passed: {passed} / {total} (failed: {failed})\n\n"
        "{table}\n"
    )
    rows = ["| App | Tier | Status | Seconds | Error |", "|---|---|---|---|---|"]
    for r in results:
        status = "PASS" if r["ok"] else "FAIL"
        err = (r.get("error") or "").replace("|", "\\|").replace("\n", " ")[:120]
        rows.append(f"| {r['id']} | {r['tier']} | {status} | {r['seconds']} | {err} |")
    summary = template.format(
        tier=tier,
        geno=geno,
        pin=pin.get("pip", ""),
        passed=payload["passed"],
        failed=payload["failed"],
        total=payload["total"],
        table="\n".join(rows),
    )
    (RESULTS_DIR / "summary.md").write_text(summary)
    return out


def print_table(results: list[dict]) -> None:
    print()
    print(f"{'APP':<28} {'TIER':<10} {'TEST':<6} {'RUN':<6} {'SEC':>7}  STATUS")
    print("-" * 72)
    for r in results:
        print(
            f"{r['id']:<28} {r['tier']:<10} "
            f"{'ok' if r['test_ok'] else 'FAIL':<6} "
            f"{'ok' if r['run_ok'] else 'FAIL':<6} "
            f"{r['seconds']:>7.3f}  "
            f"{'PASS' if r['ok'] else 'FAIL'}"
        )
    passed = sum(1 for r in results if r["ok"])
    print("-" * 72)
    print(f"{passed}/{len(results)} passed")


def main() -> int:
    ap = argparse.ArgumentParser(description="Geno corpus conformance harness")
    ap.add_argument(
        "--tier",
        choices=["flagship", "reference", "corpus", "all"],
        default="all",
        help="Which apps to run (default: all)",
    )
    ap.add_argument("--geno-bin", default=None, help="Path to geno binary")
    ap.add_argument("--fail-fast", action="store_true", help="Stop on first failure")
    args = ap.parse_args()

    geno = resolve_geno(args.geno_bin)
    apps = select_apps(args.tier)
    print(f"geno={geno}")
    print(f"tier={args.tier} apps={len(apps)}")

    results: list[dict] = []
    for app in apps:
        print(f"→ {app['id']} ({app['tier']}) ...", flush=True)
        r = run_app(geno, app)
        results.append(r)
        status = "PASS" if r["ok"] else "FAIL"
        print(f"  {status} in {r['seconds']:.3f}s", flush=True)
        if not r["ok"] and args.fail_fast:
            break

    print_table(results)
    out = write_results(results, args.tier, geno)
    print(f"Wrote {out}")

    if any(not r["ok"] for r in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
