#!/usr/bin/env python3
"""Run the geno-corpus conformance suite against a pinned geno-lang."""

from __future__ import annotations

import argparse
import os
import json
import re
import shutil
import subprocess
import sys
import tempfile
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


def geno_version(geno: str) -> str:
    try:
        proc = subprocess.run(
            [geno, "--version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        text = ((proc.stdout or "") + (proc.stderr or "")).strip()
        return text.splitlines()[0].strip() if text else "unknown"
    except Exception as e:
        return f"unknown ({e})"


def resolve_geno(geno_bin: str | None) -> str:
    if geno_bin:
        p = Path(geno_bin)
        if p.exists():
            return str(p.resolve())
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


def snippet(text: str, limit: int = 600) -> str:
    """Collapse whitespace and return a readable error snippet."""
    if not text:
        return ""
    lines = [ln.rstrip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return ""
    tail = "\n".join(lines[-12:])
    tail = re.sub(r"[ \t]+", " ", tail)
    if len(tail) > limit:
        return "…" + tail[-(limit - 1) :]
    return tail


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
        out = e.stdout or ""
        err = e.stderr or ""
        if isinstance(out, bytes):
            out = out.decode(errors="replace")
        if isinstance(err, bytes):
            err = err.decode(errors="replace")
        return 124, (str(out) + str(err) + "\nTIMEOUT after 120s").strip(), time.perf_counter() - t0


def run_app(geno: str, app: dict, do_compile: bool) -> dict:
    path = ROOT / app["path"]
    main = path / "Main.geno"
    toml = path / "geno.toml"

    base = {
        "id": app["id"],
        "tier": app["tier"],
        "ok": False,
        "seconds": 0.0,
        "error": "",
        "test_ok": False,
        "run_ok": False,
        "compile_ok": None,
    }

    if not path.is_dir():
        base["error"] = f"missing path {app['path']}"
        return base

    if toml.exists():
        test_target = [geno, "test", "."]
        test_cwd = path
    elif main.exists():
        test_target = [geno, "test", str(main)]
        test_cwd = path
    else:
        base["error"] = "no Main.geno or geno.toml"
        return base

    test_rc, test_out, test_s = run_cmd(test_target, test_cwd)
    test_ok = test_rc == 0

    if main.exists():
        run_target = [geno, "run", str(main.name)]
        run_cwd = path
    else:
        run_target = [geno, "run", "."]
        run_cwd = path

    run_rc, run_out, run_s = run_cmd(run_target, run_cwd)
    run_ok = run_rc == 0

    compile_ok = None
    compile_s = 0.0
    compile_out = ""
    compile_rc = 0
    if do_compile:
        # geno compile -o expects an output *file* (python target by default)
        fd, out_path = tempfile.mkstemp(prefix=f"geno-compile-{app['id']}-", suffix=".py")
        os.close(fd)
        out_file = Path(out_path)
        try:
            if toml.exists():
                compile_target = [geno, "compile", "-o", str(out_file), "--target", "python", "."]
            elif main.exists():
                compile_target = [geno, "compile", "-o", str(out_file), "--target", "python", str(main.name)]
            else:
                compile_target = [geno, "compile", "-o", str(out_file), "--target", "python", "."]
            compile_rc, compile_out, compile_s = run_cmd(compile_target, path)
            compile_ok = compile_rc == 0
        finally:
            out_file.unlink(missing_ok=True)

    ok = test_ok and run_ok and (compile_ok is not False)
    errors: list[str] = []
    if not test_ok:
        errors.append(f"test failed (rc={test_rc}):\n{snippet(test_out)}")
    if not run_ok:
        errors.append(f"run failed (rc={run_rc}):\n{snippet(run_out)}")
    if compile_ok is False:
        errors.append(f"compile failed (rc={compile_rc}):\n{snippet(compile_out)}")

    return {
        "id": app["id"],
        "tier": app["tier"],
        "ok": ok,
        "seconds": round(test_s + run_s + compile_s, 3),
        "error": "\n---\n".join(errors),
        "test_ok": test_ok,
        "run_ok": run_ok,
        "compile_ok": compile_ok,
    }


def write_results(
    results: list[dict],
    tier: str,
    geno: str,
    geno_ver: str,
    json_out: Path,
) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    pin = load_json(PIN)
    payload = {
        "tier": tier,
        "geno": geno,
        "geno_version": geno_ver,
        "pin": pin,
        "passed": sum(1 for r in results if r["ok"]),
        "failed": sum(1 for r in results if not r["ok"]),
        "total": len(results),
        "apps": results,
    }
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, indent=2) + "\n")

    latest = RESULTS_DIR / "latest.json"
    if json_out.resolve() != latest.resolve():
        latest.write_text(json.dumps(payload, indent=2) + "\n")

    template = SUMMARY_TEMPLATE.read_text() if SUMMARY_TEMPLATE.exists() else (
        "# Corpus results\n\n"
        "Tier: {tier} | geno: {geno} | pin: {pin}\n\n"
        "Passed: {passed} / {total} (failed: {failed})\n\n"
        "{table}\n"
    )
    rows = ["| App | Tier | Status | Seconds | Error |", "|---|---|---|---|---|"]
    for r in results:
        status = "PASS" if r["ok"] else "FAIL"
        err = (r.get("error") or "").replace("|", "\\|").replace("\n", " ")[:160]
        rows.append(f"| {r['id']} | {r['tier']} | {status} | {r['seconds']} | {err} |")
    summary = template.format(
        tier=tier,
        geno=f"{geno_ver} ({geno})",
        pin=pin.get("pip", ""),
        passed=payload["passed"],
        failed=payload["failed"],
        total=payload["total"],
        table="\n".join(rows),
    )
    (RESULTS_DIR / "summary.md").write_text(summary)
    return json_out


def print_table(results: list[dict], show_compile: bool) -> None:
    print()
    if show_compile:
        hdr = f"{'APP':<28} {'TIER':<10} {'TEST':<6} {'RUN':<6} {'CMPL':<6} {'SEC':>7}  STATUS"
        width = 80
    else:
        hdr = f"{'APP':<28} {'TIER':<10} {'TEST':<6} {'RUN':<6} {'SEC':>7}  STATUS"
        width = 72
    print(hdr)
    print("-" * width)
    for r in results:
        if show_compile:
            c = r.get("compile_ok")
            cmpl = "ok" if c else ("FAIL" if c is False else "-")
            print(
                f"{r['id']:<28} {r['tier']:<10} "
                f"{'ok' if r['test_ok'] else 'FAIL':<6} "
                f"{'ok' if r['run_ok'] else 'FAIL':<6} "
                f"{cmpl:<6} "
                f"{r['seconds']:>7.3f}  "
                f"{'PASS' if r['ok'] else 'FAIL'}"
            )
        else:
            print(
                f"{r['id']:<28} {r['tier']:<10} "
                f"{'ok' if r['test_ok'] else 'FAIL':<6} "
                f"{'ok' if r['run_ok'] else 'FAIL':<6} "
                f"{r['seconds']:>7.3f}  "
                f"{'PASS' if r['ok'] else 'FAIL'}"
            )
        if not r["ok"] and r.get("error"):
            for line in snippet(r["error"], limit=400).splitlines():
                print(f"    {line}")
    passed = sum(1 for r in results if r["ok"])
    print("-" * width)
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
    ap.add_argument(
        "--json-out",
        default=str(RESULTS_DIR / "latest.json"),
        help="Write JSON results here (default: results/latest.json)",
    )
    ap.add_argument(
        "--compile",
        action="store_true",
        help="Also run `geno compile -o /tmp/...` (useful for reference tier)",
    )
    args = ap.parse_args()

    geno = resolve_geno(args.geno_bin)
    ver = geno_version(geno)
    apps = select_apps(args.tier)
    print(f"geno={geno}")
    print(f"geno_version={ver}")
    print(f"tier={args.tier} apps={len(apps)} compile={args.compile}")

    results: list[dict] = []
    for app in apps:
        print(f"→ {app['id']} ({app['tier']}) ...", flush=True)
        r = run_app(geno, app, do_compile=args.compile)
        results.append(r)
        status = "PASS" if r["ok"] else "FAIL"
        print(f"  {status} in {r['seconds']:.3f}s", flush=True)
        if not r["ok"] and args.fail_fast:
            break

    print_table(results, show_compile=args.compile)
    out = write_results(results, args.tier, geno, ver, Path(args.json_out))
    print(f"Wrote {out}")

    if any(not r["ok"] for r in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
