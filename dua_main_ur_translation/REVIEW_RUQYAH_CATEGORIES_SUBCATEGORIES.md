# Urdu review: ruqyah categories and subcategories

Date: 2026-10-04. Scope: the one `ruqyah_categories` chunk and all four
`ruqyah_subcategories` chunks, comprising 178 English-routed `name` fields.
The assistant reviewed the complete English source, Bengali context,
`GLOSSARY.json`, and the project's natural-Urdu standard. Every target was
then reread independently as an Urdu app heading.

| Chunk | IDs | Fields | Result |
|---|---|---:|---|
| `ruqyah_categories_001.json` | 1–15 | 15 | Reviewed; verifier passed |
| `ruqyah_subcategories_001.json` | 1–50 | 50 | Reviewed; verifier passed |
| `ruqyah_subcategories_002.json` | 51–100 | 50 | Reviewed; verifier passed |
| `ruqyah_subcategories_003.json` | 101–150 | 50 | Reviewed; verifier passed |
| `ruqyah_subcategories_004.json` | 151–163 | 13 | Reviewed; verifier passed |

## Source and language review

- English is the routed source for both tables. The Bengali category table
  uses a substantially different category arrangement, and the Bengali
  subcategory table has only 117 rows whose same IDs often describe unrelated
  subjects. It was read as context but was not substituted for the routed
  English records.
- Refined 38 target headings. The changes restore omitted meaning such as the
  7-day detoxification programme, the existence of jinn, bloodletting, the
  exact sexual-health distinction in *Sihr ar-Rabt*, and the plural Ajwa
  dates. They also replace mechanical phrases with natural headings, including
  self-ruqyah treatment, Satanic temptation, practitioner commitment, and the
  method of reciting ruqyah over water, oil, and honey.
- Standardized relevant Islamic terms and distinctions: `سحر`, `رقیہ`,
  `نظرِ بد`, `حسد`, `راقی`, `حجامہ`, `فصد`, `سنا مکی`, and `قسط ہندی`.
  In particular, “jealousy” remains `حسد`, not the positive Urdu concept
  `رشک`.
- No title contains supplied Arabic scripture or a cited primary-text passage,
  and no genuine primary-source conflict arose. Therefore no new field-specific
  glossary override was required.
- Preserved all IDs, keys, types, category links, source strings, ordering,
  row counts, ASCII number values, and `done` statuses. Only target `name`
  values and the review ledger in `PLAN.md` were changed.

## Verification and residual checks

- Ran `scripts/verify.py` separately on all five files after their final edits;
  every file passed with 178/178 translated fields.
- The target-only scan found zero blank targets, Bengali characters,
  unintended Latin prose, non-ASCII digit glyphs, or replacement characters.
- Updated `PLAN.md` to record the already existing complete review coverage of
  duas, ruqyah instants, and ruqyah details, plus this five-chunk taxonomy
  batch. No postponed book work was started and no final database was built.
