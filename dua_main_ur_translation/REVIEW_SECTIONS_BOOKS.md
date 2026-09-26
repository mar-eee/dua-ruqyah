# Urdu review: sections and books

Reviewed on 2026-09-24 against the routed English/Bengali source files,
`GLOSSARY.json`, and the project's natural-Urdu standard.

| File | Entries | Translated fields | Result |
|---|---:|---:|---|
| `work/sections/sections_001.json` | 21 | 21 | Reviewed; verification passed |
| `work/books/books_001.json` | 3 | 9 | Reviewed; verification passed |
| Total | 24 | 30 | |

## Checks completed

- Read every title and name for faithful meaning, natural Pakistani Urdu, and
  consistent Islamic terminology.
- Used English as the routed source for `sections` and Bengali as the routed
  source for `books`; the other available language was used only as context.
- Preserved all IDs, composite keys, row order, null values, and source text.
- Reused the earlier section-title work where sound, then refined wording that
  omitted details such as bathing with the recited water, applying olive oil to
  the skin, and the before/during/after-recitation distinction.
- Ran `verify.py` separately on both chunks; both pass with no problems.
- Re-ran `verify.py` on every chunk currently marked `done` (51 chunks); all
  pass the structural and automated language checks.

The next required untranslated area is determined by `WORK_STATUS.md` after
its final regeneration.
