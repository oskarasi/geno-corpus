# geno-palindrome

Palindrome checker (ignores case and spaces) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- check Race Car
geno run --unsafe --cap env,print Main.geno -- check hello
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `normalize(text: String) -> String`
- `is_palindrome(text: String) -> Bool`
- `run(args: List[String]) -> Result[String, String]` — `check <text...>`
- `main() -> String` — demo via `run`
