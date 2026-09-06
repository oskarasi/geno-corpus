# geno-collatz

Collatz steps-to-one counter (CLI capped at **1_000_000**) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 27
geno run --unsafe --cap env,print Main.geno -- 6
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `steps_to_one(n: Int) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<n>``
- `main() -> String — demo via `run``
