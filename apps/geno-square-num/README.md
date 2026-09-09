# geno-square-num

Perfect-square and perfect-cube checks in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- square 16
geno run --unsafe --cap env,print Main.geno -- cube 8
geno run --unsafe --cap env,print Main.geno -- both 64
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_square(n: Int) -> Bool`
- `is_cube(n: Int) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `square|cube|both <n>``
- `main() -> String — demo via `run``
