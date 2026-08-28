## Indonesian Translation Update — 2026-08-28

### Completed: `dua_main_id_planned_json/tables/subcategories/subcategories_001.json`

- ID range: `1-118`
- Rows: `118`
- Translated field: `name`
- Source: matching English rows from `dua_main_en.sqlite`
- Bengali usage: consulted only where the English wording was ambiguous
- Preserved fields: `id`, `cat_id`, JSON keys, row order, and nullness
- Language review: natural, clear Indonesian; Islamic terms and related category names checked for consistency
- Verification: JSON valid, no Bengali remains, structural comparison passed, rebuild passed, SQLite integrity `ok`

### Second editorial review: `subcategories_001.json`

- Reviewed on: `2026-08-28`
- Scope: all `118` Indonesian subcategory names checked again against the English source and parent categories
- Refinements: improved clarity and natural phrasing in 11 labels without changing their meaning
- Verification: frozen fields and row count preserved; encoding, JSON, rebuild, and SQLite integrity rechecked successfully

### Completed: `dua_main_id_planned_json/tables/duas/duas_001.json`

- ID range: `1-34`
- Rows: `34`
- Completed on: `2026-08-28`
- Translated fields: `name`, `content`, `translation`, `note`
- Source: matching English rows from `dua_main_en.sqlite`
- Transliteration: copied from the English database
- References: copied from the English database, kept in English, and normalized to README formatting
- Preserved fields: `id`, `groups`, `uthmani`, `indopak`, `clean`, `audio`, `cat_id`, `subcat_id`, JSON keys, row order, and nullness
- Language review: sincere, clear Indonesian with consistent Islamic terminology
- Verification: JSON valid, no Bengali in translated top-level fields, frozen fields unchanged, rebuild passed, SQLite integrity `ok`

### Editorial recheck: `dua_main_id_planned_json/tables/duas/duas_001.json`

- Reviewed on: `2026-08-28`
- Scope: all `34` rows reread against the English source and checked for natural Indonesian devotional wording
- Corrections: refined direct-address wording, repaired nested quotation flow, and corrected the narrator name `Busr bin Artha'ah`
- Verification: structural comparison, English transliteration/reference checks, rebuild, and SQLite integrity repeated successfully
