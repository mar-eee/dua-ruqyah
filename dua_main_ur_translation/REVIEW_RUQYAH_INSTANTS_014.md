# Urdu review: ruqyah instants 014

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_014.json` | 201–211 | 11 | 33 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 33 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, and dignified Pakistani Urdu.
- Reused the reviewed Quran 8:12 wording in row 202, Quran 4:167–168 in row
  210, and Quran 5:33–34 in row 211, adapting only the direct address where
  respectful standalone wording required it.
- Row 206 preserves respectful Quranic address without importing Muhammad's
  name from the explanatory English bracket. This source decision is recorded
  as a field-specific `GLOSSARY.json` override.
- The longer passages in rows 201, 204, 206, and 211 received an additional
  spoken-flow pass covering quotation boundaries, pronoun references, tense,
  and every verse transition.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_014.json`
  after the naturalness edits: 11 entries and 33 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

