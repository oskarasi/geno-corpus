# geno-mortgage

Standard amortizing mortgage monthly payment (rate 0 uses principal / (years*12)) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 200000 6 30
geno run --unsafe --cap env,print Main.geno -- 120000 0 10
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `pow_float(base: Float, exp: Int) -> Float`
- `monthly_payment(principal: Float, annual_rate_percent: Float, years: Int) -> Float`
- `run(args: List[String]) -> Result[String, String] — `<principal> <annual_rate_percent> <years>``
- `main() -> String — demo via `run``
