# geno-rle

Run-length encoding (RLE) for simple alphanumeric strings, written in [Geno](https://github.com/davidiach/geno-lang).

## Encoding scheme

Each run of identical characters becomes `<char><count>`:

| Input | Encoded |
|-------|---------|
| `aaabbc` | `a3b2c1` |
| `abc` | `a1b1c1` |
| long W/B runs | `W12B1W12B3` |
| `` (empty) | `` |

- Encode accepts any characters (including non-alnum).
- Decode requires alphanumeric characters and counts ≥ 1; returns `Result[String, String]`.

## Install

```bash
pip install geno-lang
```

## Test / run (sandboxed, no capabilities)

```bash
geno test .
geno run .
```

Default `main()` returns a String summary of a few `describe(...)` demos.

## API

- `encode(s: String) -> String`
- `decode(s: String) -> Result[String, String]`
- `round_trip(s: String) -> String`
- `describe(s: String) -> String`
- `run(args: List[String]) -> Result[String, String]` — `encode|decode <text>` (aliases `enc`/`dec`)

## Optional real CLI

Default sandboxed `geno run` **rejects** `--cap` unless you also pass `--unsafe` or `--json`.

```bash
geno run --unsafe --cap env,print Main.geno -- encode aaabbc
geno run --unsafe --cap env,print Main.geno -- decode a3b2c1
```

`cli_main` is `@untested` and uses `cli_args()` / `print`; default `geno run` stays on capability-free `main`.
