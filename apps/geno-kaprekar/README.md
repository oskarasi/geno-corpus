# geno-kaprekar

Kaprekar's routine for 4-digit numbers (leading zeros allowed) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 3524
geno run --unsafe --cap env,print Main.geno -- 6174
geno run --unsafe --cap env,print Main.geno -- 1234
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `kaprekar_step(n: Int) -> Int`
- `kaprekar_count(n: Int) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<n>``
- `main() -> String — demo via `run``
