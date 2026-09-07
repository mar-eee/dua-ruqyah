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
| `duas_009.json` | 273-306 | 34 | complete | Japanese complete; Indonesian complete 2026-09-07; references kept English; transliteration copied from EN |
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
