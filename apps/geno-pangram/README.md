# geno-pangram

Pangram checker (every letter a-z at least once) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- The quick brown fox jumps over the lazy dog
geno run --unsafe --cap env,print Main.geno -- Hello World
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_letter(c: String) -> Bool`
- `is_pangram(text: String) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
