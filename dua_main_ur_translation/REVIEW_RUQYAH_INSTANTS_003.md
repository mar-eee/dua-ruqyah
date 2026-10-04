# Urdu review: ruqyah instants 003

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and
the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_003.json` | 33–40 | 8 | 26 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, and Quranic or Sunnah meaning
  while preserving Arabic, transliteration, references, audio links, IDs,
  keys, and nullness.
- Rows 33 and 35 use identical Urdu for Quran 2:254–257 and retain the already
  reviewed Ayat al-Kursi wording within the passage.
- Rows 34 and 36 follow the supplied Arabic where the English changes number
  or meaning: the former retains plural devils, and the latter preserves
  Allah's undefeated army and the correct wealth clause.
- Rows 37, 39, and 40 reuse reviewed Urdu for Surah al-Ikhlas, Quran 2:284–286,
  and the bodily-pain supplication.
- Row 38 follows the Arabic and Bengali wording “Lord of the Mighty Throne.”
- Field-specific source decisions are recorded in `GLOSSARY.json`.

## Verification and residual checks

- `scripts/verify.py` passed with 8 entries and 26 translated fields.
- A separate continuous-Urdu reading checked fluency, devotional register,
  agreement, terminology, and source fidelity.
- The target-only scan found no Bengali script, non-ASCII digit glyphs,
  replacement characters, or unintended Latin prose.
- An immutable-data comparison against Git `HEAD` confirmed that only target
  text and permitted status/review metadata changed.
