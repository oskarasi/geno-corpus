# geno-diff-list

Adjacent differences of an integer list in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 1 3 6 10
geno run --unsafe --cap env,print Main.geno -- 10 7 7 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `diff_list(xs) -> List[Int]`
- `run(args: List[String]) -> Result[String, String] — `<ints...>``
- `main() -> String — demo via `run``
