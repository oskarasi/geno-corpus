# geno-currency

Format integer cents as a dollar string with two decimals in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 1234
geno run --unsafe --cap env,print Main.geno -- -50
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `pad2(n) -> String`
- `format_cents(cents) -> String`
- `run(args: List[String]) -> Result[String, String] — `<cents>``
- `main() -> String — demo via `run``
