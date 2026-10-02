# Urdu review — dua_infos 041–045

Scope: five chunks, 16 item-parts, 21 translated fields (16 descriptions and five names), spanning records 27–32. Record 27 ends in 042, record 28 ends in 044, and record 32 continues in 046. Every target field is filled; all 15 protected Arabic spans are copied unchanged. Source, frozen values, identifiers, part boundaries and HTML tag sequences are preserved. Pronunciations use Urdu script and references use ASCII numerals.

## Semantic and source review

- The source meaning of the Busr ibn Arta'ah prayer in 042 says disgrace in both worlds, but its Arabic asks protection from *disgrace in this world and punishment in the Hereafter*. The Urdu meaning follows the Arabic.
- The source meaning of Muslim 2739 in 042 calls `عَافِيَتِكَ` forgiveness. It means well-being/afiyah, and Urdu follows the unchanged Arabic. [Sahih Muslim 2739](https://sunnah.com/muslim:2739).
- The source gives Muslim 2654 for the hearts-and-obedience prayer. That number is a different report; the matching report is [Sahih Muslim 2655](https://sunnah.com/muslim:2655), so Urdu corrects only that reference. [Compare 2654](https://sunnah.com/muslim:2654). This is logged in `GLOSSARY.json` as a number override.
- The Quran verse meanings in records 28 and 29 were checked against [41:44](https://quran.com/41/44), [17:82](https://quran.com/17/82), [10:57](https://quran.com/10/57), [29:51](https://quran.com/29/51), and [33:56](https://quran.com/33/56). The supplied Arabic fragments remain byte-for-byte unchanged.
- Broad claims in the source about Quranic ruqyah curing all bodily illness and the limits of medicine are rendered as the author's or Ibn al-Qayyim's teaching and personal account, not as an established medical guarantee. This does not remove the source's argument. The three permitted-ruqyah conditions and warnings about divination remain complete.
- The source labels the Friday salawat report at Abu Dawud 1047 weak. The Urdu explicitly attributes that grade to the source because [the modern listing of Abu Dawud 1047](https://sunnah.com/abudawud:1047) records a different grading; this review does not settle the scholarly grading.
- The source's long halal-income hadith cites a hard-to-parse older/Indian-edition reference containing 1703. The Urdu preserves those source numbers. Its text matches [Sahih Muslim 1015](https://sunnah.com/muslim:1015) in common modern numbering. The source's categorical commentary that a haram earner's prayer is never accepted is attributed to the author; the hadith itself asks how such a prayer could be accepted.
- The source's references and grading labels elsewhere are retained as author/source attributions, not independently certified hadith authentication. No scholar sign-off is claimed.

## Verification

Each of `dua_infos_041.json` through `dua_infos_045.json` passes `python -X utf8 scripts/verify.py work/dua_infos/<filename>`. Arabic spans, HTML sequence, field/key preservation, Bengali-script leakage, and numeric consistency were checked; the one deliberate citation-number correction is documented above. The next untranslated chunk is `dua_infos_046.json`.
