# geno-sort-ints

Insertion sort for integer lists in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- sort 5 1 4 2 3
geno run --unsafe --cap env,print Main.geno -- 3 1 2
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `insert_sorted(sorted: List[Int], x: Int) -> List[Int]`
- `sort_ints(xs: List[Int]) -> List[Int]`
- `run(args: List[String]) -> Result[String, String] — `sort <ints...>` | `<ints...>``
- `main() -> String — demo via `run``
