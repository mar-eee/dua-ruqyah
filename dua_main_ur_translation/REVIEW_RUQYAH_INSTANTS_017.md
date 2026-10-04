# Urdu review: ruqyah instants 017

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_017.json` | 224–244 | 21 | 63 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 63 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, quotation boundaries, and dignified Pakistani Urdu.
- Row 243 reuses the exact reviewed Urdu for Quran 17:81. Repeated Arabic was
  also compared across the completed ruqyah chunks for wording consistency.
- Row 232 preserves Arabic `alladhina ittaqaw` naturally as those who adopted
  taqwa without importing Allah from the explanatory English expansion. This
  decision is recorded as a field-specific glossary override.
- The longer passages in rows 224, 232, 236, and 242 received dedicated
  continuous-flow checks for speaker changes, pronouns, and verse order.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_017.json`
  after the naturalness edits: 21 entries and 63 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.
