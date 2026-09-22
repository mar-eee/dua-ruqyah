# Japanese Dua Translation Work Plan

## Overview

- Main workspace: `dua_main_ja_planned_json`
- Main dua folder: `dua_main_ja_planned_json/tables/duas`
- Total dua rows: `1001`
- Total dua chunks: `30`
- Final rebuilt DB: `dua_main_ja_rebuilt.sqlite`

## Current Translation Rule

Follow `README.md`.

The Japanese should be natural, clear, respectful, and easy to understand. It should feel human and polished, not machine-translated.

Translate these top-level fields:

- `name`
- `content`
- `translation`
- `note`

Keep these fields unchanged:

- `id`
- `groups`
- `uthmani`
- `indopak`
- `clean`
- `transliteration`
- `audio`
- `cat_id`
- `subcat_id`

Reference rule:

- `reference` must stay English.
- Do not translate `reference` into Japanese.
- If a source reference is Bengali or another language, use the matching English DB reference when available.

## Status Fill-Up Instruction

Every time a file is translated, update this plan before finishing the task.

Do these four things every time:

1. Change that file's row in **Dua Chunk Status** from `pending` to `complete`.
2. Add a short note in the row, for example: `translated; references kept English`.
3. Add a detail block under **Work Status Details**.
4. Also update `dua_main_ja_planned_json/_database_metadata.json` under `work_status`.

Use this detail format every time:

```md
### Completed: `duas_XXX.json`

- ID range: `START-END`
- Rows: `COUNT`
- Completed on: `YYYY-MM-DD`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`
```

For metadata, use this meaning:

- `language`: `Japanese`
- `status`: `translated`
- `translated_fields`: `name`, `content`, `translation`, `note`
- `reference_rule`: references are English and not translated
- `unchanged_fields_by_instruction`: IDs, Arabic fields, `groups`, `transliteration`, audio, and category links
- `rows`: number of rows in the JSON file
- `id_range`: first ID to last ID
- `updated_at`: completion date
- `note`: short human note about what was done

## Completed Non-Dua Tables

| File | Rows | Status |
|------|------|--------|
| `tables/categories/categories_001.json` | 44 | complete; titles improved |
| `tables/subcategories/subcategories_001.json` | 118 | complete |
| `tables/dua_infos/dua_infos_001.json` | 21 | complete |
| `tables/dua_infos/dua_infos_002.json` | 21 | complete |
| `tables/ruqyah_categories/ruqyah_categories_001.json` | 15 | complete; titles improved |
| `tables/sections/sections_001.json` | 21 | complete; titles improved |
| `tables/ruqyah_instants/ruqyah_instants_001.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_002.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_003.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_004.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_005.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_006.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_007.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_008.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_009.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_010.json` | 29 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_001.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_002.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_003.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_004.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_005.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_006.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_007.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_008.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_009.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_010.json` | 20 | complete; translated, references kept English |
| `tables/ruqyah_subcategories/ruqyah_subcategories_001.json` | 163 | complete; titles translated, terms aligned with categories |
| `tables/ruqyah_videos/ruqyah_videos_001.json` | 74 | complete; translated from Bengali (no EN rows), authors in katakana |
| `tables/drawer_items/drawer_items_001.json` | 6 | complete; titles, hero lines and content JSON translated |
| `tables/ids/ids_001.json` | 1001 | n/a; numeric only, nothing to translate |
| `tables/drawer_item_actions/drawer_item_actions_001.json` | 0 | n/a; table is empty |
| `tables/books/books_001.json` | 3 | skipped by instruction (book tables excluded) |
| `tables/book_details/book_details_001.json` | 86 | skipped by instruction (book tables excluded) |

## Dua Chunk Status

| Chunk | ID Range | Rows | Status | Notes |
|------|----------|------|--------|-------|
| `duas_001.json` | 1-34 | 34 | complete | translated; references kept English |
| `duas_002.json` | 35-68 | 34 | complete | translated; references kept English |
| `duas_003.json` | 69-102 | 34 | complete | translated; references kept English |
| `duas_004.json` | 103-136 | 34 | complete | translated; references kept English |
| `duas_005.json` | 137-170 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_006.json` | 171-204 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_007.json` | 205-238 | 34 | complete | translated; references kept English |
| `duas_008.json` | 239-272 | 34 | complete | translated; references kept English |
| `duas_009.json` | 273-306 | 34 | complete | Japanese complete; Indonesian complete 2026-09-07; references kept English; transliteration copied from EN |
| `duas_010.json` | 307-340 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_011.json` | 341-374 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_012.json` | 375-408 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_013.json` | 409-442 | 34 | pending |  |
| `duas_014.json` | 443-476 | 34 | pending |  |
| `duas_015.json` | 477-510 | 34 | pending |  |
| `duas_016.json` | 511-544 | 34 | pending |  |
| `duas_017.json` | 545-578 | 34 | complete | Indonesian complete; references kept English |
| `duas_018.json` | 579-612 | 34 | complete | Indonesian complete; references kept English |
| `duas_019.json` | 613-646 | 34 | complete | Indonesian complete; references kept English |
| `duas_020.json` | 647-680 | 34 | complete | Indonesian complete; references kept English |
| `duas_021.json` | 681-714 | 34 | complete | Indonesian complete; references kept English |
| `duas_022.json` | 715-748 | 34 | complete | Indonesian complete; references kept English |
| `duas_023.json` | 749-782 | 34 | complete | Indonesian complete; references kept English |
| `duas_024.json` | 783-816 | 34 | complete | Indonesian complete; references kept English |
| `duas_025.json` | 817-850 | 34 | complete | Indonesian complete; references kept English |
| `duas_026.json` | 851-884 | 34 | complete | Indonesian complete; references kept English |
| `duas_027.json` | 885-918 | 34 | complete | Indonesian complete; references kept English |
| `duas_028.json` | 919-952 | 34 | complete | Indonesian complete; references kept English |
| `duas_029.json` | 953-986 | 34 | complete | Indonesian complete; references kept English |
| `duas_030.json` | 987-1001 | 15 | complete | Indonesian complete; references kept English |
| `duas_013.json` | 409-442 | 34 | complete | translated; references kept English |
| `duas_014.json` | 443-476 | 34 | complete | translated; references kept English |
| `duas_015.json` | 477-510 | 34 | complete | translated; references kept English |
| `duas_016.json` | 511-544 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_017.json` | 545-578 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_018.json` | 579-612 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_019.json` | 613-646 | 34 | complete | translated; references kept English |
| `duas_020.json` | 647-680 | 34 | complete | translated; references kept English |
| `duas_021.json` | 681-714 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_022.json` | 715-748 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_023.json` | 749-782 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_024.json` | 783-816 | 34 | complete | translated; references kept English |
| `duas_025.json` | 817-850 | 34 | complete | translated; references kept English |
| `duas_026.json` | 851-884 | 34 | complete | translated; references kept English |
| `duas_027.json` | 885-918 | 34 | complete | translated; references kept English |
| `duas_028.json` | 919-952 | 34 | complete | translated; references kept English |
| `duas_029.json` | 953-986 | 34 | complete | translated; references kept English |
| `duas_030.json` | 987-1001 | 15 | complete | translated; references kept English |

## Work Status Details

### Completed: `duas_001.json`

- ID range: `1-34`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_002.json`

- ID range: `35-68`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_003.json`

- ID range: `69-102`
- Rows: `34`
- Completed on: `2026-09-03`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`; ID `83` retained from the original non-null citation and normalized to `Abu Dawud 4/322: 5084` because the matching English reference is `null`
- Verification: JSON valid, exact English IDs matched, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Completed: `duas_005.json`

- ID range: `137-170`
- Rows: `34`
- Completed on: `2026-09-03`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to README formatting
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: second-pass review completed; JSON valid, exact English IDs matched, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Completed: `duas_006.json`

- ID range: `171-204`
- Rows: `34`
- Completed on: `2026-09-03`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to README formatting
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: second-pass review completed; JSON valid, exact English IDs matched, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Completed: `duas_009.json`

- ID range: `273-306`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`; ID `304` normalized to ASCII English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `duas_010.json`

- ID range: `307-340`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`; ID `340` normalized to ASCII English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `duas_011.json`

- ID range: `341-374`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_012.json`

- ID range: `375-408`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_016.json`

- ID range: `511-544`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_017.json`

- ID range: `545-578`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_018.json`

- ID range: `579-612`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_021.json`

- ID range: `681-714`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_022.json`

- ID range: `715-748`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `duas_023.json`

- ID range: `749-782`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied exactly from `dua_main_en.sqlite` and kept in English
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, references/transliteration matched English DB, frozen fields unchanged

### Completed: `dua_infos_001.json`

- ID range: `1-21`
- Rows: `21`
- Completed on: `2026-08-28`
- Translated fields: `name`, `description`
- Source: translated from Bengali source because metadata marks `dua_infos` source as `BN`; the English DB has a different 16-row `dua_infos` table
- Arabic blocks: preserved exactly from backup
- Verification: JSON valid, no Bengali in translated top-level fields, IDs/key order/nullness unchanged

### Completed: `dua_infos_002.json`

- ID range: `22-42`
- Rows: `21`
- Completed on: `2026-08-28`
- Translated fields: `name`, `description`
- Source: translated from Bengali source because `dua_main_en.sqlite` has no matching `dua_infos` rows for IDs `22-42`
- Arabic blocks: preserved exactly from backup
- Quality review: polished machine-style wording and fixed awkward terms in difficult rows, including `22`, `30`, `38`, `40`, `41`, and `42`
- Verification: JSON valid, no Bengali in translated top-level fields, known machine-translation artifacts removed, IDs/key order/nullness unchanged, HTML tag counts unchanged, rebuild passed, SQLite integrity `ok`

## Rebuild Command

Run this after each completed chunk:

```bash
cd /Users/mdabdurrahman/Desktop/Database/Dua/dua_main_ja_planned_json
python3 rebuild_japanese_from_json.py
```

## Final Verification Checklist

- JSON file is valid.
- No Bengali remains in translated top-level fields.
- `reference` is English.
- Arabic fields are unchanged.
- `groups` is unchanged.
- IDs and category links are unchanged.
- Rebuild script runs without error.
- SQLite integrity check returns `ok`.

### Completed: `duas_004.json`

- ID range: `103-136`
- Rows: `34`
- Completed on: `2026-09-03`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to README formatting
- Verification: second-pass review completed; JSON valid, exact English IDs matched, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Completed: `duas_007.json`

- ID range: `205-238`
- Rows: `34`
- Completed on: `2026-09-03`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to README formatting
- Transliteration: copied verbatim from `dua_main_en.sqlite`
- Verification: second-pass review completed; JSON valid, all IDs matched exactly, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Completed: `duas_008.json`

- ID range: `239-272`
- Rows: `34`
- Completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to README formatting
- Transliteration: copied verbatim from `dua_main_en.sqlite`
- Source exception: ID `268` has `null` English `content` and `note`; the existing non-null Bengali values were translated to preserve nullness and complete the record
- Verification: second-pass review completed; JSON valid, all IDs matched exactly, no Bengali in translated top-level fields, protected fields and record order unchanged, Node.js rebuild passed, SQLite integrity `ok`

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_009.json`

- Status: `pending` → `complete` (Indonesian; existing Japanese completion preserved)
- ID range: `273-306`
- Rows: `34`
- Completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- References: English, not translated; copied from `dua_main_en.sqlite`, with README spacing normalization and ASCII apostrophe at ID `304`; all numbers preserved
- Transliteration: copied verbatim from `dua_main_en.sqlite`
- Source matching: all 34 IDs matched; no missing English rows
- Verification: second-pass language review completed; JSON valid; record and key order, null values, protected fields and HTML unchanged; no Bengali in translated top-level fields; protected `groups` retained verbatim, including nested Bengali
- Rebuild: Python executable unavailable; equivalent Node.js SQLite rebuild completed using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_010.json`

- Status: `pending` → `complete` (Indonesian; existing Japanese completion preserved)
- ID range: `307-340`
- Rows: `34`
- Completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- References: English, not translated; copied from `dua_main_en.sqlite`, with README formatting normalization at IDs `332`, `336`, `338`, `339` and ASCII English honorific at ID `340`; all numbers preserved
- Transliteration: copied verbatim from `dua_main_en.sqlite`
- Source matching: all 34 IDs matched; no missing English rows; ID `339` note kept `null` as required despite a non-null English note
- Source review: corrected awkward English meanings in Indonesian, including IDs `315`, `321`, `329`; retained source titles, including travel-title/content inconsistencies at IDs `319`, `323`, `324`
- Verification: second-pass language review completed; JSON valid with 2-space indentation and trailing newline; record and key order, null values, protected fields and HTML unchanged; no Bengali in translated top-level fields; protected `groups` retained verbatim, including nested Bengali
- Rebuild: Python executable unavailable; equivalent Node.js SQLite rebuild completed using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_010.json`

- Status: `complete` (independent recheck complete)
- ID range: `307-340`; rows: `34`; reviewed on: `2026-09-07`
- Every translated field (`name`, `content`, `translation`, `note`) reviewed record by record against the exact matching English database row
- Corrected IDs: `310`, `311`, `315`, `321`, `327`, `328`, `329`, `338`, `339`, `340`; improved source fidelity, wording, completeness and quotation punctuation
- Source fidelity: English meanings retained for ID `315` (adultery), ID `321` (safety) and ID `329` (hearing praise), superseding the prior interpretations; existing source title/content inconsistencies retained
- References: English, not translated; unchanged from pre-review backup; all reference numbers matched the English database; transliterations unchanged and matched verbatim
- Validation: JSON valid; record/key order, null values, protected fields, Arabic, audio, category/subcategory IDs and HTML unchanged; no Bengali in editable fields; protected `groups` retained verbatim; ID `339` note remains `null`
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON; temporary files removed after verification

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_011.json`

- Status: `pending` → `complete` (Indonesian; existing Japanese completion preserved)
- ID range: `341-374`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact IDs matched `dua_main_en.sqlite`; no missing English rows; Bengali consulted only for the animal-color ambiguity at ID `347`
- References: English, not translated; copied from English DB with README spacing/punctuation normalization at IDs `348`, `354`, `361`, `362`; all numbers preserved
- Transliteration: copied verbatim from English DB
- Review: every translated field checked record by record for meaning, completeness, natural Indonesian and terminology; source inconsistencies retained at IDs `358` (entering-mosque wording) and `368` (repeated narration)
- Validation: JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, null values, protected fields, Arabic, audio and category/subcategory IDs unchanged; HTML preserved; no Bengali in editable fields; protected `groups` preserved verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable) using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_011.json`

- Status: `complete` (independent recheck complete)
- ID range: `341-374`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed every translated field (`name`, `content`, `translation`, `note`) record by record against the exact corresponding English row
- Corrected IDs: `348`, `349`, `350`, `354`, `355`, `361`, `364`, `366`, `367`; clarified offering, restored visitor and standing meanings, and improved wording and completeness
- References: English, not translated; unchanged from review backup and matched to English with existing README formatting normalization; transliteration unchanged and matched verbatim
- Validation: JSON valid; row/key order, null values, protected fields, Arabic, audio, category/subcategory IDs, references, transliteration, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` preserved verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_012.json`

- Status: `pending` → `complete` (Indonesian; existing Japanese completion preserved)
- ID range: `375-408`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing rows; Bengali/Arabic consulted only for ambiguities, particularly IDs `389` and `394`
- References: English, not translated; copied from English DB with README spacing/language normalization at IDs `381`, `390`; all numbers preserved
- Transliteration: copied verbatim from English DB
- Source anomalies retained: ID `379` variant explanation differs from Arabic/Bengali; ID `381` note repeats “forgiven”; ID `390` English introduction names prayer tashahhud and omits the Arabic kinship clause from the translation; followed mandated English source without inventing replacements
- Review and validation: every translated field reviewed for meaning, completeness, natural Indonesian and terminology; JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` preserved verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable), using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_012.json`

- Status: `complete` (independent recheck complete)
- ID range: `375-408`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed every translated field (`name`, `content`, `translation`, `note`) record by record against the exact corresponding English row
- Corrected IDs: `381`, `391`, `393`, `400`, `401`, `402`, `403`; improved glorification wording, family comfort meaning, natural phrasing and the meaning of being raised by parents
- References: English, not translated; unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim
- Validation: JSON valid; record/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim; previously documented source inconsistencies preserved
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_013.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `409-442`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from English DB with README spacing/language normalization at IDs `417`, `420`, `421`, `422`, `423`, `424`, `431`, `432`; all reference numbers preserved
- Transliteration: copied verbatim from English DB
- Review: every translated field checked for accurate meaning, completeness, natural wording and consistent terminology; source quirks retained at IDs `416` (repeated phrase), `421` (duplicate title number), `425` (footnotes); Bengali title digit at ID `431` rendered as ASCII `2`; English meanings retained where source differs from Arabic
- Validation: JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` preserved verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable) with unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_013.json`

- Status: `complete` (independent recheck complete)
- ID range: `409-442`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed every translated field (`name`, `content`, `translation`, `note`) record by record against the exact English row
- Corrected IDs: `409`, `411`, `419`, `427`, `441`; improved natural wording, sentence completeness and subject clarity
- References: English, not translated; unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim
- Validation: JSON valid; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim; previously documented source quirks preserved
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_014.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `443-476`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from English DB with colon spacing normalization only at ID `475`; all reference numbers preserved
- Transliteration: copied verbatim from English DB
- Review: every translated field checked for meaning, completeness, natural Indonesian and terminology; source quirks retained at IDs `453`, `457`, `459` (title/content perspective), `458` (half-family wording), `463` (repeated greeting); clarified sneezer/listener roles at IDs `469`, `471` using immediate context
- Validation: JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` preserved verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable), using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_014.json`

- Status: `complete` (independent recheck complete)
- ID range: `443-476`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed every translated field (`name`, `content`, `translation`, `note`) record by record against the exact English row
- Corrected IDs: `443`, `458`, `462`, `470`, `471`, `473`; improved natural wording, restored fragrance in the question, clarified utensils and listener instructions, and translated affairs more precisely
- References: English, not translated; unchanged from review backup and matched English with existing colon normalization at ID `475`; transliteration unchanged and matched verbatim
- Validation: JSON valid; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim; previously documented source quirks preserved
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_015.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `477-510`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing rows; Bengali consulted only for ambiguities at IDs `486`, `497`, `505`, `509`
- References: English, not translated; copied from English DB with README formatting normalization at IDs `480`, `498`, `505`, `506`; all numbers preserved; inline citations in ID `496` kept English
- Transliteration: copied verbatim from English DB
- Review: every translated field checked for meaning, completeness, natural Indonesian and terminology; ID `496` long note translated in full; English anomalies retained at IDs `479` (praiser title), `483` (sacrificial reward), `494` (after-meeting timing), `502` (repeated drinking wording)
- Validation: JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable), using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_015.json`

- Status: `complete` (independent recheck complete)
- ID range: `477-510`; rows: `34`; reviewed on: `2026-09-07`
- Every translated field (`name`, `content`, `translation`, `note`) reviewed record by record against its exact English row, including the complete note at ID `496`
- Corrected IDs: `485`, `491`, `496`, `504`; clarified the angels description, release from a burden, bearing calamities, and the request for more milk
- References: English, not translated; unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim
- Validation: JSON valid; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim; previously documented source anomalies preserved
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_016.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `511-544`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing rows; Bengali consulted only for ambiguities at IDs `516`, `519`
- References: English, not translated; copied from English DB with README spacing/punctuation normalization at IDs `511`, `516`, `535`, `543`; all numbers preserved
- Transliteration: copied verbatim from English DB
- Review: every translated field checked for meaning, completeness, natural Indonesian and terminology; source quirks retained at IDs `511` (title/content), `520` (clouds wording), `535` (healing statement), `544` (incomplete introduction)
- Validation: JSON valid, UTF-8, 2-space indentation, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable), using unchanged Indonesian schema metadata; integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_016.json`

- Status: `complete` (independent recheck complete)
- ID range: `511-544`; rows: `34`; reviewed on: `2026-09-07`
- Every translated field (`name`, `content`, `translation`, `note`) reviewed record by record against its exact English row
- Corrected IDs: `511`, `533`, `535`, `538`, `541`, `543`, `544`; improved action descriptions, sentence flow, conditional assurance and survival wording
- References: English, not translated; unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim
- Validation: JSON valid; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs unchanged; no Bengali in editable fields; protected `groups` retained verbatim; previously documented source quirks preserved
- Rebuild: equivalent Node.js SQLite rebuild (Python unavailable); integrity `ok`; all 15 tables / 3082 rows verified against workspace JSON

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_017.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `545-578`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `content`, `translation`, `note`
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from English DB with ASCII apostrophe/spacing normalization at IDs `556`, `558`, `569`; all reference numbers preserved
- Transliteration: copied verbatim from English DB
- Review: English source wording retained at IDs 553 (prayer for another person and note referring to verses), 563 (temporal wording), 566 (night/day wording), 574 (Bestower of Faith), and 575 (sending a messenger). Bengali consulted only to review ambiguities at these IDs. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata. Protected groups retained verbatim.
- Validation and rebuild: All 34 exact English IDs matched; every translated field rechecked for meaning, completeness, natural Indonesian, spelling and grammar. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML and URLs preserved; no Bengali in editable fields; references ASCII English. Equivalent Node.js rebuild passed; integrity ok; all 15 tables / 3082 rows verified against JSON; schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_017.json`

- Status: `complete` (independent recheck complete)
- ID range: `545-578`; rows: `34`; reviewed on: `2026-09-07`
- Every translated field (`name`, `content`, `translation`, `note`) reviewed record by record against its exact English row
- Corrected IDs: `547`, `551`, `552`, `557`, `559`, `560`, `562`, `565`, `568`, `573`, `576`; improved meaning, completeness, grammar and natural phrasing
- References: English, not translated; unchanged from review backup with existing README normalization at IDs `556`, `558`, `569`; transliteration unchanged and matched verbatim
- Validation and rebuild: Every translated field reviewed against its exact English row. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, verse numbering and Bengali checks passed. References and transliteration unchanged from review backup and matched English with existing reference formatting normalization. Equivalent Node.js SQLite rebuild passed; reopened database integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Previously documented English source quirks retained; no other translation file changed; Python unavailable, so the equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_018.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `579-612`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `translation`; `content` and `note` remain null throughout
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with colon-spacing normalization where needed and removal of the extra colon after Surah Nisa at ID 579; all numbers preserved. Normalized IDs: 579, 581, 584, 586, 587, 588, 589, 590, 594, 595, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612.
- Transliteration: copied verbatim from English DB
- Review: Bengali and protected Arabic consulted only to check ambiguities at IDs 579, 586, 590, 596 and 607; English remained the translation source. Retained English source wording for great stars (582), lowland (586), and place for rites (607). Protected groups retained verbatim. Python unavailable; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched; every name and translation reviewed record by record for meaning, completeness, natural Indonesian, spelling, grammar and consistent terminology. Content and note remain null. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and verse numbers preserved; no Bengali in editable fields; references ASCII English. Equivalent Node.js rebuild passed; reopened database integrity ok; all 15 tables / 3082 rows verified against JSON; schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_018.json`

- Status: `complete` (independent recheck complete)
- ID range: `579-612`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed fields: `name`, `translation`; verified `content` and `note` remain null
- Corrected IDs: `579`, `583`, `589`, `593`, `605`
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim
- Review: Corrected disdain wording (579), independence from a protector (583), complete loss (589), graciously overlooking faults (593), and descendants establishing prayer (605). Previously documented English source quirks retained. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every translated name and translation reviewed record by record against its exact English row; content and note remain null. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and verse numbering preserved; no Bengali in editable fields. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Scope: hashes confirm no other translation file changed

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_019.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `613-646`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `translation`; `content` and `note` remain null throughout
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with colon-spacing normalization at all IDs 613-646 and removal of the extra separator before the chapter number at ID 634; all reference numbers preserved.
- Transliteration: copied verbatim from English DB
- Review: Repeated passages matched established Indonesian wording: ID 626 with ID 564 and ID 635 with ID 559. English wording retained at ID 619 (authority) and ID 621 (objects of torment). Protected groups retained verbatim. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched. Every name and translation rechecked record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology; content and note remain null. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and verse numbering preserved. No Bengali in editable fields; references ASCII English. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_019.json`

- Status: `complete` (independent recheck complete)
- ID range: `613-646`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed fields: `name`, `translation`; verified `content` and `note` remain null
- Corrected IDs: `617`, `631`, `637`, `642`, `644`
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim
- Review: Corrected sentence construction at ID 617, conditional possibility at ID 631, divine-name phrasing at ID 637, the tongue-knot image at ID 642, and the request for help at ID 644. Previously documented source wording and repeated-passage consistency retained. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every translated name and translation reviewed record by record against its exact English row; content and note remain null. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and verse numbering preserved; no Bengali in editable fields. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Scope: hashes confirm no other translation file changed

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_020.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `647-680`; rows: `34`; completed on: `2026-09-07`
- Translated fields: `name`, `translation`, `note`; `content` remains null throughout; all other nulls preserved
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with colon spacing at IDs 647-676, doubled-space cleanup at ID 669, and the collection/number colon at ID 680; all numbers preserved. IDs 677-679 copied verbatim.
- Transliteration: copied verbatim from English DB
- Review: Full notes at IDs 677-680 translated, including women's wording and meaning, footnotes, narration and memorization instructions. English title/content differences retained at IDs 656 and 661; source perspective retained at ID 663 (human master) and source Eternal wording retained at ID 679. Repeated prayer at ID 649 matches ID 605; ID 680 matches ID 625. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched. Every name, translation and non-null note rechecked record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology; content remains null. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and footnote markers preserved. No Bengali in editable fields; references ASCII English; women's transliterated wording in ID 677 matched English verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_020.json`

- Status: `complete` (independent recheck complete)
- ID range: `647-680`; rows: `34`; reviewed on: `2026-09-07`
- Reviewed fields: `name`, `translation`, `note`; verified `content` and all other null values remain null
- Corrected IDs: `653`, `668`, `671`, `677`, `678`, `679`
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim
- Review: Clarified who becomes an example in title 653, improved accommodation and Paradise wording at IDs 668 and 671, restored the exclusive retention of names in ID 677, and improved prayer-response wording in notes 678-679. Previously documented source quirks retained. Python unavailable; Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every name, translation and non-null note reviewed record by record against its exact English row, including complete notes at IDs 677-680. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and footnotes preserved; no Bengali in editable fields. Women's transliterated wording at ID 677 preserved verbatim. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Scope: hashes confirm no other translation file changed

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_021.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `681-714`; rows: `34`; completed on: `2026-09-08`
- Translated fields: `name`, `content`, `translation`, `note`; all null values preserved
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with grading punctuation and collection/number colon at IDs 681-682, Quran chapter/verse spacing at ID 692, and multiple-source semicolon at ID 697; all numbers preserved.
- Transliteration: copied verbatim from English DB
- Review: Translated all non-null text fields, including complete narrations and notes. ID 683 follows the shorter English passage, excluding the extra Bengali sentence. English reference typo Suya al-Ambiya retained verbatim at ID 688. Source wording retained where repeated prayers differ, including protection at ID 700 and Mighty at ID 707. Repeated passages aligned with earlier Indonesian wording where meanings match. Python unavailable; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched. Every name, content, translation and note reviewed record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers preserved. No Bengali in editable fields; references ASCII English; transliteration copied verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_021.json`

- Status: `complete` (independent recheck complete)
- ID range: `681-714`; rows: `34`; reviewed on: `2026-09-08`
- Reviewed fields: `name`, `content`, `translation`, `note`; all null values preserved
- Corrected IDs: `683`, `690`, `699`, `702`, `705`, `711`
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim.
- Review: Clarified Self-Subsisting at ID 683, natural patience wording at ID 690, weakness in old age at ID 699, livelihood wording at ID 702, righteousness as kesalehan at ID 705, and the missing Indonesian object in the introduction at ID 711. Previously documented English source quirks retained. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every name, content, translation and note reviewed record by record against its exact English row. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers preserved; no Bengali in editable fields. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Scope: hashes confirm no other translation file changed

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_022.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `715-748`; rows: `34`; completed on: `2026-09-08`
- Translated fields: `name`, `content`, `translation`, `note`; all null values preserved
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with grading punctuation and collection/number colon at ID 731 and multiple-source semicolons at IDs 733 and 744; all numbers preserved. ID 724 English explanatory reference footnote retained verbatim.
- Transliteration: copied verbatim from English DB
- Review: Translated all non-null fields, including the full narration at ID 724. English source wording retained for diseases at ID 721, haste/deferred and First/Last at ID 728, fried goat at ID 734, and the title/content differences at IDs 732 and 746. The English refuge-from-you typo at ID 719 rendered as seeking refuge in Allah consistently with the sentence meaning. ID 726 inheritance idiom expressed as retaining faculties until the end of life. Repeated prayers at IDs 747-748 match IDs 679 and 678. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched. Every name, content, translation and note reviewed record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, numbers and footnotes preserved. No Bengali in editable fields; references ASCII English; transliteration copied verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_022.json`

- Status: `complete` (independent recheck complete)
- ID range: `715-748`; rows: `34`; reviewed on: `2026-09-08`
- Reviewed fields: `name`, `content`, `translation`, `note`; all null values preserved
- Corrected IDs: `717`, `718`, `719`, `723`, `724`, `727`, `742`
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim.
- Review: Improved the introduction and inner treachery wording at ID 717, protection-request grammar at IDs 718-719, pardon wording and punctuation at ID 723, anticipation of sunrise and activity wording at ID 724, title accuracy and handwriting instruction at ID 727, and the learned-scholar meaning at ID 742. Previously documented English source quirks retained. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every name, content, translation and note reviewed record by record against its exact English row, including the full narration at ID 724. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers preserved; no Bengali in editable fields. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified.
- Scope: hashes confirm no other translation file changed

### Indonesian independent recheck 2: `dua_main_id_planned_json/tables/duas/duas_022.json`

- Status: `complete` (second independent recheck complete)
- ID range: `715-748`; rows: `34`; reviewed on: `2026-09-08`
- Reviewed fields: `name`, `content`, `translation`, `note`; all null values preserved
- Corrected IDs: `724` (`note` only)
- References: English, not translated; unchanged from review backup with existing README normalization; transliteration unchanged and matched verbatim
- Review: Only ID 724 note corrected: natural wording for looking toward sunrise and restoration of the first My Lord address in the first response. All other translated fields reviewed and retained. Previously documented English source quirks retained. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every name, content, translation and note reviewed again against all 34 exact English rows, including the full narration at ID 724. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, numbers and Bengali checks passed. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_023.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `749-782`; rows: `34`; completed on: `2026-09-08`
- Translated fields: `name`, `content`, `translation`, `note`; all null values preserved
- Source matching: all 34 exact English IDs matched; no missing English rows
- References: English, not translated; copied from dua_main_en.sqlite with collection/number colons at IDs 750 and 776; all numbers preserved. Reference at ID 772 remains null.
- Transliteration: copied verbatim from English DB
- Review: All non-null text fields translated. English source quirks retained: Innermost/beyond wording at ID 758, narrator transition at ID 759, title/translation differences at IDs 761 and 764, inline transliterated forms including Astigfirullah at ID 767, singular/plural switch at ID 776, and sacrificial-slaughter reward at ID 781 (different from earlier ID 450). Repeated wording at IDs 763, 780 and 782 aligned with earlier Indonesian entries. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: All 34 exact English IDs matched. Every name, content, translation and note reviewed record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology, including the long prayers and narrations at IDs 750, 760, 764 and 770. JSON valid, UTF-8, 2-space indent, trailing newline; row/key order, nulls, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers preserved. No Bengali in editable fields; non-null references ASCII English; transliteration copied verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_023.json`

- Status: `complete` (independent recheck complete)
- ID range: `749-782`; rows: `34`; reviewed on: `2026-09-08`
- Reviewed fields: `name`, `content`, `translation`, `note`; all null values preserved
- Corrected IDs: `750`, `753`, `759`, `762`, `768`, `774`, `775`
- References: English, not translated; unchanged from review backup with existing README normalization; null reference at ID 772 preserved; transliteration unchanged and matched verbatim
- Review: Clarified private worship wording at ID 750, the subject of second childhood at ID 753, proclaiming blessings at ID 759, the introduction at ID 762, who receives the ability to retaliate at ID 768, the number of individual horse riders at ID 774, and ownership of the Throne at ID 775. Previously documented English source quirks retained. Python unavailable in this session environment; equivalent Node.js SQLite rebuild used unchanged Indonesian schema metadata.
- Validation and rebuild: Every name, content, translation and note reviewed record by record against all 34 exact English rows, including complete long prayers and narrations. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, numbers and Bengali checks passed. References unchanged from review backup and matched English with existing README normalization; transliteration unchanged and matched verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows, schema, sequences and pragmas verified. Hashes confirm no other translation file changed.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_024.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `783-816`
- Rows: `34`
- Completed on: `2026-09-09`
- Translated fields: `name`, `content`, `translation`, `note`
- Source: matching English rows from `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied from dua_main_en.sqlite with Quran chapter:verse spacing normalized and a colon added after Musnad Ahmad at ID 806. ID 789 English reference is null: retained the existing non-null Bengali citation as Muslim: 2491 to preserve nullness. All citation numbers preserved.
- Verification: All 34 exact English IDs matched; all non-null name, content, translation and note fields reviewed for completeness, meaning and natural Indonesian. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and footnotes checked. No Bengali in editable fields; references ASCII English; transliteration copied verbatim. Equivalent Node.js SQLite rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. Other translation files match HEAD after normalizing Git checkout line endings.
- Source notes: English source quirks retained: ID 787 prayer differs from protected Arabic and includes the stray phrase a time of distress; ID 794 names Walid bin Uqba; ID 795 describes Abu Bakr as elderly and the Prophet as a youth; ID 798 describes poison; ID 800 dates Ahzab to the fourth year after Hijrah; ID 810 says elephantiasis. Bengali consulted for the household wording at ID 787 and incomplete wording at ID 789. ID 804 matches established wording at ID 700, and ID 810 matches ID 721. Python unavailable; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Rebuilt artifact: `dua_main_id_rebuilt.sqlite`. Temporary backup and helper scripts removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_024.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `783-816`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note`
- Corrected IDs: 784, 785, 798, 799, 800, 803, 805, 806, 808
- References: English, not translated; unchanged from review backup, including existing normalization and ID 789 fallback. Transliteration preserved verbatim.
- Verification: Every name, content, translation and note reviewed record by record against all 34 exact English rows. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup, with existing documented reference normalization and ID 789 fallback preserved. Equivalent Node.js rebuild passed; reopened database integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Restored the exclusive wording at IDs 784-785; clarified the whip sound at ID 798 and shifting eyes at ID 799; improved sentence flow at ID 799, reckoning wording at ID 800, weakness in old age at ID 803, the withheld-things/rest clause at ID 805, devotional phrasing at ID 806 and firmness in religion at ID 808. Previously documented English source quirks, including the mismatched prayer and stray distress phrase at ID 787, retained. Python unavailable in this session; equivalent Node.js rebuild followed the unchanged Python script and Indonesian schema metadata.
- Temporary review backup, script and intermediate database removed; verified final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_025.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `817-850`; rows: `34`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `content`, `translation`, `note` (93 non-null fields)
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied from dua_main_en.sqlite. README formatting applied at IDs 820, 822, 824 and 837 (colons, removal of No., ASCII apostrophe and spacing); every citation number preserved. References at IDs 819 and 829 remain null.
- Verification: All 34 exact English IDs matched. All 93 non-null name, content, translation and note fields translated and rechecked record by record for accuracy, completeness, natural Indonesian, spelling, grammar and consistent Islamic terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and footnotes validated. No Bengali in editable fields; references ASCII English with all citation numbers preserved; transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: Bengali consulted to resolve ambiguity in IDs 820, 830, 833, 840 and 847; English remains the primary source. Reversed benefactor/recipient wording clarified at IDs 830 and 847; the malformed eating instruction at ID 840 rendered as eating with the right hand and from the nearest part, with the continuing practice expressed naturally. Preserved source quirks: incomplete continuation at ID 819; dates in ID 826; seven clauses per paragraph in ID 839 despite differences in protected Arabic/transliteration; from Allah wording in ID 845. Removed the stray p before I in ID 839 when translating. Final review refined the prayer syntax at ID 825, tasbih wording at ID 839 and title at ID 842. Python unavailable in this session; equivalent Node.js rebuild followed the unchanged Python rebuild script and Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_025.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `817-850`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note` (93 non-null fields)
- Corrected IDs: 819, 825, 826, 833, 838, 848
- References: English, not translated; unchanged with existing README normalization. Null references at IDs 819 and 829 preserved; transliteration unchanged and matched English verbatim.
- Verification: Every record and all 93 non-null name, content, translation and note fields rechecked against all 34 exact English rows. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, all protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup and matched English with existing documented reference normalization; null references preserved. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Smoothed the introductions at IDs 819, 825 and 848; clarified newly appearing seasonal fruit and restored the beneficiaries of the blessing at ID 826; replaced casual Sesukamu with respectful wording at ID 833; restored the second direct address at ID 838. All other translated fields reviewed and retained, including previously documented source ambiguities and quirks. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary review backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_026.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `851-884`; rows: `34`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `content`, `translation`, `note` (78 non-null fields)
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied from dua_main_en.sqlite with collection/number colons at IDs 854, 865, 866, 867, 871 and 880. All numbers preserved. References at IDs 877 and 878 remain null.
- Verification: All 34 exact English IDs matched. All 78 non-null name, content, translation and note fields translated and rechecked record by record for meaning, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers verified. No Bengali in editable fields; references ASCII English; transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: English source quirks retained: from Allah wording at ID 853; goat, jaws and horn-color description at ID 858; waning/disappearing moon at ID 866; spine and Almighty wording at ID 871; rukoo titles at IDs 874 and 876 despite standing-after-rukoo subcategory; safety at ID 882; shorter forgiveness prayer and Merciful at ID 884. Bengali and protected Arabic consulted only to clarify the malformed body-support clause at ID 871 and review source differences. Repeated devotional phrases matched established Indonesian wording; final review smoothed ID 855 introduction and ID 871 grammar. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, helper scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_026.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `851-884`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note` (78 non-null fields)
- Corrected IDs: 855, 860, 872, 878, 879
- References: English, not translated; unchanged with existing README normalization. Null references at IDs 877 and 878 preserved; transliteration unchanged and matched English verbatim.
- Verification: Every record and all 78 non-null name, content, translation and note fields rechecked against all 34 exact English rows for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup; matched English with existing documented reference normalization. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Restored habitual wording at IDs 855 and 878, simplified the narration sentence structure at ID 860, replaced Mahaberkah with natural Indonesian at ID 872, and improved the distance request at ID 879. All other translated fields reviewed and retained. Previously documented English source quirks preserved. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_027.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `885-918`; rows: `34`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `content`, `translation`, `note` (76 non-null fields)
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied from dua_main_en.sqlite with ASCII apostrophes and collection/number colons at IDs 892, 894, 895, 903, 905, 912, 917 and 918. All citation numbers preserved; ID 904 reference remains null.
- Verification: All 34 exact English IDs matched; all 76 non-null name, content, translation and note fields translated and rechecked record by record for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nulls, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and numbers verified. No Bengali in editable fields; references ASCII English with citation numbers preserved; transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: Bengali consulted to clarify malformed English at IDs 897, 899, 905 and 917. ID 905 rendered the intended bestowed-guidance, continuing need for Allah, and darkness-to-faith meanings; no extra Arabic clauses added. Source quirks preserved: peace/holy wording at ID 889; inline Takbabbal Minni spelling at ID 891; my debt at ID 899; repeated knowledge requests at ID 903; cloth-turning instructions at ID 907; rain titles versus wind/storm prayers at IDs 909-911; identical repeated clause at ID 911. Final review clarified poverty at ID 907 and enemy-attack wording at ID 914. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_027.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `885-918`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note` (76 non-null fields)
- Corrected IDs: 886, 890, 892, 893, 905, 907, 915
- References: English, not translated; unchanged with existing README normalization; null reference at ID 904 preserved. Transliteration unchanged and matched English verbatim.
- Verification: Every record and all 76 non-null name, content, translation and note fields rechecked against all 34 exact English rows for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup; matched English with existing documented reference normalization. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Improved alone wording at ID 886, clarified rukun as a corner of the Kaaba at ID 890, repaired guidance-request grammar at ID 892, made the replaced affliction explicit at ID 893, corrected relative-clause order at ID 905, removed the excessive maximum-height wording at ID 907, and improved the request to die in Medina at ID 915. All other translated fields reviewed and retained, including previously documented source ambiguities and quirks. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_028.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `919-952`; rows: `34`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `content`, `translation`, `note` (81 non-null fields)
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied from dua_main_en.sqlite with collection/number colons at IDs 920-922 and 928, and duplicate spacing removed at ID 925. All citation numbers preserved.
- Verification: All 34 exact English IDs matched; all 81 non-null name, content, translation and note fields translated and rechecked record by record for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and footnotes verified. No Bengali in editable fields; references ASCII English with citation numbers preserved; transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: Exact repeated English prayers matched reviewed Indonesian translations in earlier chunks, including IDs 930-931, 933-940, 942 and 944-952. Full notes at IDs 928 and 937 translated without omissions. English source quirks preserved: laughter/reluctance wording at ID 920; narrator mismatch between content and note at ID 936; Eternal at ID 937; place-for-rites wording at IDs 931 and 945, distinct from rites wording at ID 939. Final review clarified the necessary consequence of forgiveness at ID 932 and devotion in title 950. English remained the source; no Bengali fallback required. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_028.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `919-952`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note` (81 non-null fields)
- Corrected IDs: 932, 935, 937
- References: English, not translated; unchanged with existing README normalization. Transliteration unchanged and matched English verbatim.
- Verification: Every record and all 81 non-null name, content, translation and note fields rechecked against all 34 exact English rows for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup; matched English with existing documented reference normalization. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Restored every day/night wording at ID 932, righteous deeds at ID 935, and indeed plus the repeated direct address to the Eternal at ID 937. All other translated fields reviewed and retained, including full notes, repeated prayers and previously documented English source quirks. These completeness corrections intentionally refine wording inherited from earlier chunks without changing those files. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_029.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `953-986`; rows: `34`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `content`, `translation`, `note` (76 non-null fields)
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied verbatim from dua_main_en.sqlite except chapter:verse spacing normalized at ID 983. All citation numbers preserved.
- Verification: All 34 exact English IDs matched; all 76 non-null name, content, translation and note fields translated and rechecked record by record for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and digits verified. No Bengali in editable fields; references ASCII English with citation numbers preserved; transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: Repeated exact English prayers aligned with reviewed Indonesian entries after record-by-record checking. ID 964 follows the English refuge with You wording, without the added majesty/from below wording in the earlier Indonesian duplicate. English source quirks preserved at ID 960: haste/deferred and First/Last. Bracketed Generous at ID 958 and trailing verse numbers at ID 955 preserved. Complete narrations and notes at IDs 958-959 and 962-964 translated. Final review improved title grammar at ID 953 and the introduction at ID 962. English remained the source; no Bengali fallback needed. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_029.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `953-986`; rows: `34`
- Reviewed fields: `name`, `content`, `translation`, `note` (76 non-null fields)
- Corrected IDs: 955, 964, 973, 974
- References: English, not translated; unchanged with existing README normalization. Transliteration unchanged and matched English verbatim.
- Verification: Every record and all 76 non-null name, content, translation and note fields rechecked against all 34 exact English rows for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup; matched English with existing documented reference normalization. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Improved descendants phrasing at ID 955, the request to ease fear at ID 964, inclusive whoever wording at ID 973, and the call to faith at ID 974. All other translated fields reviewed and retained, including full narrations, repeated prayers and previously documented English source quirks. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_030.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `987-1001`; rows: `15`
- Completed on: `2026-09-09`
- Translated and rechecked fields: `name`, `translation`, `note` (31 non-null fields); `content` remains null.
- Source: exact English rows in `dua_main_en.sqlite`; transliteration copied verbatim.
- References: English, not translated; copied verbatim from the English database.
- Verification: All 15 exact English IDs matched; all 31 non-null name, translation and note fields translated and rechecked record by record for accuracy, completeness, natural Indonesian, spelling, grammar and terminology. Content remains null. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs and digits verified. No Bengali in editable fields; references ASCII English; references and transliteration copied verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Source and review notes: Repeated prayers aligned with earlier reviewed Indonesian wording at IDs 987, 989, 991, 993, 995 and 999; IDs 988 and 1000 use identical wording. Preserved English source scope, including the shorter verse 9 excerpt at ID 994, the torment wording at ID 998, and both morning/evening statements in the note at ID 1001. Final review improved the eternal-residence sentence and inclusive wording at ID 994. English remained the source; no Bengali fallback required. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, scripts, state file and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/duas/duas_030.json`

- Status: complete; reviewed on `2026-09-09`
- ID range: `987-1001`; rows: `15`
- Reviewed fields: `name`, `content`, `translation`, `note` (31 non-null fields)
- Corrected IDs: 990, 997
- References: English, not translated; unchanged and matched English verbatim, as did transliteration.
- Verification: Every record and all 31 non-null name, translation and note fields rechecked against all 15 exact English rows for accuracy, completeness, natural Indonesian, spelling, grammar and terminology; content remains null. JSON, UTF-8, 2-space indent, trailing newline, row/key order, nullness, protected fields, Arabic, audio, category/subcategory IDs, HTML, URLs, digits and Bengali checks passed. References and transliteration unchanged from review backup and matched English verbatim. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows exactly match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Improved the ever-adhering punishment wording at ID 990 and clarified the completed return and final destination at ID 997. All other translated fields reviewed and retained, including the full note at ID 1001, the shorter English verse excerpt at ID 994 and torment wording at ID 998. Python unavailable in this session; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and intermediate database removed; final artifact: `dua_main_id_rebuilt.sqlite`.
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_013.json`

- ID range: `409-442`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_014.json`

- ID range: `443-476`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_015.json`

- ID range: `477-510`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_019.json`

- ID range: `613-646`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_020.json`

- ID range: `647-680`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_024.json`

- ID range: `783-816`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_025.json`

- ID range: `817-850`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_026.json`

- ID range: `851-884`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_027.json`

- ID range: `885-918`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_028.json`

- ID range: `919-952`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_029.json`

- ID range: `953-986`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_030.json`

- ID range: `987-1001`
- Rows: `15`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Review: categories & subcategories (2026-08-28)

- Checked all 44 category names and 118 subcategory names against `dua_main_en.sqlite` and the Bengali source.
- Frozen fields intact: `icon`, `dua_count`, `subcat_count`, `id`, `cat_id` unchanged.
- Term consistency with the translated duas — fixed:
  - `シャイターン` -> `悪魔` (cat 20, subcat 63): the duas use `悪魔` for Satan.
  - `ルクー` -> `ルクーゥ` (subcats 33-35): the duas use `ルクーゥ（立礼）`.
  - `サジダ` -> `スジュード` for the act of prostration (subcats 36-37); `サジダの節` kept as the verse term (subcat 38, act -> `平伏`).
  - dua id 646 name `業火からの救い` -> `地獄からの救い` (its body and the Arabic are جهنم / Jahannam).
- Wording clarified:
  - cat 19 `犠牲祭の供犠` -> `犠牲の供物（クルバーニー）` (removed the doubled 犠牲).
  - cat 27 `非難と善意の祈り` -> `非難・称賛と幸いを願う祈り` (the old label did not parse).
- Note: cat 2 `ズィクルの徳` correctly follows the Bengali (`যিকিরের ফযীলত`); the English label "Dua's Excellence" is a source error and was not copied.
- Verification: JSON valid, rebuild passed, SQLite integrity `ok`, row counts unchanged (44 / 118 / 1001).

### Review: main category titles (2026-08-28)

- Improved all titles in `categories_001.json`, `ruqyah_categories_001.json`, and `sections_001.json`.
- Translated/improved field: `name`
- Frozen fields intact:
  - `categories`: `id`, `icon`, `dua_count`, `subcat_count`
  - `ruqyah_categories`: `id`, `type`, `icon`
  - `sections`: `id`, `book_id`
- Verification: JSON valid, no Bengali in title fields, row counts unchanged (44 / 15 / 21), rebuild passed, SQLite integrity `ok`.

### Completed: `ruqyah_instants_001.json`

- Path: `dua_main_ja_planned_json/tables/ruqyah_instants/ruqyah_instants_001.json`
- ID range: `1-31`
- Rows: `31`
- Completed on: `2026-08-30`
- Status: `pending` -> `complete`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- Source: translated from `dua_main_en.sqlite` (`ruqyah_instants`, ids 1-31); Bengali used only to resolve ambiguity
- References: not translated; English values kept as-is from `dua_main_en.sqlite`
- Transliteration: unchanged (matches `dua_main_en.sqlite` exactly)
- Frozen fields intact: `id`, `topic_id`, `uthmani`, `transliteration`, `reference`, `cat_id`, `subcat_id`, `audio`
- Naming convention set for this table: source labels localised in katakana with ASCII numerals
  (`Al-Fatiha 1:1-7` -> `アル・ファーティハ 1:1-7`, `Abu Dawud : 775` -> `アブー・ダーウード: 775`),
  matching how the Bengali edition localises the same field
- Topic names: `From Quran` -> `クルアーンより`, `From Sunnah` -> `スンナより`
- Term consistency with the translated duas:
  - `ルキヤ` for ruqyah, `アッラー` / `クルアーン` in katakana
  - `完全なる御言葉` for Allah's perfect words
  - `呪われた悪魔` for Satan the outcast, `邪視` for the envious eye
  - Quran passages reuse the wording already used in `duas` for the same ayat
    (Al-Fatiha, Al-Baqarah 2:1-5, 2:163-164, 2:255, 2:284-286, Yusuf 12:64, Al-Kafirun)
- Verification: structure check passed (row count 31, key order, frozen fields, nullness),
  every `reference` ASCII English, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_002.json`

- ID range: `32-62`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_003.json`

- ID range: `63-93`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_004.json`

- ID range: `94-124`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_005.json`

- ID range: `125-155`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_006.json`

- ID range: `156-186`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_007.json`

- ID range: `187-217`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_008.json`

- ID range: `218-248`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_009.json`

- ID range: `249-279`
- Rows: `31`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Completed: `ruqyah_instants_010.json`

- ID range: `280-308`
- Rows: `29`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `name`, `content`, `translation`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated fields, frozen fields and nullness intact, rebuild passed, SQLite integrity `ok`

### Review note: `ruqyah_instants_002-010.json`

- Qur'anic wording was checked against Saeed Sato's modern Japanese rendering and polished to match this database's calm, readable devotional style.
- Exact Arabic passages already translated elsewhere in the Japanese workspace reuse the established wording.
- Source inconsistencies were resolved by following each row's Arabic text and verse title: ID `98` contains Al-Mulk 67:1-4 (not the extra verse present in the English translation), and ID `184` contains Al-Ahzab 33:70-71 (not the unrelated English translation text).

### Completed: `tables/ruqyah_details/ruqyah_details_001.json` – `ruqyah_details_010.json`

- ID range: `1-200` (10 chunks of 20 rows)
- Rows: `200`
- Completed on: `2026-09-08`
- Translated fields: `topic_name`, `text`
- References: kept in English; inline hadith citations left in ASCII English form
- Note: the completed Japanese text had been overwritten when `rechunk_planned_json.py` regenerated these chunks from English on `2026-08-30`. It was restored from the committed 40-row chunks and re-laid out into the current 20-row chunk layout. Arabic `<ar>` blocks, HTML tags and hadith numbers untouched.
- Verification: JSON valid, 200/200 rows contain Japanese, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `tables/ruqyah_subcategories/ruqyah_subcategories_001.json`

- ID range: `1-163`
- Rows: `163`
- Completed on: `2026-09-08`
- Translated fields: `name`
- References: none in this table
- Note: translated from the English source. Terminology aligned with `ruqyah_categories`: ルキヤ, ジン, シフル（魔術）, 邪視（アイン）, ラーキー, ワスワス, ヒジャーマ, タウィーズ.
- Verification: JSON valid, 163/163 rows in Japanese, `id`/`type`/`cat_id` unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `tables/ruqyah_videos/ruqyah_videos_001.json`

- ID range: `1-74`
- Rows: `74`
- Completed on: `2026-09-08`
- Translated fields: `name`, `author`
- References: none in this table
- Note: `dua_main_en.sqlite` has no matching rows for this table — it holds a different 40-row set of English-language videos, while these 74 rows are the Bengali-language videos whose links are in the workspace. Per the README rule, these were translated from the Bengali source. Author names are transliterated to katakana. `link`, `link_id`, `cat_id`, `subcat_id` untouched.
- Open data issue (not a translation issue): `subcat_id` values here are `105-117`, which come from the Bengali `ruqyah_subcategories` table. The workspace's `ruqyah_subcategories` is the 163-row English set, whose VIDEO subcategories are `150-163`. These video rows therefore do not link to a matching subcategory. Left as-is because `subcat_id` is a frozen field.
- Verification: JSON valid, 74/74 rows in Japanese, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `tables/drawer_items/drawer_items_001.json`

- ID range: `19-24`
- Rows: `6`
- Completed on: `2026-09-08`
- Translated fields: `title`, `hero_title1`, `hero_title2`, `content`
- References: none in this table
- Note: translated from the English `drawer_items` rows, matched by `item_type` (English IDs are `1-6`, these are `19-24`). The `content` field is a JSON string; its `sections` array keeps the original order, section types and `spacer` heights — only `text`, `title`, `header` and `details` values were translated. Sections present only in the Bengali source (the Arabic-titled reference works in the credits list) were translated from the Bengali. Arabic book titles left in Arabic script.
- Verification: JSON valid, 6/6 rows in Japanese, `item_type`/`display_order`/timestamps unchanged, content JSON re-parses with identical section structure, rebuild passed, SQLite integrity `ok`

## Remaining Work

| Table | Rows | Status |
|---|---|---|
| `tables/books/books_001.json` | 3 | not translated — book tables excluded by instruction |
| `tables/book_details/book_details_001.json` | 86 | not translated — book tables excluded by instruction |

Every other table in the Japanese workspace is fully translated. `tables/ids` holds only numeric
ID pairs and `tables/drawer_item_actions` is empty, so neither has anything to translate.

## QA Pass — 2026-09-08

A full-database audit was run after the tables above were completed. It found defects in
work that had already been marked `complete`, so those were repaired and re-verified.

### `dua_infos` (42 rows) — machine-translation damage repaired

This table has **no English source**: `dua_main_en.sqlite` holds a different 16-row set
(EN id 1 is "Conditions of dua being accepted", BN id 1 is "Meaning of dua"). Every repair
below was therefore checked against the Bengali source row by row.

Factual corruptions found and fixed:

- 14 hadith numbers rendered as dates or years — `[Abu Dawud, 1481年]` (a hadith number, not a year);
  volume/page refs like `4/39` turned into `4 月 39 日`; `4/1882` into `1882 年 4 月`.
- A Qur'an verse number rendered as an age: `スーラ・ユヌス：18歳` for Yunus 18.
- A page number rendered as an age: `36歳` for p. 36 of `Al-Jawabul Kafi`.
- Bengali `হাতের কর` (knuckles) mistranslated as `税金` (tax).
- `قلب` (qalb, heart) rendered as `腸` (intestine); `(PBUH)` misapplied to the children of Adam
  instead of Adam himself.
- Surah `যুমার` (Zumar) rendered as `年齢` (age).
- 17 citation blocks rebuilt from the Bengali source.

Language defects fixed: 42 missing `する` verb endings (`ドゥアーます` → `ドゥアーします`),
21 duplicated-word artifacts, untranslated English left in running prose, and 7 surah
citations put into the README reference format.

Legitimate text that was checked and deliberately left alone: the hadith repetition
`完全、完全、完全` (تامة تامة تامة), the hijri lifespan `152年〜227年`, and romaji
transliteration blocks.

### `ruqyah_details` (200 rows) — corrections

- `詩` (poem) corrected to `節` (verse) throughout, including `詩篇72:1-7`, which rendered a
  Qur'an reference as the Biblical **Psalms**.
- `sahara` (سحرة, sorcerers) had been mistranslated as `砂漠` (desert).
- Broken quotations, a misplaced `ﷻ`, a dangling sentence fragment and a garbled condition
  repaired in id 1; `(’alayhis-salam)` put into Japanese.

### Terminology normalised database-wide

`アーイシャ`, `アブー・フライラ`, `ルキヤ`, `邪視`, `ハディース`, `イフラース`, `ドゥアー`,
and fullwidth honorifics `（RA）`/`（R）`/`（ﷺ）`.

One apparent match was **verified and left unchanged**: `ruqyah_instants` id 225 uses
`善い目／悪い目に遭う`, which is the idiom "to experience", not the evil eye — the row is
Qur'an 4:78.

### Verification

- Frozen fields, row counts, key order and null-ness identical to the pre-QA backup for all 63 files.
- Rebuild passes; `PRAGMA integrity_check` = `ok`.
- Final scan: 0 hits for every defect class, and 0 Bengali characters outside the book tables.

### Known issue left open (by instruction)

`ruqyah_videos.subcat_id` values (105-117) come from the Bengali subcategory table, while the
workspace uses the 163-row English `ruqyah_subcategories` whose VIDEO entries are 150-163.
None of the 74 videos therefore reaches a video subcategory. Not fixed: the user does not use
the ruqyah video feature.

## Comparison against `translation_base` — 2026-09-08

The finished Japanese was compared table by table against the new standard workspace.
Row counts, key sets and frozen fields matched for all 11 tables. Three real defects
were found, all of them in places the earlier audit had not looked.

### Fixed

1. **`duas.transliteration` — 42 rows were still in Bengali script.** The README requires
   this field to be copied verbatim from `dua_main_en.sqlite`; these rows had kept the
   Bengali (`আল্লা-হুম্মা…` instead of `Allaahumma…`). Replaced from English.

2. **`duas.groups` — 35 rows shipped untranslated Bengali.** `groups` is a JSON string
   holding whole nested dua records; earlier work treated it as a frozen field, so its
   contents were never looked at. 67 nested records were carrying Bengali `name`,
   `content`, `translation` and `note` (13 138 characters), plus Bengali `transliteration`
   and `reference`. All 150 text fields translated to Japanese, reusing the wording already
   established in the main table for Surah al-Falaq, an-Nas, al-Ikhlas and al-Kafirun;
   the nested `transliteration` and `reference` copied from English.

3. `drawer_items` was confirmed to use ids 19-24, matching the Bengali database. The first
   version of `translation_base` sourced this table from English (ids 1-6) and would have
   produced drawer items the app cannot find. Fixed in the template.

### Verified and deliberately left alone

- `categories` and `subcategories` were translated from the **Bengali**, not the English,
  and were right to be. English category 2 is "Dua's Excellence", but the subcategory it
  contains is "Excellence of doing Tasbeeh, Tahmid, Tahlil, Takbeer" — that is dhikr, and
  the Bengali name says dhikr. Category 5 is "Morning & Evening" in English and
  "morning and evening dhikr" in Bengali, which matches its contents.
  `translation_base` now shows the Bengali reading alongside the English for these tables.

### Result

`dua_main_ja_rebuilt.sqlite` now contains **no Bengali in any field of any table outside
the excluded book tables**, nested JSON included. Structure, row counts and frozen fields
are unchanged from before the fixes; `PRAGMA integrity_check` = `ok`.

### Still open for Indonesian

`dua_main_id_planned_json` has the same `groups` issue (35 rows) and 686 rows of Bengali
`transliteration`. Its `duas` table is still largely untranslated (all 1001 names are
Bengali), so this is pending work rather than a shipped defect.

## Pre-release audit — 2026-09-08

A full pre-shipping audit of `dua_main_ja_rebuilt.sqlite`. Every field of every table was
checked, plus the nested JSON inside `duas.groups`.

### Fixed

| Issue | Count | Note |
|---|---:|---|
| `<b>text<b>` instead of `</b>` | 42 | upstream typo, faithfully copied; broke bold rendering from that point on |
| "on the authority of" as `の権限で` / `の権威に基づいて` | 82 | machine-translation of *عن*; now `〜が伝えるところによると` |
| `ナレーション` for *narration* | 24 | now `伝承` |
| `（ラー）` instead of `（RA）` | 31 | |
| Katakana name + `氏` / `さん` | 36 | `アブー・フライラ氏` → `アブー・フライラ`; `ラビ` (narrator) → `伝承者` |
| Duplicated reporting verb `と言った、と述べた` | 6 | |
| Invisible zero-width characters in Japanese prose | 44 | U+200B/200C/200E/200F left by machine translation; the 26 that sit next to Arabic were kept, since they are legitimate direction marks |
| Double spaces / full-width digits | 11 | |
| Mixed politeness register in narrative prose | 203 | `〜と述べた。` → `〜と述べました。`, `〜である。` → `〜です。` etc., in `dua_infos` and `ruqyah_details` only |

### Deliberately not changed

- **Qur'an translations keep their literary plain form.** `ruqyah_instants.translation` and
  the Qur'anic passages in `duas.translation` use `〜のだ。` / `〜投げ込もう。` / `〜何と醜悪なことか。`
  That is the correct register for scripture in Japanese; converting it to `です・ます` would
  have damaged 113 fields. The register fix was restricted to narrative prose, with quoted
  speech, Arabic blocks, citations and headings masked out.
- **`ruqyah_instants` id 225** uses `善い目／悪い目に遭う` — the idiom "to experience" in
  Qur'an 4:78, not the evil eye.
- **`ruqyah_videos.author`** keeps `氏` — these are living presenters, where it is correct.
- **Counting style is mixed on purpose**: `三回唱えます` in devotional prose, `7回` in the
  step-by-step ruqyah programmes. Both are correct Japanese for their context.
- 3 rows where the English database has a `note` that the Bengali original does not
  (`duas` 339 and 2 others). The workspace is Bengali-derived and `null` stays `null`.

### Verification

- Frozen fields checked against their source database for all 11 tables: **intact**.
- `duas.transliteration` differing from English: **0**.
- Bengali anywhere outside the book tables, nested JSON included: **0**.
- Unbalanced HTML tags: **0**. Invisible characters in prose: **0**. Mojibake: **0**.
- Foreign keys resolve; audio and video URLs well-formed; row counts unchanged.
- `PRAGMA integrity_check` = `ok`.
