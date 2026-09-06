# geno-happy

Happy-number checker in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- check 19
geno run --unsafe --cap env,print Main.geno -- check 2
geno run --unsafe --cap env,print Main.geno -- check 7
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `sum_sq_digits(n: Int) -> Int`
- `contains_int(xs: List[Int], x: Int) -> Bool`
- `is_happy(n: Int) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `check <n>``
- `main() -> String — demo via `run``
