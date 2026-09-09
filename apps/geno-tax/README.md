# geno-tax

Sales tax in cents (`tax` / `total`) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- tax 10000 8
geno run --unsafe --cap env,print Main.geno -- total 10000 8
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `tax_cents(price_cents: Int, tax_percent: Int) -> Result[Int, String]`
- `price_with_tax_cents(price_cents: Int, tax_percent: Int) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `tax|total <cents> <percent>``
- `main() -> String — demo via `run``
