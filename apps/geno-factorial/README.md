# geno-factorial

Factorial for non-negative integers (CLI capped at **20**) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 5
geno run --unsafe --cap env,print Main.geno -- 10
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `factorial(n: Int) -> Int — requires n >= 0`
- `run(args: List[String]) -> Result[String, String] — `<n>``
- `main() -> String — demo via `run``
