# geno-units-weight

Weight conversion (kg ↔ lb; 1 kg = 2.20462 lb) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- kg2lb 1
geno run --unsafe --cap env,print Main.geno -- lb2kg 2.20462
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `kg_to_lb(kg: Float) -> Float`
- `lb_to_kg(lb: Float) -> Float`
- `run(args: List[String]) -> Result[String, String] — `kg2lb|lb2kg <value>``
- `main() -> String — demo via `run``
