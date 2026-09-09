# geno-temp

Temperature converter (C / F / K) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- 0 C F
geno run --unsafe --cap env,print Main.geno -- 212 F C
geno run --unsafe --cap env,print Main.geno -- 0 C K
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `c_to_f / f_to_c / c_to_k / k_to_c / f_to_k`
- `convert(value: Float, frm: String, to: String) -> Result[Float, String]`
- `run(args: List[String]) -> Result[String, String] — `<value> <from> <to>``
- `main() -> String — demo via `run``
