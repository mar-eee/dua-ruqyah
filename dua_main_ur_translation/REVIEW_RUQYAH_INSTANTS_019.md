# Urdu review: ruqyah instants 019

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_019.json` | 269–290 | 22 | 66 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 66 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, quotation boundaries, and dignified Pakistani Urdu.
- Rows 271, 274, 275, 281, 283, and 289 reuse exact reviewed Urdu from earlier
  completed material.
- Row 272 follows the supplied Arabic and correct English text for Quran 10:57;
  its Bengali reference is unrelated Quran 10:15. Row 280 follows the supplied
  Arabic, title, and Bengali for Quran 6:125 because the English is unrelated
  Quran 4:125. Row 285 retains the Arabic's general “great distress” rather
  than narrowing it to the English's “great flood.” These source conflicts are
  documented in `GLOSSARY.json`.
- Rows 286 and 288 preserve the Arabic's cohesive pronouns without importing
  Allah from explanatory English brackets. The longer passages in rows 269
  and 279 received dedicated continuous-flow and speaker-transition checks.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_019.json`
  after the naturalness edits: 22 entries and 66 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
