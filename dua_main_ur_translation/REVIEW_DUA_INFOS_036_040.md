# Urdu review: dua_infos 036–040

This batch completes record 24 (parts 1–5) and record 25 (parts 1–6), translates record 26, and begins record 27 (part 1/7). All 13 item-parts and 17 target fields in the five chunks are filled and marked `done`. Record 27 continues in chunk 041.

## Translation and preservation

- Compared each paragraph with the Bengali source for sequence, conditions, quoted speaker, and degree of certainty, then reviewed the Urdu as standalone prose. The record 24 discussion of sectarian hostility and the record 25 statements about prayer timings and virtues remain the author's exposition where the source does not give a universal ruling.
- Preserved all 10 supplied `<ar>`/`<ar1>` spans byte-for-byte, including the long istikhara dua, Quran excerpts, and Arabic dhikr. Bengali pronunciation sections were rendered in Urdu script, while keeping the `<i>`/`<b>` tag sequence unchanged. No Arabic was silently normalized.
- Compared Quran excerpts and meanings with [6:159](https://quran.com/6:159), [35:15](https://quran.com/35:15), [15:21](https://quran.com/15:21), [18:17](https://quran.com/18:17), and [1:5](https://quran.com/1:5). The source's Arabic script convention was retained; the Urdu meaning is an editorial rendering, not a quotation attributed to a named published translator.
- Record 27's Bengali title stops mid-word. Urdu uses the complete contextual heading “اللہ سے مانگنے کی اہم ترین چیزیں”; the frozen Bengali field is unchanged.

## Hadith reference and grading checks

| Location | Finding and handling |
|---|---|
| Record 25, part 4 | The Bengali cites Bukhari `1880` for Abu Hurayrah's three recommendations. [Bukhari 1880](https://sunnah.com/bukhari:1880) is unrelated; the fasting-book narration is [Bukhari 1981](https://sunnah.com/bukhari:1981). Urdu corrects the number and keeps the source's edition-specific page/book references. “Salat al-Awwabin” is presented as author commentary, not part of the verified Bukhari quotation. |
| Record 24, part 4 | [Tirmidhi 1997](https://sunnah.com/tirmidhi:1997) has the moderate-love wording, but published grading differs from the source's “sahih” label. Urdu attributes that label to the author rather than making a fresh authentication claim. |
| Record 25, part 3 | [Tirmidhi 586](https://sunnah.com/tirmidhi:586) has the Fajr-to-sunrise and Hajj/Umrah wording. Tirmidhi calls it hasan gharib, while the displayed Darussalam grade is da'if; the Bengali's hasan claim is therefore attributed to the author. The adjacent source token `2481` is preserved because its edition role is not confirmed. |

Additional content spot checks: [Bukhari 6382](https://sunnah.com/bukhari:6382) for the istikhara instruction, [Muslim 720](https://sunnah.com/muslim:720) for the joints and Duha report, [Muslim 2577](https://sunnah.com/muslim:2577a) for the long hadith qudsi, [Bukhari 844](https://sunnah.com/bukhari:844) for the post-prayer dhikr, and [Muslim 770](https://sunnah.com/muslim:770) for the night-prayer plea for guidance. The supplied Arabic is preserved, not certified as an exact match to a particular printed hadith edition.

## Checks and open items

- `scripts/verify.py` passed separately on chunks 036, 037, 038, 039, and 040. An independent per-part numeric multiset comparison found only the documented `1880 → 1981` correction; all other numeric tokens remain unchanged.
- The source's Tirmidhi `f/257` token for the repentance-prayer report and `2481` before Tirmidhi 586 need edition-level bibliographic review. They were not guessed into new hadith numbers. Some secondary grading claims in these essays were attributed but not independently authenticated.
- This review is editorial and automated. It is not a claim of scholar or native-editor sign-off; full SQLite construction remains deferred until the required remaining chunks are complete.
