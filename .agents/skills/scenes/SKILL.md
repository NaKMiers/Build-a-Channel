---
name: scenes
description: Write one detailed text-to-image prompt for every timestamp in a TossExplains transcript, using the locked cast, into prompts/image-prompts.md. Use when the user says "scenes", "image prompts", "scene prompts", or "prompts for every timestamp".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# scenes

Stage 4 of the TossExplains pipeline, and the largest artifact: one prompt per transcript
cue, typically 230 to 255 of them.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md` - **the whole file.** The two verbatim strings, the
  background tone map, where emotion lives, the head color code, the nine frame types.
- `.agents/rules/file-formats.md` - the `prompts/image-prompts.md` section
- `.agents/skills/scenes/references/memory.md`
- The project's `prompts/character-prompts.md` cast table. This is the only legal source
  of `@` tokens.

## Preconditions - both required

```bash
P="projects/<n>-<slug>"
wc -l "$P"/transcribes/transcript.md
grep -oE '@[A-Z]+' "$P"/prompts/character-prompts.md | sort -u
```

- No transcript: stop, say to run `/transcript`.
- No cast file: stop, say to run `/cast`. **Never invent a cast inline.** The whole point
  of the cast system is that the sheet carries the design.
- Transcript under 20 lines: stop and say "This looks incomplete. A 10 to 14 minute video
  should have 80 to 120 timestamp lines."

## Step 1 - Inventory the transcript

```bash
T="$P/transcribes/transcript.md"
grep -c . "$T"                           # total cues
awk '{print $1}' "$T" | sort | uniq -d   # duplicate timestamps
```

Record the totals. They go in the file header and the `check` skill verifies them.

## The prompt rules

1. **Every prompt begins with its timestamp, copied character for character from the
   transcript.** `[0:00]` stays `[0:00]`, `[00:00]` stays `[00:00]`. Never reformat,
   re-pad, or renumber a timestamp: these strings become the image file names, so they
   must match the transcript exactly.
2. **The `[MM:SS]` prefix and every `@TOKEN` are instructions for the human and the file
   system, not visual content.** They must never appear as rendered text in the generated
   image: no timestamp, clock, or counter burned into a corner, no literal "@NAME" caption
   anywhere in the frame. This is why every prompt's STYLE LOCK explicitly repeats that
   negative. **Never drop it.**
3. **Every prompt opens with the STYLE ANCHOR** from `visual-style.md`, copied character
   for character.
4. **Every prompt ends with the STYLE LOCK** from `visual-style.md`, copied character for
   character.
5. **Refer to every cast member by their `@` token, never by description.** Write
   `@ALAN sits hunched on the edge of a bed`, never `a thin stick figure with a brown
   tunic sits hunched`. The `@` token carries the entire design. Your job is only the
   action, expression, posture, and position in frame.
   - Use the exact tokens from the cast table: correct spelling, ALL CAPS, always `@`
     prefixed.
   - **Never re-describe a cast member's head shape, clothing, color, build, hair, or face
     design.** That is what caused the drift this system exists to prevent. Expression and
     posture ARE allowed and required: `@YOU with flat resigned brows, shoulders dropped`.
   - **Never invent a token that is not in the cast table.** If a timestamp genuinely needs
     a new recurring character, stop, say which line needs it, and add it to the cast with
     its own reference sheet before continuing.
   - One-off background figures that appear in a single moment do not need a token. Write
     them as `three generic unnamed doodle stick figures`, and keep them small, faceless or
     minimal, and clearly secondary so they never compete with the cast.
   - **Every prompt that contains a cast member places the `@` token at the start of that
     character's clause**, so it is easy to see which sheets to attach when generating.
6. **Be specific about everything that is NOT the cast:** what the character is doing,
   their exact expression, what objects are in the scene, what background color is used,
   whether any on-screen text or labels appear.
7. **Translate abstract narration into concrete visuals.** See the examples in
   `visual-style.md`. Never render an abstraction as an abstraction.
8. **Match background color to tone** using the tone map in `visual-style.md`, and respect the
   background budget there. **Plain white is the default and must be the clear majority, 55 to
   75 percent of all prompts.** Cobalt blue is capped at 15 percent and means literally inside
   the mind, a brain or a thought loop as the subject. It does not mean night, sad, or serious.
   A 2am bedroom is modern everyday life and gets white. Labs and restaurants get white.
   - **Budget the warm backgrounds against the act sizes before writing a single prompt.** Count
     the cues in the script's other-era act. If that act is larger than the tan plus orange plus
     green ceiling, the surplus must be planned as white concept, number, and diagram frames from
     the start. Project 3's ancestral act was 83 of 266 cues, 31 percent, against a 25 percent
     warm ceiling, so about 20 of them were designed as white frames up front rather than
     discovered in review.
   - Also read the project's `character-prompts.md` colour notes for per-video constraints, for
     example a cast member whose garment colour matches a background colour, and add one grep per
     constraint to Step 3.
9. **On-screen text is black by default, red only for danger, threat, failure, or negation.**
   Never yellow on a white background, it is unreadable.
10. **Emotion lives in the eyebrows, mouth line, body posture, and head color**, never in
   background detail. Red equals embarrassed, angry, or overheated. White is neutral.
   Blue-tinted is sad, cold, or lonely. Keep every frame down to the fewest objects that
   carry the idea.
11. **Hold scenes across consecutive timestamps.** If 3 lines describe the same moment,
    keep the same scene, the same cast members, and the same background, and only adjust
    their expression or add one new element. **Do not generate a brand new scene every 5
    seconds.**
12. **Keep the cast internally logical.** `@YOU` carries the modern-life frames. The cast
    member from the script's other era or setting carries those frames. The two appear
    together only in a deliberate then-vs-now split frame. Do not swap who plays which
    role mid-video, and never place a character in an era their reference sheet was not
    drawn for.
13. **Use the nine proven frame types** from `visual-style.md` when appropriate rather than
    inventing a layout.

## Step 2 - Generate in internal chunks

**Write NO header. The file contains prompts and nothing else.** The first byte of the file is
the `[` of the first prompt. No title, no cast line, no source-transcript line, no attachment
note, no GENERATION LINE, no commentary anywhere. `image-prompts.md` is imported wholesale into
an image tool that treats every line as a prompt, so a header becomes a junk generation. The
cast list, cue counts, duplicate-timestamp note and GENERATION LINE all go in the **chat
report** at Step 4 instead, where the human reads them and the tool never sees them.

Work through the transcript in **internal chunks of 25 cues**, appending each chunk to the
file. Do not ask the user between chunks. Before each chunk after the first, re-read the
last 3 prompts you wrote so the scene-holding rule survives the chunk boundary, and re-check
the tone map so the background palette does not drift.

Chunking is not cosmetic. A single uninterrupted pass over 250 prompts degrades: scenes stop
holding, backgrounds drift toward white, and the last 50 prompts get shorter than the first
50. Chunk, re-anchor, continue.

## Step 3 - Verify mechanically

```bash
source .agents/bin/style-strings.sh   # exports STYLE_ANCHOR and STYLE_LOCK
F="$P/prompts/image-prompts.md"
T="$P/transcribes/transcript.md"

# one prompt per cue
echo "cues: $(grep -c . "$T")  prompts: $(grep -c '^\[' "$F")"

# PROMPTS ONLY: no header, no title, no commentary. Must be 0.
grep -v '^\[' "$F" | grep -c .
head -c1 "$F"   # must be [

# timestamps identical and in order
diff <(awk '{print $1}' "$T") <(grep -o '^\[[0-9:]*\]' "$F") && echo "timestamps match"

# anchor and lock on every prompt, compared against the one definition
echo "anchor: $(grep -cF "$STYLE_ANCHOR" "$F")  lock: $(grep -cF "$STYLE_LOCK" "$F")"

# no token outside the cast table
comm -13 <(grep -oE '@[A-Z]+' "$P"/prompts/character-prompts.md | sort -u) \
         <(grep -oE '@[A-Z]+' "$F" | sort -u)

grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"

# BACKGROUND BUDGET - white must be the clear majority, cobalt capped
N=$(grep -c '^\[' "$F")
S=0
for pat in 'plain white background' 'cobalt blue' 'tan #C4965A' 'orange #F5820D' 'grass green #3A9E3A'; do
  c=$(grep -ci "$pat" "$F"); S=$((S+c)); printf '  %-26s %3s  %2s%%\n' "$pat" "$c" "$((c*100/N))"
done
# the five counts must sum to N: anything else means a prompt has two backgrounds or none
echo "  sum $S of $N"
# text colour: black default, red for threat, yellow never
for col in black red yellow; do printf '  text %-7s %3s\n' "$col" "$(grep -c "bold $col ALL CAPS" "$F")"; done
grep '^\[' "$F" | grep 'plain white background' | grep -c 'bold yellow'   # must be 0
```

**FAIL the run and fix it if** white is under 55 percent, cobalt is over 15 percent, any
`solid blue` background appears, any yellow caption appears, or any yellow caption sits on a
white background. These are the exact faults that got project 2's first pass rejected.

Sourcing `.agents/bin/style-strings.sh` extracts the anchor and lock from
`.agents/rules/visual-style.md` at run time. Never hard-code them into a grep pattern here:
a hard-coded pattern can drift from the definition it is meant to be checking, which defeats
the purpose.

Prompt count must equal cue count. Anchor count and lock count must both equal prompt
count. The `comm` output must be empty except for `@[name]`, which is part of the style
lock. Fix anything that fails before reporting.

## Step 4 - Report and hand off

**The chat report carries everything the header used to.** Since the file is prompts only,
this is the only place the human gets it, so do not abbreviate it. Give the prompt count
against the cue count, the cast list with its `.jpeg` file names, any duplicate timestamps
with the file-naming workaround, the background budget table, and the first 3 prompts as a
sample. Then, quoting the GENERATION LINE from `visual-style.md` verbatim so the human can
copy it:

> Image prompts saved to `<path>`. The file is prompts only, so it imports directly.
>
> Paste them into Nano Banana, Gemini, Midjourney, DALL-E 3, or Stable Diffusion. For each
> prompt, attach only the `.jpeg` sheets for the `@` tokens it contains, and add this line to
> every generation: `<GENERATION LINE, verbatim>`
>
> **Pro tip:** generate the 3 or 4 frames where your main character is most visible first.
> If any drifts from the reference sheet, fix it before generating the rest. Drift
> compounds.
>
> Save each image to `scenes/` named by its timestamp, then run **`/check`**.

## Guardrails

- Never skip a timestamp. One timestamp equals one prompt.
- Never output prompts out of chronological order.
- Never wrap a prompt across two lines. Downstream tools split this file on newlines, so a
  wrapped prompt becomes two broken prompts.
- Never write a header, a title, a cast line, or any commentary into the file. Every line is
  either a prompt or one of the single blank separators between them. The file is imported
  wholesale, so a header line becomes a junk image.
- Never put a blank second line between prompts. Exactly one blank line separates them.
- Never re-describe a cast member. Never invent a token.

## Self-improvement

Read `.agents/skills/scenes/references/memory.md` at the start of every run. Append when a
prompt shape generates badly, when a scene-holding decision was wrong, or when the user
corrects a background choice.
