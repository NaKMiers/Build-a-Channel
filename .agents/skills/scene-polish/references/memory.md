# Scene Polish Memory

- Validate counts and destinations before any rename.
- Never trust directory listing order. Map numbered downloads to prompt timestamps only
  after confirming a contiguous sequence.
- Scene filenames use `[M-SS].jpg` because Windows forbids colons.
- Range-folder labels are claims, not evidence. Compare their actual contents with the
  prompt timestamps in range.
- Accept `.jpg` and `.jpeg` as numbered inputs, but normalize final names to `.jpg`.
- A duplicate timestamp or existing destination is a hard stop.
