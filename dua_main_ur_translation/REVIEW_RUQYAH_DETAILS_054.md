# Urdu review: ruqyah details 054

Translated, reviewed, and completed on 2026-09-28 against the complete English
source, the Bengali cross-check, `GLOSSARY.json`, the reviewed parallel in row
106, and the project's natural-Urdu standard. The English entry contains no
supplied Arabic or cited primary-text reference requiring an external conflict
check.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_054.json` | 107 | 1 | 1 | Reviewed; verification passed |

## Review and corrections

- Translated all nine signs of a genuine `راقی`, the subheading, and all seven
  further conditions, including the prohibitions, patient confidentiality,
  religious counsel, knowledge of illnesses, and knowledge of جنّات.
- Reused the same natural Urdu for the duplicated conditions already reviewed
  in English row 106, while preserving row 107's numbered `<b>` list exactly.
- Read Bengali row 107 as the required cross-check. It is unrelated material
  about neurological illness and routes to category/subcategory 8/55, whereas
  English row 107 routes to 6/88. Because `ruqyah_details` is English-routed,
  no Bengali wording was imported and no glossary override was needed.
- Reread the target independently as continuous Urdu and checked sentence
  flow, agreement, devotional register, and consistent use of `توحید`, `شرک`,
  `قرآن و سنت`, `رقیہ`, and `راقی`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py
  work\ruqyah_details\ruqyah_details_054.json` after the final target edits;
  the entry and translated field passed.
- Preserved every ID, key, frozen field, category link, order, null, source
  number value, and HTML tag sequence. The list numbers remain ASCII digits.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit glyph, or unintended Latin prose after HTML tags
  were excluded.
