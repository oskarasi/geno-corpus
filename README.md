# geno-corpus

[![conformance](https://img.shields.io/badge/conformance-pending-lightgrey)](./ci/conformance.yml)
[![geno-lang](https://img.shields.io/badge/geno--lang-0.4.3-blue)](https://github.com/davidiach/geno-lang)
[![license](https://img.shields.io/badge/license-Apache--2.0-green)](./LICENSE)

**Conformance corpus:** pin a [geno-lang](https://github.com/davidiach/geno-lang) version and fail CI if listed agent-written Geno apps regress (`geno test` + default `geno run`).

This is the external, agent-written companion to geno-lang’s in-tree `examples/apps/` release gate. It does **not** replace in-tree examples — it extends the release story with programs living under [oskarasi](https://github.com/oskarasi)’s `geno-*` apps.

## Tiers

| Tier | Meaning | CI matrix |
|------|---------|-----------|
| **flagship** | Must-pass core mini-apps (tip, roman, cipher, …) | `matrix.tier: flagship` |
| **reference** | Larger multi-module reference (`geno-ref-ledger`) | `matrix.tier: reference` |
| **corpus** | Remaining vendored `geno-*` mini-apps (~90) | `matrix.tier: corpus` |
| **all** | Every app in `manifest.json` (local default) | not a CI job — use locally |

See `manifest.json` for the authoritative app list and `pin.json` for the pinned `geno-lang` version.

CI runs one job per tier (`flagship`, `reference`, `corpus`) with `fail-fast: false`, so a corpus failure does not cancel flagship.

## Quick start (local)

```bash
# Prefer an existing geno, or let the harness bootstrap from pin.json
python harness/run_corpus.py --tier flagship
python harness/run_corpus.py --tier reference
python harness/run_corpus.py --tier corpus
python harness/run_corpus.py --tier all          # default

# Explicit binary (e.g. workspace venv)
python harness/run_corpus.py --tier flagship --geno-bin /workspace/geno-venv/bin/geno

# Also compile (python target) — useful for reference tier
python harness/run_corpus.py --tier reference --compile

# Custom JSON output (still mirrors to results/latest.json)
python harness/run_corpus.py --tier all --json-out results/latest.json

# Stop on first failure
python harness/run_corpus.py --tier flagship --fail-fast
```

The harness prints the `geno` binary path and `geno --version` string, writes
`results/latest.json` + `results/summary.md`, and prints clearer trailing error snippets on failure.

## Syncing vendors

Apps under `apps/` are **vendored snapshots** from `https://github.com/oskarasi/<id>` (not submodules).
Each directory includes `SOURCE.json`:

```json
{
  "repo": "https://github.com/oskarasi/geno-bmi",
  "commit": "<main SHA>",
  "vendored_at": "2026-09-06T17:00:00Z"
}
```

To refresh every app from GitHub remotes (main tip):

```bash
python harness/sync_vendors.py
# or a subset:
python harness/sync_vendors.py geno-roman geno-ref-ledger
```

The sync script resolves each repo’s main SHA via `gh api`, downloads that commit’s tarball, and copies `Main.geno` / `geno.toml` / `*.geno` / `README*` / `LICENSE*` into `apps/<id>/`. Multi-file apps (`geno-roman`, `geno-ref-ledger`) must include every module listed in `geno.toml`.

Requires [GitHub CLI](https://cli.github.com/) (`gh`) authenticated for the `oskarasi` org/user.

## Pin policy

`pin.json` locks the corpus to a specific PyPI release, e.g.:

```json
{
  "geno_lang": "0.4.3",
  "pip": "geno-lang==0.4.3",
  "note": "Bump this pin when validating a new geno-lang release against the corpus."
}
```

When validating a new geno-lang release:

1. Bump `pin.json` to the candidate version.
2. Run the harness locally (at least `--tier flagship` and `--tier reference`).
3. Fix or quarantine failing apps, then merge the pin bump so CI enforces the new floor.

## Layout

```
manifest.json          # tiers + app list
pin.json               # pinned geno-lang
harness/run_corpus.py  # install pin (if needed), run apps, exit non-zero on failure
harness/sync_vendors.py# re-vendor apps/<id> from GitHub remotes
apps/                  # VENDORED snapshots (not submodules), each with SOURCE.json
ci/conformance.yml     # workflow copy (no workflow-scope permission needed to commit)
docs/conformance.yml.example
workflows/conformance.yml.example
.github/workflows/conformance.yml  # live Actions workflow (needs `workflows` scope to push)
```

## CI / workflow scope

GitHub Actions runs the corpus weekly and on every push/PR, matrixed by tier (`flagship`, `reference`, `corpus`). Each job installs the pin and runs:

```bash
.venv/bin/python harness/run_corpus.py --tier <tier> --geno-bin .venv/bin/geno
```

**Note:** pushing `.github/workflows/*` requires a token with the `workflow` scope.
If a push is rejected for workflow scope, keep the live workflow local/untracked and use the copies under `ci/conformance.yml` or `docs/conformance.yml.example` / `workflows/conformance.yml.example` — maintainers with workflow scope can install them into `.github/workflows/`.


## Changelog

- **2026-09-06** — Vendors refreshed from GitHub `main` (SOURCE.json SHAs) after the flagship-bar batch-2 upgrades (fizzbuzz, palindrome, factorial, fib, gcd, collatz, binary, hex, leap, rot13, atbash, ordinal, perfect, happy, stack), plus flagships and `geno-ref-ledger`. Harness green on geno-lang 0.4.3: flagship 10/10, reference 1/1, corpus 90/90.

## Related

- [davidiach/geno-lang](https://github.com/davidiach/geno-lang) — language + in-tree `examples/apps/`
- [oskarasi geno-* apps](https://github.com/oskarasi?tab=repositories&q=geno-) — agent-written programs vendored here

## License

Apache-2.0
