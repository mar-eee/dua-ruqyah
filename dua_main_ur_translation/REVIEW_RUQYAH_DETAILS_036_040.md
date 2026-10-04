# Urdu review: ruqyah details 036–040

Translated and reviewed on 2026-09-27 against the complete English source,
the supplied Arabic, `GLOSSARY.json`, cited primary texts, established reviewed
parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_036.json`–`040.json` | 61–73 | 16 | 18 | Reviewed; verification passed |

## Review and corrections

- Translated all 16 entries, including all four parts of split row 66. The two
  non-null topic names in row 72 and row 73 were translated as `تعارف` and
  `پہلی تدبیر`; all null topic names remain null.
- Preserved every Arabic block and all nine Latin transliterations verbatim.
  Quranic passages were rendered directly from the supplied Arabic, while all
  reference numbers and normalized English citations remain unchanged.
- In row 61, corrected the misleading parenthetical definition of `istihadha`
  by identifying it as bleeding outside the normal menstrual period.
- In row 62, corrected `both arms` to joining the palms before reciting,
  blowing and wiping the body, consistent with the established wording in
  [Sahih al-Bukhari 5017](https://sunnah.com/bukhari:5017) and reviewed row 58.
- In row 66, translated Quran 7:119 without the English insertion of Pharaoh
  and his people, translated Quran 10:81 as Allah nullifying the magic, and
  corrected `All-Seeing` to `خوب سننے والا` for Arabic `السميع`. The ingredient
  mistranslated as green lotus was rendered as green sidr/lote leaves; the
  Arabic formulation `سبع ورقات من السدر الأخضر` is independently reflected in
  [the cited treatment description](https://binbaz.org.sa/fatwas/12287/العلاج-الشرعي-للسحر).
- In row 67, rendered `غذاء ملكات النحل` accurately as royal jelly and avoided
  repeating the source's claim of three types when it actually lists four.
- In rows 68–69, corrected the evident `al-'ast` typo to the intended Asr time,
  matching the identical symptom wording in row 62.
- In row 71, corrected Arabic `السميع` from `All-Seeing` to `خوب سننے والا` and
  rendered `عين لامة` as a harmful evil eye rather than an accusing eye.
- In row 72, restored the dropped first-person pronouns in the threat and
  challenge dialogue and resolved the source's `sahara`/`sanir` spelling errors
  without altering the narrative.
- In row 73, restored `Ajwah` where the English repeatedly says `pressed dates`;
  the cited hadith explicitly names seven Ajwah dates in
  [Sahih al-Bukhari 5779](https://sunnah.com/bukhari/76/91).
- Read every target independently as continuous Urdu and refined agreement,
  pronoun direction, list rhythm, sensitive clinical phrasing and religious
  terminology. Unsupported medical or causal assertions remain clearly framed
  as claims made by the source rather than being strengthened by the Urdu.

## Verification and residual checks

- Ran `python scripts/verify.py` separately on chunks 036–040 after the
  naturalness pass; all 16 entries and 18 translated fields passed.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, order, citation number, null, source value and Latin
  transliteration.
- The target-only scan found no blank target, Bengali script, replacement
  character or unintended English prose. Remaining Latin spans are required
  citations, source reference labels and transliterations.
