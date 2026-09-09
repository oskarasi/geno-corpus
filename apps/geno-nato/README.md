# geno-nato

NATO phonetic alphabet encoder in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- Geno
geno run --unsafe --cap env,print Main.geno -- NATO
geno run --unsafe --cap env,print Main.geno -- Hi
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `nato_word(c: String) -> String`
- `encode(s: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
