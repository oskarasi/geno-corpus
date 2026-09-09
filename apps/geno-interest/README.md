# geno-interest

Simple interest in cents (principal * rate * time / 100) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 10000 5 2
geno run --unsafe --cap env,print Main.geno -- 5000 10 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `simple_interest_cents(principal_cents: Int, rate_percent: Int, time: Int) -> Int`
- `amount_cents(principal_cents: Int, rate_percent: Int, time: Int) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<principal_cents> <rate_percent> <time>``
- `main() -> String — demo via `run``
