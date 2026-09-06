# geno-stack

Stack ADT over `List[Int]` (top at list end) in [Geno](https://github.com/davidiach/geno-lang).

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
geno run --unsafe --cap env,print Main.geno -- demo
geno run --unsafe --cap env,print Main.geno -- push 1 2 3
```

Note: `run(args)` is capability-free; OS argv via `cli_args()` needs `--cap env`.

## API

- `push(s: List[Int], x: Int) -> List[Int]`
- `peek(s: List[Int]) -> Result[Int, String]`
- `pop(s: List[Int]) -> Result[List[Int], String]`
- `is_empty(s: List[Int]) -> Bool`
- `ints_csv(xs: List[Int]) -> String`
- `run(args: List[String]) -> Result[String, String] — `demo` | `push <ints...>``
- `main() -> String — demo via `run``
