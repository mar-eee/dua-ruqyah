# Pitfalls — every one of these actually shipped

This is not a hypothetical list. Each entry was found by auditing the *finished* Japanese
translation of this same database, after it had been marked complete. They are recorded
here because the same machine will make the same mistakes in Urdu, and because several of
them are invisible unless you go looking.

Use this as an audit checklist, and read it when a file feels wrong but you cannot say why.

---

## 1. Numbers turning into dates, years and ages

The worst class, because the output looks confident and a reader has no way to know.

| Source | What was produced | What it should have been |
|---|---|---|
| `[Abu Dawud, 1481]` | "1481年" — the year 1481 | hadith number 1481 |
| `4/39` (volume/page) | "4 月 39 日" — April 39th | 4/39 |
| `4/1882` | "1882 年 4 月" — April 1882 | 4/1882 |
| `Yunus: 18` (verse) | "18歳" — 18 years old | verse 18 |
| `Al-Jawabul Kafi, 36` (page) | "36歳" — 36 years old | page 36 |

14 of these in one table. **Countermeasure:** copy digit strings mechanically; never
reformat them. `verify.py` compares the digit multiset on both sides.

In Urdu specifically: do not convert to Urdu-Indic numerals (`۱۴۸۱`), and do not spell
counts out in words. Keep ASCII.

## 2. A Qur'an reference read as the Bible

`72:1-7` — Surah Al-Jinn — was rendered as `詩篇72:1-7`, the **Psalms**. A Biblical
reference inside an Islamic text.

**Countermeasure:** when a bare `chapter:verse` appears, resolve it to the surah before
writing anything. Never let a generic scripture word attach itself.

## 3. Words mistranslated into something else entirely

| Word | Became | Should have been |
|---|---|---|
| `qalb` (قلب, heart) | 腸 — intestine | heart |
| `sahara` (سحرة, sorcerers) | 砂漠 — desert | sorcerers |
| Bengali `হাতের কর` (knuckles, for counting dhikr) | 税金 — tax | knuckles |
| Surah `Zumar` | 年齢 — "age" | Az-Zumar |
| "verse" (of the Qur'an) | 詩 — poem | verse |

These are homograph and sound-alike traps. In Urdu the equivalent risks are real: `سحر`
is *magic* but also *dawn*; `آیت` is a Qur'anic verse, never a poem (`شعر`); `رَاوی` is a
narrator, not a river or a rabbi.

**Countermeasure:** when a word has a second meaning in another domain, check which one
the surrounding rows are about.

## 4. Honorifics attached to the wrong person

`(PBUH)` was applied to *the children of Adam* rather than to Adam himself. Elsewhere a
vocative address — "O Umm Salama, there is no child of Adam whose heart…" — was
restructured until Umm Salama appeared to be the subject.

**Countermeasure:** identify who is speaking and who is spoken about before writing the
sentence. In Urdu, honorific concord is visible in the verb, so getting this wrong is
doubly obvious: `آپ ﷺ نے فرمایا` vs `اُس نے کہا`.

## 5. Fixed narration formulas translated literally

Arabic `عن` → English "on the authority of" → rendered as a *power/jurisdiction* word,
82 times. Also "narration" transliterated as a foreign loanword 24 times, and `rawi`
(narrator) read as "rabbi".

**Countermeasure:** narration chains are formulas. Learn the Urdu equivalents once —
`سے روایت ہے`, `سے مروی ہے`, `راوی کہتے ہیں` — and use them.

## 6. Text hidden inside a JSON string field

`duas.groups` is a JSON string holding **whole nested dua records** — 67 of them across 35
rows, each with its own `name`, `content`, `translation`, `note`, `transliteration` and
`reference`. Because earlier workspaces listed `groups` as a frozen field, nobody opened
it, and both the Japanese and Indonesian databases shipped Bengali inside it.

It also hides from scanning: the JSON is stored with `\uXXXX` escapes, so a regex for
source-language characters over the raw column finds **nothing**. You have to decode the
JSON first.

**Countermeasure:** the workspace now exposes these as `group_items`. Translate them. When
auditing, always decode nested JSON before scanning.

## 7. A field that must be copied, left in the source language

`duas.transliteration` must be copied verbatim from the English database. 42 Japanese rows
— and 686 Indonesian rows — kept the Bengali-script transliteration instead, which is
unusable for the target reader.

**Countermeasure:** `verify.py` now fails on frozen fields carrying source-language script.

## 8. Invisible characters

44 zero-width characters (U+200B, U+200C, U+200E, U+200F) were sitting inside words —
`言い␣␣ました`. They break search and line-breaking, and nobody can see them.

Urdu is especially exposed here, because ZWNJ (U+200C) is *legitimately* used in Urdu and
Persian typography, and RLM/LRM marks are legitimate around bidirectional text. So do not
strip blindly: remove them inside plain Urdu words, keep them where they are doing
directional work around Arabic or Latin.

## 9. Broken markup copied faithfully

The English source contains `<b>text<b>` where the closing tag should be `</b>` — 42
instances. Copying it faithfully means everything after that point renders bold.

**Countermeasure:** keep tag *structure*, but fix an obviously broken closing tag. Note it
in the plan file so the change is visible.

## 10. Register drift and duplicated MT artifacts

- 203 sentences mixed polite and plain register inside the same narrative passage.
- 21 duplicated-word artifacts: "complete, complete, complete", "sovereignty, sovereignty",
  "praise, praise".
- Untranslated English left sitting in running prose: surah names, `Chapter`, `No.`.

**Countermeasure:** read the file back as prose, not as a list of fields.

### But do not over-correct

Three things looked like defects and were correct. Check before "fixing":

- **`完全、完全、完全`** — the hadith really does repeat it three times (تامة تامة تامة).
- **`152年〜227年`** — a real hijri lifespan, not a mangled hadith number.
- **`善い目／悪い目に遭う`** in Qur'an 4:78 — the idiom "to experience", not the evil eye.
  A blind find-and-replace would have corrupted a Qur'anic verse.

And a whole class was left alone deliberately: **Qur'an translations use a literary plain
register** (`〜のだ。`, `〜投げ込もう。`). A blanket register normalisation would have
damaged 113 fields. The register fix was restricted to narrative prose, with quoted
speech, Arabic blocks, citations and headings masked out first.

The Urdu parallel: Qur'anic rendering has its own elevated voice. Do not flatten it to
match the surrounding prose.

---

## Audit method

When checking finished Urdu, scan for each of these:

1. digits differing from the source
2. bare `chapter:verse` resolved to the wrong scripture
3. `کہا` used for Allah or the Prophet ﷺ
4. missing or mismatched honorifics
5. `authority` / `narration` / `narrator` rendered literally
6. nested JSON in `groups` — decode before scanning
7. `transliteration` and `reference` not matching English
8. zero-width characters inside Urdu words
9. unbalanced HTML tags
10. register mixing within one narrative passage
11. one term rendered two ways across tables

Then read a few passages aloud. The defects that survive automated checks are exactly the
ones that only sound wrong.
