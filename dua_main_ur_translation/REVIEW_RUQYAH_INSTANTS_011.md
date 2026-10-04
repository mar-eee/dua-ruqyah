# Urdu review: ruqyah instants 011

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_011.json` | 158–173 | 16 | 48 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning. All 48 target values were
  then read continuously for meaning, fluency, speaker, number, agreement,
  devotional register, and terminology.
- Reused the complete reviewed wording for Quran 41:44 in row 159. Rows 158,
  160, 166, and 170 preserve reviewed Urdu for matching Arabic subsections and
  add the remaining verses without altering those established passages.
- The Urdu-only pass naturalized the throwing instruction in rows 158 and 162,
  clarified the punishment clause in row 166, corrected the victory clause in
  row 167, and smoothed the long rhetorical passages in rows 168 and 170.
- Row 160 retains the Arabic first-person plural “We said,” rather than the
  English substitution “Allah said.” Row 162 omits an explanatory English
  bracket after prostration. Rows 168 and 170 preserve respectful Quranic
  address without inserting Muhammad's name. These decisions are recorded as
  field-specific `GLOSSARY.json` overrides.
- The one complete Arabic passage repeated in earlier ruqyah chunks has
  identical Urdu; all partial repetitions also retain their reviewed wording.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edits: 16 entries and 48
  translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, source text, and source number values. Only target text and the
  permitted status/review metadata changed in the work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

