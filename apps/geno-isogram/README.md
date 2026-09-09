# geno-isogram

Isogram check (no repeating letters; case-insensitive; non-letters ignored) in [Geno](https://github.com/davidiach/geno-lang).

## Install

```bash
pip install geno-lang
```

## Test

```bash
geno test Main.geno
```

## Run

Default sandbox demo (capability-free `main()`):

```bash
geno run Main.geno
```

Optional real CLI (needs `--unsafe` because default sandbox does not allow `--cap` without `--unsafe`/`--json`):

```bash
geno run --unsafe --cap env,print Main.geno -- isogram
geno run --unsafe --cap env,print Main.geno -- Alphabet
geno run --unsafe --cap env,print Main.geno -- thumbscrew-japingly
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_letter(c: String) -> Bool`
- `is_isogram(text: String) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
