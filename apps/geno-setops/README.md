# geno-setops

Order-preserving set ops (`union` / `intersect` / `diff`) on integer lists in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- union 1 2 -- 2 3
geno run --unsafe --cap env,print Main.geno -- intersect 1 2 3 -- 2 4 1
geno run --unsafe --cap env,print Main.geno -- diff 1 2 3 -- 2 4
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `contains_int(xs: List[Int], x: Int) -> Bool`
- `dedupe(xs: List[Int]) -> List[Int]`
- `union / intersect / diff (List[Int], List[Int]) -> List[Int]`
- `run(args: List[String]) -> Result[String, String] — `union|intersect|diff <a...> -- <b...>``
- `main() -> String — demo via `run``
