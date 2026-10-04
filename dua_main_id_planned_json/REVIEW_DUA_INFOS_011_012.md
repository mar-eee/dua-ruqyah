# Indonesian dua_infos 011–012 review

Scope: Bengali-source records 33–34, translated into natural standard
Indonesian (`id-ID`). Both `name` and `description` are translated.
The 137 paragraph positions are retained (106 and 31). The two input
rows matched the Bengali snapshot at Git commit `eacd42a` before
translation.

Mechanical checks: record IDs, JSON keys, nontranslated field values,
paragraph counts, per-paragraph markup tags, and `ﷺ` counts match the
source. All three protected `<ar>` spans match character for character.
No Bengali script remains in translated fields. A temporary Indonesian
SQLite rebuild passed `integrity_check` and `foreign_key_check`; both
rows round-tripped. These checks do not establish native-speaker or
scholarly approval.

Selected Quran meaning checks used
[Fussilat 41:51](https://quran.com/41/51),
[Al-A'raf 7:180](https://quran.com/7/180), and
[Al-Ma'idah 5:75–76](https://quran.com/5/75-76).
The Indonesian is a fresh rendering of meaning, not a quotation from
an identified published translation. The supplied Arabic remains
unchanged; full letter-by-letter comparison against a specified Quran
edition, including excerpt boundaries and script convention, remains
pending.

Selected hadith checks used
[At-Tirmidzi 3382](https://sunnah.com/tirmidhi:3382),
[Muslim 2735c](https://sunnah.com/muslim:2735c),
[Muslim 2732b](https://sunnah.com/muslim:2732b),
[At-Tirmidzi 3507](https://sunnah.com/tirmidhi:3507),
[At-Tirmidzi 3525](https://sunnah.com/tirmidhi:3525),
[Al-Bukhari 1029](https://sunnah.com/bukhari:1029),
[Abu Dawud 1486](https://sunnah.com/abudawud:1486),
[At-Tirmidzi 3386](https://sunnah.com/tirmidhi:3386),
[Abu Dawud 1643](https://sunnah.com/abudawud:1643),
[At-Tirmidzi 2516](https://sunnah.com/tirmidhi:2516), and
[At-Tirmidzi 2326](https://sunnah.com/tirmidhi:2326).
These are selected checks only; other quotations, variants, numbers,
and grades need individual verification.

Issues for source or qualified scholarly review:

- Record 33, paragraph 19: the source's Muslim “no. 275” is an
  edition-dependent or incomplete reference. The matching report is
  [Muslim 2735c](https://sunnah.com/muslim:2735c); the Indonesian
  gives both the checked index and the source's citation.
- Record 33, paragraphs 44–46: the well-known report about 99 names
  and the separate enumerated list have different transmission
  histories. The source gives a scholarly dispute over the list in
  [At-Tirmidzi 3507](https://sunnah.com/tirmidhi:3507). Do not read
  the translation as an independently verified final grading of it.
- Record 33, paragraphs 51–52: the source names Rabi'ah bin Amir as
  narrator of “Ya Dzal-Jalali wal-Ikram,” while the matching wording
  in [At-Tirmidzi 3525](https://sunnah.com/tirmidhi:3525) is narrated
  from Anas. The source's edition citation is ambiguous. The
  Indonesian retains the source narrator and avoids attaching 3525
  to that attribution until the routes are reconciled.
- Record 33, paragraph 84: the Friday rain report with the
  congregation raising hands is [Al-Bukhari 1029](https://sunnah.com/bukhari:1029);
  the Indonesian also retains the source's edition reference.
- Record 33, paragraphs 89–95: wiping the face after supplication
  is explicitly presented as disputed. The displayed text of
  [At-Tirmidzi 3386](https://sunnah.com/tirmidhi:3386) calls the report
  *sahih gharib*, while the displayed Darussalam grade is *da'if*;
  the Bengali source cites additional manuscript and juristic views.
  Review the exact edition and attribution before issuing practice
  guidance. Other claims about qibla orientation, hand raising, and
  moving the index finger also need qualified school-aware review.
- Record 34, paragraphs 9–15: the author's distinction between
  calling potentially present unseen beings and calling a specific
  absent being rests on contested religious interpretation and a
  report for which the source itself cites Al-Albani's *Da'if*
  collections. Its narration and legal implications are not fully
  verified here. The polemical discussion of Christians and the
  application of *shirk* must not be used as an automatic judgment
  about individuals or a neutral description of all Christians.
- Record 34, paragraphs 20–24 and 30: confirm the “shoelace and
  salt” report, the added fallen-stick detail in the Tsauban story,
  and the alternative “early death or provision” wording against
  their exact narrations. [Abu Dawud 1643](https://sunnah.com/abudawud:1643)
  contains the pledge not to ask people, but the displayed text does
  not include the stick episode. [At-Tirmidzi 2326](https://sunnah.com/tirmidhi:2326)
  displays “provision sooner or later”; the source's alternate
  wording and its *sahih* grading require reconciliation with the
  displayed Darussalam *hasan* grade.

Translation coverage for both records is complete. Full Quran and
hadith verification, native-speaker review, and scholarly approval
are **not** complete. Progress continues at record 35 in
[translation_progress.json](translation_progress.json).
