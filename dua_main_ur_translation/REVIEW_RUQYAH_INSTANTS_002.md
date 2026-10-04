# Urdu review: ruqyah instants 002

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and
the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_002.json` | 19–32 | 14 | 45 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, and Quranic or Sunnah meaning
  while preserving Arabic, transliteration, references, audio links, IDs,
  keys, and nullness.
- Reused reviewed Urdu wording for Quran 2:163–164 and 2:284–286, Yusuf 12:64,
  Surah al-Kafirun, Abu Dawud 5088, Muslim 2186 and 2708, and the bodily-pain
  supplication.
- Rows 21 and 23 use identical wording for Quran 2:137; row 23 then continues
  naturally with verse 138.
- Rows 22 and 30 follow the complete supplied Arabic by retaining refuge from
  everything Allah created, originated, and spread, and by preserving the
  correct order of the sky and earth clauses omitted or reversed in English.
- Row 32 keeps the frozen/source display citation `Muslim: 222` unchanged even
  though the project evidence identifies the report as Muslim 2202. Its Urdu
  instruction carries the three- and seven-time counts, while its translation
  follows the supplied Arabic without duplicating *Bismillah*.
- Repeated brief, medium, and long-set texts use identical Urdu wherever the
  supplied Arabic is identical.
- Field-specific source decisions are recorded in `GLOSSARY.json`.

## Verification and residual checks

- `scripts/verify.py` passed with 14 entries and 45 translated fields.
- A separate continuous-Urdu reading checked fluency, devotional register,
  agreement, terminology, and source fidelity.
- The target-only scan found no Bengali script, non-ASCII digit glyphs,
  replacement characters, or unintended Latin prose.
- An immutable-data comparison against Git `HEAD` confirmed that only target
  text and permitted status/review metadata changed.
