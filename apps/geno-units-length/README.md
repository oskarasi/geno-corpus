# geno-units-length

Length conversion (meters ↔ feet; 1 m = 3.28084 ft) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- m2ft 1
geno run --unsafe --cap env,print Main.geno -- ft2m 3.28084
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `meters_to_feet(meters: Float) -> Float`
- `feet_to_meters(feet: Float) -> Float`
- `run(args: List[String]) -> Result[String, String] — `m2ft|ft2m <value>``
- `main() -> String — demo via `run``
