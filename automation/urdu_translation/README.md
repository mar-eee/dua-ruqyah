# Urdu Dua/Ruqyah translation automation

This controller runs one bounded Codex batch at a time and invokes the
`urdu-dua-ruqyah` skill on every run.

## Behaviour

- Windows Task Scheduler checks every 5 minutes.
- `state.json` contains the actual adaptive `next_run_at`; checks before that
  time exit without launching Codex, so these checks consume no model tokens.
- Review-only runs handle at most five chunks.
- New-translation runs handle at most three chunks.
- Measured CLI token usage, model-reported pressure, verification failures, and
  the user's requested 1–2 hour cadence determine the next delay.
- Before every run, the controller reads the real Codex primary and secondary
  usage windows from the local app server. For the five-hour window it enters
  conservation mode at 60% and pauses new work at 80%; for longer/weekly
  windows it conserves at 75% and pauses at 92%. Conservation means at most two
  review chunks or one new chunk. A paused controller resumes five minutes
  after the exact limiting reset time, without guessing reset schedules.
- A lock prevents overlapping runs. Failures use exponential backoff up to
  eight hours.
- Every successful run must verify changed chunks, perform a naturalness and
  residual-language pass, create review evidence, and regenerate status.
- Books and book details are deliberately excluded for now.

## Controls

- Pause: set `enabled` to `false` in `state.json`.
- Resume immediately: set `enabled` to `true`, set `next_run_at` to `null`, and
  run `run.ps1 -Force` or wait for the next 5-minute scheduler check.
- Logs and structured results are written under `logs/`.
- Scheduled task name: `Dua Ruqyah Urdu Translation Automation`.

The controller works directly in `G:\dua-ruqyah`, so keep the ChatGPT desktop
app and computer running for local scheduled work.
