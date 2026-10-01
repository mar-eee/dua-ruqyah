# Urdu review: dua_infos 016–020

Scope: Bengali-source record 8, parts 16–18; record 9, parts 1–10;
and record 10, part 1. These five chunks contain 14 split parts and
16 non-null Urdu fields.

## Translation and structural review

- Read the split articles in order and translated the Bengali prose in
  natural Urdu. Bengali pronunciation notes are rendered in Urdu script.
- Compared the 20 supplied `<ar>` blocks byte for byte with the target
  copies. IDs, keys, source fields, part numbering, and HTML tag
  sequence remain unchanged. No Bengali script remains in Urdu targets.
- Ran `python -X utf8 scripts/verify.py` separately for each of the
  five chunks; all passed. Independently audited identity, target
  coverage, Arabic blocks, HTML tags, and numeric differences.

## Source-text decisions

- Record 8, part 16: the chain of [Abu Dawud 96](https://sunnah.com/abudawud:96)
  names Abu Nu'amah as an intermediary, so the source's companion
  honorific is not repeated. The warning about excessive detail in
  supplication is translated without suggesting that any specific
  request is categorically forbidden.
- Record 9, part 2: the source repeats Bukhari 755 for the
  three-supplications report, but [Bukhari 755](https://sunnah.com/bukhari:755)
  is the preceding Sa'd incident. The supplications appear in
  [Abu Dawud 1536](https://sunnah.com/abudawud:1536) and
  [Tirmidhi 1905](https://sunnah.com/tirmidhi:1905). The complete
  Arwa/Sa'id account is in [Muslim 1610](https://sunnah.com/muslim:1610b);
  [Bukhari 2452](https://sunnah.com/bukhari:2452) contains its
  land-usurpation saying only. Urdu cites both for the combined account.
- Record 9, part 5: the Bengali gloss of the calamity supplication
  says “shelter me”; the report asks Allah to reward the sufferer and
  grant a better replacement. Urdu follows
  [Muslim 918](https://sunnah.com/muslim:918a). The supplied Arabic
  block has apparent transcription errors but is deliberately unchanged;
  it needs a source-level check before any Arabic amendment.
- Record 10: the two different hadiths both carry the source's
  Tirmidhi 2370 reference. The matching reports are
  [Tirmidhi 3370](https://sunnah.com/tirmidhi:3370) and
  [Tirmidhi 3373](https://sunnah.com/tirmidhi:3373). Their grading is
  not presented as settled: Tirmidhi calls the former hasan gharib,
  while the displayed Darussalam grading differs.

The intentional numeric changes are documented in field-specific
`GLOSSARY.json` `number_overrides` entries. Quran passages were
translated from the displayed Arabic without altering it. This review
does not authenticate every secondary bibliography or grading claim
in the source.
