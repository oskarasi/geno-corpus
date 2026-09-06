# geno-binary

Binary encode/decode for non-negative integers in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- to 13
geno run --unsafe --cap env,print Main.geno -- from 1101
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `int_to_binary(n: Int) -> Result[String, String]`
- `binary_to_int(s: String) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `to <n>` | `from <bits>``
- `main() -> String — demo via `run``
