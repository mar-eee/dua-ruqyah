# Urdu review: ruqyah instants 004

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and
the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_004.json` | 41–52 | 12 | 37 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, and Quranic or Sunnah meaning
  while preserving Arabic, transliteration, references, audio links, IDs,
  keys, and nullness.
- Reused reviewed Urdu for Quran 2:284–286, Surahs al-Falaq and al-Nas, Abu
  Dawud 5088 and 3893, Bukhari 5675 and 5745, and Muslim 2186.
- Rows 45 and 47 use identical wording through Quran 3:1–6; row 47 continues
  through verse 10 in fluent Urdu without importing the explanatory English
  insertions of Muhammad's name.
- Row 44 follows the supplied Arabic address to the Lord of mankind and does
  not import the extra English opening “O Allah.”
- Row 48 retains the Arabic plural reference to devils, consistent with row
  34, and row 50 preserves all three effects of the evil eye named in Arabic.
- Field-specific source decisions are recorded in `GLOSSARY.json`.

## Verification and residual checks

- `scripts/verify.py` passed with 12 entries and 37 translated fields.
- A separate continuous-Urdu reading checked fluency, devotional register,
  agreement, terminology, and source fidelity.
- The target-only scan found no Bengali script, non-ASCII digit glyphs,
  replacement characters, or unintended Latin prose.
- An immutable-data comparison against Git `HEAD` confirmed that only target
  text and permitted status/review metadata changed.
