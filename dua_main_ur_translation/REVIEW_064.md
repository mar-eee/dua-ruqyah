# Urdu review: duas 064

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels, and
the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Nested targets | Result |
|---|---|---:|---:|---:|---|
| `work/duas/duas_064.json` | 980–1001 | 22 | 45 | 0 | Reviewed; verification passed |

This completes the indexed `duas` range through ID 1001. It does not complete
the whole database, whose other required tables remain tracked separately in
`WORK_STATUS.md`.

## Review and corrections

- Reused reviewed Urdu wording for exact Quranic and hadith parallels, then
  read every target again in its current context for natural flow, meaning,
  speaker, number, agreement, and devotional register.
- Row 981 restores the supplied opening reliance clause omitted by English.
- Row 994 restores the opening protection request in verse 9, which appears in
  the supplied Arabic and Bengali but is absent from English.
- Row 995 stops where the supplied Arabic stops because row 996 separately
  stores the verse's final clause; this avoids duplicating it from English.
- Rows 988 and 1000 use identical Urdu for the identical supplied verse, and
  row 1001 preserves the morning/evening distinction and the full instruction
  about thanking Allah.
- All source-conflict decisions are recorded as field-specific overrides in
  `GLOSSARY.json`.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edits: 22 entries and 45
  translated fields passed with no problems.
- Preserved Arabic, IDs, keys, references, audio, transliteration, ordering,
  nullness, and source number values.
- The target-only scan found no Bengali script, non-ASCII digit glyphs,
  replacement characters, or unintended Latin text.
