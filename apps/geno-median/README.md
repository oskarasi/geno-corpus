# geno-median

Median of a list of integers (integer average for even length) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1 3 2 8 5
geno run --unsafe --cap env,print Main.geno -- 1 2 3 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `sort_ints(xs: List[Int]) -> List[Int]`
- `median(xs: List[Int]) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<ints...>``
- `main() -> String — demo via `run``
