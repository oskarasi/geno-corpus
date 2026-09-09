# geno-dot

Dot product of two equal-length integer vectors in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 1 2 3 -- 4 5 6
geno run --unsafe --cap env,print Main.geno -- 1 0 -- 0 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `dot(a, b) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<ints_a...> -- <ints_b...>``
- `main() -> String — demo via `run``
