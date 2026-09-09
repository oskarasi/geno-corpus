# geno-html-escape

HTML-escape &, <, >, ", and ' in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- '<b>&x</b>'
geno run --unsafe --cap env,print Main.geno -- a<b c>d
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `escape_char(c: String) -> String`
- `html_escape(s: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
