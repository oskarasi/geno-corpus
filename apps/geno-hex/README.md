# geno-hex

Hex encode/decode for non-negative integers (lowercase output) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- to 255
geno run --unsafe --cap env,print Main.geno -- from ff
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `nibble_to_hex(n: Int) -> String`
- `hex_nibble(c: String) -> Option[Int]`
- `int_to_hex(n: Int) -> Result[String, String]`
- `hex_to_int(s: String) -> Result[Int, String]`
- `run(args: List[String]) -> Result[String, String] — `to <n>` | `from <hex>``
- `main() -> String — demo via `run``
