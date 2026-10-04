# Urdu review: ruqyah instants 020

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_020.json` | 291–308 | 18 | 54 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 54 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, quotation boundaries, and dignified Pakistani Urdu.
- Rows 294, 295, and 303–308 reuse exact reviewed Urdu. Row 299 retains the
  reviewed wording of Quran 9:129, row 300 retains the reviewed closing clause
  of Quran 12:64, and row 302 follows its exact reviewed parallel.
- Rows 295 and 299 preserve respectful direct Quranic address without importing
  Muhammad from explanatory English brackets. These decisions are recorded as
  field-specific glossary overrides.
- Rows 291 and 299 received dedicated continuous-flow checks for ellipsis,
  respectful reference, pronouns, and natural spoken Urdu.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_020.json`
  after the naturalness edits: 18 entries and 54 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
