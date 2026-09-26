# Urdu review: duas 044

Translated and reviewed on 2026-09-25 against the English source, Bengali
context, supplied Arabic, cited Quran text where sources conflicted,
`GLOSSARY.json`, and the project's natural-Urdu standard.

| File | IDs | Entries | Top-level translated fields | Result |
|---|---|---:|---:|---|
| `work/duas/duas_044.json` | 591–620 | 30 | 60 | Reviewed; verification passed |

There are no nested group targets in this chunk.

## Review and corrections

- Read all 60 targets as continuous Urdu after semantic comparison with the
  English, Bengali, and supplied Arabic. Titles and Quranic renderings were
  checked for fluent Pakistani Urdu, agreement, speaker, number, and meaning.
- Preserved Arabic, IDs, keys, references, audio values, ordering, nullness,
  and ASCII verse/title numbers.
- Restored `على الله توكلنا` in row 595 because the English omits it while the
  supplied Arabic, Bengali context, and Quran 7:89 contain it.
- Named steadfastness rather than the English title's mismatched devotion in
  row 613, following `وثبت أقدامنا` and Quran 3:147.
- Rendered `حكما` in row 619 as `حکمت`, supported by the Bengali context and
  Quran 26:83 rather than the English source's `authority`.
- Recorded all three genuine source decisions as field-specific
  `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `scripts/verify.py` on this file after the final target edits; all 30
  entries and 60 translated fields pass.
- The target-only scan found no Bengali script, unintended Latin prose,
  non-ASCII digit glyphs, or replacement characters.
