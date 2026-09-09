# geno-csv-row

Simple CSV row join/split (no quoting) in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- join a b c
geno run --unsafe --cap env,print Main.geno -- split a,b,c
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `join_row(fields) -> String`
- `split_row(row) -> List[String]`
- `run(args: List[String]) -> Result[String, String] — `join <fields...>` | `split <row>``
- `main() -> String — demo via `run``
