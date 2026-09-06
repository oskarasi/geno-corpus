# geno-tip

Tip and bill splitter in [Geno](https://github.com/davidiach/geno-lang). All amounts are in **cents** (`Int`) to avoid floating-point money issues.

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
geno run --unsafe --cap env,print Main.geno -- tip 10000 15
geno run --unsafe --cap env,print Main.geno -- split 11500 4
```

Note: `run(args)` itself is capability-free and parses a `List[String]`; wiring OS argv uses `cli_args()` which requires `--cap env`.

## API

- `tip_cents(bill_cents, tip_percent) -> Int` — tip amount in cents (`requires` non-negative inputs)
- `total_cents(bill_cents, tip_percent) -> Int` — bill + tip
- `split_cents(total, people) -> Result[Int, String]` — per-person share (`Err` if `people < 1`)
- `run(args: List[String]) -> Result[String, String]` — `tip <bill> <pct>` or `split <total> <people>`
- `main() -> String` — demo via `run`
