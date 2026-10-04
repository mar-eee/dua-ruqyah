# Urdu review: ruqyah details 021–025

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and the
project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_021.json`–`025.json` | 32–41 | 9 | 11 | Reviewed; verification passed |

## Review and corrections

- Translated all nine text fields and the two non-null topic titles. All eight
  null topic names remain null.
- Rendered the Quranic passages directly from the supplied Arabic in the
  project's established Urdu register, while preserving every English inline
  citation and source number. Editorial bracket glosses were not inserted into
  the verses; the decisions are documented in field-specific glossary entries.
- Preserved both Arabic tahreej formulas and their Latin transliterations
  verbatim. The term `tahreej` is retained once beside its Urdu form for clarity.
- Corrected the visibly corrupted source names `Abdullah ibn Sajis` and
  `Abu Lubabahit` to Abdullah ibn Sarjis and Abu Lubabah after checking Sunan
  an-Nasa'i 34 and Sahih Muslim 2233h. Correct honorifics were applied.
- Corrected the source's mistaken `SWT` after Messenger of Allah in row 38 to
  the appropriate Prophetic honorific `ﷺ`; frozen source text remains unchanged.
- Restored the final clause of Quran 17:82 in row 41 because it is present in
  the supplied Arabic and in reviewed parallel rows 163 and 274.
- Read every target independently as continuous Urdu and corrected agreement,
  word order, dialogue flow, pronoun reference, terminology, and list rhythm.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 021–025 after the
  naturalness pass; all nine entries and eleven fields passed with no problems.
- Reverified chunks 019–020 as part of the requested range; both remained clean.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, split marker, order, citation number, null, and source value.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit outside preserved Arabic, or unintended English
  prose. Remaining Latin spans are required citations and transliterations.
