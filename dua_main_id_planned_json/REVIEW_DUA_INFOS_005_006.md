# Indonesian dua_infos 005–006 review

Scope: Bengali-source records 13–19, translated into natural standard
Indonesian (`id-ID`). Both `name` and `description` are translated. The
seven records retain all 151 source paragraph positions (18, 9, 27, 7,
21, 57, and 12 respectively). Legal conclusions and historical claims
remain attributed to the source or named scholars where appropriate;
the differing juristic views in record 18 have not been flattened into
a single ruling.

Mechanical checks against the Bengali source at commit `eacd42a`:
record IDs, JSON keys, nontranslated values, per-paragraph markup tags,
and salawat glyph counts match. All nine protected Arabic spans (seven
`<ar>` blocks and two `<ar1>` inline spans) match character for
character. No Bengali-script characters remain in translated fields.
The Indonesian SQLite rebuild passed `integrity_check` and
`foreign_key_check`; all seven translated rows round-tripped exactly.

Selected Quran meaning checks used [Al-A'raf 7:23](https://quran.com/7/23),
[Al-Baqarah 2:152](https://quran.com/2/152),
[Az-Zumar 39:3](https://quran.com/39/3),
[Yunus 10:18](https://quran.com/10/18),
[Yusuf 12:106](https://quran.com/12/106), and
[Al-A'raf 7:204](https://quran.com/7/204). Passages labelled
“Makna ayat” are fresh Indonesian renderings of meaning, **not**
verbatim text from an identified published translation. Full
verse-by-verse checking of every citation and of Arabic orthography
against a specified Quran edition remains pending; protected Arabic
was not silently changed.

Selected hadith checks used [Al-Bukhari 7405](https://sunnah.com/bukhari:7405),
[Al-Bukhari 4920](https://sunnah.com/bukhari:4920),
[Al-Bukhari 5025](https://sunnah.com/bukhari:5025),
[Muslim 2699a](https://sunnah.com/muslim:2699a),
[Muslim 373](https://sunnah.com/muslim:373),
[Ibnu Majah 3827](https://sunnah.com/ibnmajah:3827),
[Ibnu Majah 215](https://sunnah.com/ibnmajah:215),
[At-Tirmidzi 3486](https://sunnah.com/tirmidhi:3486),
[At-Tirmidzi 3583](https://sunnah.com/tirmidhi:3583),
[Abu Dawud 1501](https://sunnah.com/abudawud:1501),
[Abu Dawud 1502](https://sunnah.com/abudawud:1502), and
[An-Nasa'i 1010](https://sunnah.com/nasai:1010).
This is a selected check, not a complete narration-by-narration review.

Issues for editorial or scholarly review:

- Record 14: the Bengali source calls the report in Ibnu Majah 3827
  *hasan*, while Sunnah.com displays a Darussalam grade of *da'if*.
  The Indonesian explicitly attributes the grade to the source.
- Record 15: the source's “কম:৩৩” in the distress-verse list is
  ambiguous; [Ar-Rum 30:33](https://quran.com/30/33) fits the context,
  unlike Al-Qamar 54:33. The same source gives Luqman 31:23, which
  does not match the topic; the Indonesian uses
  [Luqman 31:32](https://quran.com/31/32). Confirm both corrections
  against the author's intended references.
- Record 17: source citation Al-Bukhari 7091 does not contain the
  “two people worth envying” report; the Indonesian cites
  [Al-Bukhari 5025](https://sunnah.com/bukhari:5025). The source calls
  Ibnu Majah 215 *sahih*, while the displayed Darussalam grade is
  *hasan*; the Indonesian keeps the source attribution.
- Record 18: source citation Abu Dawud 282 for finger-counting was
  corrected to 1502; Yusairah's fingertip report is At-Tirmidzi 3583
  and Abu Dawud 1501, not the repeated At-Tirmidzi 3486. The
  [An-Nasa'i 1010](https://sunnah.com/nasai:1010) wording visible in
  this check confirms repetition of Al-Ma'idah 5:118 during night
  prayer, but does **not** explicitly establish the source's added
  claim that the verse was repeated in both bowing and prostration.
  The Indonesian labels that detail “menurut sumber”; it needs a
  narration-level check. All rulings on purity, Quran recitation,
  touching the mushaf, and non-Arabic supplication require qualified
  scholarly review before being presented as practical guidance.
- Record 19: the source cites Az-Zukhruf 43:1 for an admission that
  Allah is Creator, but [43:9](https://quran.com/43/9) matches that
  point. The Indonesian uses 43:9. The source's distinction between
  *ubudiyah* and *ibadah* is presented as its explanation, not as a
  universally agreed lexical definition.
- Record 18's reference to “bahasa ibu” localizes the Bengali source's
  audience-specific “Bengali” to Indonesian readers without changing
  the author's stated legal distinction.

Translation coverage for these seven records is complete. Full Quran
and hadith verification, native-speaker review, and scholarly approval
are **not** complete. Progress continues at record 20 in
[translation_progress.json](translation_progress.json).
