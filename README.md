# geno-corpus

**Conformance corpus:** pin a [geno-lang](https://github.com/davidiach/geno-lang) version and fail CI if listed agent-written Geno apps regress (`geno test` + default `geno run`).

This is the external, agent-written companion to geno-lang’s in-tree `examples/apps/` release gate. It does **not** replace in-tree examples — it extends the release story with programs living under [oskarasi](https://github.com/oskarasi)’s `geno-*` apps.

## Tiers

| Tier | Meaning |
|------|---------|
| **flagship** | Must-pass core mini-apps (tip, roman, cipher, …) |
| **reference** | Larger multi-module reference (`geno-ref-ledger`) |
| **corpus** | Remaining vendored `geno-*` mini-apps |

See `manifest.json` for the authoritative app list and `pin.json` for the pinned `geno-lang` version.

## Quick start (local)

```bash
# Prefer an existing geno, or let the harness bootstrap from pin.json
python harness/run_corpus.py --tier flagship
python harness/run_corpus.py --tier reference
python harness/run_corpus.py --tier corpus
python harness/run_corpus.py --tier all

# Explicit binary (e.g. workspace venv)
python harness/run_corpus.py --tier flagship --geno-bin /workspace/geno-venv/bin/geno

# Stop on first failure
python harness/run_corpus.py --tier flagship --fail-fast
```

Results land in `results/latest.json` and `results/summary.md`.

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
apps/                  # VENDORED snapshots (not submodules), each with SOURCE.json
.github/workflows/conformance.yml
```

Apps are **vendored** copies (not git submodules). Each app directory includes `SOURCE.json` pointing at the upstream repo (typically `https://github.com/oskarasi/<app>`).

## CI

GitHub Actions runs the corpus weekly and on every push/PR, matrixed by tier (`flagship`, `reference`, `corpus`). Each job installs the pin and runs:

```bash
.venv/bin/python harness/run_corpus.py --tier <tier> --geno-bin .venv/bin/geno
```

## Related

- [davidiach/geno-lang](https://github.com/davidiach/geno-lang) — language + in-tree `examples/apps/`
- [oskarasi geno-* apps](https://github.com/oskarasi?tab=repositories&q=geno-) — agent-written programs vendored here

## License

Apache-2.0
