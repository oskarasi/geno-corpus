# geno-power-set-size

Power set cardinality `|P(S)| = 2^n` in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 5
geno run --unsafe --cap env,print Main.geno -- 10
geno run --unsafe --cap env,print Main.geno -- 0
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `power_set_size(n: Int) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<n>` (0..60)`
- `main() -> String — demo via `run``
