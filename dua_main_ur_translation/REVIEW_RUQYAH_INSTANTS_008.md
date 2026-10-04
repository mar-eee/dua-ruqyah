# Urdu review: ruqyah instants 008

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_008.json` | 105–125 | 21 | 64 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, Quranic meaning, and Sunnah
  meaning. All 64 target values were then read continuously for meaning,
  fluency, speaker, number, agreement, devotional register, and terminology.
- Reused already reviewed Urdu wherever the supplied Arabic matches, including
  rows 107, 109, 111–113, 115–116, 119, 121, 124, and 125. This preserves
  wording already established in the dua table and earlier ruqyah chunks.
- Reviewed the newly rendered Quran passages in rows 105, 108, 110, 114, 117,
  120, 122, and 123 against the English, Bengali, and supplied Arabic. Verse
  numbers remain ASCII, and Quranic commands retain their intended voice.
- The separate Urdu-only read-through made row 108's earnings clauses more
  idiomatic, clarified the question sequence in row 110, and regularized the
  vocative rhythm in row 118 without changing meaning.
- Row 107 does not insert Allah into the prostration clause merely because the
  English includes an explanatory bracket. Row 119 likewise renders the
  Quranic imperative respectfully without inserting Muhammad's name. Both
  decisions follow the supplied Arabic and are recorded as field-specific
  `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edits: 21 entries and 64
  translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, source text, and source number values. Only target text and the
  permitted status/review metadata changed in the work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

