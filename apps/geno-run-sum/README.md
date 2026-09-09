# geno-run-sum

Running (prefix) sums of integer lists in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- sum 1 2 3 4
geno run --unsafe --cap env,print Main.geno -- 10 20 30
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `run_sum(xs: List[Int]) -> List[Int]`
- `ints_csv(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String] — `sum <ints...>` | `<ints...>``
- `main() -> String — demo via `run``
