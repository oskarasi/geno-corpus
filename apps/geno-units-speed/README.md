# geno-units-speed

Speed conversion (mph ↔ km/h; 1 mi = 1.60934 km) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- mph2kmh 60
geno run --unsafe --cap env,print Main.geno -- kmh2mph 96.5604
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `mph_to_kmh(mph: Float) -> Float`
- `kmh_to_mph(kmh: Float) -> Float`
- `run(args: List[String]) -> Result[String, String] — `mph2kmh|kmh2mph <value>``
- `main() -> String — demo via `run``
