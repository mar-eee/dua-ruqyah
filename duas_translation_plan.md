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
| `duas_009.json` | 273-306 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_010.json` | 307-340 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_011.json` | 341-374 | 34 | complete | translated; references kept English; transliteration copied from EN |
| `duas_012.json` | 375-408 | 34 | complete | translated; references kept English; transliteration copied from EN |
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
