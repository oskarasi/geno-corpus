# geno-credit-mask

Mask a credit-card number, keeping the last 4 digits in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 4111-1111-1111-1111
geno run --unsafe --cap env,print Main.geno -- 4111111111111111
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `digits_only(s) -> String`
- `mask(card) -> String`
- `run(args: List[String]) -> Result[String, String] — `<card...>``
- `main() -> String — demo via `run``
