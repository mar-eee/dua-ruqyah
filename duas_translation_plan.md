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

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_categories/ruqyah_categories_001.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `1-15`; rows: `15`
- Completed on: `2026-09-28`
- Translated and rechecked fields: `name`
- Source: all exact English rows in `dua_main_en.sqlite`; no Bengali fallback needed.
- References: not applicable; this chunk contains no reference or transliteration fields.
- Verification: All 15 exact English IDs matched and all names reviewed. JSON, UTF-8, 2-space indentation, trailing newline, row/key order, types, icons, protected fields, nullness and digits passed; no Bengali remains. Equivalent Node.js rebuild passed; reopened SQLite integrity ok; all 15 tables / 3082 rows match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: All names reviewed for meaning, completeness, natural Indonesian, spelling and grammar. Related subcategories checked and left unchanged; existing Indonesian term penyakit ain retained. Instant Ruqyah rendered as Ruqyah langsung for direct access to recitations; Raqi as peruqyah; Hijamah as bekam with the separate bloodletting meaning preserved.
- Status recorded in the existing shared work_status registry in Japanese metadata, following the plan's status instruction; all schema metadata unchanged. Python unavailable; equivalent Node.js rebuild used.
- Final artifact: `dua_main_id_rebuilt.sqlite`; temporary backup, helper and intermediate database removed after verification.

### Indonesian independent recheck: `dua_main_id_planned_json/tables/ruqyah_categories/ruqyah_categories_001.json`

- Status: complete; reviewed on `2026-09-28`
- ID range: `1-15`; rows: `15`
- Reviewed fields: `name`; corrected ID: `11`
- References: not applicable; no reference or transliteration fields.
- Verification: All 15 records reviewed one by one against exact English IDs. JSON, UTF-8, 2-space indentation, trailing newline, row/key order, IDs, type values, icons, protected fields, nullness and digits verified; no Bengali or unintended English in names. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm no other translation file changed.
- Review notes: Changed Waswas dan bisikan to Waswas (bisikan) to preserve the English explanatory relationship. All other 14 names retained after reviewing meaning, natural wording, Islamic terminology, spelling, grammar, capitalization and completeness. Python unavailable; equivalent Node.js rebuild used unchanged Indonesian schema metadata.
- Temporary backup, helper and verification database removed; `dua_main_id_rebuilt.sqlite` also removed as requested, superseding the preceding batch's retained-artifact note.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_001.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `1-40`; rows: `40`
- Completed on: `2026-09-28`
- Translated and second-pass reviewed fields: `text` (40), `topic_name` (4 non-null, IDs 25, 26, 27 and 40); all other topic names remain null.
- Source: exact English rows in `dua_main_en.sqlite`; no Bengali fallback required.
- References: English, not translated; inline references and citation numbers preserved. No separate reference field. All standalone and inline transliterations retained verbatim; their display labels translated.
- Verification: All 40 exact English IDs matched; all 40 text fields and four non-null topic_name fields translated and rechecked record by record. JSON, UTF-8, 2-space indentation, trailing newline, row/key order, protected values and nullness passed. All 521 paragraph segments and original newline runs preserved, including whitespace-only lines; HTML tag sequence and nesting valid; 51 Arabic blocks, all Arabic characters, seven standalone transliterations and inline transliterations preserved. Inline reference strings, citation numbers and all digits retained. No Bengali or unintended English prose remains. Equivalent Node.js rebuild passed; reopened SQLite integrity ok; all 15 tables / 3082 rows match JSON; schema, sequences and pragmas verified. Git scope check confirms no other translation file changed; source databases, Indonesian schema metadata and rebuild script hashes unchanged.
- Review notes: Second pass corrected timing in ID 15, wording about the jinn in ID 23, persuade in ID 29, added oil in ID 33, and wording in ID 40; restored parenthetical glosses and bracketed meanings where needed. Retained source citation/numbering quirks (including 17:81-2 in ID 1, verse 7 in ID 17, item 16 in ID 25), source honorifics, quotation structure and protected Arabic/transliteration spelling. Repaired ordinary prose typos and malformed wording without adding claims, including Sinn in ID 34, mengine in ID 30 and the missing eating verb in ID 38. Existing English reference text and source book titles remain protected; no separate reference field exists. No Bengali fallback needed. Python unavailable; equivalent Node.js rebuild followed the existing Python script. All task temporary files and dua_main_id_rebuilt.sqlite removed after verification.
- Status recorded in the existing shared `work_status` registry in Japanese metadata, following the plan instruction; schema metadata unchanged.
- Cleanup: temporary backup, translation draft, apply/validation/status helpers and verification results removed, including `dua_main_id_rebuilt.sqlite`; no database artifact retained.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_002.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `41-80`; rows: `40`
- Completed on: `2026-09-28`
- Translated and second-pass reviewed fields: `text` (40), `topic_name` (15 non-null, IDs 41-43, 49-51 and 72-80); all other topic names remain null.
- Source: exact English rows in `dua_main_en.sqlite`; no Bengali fallback.
- References: English, not translated; inline references and citation numbers preserved. No separate reference field. All transliterations retained verbatim; display labels translated.
- Verification: All 40 exact English IDs (41-80) matched. All 40 text fields and 15 non-null topic_name fields translated and reviewed a second time, paragraph by paragraph. JSON, UTF-8, 2-space indentation, trailing newline, row/key order, protected fields, IDs, nullness, 520 paragraph segments, newline runs, whitespace-only segments, bracket structure, numbering and all digits verified. All 54 Arabic blocks and Arabic characters, 23 transliterations, inline references, URLs and HTML tag sequences preserved. No Bengali, unintended English prose, unresolved placeholders or broken escape sequences. Original malformed bold tags at ID 53 retained under the explicit tag-preservation instruction; no new HTML issues. Equivalent Node.js rebuild passed; reopened integrity ok; all 15 tables / 3082 rows match JSON; schema, sequences and pragmas verified. SHA-256 checks confirm every other translation file, source database, Indonesian schema metadata and rebuild script unchanged.
- Review notes: Second pass restored parenthetical meanings at IDs 42 and 45, refined Indonesian wording, retained the exact Chapter 62 reference, and resolved green lotus in ID 66 as green bidara leaves using matching Sidr/Ziziphus treatment context in English IDs 122, 142 and 148. Bengali ID 66 was inspected for ambiguity but describes a different passage and was not used as a translation source; no Bengali fallback needed. Exact duplicate ID 50 follows reviewed ID 19 in the preceding Indonesian chunk after verifying identical English source; IDs 68 and 69 use identical translations. Repeated Quran passages checked against the earlier reviewed wording. Source anomalies retained rather than silently rewritten: ID 45 references 36:29 and Chapter 62 and attributes circulation through the body to the Prophet; lowest rank at ID 47; does know at ID 56; three types followed by four entries and queen-bee honey wording at ID 67; All-Seeing in IDs 66 and 71; accusing eye at ID 71; the citation containing bold markup at ID 78. Original quotation/numbering quirks and protected spelling retained. Obvious prose typos such as vetem, anicured, sini, al-ast and the stray A were resolved in Indonesian. Python unavailable; Node.js followed the existing rebuild script. All task temporary files and dua_main_id_rebuilt.sqlite removed after verification.
- Status recorded in the existing shared `work_status` registry in Japanese metadata, following the plan instruction; schema metadata unchanged.
- Cleanup: all task backup, draft, apply/validation/status scripts, state and verification files removed, including `dua_main_id_rebuilt.sqlite`; no database artifact retained.

### Indonesian final verification: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_002.json`

- Status: `complete`; final verification complete.
- ID range: `41-80`; rows: `40`
- Completed on: `2026-10-02`
- Reviewed fields: `text` (40), `topic_name` (15 non-null); null topic names unchanged.
- References: English, not translated; inline references preserved verbatim.
- Verification: All 40 exact English IDs (41-80), 40 text fields and 15 non-null topic_name fields rechecked for meaning, completeness and natural Indonesian. JSON/UTF-8, 2-space indentation, trailing newline, row/key order, all protected values and nullness verified. All 54 Arabic blocks, Arabic characters, 23 transliterations, inline references, URLs, digits and newline runs preserved. HTML nesting passes after repairing seven malformed closing bold tags at ID 53 as requested. No Bengali, unintended English prose or broken newline escapes. Equivalent Node.js SQLite rebuild passed; reopened integrity_check ok; all 15 tables / 3082 rows match JSON; schema SQL, sequences and pragmas verified. SHA-256 checks confirm all other translation files, source databases, Indonesian schema metadata and rebuild scripts unchanged.
- Review notes: Final review corrected unnecessary-action meaning (44), nourishment wording (42), signal direction (59), side-lying phrasing (58), unspecified wedding-day wording (72), and prayer-follower role (80). Improved grammar, spelling, punctuation, quotation closure and spacing; removed stray punctuation; repaired malformed bold tags (53). All non-null topic names retained after review. English inline references and prior documented source anomalies retained exactly. Python unavailable; Node.js reproduced the repository rebuild procedure.
- Status updated only in this plan and the existing shared `work_status` entry in Japanese metadata; schema metadata unchanged.
- Cleanup: task backup/state, verification helper and `dua_main_id_rebuilt.sqlite` removed after verification; no commit or push.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_003.json`

- Status: `pending` → `complete` (Indonesian)
- ID range: `81-120`; rows: `40`
- Completed on: `2026-10-02`
- Translated and second-pass reviewed fields: `text` (40), `topic_name` (7 non-null, IDs 81-87); other topic names remain null.
- Source: exact English rows in `dua_main_en.sqlite`; no Bengali fallback.
- References: English, not translated; inline references and bibliographic titles preserved verbatim. No separate reference field. Transliterations retained verbatim; labels translated.
- Verification: All 40 exact English IDs (81-120) matched. Every text field and all seven non-null topic_name fields translated and second-pass reviewed for meaning, completeness, natural Indonesian, spelling and grammar. JSON, UTF-8, 2-space indentation, trailing newline, row/key order, protected fields and nullness verified. All 393 paragraph segments, newline runs, whitespace-only segments, four U+2028 line separators (IDs 91 and 96), HTML tag sequence/nesting, quotation marks and digits preserved. All 26 Arabic blocks and Arabic characters, 10 transliterations, references, titles and URLs preserved. No Bengali, unintended English prose, unresolved temporary placeholders or incorrect newline escapes. Equivalent Node.js SQLite rebuild passed; reopened integrity_check ok; all 15 tables / 3082 rows match JSON; schema SQL, sequences and pragmas verified. SHA-256 checks confirm every other translation file, source database, Indonesian schema metadata and rebuild script unchanged.
- Review notes: English remained the source for every record; no Bengali fallback required. Complete repeated narrations retained. Translatable explanatory brackets and parentheses translated, including IDs 109, 112 and 117. Second pass refined jin-manifestation wording (120) and translated the descriptive parenthesis in 115. Recovered the meaning of the corrupted sentence in 99 and split definition in 106 without moving paragraphs. Source anomalies retained: incomplete citation and quotations (81), Allah (RA) (82), ten deeds wording (83), All-Seeing (85), citation markup (92), quotation/parenthesis irregularities, Albatross snake name and soul-influence wording (101), source addressee (102), washing instructions and narration wording (104), dialogue roles (105), Shirk in the treatment definition (106), and the application of 24/2 to sorcerers (108). English bibliographic text, article/book/video titles and original citation Unicode retained verbatim as instructed. Python unavailable in this environment; Node.js reproduced the repository rebuild procedure.
- Status recorded in the existing shared `work_status` registry in Japanese metadata, following README; schema metadata unchanged.
- Cleanup: task backup/state, templates, translation drafts, apply/validation/status helpers, verification results and `dua_main_id_rebuilt.sqlite` removed; no database artifact retained. No commit or push.

### Indonesian final independent review: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_003.json`

- Status: `complete`; independent final review complete.
- ID range: `81-120`; records reviewed: `40`.
- Completed on: `2026-10-02`.
- Reviewed fields: `text` (40), `topic_name` (7 non-null); nulls unchanged.
- Corrected IDs: `94, 99, 108, 110, 115, 116` (6 records); other 34 records retained.
- References: English, not translated; protected citations and transliterations preserved verbatim.
- Verification: Independent line-by-line review of all 40 exact English IDs (81-120), all 40 text fields and seven non-null topic_name fields completed against dua_main_en.sqlite and README.md. Meanings, instructions, warnings, conditions, sequences, negations, religious statements, names and honorifics reviewed. JSON/UTF-8, 2-space indentation, trailing newline, row/key order, nullness and protected fields pass. All 393 paragraph segments, whitespace edges, newline sequences, four U+2028 separators, quotation marks, numbers, HTML tags/nesting, 26 Arabic blocks, Arabic characters, 10 transliterations and references preserved. No Bengali, unintended English prose or incorrect escapes. Equivalent Node.js rebuild passed; reopened integrity_check ok; all 15 tables / 3082 rows exactly match JSON; schema SQL, sequences and pragmas verified. SHA-256 scope checks confirm no other translation file, source database, Indonesian schema metadata or rebuild script changed.
- Review notes: Corrected only IDs 94, 99, 108, 110, 115 and 116: Indonesian grammar in the final paragraph (94); knight as kesatria (99); scope of a certain level across faith and religious practice (108); future-completed time frame (110); removed unsupported ownership wording from the Masjid Humera descriptor (115); made avoidance apply unambiguously to both major sins and repeated minor sins (116). All seven topic names and remaining 34 records retained. Documented source anomalies, incomplete quotations and references remain unchanged. Python unavailable; Node.js reproduced the existing rebuild procedure.
- Status updated only in this plan and the existing exact shared work_status entry in Japanese metadata; schema unchanged.
- Cleanup: task backup/state, validator, results and `dua_main_id_rebuilt.sqlite` removed after verification. No commit or push.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_004.json`

- Status: `pending` → `complete` (Indonesian).
- ID range: `121-160`; records reviewed: `40`.
- Completed on: `2026-10-02`.
- Translated and independently second-pass reviewed fields: `text` (40), `topic_name` (13 non-null); all null values unchanged.
- Second-pass corrected IDs: `122, 123, 124, 128, 129, 130, 131, 132, 134, 136, 138, 139, 140, 141, 147, 149, 160` (17 records).
- References: English, not translated; inline references, gradings, bibliographic titles and transliterations preserved verbatim.
- Verification: All 40 exact English IDs (121-160), all 40 text fields and 13 non-null topic_name fields translated and independently rechecked line by line against dua_main_en.sqlite and README.md. Instructions, warnings, conditions, sequences, negations, religious statements, terminology, names and honorifics reviewed. JSON/UTF-8, 2-space indentation, trailing newline, row/key order, nullness and protected fields pass. All 471 paragraph segments, newline runs, whitespace edges, digits, double quotation marks, parentheses counts, 33 Arabic blocks and Arabic characters, 12 transliterations and protected references verified. Both U+200B characters at ID 136 preserved; no U+2028, U+2029 or U+0085 line separators occur in this source chunk. Repaired 31 malformed closing bold tags at ID 122 under the latest instruction to correct broken HTML; all other HTML tags preserved and nesting passes. No Bengali, unintended English prose, unresolved temporary placeholders or broken newline escapes. Remaining English is protected citations/gradings, reference titles, names, transliterations and explicitly identified terminology. Equivalent Node.js rebuild passed; reopened integrity_check ok; all 15 tables / 3082 rows exactly match JSON; schema SQL, sequences and pragmas verified. SHA-256 checks confirm every other translation file, source database, Indonesian schema metadata and rebuild script unchanged.
- Review notes: Second-pass corrections: repaired source HTML (122); restored the scope of the authenticity claim (123); retained normality wording (124); standardized habbatussauda and clarified digestive gas as perut kembung (128); clarified divine will and restored explanatory parentheses (129); preserved parentheses structure in honey etymology wording (130); avoided restricting other diseases to hair and preserved parenthesis count (131); corrected dry-spitting instruction (132); corrected a couple of years to approximately two years (134); removed unsupported oil specification for musk (136); restored parentheses (138), parenthetical gloss (139) and healer description (140); removed an unsupported between-the-sermons restriction (141); corrected regularity versus frequency and Indonesian wording (147); refined bracketed Quran translation grammar and immersion wording (149); removed unsupported scholar/two-form specifications (160). All 40 records and 13 topic names reviewed; remaining records retained after the first pass. English source used for every ID; no Bengali fallback. Source anomalies retained rather than silently rewriting meaning: differing senna quantities/timing and hair-spread wording (123-124), original narration/citation spellings, honey etymology claim (130), repeated ingredient sequence (136), magician wording (137), Israa description (139), damaged honorific legalaw resolved as an honorific and original mismatched citation bracket retained (142), first/third-person statement (158), and the original medical claims and advice throughout. Original incomplete quotation marks retained as requested. Python is unavailable; Node.js reproduced the repository rebuild procedure.
- Status updated only in this plan and the exact entry in the existing shared `work_status` registry in Japanese metadata, as required by README; schema metadata unchanged.
- Cleanup: all `.r004` task backup/state, templates, drafts, first-pass snapshot, apply/review/correction/validation/rebuild/status helpers and result files, plus `dua_main_id_rebuilt.sqlite`, removed after verification. No other translation file modified. No commit or push.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_details/ruqyah_details_005.json`

- Status: `pending` → `complete` (Indonesian).
- ID range: `161-200`; records reviewed: `40`.
- Completed on: `2026-10-02`.
- Translated and independently second-pass reviewed fields: `text` (40), `topic_name` (28 non-null); all null values unchanged.
- Second-pass corrected IDs: `161, 162, 165, 166, 170, 171, 175, 177, 182, 186, 188, 189, 191, 192, 193, 194, 199, 200` (18 records).
- References: English, not translated; inline citations, gradings, bibliographic titles and transliterations preserved verbatim.
- Verification: All 40 exact English IDs (161-200), all 40 text fields and 28 non-null topic_name fields translated and independently reviewed line by line against dua_main_en.sqlite and README.md. Meaning, instructions, warnings, conditions, sequences, negations, religious statements, names, honorifics and terminology checked. JSON/UTF-8, 2-space indentation, trailing newline, row/key order, nullness and all protected fields pass. All 282 paragraph segments, newline runs and whitespace edges, digits, double quotation marks, parenthesis counts, HTML tag sequences, five Arabic blocks and Arabic characters, three transliterations, URLs, references and bibliographic titles preserved. Source has no U+2028, U+2029, U+0085, U+200B or U+FEFF characters in its text; no line terminators normalized. Original malformed bold tags in ID 163 retained under the explicit all-tags preservation instruction; no new HTML defects. No Bengali, unintended English prose, unresolved temporary placeholders or incorrect newline escapes. Remaining English consists of protected citations, gradings, reference titles, search phrases, proper names and identified terminology. Node.js equivalent of the repository rebuild passed; reopened integrity_check ok; all 15 tables / 3082 rows match every JSON value; schema SQL, sequences and pragmas verified. SHA-256 scope check confirms all other translation files, source databases, Indonesian schema metadata and rebuild script unchanged.
- Review notes: Second-pass corrected IDs: 161, 162, 165, 166, 170, 171, 175, 177, 182, 186, 188, 189, 191, 192, 193, 194, 199, 200. Corrections restore parenthetical dashes (161), blackcurrant ingredient identity without substituting raisins or black seed (162), Islamic exorcism terminology (165), win/lose distinction and to-Himself meaning (166), categorical not-correct meaning (170), Yang energy capitalization (171), repeated Nabi (SAW) honorific and list spacing (175), bleeding wording (177), drug-use scope without restricting it to narcotics (182), natural personality wording (186), leaden color as timbal (188), injury rather than mere disturbance (189), list punctuation and organ singular/plural parenthesis (191), five-centers terminology (192), comparative coldness (193), intended audience wording (194), afternoon timing (199), and translated abbreviation punctuation (200). All 28 topic names independently reviewed. IDs 167-169 use the reviewed wording of 137-139 after exact English text equality was verified, followed by another line-by-line review; other translation files were read only. English source used for every ID; no Bengali fallback. Source anomalies retained: blackcurrant ingredient and Al-Baqarah 284-287 reference (162), malformed HTML/transliteration punctuation (163), original magician wording (167), Israa description and reference spelling (169), mismatched citation bracket and stray parenthesis (172), mixed quotation styles (184 and 189), and source medical/legal claims throughout. Obvious English prose typos resolved in Indonesian. The b1 typo in 166 is rendered nomor 1. Original unmatched parentheses and quotation marks retained where required. Python unavailable in this session; Node.js followed the existing Python rebuild procedure without modifying it.
- Status updated only in this plan and the exact existing shared `work_status` registry entry in Japanese metadata, as required by README; schema metadata unchanged.
- Cleanup: all `.r005` task backups/state, templates, drafts, first-pass snapshot, review/correction/apply/validation/rebuild/status helpers and result files, plus `dua_main_id_rebuilt.sqlite`, removed after verification. No other translation file modified. No commit or push.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_instants/ruqyah_instants_001.json`

- Status: `pending` → `complete` (Indonesian).
- ID range: `1-31`; records translated and independently second-pass reviewed: `31`.
- Completed on: `2026-10-05`.
- Translated fields: `topic_name` (31), `name` (16 Quran titles; 15 bibliographic names retained), `content` (2; 29 nulls unchanged), `translation` (31): 80 changed field values.
- References: English, not translated; references and transliterations copied verbatim from exact English rows and unchanged from backup.
- Second-pass corrected IDs: `1, 3, 5, 13, 22, 30` (6 records). Removed unsupported exclusivity in praise wording (1, 3, 5), clarified Sustainer wording (13), restored escape/avoidance meaning (22, 30). All 31 records reviewed individually, including differences between repeated prayers; unmatched source quotation marks retained.
- Verification: All 31 exact English ruqyah_instants IDs (1-31) matched and independently reviewed line by line. JSON/UTF-8, two-space indentation, trailing newline, row/key order, nullness, all protected fields, Arabic, URLs, digits, HTML tag sequences, newline escapes and unusual Unicode preserved. Transliteration and reference copied verbatim from English and also identical to backup; references ASCII English, not translated. No Bengali or unintended English prose. Node.js equivalent of the unchanged repository Python rebuild used because Python cannot run. Reopened integrity_check ok; all 15 tables / 3082 rows compared value by value with JSON; schema SQL, sequences and pragmas verified. SHA-256 checks confirm every other translation file, source database, Indonesian schema metadata and rebuild script unchanged.
- Database row counts: categories=44; subcategories=118; dua_infos=42; duas=1001; ruqyah_categories=15; ruqyah_details=200; ruqyah_instants=308; sections=21; ruqyah_subcategories=163; books=3; book_details=86; ids=1001; ruqyah_videos=74; drawer_items=6; drawer_item_actions=0.
- Status updated only in this plan and the exact path in the existing Japanese metadata work_status registry, as required by README; schema metadata unchanged.
- Cleanup: all task scripts, backup, first-pass draft, hash state and verification result files, plus `dua_main_id_rebuilt.sqlite`, removed after verification. No other translation file modified. No commit or push.

### Indonesian completed: `dua_main_id_planned_json/tables/ruqyah_instants/ruqyah_instants_002.json`

- Status: `pending` → `complete` (Indonesian).
- ID range: `32-62`; records translated and independently second-pass reviewed: `31`.
- Completed on: `2026-10-05`.
- Translated fields: `topic_name` (31), `name` (14 Quran titles; 17 bibliographic names retained), `content` (5; 26 nulls unchanged), `translation` (31): 81 changed field values.
- References: English, not translated; references and transliterations copied verbatim from exact English rows and unchanged from backup.
- Second-pass corrected IDs: `32, 36, 40, 43, 47, 49, 53, 54, 56` (9 records). Second pass corrected instruction order and refuge phrasing (32, 40, 54), fighting as berperang (36), natural knot-blowing wording (43), precise versus unspecific verse meanings and bracketed scope (47), retreating whisperer wording (49), unlearned and notification-duty wording (53), and restored the explanatory bracket around all (56). All repeated records individually reviewed. Quran titles localized in 14 names; 17 bibliographic names retained. Five non-null content fields translated, 26 null content fields preserved. Source unmatched quotation marks and distinct English meanings retained; no Bengali fallback.
- Verification: All 31 exact English ruqyah_instants IDs (32-62) matched; every applicable topic_name, name, content and translation independently reviewed line by line against its exact English row after translation. JSON/UTF-8, two-space indentation, trailing newline, row/key order, nullness, all protected fields, Quranic Arabic, URLs, digits, HTML tag sequences, newline escapes, unusual Unicode and quotation/bracket counts verified. References and transliterations copied verbatim from English and identical to backup; references ASCII English, not translated. No Bengali or unintended English prose. Node.js followed the unchanged repository rebuild script because Python was unavailable in this environment. Reopened integrity_check ok; all 15 tables / 3082 rows compared value by value with JSON, including 308 ruqyah_instants rows; schema SQL, sequences and pragmas verified. SHA-256 scope checks confirm every other translation file, source database, Indonesian schema metadata and rebuild script unchanged.
- Database row counts: categories=44; subcategories=118; dua_infos=42; duas=1001; ruqyah_categories=15; ruqyah_details=200; ruqyah_instants=308; sections=21; ruqyah_subcategories=163; books=3; book_details=86; ids=1001; ruqyah_videos=74; drawer_items=6; drawer_item_actions=0.
- Status updated only in this plan and the exact JSON path in the existing Japanese metadata work_status registry, as required by README; schema metadata unchanged.
- Cleanup: all task scripts, backup, first-pass draft, hash state and verification result files, plus `dua_main_id_rebuilt.sqlite`, removed after verification. No other translation file modified. No commit or push.
