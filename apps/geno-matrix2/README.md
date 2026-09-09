# geno-matrix2

Determinant of a 2x2 integer matrix [[a, b], [c, d]] = ad - bc in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 1 2 3 4
geno run --unsafe --cap env,print Main.geno -- 3 1 2 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `det2(a: Int, b: Int, c: Int, d: Int) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<a> <b> <c> <d>``
- `main() -> String — demo via `run``
