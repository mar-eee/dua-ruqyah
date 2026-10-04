# Urdu review: ruqyah details 055

Translated, reviewed, and completed on 2026-09-28 against the complete English
source, `GLOSSARY.json`, the full five-part source context for row 109, the
cited Quranic text, and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_055.json` | 108–109 | 2 | 2 | Reviewed; verification passed |

## Review and corrections

- Translated both text fields and retained both null topic names. Row 109 is a
  five-part split record; only its complete first part belongs to this chunk,
  and its continuation in chunk 056 was read for context without being edited.
- In row 108, retained every substantive point about the reciter's fluency,
  attention to meaning, reliance on Allah, intention during treatment, and
  reading from the mushaf. Experiential and prescriptive claims that are not
  themselves Quranic quotations are clearly presented as the author's views
  where needed, without adding a new ruling.
- The English source incorrectly introduces Quran 24:2 as a statement about
  punishing sorcerers. The verse actually gives the prescribed punishment for
  zina and then says not to let pity prevent Allah's command. Urdu translates
  the supplied excerpt accurately and identifies its real context, checked
  against [Quran 24:2](https://quran.com/24/2). This correction is documented
  in `GLOSSARY.json` under `ruqyah_details.text.108`.
- In row 109, preserved the source's two-stage protection advice, the example
  concerning lowering the gaze, the claimed spiritual and physical effects,
  and the concluding description of ruqyah as a means of improving one's
  spiritual condition. Pronoun references were clarified without importing
  content from the later split parts.
- Reread both targets independently as continuous Urdu and refined sentence
  rhythm, agreement, attribution, devotional wording, and consistent use of
  `قرآن`, `رقیہ`, `سحر`, `نظرِ بد`, `جنات` and `توبہ`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py
  work\ruqyah_details\ruqyah_details_055.json` after the final naturalness
  pass; both entries and both translated fields passed.
- Preserved every ID, key, frozen field, category link, part count, split-field
  marker, order, source number and null. The verse reference remains in ASCII
  digits.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit glyph or unintended English prose.
