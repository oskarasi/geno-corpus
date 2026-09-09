# geno-triangle

Triangle area via Heron's formula in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- area 3 4 5
geno run --unsafe --cap env,print Main.geno -- area 5 5 6
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `heron_area(a: Float, b: Float, c: Float) -> Result[Float, String]`
- `run(args: List[String]) -> Result[String, String] — `area <a> <b> <c>``
- `main() -> String — demo via `run``
