# geno-leap

Gregorian leap-year checker in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 2000
geno run --unsafe --cap env,print Main.geno -- 1900
geno run --unsafe --cap env,print Main.geno -- 2024
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_leap_year(year: Int) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `<year>``
- `main() -> String — demo via `run``
