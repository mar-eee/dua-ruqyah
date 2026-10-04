# Urdu review: ruqyah details 041–045

Reviewed and completed on 2026-09-28 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, cited primary texts, established reviewed
parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_041.json`–`045.json` | 74–94 | 21 | 35 | Reviewed; verification passed |

## Review and corrections

- Preserved the already translated and reviewed chunks 041–042, checked their
  14 entries against the full source again, and reran their structural
  verification. Completed the seven previously blank text fields in chunks
  043–045. All topic names in IDs 88–94 are null and remain null.
- In row 88, resolved the grammatically confused English paraphrase of Ibn
  al-Qayyim's arrow analogy without changing its intended comparison: the
  figurative arrow may strike an unprotected target, miss a defended one, or
  return to its source.
- In row 89, translated the four supplied categories as `عین`, `حسد`, `نفس`
  and `نظرہ`, preserved every `<ar1>` block, and omitted only the isolated
  source-layout full stop.
- In row 90, restored the missing speaker in the blessing instruction. The
  divine-decree wording was checked against
  [Sahih Muslim 2188](https://sunnah.com/muslim:2188), and the instruction to
  pray for blessing against one's own evil eye was checked against
  [Hisn al-Muslim 244](https://sunnah.com/hisn:244). The Umm Salamah report was
  corrected from the source's specific “eye of a jinn” claim to the actual
  evil-eye wording in
  [Sahih al-Bukhari 5739](https://sunnah.com/bukhari:5739).
- In rows 91 and 93, translated Quran 2:109, 4:54 and 113:5 directly and
  completely from the displayed Arabic. This restores the omitted ending of
  Quran 2:109 and avoids importing explanatory names into Quran 4:54.
- In row 92, corrected the claim that `Nathara` is the Urdu term to the
  established `نظرِ بد`, while retaining Arabic `عین`. Restored the omitted
  ending of Quran 68:51 and rendered `عين لامة` as a harmful eye rather than
  narrowing it to an envious eye. The malformed but frozen citation markup
  `4/2<b>16.</b>` remains structurally unchanged.
- In row 94, retained the source's complete three-part distinction between
  destructive envy and permissible `غبطہ`, as well as all attributed advice
  and quotations. The jealousy-and-hatred report was checked against
  [Musnad Ahmad 1412](https://sunnah.com/ahmad/7/8). The supplied
  `(Bukhari - 2033)` citation does not contain the quoted wording about
  mistakes, forgetfulness and coercion; that wording was verified at
  [Sunan Ibn Majah 2043](https://sunnah.com/ibnmajah:2043), while the frozen
  source citation was retained for a later source-data audit.
- All source corrections and citation-only glossary exceptions for rows 88–94
  are documented in `GLOSSARY.json`. Every target was read independently as
  continuous Urdu and refined for sentence rhythm, respectful address,
  honorifics, speaker attribution, and clear handling of claims made by the
  source.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 041–045 after
  the final naturalness pass; all 21 entries and 35 translated fields passed.
- Preserved every supplied Arabic block, Latin transliteration, HTML tag
  sequence, ID, key, frozen field, category link, order, reference number,
  null and source value. Inline references remain normalized English with
  ASCII digits.
- The target-only scan found no blank target, Bengali script, replacement
  character or unintended English prose. Remaining Latin spans are required
  transliterations, source reference labels and citations.
