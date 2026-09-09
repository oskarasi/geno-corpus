# geno-template

Simple `{name}` template renderer in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- render "Hello, {name}!" name World
geno run --unsafe --cap env,print Main.geno -- render "{x}" x Geno
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `render(template: String, name: String, value: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `render <template> <name> <value>``
- `main() -> String — demo via `run``
