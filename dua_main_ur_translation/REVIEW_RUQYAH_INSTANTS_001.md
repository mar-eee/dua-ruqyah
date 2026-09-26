# Urdu review: ruqyah instants 001

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and
the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_001.json` | 1–18 | 18 | 54 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic or Sunnah meaning while preserving
  Arabic, transliteration, references, audio links, IDs, keys, and nullness.
- Reused reviewed Urdu wording for exact repetitions of Surah al-Fatihah,
  Quran 2:1–5, Ayat al-Kursi, and the established refuge supplications.
- Rows 7, 9, and 11 retain the Quran's respectful direct address without
  inserting the personal name supplied only in an English explanatory bracket.
- Rows 8 and 18 follow the supplied Arabic of Bukhari 3371: refuge from every
  devil, harmful creature, and evil eye. The unrelated extra English clause
  about everything created was not imported.
- Repeated brief, medium, and long-set texts use identical Urdu wherever the
  supplied Arabic is identical.
- Field-specific source decisions are recorded in `GLOSSARY.json`.

## Verification and residual checks

- `scripts/verify.py` passed with 18 entries and 54 translated fields.
- A separate continuous-Urdu reading checked fluency, devotional register,
  agreement, terminology, and source fidelity.
- The target-only scan found no Bengali script, non-ASCII digit glyphs,
  replacement characters, or unintended Latin prose.
- An immutable-data comparison against Git `HEAD` confirmed that only target
  text and permitted status/review metadata changed.
