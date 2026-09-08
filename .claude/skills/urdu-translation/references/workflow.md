# Workflow and mechanics

## Layout

```
Dua/
├── dua_main_en.sqlite  dua_main_bn.sqlite    sources
├── translation_base/                          template — never translate here
└── dua_main_ur_translation/                   work here
    ├── GLOSSARY.json      fill first
    ├── PLAN.md            263 files, in working order
    ├── work/<table>/<table>_NNN.json          you edit these
    ├── source/{en,bn}/<table>.json            reference only
    └── scripts/  verify.py · build.py · status.py · generate.py
```

## File format

```jsonc
{ "table": "subcategories", "status": "pending",   // → "done" when finished
  "items": [{
    "key": [1], "id": 1, "part": 1, "of": 1,       // never change
    "frozen": { … },                                // context only
    "source": { "name": "The servant is dependent on his Lord" },
    "target": { "name": "" },                       // ← write here
    "reference_bn": { "name": "বান্দা তার রবের মুখাপেক্ষী" }
  }]}
```

Edit `target` only. `null` source → `null` target, never `""`. Never add/remove/reorder items.

- `drawer_items` rows also have `content_sections` — fill each `target`.
- `duas` rows may have `group_items` — nested dua records inside `duas.groups`. **These are
  user-visible and must be translated.** Treating `groups` as frozen is how Bengali shipped
  inside the Japanese and Indonesian databases.

## Source per table

English by default. Three are Bengali, because the English DB holds a *different dataset*:

| Table | Source | Why |
|---|---|---|
| `dua_infos` | BN | EN has 16 unrelated rows; BN has the 42 the app uses |
| `ruqyah_videos` | BN | EN has 40 English videos; BN has the 74 the links point to |
| `drawer_items` | BN | EN numbers rows 1–6; the app uses 19–24 |

## Field rules

| Never change | Translate | Copy from English |
|---|---|---|
| `id`, `key`, `cat_id`, `subcat_id`, `topic_id`, `book_id`, `section_id`, `audio`, `link`, `uthmani`, `indopak`, `clean` | `name`, `title`, `content`, `translation`, `note`, `description`, `topic_name`, `text`, `hero_title1/2` | `transliteration`, `reference` |

## Reference format

```text
Surah Al-Fatir 35:15              Quran: Surah Name chapter:verse
Bukhari: 844                      Hadith: Collection: Number
Sahih (Albani). Abu Dawud: 1522   grading first, then a period
Bukhari: 6403; Muslim: 2693       multiple sources, semicolon
```

ASCII digits. One space after the colon, none before. Drop `No`.

## Commands

```bash
cd dua_main_ur_translation
python3 scripts/verify.py work/duas/duas_001.json   # one file
python3 scripts/verify.py duas                       # one table
python3 scripts/status.py                            # progress
python3 scripts/build.py ur                          # → ../dua_main_ur.sqlite
python3 scripts/build.py ur --partial                # preview with gaps
```

## Chunking

Sized by translatable characters (6 000 budget, ≤50 rows, long rows split at paragraph
boundaries). Median ~5 400 chars.

In the Japanese work, the two tables with the biggest chunks — `dua_infos` at ~178 000
chars/file and `ruqyah_details` at ~46 000 — were the only two that came out as unusable
machine translation. **Chunk size, not language difficulty, was the cause. Do not batch
files together.**

## verify.py checks

Invalid JSON · changed field sets · added/removed items · null-rule violations · empty
targets · source-language characters in target · HTML tags changed · Arabic lost · **any
digit differing from source** · known corruption patterns · glossary term not used · one
term spelled two ways · frozen fields in source-language script.

It cannot hear whether the Urdu sounds human. That part is yours.

## GLOSSARY.json

`canonical` — if a source field mentions the term, the translation must contain the value.
Enforced.
`overrides` — switch that off for one field when the English source is wrong. Give a reason:

```json
"overrides": { "categories.name.2": "EN says \"Dua's Excellence\" but the category holds Tasbeeh/Tahmid/Tahlil/Takbeer; BN says dhikr." }
```

`settled_wording` — not enforced; shared memory so later files match earlier ones.

## ⚠ generate.py destroys work/

`python3 scripts/generate.py` rebuilds the workspace and **overwrites `work/`, destroying
any translation in it.** Commit or copy first. This already cost one real data loss: a
completed 200-row Japanese table, recovered only from git history.
