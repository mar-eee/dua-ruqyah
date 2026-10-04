# Urdu review: ruqyah details 042

Translated and reviewed on 2026-09-28 against the complete English source,
the non-aligned Bengali context, supplied Arabic, `GLOSSARY.json`, cited
primary texts, established reviewed parallels, and the project's natural-Urdu
standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_042.json` | 80–87 | 8 | 16 | Reviewed; verification passed |

## Review and corrections

- Translated all eight topic names and text fields as the eighth through
  fifteenth protective measures. Bengali `ruqyah_details` IDs 80–87 belong to
  a different eye-affliction dataset, with different topic, category and
  subcategory identities, so they were checked as context but not substituted
  for the required English-routed rows.
- In row 80, followed the supplied Arabic plural `أهلي` / `لهم` as household
  or family rather than narrowing it to the English wife/her wording. The
  prayer is consistent with the reviewed parallel at dua row 394.
- In row 81, corrected the corrupt narrator name and placed the invocation
  before intercourse, as stated in
  [Bukhari 141](https://sunnah.com/bukhari:141) and the reviewed parallel at
  dua row 395. The author's personal jinn anecdote remains explicitly
  attributed to the author.
- In row 82, removed the improper Companion honorific attached to Allah and
  rendered the promised protection as a guardian appointed by Allah, matching
  [Bukhari 2311](https://sunnah.com/bukhari:2311).
- In row 83, followed [Muslim 2691](https://sunnah.com/muslim:2691): the
  remembrance is recited 100 times in a day, earns 100 good deeds, and erases
  100 bad deeds. The unsupported restriction to after Fajr and the source's
  two incorrect counts of 10 were corrected; the number decision is recorded
  in `GLOSSARY.json`.
- In row 84, used the established reviewed wording for the mosque-entry
  invocation and its day-long protection, checked against
  [Abu Dawud 466](https://sunnah.com/abudawud:466).
- In row 85, corrected English “All-Seeing” to “All-Hearing” for Arabic
  `السميع`, checked against the Arabic of
  [Ibn Majah 3869](https://sunnah.com/ibnmajah:3869).
- In row 86, kept the established reviewed translation and promise of
  guidance, sufficiency and protection, checked against
  [Abu Dawud 5095](https://sunnah.com/abudawud:5095). The citation spelling
  `At-Tirmidi` was normalized to `At-Tirmidhi` without changing any reference
  number.
- In row 87, followed the cited [Muslim 2709b](https://sunnah.com/muslim:2709b)
  report's evening timing rather than the source's unsupported morning-and-
  evening expansion. All genuine field-specific decisions were recorded in
  `GLOSSARY.json`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py work/ruqyah_details/ruqyah_details_042.json`
  after the final naturalness pass: all 8 entries and 16 translated fields
  passed.
- Preserved every supplied Arabic block, HTML tag sequence, ID, key, frozen
  field, category link, order, null, source value and Latin transliteration.
  Inline references remain normalized English with ASCII digits.
- Read every target independently as continuous Urdu and refined sentence
  rhythm, respectful address, speaker attribution, honorifics and devotional
  wording. The target-only scan found no blank target, Bengali script,
  replacement character or unintended Latin prose; remaining Latin spans are
  HTML tags, required transliterations and normalized English citations.
- The chunk is marked `done`, its `PLAN.md` checkbox is checked, and no final
  database build was attempted because later non-book scope remains pending.
