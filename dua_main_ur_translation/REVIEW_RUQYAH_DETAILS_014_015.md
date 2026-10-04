# Urdu review: ruqyah details 014–015

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, established reviewed Quranic parallels,
and the project's natural-Urdu standard.

| Files | ID | Split parts | Translated fields | Result |
|---|---:|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_014.json`–`015.json` | 26 | 2–7 of 12 | 6 | Reviewed; verification passed |

## Review and corrections

- Translated all six requested `text` fields, preserving the continuity of the
  long treatment entry across both chunks.
- Reused the project's reviewed Urdu wording for Quran 2:1–6, 2:163–164,
  2:255–256, 2:285–286, 3:18–19, 7:54–56, 23:115–118, and 37:1–10.
- Read the Urdu independently after semantic comparison and checked flow,
  agreement, respectful direct address, verse numbering, headings, and
  established Islamic terminology.
- Documented the field-specific source exceptions for explanatory occurrences
  of `Muhammad` and the inaccurate English rendering “your Allah” for
  `إِلَٰهَكُمْ`; the Urdu follows the supplied Quranic Arabic.
- Part 7 ends with the Arabic of Quran 46:29–32. Its translation belongs to the
  next split part, so no text from chunk 016 was moved into this requested range.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 014 and 015 after
  the naturalness pass; all six translated fields passed with no problems.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, split marker, order, verse number, and source value.
- The target-only scan found no blank target, Bengali script, replacement
  character, or unintended Latin prose.
