# Urdu review: ruqyah instants 010

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_010.json` | 144–157 | 14 | 42 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning. All 42 target values were
  then read continuously for meaning, fluency, speaker, number, agreement,
  devotional register, and terminology.
- Reused the reviewed wording for Quran 10:77 in row 156. Rows 152 and 154
  also preserve the already reviewed Urdu for their matching Arabic sections,
  while translating the additional verses in full.
- Reviewed all other passages against the English, Bengali, and supplied
  Arabic. Verse numbers remain ASCII, Quranic direct address is respectful,
  and the deliberately incomplete source fragment in row 148 remains a
  fragment rather than importing the following verse.
- The Urdu-only pass improved the spoken flow in rows 144–147, replaced a
  stiff reward phrase in row 152, distinguished the two alternatives in row
  154, and regularized the respectful address in row 157.
- Row 152 does not insert “Children of Israel” as the subject where the Arabic
  and Bengali retain an unspecified plural. Row 157 does not insert Muhammad's
  name from an explanatory English bracket. Both decisions are recorded as
  field-specific `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edits: 14 entries and 42
  translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, source text, and source number values. Only target text and the
  permitted status/review metadata changed in the work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

