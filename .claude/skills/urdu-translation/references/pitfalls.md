# Pitfalls — all of these actually shipped

Found by auditing the *finished* Japanese translation of this database, after it was marked
complete. The same engine makes the same mistakes in Urdu.

## 1. Numbers becoming dates, years, ages

| Source | Shipped as | Should be |
|---|---|---|
| `[Abu Dawud, 1481]` | 1481年 — the year 1481 | hadith no. 1481 |
| `4/39` vol/page | 4月39日 — April 39th | 4/39 |
| `4/1882` | 1882年4月 | 4/1882 |
| `Yunus: 18` verse | 18歳 — 18 years old | verse 18 |
| `Al-Jawabul Kafi, 36` page | 36歳 | page 36 |

14 in one table. **Fix:** copy digit strings mechanically. In Urdu also: no Urdu-Indic
numerals (`۱۴۸۱`), no spelling counts out.

## 2. Scripture reference sent to the wrong book

`72:1-7` (Surah Al-Jinn) → `詩篇72:1-7` — **the Psalms**, inside an Islamic text.
**Fix:** resolve bare `chapter:verse` to the surah before writing.

## 3. Words turned into something else

| Word | Became | Correct |
|---|---|---|
| `qalb` قلب heart | 腸 intestine | heart |
| `sahara` سحرة sorcerers | 砂漠 desert | sorcerers |
| BN `হাতের কর` knuckles | 税金 tax | knuckles |
| Surah `Zumar` | 年齢 age | Az-Zumar |
| "verse" of Qur'an | 詩 poem | verse |

Urdu equivalents to watch: `سحر` = magic *and* dawn · `آیت` = Qur'anic verse, never `شعر`
· `راوی` = narrator.

## 4. Honorifics on the wrong person

`(PBUH)` applied to *the children of Adam* instead of Adam. A vocative ("O Umm Salama…")
restructured until she became the subject.
**Fix:** identify who speaks and who is spoken about first. Urdu shows this in the verb.

## 5. Narration formulas translated literally

`عن` → "on the authority of" → a *power/jurisdiction* word, 82×. "Narration" transliterated
24×. `rawi` read as "rabbi".
**Fix:** formulas are fixed. `سے روایت ہے` · `سے مروی ہے` · `راوی کہتے ہیں`.

## 6. Text hidden inside a JSON field

`duas.groups` holds **67 whole nested dua records** with their own name/content/translation/
note/transliteration/reference. Treated as frozen, so never opened → Bengali shipped in both
Japanese and Indonesian.

It also hides from scanning: stored with `\uXXXX` escapes, so a regex over the raw column
finds **nothing**. **Decode nested JSON before scanning.**

## 7. Copy-through field left in source language

`duas.transliteration` must come from the English DB. 42 Japanese rows — and 686 Indonesian
— kept Bengali script, unusable for the reader.

## 7b. `reference_bn` pointing at the wrong row (caught during Urdu, before shipping)

The workspace shows a Bengali "reference" next to the English source for some tables, by
joining EN row *n* to BN row *n*. That join assumes both languages tell the story in the
same row order. They do not, for the ruqyah supplementary content: BN `ruqyah_subcategories`
has 117 rows to EN's 163, and BN `ruqyah_categories` has the *same* 15 rows as EN but
reordered — EN "About Raqi" (id 6) is really BN's row 10; BN's icon `next_step` is reused
across two unrelated EN rows. The row-count coincidence for `ruqyah_categories` (15 = 15)
made it look aligned when it was not.

Trusting it would have produced a *confident, wrong* Urdu name — worse than no reference at
all, because a wrong reference reads as evidence. Caught by spot-checking actual subcategory
content against the shown reference before writing anything, exactly as the skill says to do
for the English source. `duas` and `ruqyah_instants` were checked the same way and are fine
— those two are id-aligned between EN and BN.

**Fix:** don't trust a same-language pairing shown by the workspace until you have checked a
few rows against real content. `reference_bn` is now only shown for tables verified aligned.

## 7c. Bengali-Indic digits false-flagged as corrupted (caught, fixed in verify.py)

`ruqyah_videos` is BN-sourced, and Bengali writes numbers in Bengali-Indic digits
(`পর্ব-১০`). Converting `১০` to `10` for the Urdu target is *correct* — the skill's own
rule is ASCII digits only, never a non-Latin numeral script. But `verify.py`'s digit check
originally compared the raw digit strings, so `১০` vs `10` looked like a changed number and
failed every episode-numbered row, even though the value never moved.

This is the opposite failure mode from pitfall 1 (a real value change disguised as fine) —
here a fine conversion was disguised as a value change. Both matter: a check that never
fires misses corruption; a check that fires on correct work gets silenced or ignored, which
is just as dangerous across a workspace this size.

**Fix:** `verify.py` now normalises Bengali-Indic, Urdu-Indic and Arabic-Indic digits to
ASCII on both sides before comparing. Re-verified afterward that it still catches a genuine
value change (`10` deliberately corrupted to `100` was still flagged).

## 8. Invisible characters

44 zero-width chars (U+200B/200C/200E/200F) inside words: `言い␣␣ました`. Break search and
line-breaking.

**Urdu caution:** ZWNJ (U+200C) is *legitimate* in Urdu/Persian typography, and RLM/LRM are
legitimate around bidirectional text. Strip only inside plain Urdu words; keep those doing
directional work.

## 9. Broken markup copied faithfully

Source has `<b>text<b>` instead of `</b>`, 42×. Copied faithfully → everything after renders
bold. **Fix the closing tag; note it in the plan.**

## 10. Register drift and MT residue

203 sentences mixed polite/plain register mid-passage · 21 duplicated-word artifacts
("complete, complete, complete") · untranslated English in running prose.
**Fix:** read the file back as prose, not as fields.

## 11. Translating a table that is out of scope

`sections` (21 rows: two books' chapter-title lists, e.g. "Introduction", "How To
Supplicate") was translated into Urdu even though the user had said not to work on the
book content. It is a separate table from `books` and `book_details` - which *were*
correctly excluded - so it slipped through: it was in the generated file list, it was in
every `status.py` and `PLAN.md` table the user had already seen, and the previous Japanese
translation (done before this workspace existed) had also translated it. None of that made
it in scope. `sections` exists only as a table of contents for `book_details`, which stays
untranslated - a translated chapter title over an untranslated Bengali chapter body serves
no one.

**Fix:** don't infer scope from what a generated file list or an earlier language happened
to include. When a table is adjacent to an explicitly excluded one - shares a foreign key
with it, exists only to label it, is meaningless without it - check whether it's actually
inside the boundary the user drew, not just outside the two table names they said. `sections`
is now excluded in `generate.py` alongside `books` and `book_details`; the 21-row Urdu
translation was reverted before it reached the database.

## Do NOT over-correct — these looked wrong and were right

- `完全、完全、完全` — the hadith genuinely repeats it (تامة تامة تامة)
- `152年〜227年` — a real hijri lifespan, not a mangled hadith number
- `善い目／悪い目に遭う` in Qur'an 4:78 — the idiom "to experience", not the evil eye. A blind
  replace would have corrupted a Qur'anic verse.
- **Qur'an translations legitimately use a literary plain register.** A blanket register
  normalisation would have damaged 113 fields. Restrict register fixes to narrative prose,
  masking quotes, Arabic, citations and headings first. Same applies to Urdu: do not flatten
  Qur'anic voice to match surrounding prose.

## Audit checklist

1. digits differing from source · 2. `chapter:verse` → wrong scripture · 3. `کہا` used for
Allah or the Prophet ﷺ · 4. missing/mismatched honorifics · 5. authority/narration/narrator
literal · 6. decode `groups` JSON before scanning · 7. `transliteration`/`reference` ≠ English
· 8. zero-width chars inside Urdu words · 9. unbalanced tags · 10. register mixing ·
11. one term, two renderings.

Then read passages aloud. What survives automated checks is exactly what only *sounds* wrong.
