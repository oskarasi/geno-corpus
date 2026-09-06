# geno-gcd

Greatest common divisor via the Euclidean algorithm in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 48 18
geno run --unsafe --cap env,print Main.geno -- 17 13
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `abs_int(n: Int) -> Int`
- `gcd(a: Int, b: Int) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<a> <b>``
- `main() -> String — demo via `run``
