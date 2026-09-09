# geno-manhattan

Manhattan (taxicab) distance between 2D integer points in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 0 0 3 4
geno run --unsafe --cap env,print Main.geno -- -2 3 1 -1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `manhattan(x1: Int, y1: Int, x2: Int, y2: Int) -> Int`
- `run(args: List[String]) -> Result[String, String] — `<x1> <y1> <x2> <y2>``
- `main() -> String — demo via `run``
