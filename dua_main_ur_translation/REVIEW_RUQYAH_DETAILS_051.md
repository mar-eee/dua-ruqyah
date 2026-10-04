# Urdu review: ruqyah details 051

Reviewed and completed on 2026-09-28 against the complete English source,
the Bengali cross-check, `GLOSSARY.json`, cited primary texts, established
reviewed parallels, and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_051.json` | 102–103 | 2 | 2 | Reviewed; verification passed |

## Review and corrections

- Translated both text fields and retained both null topic names. The Bengali
  rows with IDs 102–103 belong to unrelated material and have different
  category/subcategory routing, so they were read as the required cross-check
  but were not treated as aligned translations of these English rows.
- In row 102, preserved all eight source paragraphs distinguishing حسد from
  نظرِ بد, including the claims about expected and presently visible blessings,
  a person's own self and property, and righteous people unintentionally
  causing the evil eye. Corrected `Sahi Ibn Hunayf` to سہل بن حنیف رضی اللہ
  عنہ and clarified that the Prophet ﷺ addressed عامر بن ربیعہ رضی اللہ عنہ
  about invoking blessing for Sahl. The speaker roles and instruction were
  checked against [Muwatta Malik 50:2](https://sunnah.com/malik/50/2).
- In row 103, corrected `Abu Sa'id Al-Khudris` and `Jinr` in Urdu. The source's
  “discarded any other inappropriate invocations” does not match the cited
  primary wording: the report says that the Prophet ﷺ adopted the Mu'awwidhatayn
  and left what was other than them. Urdu follows
  [Jami' at-Tirmidhi 2058](https://sunnah.com/tirmidhi:2058) and
  [Sunan Ibn Majah 3511](https://sunnah.com/ibnmajah/31/76), while the frozen
  source citation number 2059 remains unchanged. The Umm Salama report was
  checked against [Sahih al-Bukhari 5739](https://sunnah.com/bukhari:5739).
- The concluding inference about the evil eye of jinn is explicitly presented
  as the author's conclusion rather than inserted into either hadith. Both
  conflict decisions are recorded as field-specific `GLOSSARY.json` overrides.
- Each target was reread independently as continuous Urdu and refined for
  natural sentence flow, clear contrast, correct speaker attribution,
  respectful honorifics, and consistent use of حسد, نظرِ بد, رقیہ and معوذتین.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py
  work\ruqyah_details\ruqyah_details_051.json` after the final naturalness pass;
  both entries and both translated fields passed.
- Preserved every ID, key, frozen field, category link, order, reference number,
  null and source value. Inline references remain normalized English with ASCII
  digits.
- The target-only scan found no blank target, Bengali script, replacement
  character or unintended English prose. The remaining Latin text consists
  only of the two required normalized citations.
