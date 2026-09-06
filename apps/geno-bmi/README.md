# geno-bmi

BMI calculator in [Geno](https://github.com/davidiach/geno-lang). Height must be **> 0**. Categories follow common WHO-style cutoffs.

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
geno run --unsafe --cap env,print Main.geno -- 70 1.75
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `bmi(weight_kg, height_m) -> Float` — `weight / height^2` (`requires height_m > 0`)
- `safe_bmi(weight_kg, height_m) -> Result[Float, String]` — `Err` when height ≤ 0
- `category(bmi_value) -> String` — `underweight` (<18.5), `normal` (<25), `overweight` (<30), `obese` (≥30)
- `run(args: List[String]) -> Result[String, String]` — `<weight_kg> <height_m>`
- `main() -> String` — demo via `run`
