# Indonesian dua_infos 003–004 review

Scope: Bangla-source records 8–12, translated into standard Indonesian
(id-ID). Both `name` and `description` are translated. Records 8 and 9 are
long source articles; every one of their 182 and 82 source paragraphs,
respectively, has a corresponding Indonesian paragraph. Records 10–12 also
retain all 22, 7, and 47 paragraphs. The source's repeated paragraph in
record 9 (paragraphs 47–48) remains repeated; it was not silently deleted.

Mechanical checks: record IDs, JSON keys, paragraph counts, and HTML tag
counts match the Bangla source snapshot at commit `eacd42a`. All 57 protected
`<ar>...</ar>` blocks match the source character for character. No Bangla
characters remain in the translated fields. The Indonesian SQLite rebuild
passed integrity and foreign-key checks, and all five rows round-tripped
exactly. This does not constitute scholarly or native-speaker review.

Selected Quran meaning checks used [Al-A'raf 7:55](https://quran.com/7/55),
[Al-Anbiya 21:87–88](https://quran.com/21/87),
[Al-Baqarah 2:186](https://quran.com/2/186),
[Ghafir 40:60](https://quran.com/40/60), and
[Al-Kahf 18:110](https://quran.com/18/110). The Indonesian passages headed
“Makna ayat” are independently written translations of meaning, **not**
verbatim quotations from a published Indonesian Quran translation. Complete
verse-by-verse verification, including Arabic script/reading comparison, is
still pending. Protected Arabic remains untouched even where the source may
need correction.

Selected hadith checks used
[Abu Dawud 1481](https://sunnah.com/abudawud:1481),
[Al-Bukhari 755](https://sunnah.com/bukhari:755),
[Al-Bukhari 6338](https://sunnah.com/bukhari:6338),
[Al-Bukhari 6502](https://sunnah.com/bukhari:6502),
[Muslim 918](https://sunnah.com/muslim:918a),
[Ibnu Majah 1753](https://sunnah.com/ibnmajah:1753),
[At-Tirmidzi 2139](https://sunnah.com/tirmidhi:2139),
[At-Tirmidzi 3370](https://sunnah.com/tirmidhi:3370),
[At-Tirmidzi 3373](https://sunnah.com/tirmidhi:3373), and
[At-Tirmidzi 3448](https://sunnah.com/tirmidhi:3448).
Other hadith wordings, numbering conventions, and source grading claims
remain pending independent, narration-by-narration review. In particular,
the source's “hasan gharib” grading for record 10's second Tirmidhi report
does not match the Darussalam grade displayed on Sunnah.com; the Indonesian
text attributes that grading to the source, not to this review.

Issues requiring source/editorial review:

- Record 8, paragraph 52: the Bangla gloss says “forgive me”, while the
  preserved Arabic `أَنْ تُعَافِيَنِيْ` asks for well-being. The Indonesian
  meaning follows the Arabic; the Bangla gloss needs correction.
- Record 8, paragraph 134: the wound report says water came out after the
  arrow was removed, as in [Al-Bukhari 4323](https://sunnah.com/bukhari:4323).
  This unusual detail was retained, not changed to “blood”.
- Record 9, paragraph 15: the source cites Al-Bukhari 755 for the three
  accepted supplications, but that number belongs to the Sa'd narrative in
  paragraphs 5–6. The Indonesian citation points instead to
  [At-Tirmidzi 3448](https://sunnah.com/tirmidhi:3448); the variant about
  parental prayer **for** versus **against** a child needs a separate
  narration-level review.
- Record 9, paragraph 21: the Bangla source omits the negation in “not
  rejected”. The Indonesian follows [Ibnu Majah 1753](https://sunnah.com/ibnmajah:1753).
- Record 9, paragraph 45: the Arabic supplication appears to contain
  transcription differences from the Muslim 918 narration. It was kept
  character for character, as required, and must be checked against a
  specified Arabic edition before correction.
- Record 10, paragraphs 14–15: the source cites At-Tirmidzi 2370 for both
  reports; that number concerns a different topic. The Indonesian references
  were corrected to 3370 and 3373, respectively. Source attribution and
  grades need editorial reconciliation.
- Honorific placement outside protected Arabic differs from the Bangla
  wording in records 8 and 9 (source/target counts: 85/88 and 35/34).
  Source honorifics attached to generic “messengers” in Quran meaning were
  not reproduced as if they were part of the verse. No honorific glyph within
  a protected Arabic block was altered. A human editor should review the
  remaining placement choices.

Translation coverage is complete for these five records, but quotation
verification and human review are **not** complete. Progress continues at
record 13 in [translation_progress.json](translation_progress.json).
