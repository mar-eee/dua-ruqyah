# Urdu review: ruqyah instants 009

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_009.json` | 126–143 | 18 | 56 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, Quranic meaning, and Sunnah
  meaning. All 56 target values were then read continuously for meaning,
  fluency, speaker, number, agreement, devotional register, and terminology.
- Reused the reviewed wording for rows 126–130, 133, 139, and 142 wherever the
  supplied Arabic matches earlier ruqyah or dua records. The seven repeated
  Arabic passages shared with earlier ruqyah chunks have identical Urdu.
- Reviewed the newly rendered Quran passages in rows 131–132, 134–135, 137–138,
  140–141, and 143 against both prose references and the supplied Arabic.
  Verse numbers remain ASCII and direct address to the Prophet is respectful.
- The Urdu-only read-through replaced a stiff temporal phrase in row 132,
  preserved the unfinished conditional fragment actually supplied in row 135,
  simplified row 137, and made row 143's rhetorical question natural without
  changing its scope.
- Rows 132, 134, 140, and 141 omit explanatory English bracket additions that
  are absent from the Arabic. Row 135 follows the Arabic and Bengali
  conditional rather than the English “although.” These decisions are recorded
  as field-specific `GLOSSARY.json` overrides.
- Row 127 follows the required English/frozen Abu Dawud 3106 attribution rather
  than the conflicting Bengali title; row 133 likewise retains the required
  English Bukhari 5656 title.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edits: 18 entries and 56
  translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, source text, and source number values. Only target text and the
  permitted status/review metadata changed in the work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

