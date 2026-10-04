# Urdu review: ruqyah details 053

Translated, reviewed, and completed on 2026-09-28 against the complete English
source, the Bengali cross-check, `GLOSSARY.json`, and the project's
natural-Urdu standard. Neither English entry contains supplied Arabic or a
cited primary-text reference requiring an external conflict check.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_053.json` | 105–106 | 2 | 2 | Reviewed; verification passed |

## Review and corrections

- Translated all three case narratives in row 105, including their headings,
  reported dialogue, treatment descriptions, and the morning-and-evening
  protection instruction. The null topic name remains null.
- Translated every qualification, prohibition, numbered condition, and
  explanatory definition of a `راقی` in row 106. The list structure and every
  `<b>` tag remain aligned with the source.
- Read Bengali rows 105 and 106 as the required cross-check. They contain
  unrelated material and route respectively to category/subcategory 8/54 and
  8/55, while the English source rows route to 5/86 and 6/87. Because
  `ruqyah_details` is English-routed, no Bengali wording was imported.
- Repaired the mechanical splice in English row 106, where `A Raaqi is a p`
  is separated from the continuation `erson who...`. The Urdu retains the
  supplied paragraph order and every substantive condition while presenting
  complete sentences. This decision is recorded in the field-specific
  `GLOSSARY.json` override `ruqyah_details.text.106`.
- Restored the evident omitted first-person subject before the final teaching
  sentence in row 105 and normalized broken sentence boundaries without adding
  a new claim.
- Reread both targets independently as continuous Urdu and refined titles,
  sentence flow, agreement, pronoun references, devotional vocabulary, and
  consistent use of `نظرِ بد`, `رقیہ`, `توحید`, `شرک`, and `سحر`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py
  work\ruqyah_details\ruqyah_details_053.json` after the final target edits;
  both entries and both translated fields passed.
- Preserved every ID, key, frozen field, category link, order, null, source
  number value, and HTML tag sequence. The source numbers 112, 113, and 114
  remain ASCII digits.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit glyph, or unintended Latin prose after HTML tags
  were excluded.
