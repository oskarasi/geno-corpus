# geno-histogram

Frequency histogram helpers for integer lists in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1 2 2 3 1 1
geno run --unsafe --cap env,print Main.geno -- 5 5 5
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `count_of(xs: List[Int], target: Int) -> Int`
- `unique_values(xs: List[Int]) -> List[Int]`
- `frequencies(xs: List[Int]) -> List[Int]`
- `describe(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String] — `<ints...>``
- `main() -> String — demo via `run``
