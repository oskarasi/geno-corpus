# geno-area-rect

Rectangle area and perimeter. Dimensions must be **non-negative** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 3 4
geno run --unsafe --cap env,print Main.geno -- 5 5
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `area(width, height) -> Result[Int, String]`
- `perimeter(width, height) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<width> <height>``
- `main() -> String — demo via `run``
