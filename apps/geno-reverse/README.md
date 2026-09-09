# geno-reverse

Reverse a string or a list of integers in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- str Geno
geno run --unsafe --cap env,print Main.geno -- list 1 2 3 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `reverse_string(text: String) -> String`
- `reverse_list(xs: List[Int]) -> List[Int]`
- `ints_csv(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String] — `str <text...>` | `list <ints...>``
- `main() -> String — demo via `run``
