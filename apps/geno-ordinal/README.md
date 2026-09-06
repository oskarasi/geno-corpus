# geno-ordinal

Integer-to-ordinal converter (1st, 2nd, 3rd, 11th, …) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1
geno run --unsafe --cap env,print Main.geno -- 22
geno run --unsafe --cap env,print Main.geno -- 11
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `ordinal(n: Int) -> String`
- `run(args: List[String]) -> Result[String, String] — `<n>``
- `main() -> String — demo via `run``
