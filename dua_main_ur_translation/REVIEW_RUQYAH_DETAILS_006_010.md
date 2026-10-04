# Urdu review: ruqyah details 006–010

Translated and reviewed on 2026-09-27 against the complete English source,
supplied Arabic and transliteration, `GLOSSARY.json`, and the project's
natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_006.json`–`010.json` | 11–19 | 9 | 9 | Reviewed; verification passed |

## Review and corrections

- Translated every non-null user-visible target. These chunks contain nine
  `text` values and no non-null `topic_name` values.
- Read all nine Urdu entries independently after translation and corrected
  sentence flow, agreement, quotation nesting, terminology, and natural
  Pakistani Urdu without removing source qualifications or repetitions.
- Preserved the long inline transliteration in ID 11. In ID 19, all three
  Arabic blocks and both Latin transliterations were copied directly from the
  source; only the visible `Transliteration` labels were translated.
- ID 15 says there are five commands although its supplied list visibly names
  six actions. The Urdu retains the source number and complete list rather
  than silently rewriting the source data.
- English collection names occurring only inside inline citations in IDs 14,
  15, and 16 remain in English under the project rules. Their field-specific
  glossary exceptions document this presentation.

## Verification and residual checks

- Ran `python scripts/verify.py` separately on chunks 006–010 after the
  naturalness edits: all nine translated fields passed with no problems.
- Compared HTML tag sequences and `<ar>` contents between source and target;
  no mismatches were found. The text inside each ID 19 transliteration block
  also matches the source exactly after its translated label.
- The target-only scan found no blank target, Bengali script, replacement
  character, or unexplained Latin prose outside preserved transliterations
  and citations.
- Preserved IDs, keys, category links, ordering, source values, reference
  numbers, and frozen metadata. Only target text and permitted status/review
  metadata changed in the work chunks.
