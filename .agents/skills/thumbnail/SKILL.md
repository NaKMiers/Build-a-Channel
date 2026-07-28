---
name: thumbnail
description: Write five A/B-testable thumbnail concepts for a TossExplains video into prompts/thumbnail-prompts.md, following the evidence-backed rules from the competitor teardown. Use when the user says "thumbnail", "thumbnails", "thumbnail prompts", or "thumbnail concepts".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# thumbnail

Stage 5b of the TossExplains pipeline. The thumbnail decides whether the video is watched at
all, so it is generated to a fixed, proven pattern, not invented per video.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/thumbnail-rules.md` - **the whole file, every run.** Rules A to F and the
  two layout templates. Every rule there was validated or forced by a real generation
  round.
- `.agents/rules/visual-style.md` - the two verbatim strings and the palette
- `.agents/rules/file-formats.md` - the `prompts/thumbnail-prompts.md` section
- `.agents/skills/thumbnail/references/memory.md`
- `research/thumbnail-swipe/ANALYSIS.md` when you need the reasoning behind a rule

## Preconditions

```bash
P="projects/<n>-<slug>"
ls "$P"/script_*.md
grep -oE '@[A-Z]+' "$P"/prompts/character-prompts.md | sort -u
```

Both the script and the cast file are required. The transcript is not. If the cast file is
missing, stop and say to run `/cast`: thumbnails refer to cast members by `@TOKEN` and the
sheets must exist for generation.

## Step 1 - Mine the script for drawable hooks

Read the script and extract, in writing to yourself:

- Every **physical object or creature** the script actually contains. This is the critical
  list. Rule C says every noun in a thumbnail question must be a thing drawn in the frame,
  and the two concepts that failed our A/B round failed exactly here.
- Every **number** the script states, and which two of them invite subtraction.
- The **five distinct moments** the concepts will be built on: the opening feeling, the
  named experiment, the ancestral scene, the then-vs-now split, the counterintuitive
  number.
- The **read title**, so no thumbnail question restates it.

If the script yields no drawable objects at all, say so. That is a script problem, not a
thumbnail problem, and no amount of prompt wording fixes it.

## Step 2 - Draft the five questions first, before any prompt

For each of the five, write the 2 to 4 word ALL CAPS question and name the object in the
frame that the question points at. Then run each one through this gate:

- Is every noun in it drawn in the frame? If not, rewrite.
- Does it restate the title? If so, rewrite.
- Is it 4 words or fewer, ALL CAPS, ending in `?`
- Does the frame have two parties with something happening between them?
- If it uses a number, is that number NOT also printed in the question text?

A question that fails any gate is dead. Rewrite it before writing the prompt.

## Step 3 - Build the prompts

- **At least two of the five use the split comparison layout.** It won the A/B round
  outright.
- Fill the bracketed slots in the layout templates from `thumbnail-rules.md`. Keep
  everything outside the brackets verbatim, including the STYLE ANCHOR and STYLE LOCK.
- Each concept is built on a different moment from the script, so the five are genuinely
  A/B testable rather than five variants of one idea.

Every prompt must satisfy all of these, and they are all in `thumbnail-rules.md`:

- Text runs perfectly straight, full-bleed edge to edge, at the very top. Not arced.
- The band behind the text is the darkest area of the image.
- A drawn number is roughly half the frame height, the largest object in its half.
- The scene has a ground line, a horizon, and one environment prop from the script, plus
  one warm light source against a dark cool palette.
- Co-stars have visible faces with visible expressions. **Never featureless, blank, or
  silhouette crowds.**
- The sad expression is written as explicit eyebrow geometry plus "not angry, not
  frowning".
- No body modification on the mascot.
- No exact figure count above five.
- No prop in the lettering yellow `#F5C518`.
- Exactly one figure looks straight out at the viewer, and it is a figure that has eyes.
- The bottom-right corner is left completely empty.

## Step 4 - Write the file

Path: `projects/<n>-<slug>/prompts/thumbnail-prompts.md`

Header block, then five unbroken lines `[thumb-a]` through `[thumb-e]`, one blank line
between, nothing after the last. The header must include the note that the logo badge is
added in the editor at bottom-left, not drawn by the image model.

## Step 5 - Verify mechanically

```bash
F="$P/prompts/thumbnail-prompts.md"
grep -c '^\[thumb-' "$F"                                    # must be 5
grep -c 'running perfectly straight across the very top' "$F"
grep -c 'not arced and not curved' "$F"
grep -c 'darkest area of the whole image' "$F"
grep -c 'straight out of the frame directly at the viewer' "$F"
grep -c 'bottom-right corner of the frame left completely empty' "$F"
grep -c 'educational YouTube explainer doodle style\.$' "$F"

# banned patterns, all must be 0
grep -ciE 'silhouette|featureless|blank (white )?(oval|head)' "$F"

grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"
```

Every count except the banned-pattern line must be 5. The banned-pattern line must be 0.

## Step 6 - Report and hand off

In chat, list **only the five questions** as a short numbered list so the user can judge
the hooks at a glance, say which one you recommend and why, and name which layout each
uses. **Do not paste the five full prompts into chat**, they live in the file. Then:

> Thumbnail prompts saved to `<path>`.
>
> Generate all five, attaching the sheets for the `@` tokens in each, and save them to
> `outputs/` as `thumbnail-1.jpg` through `thumbnail-5.jpg`. Export at 1280x720, under 2 MB.
>
> Add the channel logo in your editor, small, bottom-left of the winner. Do not ask the
> image model to draw it.
>
> Then shrink your favourite to 120 px wide and look at it. If the question is not readable
> and the emotion is not obvious in half a second, regenerate. Do not rescue a weak
> thumbnail with more text. If the model garbles the lettering, generate the frame with the
> text clause deleted and add the words in your editor. If a frame comes back with large
> empty areas, the background was too flat: add a ground line, a horizon, and one warm
> light source, then regenerate.
>
> Rename the accepted one with an `-accepted` suffix, then run **`/check`**.

## Guardrails

- Never write a question whose noun is not drawn in the frame. This is the single rule that
  killed our v1 and v2 rounds.
- Never arc the text. Never move it off the top. Never add a second line.
- Never use a flat single-color empty background.
- Never repeat a drawn number in the question text.
- Never ask the image model to draw the logo.

## Self-improvement

Read `.agents/skills/thumbnail/references/memory.md` at the start of every run. **Append
after every generation round**: which concept the user accepted, which failed, and the
specific visual failure mode. This memory is the mechanism that produced rules A to F, and
it is how the next round gets better. Record the failure even when it seems obvious.
