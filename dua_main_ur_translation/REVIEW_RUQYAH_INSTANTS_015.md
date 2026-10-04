# Urdu review: ruqyah instants 015

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_015.json` | 212–215 | 4 | 12 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 12 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, and dignified Pakistani Urdu.
- Row 214 reuses the exact reviewed Urdu for Quran 22:19–22. Within row 215,
  the reviewed wording of verses 97–98, 107, 109, and 115–118 is retained.
- Rows 213 and 215 preserve respectful direct Quranic address without importing
  Muhammad or the believers from explanatory English brackets. Row 215 also
  follows Arabic `Rabbi` (“my Lord”) in verse 118 rather than Bengali's plural
  address. These decisions are recorded as field-specific glossary overrides.
- The forty-verse passage in row 215 received a dedicated continuous-flow pass
  for speaker changes, nested quotations, pronouns, verse order, and repeated
  divine address.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_015.json`
  after the naturalness edits: 4 entries and 12 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

