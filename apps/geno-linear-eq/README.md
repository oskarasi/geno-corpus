# geno-linear-eq

Solve ax + b = 0 for x in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 2 -4
geno run --unsafe --cap env,print Main.geno -- 5 10
geno run --unsafe --cap env,print Main.geno -- 0 3
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `solve(a: Float, b: Float) -> Result[Float, String]`
- `describe(a: Float, b: Float) -> String`
- `run(args: List[String]) -> Result[String, String] — `<a> <b>``
- `main() -> String — demo via `run``
