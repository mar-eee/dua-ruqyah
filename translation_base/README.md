# Dua & Ruqyah — Standard Translation Workspace

Copy this whole folder once per language, then translate inside the copy.

```bash
cp -R translation_base dua_main_ur_translation     # Urdu
cp -R translation_base dua_main_tr_translation     # Turkish, etc.
```

Nothing here is language-specific until you edit `GLOSSARY.json`.

---

## 1. What is in the folder

| Path | What it is | Do you edit it? |
|---|---|---|
| `work/<table>/<table>_NNN.json` | the files you translate | **yes** — this is the work |
| `GLOSSARY.json` | one agreed word per term | **yes** — fill it in first |
| `PLAN.md` | checklist of every file, with sizes | **yes** — tick files off |
| `source/en/<table>.json` | full English rows, for reference | no |
| `source/bn/<table>.json` | full Bengali rows, for reference | no |
| `metadata/chunk_index.json` | machine-readable index of all chunks | no |
| `metadata/schema.json` | table definitions | no |
| `scripts/generate.py` | rebuilds the workspace from the two databases | no |
| `scripts/build.py` | `work/` → `dua_main_<lang>.sqlite` | no |
| `scripts/verify.py` | quality gate | no |
| `scripts/status.py` | progress report | no |

---

## 2. How the work is divided

Files are sized by **translatable characters**, not by row count. That is the whole
point: a file is one comfortable sitting, so quality does not fall off near the end.

- Budget: **6 000 source characters** per file
- At most **50 rows** per file
- A row bigger than one budget is **split into parts at paragraph boundaries**.
  A paragraph is never split. `build.py` rejoins parts with a blank line.

This matters. In the earlier Japanese work, the two tables with the biggest chunks
(`dua_infos` at ~178 000 characters per file and `ruqyah_details` at ~46 000) were
also the only two tables that came out as unusable machine translation. Everything
chunked small came out fine. Keep the files small.

| Table | Files | Rows | Source chars | Source |
|---|---:|---:|---:|---|
| `categories` | 1 | 44 | 461 | EN |
| `subcategories` | 3 | 118 | 3 531 | EN |
| `sections` | 1 | 21 | 846 | EN |
| `dua_infos` | 70 | 42 | 357 024 | **BN** |
| `duas` | 61 | 1 001 | 349 211 | EN |
| `ruqyah_categories` | 1 | 15 | 312 | EN |
| `ruqyah_subcategories` | 4 | 163 | 4 805 | EN |
| `ruqyah_details` | 95 | 200 | 457 751 | EN |
| `ruqyah_instants` | 20 | 308 | 112 037 | EN |
| `ruqyah_videos` | 2 | 74 | 3 884 | **BN** |
| `drawer_items` | 2 | 6 | 7 727 | EN |
| **total** | **260** | **1 992** | **1 297 589** | |

Excluded on purpose: `books` and `book_details` (book tables), `ids` and
`drawer_item_actions` (no text).

### Why two tables come from Bengali

`dua_main_en.sqlite` is **not** a translation of `dua_main_bn.sqlite` for every table.
For `dua_infos` and `ruqyah_videos` the English database holds a completely different
dataset — English `dua_infos` id 1 is "Conditions of dua being accepted", Bengali id 1
is "Meaning of dua". Translating those two tables against English by id produces text
that does not belong to the row it is attached to. They are therefore taken from
Bengali, and `build.py` swaps those tables in wholesale.

---

## 3. The file format

```jsonc
{
  "table": "duas",
  "chunk": "duas_001.json",
  "source_language": "en",
  "target_language": "TARGET",   // set to your language code
  "status": "pending",           // set to "done" when finished
  "rows": 15,
  "id_range": "1-15",
  "source_chars": 5906,
  "items": [
    {
      "key": [1],                // row identity — never change
      "id": 1,
      "part": 1, "of": 1,        // part of a split row
      "frozen": { ... },         // copied through untouched, for context only
      "source": { "name": "…", "content": "…", "translation": null },
      "target": { "name": "",   "content": "",  "translation": null }
    }
  ]
}
```

**You edit `target` and nothing else.**

- `null` in `source` stays `null` in `target`. Never turn it into `""`.
- Never add, remove or reorder items. Never touch `key`, `id`, `part`, `of`, `frozen`.
- `drawer_items` has an extra `content_sections` array; fill each `target` there.
  Section order, types and spacer heights are handled for you.

---

## 4. Translation rules

### Fields

| Never change | Translate | Keep in English |
|---|---|---|
| `id`, `key`, `cat_id`, `subcat_id`, `topic_id`, `book_id`, `section_id` | `name`, `title`, `content` | `reference` |
| `audio`, `link`, `link_id`, `groups` | `translation`, `note`, `description` | `transliteration` |
| `uthmani`, `indopak`, `clean` (Arabic) | `topic_name`, `text`, `hero_title1`, `hero_title2` | |

### Everywhere

- Translate meaning, not words. It must read as if a careful person prepared it for worship.
- **Keep every digit exactly as it is.** Hadith numbers, verse numbers, volume/page
  refs like `4/39`, and years are all numbers you must copy, never convert.
  `verify.py` compares the digits in source and target and fails on any change.
- Keep HTML structure. Translate only the words between tags: `<p>Text</p>` → `<p>訳文</p>`.
- Copy `<ar>…</ar>` Arabic blocks through untouched.
- Inline citations stay in English: `[Bukhari: 6403; Muslim: 2693]`.
- Never add religious explanation that is not in the source.
- One term, one translation, across the whole language — fill `GLOSSARY.json` first.

### Reference format

```text
Surah Al-Fatir 35:15              Quran: Surah Name chapter:verse
Bukhari: 844                      Hadith: Collection: Number
Sahih (Albani). Abu Dawud: 1522   grading first, then a period
Bukhari: 6403; Muslim: 2693       multiple sources, semicolon
```

ASCII digits only. One space after the colon, none before. Drop `No`.

---

## 5. Mistakes that have actually happened

Every one of these shipped in a previous language before being caught. `verify.py`
now checks for all of them.

| What went wrong | Example |
|---|---|
| Hadith number read as a year | `[Abu Dawud, 1481]` → `[アブ・ダウド、1481年]` |
| Volume/page ref read as a date | `4/39` → `4 月 39 日`; `4/1882` → `1882 年 4 月` |
| Verse number read as an age | `Yunus: 18` → `スーラ・ユヌス：18歳` |
| Page number read as an age | `Al-Jawabul Kafi, 36` → `36歳` |
| A Qur'an reference read as the Bible | `72:1-7` → `詩篇72:1-7` (Psalms) |
| A word mistranslated into a different body part | `qalb` (heart) → `腸` (intestine) |
| A word mistranslated by sound | `sahara` (sorcerers) → `砂漠` (desert) |
| Bengali homograph taken the wrong way | `হাতের কর` (knuckles) → `税金` (tax) |
| "verse" rendered as "poem" | `verses` → `詩` instead of `節` |
| Honorific attached to the wrong person | `children of Adam (PBUH)` |
| Verb ending dropped | `ドゥアーます` instead of `ドゥアーします` |
| Same name spelled three ways | `アーイシャ` / `アイシャ` / `アイーシャ` |

**Rule of thumb:** if a number or a proper noun changes shape between source and
target, it is a bug until proven otherwise.

Do not over-correct either. These looked like bugs and were **correct**:

- `完全、完全、完全` — the hadith really does repeat it (تامة تامة تامة).
- `152年〜227年` — a real hijri lifespan.
- `善い目／悪い目に遭う` in Qur'an 4:78 — the idiom "to experience", not the evil eye.

---

## 6. Workflow

```bash
# 0. once: copy the base and name your language
cp -R translation_base dua_main_ur_translation
cd dua_main_ur_translation

# 1. fill in GLOSSARY.json  (do this before translating anything)

# 2. translate one file at a time, smallest tables first
#    order: categories → ruqyah_categories → sections → subcategories →
#           ruqyah_subcategories → ruqyah_videos → drawer_items →
#           duas → ruqyah_instants → ruqyah_details → dua_infos

# 3. after each file
python3 scripts/verify.py work/duas/duas_001.json

# 4. any time
python3 scripts/status.py

# 5. when a table is done
python3 scripts/verify.py duas

# 6. when everything is done
python3 scripts/verify.py
python3 scripts/build.py ur          # writes ../dua_main_ur.sqlite
```

`build.py` refuses to run while anything is untranslated. Use `--partial` to build
a preview anyway; untranslated fields keep their source text.

### Why that order

Small tables first gets the vocabulary settled — category and subcategory names are
the words that then have to match inside `duas` and `ruqyah_details`. Doing the long
prose first means re-editing it later when the terms change.

---

## 7. Regenerating the workspace

If the source databases change:

```bash
python3 scripts/generate.py        # rebuilds work/, source/, metadata/
```

**This overwrites `work/` and destroys any translation in it.** Commit or copy your
work first. This has already caused one real data loss: a completed 200-row Japanese
table was wiped by a regeneration script and had to be recovered from git.

---

## 8. Verification gates

`verify.py` fails on:

- invalid JSON, changed field sets, added or removed items
- a `null` source with a non-`null` target, or the reverse
- an empty target
- source-language characters left in the target
- HTML tags added, removed or reordered
- Arabic text lost from a field that had it
- **any digit that differs between source and target**
- the specific corruption patterns in section 5
- a glossary term rendered differently from `GLOSSARY.json`
- the same watched term spelled more than one way across the workspace

`build.py` additionally runs `PRAGMA integrity_check` on the result.

The workspace round-trips losslessly: generating it and building it back with nothing
translated reproduces both source databases field for field. That is the guarantee
that the chunking itself never damages content.
