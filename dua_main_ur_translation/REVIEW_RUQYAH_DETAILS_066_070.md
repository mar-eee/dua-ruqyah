# Urdu translation review: ruqyah details 066–070

Date: 2026-09-30. Scope: English-routed records 128–141, including the
four-part record 129, all non-null topic names, and all text fields. The
assistant translated and separately reread the Urdu using the
`urdu-dua-ruqyah` skill. This is not independent human, scholarly, or
medical certification.

| Chunk | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `ruqyah_details_066.json` | 128–129 | 2 | 4 | Reviewed; verifier passed |
| `ruqyah_details_067.json` | 129–130 | 4 | 4 | Reviewed; verifier passed |
| `ruqyah_details_068.json` | 131–132 | 2 | 3 | Reviewed; verifier passed |
| `ruqyah_details_069.json` | 133–137 | 5 | 10 | Reviewed; verifier passed |
| `ruqyah_details_070.json` | 138–141 | 4 | 6 | Reviewed; verifier passed |

## Source and translation decisions

- All 17 entries and 27 non-null fields were translated from their own English
  sources; the continuing record 129 remains in its original four parts.
  Source, routing, frozen IDs, field order, nullness, Arabic, HTML tags,
  citations and source transliteration remain structurally intact.
- Record 128's black-seed reports were checked with
  [Bukhari 5687](https://sunnah.com/bukhari:5687),
  [Tirmidhi 2041](https://sunnah.com/tirmidhi:2041), and
  [Ibn Majah 3448](https://sunnah.com/ibnmajah:3448). The source calls
  [Ibn Majah 3449](https://sunnah.com/ibnmajah:3449) a Buraidah report;
  that citation actually narrates the Khalid/Ghalib/Aisha report. Urdu flags
  the mismatch while retaining the supplied number. Its extra claim that
  Ghalib recovered is kept as the author's account, not inserted into the
  Bukhari quotation.
- Record 129's discussion comes from
  [IslamQA 154257](https://islamqa.info/en/answers/154257/are-there-any-guidelines-or-conditions-with-regard-to-using-the-black-seed).
  Competing scholarly readings of “every disease,” their conditions, and
  the absence of a fixed threefold Ikhlas recitation are preserved. Quran
  [16:69](https://quran.com/16/69) and
  [46:25](https://quran.com/46/25) were checked in records 129–130.
- Record 131's Umm Qays narration was checked against
  [Bukhari 5713](https://sunnah.com/bukhari:5713). The separate Anas wording
  is in [Bukhari 5696](https://sunnah.com/bukhari:5696), where the Arabic
  says *al-qust al-bahri* (sea costus), not Indian costus; the source
  conflates them. The source's purported Jabir/Ahmad/Sunan wording and wide
  medical benefits were not independently authenticated. Both remain
  attributed, not certified treatments.
- Record 132 preserves the source's ordered recitations and all Quran
  references. Bottle size, a claimed effect of sound vibration or
  visualization, and efficacy changes through dilution or heat are the
  author's method and assertions, not established Sunnah or science.
- Record 139's supplied `Bukhari 5371` citation does **not** concern
  cupping; compare [Bukhari 5371](https://sunnah.com/bukhari:5371).
  The Urdu uses the actual relevant wording about cupping and sea costus in
  [Bukhari 5696](https://sunnah.com/bukhari:5696). This single number
  correction is recorded in the field-specific `GLOSSARY.json`
  `number_overrides`.
- The angel/cupping reports displayed under
  [Tirmidhi 2052](https://sunnah.com/tirmidhi:2052) and
  [Ibn Majah 3478](https://sunnah.com/ibnmajah:3478) have disputed or weak
  grading despite the source's “Sahih” labels. Urdu does not independently
  certify them. The “detoxification” explanation is not inserted into a
  hadith quotation. [Abu Dawud 3857](https://sunnah.com/abudawud:3857)
  supports the final cupping report's core wording.

## Editorial and safety review before publication

Translation `done` means translated, structurally checked and reread, not
that the source's medical or religious claims are approved.

- Record 130's Hebrew “honey” etymology, bee-mileage calculation and simple
  nutrition figures are source claims, not verified facts. Its blanket
  diabetes/honey avoidance is presented as the author's advice. A person's
  carbohydrate management needs individualized clinical guidance; see the
  [NHS diabetes resource](https://www.cuh.nhs.uk/patient-information/carbohydrate-awareness-and-glycaemic-index-for-people-with-diabetes/).
- Record 131 lists claimed benefits for infertility, syphilis, oral cancer,
  immune and bowel disorders, and spiritual conditions. These are retained
  as source claims and must not replace medical assessment or treatment.
- Record 133's instruction against consuming 2–5 litres in one sitting is
  an important caution: excessive water intake can contribute to low blood
  sodium, though risk depends on context. See
  [NHS hyponatraemia guidance](https://www.nhs.uk/conditions/diabetes-insipidus/treatment/).
  The author's claim that Zamzam alone never spoils is not a verified
  water-safety rule.
- Record 136 has an internal recipe conflict: jujube stones appear among
  the first three ingredients and are then added again at step 3. Urdu
  preserves the source's sequence rather than inventing a corrected recipe.
  Its skin application and black-musk/ginger suggestions need tolerability
  and clinical review.
- Records 137–138 call cupping non-invasive, risk-free, preventive and
  effective for serious disorders, while record 137 actually describes
  incisions. [NCCIH's cupping review](https://www.nccih.nih.gov/health/cupping)
  describes limited evidence beyond possible pain relief and risks including
  infection, burns, scarring, blood loss and transmission via unsterilized
  equipment. Urdu explicitly attributes the source's therapeutic promises;
  they are not approved clinical guidance.
- Record 140 clearly states that the combined programme is **not** itself
  transmitted as a complete Sunnah. Record 141's preferred prayer times
  follow that programme; their individual textual bases were not all
  authenticated in this batch.

## Final checks

- Five individual `scripts/verify.py` runs passed.
- Comparison with the pending repository versions found every non-target
  field unchanged apart from each permitted `status` change.
- HTML-tag sequences, Arabic blocks, Latin transliteration, numerical tokens
  (with the documented record-139 citation correction), and null topic names
  were checked. No Bengali characters, replacement glyphs or non-ASCII
  digit glyphs were found.
- Only chunks 066–070 and their plan rows were marked done. The local
  work-status audit was regenerated. No final database build was attempted;
  the wider Urdu translation remains incomplete.
- The commit includes only this batch, its metadata, and the small verifier
  support for documented citation-number corrections. Other pre-existing
  translations, reviews and automation state are excluded.
