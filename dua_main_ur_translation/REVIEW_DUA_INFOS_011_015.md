# Urdu review: dua_infos 011–015

Scope: Bengali-source record 8, parts 1–15 of 18, stored in five chunks.
These chunks contain 15 split parts and 16 non-null target fields. Parts
16–18 and the remaining `dua_infos` records are outside this batch.

## Translation and structural review

- Read the 15 parts in sequence so headings, rain-prayer narration and
  supplications continue naturally across file boundaries.
- Translated the Bengali prose and pronunciation notes into natural Urdu.
  Pronunciation notes are explicitly converted to Urdu script; they are not
  untouched Arabic quotations.
- Compared every supplied `<ar>` block with its Urdu-file copy: all 28
  blocks are identical. IDs, keys, source fields, nullness, part numbering
  and HTML tag sequence are unchanged. No Bengali script remains in targets.
- Ran `python -X utf8 scripts/verify.py` separately on each of
  `dua_infos_011.json` through `dua_infos_015.json`; all five passed.
  Independently compared every numeric token part by part. Only the
  documented citation/OCR corrections below differ.

## Source-text decisions

- Part 1: the Fudalah report about praising Allah and sending salawat
  before supplication is [Nasa'i 1284](https://sunnah.com/nasai:1284)
  under the current collection numbering, not source 1285.
- Part 4: OCR-separated `1/2 69-275` is written `1/269-275`, as
  with the same reference reviewed in record 7.
- Part 5: the displayed Arabic example ending `أَنْ تُعَافِيَنِيْ`
  asks for well-being, not the Bengali gloss's forgiveness. The Arabic
  was left unchanged and its Urdu meaning corrected.
- Part 6: the Buraidah report is
  [Abu Dawud 1493](https://sunnah.com/abudawud:1493); the source's
  Nasa'i 1300 citation points to a different Anas report.
- Part 7: the full Anas wording printed across parts 6–7 is
  [Nasa'i 1300](https://sunnah.com/nasai:1300); the cited
  [al-Adab al-Mufrad 705](https://sunnah.com/adab:705) gives a shorter
  variant. The following Mihjan report, including the threefold
  “he has been forgiven,” is
  [Nasa'i 1301](https://sunnah.com/nasai:1301), not 1300.
- Part 10: the full Friday rain account through the flooded Qanat valley
  is [Bukhari 933](https://sunnah.com/bukhari:933), rather than
  [Bukhari 932](https://sunnah.com/bukhari:932), which has only a short
  account. Urdu follows the full report.
- Part 12: the source note calls “Walid ibn Uqbah” correct. In
  [Muslim 1794a](https://sunnah.com/muslim:1794a), Abu Ishaq calls that
  name an error; [Muslim 1794c](https://sunnah.com/muslim:1794c) gives
  Walid ibn Utbah. Urdu states the correction without changing the
  supplied page or hadith numbers.
- Part 15: the source loosely says the Prophet ﷺ began with himself
  when mentioning someone. [Abu Dawud 3984](https://sunnah.com/abudawud:3984)
  says he began with himself when supplicating; Urdu follows that wording
  and retains the example concerning Musa عليه السلام.

All numeric changes are explained in the field-specific
`GLOSSARY.json` `number_overrides` entry for record 8. Quran passages
were translated from their displayed Arabic without changing that Arabic.
This batch review does not constitute a full authentication of every
secondary bibliographic or grading claim in the source.
