# Urdu review: ruqyah details 011–013

Translated and reviewed on 2026-09-27 against the complete English source,
the non-aligned Bengali context, supplied Arabic, `GLOSSARY.json`, established
reviewed Quranic parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_011.json`–`013.json` | 20–26 | 7 | 9 | Reviewed; verification passed |

## Review and corrections

- Translated every non-null user-visible target: seven `text` values and the
  two non-null `topic_name` values in chunk 013. Null topic names remain null.
- Read the Urdu independently as continuous prose after semantic comparison
  and checked sentence flow, agreement, pronoun references, list continuity,
  religious terminology, honorifics, and dignified Pakistani Urdu.
- The Bengali database rows with IDs 20–26 belong to a different dataset and
  do not parallel these English rows. They were inspected as context but not
  substituted for the required English-routed source.
- Row 20 retains the reviewed Quran 72:6 wording; row 26 retains the exact
  reviewed Urdu meaning of Surah al-Fatiha. Row 22 follows the supplied Arabic
  wording for Quran 55:15 while preserving its normalized English citation.
- Row 25's source numbering jumps from `9` to `16` and then to `11`; these
  frozen numbers were deliberately preserved rather than silently repaired.
- English text remaining in targets is limited to normalized inline citations.
  The field-specific glossary exception for row 25 documents `Muslim` in its
  citation while the generic hadith label itself is translated.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 011, 012, and 013
  after the naturalness pass: all seven entries and nine translated fields
  passed with no problems.
- Preserved all Arabic blocks, HTML tag sequences, IDs, keys, category links,
  split metadata, ordering, nullness, reference numbers, and source values.
- The target-only scan found no blank target, Bengali script, non-ASCII digit
  glyph outside preserved Arabic blocks, replacement character, or unintended
  Latin prose. The only Latin spans are normalized inline citations.

