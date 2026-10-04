# Urdu review: ruqyah details 041

Translated and reviewed on 2026-09-27 against the complete English source,
the non-aligned Bengali context, supplied Arabic, `GLOSSARY.json`, cited
primary texts, established reviewed parallels, and the project's natural-Urdu
standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_041.json` | 74–79 | 6 | 12 | Reviewed; verification passed |

## Review and corrections

- Translated all six topic names and text fields as the second through seventh
  protective measures. The Bengali database uses different row identities and
  content at IDs 74–79, so it was checked as context but was not substituted
  for the required English-routed rows.
- In row 75, rendered the Abu al-Darda report according to its verified
  congregational-prayer meaning. The exact report appears at
  [Abu Dawud 547](https://sunnah.com/abudawud:547) and
  [Nasa'i 847](https://sunnah.com/nasai:847), while the supplied citation
  names Bukhari and Muslim; that frozen citation remains unchanged.
- In row 76, corrected the source's narrow paraphrase to the cited report's
  wording: the man slept until morning without rising for prayer. This matches
  [Bukhari 3270](https://sunnah.com/bukhari:3270) and
  [Muslim 774](https://sunnah.com/muslim:774). Sa'id ibn Mansur is given
  `رحمہ اللہ`, not the source's Companion honorific.
- In row 77, resolved the English anecdote's incoherent `us/them` pronouns by
  making the speaker roles explicit: the jinn says that humans were given
  Prophetic invocations to use against jinn. The first-person claims remain
  clearly attributed to the author rather than strengthened as established
  fact. The lavatory supplication was checked against
  [Bukhari 6322](https://sunnah.com/bukhari:6322).
- In row 78, corrected English “voice” for Arabic `نفثه` to the devil's
  spitting, matching the supplied Arabic, the reviewed parallel at dua row 192,
  and [Abu Dawud 764](https://sunnah.com/abudawud:764). The citation typos
  `ai Ahmad` and `Hadil` were normalized to `Ahmad` and `Hadith`
  without changing any number or markup.
- Preserved the complete invocations and their repetitions in rows 77–79.
  Urdu labels replace the English user-interface labels, while Latin
  transliterations and normalized English references remain verbatim.
- Recorded the genuine field-specific decisions for rows 75–79 in
  `GLOSSARY.json`. Read every target independently as continuous Urdu and
  refined pronoun direction, sentence rhythm, honorifics, and devotional
  wording.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_details/ruqyah_details_041.json`
  after the final naturalness pass: all 6 entries and 12 translated fields
  passed.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, order, reference number, null, source value, and Latin
  transliteration. The chunk is marked `done` and its `PLAN.md` checkbox is
  checked.
- The target-only scan found no blank target, Bengali script, replacement
  character, or unintended Latin prose. Remaining Latin spans are HTML tags,
  required transliterations, and normalized English citations.
