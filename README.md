# Dua Ruqyah Translation Guide

Databases are split into small JSON files so they can be translated safely, then rebuilt into SQLite.

Translate meaning, not words. The result must read as if a careful person prepared it for worship and daily use.

## Source of Truth

**Translate from the English database, not from the Bengali text in the JSON files.**

`dua_main_en.sqlite` holds the same rows, matched by `id`. English → target is far more reliable than Bengali → target. Use the Bengali only to resolve ambiguity.

Two fields are **copied verbatim** from the English DB, never written by hand:

- `transliteration`
- `reference`

```python
import sqlite3
en = dict(sqlite3.connect("dua_main_en.sqlite").execute(
    "SELECT id, transliteration FROM duas"))
```

If the English DB has no row for an `id`, translate from the Bengali and say so in the plan file.

## Folders

| Path | Purpose |
|---|---|
| `dua_main_ja_planned_json/` | Japanese workspace |
| `dua_main_id_planned_json/` | Indonesian workspace |
| `<workspace>/tables/<table>/*.json` | the chunk files you edit |
| `<workspace>/_database_metadata.json` | schema — never delete or edit |
| `<workspace>/rebuild_*_from_json.py` | rebuild script — never delete or rename |
| `duas_translation_plan.md` | progress log — update after every batch |

## Fields

| Never change | Translate | Copy from English DB |
|---|---|---|
| `id`, `cat_id`, `subcat_id`, `topic_id`, `book_id`, `section_id` | `name`, `title`, `content` | `transliteration` |
| `audio`, `link`, `link_id`, `groups` | `translation`, `note`, `description` | `reference` |
| `uthmani`, `indopak`, `clean` (Arabic) | `topic_name`, `text`, `hero_title1`, `hero_title2` | |
| JSON keys, file names, folder names | | |

Rules that apply everywhere:

- `null` stays `null`. Never turn it into `""` or a translated string.
- Never add or remove a row. Row count must not change.
- Never add religious explanation that is not in the source.
- Keep HTML structure. Translate only the words between tags: `<p>Text</p>` → `<p>訳文</p>`.
- Leave URLs, audio numbers, and hadith numbers untouched.

## Reference Format

Copy the English DB value, then fix only spacing and language — never the numbers.

```text
Surah Al-Fatir 35:15          Quran: Surah Name chapter:verse
Bukhari: 844                  Hadith: Collection: Number
Sahih (Albani). Abu Dawud: 1522    grading first, then a period
Bukhari: 6403; Muslim: 2693        multiple sources, semicolon
[1] Muslim: 2137                   footnotes, ASCII brackets, own line
```

- One space after the colon, none before. Drop `No`: write `Bukhari: 6403`.
- ASCII digits only — no Bengali, Arabic-Indic, or full-width numerals.
- Inline citations inside translated prose use the same English form.

## Japanese Standard

Calm, respectful, warm but not casual. Literary where it fits, never difficult. Smooth when read aloud.

```text
✅ アッラーに助けを求め、心を落ち着けて祈ります。
❌ アッラーへ援助を要求し、精神を安定化して祈願します。
```

Avoid stiff machine translation, heavy kanji compounds, legal-style phrasing, childish wording, and slang.

Devotional register: お祈り・願い・慈しみ・お守りください・お許しください・導いてください
Proper nouns in katakana: アッラー・ムハンマド・クルアーン
For ruqyah, stay clear and reassuring — never dramatic or frightening.

## Indonesian Standard

Sincere, clear, pleasant. Respectful and Islamic in tone, warm but not casual.

```text
✅ Mintalah pertolongan kepada Allah dengan hati yang tenang dan penuh harap.
❌ Lakukan permintaan bantuan kepada Allah dengan kondisi hati yang distabilkan.
```

Avoid stiff machine translation, slang, very long sentences, and Arabic loanwords where plain Indonesian is clearer.

Devotional register: doa, rahmat, ampunan, lindungilah, bimbinglah, karuniakanlah
For ruqyah, stay calm, clear, and helpful.

## Consistency

One term, one translation — across the whole language, not just one file. Allah, dua, ruqyah, and category names must match their related subcategory names. Before finishing a file, check that no term drifted.

## Workflow

Work one chunk file at a time.

1. Back up the file.
2. Load the matching English rows by `id`.
3. Translate the text fields; copy `transliteration` and `reference` verbatim.
4. Write the file back: UTF-8, 2-space indent, same key order, trailing newline.
5. Run the checks below.
6. Mark the batch done in `duas_translation_plan.md`.

## Progress Update Rule

Every completed translation must update the work status before the task is considered finished.

For dua chunks, update both places:

- `duas_translation_plan.md`
- `dua_main_ja_planned_json/_database_metadata.json`

The plan file must show:

- the chunk changed from `pending` to `complete`
- ID range
- row count
- completed date
- translated fields
- reference status: English, not translated
- verification result

The metadata file must add or update `work_status` for that exact JSON path.

## Verify

Structure check — run against your backup before rebuilding:

```bash
python3 - <<'PY'
import json, sys
old = json.load(open("BACKUP.json")); new = json.load(open("EDITED.json"))
FROZEN = ["id","groups","uthmani","indopak","clean","audio","cat_id","subcat_id"]
assert len(old) == len(new), "row count changed"
for a, b in zip(old, new):
    assert list(a) == list(b), f"keys changed at id {a['id']}"
    for f in FROZEN:
        assert a[f] == b[f], f"{f} changed at id {a['id']}"
    for f in a:
        assert (a[f] is None) == (b[f] is None), f"{f} nullness changed at id {a['id']}"
bad = [r["id"] for r in new if r["reference"] and not r["reference"].isascii()]
assert not bad, f"non-English reference at {bad}"
print("structure ok")
PY
```

Then rebuild:

```bash
cd dua_main_ja_planned_json && python3 rebuild_japanese_from_json.py
```

```bash
cd dua_main_id_planned_json && python3 rebuild_indonesian_from_json.py
```

The rebuild runs `PRAGMA integrity_check` and fails loudly if the JSON is broken. It writes `dua_main_ja_rebuilt.sqlite` / `dua_main_id_rebuilt.sqlite`.

## Done When

- structure check passes, rebuild succeeds, integrity check says `ok`
- Arabic intact, IDs and links unchanged, row count unchanged
- every `reference` is ASCII English in the format above
- the text sounds human, natural, and respectful when read aloud
