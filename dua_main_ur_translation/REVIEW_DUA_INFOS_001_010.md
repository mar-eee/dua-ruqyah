# Urdu review: dua_infos 001–010

Scope: the first 10 Bengali-source chunks, covering records 1–7, 30 split
parts, and 37 non-null Urdu target fields. This is a translation review of
these chunks only; the remaining 60 `dua_infos` chunks and the final database
build are still pending.

## Review performed

- Translated the full prose and names into natural Urdu, then read the split
  parts in order to check transitions and headings.
- Kept all 21 marked `<ar>`/`<ar1>` Arabic blocks byte-for-byte identical
  to their supplied source blocks. Preserved field keys, IDs, part numbering,
  nullness, and HTML tag sequences. Bengali-script pronunciation notes were
  rendered in Urdu script; they were not silently left as Bengali.
- Ran `python -X utf8 scripts/verify.py` separately on each of
  `dua_infos_001.json` through `dua_infos_010.json`; all 10 passed.
  Compared every marked Arabic block directly as a second check.

## Source-text decisions

- Record 1: the Bengali gloss of Quran 17:110 says “praise Allah or
  al-Rahman,” but the verse says to **call upon** Him by either name. Urdu
  follows [Quran 17:110](https://quran.com/17/110).
- Record 2: the source cites Tirmidhi 2481 for the Fajr-to-sunrise dhikr
  and two-rak'ah report. [Tirmidhi 2481](https://sunnah.com/tirmidhi:2481)
  concerns clothing; the quoted report is
  [Tirmidhi 586](https://sunnah.com/tirmidhi:586). Urdu corrects the hadith
  number. The source calls the report hasan; Tirmidhi says *hasan gharib*
  on that page, while Darussalam grades that chain da'if. The Urdu does
  not present a unanimous grading.
- Record 5: the Bengali summary of Muslim 202 changes the divine answer.
  Urdu follows [Muslim 202](https://sunnah.com/muslim:202): Allah will
  please the Prophet ﷺ regarding his Ummah and will not displease him.
- Record 5: Bukhari 6383 calls the person prayed for “Ubaid Abi 'Amir.”
  Urdu identifies him as Abu Amir Ubaid, rather than treating “Ubaid” and
  “Abu Amir” as two people. See
  [Bukhari 6383](https://sunnah.com/bukhari:6383).
- Record 7: the source's `1/2 69-275` and `111 33` are OCR-split
  references. Urdu uses `1/269-275` for *Jami al-Ulum wa al-Hikam* and
  `11133` for *Musnad Ahmad*. The latter is independently identifiable as
  [Ahmad 11133](https://hadeethenc.com/en/browse/hadith/5100); the former
  is supported by the [Arabic source discussion](https://d1.islamhouse.com/data/ar/ih_books/single4/ar_Terms_of_prayer.pdf).
  These numeric corrections are declared in `GLOSSARY.json`'s
  `number_overrides`.

Quoted Quran wording was rendered in Urdu to match the supplied Arabic;
the Arabic itself was never normalized or edited. Other inherited
bibliographic details remain as supplied unless documented above.
Automated checks cannot certify every narrator, grading, or legal inference;
the review does not claim full scholarly authentication of all cited reports.
