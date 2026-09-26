Use the `$urdu-dua-ruqyah` skill for this run. Read its complete `SKILL.md`,
the required project-scope and Urdu-style references, and the complete
`G:\dua-ruqyah\dua_main_ur_translation\GLOSSARY.json` before editing.

{{AUTOMATION_CONTEXT}}

Work autonomously on exactly one safe batch in
`G:\dua-ruqyah\dua_main_ur_translation`.

Selection rules, in priority order:

1. Never repeat a chunk that already has explicit natural-Urdu review evidence.
2. The durable review sequence currently resumes at `duas_011.json`; row/chunk
   010 was already reviewed. Review at most five consecutive chunks per run:
   011–015, 016–020, 021–025, 026–030, 031–035, then 036–039. Chunk 040 is not
   reviewable until it has first been translated.
3. After the existing translated dua chunks have review evidence, translate and
   fully review at most three new consecutive dua chunks per run, beginning with
   the first pending chunk reported by the workspace status.
4. After `duas` is translated and reviewed, continue the Dua/Ruqyah scope in
   this order: `ruqyah_instants`, `ruqyah_details`, and any translated ruqyah
   category/subcategory/video chunks that still lack natural-Urdu review
   evidence. Use at most five chunks for review-only work or three chunks when
   creating new translations.
5. Do not work on `books` or `book_details`; the user has explicitly postponed
   book work.
6. If five review chunks or three translation chunks are unusually large or
   deeply nested, reduce the batch rather than lowering quality. Never exceed
   those maxima.

Quality and safety rules:

- Run the skill's work-status audit at the start and end.
- Read the English source and Bengali context together. Check supplied Arabic
  and the cited primary text when they conflict, and record genuine conflict
  decisions as specific `GLOSSARY.json` overrides.
- Write natural, dignified, literary Pakistani Urdu—not literal or mechanical
  Urdu. Every user-visible target must be Urdu; only inline and top-level
  references remain normalized English with ASCII digits.
- Translate nested `group_items` and other user-visible nested text.
- Preserve Arabic, IDs, keys, links, audio, transliteration, reference values,
  numbers, ordering, markup, and nullness.
- Edit with `apply_patch`. Do not regenerate translated work files and do not
  overwrite unrelated user changes.
- Verify every changed chunk separately with `scripts/verify.py`, perform a
  target-only naturalness pass, scan for Bengali and unintended Latin prose,
  mark successfully completed chunks `done`, retain/update `PLAN.md`, create or
  update a precise `REVIEW_*.md` evidence file, and regenerate
  `WORK_STATUS.md`.
- Do not build the final database until all relevant completion gates pass.
- Do not use subagents.

Cadence guidance:

- Baseline review delays requested by the user are: through chunk 020: 2 hours;
  through 025: 2 hours; through 030: 1 hour; through 035: 1 hour; through 040:
  2 hours.
- For later translation runs, recommend 1 hour for low token pressure, 2 hours
  for medium pressure, and 4 hours for high pressure. Increase the delay after
  a difficult or correction-heavy batch. The controller will combine this with
  measured CLI token usage and failure backoff.

Your final response must satisfy the provided JSON output schema. Set
`verification_passed` true only if every changed chunk passes. In `summary`,
briefly state what was corrected or translated. In `next_action`, identify the
next concrete batch without claiming that postponed books are complete.
