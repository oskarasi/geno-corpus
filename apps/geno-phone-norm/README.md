# geno-phone-norm

Phone number normalizer (digits only) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- (555) 123-4567
geno run --unsafe --cap env,print Main.geno -- +1-555-000-1111
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_digit(c: String) -> Bool`
- `normalize(phone: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<phone...>``
- `main() -> String — demo via `run``
