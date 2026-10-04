# Indonesian `dua_infos` work chunks

Work through one JSON file per translation prompt, in numerical order. Each
entry stays whole; no source text was changed when the original two files were
split. The larger single-entry files are long because splitting a database row
would make translation and rebuilding less reliable.

| File | Entry IDs | Rows |
| --- | ---: | ---: |
| `dua_infos_001.json` | 1–4 | 4 |
| `dua_infos_002.json` | 5–7 | 3 |
| `dua_infos_003.json` | 8 | 1 |
| `dua_infos_004.json` | 9–12 | 4 |
| `dua_infos_005.json` | 13–16 | 4 |
| `dua_infos_006.json` | 17–19 | 3 |
| `dua_infos_007.json` | 20–23 | 4 |
| `dua_infos_008.json` | 24–27 | 4 |
| `dua_infos_009.json` | 28–31 | 4 |
| `dua_infos_010.json` | 32 | 1 |
| `dua_infos_011.json` | 33 | 1 |
| `dua_infos_012.json` | 34 | 1 |
| `dua_infos_013.json` | 35–36 | 2 |
| `dua_infos_014.json` | 37–40 | 4 |
| `dua_infos_015.json` | 41–42 | 2 |

Keep the same IDs and JSON structure when translating. The rebuild reads these
files in the order listed in `../../_database_metadata.json`.
Translation and review status are recorded in
[`../../translation_progress.json`](../../translation_progress.json).
