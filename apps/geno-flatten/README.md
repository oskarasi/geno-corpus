# geno-flatten

Flatten nested integer lists (row-major) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1,2 3 4,5
geno run --unsafe --cap env,print Main.geno -- 7,8,9
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `flatten_ints(xss: List[List[Int]]) -> List[Int]`
- `parse_row(text: String) -> Result[List[Int], String]`
- `run(args: List[String]) -> Result[String, String] — `<row...>` (comma-separated ints per arg)`
- `main() -> String — demo via `run``
