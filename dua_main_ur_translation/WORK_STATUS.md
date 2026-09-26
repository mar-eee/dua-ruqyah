# Urdu Translation Work Status

Generated: `2026-09-26T13:41:47+09:00`

> Status is calculated from work files. It does not treat the partial chunk index as the full project scope.

| Table | Source | Source rows | Chunks done | Target fields | State |
|---|---:|---:|---:|---:|---|
| `categories` | EN | 44 | 1/1 | 44/44 | translated/declared done; review gate still required |
| `ruqyah_categories` | EN | 15 | 1/1 | 15/15 | translated/declared done; review gate still required |
| `sections` | EN | 21 | 1/1 | 21/21 | translated/declared done; review gate still required |
| `subcategories` | EN | 118 | 3/3 | 118/118 | translated/declared done; review gate still required |
| `ruqyah_subcategories` | EN | 163 | 4/4 | 163/163 | translated/declared done; review gate still required |
| `books` | BN | 3 | 1/1 | 9/9 | translated/declared done; review gate still required |
| `ruqyah_videos` | BN | 74 | 2/2 | 148/148 | translated/declared done; review gate still required |
| `drawer_items` | BN | 6 | 2/2 | 105/105 | translated/declared done; review gate still required |
| `duas` | EN | 1001 | 64/64 | 2834/2834 | translated/declared done; review gate still required |
| `ruqyah_instants` | EN | 308 | 1/20 | 54/939 | in progress |
| `ruqyah_details` | EN | 200 | 0/95 | 0/307 | pending |
| `dua_infos` | BN | 42 | 0/70 | 0/238 | pending |
| `book_details` | BN | 86 | 0/49 | 0/176 | pending |
| `ids` | BN | 1001 | n/a | n/a | preserve and verify |
| `drawer_item_actions` | EN | 0 | n/a | n/a | preserve and verify |

## Totals

- Existing indexed chunks declared done: **80/313 (25.6%)**
- Existing indexed target fields filled: **3511/5117 (68.6%)**
- Required tables missing from the index: **none**
- Final build: **BLOCKED**
- Natural-Urdu review: **not inferable from filled fields; record review evidence per chunk**

## Next action

Continue with `work/ruqyah_instants/ruqyah_instants_002.json`, then run the per-file verifier and naturalness review.

## Completion rule

The project is complete only when every required table is in scope, every target is translated, each chunk is structurally verified and reviewed for natural Urdu, and the final SQLite database passes integrity, schema, row-count, key-set, and residual-language checks.
