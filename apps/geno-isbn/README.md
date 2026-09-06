# geno-isbn

ISBN-10 and ISBN-13 checksum validation in [Geno](https://github.com/davidiach/geno-lang).

## Install

```bash
pip install geno-lang
```

## Test / run (sandboxed, no capabilities)

```bash
geno test .
geno run .
```

Default `main()` prints a String summary of a few validate demos.

## API

- `normalize(isbn: String) -> String` — strip hyphens and spaces
- `is_valid_isbn10(isbn: String) -> Bool` — weighted sum mod 11 (`X` check digit allowed)
- `is_valid_isbn13(isbn: String) -> Bool` — alternating 1/3 weights, sum mod 10 == 0
- `validate(isbn: String) -> Result[String, String]` — `Ok("ISBN-10"|"ISBN-13")` or Err
- `summarize(isbn: String) -> String`
- `run(args: List[String]) -> Result[String, String]` — `validate <isbn>` or bare `<isbn>`

## Known valid examples

| Input | Result |
|-------|--------|
| `0-306-40615-2` | ISBN-10 |
| `978-0-306-40615-7` | ISBN-13 |
| `048665088X` | ISBN-10 |

## Optional real CLI

Default sandboxed `geno run` **rejects** `--cap` unless you also pass `--unsafe` or `--json`.

```bash
geno run --unsafe --cap env,print Main.geno -- validate 0-306-40615-2
geno run --unsafe --cap env,print Main.geno -- 978-0-306-40615-7
```

`cli_main` is `@untested` (`cli_args`/`print`); default `geno run` uses capability-free `main`.
