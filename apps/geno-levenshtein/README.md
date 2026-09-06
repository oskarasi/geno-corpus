# geno-levenshtein

Levenshtein edit distance for **short strings** in [Geno](https://github.com/davidiach/geno-lang). Uses prelude `set_at` for DP row updates; helpers with ≥3 parameters use named arguments.

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
geno run --unsafe --cap env,print Main.geno -- kitten sitting
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `min3(a, b, c) -> Int` — call with named args
- `iota0(n) -> List[Int]` / `filled(count, value) -> List[Int]`
- `levenshtein(a, b) -> Int`
- `run(args: List[String]) -> Result[String, String]` — `<string_a> <string_b>`
- `main() -> String` — demo via `run`
