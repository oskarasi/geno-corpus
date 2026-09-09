# geno-coin-change

Greedy US coin change (quarters, dimes, nickels, pennies). Cents must be **non-negative** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 41
geno run --unsafe --cap env,print Main.geno -- 99
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `change(cents) -> Result[List[Int], String] — [q, d, n, p]`
- `describe(cents) -> String`
- `run(args: List[String]) -> Result[String, String] — `<cents>``
- `main() -> String — demo via `run``
