# check - memory

Self-improving notes for validation. Single canonical copy.

## V2 version and plan checks, 2026-08-03

V1 and V2 strings are separately canonical in `visual-style.md`. Projects 1 through 5 remain
V1. A V2 project must have one `prompts/visual-plan.md`, complete V2 anchor and lock coverage,
and zero V1 string occurrences. A V1 project must not be failed for lacking a visual plan.

The V2 plan is checked mechanically for generated-row coverage, enums, tier totals, surface
totals, backward source links, one delta per non-plate beat, 4 second holds, 28 to 32 whole-video
beats per minute, register runs, and one-to-five-word editorial text. The pilot found two prompt
failures worth retaining as checks: generic crowd clothing must not take Toss's saturated blue,
and ATMOSPHERIC richness must remain at or below 10 percent.

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

## Project 7 full-rebuild check (2026-08-07): two by-the-letter V2 deviations worth understanding

- **Rhythm arithmetic when the plan has zero CAPCUT rows.** With no CapCut-only beats, planned
  beats per minute equals raw transcript cue density. Project 7's 297 cues over 669 seconds is
  26.6, under the 28 to 32 band, even though no individual hold exceeds 4 seconds. The lever is
  CapCut rows, not more generations: 16 added CapCut beats lift it to 28.0. Report the number
  and the cheapest fix, do not demand new prompts for it.
- **Reading the register-run flags.** The run check fires on more-than-3 same-register beats
  that cross a plate boundary. Two adjacent 2-beat build chains in the same register (a card
  pair followed by another card pair) trip it exactly like a lazy 5-beat hold does. Before
  reporting, print the flagged window: a run whose plates each carry sourced deltas is a
  pacing observation, a run of near-identical variants is real monotony. Project 7's 10 flags
  were all the former, including one deliberate 12-beat STORY stretch that is a single
  continuous scene (the yell, then the pull-back to the room).

## Project 15 check (2026-09-12): the zsh glob trap again, from a second snippet

Project 11 recorded that Step 1's inventory `for` loop aborts under zsh because `script_*.md`
is expanded in the current directory. **The same trap lives in the four counting lines directly
below it**, and it fired here:

```bash
echo "characters: $(ls "$P"/characters/* 2>/dev/null | grep -v '\.gitkeep$' | grep -c . )"
```

A freshly scaffolded directory holds only `.gitkeep`, which is hidden, so `*` matches nothing and
zsh's `nomatch` kills the subshell with `no matches found` before `ls` ever runs. The `2>/dev/null`
does not help, because the shell aborts before redirecting anything. It printed 0, which happens to
be the right answer, so **the bug is invisible exactly when the count is zero and would be wrong
the moment it is not.**

Durable fix, and it needs no glob at all:

```bash
for d in audios characters outputs scenes; do
  echo "$d: $(find "$P/$d" -type f ! -name '.gitkeep' | wc -l)"
done
```

**Second distinct snippet in this file with the same cause.** Treat any unquoted `*` inside a
`check` command as a defect on sight, not just the ones already recorded.

### Result on project 15

Every artifact that exists passes. Script 1923 words with zero markdown characters, 297 cues with
zero malformed lines, cast 6 tokens over 12 fences with 5 V2 sheet openings and zero positive
`mitten` hits, image prompts 297 for 297 cues with V2 anchor and lock on all of them and zero V1
strings, 108 chain breaks all well formed and all opening a PLATE, 36 `@[timestamp]` references all
resolving backward and all carrying the SCENE REFERENCE LIMIT, zero ledger returns missing their
reference, plan 330 rows with exactly 297 generated, all four enums clean, surfaces summing to 297
with cobalt and pure white inside their ceilings, cadence 31.5 beats per minute, zero holds over 4
seconds, thumbnails 9 lines and 5 records with every required clause at 5.

**The 15 register-run flags are all the project 7 shape and none is monotony.** Every flagged
window is two or three adjacent short build chains in the same register, each opening its own
`PLATE` and each carrying a sourced delta, which is what a card-and-diagram act looks like when it
is planned per cue. Printing the window is what distinguishes it from a lazy five-beat hold, and
that step is not optional.

### REPO-WIDE FAIL that is not project 15's: em dashes in four tracked files

Step 2's repo sweep is not project-scoped and it found live violations of the house rule outside
the grandfathered fixture and outside `prompts/retired/`:

| File | Hits |
| ---- | ---- |
| `.agents/skills/metadata/SKILL.md` | 5 |
| `.agents/skills/check/SKILL.md` | 3 |
| `.agents/rules/file-formats.md` | 1 |
| `projects/9-.../outputs/metadata.md` | 1 |

The project 9 one is the serious one: it sits in a shipped description at line 22, so it would go
out on YouTube. The other three are rule and skill prose, which the house rule covers explicitly
("rule files, or chat replies"). **`check` has run many times without these being reported, which
means the Step 2 sweep output was being skimmed rather than read.** Report the file list every
run, not just the count.


## Project 11 check (2026-08-28): the skill's own Step 1 snippet aborts under zsh

Step 1's inventory loop is

```bash
for f in script_*.md outputs/metadata.md ...; do ls "$P"/$f ...
```

The unquoted `script_*.md` is glob-expanded **by the shell in the current directory**, not by
`ls` inside the project directory. Under zsh with default `nomatch`, no `script_*.md` exists at
the repo root, so the shell aborts the entire command with
`no matches found: script_*.md` and **exit 1 before a single check runs**. Under bash it would
degrade differently: the pattern passes through literally and `ls` reports one missing file, so
the loop keeps going and only that row is wrong.

Fix in place when running it: name the script file literally, or test with `[ -f "$P/$f" ]`
instead of `ls`, which needs no glob at all. The durable fix is to change the snippet in
`check/SKILL.md` to `[ -f ... ]` and drop the glob, since the script's real name is discoverable
with one `ls "$P"/script_*.md` beforehand. **A verification snippet that cannot run is worse
than a missing one: the exit status looked like a failed project rather than a failed check.**

### Result on project 11

Everything that exists passes: script 2076 words with zero markdown characters, 332 cues with
zero malformed lines and zero duplicate timestamps, cast 10 fences with 4 V2 opening lines and
zero positive `mitten` hits, 5 cast tokens all used legally and zero orphan tokens in the
thumbnail file, thumbnails 9 lines and 5 records, metadata 7 chapters all resolving to real
transcript timestamps and 20 hashtags, visual plan 370 rows with exactly 332 generated matching
the cue count, zero em dashes anywhere.

Legitimately absent, not defects: `prompts/image-prompts.md` (the scenes prose pass is the
declared next step), `characters/` empty (sheets not generated yet, prompts are ready),
`scenes/` empty (follows image-prompts), and `outputs/captions/` holding 2 of 8 languages.
**`check` should report an empty `characters/` alongside a complete `character-prompts.md` as
PENDING GENERATION rather than a fault**, because the pipeline's artifact is the prompt file and
the images are a human step.
