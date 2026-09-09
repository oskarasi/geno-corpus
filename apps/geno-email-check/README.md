# geno-email-check

Simple email shape check (`local@domain` with a dot in the domain) in [Geno](https://github.com/davidiach/geno-lang).
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
geno run --unsafe --cap env,print Main.geno -- user@example.com
geno run --unsafe --cap env,print Main.geno -- nope
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_email(s) -> Bool`
- `run(args: List[String]) -> Result[String, String] — `<email>``
- `main() -> String — demo via `run``
