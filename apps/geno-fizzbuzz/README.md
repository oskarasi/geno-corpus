# geno-fizzbuzz

Classic FizzBuzz in [Geno](https://github.com/davidiach/geno-lang). Range demos are capped at **100** numbers.

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
geno run --unsafe --cap env,print Main.geno -- 15
geno run --unsafe --cap env,print Main.geno -- range 1 15
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `fizz_buzz(n: Int) -> String`
- `fizz_range(start: Int, stop: Int) -> Result[String, String]`
- `run(args: List[String]) -> Result[String, String]` — `<n>` | `range <start> <stop>`
- `main() -> String` — demo via `run` (`range 1 15`)
