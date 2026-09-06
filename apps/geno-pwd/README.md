# geno-pwd

Password strength meter written in [Geno](https://github.com/davidiach/geno-lang).

## Scoring

`score(password)` returns an integer from **0–5**:

| Criterion | Points |
|-----------|--------|
| Has lowercase letter | +1 |
| Has uppercase letter | +1 |
| Has digit | +1 |
| Has symbol (non-alphanumeric) | +1 |
| Length ≥ 8 | +1 |

`label(score)` maps the score to:

| Score | Label |
|-------|-------|
| 0–1 | weak |
| 2 | fair |
| 3 | good |
| 4–5 | strong |

Helpers `has_lower`, `has_upper`, `has_digit`, and `has_symbol` scan the string with `char_at`.

## Run

```bash
geno test .
geno run .
```

## Layout

- `geno.toml` — project manifest
- `Main.geno` — strength helpers, scoring, and `main`
