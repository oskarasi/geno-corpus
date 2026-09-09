# geno-unique

Order-preserving dedupe for integer lists in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- unique 1 2 2 3 1
geno run --unsafe --cap env,print Main.geno -- 4 1 4 2 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `contains_int(xs: List[Int], x: Int) -> Bool`
- `unique(xs: List[Int]) -> List[Int]`
- `run(args: List[String]) -> Result[String, String] — `unique <ints...>` | `<ints...>``
- `main() -> String — demo via `run``
