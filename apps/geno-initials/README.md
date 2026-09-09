# geno-initials

Extract uppercase initials from a personal name in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- Ada Lovelace
geno run --unsafe --cap env,print Main.geno -- john quincy adams
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_letter(c: String) -> Bool`
- `initials(name: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<name...>``
- `main() -> String — demo via `run``
