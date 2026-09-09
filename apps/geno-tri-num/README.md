# geno-tri-num

Triangular numbers (`nth` / `check`) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- nth 8
geno run --unsafe --cap env,print Main.geno -- check 10
geno run --unsafe --cap env,print Main.geno -- check 7
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `tri_num(n: Int) -> Result[Int, String]`
- `is_triangular(x: Int) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `nth <n>` | `check <x>``
- `main() -> String — demo via `run``
