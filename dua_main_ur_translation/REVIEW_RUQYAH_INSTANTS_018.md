# Urdu review: ruqyah instants 018

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_018.json` | 245–268 | 24 | 72 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 72 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, quotation boundaries, and dignified Pakistani Urdu.
- Rows 245, 248, 250, 260, 263, and 265 reuse exact reviewed Urdu. The exact
  duplicate rows 258–259 retain identical titles and translations.
- Row 247 is mislabeled Ash-Shu'ara in both reference titles, although the
  supplied Arabic is Quran 42:24 from Ash-Shura; the Urdu title gives the
  correct surah. Row 266 omits Muhammad because it occurs only in an
  explanatory English bracket. Both decisions are recorded in `GLOSSARY.json`.
- The longer passages in rows 248, 253, 255, 256, and 261 received dedicated
  continuous-flow checks for legal wording, pronouns, and verse order.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_018.json`
  after the naturalness edits: 24 entries and 72 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
