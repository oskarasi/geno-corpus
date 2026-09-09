# geno-armstrong

Armstrong (narcissistic) number checker in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 153
geno run --unsafe --cap env,print Main.geno -- 100
geno run --unsafe --cap env,print Main.geno -- 9474
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `pow_int(base, exp) -> Int`
- `digit_count(n) -> Int`
- `is_armstrong(n) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `<n>``
- `main() -> String — demo via `run``
