# Urdu review: ruqyah details 019–020

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, established reviewed Quranic parallels,
and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_019.json`–`020.json` | 30–31 | 7 | 7 | Reviewed; verification passed |

## Review and corrections

- Translated all seven requested `text` fields: the six continuous parts of
  row 30 and the complete symptom list in row 31. Null topic names remain null.
- Reused the project's reviewed Urdu wording for Quran 10:81–82, 7:117–122,
  and 20:69; translated Quran 4:76, 5:72, and 9:30 in the same register.
- Read the Urdu independently as continuous prose and checked imperative
  consistency, pronoun references, ordinals, list continuity, Quranic titles,
  treatment terminology, and established Islamic vocabulary.
- Preserved the embedded transliteration `la ilaha illa lah` verbatim and kept
  all source numbers as ASCII outside the supplied Arabic blocks.
- The corrupted source phrase `Allah mengine removed him/her` was rendered by
  its clear intended alternatives: Allah removed or sent the jinn away. No
  frozen source text was altered.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 019 and 020 after
  the naturalness pass; all seven entries and fields passed with no problems.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, split marker, order, verse number, null, and source value.
- The target-only scan found no blank target, Bengali script, non-ASCII digit
  outside preserved Arabic, replacement character, or unintended English
  prose. The one Latin phrase is the required source transliteration.
