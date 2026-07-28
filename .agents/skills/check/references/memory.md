# check - memory

Self-improving notes for validation. Single canonical copy.

**The rule for this file: every defect that reaches a generated image, and that could have
been caught mechanically, becomes a permanent check here and in SKILL.md.**

## Grandfathered INFO results on the regression fixture

`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/` predates several rules.
These are expected and must not be reported as FAIL:

- `transcribes/*.txt` still use `.txt`. The `.md` rule applies from project 2 onward.
- `prompts/image-prompts.md` contains "mitten hands", from before the hand-shape conflict was
  resolved.
- `prompts/video-prompts.md` is empty. That is a reserved slot, always correct.

## Checks that exist because something actually went wrong

- **Duplicate timestamps.** Project 1 has `[3:24]` twice. Without the header note, the second
  scene image silently overwrites the first.
- **Style lock coverage counted, not eyeballed.** The old prompt re-typed the lock 7 times
  across files, and a thumbnail rule was fixed in one copy while two others still contradicted
  it. Counting the lock per prompt is how a partial edit gets caught.
- **Markdown inside the script file.** A hard FAIL, not a nit: the forced aligner flattens the
  file into a word stream, so `##` becomes a spoken token and shifts every later timestamp.
- **Banned thumbnail patterns.** silhouette, featureless, blank heads, and `arced across` are
  each a recorded generation failure. See the thumbnail skill's memory for the round history.
