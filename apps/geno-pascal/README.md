# geno-pascal

Pascal's triangle row (0-indexed) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 3
geno run --unsafe --cap env,print Main.geno -- 0
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `pascal_row(n: Int) -> List[Int] — requires n >= 0`
- `ints_csv(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String] — `<n>` (0..20)`
- `main() -> String — demo via `run``
