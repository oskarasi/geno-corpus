# geno-ratio

Simplify an integer ratio a:b using GCD in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 15 25
geno run --unsafe --cap env,print Main.geno -- -6 -9
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `abs_int(n: Int) -> Int`
- `gcd(a: Int, b: Int) -> Int`
- `simplify(a: Int, b: Int) -> Result[List[Int], String]`
- `describe(a: Int, b: Int) -> String`
- `run(args: List[String]) -> Result[String, String] — `<a> <b>``
- `main() -> String — demo via `run``
