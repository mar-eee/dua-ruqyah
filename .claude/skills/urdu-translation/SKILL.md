---
name: urdu-translation
description: Translate the Dua & Ruqyah database into literary, human Urdu — dua and ruqyah texts, category and subcategory names, hadith narration, Qur'an renderings, and app screens. Use this skill whenever work touches Urdu translation in this project: translating a chunk file under dua_main_ur_translation/work/, reviewing or fixing existing Urdu, deciding wording for a category or a hadith, checking terminology consistency, or any request that mentions Urdu along with duas, ruqyah, categories, subcategories, dua_infos, ruqyah_details, drawer_items, or the translation_base workspace. Also use it when asked to make Urdu "sound natural", "not machine translated", "literary", or "human", or when auditing Urdu for machine-translation artifacts.
---

# Urdu Translation — Dua & Ruqyah

This is devotional text. People will read it while praying, when they are ill, and when
they are frightened. It has to sound like a careful Urdu-speaking scholar wrote it, not
like it arrived through a translation engine. Everything below exists to serve that.

## The one rule everything else follows from

**Translate the meaning into Urdu that an Urdu speaker would actually write. Do not
transport English grammar into Urdu words.**

Machine translation fails here not because it picks wrong words but because it keeps the
source language's *shape* — its word order, its connectives, its flat noun stacking — and
swaps in Urdu vocabulary. The result is technically parseable and immediately, obviously
foreign. A reader can feel it in one sentence.

So the working method is: read the source until you know what it *says*, look away, and
write that in Urdu. Then check nothing was lost.

## The registers — pick the right one

Urdu religious prose is not one voice. Three are in play here, and mixing them is the
fastest way to sound synthetic.

**1. Qur'an rendering** — elevated, restrained, follows the classical Urdu translation
tradition. Never colloquial, never explanatory. If a well-known Urdu rendering exists for
a verse, stay close to it; readers recognise these phrasings and a fresh paraphrase reads
as wrong even when the meaning is right.

**2. Hadith narration and religious prose** — dignified but readable. `فرمایا`, `روایت ہے`,
`ارشاد فرمایا`. This is the bulk of `dua_infos` and `ruqyah_details`.

**3. Interface labels** — category and subcategory names, screen titles. Short noun
phrases, scannable in a list. Not sentences.

The register is a property of the field, not of your mood. Keep it stable across a file
and across the whole database.

## Verbs of speech carry respect — get these right

This is the single most common way a translation reveals itself as machine-made, and to a
religious reader it is not a style problem but a discourtesy.

| Subject | Use | Never |
|---|---|---|
| Allah | `اللہ تعالیٰ فرماتا ہے` / `ارشاد فرماتا ہے` | `اللہ کہتا ہے` |
| The Prophet ﷺ | `رسول اللہ ﷺ نے فرمایا` | `نبی نے کہا` |
| A Companion | `حضرت … رضی اللہ عنہ نے فرمایا` / `بیان کیا` | `اس نے کہا` |
| An ordinary person | `اُس نے کہا` | — |

Honorifics are not decoration; omitting them is an error. `ﷺ` after the Prophet,
`رضی اللہ عنہ` / `رضی اللہ عنہا` / `رضی اللہ عنہم` after Companions, `علیہ السلام` after
prophets, `رحمہ اللہ` after later scholars. Match the gender and number.

## Narration formulas — where machines reliably break

Hadith chains use fixed Arabic formulas. Urdu has fixed equivalents. Word-for-word
translation of the English gloss produces nonsense that reads as authoritative, which is
worse than obvious nonsense.

| Source | Correct Urdu | The machine failure |
|---|---|---|
| "on the authority of X" / `عن` | `X سے روایت ہے` / `X سے مروی ہے` | rendering *authority* as a power word — the Japanese pass produced `の権限で` ("by the jurisdiction of") 82 times before it was caught |
| "narrated by X" | `X سے روایت ہے` | transliterating "narration" as a loanword |
| "It was reported that…" | `مروی ہے کہ…` | `رپورٹ کیا گیا` |
| "he said, Say:" | `آپ ﷺ نے فرمایا: کہو —` | `اس نے کہا: کہو` |
| "The Messenger of Allah (ﷺ) used to…" | `رسول اللہ ﷺ … کیا کرتے تھے` | present tense |

`رَاوِی` (narrator) is a technical term. If a source says "the narrator said", that is
`راوی کہتے ہیں` — not a name, not "rabbi". That exact confusion shipped in the Japanese.

## Sentence shape

English piles modifiers before the noun and hangs relative clauses after it. Urdu prefers
to unfold the same information in order, ending on the verb. Restructure rather than
transplant.

**Example — subcategory 80**

Source: *Duas to be recited when one is in danger*
- Machine shape: `دعائیں پڑھی جانے کے لیے جب کوئی خطرے میں ہو` — English skeleton, Urdu skin
- Human shape: `مصیبت و تکلیف میں مبتلا ہونے پر پڑھی جانے والی دعائیں`

**Example — a hadith frame**

Source: *Abu Hurayra (RA) reported that the Messenger of Allah (ﷺ) said…*
- Machine shape: `ابو ہریرہ رضی اللہ عنہ نے رپورٹ کیا کہ اللہ کے رسول ﷺ نے کہا`
- Human shape: `حضرت ابو ہریرہ رضی اللہ عنہ سے روایت ہے کہ رسول اللہ ﷺ نے فرمایا`

Use *izafat* (`ـِ` / `ئے`) where Urdu naturally does — `نمازِ جنازہ`, `قبولیتِ دعا`,
`دعائے قنوت`, `خطبۂ نکاح`, `قعدۂ اخیرہ`. Flat noun-noun stacking where Urdu wants izafat
is a reliable machine-translation tell.

## Vocabulary register

Urdu draws on Arabic, Persian and Indic layers. Religious writing sits in the
Arabic–Persian layer. Reaching for the Indic word is not wrong Urdu, but it is wrong
*here* and sounds jarring.

| Prefer | Not | Why |
|---|---|---|
| دعا | پرارتھنا, بنتی | Indic register, wrong domain |
| عبادت | پوجا | pooja is Hindu worship |
| فرشتہ | دیوتا | deity ≠ angel |
| گناہ | پاپ | Indic register |
| مغفرت / بخشش | معافی (for sins) | معافی is everyday pardon |
| نمازِ جنازہ | انتم سنسکار | entirely wrong tradition |

At the same time, do not over-Arabize. If a plain Urdu word is the one a reader knows,
use it. The aim is dignified and *readable*, not a display of vocabulary.

## Keep every number exactly as it is

Hadith numbers, verse numbers, volume/page references like `4/39`, counts like "33 times".
Copy them; never convert, never spell them out, never let them drift into dates.

The Japanese pass turned `[Abu Dawud, 1481]` into "1481年" (the year 1481), `4/39` into
"April 39th", a verse number into an age, and a page number into an age. `verify.py`
compares the digits on both sides and fails the file if they differ — that check exists
because of those bugs.

Counting instructions (`33 مرتبہ`) use ASCII digits.

## Never invent, never trim

Add nothing that is not in the source — no explanations, no softening, no extra piety.
Drop nothing either. If the source has a `null`, the translation stays `null`; an empty
string is not the same thing and breaks the app.

Arabic passages inside `<ar>…</ar>` are copied through untouched. `transliteration` and
`reference` come from the English database verbatim — they are not translated. HTML tags
keep their exact structure; translate only the words between them.

## One term, one rendering

Fix the vocabulary in `GLOSSARY.json` *before* translating, and keep to it everywhere.
Drift is invisible while you work on one file and glaring when a reader moves between
screens.

The Japanese translation ended up with `アーイシャ` / `アイシャ` / `アイーシャ` for one
Companion's name across three tables. `verify.py` checks the glossary on every run so this
surfaces immediately rather than at the end.

Where the English source is itself wrong, record the deviation in `GLOSSARY.json` under
`overrides` with the reason, rather than silently diverging.

## The English source is not always right — check the Bengali

Every work item for the short tables carries `reference_bn`. Read both. Where they
disagree, the Bengali usually matches what the rows actually contain, because the app is
Bengali-origin and the English is a later, looser pass.

Two real cases from this project:

- Category 2 is *"Dua's Excellence"* in English, but its only subcategory is *"Excellence
  of doing Tasbeeh, Tahmid, Tahlil, Takbeer"*. That is dhikr. The Bengali says dhikr →
  `ذکر کی فضیلت`.
- Category 37 is *"Prophet's Dua"* in English, but it holds the duas of Adam, Ayyub and
  Yunus عليهم السلام. The Bengali is plural → `انبیاء و رُسل کی دعائیں`. The singular
  reading would have been wrong.

When the two sources disagree, **look at what the category actually contains** before
choosing. That check takes a minute and it is the difference between a correct name and a
plausible one.

## Working method

Read `references/workflow.md` for the mechanics — file format, which database each table
comes from, and how to build and verify. Read it before touching a work file for the first
time.

The short version:

1. Fill `GLOSSARY.json` first.
2. Work one file at a time, in the order in `PLAN.md`: the small tables settle the
   vocabulary that the long prose then has to match.
3. Edit only `target`. Never touch `key`, `id`, `part`, `of`, `frozen`, or `source`.
4. `python3 scripts/verify.py <file>` after each file.
5. Read your own output aloud before moving on. If a sentence would make an Urdu speaker
   pause, it needs another pass — the verifier cannot hear that.

## Self-review before declaring a file done

The checks a machine can run are in `verify.py`. These are the ones only you can do:

- Does every sentence sound like something a person would write? Read it aloud.
- Are the verbs of speech respectful and correctly assigned?
- Is the register right for this field, and consistent within the file?
- Would a reader who does not know English understand it without reconstructing the
  original?
- Is anything there that was not in the source?

`references/pitfalls.md` catalogues the specific defects found when auditing the finished
Japanese translation — every one of them shipped before being caught. Read it before an
audit, and skim it when a file feels off but you cannot say why.
