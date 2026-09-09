# geno-hamming

Hamming distance between equal-length strings in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- karolin kathrin
geno run --unsafe --cap env,print Main.geno -- 1011101 1001001
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `hamming_distance(a: String, b: String) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<a> <b>``
- `main() -> String — demo via `run``
