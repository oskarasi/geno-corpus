# geno-range-stats

Min, max, and span for a list of integers in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 3 1 4 1 5
geno run --unsafe --cap env,print Main.geno -- -2 -5 0
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `min_int(xs: List[Int]) -> Result[Int, String]`
- `max_int(xs: List[Int]) -> Result[Int, String]`
- `span(xs: List[Int]) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<ints...>``
- `main() -> String — demo via `run``
