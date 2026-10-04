# Urdu review: ruqyah instants 007

Translated and reviewed on 2026-09-26 against the English source, Bengali
context, supplied Arabic, cited primary texts where sources conflicted,
`GLOSSARY.json`, established reviewed parallels, and the project's
natural-Urdu standard.

| File | IDs | Entries | Translated fields | Result |
|---|---|---:|---:|---|
| `work/ruqyah_instants/ruqyah_instants_007.json` | 89–104 | 16 | 48 | Reviewed; verification passed |

## Review and corrections

- Translated every topic, title, and Quranic or Prophetic meaning. All 48 target
  values were then read continuously for semantic accuracy, fluency, speaker,
  number, agreement, devotional register, and glossary terminology.
- Reused nine complete reviewed translations for identical Arabic passages and
  the reviewed verses 1–4 wording in row 98. Repeated topics, collection names,
  surah titles, and ASCII references follow the established project style.
- Row 90 restores all seven requests in the Arabic, including mending the
  supplicant's deficiency, well-being, and raised rank. Row 92 omits the extra
  English phrase absent from the supplied Arabic. Row 95 retains the Arabic
  conditional fragment rather than the English concessive wording.
- Abu Dawud 3107 gives the funeral wording as the main report and explicitly
  records Ibn al-Sarh's “to prayer” variant. Row 97's frozen Arabic contains
  that prayer variant, so the Urdu follows it and was smoothed in the Urdu-only
  pass to “چل کر نماز ادا کرنے جا سکے”.
- Row 98's frozen Arabic, title, and Bengali stop at Quran 67:4, while its
  English translation continues with verse 5. The Urdu preserves verse 5 and
  its source number after checking Quran 67:5, without altering frozen data.
- Rows 100, 103, and 104 follow their supplied Arabic where the Bengali or
  English diverges. All eight genuine field-level conflict decisions are
  recorded as specific `GLOSSARY.json` overrides.

## Verification and residual checks

- Ran `scripts/verify.py` after the final naturalness edit: 16 entries and 48
  translated fields passed with no problems.
- Compared the completed chunk with Git HEAD: Arabic, IDs, keys, source text,
  Bengali context, links, audio, transliteration, references, ordering, and
  nullness are unchanged. Only target text and permitted status metadata
  changed in the work file.
- The target-only scan found no blank target, Bengali script, unintended Latin
  prose, non-ASCII digit glyph, or replacement character.

