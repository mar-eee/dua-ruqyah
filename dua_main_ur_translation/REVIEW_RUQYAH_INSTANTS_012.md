# Urdu review: ruqyah instants 012

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_012.json` | 174–189 | 16 | 48 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 48 target
  values continuously for meaning, fluency, speaker, number, agreement, verse
  sequence, and dignified Pakistani Urdu.
- Reused reviewed wording for matching passages or clauses in Quran 7:89,
  12:64, 33:70–71, 39:38, 40:44–45, and 87:4. Row 175 now also
  exactly matches the established translation of its identical verse.
- Row 183 follows the displayed Arabic's final protection clause instead of
  importing the opening dialogue that appears only in the English and Bengali
  prose fields. As a standalone verse, row 185 explicitly preserves the
  Arabic first-person plural while omitting the explanatory English bracket.
- Row 184's English translation is an unrelated copy of Quran 27:73–75. The
  supplied Arabic, title, and Bengali are Quran 33:70–71, so Urdu follows the
  actual passage and preserves its verse numbers. These source-conflict
  decisions are recorded as field-specific glossary overrides.
- The long passages in rows 180 and 186 received a separate spoken-flow pass;
  respectful direct address, rhetorical questions, quoted speech, and all
  verse transitions remain intact.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_012.json`
  after the final naturalness edits: 16 entries and 48 translated fields
  passed with no problems.
- Added a narrowly scoped `number_overrides` verifier path so an explicitly
  documented wrong source number can follow the supplied primary text; all
  other number checks remain active.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
