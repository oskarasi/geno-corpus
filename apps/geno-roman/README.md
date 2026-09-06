# geno-roman

Roman numeral converter (integers **1..3999**) in [Geno](https://github.com/davidiach/geno-lang).

## Install

```bash
pip install geno-lang
```

## Test / run (sandboxed, no capabilities)

```bash
geno test .
geno run .
```

Default `main()` demos several round-trips and prints a String summary — no `--cap` needed.

## API

Library (`Lib.geno`):

- `to_roman(n: Int) -> Result[String, String]` — `1..3999` or Err
- `from_roman(s: String) -> Result[Int, String]` — case-insensitive; empty/invalid → Err
- `roman_roundtrip(n: Int) -> Bool` — requires `1 <= n <= 3999`
- `roman_value(ch: String) -> Int` — single-character value (0 if unknown)

Driver (`Main.geno`):

- `run(args: List[String]) -> Result[String, String]` — argv-style, no capabilities:
  - `to <n>` → Roman string
  - `from <roman>` → decimal string

## Optional real CLI

Default sandboxed `geno run` **rejects** `--cap` unless you also pass `--unsafe` or `--json`.

```bash
geno run --unsafe --cap env,print Main.geno -- to 1994
geno run --unsafe --cap env,print Main.geno -- from MCMXCIV
```

`cli_main` calls `cli_args()` / `print` and is marked `@untested` so default `geno run` / CI stay capability-free (they execute `main`, not `cli_main`).

## Layout

- `Lib.geno` — conversion core
- `Main.geno` — `run`, demo `main`, optional `cli_main`
- `geno.toml` — `files = ["Lib", "Main"]`
