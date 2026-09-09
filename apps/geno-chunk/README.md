# geno-chunk

Split a list into chunks of size n (invalid n yields empty). CLI prints chunks as `a,b|c,d|e` in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 2 1 2 3 4 5
geno run --unsafe --cap env,print Main.geno -- 3 1 2 3
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `chunk_list(xs, n) -> List[List[Int]]`
- `run(args: List[String]) -> Result[String, String] — `<n> <ints...>``
- `main() -> String — demo via `run``
