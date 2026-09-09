# geno-morse

Morse code encoder for A-Z and digits 0-9 (letters separated by space; spaces become /) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- SOS
geno run --unsafe --cap env,print Main.geno -- HI
geno run --unsafe --cap env,print Main.geno -- A 1
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `morse_char(c: String) -> String`
- `encode(s: String) -> String`
- `run(args: List[String]) -> Result[String, String] — `<text...>``
- `main() -> String — demo via `run``
