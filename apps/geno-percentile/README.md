# geno-percentile

Nearest-rank percentile over a list of integers in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 50 1 2 3 4 5
geno run --unsafe --cap env,print Main.geno -- 100 1 2 3 4 5
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `sort_ints(xs: List[Int]) -> List[Int]`
- `percentile(xs: List[Int], p: Int) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<p> <ints...>``
- `main() -> String — demo via `run``
