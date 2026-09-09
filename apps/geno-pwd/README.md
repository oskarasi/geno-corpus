# geno-pwd

Password strength meter (score 0–5) in [Geno](https://github.com/davidiach/geno-lang).

## Scoring

| Criterion | Points |
|-----------|--------|
| Has lowercase letter | +1 |
| Has uppercase letter | +1 |
| Has digit | +1 |
| Has symbol (non-alphanumeric) | +1 |
| Length ≥ 8 | +1 |

Labels: 0–1 weak, 2 fair, 3 good, 4–5 strong.

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
geno run --unsafe --cap env,print Main.geno -- abc
geno run --unsafe --cap env,print Main.geno -- Password1!
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `score(password: String) -> Int`
- `label(s: Int) -> String — requires 0..5`
- `summarize(password: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<password...>``
- `main() -> String — demo via `run``
