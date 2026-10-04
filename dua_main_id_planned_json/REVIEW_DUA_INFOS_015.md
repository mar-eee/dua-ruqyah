# Indonesian dua_infos 015 review

Scope: Bengali-source records 41–42, translated into natural standard Indonesian (`id-ID`). Both `name` and `description` are translated. The 24 paragraph positions are retained (2 and 22). Both input rows matched the Bengali snapshot at Git commit `eacd42a` before translation.

Mechanical checks: IDs, JSON keys, nontranslated fields, paragraph counts, per-paragraph markup, and all 14 `ﷺ` occurrences match the source. There are no protected Arabic-script spans in these two records. No Bengali script remains in translated fields. A temporary Indonesian SQLite rebuild passed integrity and foreign-key checks, and both rows round-tripped. These are mechanical checks, not native-speaker or scholarly approval.

Selected hadith wording checks used [Muslim 1163b](https://sunnah.com/muslim:1163b), [At-Tirmidzi 2485](https://sunnah.com/tirmidhi:2485), [At-Tirmidzi 3549](https://sunnah.com/tirmidhi:3549), and [Abu Dawud 1307](https://sunnah.com/abudawud:1307). The Indonesian is a fresh rendering of meaning; it is not a quotation from a named published translation.

Issues needing source or qualified scholarly review:

- Record 41, paragraph 0: the source lists multiple recommended fasting schedules, including “one day after every two days” and fasting at the start and end of each Hijri month. Verify individual hadith references and qualifications before presenting each as a specific prophetic recommendation. The translation retains the author's list.
- Record 41, paragraph 1: the author's broad historical description of the Prophet's income, same-day distribution, and his family's food supply needs individual source checking. It remains attributed to the author.
- Record 42, paragraph 5: the Bengali source has `১১২ টার` (literally “112 o'clock”), probably a typo for 11/12 o'clock. The Indonesian avoids the impossible time by saying “late at night”; correct the authoritative source. The distinction between qiyamullail and tahajud is the author's explanation, not a universally settled legal definition.
- Record 42, paragraph 9: the Bengali quotation from Amr bin Abasah ends abruptly after “then it will be.” The Indonesian renders the evident exhortation “lakukanlah,” but the exact narration and wording need verification.
- Record 42, paragraph 10: the source cites a different numbering system for the Abu Hurairah night-prayer report; the matching report appears as [Muslim 1163b](https://sunnah.com/muslim:1163b).
- Record 42, paragraph 11: the source includes maintaining kinship ties in the Abdullah bin Salam report, while the wording displayed for [At-Tirmidzi 2485](https://sunnah.com/tirmidhi:2485) does not. The translation retains the source wording; check whether the addition belongs to another route.
- Record 42, paragraph 12: the source attributes the full “disease from the body” wording to Abu Umamah and grades the report *sahih*. [At-Tirmidzi 3549](https://sunnah.com/tirmidhi:3549) displays that clause in a route from Bilal, explicitly discusses route differences, and shows a Darussalam *da'if* grade. Reconcile narrators, wording, and grading. The disease clause is a religious report, not a proven clinical treatment claim.
- Record 42, paragraphs 15 and 17–20: descriptions of the Prophet's detailed prayer length and suggested surah combinations require individual source and school-aware practice checks; the translation preserves the author's guidance without asserting an independently verified legal ruling.

Other cited narrations, grades, quotation boundaries, and legal interpretations still need full verification. Native-speaker and qualified scholarly review are pending. Translation coverage for this `dua_infos` table is complete at 42/42; see [translation_progress.json](translation_progress.json).
