# Urdu review: ruqyah details 001–005

Translated and reviewed on 2026-09-27 against the complete English source,
supplied Arabic and transliteration, `GLOSSARY.json`, and the project's
natural-Urdu standard.

| Files | IDs | Split items | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_001.json`–`005.json` | 1–10 | 13 | 13 | Reviewed; verification passed |

## Review and corrections

- Translated every non-null user-visible target. All 13 `topic_name` values are
  null in the source and remain null; the 13 `text` values are complete.
- Read the Urdu independently after translation and corrected grammar,
  continuity, terminology, citation context, and natural Pakistani Urdu.
- Reviewed ID 9 as one continuous four-part answer across chunks 004 and 005,
  preserving all scholarly attributions, conditions, and the transition
  between drinking the water and the safeguards for written material.
- Preserved every Arabic block and Latin transliteration exactly. HTML tags,
  Qur'an references, hadith references, numeric values, and split boundaries
  retain their source structure.
- English collection names that occur only inside inline citations remain in
  English under the project rules. The field-specific glossary exceptions for
  IDs 1 and 9 document this without inserting artificial Urdu prose.

## Verification and residual checks

- Ran `python scripts/verify.py` separately on chunks 001–005 after the
  naturalness edits: all 13 translated fields passed with no problems.
- Compared HTML tag sequences and `<ar>` block contents between source and
  target: no mismatches were found.
- The target-only scan found no blank target, Bengali script, unexplained Latin
  prose outside preserved transliteration/citations, or nullness drift.
- Preserved IDs, keys, category links, ordering, source values, and all frozen
  metadata. Only target text and permitted status/review metadata changed in
  the work chunks.
