# Urdu review: ruqyah instants 005

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
cited primary reports where the sources conflicted, and the project's
natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_005.json` | 53–69 | 17 | 53 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, instruction, Quranic meaning, and Sunnah
  meaning. Reused reviewed Urdu for exact repeated passages and then read all
  53 target values continuously for meaning, fluency, speaker, number,
  agreement, devotional register, and terminology.
- Rows 53 and 56–58 preserve the complete displayed passages from Surah Ali
  Imran. Rows 58 and 61 use identical Urdu for the identical verse. Rows 63
  and 66 likewise use identical reviewed Urdu for Quran 7:54–56, and row 68
  retains the reviewed wording of Quran 17:110–111.
- In rows 63 and 66, the supplied Arabic and Bengali describe the night
  covering the day and pursuing it swiftly; Urdu preserves that sequence
  instead of the English source's reversed covering image.
- Row 54 leaves *Bismillah* in the separate three-time instruction because the
  displayed Arabic translation begins with seeking refuge, consistent with
  the reviewed parallel rows 32 and 40.
- Row 55 follows the wording of
  [Tirmidhi 3521](https://sunnah.com/tirmidhi:3521): Arabic `وعليك البلاغ`
  concerns fulfilment or reaching the intended end, not the English source's
  claim that this clause means answering prayers.
- Row 57 retains the general request and renders Arabic `المنان` as the great
  Bestower rather than the English source's request for help and
  “Compassionate.” The matching wording was checked in Abu Dawud 1495.
- Row 60 translates all three declarations and both throne descriptions in
  the frozen Arabic. The shorter cited
  [Bukhari 6345](https://sunnah.com/bukhari:6345) wording was checked and the
  frozen reference was not altered.
- Row 62 preserves a general request followed by testimony to Allah's oneness,
  as in the supplied Arabic, Bengali, and
  [Abu Dawud 1493](https://sunnah.com/abudawud:1493), rather than narrowing the
  request to help.
- Row 65 preserves the opening shift from “Our Lord is Allah” to direct
  address, as shown by its supplied Arabic and
  [Abu Dawud 3892](https://sunnah.com/abudawud:3892).
- Every genuine source-conflict decision is recorded as a field-specific
  `GLOSSARY.json` override.

## Verification and residual checks

- Ran `scripts/verify.py` on the chunk after the final naturalness edits: 17
  entries and 53 translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, and source number values.
- The target-only scan found no blank target, Bengali script, non-ASCII digit
  glyph, replacement character, or unintended Latin prose.
