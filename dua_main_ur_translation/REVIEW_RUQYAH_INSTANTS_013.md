# Urdu review: ruqyah instants 013

Translated and reviewed on 2026-09-27 against the English source, Bengali
context, supplied Arabic, `GLOSSARY.json`, established reviewed parallels,
and the project's natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_013.json` | 190–200 | 11 | 33 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic meaning, then read all 33 target
  values continuously for accuracy, fluency, speaker, number, agreement,
  verse sequence, and dignified Pakistani Urdu.
- Reused exact reviewed wording for rows 190, 193–195, 197, and 199. The
  reviewed wording of Ar-Rahman 55:33–36 is also preserved exactly at the end
  of row 192; its preceding verses 26–32 were reviewed as one continuous
  passage, including the shift from singular address to the recurring dual.
- Row 196 preserves respectful Quranic address throughout without importing
  Muhammad's name from an explanatory English bracket. Its established
  Al-A'la wording was adapted only where respectful second-person forms were
  required by this standalone passage.
- Row 198 received a separate spoken-flow correction for tense, the passive
  follower relationship, severed ties, and the final consequence, while
  retaining all three verses and their logical sequence.
- Row 190 follows the supplied Arabic and Bengali expression “the caller to
  Allah” rather than the English “Messenger of Allah.” The decisions for rows
  190 and 196 are recorded as field-specific `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `python scripts/verify.py work/ruqyah_instants/ruqyah_instants_013.json`
  after the naturalness edit: 11 entries and 33 translated fields passed with
  no problems.
- Preserved Arabic, IDs, keys, links, audio, ordering, nullness, and source
  values. Only target text and permitted status/review metadata changed in the
  work chunk.
- The target-only scan found 33 populated fields and no Bengali script,
  unintended Latin prose, non-ASCII digit glyph, or replacement character.
- Exact-repeat checks passed for six complete reviewed passages and the
  reviewed Ar-Rahman 55:33–36 subsection.

