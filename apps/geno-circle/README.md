# geno-circle

Circle area and circumference. Radius must be **non-negative** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 2
geno run --unsafe --cap env,print Main.geno -- 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `area(radius) -> Float — `requires radius >= 0``
- `circumference(radius) -> Float — `requires radius >= 0``
- `safe_area(radius) -> Result[Float, String]`
- `safe_circumference(radius) -> Result[Float, String]`
- `run(args: List[String]) -> Result[String, String] — `<radius>``
- `main() -> String — demo via `run``
