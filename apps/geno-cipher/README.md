# geno-cipher

Caesar cipher encrypt/decrypt in [Geno](https://github.com/davidiach/geno-lang). Preserves case; non-letters are left unchanged.

## Install

```bash
pip install geno-lang
```

## Test / run (sandboxed, no capabilities)

```bash
geno test Main.geno
geno run Main.geno
```

Default `main()` demos encrypt→decrypt of `"Hello, Geno!"` with shift 7.

## API

- `normalize_mod(n: Int) -> Int` — shift folded into `0..25`
- `shift_char(ch: String, shift: Int) -> String`
- `encrypt(text: String, shift: Int) -> String`
- `decrypt(text: String, shift: Int) -> String`
- `roundtrip_ok(text: String, shift: Int) -> Bool` — requires `shift >= 0`
- `run(args: List[String]) -> Result[String, String]` — argv-style, no capabilities:
  - `encrypt <shift> <text...>`
  - `decrypt <shift> <text...>`
  - aliases: `enc`, `dec`

## Optional real CLI

Default sandboxed `geno run` **rejects** `--cap` unless you also pass `--unsafe` or `--json`.

```bash
geno run --unsafe --cap env,print Main.geno -- encrypt 3 Hello
geno run --unsafe --cap env,print Main.geno -- decrypt 3 Khoor
```

`cli_main` uses `cli_args()` / `print` and is `@untested`; default `geno run` still executes capability-free `main`.
