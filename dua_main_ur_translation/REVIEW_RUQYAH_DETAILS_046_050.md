# Urdu review: ruqyah details 046–050

Reviewed and completed on 2026-09-28 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, cited primary texts, established reviewed
parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_046.json`–`050.json` | 95–101 | 7 | 7 | Reviewed; verification passed |

## Review and corrections

- Translated every user-visible field in the five chunks. All seven topic
  names are null in the source and remain null; all seven text fields are now
  complete.
- In row 95, preserved both complete versions of the Sahl ibn Hunayf incident
  because the source presents both as separate narrations. The washing
  procedure was checked against
  [Muwatta Malik](https://sunnah.com/urn/417740), and the supplied high-place
  report was checked against the matching narration indexed at
  [Dorar](https://dorar.net/h/Id8L4DRs).
- In row 96, restored the compressed chain correctly: a freed slave of the
  family of Az-Zubayr reports from Az-Zubayr ibn al-Awwam, who narrates the
  Prophetic statement. This was checked against
  [Musnad Ahmad 1430–1432](https://sunnah.com/ahmad/7/25).
- In row 97, retained all supplied symptom claims and their original order,
  including the two separately listed headache entries, while translating
  the medical terms naturally and without adding new diagnoses or promises.
- In row 99, corrected the corrupted exegete names `Qaada` and `As-suday` to
  Qatadah and al-Suddi. The mechanically garbled sentence about Quran 12:68
  was restored as the stated explanation that entering by separate gates
  fulfilled Yaqub's concern about the evil eye; the underlying commentary was
  checked in [Tafsir Ibn Kathir](https://quran-tafsir.net/katheer/sura12-aya68.html).
- In row 100, corrected obvious transcription errors in names and citation
  labels without changing any reference number: `Jabiri` to Jabir,
  `Al-Bukhati` to Al-Bukhari, `Ruga` to Ruqya, and `Sahin` to Sahih. Jabir's
  attribution for the report about deaths after divine decree was checked at
  [Dorar](https://dorar.net/h/LGYs8bXz), and the grave-and-cooking-pot report
  at [Dorar](https://dorar.net/h/hJ0mZsVS?osoul=1).
- In row 101, normalized the corrupted book titles and restored `al-Abtar`,
  the short- or mutilated-tailed snake, in place of the source's accidental
  `Albatross`; the snake wording was checked against
  [Sunan Ibn Majah 3535](https://sunnah.com/ibnmajah:3535). The English also
  turns Ibn al-Qayyim's general list of ways souls may exert influence into an
  incoherent claim that protective prayers, ruqyah and refuge verses cause the
  evil eye. Urdu follows the underlying Arabic discussion in
  [Zad al-Ma'ad](https://tafsir.app/ibn-alqayyim/113/5) and does not introduce
  that error.
- Every source correction and citation-only glossary exception for rows
  95–101 is documented in `GLOSSARY.json`. Each target was reread as
  continuous Urdu and refined for sentence rhythm, speaker attribution,
  honorifics, and consistent use of `نظرِ بد`, `عین`, `رقیہ`, `قضا` and
  `قدر`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 046, 047, 048,
  049 and 050 after the final naturalness pass; all seven entries and seven
  translated fields passed.
- Preserved every supplied Arabic block, HTML tag sequence, ID, key, frozen
  field, category link, order, reference number, null and source value.
  Inline references remain normalized English with ASCII digits.
- The target-only scan found no blank target, Bengali script, replacement
  character or unintended English prose. Remaining Latin spans are required
  audio labels, HTML tag names and normalized citations.
