# geno-luhn

Luhn checksum validator in [Geno](https://github.com/davidiach/geno-lang).

## Install

```bash
pip install geno-lang
```

## Test / run (sandboxed, no capabilities)

```bash
geno test Main.geno
geno run Main.geno
```

Default `main()` demos a few known-good / known-bad numbers as a String summary.

## API

- `is_all_digits(s: String) -> Bool`
- `normalize_digits(s: String) -> String` — strip spaces/hyphens
- `luhn_valid(digits: String) -> Bool`
- `check(raw: String) -> Result[String, String]` — normalize then validate
- `run(args: List[String]) -> Result[String, String]` — `check <digits>` or bare `<digits>`

## Optional real CLI

Default sandboxed `geno run` **rejects** `--cap` unless you also pass `--unsafe` or `--json`.

```bash
geno run --unsafe --cap env,print Main.geno -- check 79927398713
geno run --unsafe --cap env,print Main.geno -- 4532015112830366
```

`cli_main` is `@untested` (`cli_args`/`print`); default `geno run` uses capability-free `main`.
