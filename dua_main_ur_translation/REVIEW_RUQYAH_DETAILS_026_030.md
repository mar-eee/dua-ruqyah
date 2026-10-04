# Urdu review: ruqyah details 026–030

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, cited primary texts, established reviewed
parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_026.json`–`030.json` | 42–52 | 11 | 16 | Reviewed; verification passed |

## Review and corrections

- Translated all eleven text fields and five non-null topic titles. All six null
  topic names remain null.
- Rendered every Quranic passage directly and respectfully while preserving all
  supplied Arabic blocks and normalized English citations.
- In row 45, translated the first displayed Arabic and its matching `(36:29)`
  citation instead of the unrelated English sentence. Corrected the source's
  `Chapter 62` to Quran chapter 72 and documented the number override.
- In row 45, corrected the visibly corrupted claim that the Prophet circulates
  like blood: the hadith identifies Satan as the subject, as confirmed by
  [Sahih al-Bukhari 3281](https://sunnah.com/bukhari/59/90).
- In row 47, corrected the reversed rank clause: the devil who creates the
  greatest dissension is nearest to Iblis, as confirmed by
  [Sahih Muslim 2813b](https://sunnah.com/muslim:2813b).
- In row 52, corrected the accidental plural `Prophets` to the singular Prophet
  and kept the hadith wording separate from the following explanatory paragraph.
- Preserved all seven Latin transliterations verbatim and retained the established
  Urdu labels for translation and pronunciation.
- Read every target independently as continuous Urdu and refined word order,
  agreement, list rhythm, religious terminology, and awkward literal phrasing.

## Verification and residual checks

- Ran `python scripts/verify.py` separately on chunks 026–030 after the
  naturalness pass; all eleven entries and sixteen fields passed.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, order, citation number, null, source value, and transliteration.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit outside preserved Arabic, or unintended English
  prose. Remaining Latin spans are required citations and transliterations.
