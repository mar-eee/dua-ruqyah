# Urdu review: dua_infos 021–025

Scope: Bengali-source records 11–15, across five chunks. They contain
15 split parts and 20 non-null Urdu fields. Record 15 ends in chunk 025.

## Translation and structural review

- Translated each complete article in sequence, including every title,
  numbered heading, prose paragraph, pronunciation line, Quran meaning,
  and reference. The second and fifth articles continue across files.
- Compared all 15 supplied `<ar>` blocks character for character with
  their target copies. IDs, keys, frozen values, source fields, part
  numbering, and HTML tag sequence are unchanged. No Bengali script
  remains in Urdu targets.
- Ran `python -X utf8 scripts/verify.py` separately on chunks 021–025;
  each passed. A separate numeric-token audit found no added, missing,
  or changed numbers. Read the Urdu in article order for flow, honorifics,
  and faithful handling of the author's claims.

## Source-text decisions

- Record 11 begins with a paragraph on the power of supplication even
  though its title announces acceptance conditions. Its source order
  and content are preserved, without inventing a missing transition.
- Record 12, part 2: the Bengali says that an otherwise correct but
  insincere deed *is* accepted, immediately before saying sincerity
  and correctness are both necessary. Fudayl ibn Iyad's explanation
  has “not accepted” in both cases; Urdu follows that attested
  negation. See [the tafsir quotation](https://tafsir.app/althalabi/67/1).
  Fudayl is a scholar, so Urdu uses `رحمہ اللہ` rather than the source's
  companion honorific.
- Record 13: the Bengali gloss of Quran 2:152 ends “do not disobey Me.”
  The displayed Arabic asks not to be ungrateful; Urdu follows
  [Quran 2:152](https://quran.com/2:152). The quotation of 7:23 is an
  excerpt, not the complete ayah, and remains exactly as supplied.
- Record 14: the Bengali bibliography appears to garble the author
  of `Tanzih al-Shari'ah` as “Ibn Abuq.” Urdu uses Ibn Iraq, the
  [named author of that book](https://waqfeya.net/books/%D8%AA%D9%86%D8%B2%D9%8A%D9%87-%D8%A7%D9%84%D8%B4%D8%B1%D9%8A%D8%B9%D8%A9-%D8%A7%D9%84%D9%85%D8%B1%D9%81%D9%88%D8%B9%D8%A9-%D8%B9%D9%86-%D8%A7%D9%84%D8%B4%D9%86%D9%8A%D8%B9%D8%A9-%D8%A7%D9%84%D9%85%D9%88%D8%B6%D9%88%D8%B9%D8%A9-f444f0a58b2f403a917d6f491e33b8fc).
  The author's claim about the Ibrahim story is translated as his
  claim, not recast as a new independent authentication.
- Record 15, part 6: the source's surah name “কম” beside verse 33 is
  damaged. The hardship-and-supplication reference is
  [ar-Rum 30:33](https://quran.com/30:33); Urdu names ar-Rum and
  preserves the verse number. The argument's attributions to
  polytheists remain clearly attributed, not endorsed.

The intentional editorial decisions are recorded in field-specific
`GLOSSARY.json` overrides. Arabic was preserved, not silently
repaired. The verse meanings are Urdu renderings of the supplied
Arabic, not quotations from a named published Urdu translation.
This batch is translated and structurally checked; it is not a
comprehensive hadith grading or human-language review.
