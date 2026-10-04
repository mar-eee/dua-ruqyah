# Urdu review: ruqyah details 016–018

Translated and reviewed on 2026-09-27 against the complete English source,
the non-aligned Bengali context, supplied Arabic, `GLOSSARY.json`, established
reviewed Quranic parallels, and the project's natural-Urdu standard.

| Files | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_details/ruqyah_details_016.json`–`018.json` | 26–29 | 8 | 9 | Reviewed; verification passed |

## Review and corrections

- Translated all nine non-null user-visible targets: eight `text` values and
  the non-null `topic_name` in row 27. The two null topic names remain null.
- Completed split parts 8–12 of row 26 without moving text across chunk
  boundaries. Reused the already reviewed Urdu meanings of Quran 46:29–32,
  55:33–36, 59:21–24, 72:1–9, and Surahs al-Ikhlas, al-Falaq, and al-Nas.
- Read the prose independently as continuous Urdu after semantic comparison.
  Smoothed the explanations of evoking a jinn, post-treatment precautions,
  the pledge and exit procedure, and the Muslim/non-Muslim treatment cases.
- The Bengali rows 26–29 belong to a different dataset and are not parallel
  to these English rows. They were read as context but were not substituted
  for the required English-routed source.
- In row 28, the English meaning omits the opening `Allahumma` present in the
  supplied Arabic pledge. Urdu restores the direct invocation while preserving
  the Arabic and transliteration verbatim; the decision is recorded as the
  field-specific `ruqyah_details.text.28` glossary override.

## Verification and residual checks

- Ran `python -X utf8 scripts/verify.py` separately on chunks 016, 017, and
  018 after the final naturalness edits. All eight entries and nine translated
  fields passed with no problems.
- Preserved every Arabic block, HTML tag sequence, ID, key, frozen field,
  category link, split marker, order, verse number, null, and source value.
- The target-only scan found no blank target, Bengali script, non-ASCII digit
  outside preserved Arabic blocks, or replacement character. Remaining Latin
  text is limited to normalized Quran references and the source transliteration
  that the project rules require preserving; no unintended Latin prose remains.
