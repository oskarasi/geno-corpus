# geno-acronym

Acronym builder in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- Portable Network Graphics
geno run --unsafe --cap env,print Main.geno -- as soon as possible
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `acronym(text: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<words...>``
- `main() -> String — demo via `run``
