# Urdu review: ruqyah details 052

Translated, reviewed, and completed on 2026-09-28 against the complete English
source, the Bengali cross-check, supplied Arabic, `GLOSSARY.json`, cited primary
texts, established reviewed parallels, and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_052.json` | 104 | 1 | 1 | Reviewed; verification passed |

## Review and corrections

- Translated the complete introduction and all five treatment methods, including
  every heading, instruction, narration, explanatory paragraph, quoted meaning,
  and label. The null topic name remains null.
- Bengali row 104 belongs to unrelated marriage material and routes to category
  7/subcategory 53, whereas the English source row routes to category
  5/subcategory 85. It was read as the required cross-check but not treated as
  an aligned translation.
- Restored the Sahl ibn Hunayf incident from
  [Muwatta Malik 50:2](https://sunnah.com/malik/50/2): the washed parts are the
  hands, elbows, knees, ends of the feet, and inside the lower garment, and the
  Prophet's instruction includes invoking blessing. The evident crossed-hand
  error for the right foot in the later washing directions was also corrected.
- Rendered the washing command in accordance with
  [Sahih Muslim 2188](https://sunnah.com/muslim:2188) and the wudu report in
  accordance with
  [Sunan Abi Dawud 3880](https://sunnah.com/abudawud:3880).
- The first displayed ruqyah follows
  [Sahih Muslim 2186](https://sunnah.com/muslim:2186), treating the phrase as
  every soul or envious eye rather than a separate third object. The second
  displayed formula agrees with
  [Sahih Muslim 2185](https://sunnah.com/muslim:2185).
- The final healing supplication follows
  [Sahih al-Bukhari 5743](https://sunnah.com/bukhari:5743) and
  [Sahih Muslim 2191a](https://sunnah.com/muslim:2191), without the English
  source's unsupported first-person “heal me.” These conflict decisions are
  recorded in the field-specific `GLOSSARY.json` override
  `ruqyah_details.text.104`.
- Reread the target independently as continuous Urdu and refined its sentence
  flow, gender agreement, instructions, speaker roles, honorifics, devotional
  wording, and consistent use of `نظرِ بد` and `رقیہ`.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py
  work\ruqyah_details\ruqyah_details_052.json` after the final target edits;
  the entry and translated field passed.
- Preserved every ID, key, frozen field, category link, order, null, Arabic
  block, transliteration value, HTML tag sequence, and source number value.
  Inline references remain normalized English with ASCII digits.
- The target-only scan found no blank target, Bengali script, replacement
  character, non-ASCII digit glyph, or unintended Latin prose. Remaining Latin
  text is confined to the three preserved transliterations and normalized
  English references.
