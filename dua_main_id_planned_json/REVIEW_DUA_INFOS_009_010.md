# Indonesian dua_infos 009–010 review

Scope: Bengali-source records 28–32, translated into natural standard
Indonesian (`id-ID`). Both `name` and `description` are translated.
Their 107 paragraph positions are retained (32, 10, 9, 7, and 49).
The five source rows matched the Bengali JSON snapshot at Git commit
`eacd42a` before translation.

Mechanical checks: record IDs, JSON keys, nontranslated field values,
paragraph counts, per-paragraph markup tags, and `ﷺ` counts match the
source. All five protected `<ar>` spans match character for character.
No Bengali script remains in translated fields. A temporary Indonesian
SQLite rebuild passed `integrity_check` and `foreign_key_check`; all five
rows round-tripped. These checks do not establish native-speaker or
scholarly approval.

Selected Quran meaning checks used [Fussilat 41:44](https://quran.com/41/44),
[Al-Isra 17:82](https://quran.com/17/82),
[Yunus 10:57](https://quran.com/10/57),
[Al-Ankabut 29:51](https://quran.com/29/51),
[Al-Ahzab 33:56](https://quran.com/33/56), and
[Al-Baqarah 2:275](https://quran.com/2/275). Passages headed “Makna
ayat” are fresh Indonesian renderings of meaning, not quotations from
a named published translation. Full verse-by-verse Arabic, excerpt,
reading, and script comparison remains pending. Supplied Arabic was
not silently corrected.

Selected hadith checks used [Muslim 1015](https://sunnah.com/muslim:1015),
[Muslim 224a](https://sunnah.com/muslim:224a),
[Al-Bukhari 2312](https://sunnah.com/bukhari:2312),
[Al-Bukhari 2083](https://sunnah.com/bukhari:2083),
[Al-Bukhari 7429](https://sunnah.com/bukhari:7429),
[Muslim 2581](https://sunnah.com/muslim:2581),
[At-Tirmidzi 2169](https://sunnah.com/tirmidhi:2169),
[At-Tirmidzi 3540](https://sunnah.com/tirmidhi:3540),
[Abu Dawud 1047](https://sunnah.com/abudawud:1047), and
[Ibnu Majah 3818](https://sunnah.com/ibnmajah:3818).
These are selected checks only; all other reports, narration variants,
reference numbers, and grades need individual verification.

Issues for source or qualified scholarly review:

- Record 28: The discussion of ruqyah and healing presents the
  author's religious understanding and Ibnu Qayyim's reported
  experience, not established clinical efficacy or a substitute for
  medical care. Hadith quotations about divination (paragraphs 28–31)
  and their exact wording, citations, and grades remain unchecked.
- Record 29, paragraph 9: The Bengali source calls the Friday-salawat
  report [Abu Dawud 1047](https://sunnah.com/abudawud:1047) weak;
  Sunnah.com displays an Al-Albani grade of *sahih*. The Indonesian
  attributes the weak grade to the source. The source calls
  [Abu Dawud 2042](https://sunnah.com/abudawud:2042) *hasan* while
  Sunnah.com displays Al-Albani's *sahih*. Reconcile the grading
  authorities and narration variants before changing the source.
- Record 31, paragraph 5: The quoted divine saying is indexed as
  [At-Tirmidzi 3540](https://sunnah.com/tirmidhi:3540); the Bengali
  source gives edition pages but no hadith number. Paragraph 6 calls
  [Ibnu Majah 3818](https://sunnah.com/ibnmajah:3818) *sahih*, while
  Sunnah.com displays a Darussalam grade of *hasan*. The Indonesian
  attributes the grade to the source.
- Record 32, paragraphs 9–10: [Muslim 224a](https://sunnah.com/muslim:224a)
  records Ibnu Umar's response to a former governor, but does not
  establish misconduct by that man or state explicitly that Ibnu Umar
  refused to pray for him. The Indonesian distinguishes the author's
  interpretation from the hadith text. Paragraphs 8 and 36 use
  [Al-Bukhari 7429–7430](https://sunnah.com/bukhari:7429) and
  [Al-Bukhari 2083](https://sunnah.com/bukhari:2083), respectively,
  while retaining the source's different edition numbers in brackets.
- Record 32: Claims about banking, insurance, credit sales, pledged
  land, gifts, fees, wages, restitution, and repentance are presented
  as the author's discussion in its context, not universal rulings on
  modern contracts or current legal/financial advice. In particular,
  paragraphs 40–41 make strong claims about forgiveness and restoring
  others' rights that need qualified scholarly review. Readers should
  consult a qualified scholar and, for practical transactions, an
  appropriate financial or legal professional. The translation must
  not be used as a standalone ruling.

Translation coverage for these five records is complete. Full Quran
and hadith verification, native-speaker review, and scholarly approval
are **not** complete. Progress continues at record 33 in
[translation_progress.json](translation_progress.json).
