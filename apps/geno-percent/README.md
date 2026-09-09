# geno-percent

Percentage helpers (`of` / `what`) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- of 25 200
geno run --unsafe --cap env,print Main.geno -- what 50 200
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `percent_of(percent: Float, whole: Float) -> Float`
- `what_percent(part: Float, whole: Float) -> Result[Float, String]`
- `run(args: List[String]) -> Result[String, String] — `of <p> <whole>` | `what <part> <whole>``
- `main() -> String — demo via `run``
