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
