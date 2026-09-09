# geno-pluralize

Simple English pluralization in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- cat box fly day
geno run --unsafe --cap env,print Main.geno -- leaf knife
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `ends_with(s: String, suffix: String) -> Bool`
- `pluralize(word: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<word...>``
- `main() -> String — demo via `run``
