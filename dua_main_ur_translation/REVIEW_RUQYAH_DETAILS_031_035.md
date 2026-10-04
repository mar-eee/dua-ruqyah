# Urdu review: ruqyah details 031–035

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, cited primary texts, established reviewed
parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_031.json`–`035.json` | 53–60 | 8 | 8 | Reviewed; verification passed |

## Review and corrections

- Translated all eight text fields. Every topic name in this range is null and
  remains null.
- Rendered the Quranic passages directly from the supplied Arabic while keeping
  every verse number, Arabic block and normalized English citation unchanged.
- In row 54, omitted the English insertion of Pharaoh and his people from Quran
  7:119 and rendered Quran 10:81 directly as Allah nullifying the magic.
- In row 56, restored the clearly missing negation in the severe-disorientation
  symptom: the patient does not know where he is going.
- In row 58, corrected `both arms` to joining the palms before reciting and
  blowing, as confirmed by
  [Sahih al-Bukhari 5017](https://sunnah.com/bukhari:5017). The sleeping
  supplication was checked against
  [Sunan Abi Dawud 5054](https://sunnah.com/abudawud:5054).
- In row 59, restored the final loss clause of Quran 17:82. The visible `شرك`
  typo in the frozen Arabic ruqyah was resolved as `شر` in meaning after checking
  [Sahih Muslim 2186](https://sunnah.com/muslim:2186); the Arabic itself and its
  supplied Latin transliteration remain untouched.
- In row 60, omitted the stray terminal `+"` source artifact while preserving
  the complete intended sentence.
- Read every target independently as continuous Urdu and refined pronoun
  direction, agreement, clinical phrasing, list rhythm and religious terminology.

## Verification and residual checks

- Ran `python scripts/verify.py` separately on chunks 031–035 after the
  naturalness pass; all eight entries and eight fields passed.
- Preserved every Arabic block, HTML tag sequence—including the malformed source
  tags in row 53—ID, key, frozen field, category link, order, citation number,
  null, source value and all three Latin transliterations.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit outside preserved Arabic, or unintended English
  prose. Remaining Latin spans are required citations, headings and
  transliterations.
