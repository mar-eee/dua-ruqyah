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
| `tables/categories/categories_001.json` | 44 | complete |
| `tables/subcategories/subcategories_001.json` | 118 | complete |
| `tables/ruqyah_instants/ruqyah_instants_002.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_003.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_004.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_005.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_006.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_007.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_008.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_009.json` | 31 | complete; translated, references kept English |
| `tables/ruqyah_instants/ruqyah_instants_010.json` | 29 | complete; translated, references kept English |
| `tables/ruqyah_details/ruqyah_details_001.json` | 40 | complete; translated, inline references kept English |

### Indonesian completed: `tables/subcategories/subcategories_001.json`

- ID range: `1-118`
- Rows: `118`
- Completed on: `2026-08-28`
- Translated fields: `name`
- Source: English names from `dua_main_en.sqlite`; Bengali consulted only to resolve ambiguous English wording
- References: not applicable to this table
- Verification: second line-by-line editorial review completed; JSON valid, frozen fields unchanged, no Bengali remains, rebuild passed, SQLite integrity `ok`

### Indonesian completed: `tables/categories/categories_001.json`

- ID range: `1-44`
- Rows: `44`
- Completed on: `2026-08-28`
- Translated fields: `name`
- Source: English names from `dua_main_en.sqlite`
- Verification: editorial review against English categories and related subcategories passed; JSON valid, frozen fields unchanged, 44 Indonesian names present, rebuild passed, SQLite integrity `ok`

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
| `duas_009.json` | 273-306 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_010.json` | 307-340 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_011.json` | 341-374 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_012.json` | 375-408 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_013.json` | 409-442 | 34 | pending |  |
| `duas_014.json` | 443-476 | 34 | pending |  |
| `duas_015.json` | 477-510 | 34 | pending |  |
| `duas_016.json` | 511-544 | 34 | pending |  |
| `duas_017.json` | 545-578 | 34 | pending |  |
| `duas_018.json` | 579-612 | 34 | pending |  |
| `duas_019.json` | 613-646 | 34 | pending |  |
| `duas_020.json` | 647-680 | 34 | pending |  |
| `duas_021.json` | 681-714 | 34 | pending |  |
| `duas_022.json` | 715-748 | 34 | pending |  |
| `duas_023.json` | 749-782 | 34 | pending |  |
| `duas_024.json` | 783-816 | 34 | pending |  |
| `duas_025.json` | 817-850 | 34 | pending |  |
| `duas_026.json` | 851-884 | 34 | pending |  |
| `duas_027.json` | 885-918 | 34 | pending |  |
| `duas_028.json` | 919-952 | 34 | pending |  |
| `duas_029.json` | 953-986 | 34 | pending |  |
| `duas_030.json` | 987-1001 | 15 | pending |  |

## Work Status Details

### Indonesian completed: `dua_main_id_planned_json/tables/duas/duas_001.json`

- ID range: `1-34`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- Transliteration: copied from `dua_main_en.sqlite`
- References: copied from `dua_main_en.sqlite`, kept in English, and normalized to the README format
- Verification: JSON valid, no Bengali in translated top-level fields, English transliterations verified, frozen fields unchanged, rebuild passed, SQLite integrity `ok`
- Editorial recheck: all 34 rows reread against the English source; quotation flow, narrator spelling, and devotional phrasing corrected where needed

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
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English; ID `83` manually normalized to `Abu Dawud 4/322, no. 5084`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_005.json`

- ID range: `137-170`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Completed: `duas_006.json`

- ID range: `171-204`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Transliteration: copied from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

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

## Rebuild Command

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

- Qur'anic wording was checked against Saeed Sato's modern Japanese rendering and polished to match the database's calm, readable devotional style.
- Exact Arabic passages already translated in the Japanese workspace reuse the established wording.
- Source inconsistencies were resolved from the Arabic and verse title: ID `98` is Al-Mulk 67:1-4, and ID `184` is Al-Ahzab 33:70-71.

### Completed: `ruqyah_details_001.json`

- ID range: `1-40`
- Rows: `40`
- Completed on: `2026-09-05`
- Translated fields: `topic_name`, `text`
- Source: English rows from `dua_main_en.sqlite`
- References: inline citations kept in English; numbers unchanged
- Verification: JSON valid, Arabic and HTML structure unchanged, frozen fields and nullness intact, no Bengali in translated fields, rebuild passed, SQLite integrity `ok`

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
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_007.json`

- ID range: `205-238`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`

### Completed: `duas_008.json`

- ID range: `239-272`
- Rows: `34`
- Completed on: `2026-08-27`
- Translated fields: `name`, `content`, `translation`, `note`
- References: kept in English from `dua_main_en.sqlite`
- Verification: JSON valid, no Bengali in translated top-level fields, rebuild passed, SQLite integrity `ok`
