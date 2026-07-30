# check - memory

Self-improving notes for validation. Single canonical copy.

**The rule for this file: every defect that reaches a generated image, and that could have
been caught mechanically, becomes a permanent check here and in SKILL.md.**

## Grandfathered INFO results on the regression fixture

`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/` predates several rules.
These are expected and must not be reported as FAIL:

- `transcribes/*.txt` still use `.txt`. The `.md` rule applies from project 2 onward.
- `prompts/image-prompts.md` contains "mitten hands", from before the hand-shape conflict was
  resolved. So does `prompts/character-prompts.md`, 5 times.
- `prompts/video-prompts.md` is empty. That is a reserved slot, always correct.
- `metadata.md` was never written for this project. Confirmed with
  `git log -- projects/1-*/metadata.md`, which returns nothing. Step 8 has nothing to check.
- The cast sheets do not reference `brand/MASCOT.jpeg`. That instruction postdates them, so
  the Step 5 count is 0.
- Em dashes appear in all three files under `prompts/`. They predate the no-em-dash rule.
- **Step 7's banned-pattern grep fires 4 times here, and every hit is a false positive.**
  The words describe the *background crowd*, which is meant to be drawn as faceless black
  shapes: "dense packed row of flat solid black featureless silhouettes", and "blank heads"
  for the same crowd. The rule exists to stop the *subject* being rendered featureless. The
  grep cannot tell subject from background, so read the surrounding clause before calling it
  a FAIL. Only 1 of the 5 concepts uses the split comparison layout, below the 2 the skill
  asks for; that also predates the rule.
- `prompts/thumbnail-prompts.md` keeps its legacy header, `[thumb-*]` labels, and blank
  separators. The five-line prompt-only import format applies from project 2 onward.

So the fixture does **not** currently produce an all-PASS table, and the quality bar in
`AGENTS.md` overstates it. What regression testing actually means here: the items above stay
exactly as listed, and everything else passes. Steps 3, 4, and 6 are the load-bearing ones,
and those do pass clean, including the canonical one-line `[3:24]` to `[3:25]` remap diff.

## Checks that exist because something actually went wrong

- **Duplicate timestamps.** Project 1 has `[3:24]` twice, project 3 has `[8:26]` twice. Without
  a remap the second scene image silently overwrites the first. The remap now lives in the
  prompt stamps themselves (`[8:26]` then `[8:27]`), not in a header note, because
  `image-prompts.md` no longer has a header. Judge a differing diff line arithmetically: the
  transcript stamp must be one of the `declared duplicates` and the prompt stamp must be that
  stamp advanced by one second.
- **`image-prompts.md` is prompts only from project 3 onward.** It is imported wholesale into an
  image tool that treats every line as a prompt, so a title or cast line becomes a junk
  generation. `grep -v '^\[' "$F" | grep -c .` must be 0. Measured 2026-07-29: project 1 has 4
  such lines and project 4 has 4, projects 2 and 3 have none. Report those two as INFO rather
  than FAIL, and flag project 4 as needing a strip before its prompts are imported. Project 1 is
  the fixture and stays as it is.
- **Style lock coverage counted, not eyeballed.** The old prompt re-typed the lock 7 times
  across files, and a thumbnail rule was fixed in one copy while two others still contradicted
  it. Counting the lock per prompt is how a partial edit gets caught.
- **Markdown inside the script file.** A hard FAIL, not a nit: the forced aligner flattens the
  file into a word stream, so `##` becomes a spoken token and shifts every later timestamp.
- **Banned thumbnail patterns.** silhouette, featureless, blank heads, and `arced across` are
  each a recorded generation failure. See the thumbnail skill's memory for the round history.
- **Headline integration is counted, not inferred.** A dark top area ending at a hard
  horizontal seam reached generated Project 2 thumbnails and made the headline look like a
  detached banner. New cinematic thumbnail prompts must include both the continuous-scene
  integration clause and the explicit separate-band prohibition five times.
