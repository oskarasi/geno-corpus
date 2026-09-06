# geno-base-convert

Convert non-negative integers between base 10 and bases **2..16** (lowercase hex digits) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- to 255 16
geno run --unsafe --cap env,print Main.geno -- from ff 16
geno run --unsafe --cap env,print Main.geno -- roundtrip 42 8
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `digit_char(d) -> String` / `char_digit(c) -> Option[Int]`
- `to_base(n, base) -> Result[String, String]` — bases 2..16
- `from_base(s, base) -> Result[Int, String]`
- `round_trip(n, base) -> Result[Bool, String]` — `to_base` then `from_base` recovers `n`
- `run(args: List[String]) -> Result[String, String]` — `to` / `from` / `roundtrip`
- `main() -> String` — demo via `run`
