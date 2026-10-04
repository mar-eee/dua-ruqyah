# Urdu SQLite draft build — 2026-10-04

Output: `G:\dua-ruqyah\dua_main_ur.sqlite`

This is an app-compatible **draft**, not a publication-ready complete Urdu database. Built from the current local translation work with `python scripts/build.py ur --partial`. The user exempted book content from translation for this build. The 86 `book_details` rows, including 176 untranslated target slots, remain **exactly the Bengali source rows** to preserve the source database's schema and key/row structure. Translated `books` and `sections` rows remain present.

SHA-256: `6D16FA81DC319ECD288B125559A02F11987E8BF5C8A07BCE6783DF9DB13FE06C`

## Technical checks

- `PRAGMA integrity_check`: `ok`; `PRAGMA foreign_key_check`: no issues.
- `sqlite_master` schema objects match `dua_main_en.sqlite` exactly.
- Every table's row count and key set match its designated EN/BN source; all nontranslated/frozen columns match that source.
- All non-book target text in the build matches the current local work files, including 148 nested dua-group fields and 110 structured drawer-content slots. No Bengali characters were found outside `book_details`.
- A pre-build audit found 4,706 filled non-book text fields, 301 protected Arabic blocks copied exactly, 148 populated nested group fields and 87 populated drawer-content source-text fields, with no coverage or key-set errors.
- The full work-file verifier reports only the 176 intentionally untranslated `book_details` slots; no other automated errors.

## Publication blockers

The supplied Arabic in `dua_infos` contains apparent Quran-transcription errors documented in [review 056–060](REVIEW_DUA_INFOS_056_060.md) and [review 061–065](REVIEW_DUA_INFOS_061_065.md): Quran 39:23 `خُلُودُ` for `جُلُودُ`, Quran 7:205 `وَجِيفَةً` for `وَخِيفَةً`, and an extra vowel mark in the source excerpt of Quran 73:4. The Arabic remains untouched under the translation rule. Correct the authorized source and affected outputs, then rebuild and recheck before publication. Hadith/citation caveats in the per-batch reviews and independent human scholarly review also remain outside the technical SQLite checks.

The local Ruqyah translations and their review notes include uncommitted work at build time. This database was not pushed to GitHub.
