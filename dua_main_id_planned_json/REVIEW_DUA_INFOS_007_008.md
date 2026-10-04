# Indonesian dua_infos 007–008 review

Scope: Bengali-source records 20–27, translated into natural standard
Indonesian (`id-ID`). Both `name` and `description` are translated.
All 215 paragraph positions are retained: 26, 19, 3, 15, 26, 25, 24,
and 77 respectively. The source is the Bengali JSON snapshot at Git
commit `eacd42a`; the eight input rows matched it before translation.

Mechanical checks: record IDs, JSON keys, nontranslated field values,
paragraph counts, per-paragraph markup tags, and `ﷺ` counts match the
source. All 21 protected Arabic spans (20 `<ar>` blocks and one `<ar1>`
inline span) match character for character. No Bengali script remains
in translated fields. A rebuilt Indonesian SQLite database passed
`integrity_check` and `foreign_key_check`; all eight rows round-tripped.
These checks do not establish scholarly or native-speaker approval.

Selected Quran meaning checks used [Al-Hujurat 49:10](https://quran.com/49/10),
[Al-An'am 6:159](https://quran.com/6/159),
[Fatir 35:15](https://quran.com/35/15),
[Al-Hijr 15:21](https://quran.com/15/21),
[Al-Kahf 18:17](https://quran.com/18/17), and
[Al-Fatihah 1:5](https://quran.com/1/5). The passages headed “Makna
ayat” are fresh Indonesian translations of meaning, not quotations
from an identified published Indonesian Quran translation. Full
Arabic-text comparison against a specified Quran edition, including
script and reading conventions, remains pending. Supplied Arabic was
not silently corrected.

Selected hadith checks used [Al-Bukhari 3445](https://sunnah.com/bukhari:3445),
[Al-Bukhari 1981](https://sunnah.com/bukhari:1981),
[Al-Bukhari 844](https://sunnah.com/bukhari:844),
[Muslim 2566](https://sunnah.com/muslim:2566),
[Muslim 2567a](https://sunnah.com/muslim:2567a),
[Muslim 2577a](https://sunnah.com/muslim:2577a),
[Muslim 2720](https://sunnah.com/muslim:2720),
[Muslim 2739](https://sunnah.com/muslim:2739),
[At-Tirmidzi 586](https://sunnah.com/tirmidhi:586),
[At-Tirmidzi 1997](https://sunnah.com/tirmidhi:1997), and
[At-Tirmidzi 3514](https://sunnah.com/tirmidhi:3514).
Other quoted reports, numbering schemes, and grades still need
independent narration-by-narration checking.

Issues for source or scholarly review:

- Record 20, paragraph 21: the source gives Al-Bukhari “13445” for
  the warning against exaggerated praise; the matching report is
  [Al-Bukhari 3445](https://sunnah.com/bukhari:3445). The Indonesian
  gives the checked number and records the source's number.
  Historical and barzakh-life assertions in paragraphs 13 and 20
  remain attributed to the author and need separate source checks.
- Record 21, paragraph 18: the Bengali sentence literally says that
  hostility toward a claimant of faith is a minimum requirement of
  iman, contradicting this paragraph's command to love all believers
  and the preceding discussion. The Indonesian follows the apparent
  intended negation (“tidak memusuhi”); check the author's source.
- Record 23, paragraph 0: the source prints `198` for the Al-Albani
  report; [the hadith index lists 998](https://dorar.net/h/TPrp05Qa).
  The Indonesian notes both. Paragraph 14 cites Muslim 2566 in the
  source, but the visiting-a-brother narrative is
  [Muslim 2567a](https://sunnah.com/muslim:2567a); the neighboring
  divine-shade narration is [2566](https://sunnah.com/muslim:2566).
- Record 24, paragraph 18: the Bengali source calls At-Tirmidzi 1997
  *sahih*, while Sunnah.com displays a Darussalam grade of *hasan*.
  The Indonesian attributes the grade to the source. The broader
  discussion of love, enmity, and judgments about other Muslims
  requires qualified scholarly review before use as practical advice.
- Record 25, paragraph 13: the source calls At-Tirmidzi 586 *hasan*;
  At-Tirmidzi says *hasan gharib*, while the Darussalam grade displayed
  on Sunnah.com is *da'if*. The Indonesian retains source attribution.
  Paragraph 17 cites Al-Bukhari 1880, but the three-recommendations
  report is [Al-Bukhari 1981](https://sunnah.com/bukhari:1981).
  The source's discussion of isyraq, duha timing, number of rakaat,
  and relative merit of praying at home or mosque needs scholarly
  review rather than being treated as independently verified here.
- Record 27, paragraph 19: the supplied Arabic begins
  `اَللّٰهُمَّا`, which may be a transcription irregularity. It was
  preserved exactly; compare against [Muslim 2725](https://sunnah.com/muslim:2725)
  before any source correction. Paragraph 63's Bengali meaning says
  “humiliation in the world and the hereafter,” but the supplied Arabic
  asks protection from **disgrace in this world and punishment in the
  hereafter**; Indonesian follows the Arabic. Paragraph 73 glosses
  `عَافِيَتِكَ` as “forgiveness”, whereas the Arabic and
  [Muslim 2739](https://sunnah.com/muslim:2739) concern well-being or
  protection; the Indonesian follows that meaning.
- Indonesian transliterations are readability aids, not an exact
  rendering of every Arabic phonetic distinction. For recitation, use
  the preserved Arabic and a qualified teacher or checked audio.

Translation coverage for these eight records is complete. Full Quran
and hadith verification, native-speaker review, and scholarly approval
are **not** complete. Progress continues at record 28 in
[translation_progress.json](translation_progress.json).
