# Urdu review: dua_infos 026–030

Five chunks are translated: record 16 (one part), record 17 (one part), and record 18 (parts 1–9 of 10). All 11 parts and all 14 target fields in this batch are filled and marked `done`. Record 18 continues in chunk 031; this review does not cover that final part.

## Language and meaning

- Rendered the Bengali source as readable Urdu prose, retaining its sequence of points, examples, qualifications, and bibliographic references. Bengali pronunciation material was rendered in Urdu script rather than copied phonetically in Bengali.
- Preserved the single supplied `<ar>` Quran block in 027 byte-for-byte and kept the HTML structure intact. The adjacent Urdu meaning of Quran 7:204 was checked against [Quran 7:204](https://quran.com/7:204). No Arabic was invented or edited.
- Kept juristic views in record 18 attributed to the source author or named scholars. The sections on ritual purity, touching the mushaf, and supplication during prayer describe differing views; the Urdu does not present a contested view as a universal ruling.
- Retained the source's explicit weakness or qualification labels for reports where relevant. A source claim of *sahih* is attributed to its author when independently published grading differs.

## Reference checks and documented corrections

| Record / part | Source issue | Urdu handling |
|---|---|---|
| 17 | Bengali cites Bukhari 7091 for Ibn Umar's “envy only two” narration, but [7091](https://sunnah.com/bukhari:7091) is unrelated. | Cites the matching [Bukhari 5025](https://sunnah.com/bukhari:5025). The source's Indian-edition token `21123` remains unchanged because its OCR cannot be resolved confidently. |
| 18 / 2 | Abu Dawud 282 is cited for counting dhikr on the fingers. | Cites [Abu Dawud 1502](https://sunnah.com/abudawud:1502). |
| 18 / 2 | Tirmidhi 3486 is repeated for the complete Yusayrah narration, whereas its full wording is elsewhere. | Keeps [Tirmidhi 3486](https://sunnah.com/tirmidhi:3486) for the earlier Abdullah ibn Amr report, and cites [Tirmidhi 3583](https://sunnah.com/tirmidhi:3583) for Yusayrah. |
| 18 / 9 | The cited prayer-time account varies by collection. | Ruku/sujud detail is expressed as a variant report: [Nasa'i 1010](https://sunnah.com/nasai:1010) has the repeated verse, while the fuller [Musnad Ahmad version](https://hadithweb.com/ahmad:21538) contains the ruku/sujud detail. |

Other spot checks included the gathering for Quran study in [Muslim 2699](https://sunnah.com/muslim:2699a), Aisha's report on remembrance at all times in [Muslim 373](https://sunnah.com/muslim:373), and the prohibition of Quran recitation in ruku/sujud in [Muslim 479](https://sunnah.com/muslim:479a). These checks support the quoted content and do not imply that every secondary citation in the long source essay was independently authenticated.

## Mechanical checks and open item

- `scripts/verify.py` passed separately on all five JSON files: no structure, Arabic-block, tag, or status errors.
- An independent per-part numeric multiset comparison found no number changes except exactly `7091 → 5025` in record 17 and `282 → 1502`, `3486 → 3583` in record 18 part 2. Both fields are documented in `GLOSSARY.json` `number_overrides`.
- The unresolved `Indian ed. 21123` in record 17 needs edition-level bibliographic review if a normalized reference is required. It is not silently guessed here.
- This is an editorial and automated review, not a claim of formal scholar or native-editor sign-off. The final database build remains deferred until the remaining tables/chunks are complete.
