# geno-clock-angle

Smaller angle between hour and minute hands. Hour **0..23**, minute **0..59** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 3 0
geno run --unsafe --cap env,print Main.geno -- 2 20
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `clock_angle(hour, minute) -> Result[Float, String]`
- `run(args: List[String]) -> Result[String, String] — `<hour> <minute>``
- `main() -> String — demo via `run``
