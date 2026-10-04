# Dua & Ruqyah translation master

`Dua_Ruqyah_Translation_Master.xlsx` is a translation-ready view of **every user table** in the four SQLite databases. It has one tab per table, plus Start Here, Coverage, Provenance, and this guide. The table tabs contain every row and every original column from their **selected** source database, followed by green Indonesian `id_*` editing columns and a status column. The workbook is not itself an app database.

## Exact source routing

| Selected source | Table tabs |
| --- | --- |
| Bengali (`dua_main_bn.sqlite`) | `duas`, `dua_infos`, `categories`, `subcategories`, `ids` |
| English (`dua_main_en.sqlite`) | `ruqyah_categories`, `ruqyah_subcategories`, `ruqyah_details`, `ruqyah_instants`, `ruqyah_videos`, `books`, `book_details`, `sections`, `drawer_items`, `drawer_item_actions` |

This follows the requested Bengali dua/dua-info source and English ruqyah/book source. The remaining drawer tables use English; the structural `ids` table follows Bengali. Japanese and Urdu database counts are shown for comparison in Coverage but are **not** silently substituted into source rows. The English `dua_infos` table is a different dataset from the Bengali one, despite overlapping IDs. English has only 2 book rows and 40 book-detail rows versus Bengali's 3 and 86; English has 40 ruqyah-video rows versus Bengali's 74. These gaps remain visible in Coverage.

## Editing safely

1. Open a table tab and filter `translation_status` to `not_started`.
2. Read the source row, including nested JSON in `duas.groups` and embedded HTML. Translate **all** user-visible text into the green `id_*` fields. Do not edit row keys, IDs, original columns, Arabic, source citations, links, or audio references.
3. A green blank means translation is pending. `⟦SQL NULL⟧` means SQL `NULL`; `⟦EMPTY STRING⟧` means the original value was the empty string. Keep these tokens distinct. The source columns use the same tokens so neither value is silently lost in Excel.
4. For `dua_infos`, all 42 Indonesian rows are prefilled from `dua_main_id_planned_json/tables/dua_infos`. Their status is `assistant_checked`, **not** human reviewed or fully Quran/hadith verified. Read the adjacent `REVIEW_DUA_INFOS_*.md` notes before publication.
5. Translate naturally and faithfully. Preserve Arabic character for character, including diacritics and honorifics. Keep markup, placeholders, meaning, negation, numbers, and conditions. Check Quran text and meanings against a verified Quran source and hadith against the exact narration; log unresolved points outside translated text.
6. This workbook is a working surface; do not import it directly into SQLite without a reviewed import/export process. The existing JSON and database rebuild scripts remain authoritative for the app.

The table tabs do **not** align different languages by numeric ID: some IDs represent different content. Coverage lists every database's row count and the chosen source. No row has been invented to fill a language gap.

Every selected-source value and every prefilled Indonesian `dua_infos` value fits Excel's 32,767-character cell limit. Rows are deliberately compact to browse; click a long-text cell and read its full content in the formula bar. Text beginning with `=` is stored as literal text, not a formula.

## Rebuild and verification

From the repository root:

```powershell
python general/build_translation_workbook.py
```

The builder refreshes the workbook from the current SQLite files and Indonesian `dua_infos` JSON, then reopens the workbook and compares each source cell and all 42 Indonesian `dua_infos` rows. It also records the four SQLite SHA-256 hashes in Provenance. **Rebuilding overwrites manual Excel edits** in green target cells; save your edited workbook under another name, or move translations into the JSON workspace first.

This Markdown file is reproduced in the workbook's Guide Markdown tab. Cell B5 stores the exact Markdown text, while column A displays it line by line.
