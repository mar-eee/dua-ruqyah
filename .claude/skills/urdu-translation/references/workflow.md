# Workflow and mechanics

Everything here is about *how the workspace works*. The judgement calls are in `SKILL.md`.

## Where things are

```
Dua/
├── dua_main_en.sqlite            English source
├── dua_main_bn.sqlite            Bengali source
├── translation_base/             the language-neutral template — do not translate in here
└── dua_main_ur_translation/      the Urdu workspace — this is where you work
    ├── GLOSSARY.json             fill this in first
    ├── PLAN.md                   checklist of all 263 files, in working order
    ├── work/<table>/<table>_NNN.json    the files you edit
    ├── source/en/<table>.json    full English rows, reference only
    ├── source/bn/<table>.json    full Bengali rows, reference only
    └── scripts/
        ├── verify.py             quality gate
        ├── build.py              work/ → dua_main_ur.sqlite
        ├── status.py             progress
        └── generate.py           rebuilds the workspace — DESTROYS work/, see warning below
```

## The file format

```jsonc
{
  "table": "subcategories",
  "chunk": "subcategories_001.json",
  "source_language": "en",
  "target_language": "ur",
  "status": "pending",        // set to "done" when finished
  "rows": 50,
  "id_range": "1-50",
  "source_chars": 1514,
  "items": [
    {
      "key": [1],             // row identity — never change
      "id": 1,
      "part": 1, "of": 1,     // a long row split into parts
      "frozen": { … },        // context only, never edit
      "source": { "name": "The servant is dependent on his Lord" },
      "target": { "name": "" },              // ← you write here
      "reference_bn": { "name": "বান্দা তার রবের মুখাপেক্ষী" }
    }
  ]
}
```

Edit `target` and nothing else.

- `null` in `source` stays `null` in `target`. Never `""`.
- Never add, remove or reorder items.
- `drawer_items` rows also have `content_sections`; fill each `target` there. Section
  order, types and spacer heights are handled for you.
- `duas` rows may have `group_items` — nested dua records inside `duas.groups`. These are
  user-visible text and must be translated. Earlier workspaces treated `groups` as frozen,
  which is how Bengali shipped inside the Japanese and Indonesian databases.

## Chunking

Files are sized by translatable characters, not row count: a 6 000-character budget, at
most 50 rows, and rows larger than one budget split at paragraph boundaries. Median file
is ~5 400 characters. Nothing exceeds the budget.

This matters. In the Japanese work the two tables with the largest chunks — `dua_infos` at
~178 000 characters per file and `ruqyah_details` at ~46 000 — were the only two that came
out as unusable machine translation. Everything chunked small came out fine. Chunk size,
not language difficulty, was the cause. Do not batch files together to save round trips.

## Which database each table comes from

English is the default source. Three tables are Bengali, because the English database
holds a *different dataset* for them rather than a translation of the same rows:

| Table | Source | Why |
|---|---|---|
| `dua_infos` | **BN** | English has 16 unrelated rows; Bengali has the 42 the app uses |
| `ruqyah_videos` | **BN** | English has 40 English-language videos; Bengali has the 74 the links point to |
| `drawer_items` | **BN** | English numbers these rows 1–6; the app uses 19–24 |
| everything else | EN | with `reference_bn` shown alongside on the short tables |

`build.py` swaps the Bengali-sourced tables in wholesale.

## Field rules

| Never change | Translate | Copy from English |
|---|---|---|
| `id`, `key`, `cat_id`, `subcat_id`, `topic_id`, `book_id`, `section_id` | `name`, `title`, `content` | `reference` |
| `audio`, `link`, `link_id`, `groups` structure | `translation`, `note`, `description` | `transliteration` |
| `uthmani`, `indopak`, `clean` (Arabic) | `topic_name`, `text`, `hero_title1`, `hero_title2` | |

## Reference format

Inline citations stay in English, in this shape:

```text
Surah Al-Fatir 35:15              Quran: Surah Name chapter:verse
Bukhari: 844                      Hadith: Collection: Number
Sahih (Albani). Abu Dawud: 1522   grading first, then a period
Bukhari: 6403; Muslim: 2693       multiple sources, semicolon
```

ASCII digits only. One space after the colon, none before. Drop `No`.

## Commands

```bash
cd dua_main_ur_translation

python3 scripts/verify.py work/duas/duas_001.json   # one file
python3 scripts/verify.py duas                       # one table
python3 scripts/verify.py                            # everything
python3 scripts/status.py                            # progress
python3 scripts/build.py ur                          # → ../dua_main_ur.sqlite
python3 scripts/build.py ur --partial                # preview with gaps left in source language
```

`build.py` refuses to run while anything is untranslated unless you pass `--partial`.

## What verify.py checks

- invalid JSON, changed field sets, added or removed items
- a `null` source with a non-`null` target, or the reverse
- an empty target
- source-language characters left in the target
- HTML tags added, removed or reordered
- Arabic text lost from a field that had it
- **any digit that differs between source and target**
- known corruption patterns (hadith numbers as dates, verse numbers as ages, and so on)
- a glossary term rendered differently from `GLOSSARY.json`
- the same watched term spelled more than one way across the workspace
- frozen fields carrying source-language script

It cannot hear whether the Urdu sounds human. That part is yours.

## GLOSSARY.json

Fill `canonical` before translating anything. If a source field mentions the term on the
left, the translation must contain the value on the right.

`overrides` switches that check off for one field when the English source is itself wrong.
Give the reason:

```json
"overrides": {
  "categories.name.2": "English says \"Dua's Excellence\", but this category holds Tasbeeh/Tahmid/Tahlil/Takbeer, and the Bengali says dhikr. Translated as dhikr."
}
```

`settled_wording` is not enforced — it is the shared memory of decisions already made, so
later files match earlier ones.

## Regenerating the workspace — read this before running generate.py

```bash
python3 scripts/generate.py      # rebuilds work/, source/, metadata/
```

**This overwrites `work/` and destroys any translation in it.** Commit or copy first.
This has already caused one real data loss on this project: a completed 200-row Japanese
table was wiped by a regeneration script and had to be recovered from git history.
