# geno-vowels

Vowel counter (a/e/i/o/u; y excluded) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- hello
geno run --unsafe --cap env,print Main.geno -- Beautiful
geno run --unsafe --cap env,print Main.geno -- rhythm
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_vowel(c: String) -> Bool`
- `count_vowels(text: String) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
