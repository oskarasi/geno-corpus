# geno-anagram

Anagram checker. Normalizes letters (lowercase, strip spaces) and compares sorted character signatures in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- listen | silent
geno run --unsafe --cap env,print Main.geno -- hello | world
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `normalize(text) -> String — lowercase and strip spaces`
- `sorted_chars(text) -> String — characters sorted into a signature string`
- `letter_signature(text) -> String — normalize then sort`
- `is_anagram(a, b) -> Bool — true when signatures match`
- `run(args: List[String]) -> Result[String, String] — `<words...> | <words...>``
- `main() -> String — demo via `run``
