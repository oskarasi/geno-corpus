# geno-binary-search

Binary search on sorted integer lists in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 1 3 5 7 9 -- 5
geno run --unsafe --cap env,print Main.geno -- 1 3 5 7 9 -- 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `binary_search(xs, target) -> Int — index or -1`
- `run(args: List[String]) -> Result[String, String] — `<sorted ints...> -- <target>``
- `main() -> String — demo via `run``
