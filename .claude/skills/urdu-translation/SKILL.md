---
name: urdu-translation
description: Translate the Dua & Ruqyah database into literary, human Urdu — duas, ruqyah texts, hadith narration, Qur'an renderings, category names, app screens. Use whenever work touches Urdu in this project: translating a chunk under dua_main_ur_translation/work/, reviewing or fixing existing Urdu, choosing wording for a category or hadith, checking terminology consistency, or any request naming Urdu with duas, ruqyah, categories, subcategories, dua_infos, ruqyah_details, drawer_items or translation_base. Also use when asked to make Urdu sound natural, human, literary or "not machine translated", or to audit Urdu for machine-translation artifacts.
---

# Urdu Translation — Dua & Ruqyah

Devotional text. People read it while praying, ill, or frightened. It must read as though
an Urdu-speaking scholar wrote it.

**Method:** read the source until you know what it *says* → look away → write that in Urdu
→ check nothing was lost. Machine translation keeps English's *shape* and swaps in Urdu
words. That is the thing to avoid.

## Human tone vs machine tone

The tone is warm, dignified, unhurried — a knowledgeable person speaking to someone who
needs help. Not a manual, not a lecture.

| Machine | Human | Why |
|---|---|---|
| یہ دعا پڑھی جاتی ہے جب انسان پریشان ہو | پریشانی کے وقت یہ دعا پڑھیں | passive → direct address |
| اللہ سے مغفرت کی درخواست کریں | اللہ سے مغفرت مانگیں | `کرنا` padding → real verb |
| یہ ایک ایسی دعا ہے جو کہ بہت اہم ہے | یہ نہایت اہم دعا ہے | copula chain → one clause |
| اللہ کے رسول کے صحابہ کے دعاؤں کا مجموعہ | صحابہ کرام کی مسنون دعائیں | `کے` chain → izafat |
| اس کے علاوہ، مزید یہ کہ | نیز / چنانچہ | English connectives |
| مذکورہ بالا دعا کو تین بار دہرایا جائے | یہ دعا تین بار پڑھیں | bureaucratic → plain |

Signs you have drifted machine-ward: every sentence the same length; `ہے` ending
everything; `کرنا` doing all the work; three `کے` in a row; nothing you would say aloud.

## Three registers — keep them apart

| Field | Voice |
|---|---|
| Qur'an rendering | elevated, restrained, follows classical Urdu translation; stay close to known renderings — readers recognise them |
| Hadith & religious prose (`dua_infos`, `ruqyah_details`) | dignified, readable: `فرمایا`, `روایت ہے`, `ارشاد فرمایا` |
| Interface labels (categories, subcategories, titles) | short noun phrases, scannable — not sentences |

## Verbs of speech — respect is grammatical

Getting this wrong is a discourtesy, not a style slip.

| Subject | Use | Never |
|---|---|---|
| Allah | `اللہ تعالیٰ فرماتا ہے` / `ارشاد فرماتا ہے` | `اللہ کہتا ہے` |
| Prophet ﷺ | `رسول اللہ ﷺ نے فرمایا` | `نبی نے کہا` |
| Companion | `حضرت … رضی اللہ عنہ نے فرمایا` / `بیان کیا` | `اس نے کہا` |
| Ordinary person | `اُس نے کہا` | — |

Honorifics are required, not decorative: `ﷺ`, `رضی اللہ عنہ/عنہا/عنہم`, `علیہ السلام`,
`رحمہ اللہ`. Match gender and number.

## Narration formulas — fixed, not translated

| Source | Urdu | Machine failure |
|---|---|---|
| "on the authority of X" / `عن` | `X سے روایت ہے` | *authority* as a power word — this shipped 82× in Japanese |
| "narrated by X" | `X سے روایت ہے` | "narration" as a loanword |
| "It was reported that…" | `مروی ہے کہ…` | `رپورٹ کیا گیا` |
| "The Messenger ﷺ used to…" | `رسول اللہ ﷺ … کیا کرتے تھے` | present tense |

`رَاوی` = narrator → `راوی کہتے ہیں`. Not a name, not "rabbi" (that confusion shipped).

## Sentence shape

English front-loads modifiers; Urdu unfolds in order and ends on the verb. Restructure.

- *Duas to be recited when one is in danger*
  ❌ `دعائیں پڑھی جانے کے لیے جب کوئی خطرے میں ہو`
  ✅ `مصیبت و تکلیف میں مبتلا ہونے پر پڑھی جانے والی دعائیں`
- *Abu Hurayra (RA) reported that the Messenger ﷺ said…*
  ❌ `ابو ہریرہ رضی اللہ عنہ نے رپورٹ کیا کہ اللہ کے رسول ﷺ نے کہا`
  ✅ `حضرت ابو ہریرہ رضی اللہ عنہ سے روایت ہے کہ رسول اللہ ﷺ نے فرمایا`

Use izafat where Urdu does: `نمازِ جنازہ`, `قبولیتِ دعا`, `دعائے قنوت`, `خطبۂ نکاح`,
`قعدۂ اخیرہ`. Flat noun stacking is a machine tell.

## Vocabulary layer

Religious writing sits in the Arabic–Persian layer. Indic words are not wrong Urdu, they
are wrong *here*.

`دعا` not پرارتھنا · `عبادت` not پوجا · `فرشتہ` not دیوتا · `گناہ` not پاپ ·
`مغفرت` not معافی (for sins) · `نمازِ جنازہ` not انتم سنسکار

Do not over-Arabize either. Dignified and readable, not a vocabulary display.

## Hard rules

- **Numbers:** copy exactly. Never convert, spell out, or use Urdu-Indic numerals. Hadith
  numbers, verse numbers, `4/39` refs, counts. `verify.py` fails the file if digits differ.
- **Add nothing, drop nothing.** No added piety or explanation. `null` stays `null`.
- **Copy through:** `<ar>…</ar>` Arabic; `transliteration` and `reference` come from the
  English DB verbatim. Keep HTML tag structure; translate only words between tags.
- **One term, one rendering.** Fill `GLOSSARY.json` before starting. Drift is invisible in
  one file and glaring across screens.

## English is not always right — read the Bengali

Short tables carry `reference_bn`. Where the two disagree, the Bengali usually matches what
the rows actually contain. **Check what the category contains before naming it.**

- Cat 2 — EN *"Dua's Excellence"*, but holds Tasbeeh/Tahmid/Tahlil/Takbeer = dhikr →
  `ذکر کی فضیلت`
- Cat 37 — EN *"Prophet's Dua"*, but holds duas of Adam, Ayyub, Yunus عليهم السلام →
  `انبیاء و رُسل کی دعائیں` (plural)

Record deliberate deviations in `GLOSSARY.json` → `overrides`, with the reason.

## Where to start — always check first

```bash
cd dua_main_ur_translation && python3 scripts/status.py
```

It prints per-table progress, any half-finished file, and a `START HERE:` line with the
exact next file and its verify command. It reads the work files themselves, so it is
never stale — trust it over any note, including this one.

## Working

`references/workflow.md` — file format, sources, commands. Read before your first file.

1. Fill `GLOSSARY.json`. 2. One file at a time, in `PLAN.md` order (small tables settle
vocabulary first). 3. Edit only `target`. 4. `python3 scripts/verify.py <file>`.
5. Tick the file in `PLAN.md` and set `"status": "done"`.
6. **Read it aloud.** If an Urdu speaker would pause, revise — the verifier cannot hear it.

`references/pitfalls.md` — defects that actually shipped in the finished Japanese. Read
before auditing, or when a file feels wrong and you cannot say why.
