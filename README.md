# Dua Ruqyah Translation Guide

This repository keeps the dua and ruqyah databases in small JSON files so they can be translated safely. After translation, the included Python rebuild script can create a complete SQLite database again.

The goal is not only to translate words. The goal is to make the text feel natural, respectful, clear, and easy to read for real people.

## Folders

- `dua_main_ja_planned_json` is for Japanese translation.
- `dua_main_id_planned_json` is for Indonesian translation.
- Each table is split into small JSON files inside `tables/`.
- Do not delete `_database_metadata.json`.
- Do not delete or rename the rebuild Python file.

## Main Rule

Translate only human-readable text. Keep database structure exactly the same.

Do not change:

- `id`
- `cat_id`
- `subcat_id`
- `topic_id`
- `book_id`
- `section_id`
- `audio`
- `link`
- `link_id`
- `groups`
- JSON keys
- file names
- folder names

Usually you should translate fields like:

- `name`
- `title`
- `hero_title1`
- `hero_title2`
- `content`
- `translation`
- `note`
- `description`
- `topic_name`
- `text`
- `reference` only when it is normal readable text. Do not change book names, hadith numbers, URLs, or source codes.

## Keep HTML and Code Safe

Some text may contain HTML, special tags, line breaks, or code-like marks.

Keep the same structure.

Example:

```html
<p>Original text</p>
<br>
<strong>Important</strong>
```

Translate only the readable words:

```html
<p>Translated text</p>
<br>
<strong>Important translated text</strong>
```

Do not remove or change:

- HTML tags such as `<p>`, `<br>`, `<b>`, `<strong>`, `<i>`
- Arabic text
- Quran or hadith reference numbers
- URLs
- audio numbers
- punctuation used by the app
- JSON commas, quotes, brackets, or braces

If a value is `null`, keep it as `null`.

## Japanese Translation Standard

Use natural Japanese that feels calm, polished, and human.

The Japanese should be:

- easy to understand
- respectful
- warm but not casual
- literary when suitable, but not difficult
- simple enough for ordinary readers
- smooth when read aloud

Avoid:

- stiff machine translation
- too many Chinese-style compound words
- overly formal legal-style Japanese
- childish wording
- rough slang
- adding extra religious explanation that is not in the source

Preferred feeling:

```text
アッラーに助けを求め、心を落ち着けて祈ります。
```

Avoid machine-like wording:

```text
アッラーへ援助を要求し、精神を安定化して祈願します。
```

For dua translation, keep the meaning humble and devotional. Use words like:

- お祈り
- 願い
- 慈しみ
- お守りください
- お許しください
- 導いてください

For ruqyah content, keep the tone clear and reassuring. Do not make it dramatic or frightening.

## Indonesian Translation Standard

Use natural Indonesian that feels sincere, clear, and pleasant to read.

The Indonesian should be:

- easy for general readers
- respectful and Islamic in tone
- warm but not overly casual
- informative without sounding heavy
- smooth, like a human editor wrote it

Avoid:

- stiff machine translation
- unnecessary Arabic loanwords when common Indonesian is clearer
- slang
- overly long sentences
- adding explanation that is not in the source

Preferred feeling:

```text
Mintalah pertolongan kepada Allah dengan hati yang tenang dan penuh harap.
```

Avoid machine-like wording:

```text
Lakukan permintaan bantuan kepada Allah dengan kondisi hati yang distabilkan.
```

For dua translation, keep the language humble and devotional. Use words like:

- doa
- rahmat
- ampunan
- lindungilah
- bimbinglah
- karuniakanlah

For ruqyah content, keep the tone calm, clear, and helpful.

## Arabic Text

Do not translate Arabic Quran, hadith, or dua text unless the field is clearly a translation field.

Keep Arabic text exactly as it is in fields like:

- `content`
- `uthmani`
- `indopak`
- `clean`

Only translate the explanation or translation fields.

## Transliteration

Do not rewrite transliteration unless there is a clear mistake.

If transliteration exists, keep the same style. Do not mix different systems inside the same file.

## Consistency

Use the same translation for repeated terms.

Examples:

- Allah should stay consistent.
- Dua should be translated consistently in each language.
- Ruqyah should stay consistent.
- Category names should match related subcategory names.

Before finishing a file, quickly check that the same term is not translated in many different ways without reason.

## JSON Editing Rules

Every JSON file must remain valid JSON.

Important:

- keep double quotes around text
- use `\\n` for line breaks inside one JSON string if needed
- do not leave trailing commas
- do not remove commas between fields
- do not change the order of keys unless necessary
- keep the file encoded as UTF-8

After editing, validate by rebuilding the database.

## Rebuild Japanese SQLite

From the project folder:

```bash
cd dua_main_ja_planned_json
python3 rebuild_japanese_from_json.py
```

This creates:

```text
dua_main_ja_rebuilt.sqlite
```

## Rebuild Indonesian SQLite

From the project folder:

```bash
cd dua_main_id_planned_json
python3 rebuild_indonesian_from_json.py
```

This creates:

```text
dua_main_id_rebuilt.sqlite
```

## Final Check

A translation is ready only when:

- the JSON files still open correctly
- the rebuild script runs without error
- the SQLite integrity check passes
- Arabic text is not damaged
- IDs and table links are unchanged
- the final language sounds human, natural, and respectful

Good translation should feel like a careful person prepared it for worship, reading, and daily use.
