# geno-discount

Percent discount in cents. Price **non-negative**, percent **0..100** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 10000 25
geno run --unsafe --cap env,print Main.geno -- 10000 20
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `discount_amount_cents(price_cents, percent_off) -> Result[Int, String]`
- `price_after_discount_cents(price_cents, percent_off) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<price_cents> <percent_off>``
- `main() -> String — demo via `run``
