# Urdu review: ruqyah instants 006

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
cited primary reports where the sources conflicted, and the project's
natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_006.json` | 70–88 | 19 | 61 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, Quranic meaning, and Sunnah
  meaning. All 61 target values were then read continuously for meaning,
  fluency, speaker, number, agreement, devotional register, and terminology.
- Reused already reviewed Urdu where the supplied Arabic matches: the salawat
  in row 70; the invocations in rows 74, 76, 78, 80, 82, and 88; and Quran
  17:110–111 in row 75. Rows 72 and 86 use identical Urdu for their identical
  Arabic, including the separate three-time instruction.
- Reviewed the newly rendered Quran passages in rows 71, 73, 77, 79, 81, 83,
  85, and 87 against both prose sources and the supplied Arabic. Verse numbers
  remain ASCII, and the direct Quranic address is respectful and natural.
- The final Urdu-only read-through regularized the separated letters in row
  77 as `حا، میم` and made row 83's causal envy clause idiomatic without
  changing its meaning.
- Row 70 omits the English addition “in all the worlds,” which is absent from
  both the supplied Arabic and
  [Bukhari 3370](https://sunnah.com/bukhari:3370).
- Row 74 preserves a general request and renders `الْمَنَّانُ` as the great
  Bestower, following the supplied Arabic, Bengali, and
  [Abu Dawud 1495](https://sunnah.com/abudawud:1495), rather than the English
  request for help and “Compassionate.”
- Row 78 likewise preserves the general request followed by testimony to
  Allah's oneness, as in [Abu Dawud 1493](https://sunnah.com/abudawud:1493).
  Row 88 begins “Our Lord is Allah,” rather than turning that statement into
  an address, following [Abu Dawud 3892](https://sunnah.com/abudawud:3892).
- All four source-conflict decisions are recorded as field-specific
  `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `scripts/verify.py` on the chunk after the final naturalness edits: 19
  entries and 61 translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, and source number values. Only target text and permitted
  status/review metadata changed in the work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
