# geno-anagram

Anagram checker in [Geno](https://github.com/davidiach/geno-lang). Normalizes letters (lowercase, strip spaces) and compares sorted character signatures.

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

- `normalize(text) -> String` — lowercase and strip spaces
- `sorted_chars(text) -> String` — characters sorted into a signature string
- `letter_signature(text) -> String` — normalize then sort
- `is_anagram(a, b) -> Bool` — true when signatures match
