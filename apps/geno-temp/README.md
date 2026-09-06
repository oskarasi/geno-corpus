# geno-temp

Temperature converter (C/F/K) in [Geno](https://github.com/davidiach/geno-lang) using `Float` math.

## Install

```bash
pip install geno-lang
```

## Test

```bash
geno test Main.geno
```

## Run

```bash
geno run Main.geno
```

## API

- `c_to_f(c) -> Float` / `f_to_c(f) -> Float`
- `c_to_k(c) -> Float` / `k_to_c(k) -> Float`
- `f_to_k(f) -> Float`
- `round_tenths(x) -> Int` — display helper (`round(x * 10)`)
