# Urdu translation review: ruqyah details 071–075

Date: 2026-09-30. Scope: the 21 English-routed source parts in records
142–155, including all eight parts of record 149. The assistant translated
and separately reread their 21 non-null target fields using the
`urdu-dua-ruqyah` skill. This is not independent human, scholarly or
medical certification.

| Chunk | IDs | Parts | Translated fields | Result |
|---|---|---:|---:|---|
| `ruqyah_details_071.json` | 142–147 | 6 | 6 | Reviewed; verifier passed |
| `ruqyah_details_072.json` | 148–149 | 4 | 4 | Reviewed; verifier passed |
| `ruqyah_details_073.json` | 149 | 3 | 3 | Reviewed; verifier passed |
| `ruqyah_details_074.json` | 149–151 | 4 | 4 | Reviewed; verifier passed |
| `ruqyah_details_075.json` | 152–155 | 4 | 4 | Reviewed; verifier passed |

## Scriptural and source decisions

- Kept all 18 original `<ar>`/`<ar1>` blocks byte-for-byte in the target
  strings, along with the two Latin transliterations in record 152. Rendered
  the prose meaning of the Quran passages into natural Urdu without editing
  supplied Arabic or collapsing the eight-part record 149.
- Record 142's rain quotation follows [Quran 50:9](https://quran.com/50/9),
  which describes blessed water; it does not require rainwater for ruqyah.
  The rain report agrees with
  [Abu Dawud 5100](https://sunnah.com/abudawud:5100), while the Zamzam
  intention report agrees with
  [Ibn Majah 3062](https://sunnah.com/ibnmajah:3062). The olive-tree phrase
  agrees with [Quran 24:35](https://quran.com/24/35), but it does not
  establish the author's preference for oil from Palestine. The cited
  olive-oil report was compared with
  [Tirmidhi 1851](https://sunnah.com/tirmidhi:1851).
- Record 142 cites a hadith about drinking honey to insist it must be diluted
  in water. [Bukhari 5681](https://sunnah.com/bukhari:5681) mentions a drink
  of honey but does not prescribe that dilution. Urdu presents dilution as
  the shaykh's reading, not as hadith wording.
- Record 149's verse meanings were checked against the supplied Arabic,
  including [Quran 2:102](https://quran.com/2/102) and
  [2:255](https://quran.com/2/255). The English gloss of 2:102 explicitly
  inserts “Children of Israel” in a clause whose supplied Arabic says only
  “they”; Urdu follows the Arabic. The Arabic blocks and all verse numbers,
  headings and listed repetition counts remain intact.
- Record 152's two supplication meanings were checked against
  [Quran 21:87](https://quran.com/21/87) and
  [21:83](https://quran.com/21/83); both supplied Roman transliterations
  remain verbatim.
- Record 154's report about unacted and unspoken involuntary thoughts agrees
  with [Bukhari 2528](https://sunnah.com/bukhari:2528). Record 155's first
  Abu Hurayra narration agrees with
  [Muslim 132a](https://sunnah.com/muslim:132a). Its second, Ibn Abbas
  narration is **not** [Muslim 2203](https://sunnah.com/muslim:2203), which
  concerns interference in prayer; the quoted wording is in
  [Abu Dawud 5112](https://sunnah.com/abudawud:5112). Urdu corrects the
  citation to `Abu Dawud 5112`, documented in the field-specific glossary
  number override.

## Editorial and safety review before publication

Translation `done` means translated, structurally checked and reread. It
does not make the proposed ruqyah programme, dosages, benefits or diagnostics
authoritative.

- Records 142–146 specify substantial water and honey consumption, olive oil
  application, particular recitation counts and a predicted symptom course.
  The seven-/three-fold schedule and claims that worsening symptoms indicate
  progress are programme assertions, not established medical guidance.
  Worsening or persistent symptoms warrant clinical assessment rather than
  automatic escalation of the same regimen. People with diabetes or other
  dietary restrictions need individualized advice about honey.
- Records 148–150 call for vinegar, salt and other ingredients in a bath,
  and record 150 calls pain during the bath a “good sign” to endure.
  Irritation or pain should not be assumed to show healing; chemical burns
  need prompt assessment according to
  [NHS guidance](https://www.nhs.uk/conditions/acid-and-chemical-burns/).
  The source's “harmless” cupping claim is contradicted by the
  [NCCIH safety review](https://www.nccih.nih.gov/health/cupping), which
  notes infections, burns, scars, bleeding and bloodborne-disease risks.
- Record 151's proposed water spraying in ovens, washing machines and near
  other fixtures/equipment requires practical electrical and hygiene review.
  Its instruction to leave candles burning in every room is a fire risk;
  [NHS burn-prevention guidance](https://www.southwest-burncare-network.nhs.uk/_common/getdocument?id=375774)
  says never to leave burning candles unattended. Sighs, smoke, burning smells
  and dreams are the author's claimed signs of success, not verified
  diagnostic markers.
- Records 153–155 discuss intrusive religious thoughts and hearing voices.
  The source's spiritual framing is preserved as its framing, not a
  diagnosis. [NHS OCD guidance](https://www.nhs.uk/mental-health/conditions/obsessive-compulsive-disorder-ocd/symptoms/)
  explains that unwanted intrusive thoughts do not imply intent or character;
  [NHS hearing-voices guidance](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/hallucinations-hearing-voices/)
  advises medical assessment for hallucinations, urgently if voices call for
  harm. Religious support need not displace appropriate care.
- Record 152's “weekly” heading says Al-Baqarah should be read at least once
  every three days. Both heading and frequency are kept as supplied; the
  discrepancy should be resolved editorially before publication.

## Final checks

- All five individual `scripts/verify.py` runs passed after the
  natural-Urdu reread.
- Source fields, frozen IDs, keys, routing, part numbers, order, metadata and
  null topic names match the pending repository versions. Only target text
  and permitted status changed.
- HTML tag sequences, all Arabic blocks, both source transliterations and
  numeric-token counts were checked. The only intentional number change is
  record 155's documented citation correction. No Bengali script,
  replacement glyphs or non-ASCII digit glyphs remain outside frozen Arabic.
- Only chunks 071–075 and their plan rows were marked done. Work status was
  regenerated from files. No final SQLite build was attempted while other
  required Urdu work remains incomplete.
- The Git commit excludes pre-existing unrelated local translations,
  reviews and automation state.
