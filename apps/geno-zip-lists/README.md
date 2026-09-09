# geno-zip-lists

Zip two integer lists into pairs (truncated to shorter) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- zip 1 2 3 -- 4 5 6
geno run --unsafe --cap env,print Main.geno -- zip 1 2 -- 9
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `zip_lists(xs: List[Int], ys: List[Int]) -> List[List[Int]]`
- `zip_csv(pairs: List[List[Int]]) -> String`
- `run(args: List[String]) -> Result[String, String] — `zip <xs...> -- <ys...>``
- `main() -> String — demo via `run``
