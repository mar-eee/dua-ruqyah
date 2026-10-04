# Urdu review: ruqyah instants 016

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_016.json` | 216–223 | 8 | 24 | Reviewed; verification passed |

## Review and corrections

- Confirmed that this chunk was genuinely pending, then translated every
  topic, title, and Quranic meaning and read all 24 target values continuously
  for accuracy, fluency, speaker, number, agreement, verse sequence, quotation
  boundaries, and dignified Pakistani Urdu.
- Row 217 reuses the exact reviewed Urdu for Quran 37:1–11, row 220 reuses the
  exact reviewed passage for Quran 44:43–50, and row 221 retains the reviewed
  wording of verses 7–8 before continuing consistently through verse 10.
- Row 217 preserves respectful direct Quranic address without importing
  Muhammad from an explanatory English bracket. This decision is recorded as
  a field-specific glossary override.
- The longer passages in rows 218, 219, 222, and 223 received dedicated
  continuous-flow checks for changing speakers, nested quotations, pronouns,
  and verse order.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_016.json`
  after the naturalness edits: 8 entries and 24 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
