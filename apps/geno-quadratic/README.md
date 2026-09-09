# geno-quadratic

Real quadratic equation solver in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1 -5 6
geno run --unsafe --cap env,print Main.geno -- 1 0 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `discriminant(a: Float, b: Float, c: Float) -> Float`
- `solve(a: Float, b: Float, c: Float) -> Result[List[Float], String]`
- `floats_csv(xs: List[Float]) -> String`
- `describe(a: Float, b: Float, c: Float) -> String`
- `run(args: List[String]) -> Result[String, String] — `<a> <b> <c>``
- `main() -> String — demo via `run``
