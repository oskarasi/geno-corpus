# geno-intersect

Set intersection of two integer lists (order from first, deduped) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1 2 3 2 -- 2 4 1
geno run --unsafe --cap env,print Main.geno -- 5 5 6 -- 5
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `contains_int(xs: List[Int], x: Int) -> Bool`
- `intersect(a: List[Int], b: List[Int]) -> List[Int]`
- `run(args: List[String]) -> Result[String, String] — `<ints...> -- <ints...>``
- `main() -> String — demo via `run``
