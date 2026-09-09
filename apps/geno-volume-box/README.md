# geno-volume-box

Rectangular box volume and surface area in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- volume 2 3 4
geno run --unsafe --cap env,print Main.geno -- surface 2 3 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `volume(l: Int, w: Int, h: Int) -> Result[Int, String]`
- `surface(l: Int, w: Int, h: Int) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `volume|surface <l> <w> <h>``
- `main() -> String — demo via `run``
