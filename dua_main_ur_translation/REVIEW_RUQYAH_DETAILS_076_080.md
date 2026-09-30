# Urdu translation review: ruqyah details 076–080

Date: 2026-09-30. Scope: records 156–163 (8 parts and 8 non-null
translatable fields). All five files were translated and reread using the
`urdu-dua-ruqyah` skill, and each passed `scripts/verify.py`. “Done” means
translated and structurally reviewed; it is not independent scholarly or
medical certification.

| Chunk | IDs | Parts | Result |
|---|---|---:|---|
| `ruqyah_details_076.json` | 156–157 | 2 | Reviewed; verifier passed |
| `ruqyah_details_077.json` | 158 | 1 | Reviewed; verifier passed |
| `ruqyah_details_078.json` | 159 | 1 | Reviewed; verifier passed |
| `ruqyah_details_079.json` | 160–161 | 2 | Reviewed; verifier passed |
| `ruqyah_details_080.json` | 162–163 | 2 | Reviewed; verifier passed |

## Text and source decisions

- Preserved all supplied Arabic blocks and Roman transliterations verbatim.
  The final source field has malformed `<b>` tags around “Transliteration”
  and “Translation”; the target retains the same tag sequence so the
  translation does not silently change the document structure. This should
  be fixed upstream as a separate source-data task.
- Record 156's `آمَنْتُ بِاللَّهِ وَرُسُلِهِ` is plural (“His messengers”),
  not the English singular; see [Muslim 134b](https://sunnah.com/muslim:134b).
  The “First and Last, Evident and Immanent” wording follows
  [Abu Dawud 5110](https://sunnah.com/abudawud:5110), not the English “Most
  High and Most Near.” The Sayyid al-Istighfar passage was checked against
  [Bukhari 6306](https://sunnah.com/bukhari:6306).
- Record 158's Ahmad 22211 report supplicates for the young man in the
  **third person**. The supplied Arabic adapts it to the **first person**,
  although the English introduction says the reverse. Urdu corrects that
  introduction while leaving the displayed Arabic untouched. The second
  supplication was checked against
  [Abu Dawud 1551](https://sunnah.com/abudawud:1551).
- Record 159's enemy-protection prayer was checked against
  [Abu Dawud 1537](https://sunnah.com/abudawud:1537). The proposed 11
  repetitions of Ayat al-Kursi are presented as the author's advice, not
  established as prophetic practice.
- Record 162's “As-Sura 49-50” is [Ash-Shura
  42:49–50](https://quran.com/42/49-50). “Al-Baqarah 284–287” is impossible:
  [Al-Baqarah ends at 286](https://quran.com/2/286), so Urdu says 284–286.
  This sole source-number correction is documented in
  `GLOSSARY.json`'s `number_overrides`. Record 163's pain prayer was
  compared with [Muslim 2202](https://sunnah.com/muslim:2202), which has a
  related Arabic variant; the supplied Arabic was not altered.

## Editorial and safety review before publication

- Record 157 promises that a spiritual programme will make problems
  disappear; Urdu attributes this to the author rather than promising a cure.
  Record 158 discusses pornography and repeated lapses without presenting
  them as proof of a defective prayer.
- Record 159 reports apparent nocturnal sexual assault and physical injury.
  Such accounts must not automatically be assigned to jinn. Urdu explicitly
  advises medical and appropriate assault support when injury or assault is
  suspected. [NHS guidance](https://www.nhs.uk/live-well/sexual-health/help-after-rape-and-sexual-assault/)
  describes specialist medical, forensic and emotional support, including
  without an immediate police report.
- Record 160 recommends abandoning modern medicine and applying a boiled
  vinegar/herb preparation to broken or bleeding skin for 6 months. Urdu
  clearly attributes these claims and warns against stopping prescribed
  treatment or applying the mixture without medical advice.
  [NHS eczema guidance](https://www.nhs.uk/conditions/atopic-eczema/)
  describes established medical care. Record 161's forced vomiting,
  senna/rhubarb and “detox” claims likewise require medical review; the
  translation retains the author's consultation warning and does not
  certify efficacy.
- Record 162's counsel to seek forgiveness must not be read as evidence
  that infertility is caused by sin or magic. Urdu says so explicitly,
  retains specialist assessment first, and cautions on supplements.

The five files are ready as translations. The source's health and assault
advice should receive a separate qualified editorial review before
publication.
