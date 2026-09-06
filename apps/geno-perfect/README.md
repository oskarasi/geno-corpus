# geno-perfect

Perfect-number checker (CLI capped at **1_000_000**) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- check 6
geno run --unsafe --cap env,print Main.geno -- check 28
geno run --unsafe --cap env,print Main.geno -- check 12
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `divisor_sum(n: Int) -> Int — sum of proper divisors`
- `is_perfect(n: Int) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `check <n>``
- `main() -> String — demo via `run``
