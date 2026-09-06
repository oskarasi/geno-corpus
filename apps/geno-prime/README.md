# geno-prime

Prime number helpers in [Geno](https://github.com/davidiach/geno-lang). Demo `upto` limits are capped at **200** so default runs stay cheap.

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
geno run --unsafe --cap env,print Main.geno -- check 17
geno run --unsafe --cap env,print Main.geno -- next 10
geno run --unsafe --cap env,print Main.geno -- upto 20
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `is_prime(n: Int) -> Bool`
- `next_prime(n: Int) -> Int` — smallest prime ≥ `n` (or 2 if `n < 2`)
- `primes_up_to(limit: Int) -> List[Int]`
- `ints_csv(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String]` — `check` / `next` / `upto`
- `main() -> String` — demo via `run` (`upto 50`, `next 90`, `check 97`)
