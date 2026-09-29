# Urdu translation review: ruqyah details 061–065

Date: 2026-09-29. Scope: English-routed records 117–127, including all three
non-null topic names and all eleven text fields. Translation and a separate
semantic/natural-Urdu reread were performed by the assistant using the
`urdu-dua-ruqyah` skill. This is not independent human, scholarly, or medical
certification.

| Chunk | IDs | Entries | Translated fields | Translation result |
|---|---|---:|---:|---|
| `ruqyah_details_061.json` | 117–119 | 3 | 3 | Reviewed; verifier passed |
| `ruqyah_details_062.json` | 120–121 | 2 | 2 | Reviewed; verifier passed |
| `ruqyah_details_063.json` | 122 | 1 | 1 | Reviewed; verifier passed |
| `ruqyah_details_064.json` | 123–124 | 2 | 4 | Reviewed; verifier passed |
| `ruqyah_details_065.json` | 125–127 | 3 | 4 | Reviewed; verifier passed |

## Translation and source decisions

- Used the complete English source fields. The same-ID Bengali records belong
  to different material and were not substituted into this English-routed table.
- Preserved the worship lists, patient precautions, article/video titles,
  author's opinions, recipes, warnings, narration attributions, and citations.
  Refined respectful imperatives, sentence order, female-patient wording,
  measurements, and religious terminology during the separate Urdu reread.
- Records 117–121 continue the author's
  [How To Become A Raqi](https://practicalselfruqya.com/2017/08/28/how-to-become-a-raqi/).
  Claims that sins cause particular behaviours or reduce ruqyah's effects are
  retained as the author's views, not certified diagnoses or universal rulings.
- Record 117 distinguishes the author's explanation of spiritual distraction
  from the actual report in [Muslim 2702a](https://sunnah.com/muslim:2702a).
  The supplied volume/page reference `Muslim 4: 2075` is retained, not silently
  replaced with a different numbering system.
- Records 119 and 122 were checked against
  [Muslim 2186](https://sunnah.com/muslim:2186): Jibril's ruqyah and its
  supplication. The second prayer's Urdu follows the Arabic meaning, including
  the repeated invocation, rather than the defective English paraphrase.
  The first healing prayer was compared with
  [Bukhari 5743](https://sunnah.com/bukhari:5743). Its supplied Arabic wording
  and the source's Roman transliteration were not replaced with another variant.
- Record 122: the source garbles the chain and the account attributed to Aisha.
  [Al-Lalkai, report 2278](https://www.islamweb.net/ar/library/content/110/159/%D8%B3%D9%8A%D8%A7%D9%82-%D9%85%D8%A7-%D8%B1%D9%88%D9%8A-%D9%81%D9%8A-%D8%A3%D9%86-%D8%A7%D9%84%D8%B3%D8%AD%D8%B1-%D9%84%D9%87-%D8%AD%D9%82%D9%8A%D9%82%D8%A9)
  identifies Sulayman ibn Umayyah as a descendant of Urwah ibn Masud. The
  instruction concerns washing the departing woman's traces with water and
  sidr, not advising that woman to wash off magic. Urdu corrects this summary;
  no independent ruling on the report's authenticity is asserted.
- The sidr recommendation has a counterpart on
  [Ibn Baz's official site](https://binbaz.org.sa/fatwas/2253/%D8%AD%D8%B1%D9%85%D8%A9-%D9%81%D9%83-%D8%A7%D9%84%D8%B3%D8%AD%D8%B1-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D8%B3%D8%AD%D8%B1%D8%A9-%D9%88%D9%83%D9%8A%D9%81%D9%8A%D8%A9-%D9%81%D9%83%D9%87-%D8%A8%D8%A7%D9%84%D8%B7%D8%B1%D9%82-%D8%A7%D9%84%D8%B4%D8%B1%D8%B9%D9%8A%D8%A9).
  This does not verify every therapeutic claim, recitation count, or schedule
  added by the article. Those remain attributed recommendations.
- Record 123: the senna reports were compared with
  [Tirmidhi 2081](https://sunnah.com/tirmidhi:2081),
  [Tirmidhi 2048](https://sunnah.com/tirmidhi:2048), and
  [Ibn Majah 3457](https://sunnah.com/ibnmajah:3457).
  The latter confirms the narrator Abu Ubayy ibn Umm Haram, both qiblahs,
  and the senna/sannut wording. Tirmidhi's own assessments and the displayed
  Darussalam grades differ for the first two reports; the translation does not
  turn the article's blanket authenticity claim into an independent conclusion.
- Record 124: the awkward phrase “spread of hair” is rendered as hair shedding
  in its classical medical context, compared with
  [Zad Al-Maad's Arabic passage](https://www.islamicbook.ws/asol/feqh/zad-almaad-012.html).
  Historical therapeutic claims remain inside the attributed quotation.
- Record 126: the complete meaning was compared with
  [Quran 24:35](https://quran.com/24/35), and the oil report with
  [Tirmidhi 1851](https://sunnah.com/tirmidhi:1851).
  The author's Palestinian-oil preference is not inserted into the verse.
- Record 127: compared the Ajwa narration with
  [Bukhari 5445](https://sunnah.com/bukhari:5445) and
  [Muslim 2047b](https://sunnah.com/muslim:2047b).
  Corrected the second garbled narrator name to Amir ibn Sad, reporting from
  his father Sad ibn Abi Waqqas. The Companion honorific belongs to the father,
  not the son. Wider claims about other dates and later treatment remain views
  attributed in the source, not additions to the hadith.
- Recorded these decisions in field-specific `GLOSSARY.json` overrides.
  Collection names used only in citations remain normalized English, without
  inserting redundant Urdu names merely to satisfy keyword matching.

## Source issues requiring editorial review before publication

Translation `done` means translated, structurally checked, and reread for Urdu
quality. It does not mean that all source claims are safe or independently
authenticated.

- Records 123–125 contain incompatible senna recipes: a tablespoon with
  500 ml/0.5 l, a quarter teaspoon with 300 ml, and an unspecified quantity
  in one litre followed by three cups. Night-time and morning use also differ.
  The original quantities, six-day limit, and two-week interval were retained;
  no new dosage or reconciliation was invented.
- The source's no-side-effects claim conflicts with its own warnings. Its
  weight-loss, vomiting, epilepsy, and “expelling magic” claims, and its blanket
  pregnancy/nursing prohibition, need qualified clinical/editorial review.
  [NHS senna guidance](https://www.nhs.uk/medicines/senna/) describes constipation
  treatment, possible cramps and diarrhoea, and limits unsupervised duration;
  it does not validate this article's recipes or spiritual-treatment claims.
  These translations must not be treated as approved clinical instructions.
- Record 120's advice about restraining a distressed person is translated
  source material, not an emergency-care protocol. The causal and legal claims
  need appropriate clinical and religious review before publication.
- Record 123's unexplained Mustadrak/Umar attribution after an Asma narrative,
  grading claims concerning Al-Hakim/Al-Dhahabi, and its mouth-inhalation
  explanation were retained as source attributions, not independently verified.
- Record 127's “Gaktulos” etymology is retained in Urdu as a source claim;
  it has not been independently verified.
- Record 122 already contains malformed `<b>1.<b>`-style tags and an unmatched
  parenthesis in its Roman transliteration. These remain untouched under the
  structural-preservation rule. `46:29:32` was normalized to `46:29-32`, and
  stray `b` prefixes on chapter numbers were removed without changing values.

## Final checks

- All five per-file `scripts/verify.py` runs passed after the final reread.
- A separate comparison with the original pending files confirmed every
  source field, frozen value, ID, key, part, order, and other chunk metadata
  unchanged; only targets and permitted status changed.
- All four `<ar>`/`<ar1>` blocks and both Roman-transliteration passages match
  their source exactly. Every HTML tag is retained in sequence; numeric-token
  counts and values match. Null topic names remain null.
- All 14 non-null fields are filled. No Bengali script, replacement character,
  or non-ASCII digit glyph remains. Latin text is restricted to citations,
  scientific names, and the two preserved transliterations.
- Marked only chunks 061–065 done and checked their five `PLAN.md` rows.
  Regenerated `WORK_STATUS.md` from files. No final SQLite database was built;
  other required translation work remains incomplete.
- The Git commit is limited to this batch and its metadata. Pre-existing local
  translations, verifier edits, reviews, and automation changes are preserved
  and excluded. Committed status is calculated from the staged repository
  snapshot, not from other people's uncommitted local progress.
