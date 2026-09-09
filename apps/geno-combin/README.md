# geno-combin

Binomial coefficient C(n, k). Both n and k must be **non-negative** in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- 10 3
geno run --unsafe --cap env,print Main.geno -- 5 2
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `combin(n, k) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `<n> <k>``
- `main() -> String — demo via `run``
