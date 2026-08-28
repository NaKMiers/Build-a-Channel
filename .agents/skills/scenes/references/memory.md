# scenes - memory

Self-improving notes for image prompts. Single canonical copy.

## 2026-08-03 - PastTense study and Project 1 V2 pilot

The approved A/B/C pilot is under `research/visual-style-pilot/project-1-hook/`. Direction B,
Warm Editorial Storybook Doodle, is the V2 target.

Measured on the same Project 1 hook composition:

| Surface        | Near-white area | Mean saturation |
| -------------- | --------------: | --------------: |
| V1 original    |    66.1 percent |           0.035 |
| A conservative |     3.1 percent |           0.133 |
| B recommended  |     0.1 percent |           0.309 |
| C aggressive   |     0.2 percent |           0.510 |

Learnings:

- Warm paper plus two or three depth planes improved perceived quality before any extra character
  detail was added.
- A pale negative-space corridor around Toss protected the focal point in a dense crowd scene.
- Story-specific props made the frame feel authored, but Direction C showed the ceiling: many
  lamps, plants, snacks, dark corners, and foreground heads competed with the narration.
- The recommended preview allowed generic crowd shirts to become saturated channel blue. V2
  prompts now reserve it for Toss or one semantic diagram signal.
- The preview generated more than forty countable people. Say `a crowd that reads as about forty`
  unless exact counting is the information task.
- Generated text survived this edit, but mission-critical spelling still belongs in CapCut when
  the image model is unreliable.
- Google Flow is the production renderer. The preview used OpenAI image generation because Flow
  was not connected, so five base and variant pairs must be smoke-tested in Flow before publish.

## Scale reference

Project 1: 255 transcript cues, 254 unique timestamps, 515 lines in
`prompts/image-prompts.md`. That is the size of a normal job.

## Project 2 (2026-07-28), 266 prompts, clean on every mechanical check

266 cues, 266 prompts, anchor and lock on all 266, timestamps an exact diff match, zero stray
tokens, zero adjacent-prompt errors, 537 lines.

**The chunking rule works and is now measured.** Eleven internal chunks of about 25, re-reading
the last few prompts at each boundary. Length drift between the first 50 and the last 50 prompts
was 2 percent (100 words versus 98). The memory previously only asserted that a single pass
degrades; this run gives a number to compare future runs against.

Cast distribution came out sensible without being planned: @YOU 110, @ANCESTOR 32, @BAND 24,
@KIN 21, @OTHER 18, @JURY 12. If @YOU ever drops below about a third of the prompts on a
psychology-first script, the visuals have probably drifted into diagram frames and away from the
viewer's inner life.

### Handling a script term that contradicts a cast rule

The script says the imaginary audience is "a vague jury with no faces at all". `@JURY`'s sheet
forbids faceless heads, because that phrasing produced giant blank ovals in the thumbnail round.
**A script's phrase describing a feeling is not a drawing instruction.** The anonymity was drawn
instead as one long row of figures, identical to each other, small and far back. Same meaning,
no banned pattern.

### A researcher cited but not depicted stays a diagram

The cast file ruled that Gluckman appears in narration only. His three cues became a
circles-and-web diagram of cross-cutting ties rather than a character, which kept the cast at six
and made the abstract point concrete at the same time. Prefer a diagram frame over inventing a
figure for a researcher the cast deliberately excluded.

### REJECTED: the first pass was 40 percent dark blue

The user rejected the entire first pass of project 2 as "dark and ugly". The numbers, against
the accepted project 1:

|                     | project 2 first pass | project 1 accepted |
| ------------------- | -------------------- | ------------------ |
| plain white         | 37 percent           | **58 percent**     |
| cobalt + solid blue | **40 percent**       | 18 percent         |

`visual-style.md` already said "White is the default" and I ignored it, because the script is
set at 2am and is emotionally heavy. **Cobalt blue is not a mood.** It means the frame is
literally showing the inside of someone's head: a doodle brain, a thought loop, a memory as an
object. Of 109 blue frames only 17 qualified. Bedrooms, the fridge, the meeting room, the
rehearsals and every laboratory were all just modern everyday life, which is white.

Two faults came with it:

- **35 lab frames used `solid blue`**, following old tone-map wording. The accepted fixture
  uses that background zero times. Labs are white with the apparatus drawn.
- **27 captions were yellow, 4 of them on white**, which is unreadable. The fixture uses black
  114 times and red 44 times and yellow **never**. Black is the default caption colour, red is
  reserved for danger, threat, failure and negation.

After the fix: white 72 percent, cobalt 5 percent, solid blue 0, yellow 0, black 53, red 28.

The budget and the caption rule are now written into `.agents/rules/visual-style.md`, prompt
rules 8 and 9 in SKILL.md, and the Step 3 verification block, which fails the run if white is
under 55 percent or cobalt over 15 percent. **Run that block before reporting, not after the
user looks at the images.**

## `image-prompts.md` IS PROMPTS ONLY. No header. (2026-07-29)

The user imports this file wholesale into an image tool that treats **every line as a prompt**,
so the 5 line header block was producing a junk generation from the title and cast line. It is
gone from project 3 and must never be written again: the first byte of the file is the `[` of
the first prompt.

What the header used to carry now goes in the **chat report** at Step 4, which is the only place
the human will see it, so that report cannot be abbreviated: the cast list with `.jpeg` names,
the prompt and cue counts, the duplicate-timestamp remap, the background budget, and the
GENERATION LINE quoted verbatim for copying.

Consequences worth remembering:

- **The duplicate remap is no longer documented anywhere in the file.** It does not need to be.
  The prompts carry the remapped stamp (`[8:26]` then `[8:27]`), which is what actually stops
  the overwrite. `check` now judges the diff arithmetically instead of looking for a note.
- **`visual-style.md`'s GENERATION LINE heading was reworded** from "printed in every prompt
  file header" to "the instruction the human adds to every generation", because it is no longer
  in this file. That heading string is hardcoded in `.agents/bin/style-strings.sh`, so the two
  had to be edited together. **Any future rewording of one of the four string headings must
  change `style-strings.sh` in the same commit**, or the variable extracts empty and silently
  disables the anchor and lock checks everywhere. The line still lives legitimately in
  `character-prompts.md` and `thumbnail-prompts.md` headers, which are read by humans only.
- Audited 2026-07-29: **project 1 and project 4 still carry a 4 line header, project 2 does
  not.** Project 1 is the regression fixture and stays. **Project 4 is a finished video whose
  prompts would import with a junk first record**, so strip it before importing:
  `tail -n +7 <file> > <file>.new && mv <file>.new <file>`, then re-check the prompt count.
  I did not touch project 4 in this run because only project 3 was in scope.

## Project 3 (2026-07-29), 266 prompts, clean on every mechanical check

266 cues, 266 prompts, anchor and lock on all 266, timestamps an exact diff match apart from
the one documented `[8:26]` to `[8:27]` remap, zero stray tokens, zero adjacent-prompt errors,
537 lines. Eleven internal chunks of 25 with a re-anchor at each boundary. Length drift between
the first 50 and the last 50 prompts was 4.5 percent (116 words versus 110), against project
2's 2 percent. Still small, but the trend is worth watching: re-read more than the last 3
prompts at a boundary if it grows again.

Backgrounds landed at white 72 percent, tan 12, cobalt 6, orange 6, green 1. The five counts
sum to exactly 266, which is a useful invariant: **if the background greps do not sum to the
prompt count, some prompt has either two background phrases or none.** Add that check.

Captions: black 153, red 63, yellow 0.

### Budget the warm backgrounds against the act sizes BEFORE writing

This script's anthropology act is 83 of 266 cues, 31 percent. Painting all of it tan or orange
would have blown both ceilings at once (tan 15, orange 10). The fix was decided up front, not
in review: about 20 of those 83 cues became white concept frames instead, the number frames
(150, 30), Boehm's ladder as a diagram, the crossed-out police badge and gavel, the balance
scales, the reputation-system machine. **Compute the warm-background ceiling against the
ancestral act's cue count before writing the act.** If the act is larger than the ceiling, the
surplus has to be planned as white concept frames from the start.

### @YOU's share is bounded by rule 12, so judge it against eligible cues

@YOU appears in 89 of 266 prompts, 33 percent, right at the floor the note below warns about.
It is not drift here: rule 12 forbids him from the 83-cue ancestral act, so he is eligible in
183 cues and appears in 48 percent of those. **Measure @YOU against the cues where he is
allowed, not against the whole file.** Cast distribution for the record: @YOU 89, @CAMP 49,
@WORK 34, @FORAGER 33, @GYM 24, @METER 19.

### A personified-object cast member earns its slot in the callbacks

@METER (Leary's sociometer) was cast because it recurs across the whole video rather than one
section. It came out at 19 prompts spread over three acts, including the cobalt interior frames
where it is the subject. Those late callbacks at `[9:13]` through `[9:31]` are the payoff: a
locked gauge design reappearing 8 minutes after its introduction is exactly what a reference
sheet is for. An object token also solves the cobalt frames neatly, since a cast object can sit
on a cobalt ground while the surrounding doodles stay white.

### Verify the costume constraint the cast file wrote down

Project 3's cast put @YOU in an orange shirt, and orange is also the fire background, so the
cast file recorded that @YOU must never be framed on a warm ground. That is a `scenes`
obligation, not a `cast` one, and it needs its own grep:
`grep '^\[' "$F" | grep 'orange #F5820D' | grep -c '@YOU'` must be 0. **Read the cast file's
colour notes for constraints like this before writing, and add a grep for each one.**

## Lessons

- Generate in internal chunks of about 25 and re-anchor between them. A single uninterrupted
  pass over 250 prompts degrades in three measurable ways: scenes stop holding across
  consecutive cues, the background mix drifts away from the budget, and the last 50 prompts
  come out noticeably shorter than the first 50. Measure all three, do not eyeball them.
  (This line previously said backgrounds "drift toward plain white" and treated that as the
  failure. It is backwards: white is the target and drifting toward a dark ground is the
  failure. Corrected after the project 2 rejection.)
- The scene-holding rule is the one most often broken at a chunk boundary. Re-read the last 3
  prompts written before starting the next chunk.
- Project 1's prompts say "mitten hands", which is now wrong per
  `.agents/rules/mascot-toss.md`. Do not copy that phrasing forward. Use small splayed line
  fingers, or simply do not describe the hands at all, since the `@` token carries the design.

## Project 6 (2026-08-03), the first V2 job: 303 prompts, 345 plan beats, 113 chain breaks

Clean on every mechanical check: 303 cues to 303 prompts, V2 anchor and lock on all 303 and zero V1
strings, timestamps an exact diff match, zero stray tokens, zero non-prompt lines, 831 lines, plan
tier counts equal to prompt tier counts exactly, surface phrases summing to 303 with exactly one per
prompt. Thirteen internal chunks of 25.

Final budgets: cream 28.3, tinted 21.4, story environment 35.6, cobalt 7.9, pure white 6.6 percent.
Tiers CLEAN 44.2, LAYERED 51.2, ATMOSPHERIC 4.6. Assets over all 345 beats: PLATE 40.0, VARIANT
40.0, CALLBACK 7.8, CAPCUT 12.2 percent. 138 plates, motif on 20 beats, text on 101 (33.3 percent).

### Write visual-plan.md FIRST and completely, then verify it, then write prose

The plan is what makes the tier and surface greps checkable, and it is far cheaper to rebalance a
345 row table than 303 paragraphs. This run rebalanced twice before any prose existed: registers
first (PORTRAIT was 1 percent and HYBRID 24 percent on the first pass), then tiers. Both fixes were
a python pass over the table, seconds each. The same corrections after writing the prose would have
meant rewriting a hundred prompts.

### The four V2 budgets that a first pass gets wrong, and the shape of each error

1. **Surface**: the first pass came in with cream at 15.8 percent against a 30 percent target and
   tinted at 33.9 percent against 20. Cause: every card and diagram reached for a chapter tint
   because chapter colour felt like the V2 signature. Fix was moving 38 neutral editorial cards to
   cream, **as whole plate chains, never single beats.** A plate whose variants name a different
   surface than the plate is a contradiction the renderer resolves badly. Verify with a
   plate-to-surface grouping, not just a total: `plates with mixed surfaces` must be empty.
2. **Text**: 46.5 percent of prompts carried on-screen text against a 25 to 35 target. Dropping 40
   text clauses whose only job was to name what the drawing already showed landed it at 33.3.
   Keep text for verdicts, negations, numbers, and researcher names; cut it where it labels.
3. **Tier**: two prompts were written ATMOSPHERIC while the plan said LAYERED, because they were
   variants of an atmospheric plate and inherited its light. The plan was wrong, not the prompts.
   **When plan and prompt disagree on tier, ask which one the composition justifies** rather than
   defaulting to the plan.
4. **Shot grammar**: 6 of 24 thirty-second blocks carried only two or three distinct shot tasks.
   Fixed by re-shotting 10 beats. The final block is 5 seconds long and holds 3 beats, so it cannot
   carry four tasks; that is an arithmetic limit, not a defect. Check the blocks, then read the
   exceptions before "fixing" them.

### One prompt silently lost its surface phrase

`[3:10]` was written as a variant whose scene clause named the camera and the objects but not the
surface, so the surface greps summed to 302 of 303. A per-prompt count of surface phrases catches
this; a total does not, because one prompt with two phrases and one with none also sums to 303.
Both faults are in the check now.

### Breaks: 113 of them, and the callback rule that shapes where they cannot go

Prompt rule 16 says a break may only open a `PLATE`. Four act boundaries in this script open on a
`CALLBACK` instead (`[1:28]`, `[2:18]`, `[2:46]`, `[11:21]`), so no break is legal there and the
callback inherits the previous act's frame. The fix is not to bend the rule: write the callback's
scene clause to restate the surface and composition explicitly ("the illustrated story environment
of the couch scene returns, the same medium camera"), and where the act genuinely must not inherit,
**move the break to the next PLATE a beat or two later.** The one place that was worth restructuring
is the ending: `[11:33]` was planned as a callback to the hook plate and became a PLATE with
`Motif: CALLBACK` instead, so the hook echo could get its own break and a clean chain.

### Registers cannot always hit their bands, and that is a script fact

Final registers: STORY 26.4, CARD 17.8, DIAGRAM 20.8, PORTRAIT 9.9, HYBRID 14.5, SPLIT_OR_SCALE
10.6 percent. STORY is 3.6 points under its band and DIAGRAM 0.8 over. This script carries the MAC
model, an eleven-study experiment, the Hadza measurements, and an edges-versus-no-edges contrast, so
its natural centre is diagrams and cards, not scenes. Nine camp beats that had been planned as
DIAGRAM were rewritten as STORY scenes because a forager watching a trail fade is a scene and not a
flowchart, which is the right kind of conversion. Inventing 15 more scenes to reach 30 percent would
have been the wrong kind. **Report the deviation with the reason instead of padding.**

### @YOU's share, measured against eligible cues again

@YOU 78, @FORAGER 30, @PHONE 10, @HADZA 6. That is 26 percent of all prompts, which looks like the
drift project 3's note warns about, but rule 12 bars Toss from the camp act, the Hadza act, and the
experiment room, about 89 cues. Against the 214 cues where he is eligible he is at 36 percent.

## Project 8 (2026-08-12), the Diderot effect: 268 prompts, 309 plan beats, 104 breaks

Clean on all 21 mechanical checks on the first assembly pass. 268 cues to 268 prompts, V2 anchor
and lock on all 268 with zero V1 strings, timestamps an exact diff match, zero stray tokens, zero
non-prompt lines, zero adjacent pairs without a blank line, 743 lines, 131 plates, tier counts
equal to plan exactly, surfaces summing to 268 with exactly one phrase per prompt, zero
mixed-surface plates, every break opening a PLATE.

Final budgets. Registers STORY 31.0, DIAGRAM 19.4, CARD 17.5, HYBRID 12.3, PORTRAIT 10.4,
SPLIT_OR_SCALE 9.3, **all six inside their bands, the first time that has happened.** Surfaces
story 35.8, cream 26.1, tinted 24.6, white 7.5, cobalt 6.0. Assets over 309 beats PLATE 42.4,
VARIANT 37.2, CAPCUT 13.3, CALLBACK 7.1. Text 27.6 percent. Cadence 31.7 beats per minute.
Length drift first-50 to last-50 was 5.2 percent.

### THE DEFECT WORTH REMEMBERING: variants that never name their own cast

First assembly passed every mechanical check while `@YOU` sat on **22 of 268 prompts, 8 percent**.
Cause: variants and callbacks were written as "Preserve the attached source plate ... the single
delta is X", which describes only the change, so the character standing in the frame is never
named. Nothing in the Step 3 block catches this. It is invisible to prompt count, timestamps,
anchor and lock counts, surface counts, and the prompts-only grep.

It matters for two independent reasons. Flow binds reference sheets **per prompt**, so a variant
that omits `@YOU` gives the model no sheet for the character it is supposed to preserve. And the
cast-distribution note below reads as catastrophic drift when it is really a prose omission.

**Fix: propagate every plate's tokens to its variants and callbacks automatically.** Build a
`plate_key -> tokens` map from each plate's originating prose, then emit
"`@TOKEN` stays in the frame in the same position and posture as the source plate, unchanged in
design" inside the preserve clause. That took `@YOU` from 22 to 44 and token-carrying prompts from
79 to 110 without touching a single scene description.

Add this to the check block:

```bash
grep -c '@[A-Z]' "$F"     # prompts carrying at least one token; compare against plate coverage
```

### Then measure @YOU against eligible cues, and fix the real gap separately

44 of 268 is 16 percent, but rule 12 bars Toss from the 33-cue Diderot act and the 56-cue Kalahari
act, so he is eligible in 179. 44 there is 24.6 percent, still under project 6's 36. Listing the
modern-act plates with no `@YOU` showed 33 of 45, and ten of them were frames a second-person
script genuinely puts the viewer inside: the coherence ring, the dining table, the kitchen counter,
his own hands at the till, the absorbed set, the row of ordinary weeks, the four dimmed objects,
the two visible prices, the unseen bill. Adding him to those ten plates propagated through their
variants and landed 64 of 179, **35.8 percent, matching project 6.** The other 23 stayed
characterless because they are cards, diagrams, or the Diderot returns, and padding them would
have been the wrong conversion.

### 21 planned breaks opened a CALLBACK, and relocation is mechanical

Rule 16 allows a break only before a PLATE. The first pass had 21 illegal ones. Rather than
hand-resolving each, a script dropped every illegal break and moved the cut to the next PLATE
within four cues, which relocated 5 and dropped 16 as genuinely unnecessary. Breaks went 120 to
104. Then a lineage scan found **22 callbacks whose source is severed by an intervening break and
zero variants severed**, which is the correct shape: variants must inherit, callbacks can be
rebuilt in prose. Those 22 are emitted as "the earlier P0NN composition returns on the same
`<surface>`, rebuilt in full", which is project 6's prescribed fix applied by construction rather
than by hand.

The ending was the one worth restructuring instead. `[9:38]` and `[9:41]` originally pointed back
to the hook plate `P001` across 100 breaks. Same fix as project 6: they became variants of a new
ending plate carrying `Motif: CALLBACK`, so the hook echo gets a clean chain.

### `style-strings.sh` resolves its rules file relative to cwd

Sourcing it from a scratch directory silently yields empty strings, and an empty anchor makes
every `grep -cF` return the line count rather than failing. The assembler asserts
`len(ANCHOR)==163 and len(LOCK)==346` before writing anything, which caught it immediately.
**Assert the lengths, never just that the variables are set.**

### One recurring glyph carried both halves of the script

The motif is a horizontal charcoal reference line. The psychology act is a line that lifts and
quiets everything beneath it; the anthropology act is the same line held down by hand so nobody
rises above the camp. Because the script's two halves are literally the same shape, one glyph
covers 78 beats and the mismatch act is drawn simply by removing the hand. **When a script
contrasts two systems, look for the drawing they share before inventing two.**

## Project 9 (2026-08-21), advice you never take: 273 prompts, 284 plan beats, 78 breaks

Clean on every mechanical check after fixes: 273 cues to 273 prompts, V2 anchor and lock on all
273 with zero V1, timestamps an exact diff match with no duplicates, zero stray tokens, zero
non-prompt lines, zero adjacent pairs without a blank line, surfaces summing to 273 with exactly
one phrase per prompt, tier plan equal to prompt tier exactly (114 CLEAN / 154 LAYERED / 5
ATMOSPHERIC), every source pointing backward, every break opening a PLATE, no em dash. 83 plates.
Built data-first with the generator script (all beats as python data, verbatim strings
substituted, breaks inserted by flag, sources computed as previous-beat-of-plate), same method
as projects 5 and 7.

Motif: a windowpane of glass separating the calm view from outside from the flooded view when
you are trapped inside. It carries the whole script, appearing in the study/distance act, the
anthropology act (the camp wall drawn as a window), and the ending payoff (looking back at your
own life through the same glass). One glyph, both halves, exactly the shape project 8's note
recommends looking for.

Final budgets. Tiers CLEAN 41.8, LAYERED 56.4, ATMOSPHERIC 1.8 percent. Surfaces story 44.3,
cream 32.2, tinted 12.8, cobalt 5.5, white 5.1. Registers STORY 38.5, CARD 20.5,
SPLIT_OR_SCALE 14.7, PORTRAIT 13.9, HYBRID 6.2, DIAGRAM 6.2. Assets over 284 beats PLATE 29.2,
VARIANT 66.9, CAPCUT 3.9, CALLBACK 0. Text 28.6 percent. Cadence 28.1 beats per minute. Cast
@YOU 111, @CAMP 32, @SOLOMON 11, @FRIEND 7; tokens on 154 of 273 prompts. @YOU is 41 percent of
all prompts and 61 percent of the 181 cues where rule 12 allows him (barred from the Solomon
and Kalahari acts).

### NEW TRAP: a plate's `tokens` field does not put the token in the plate's prose

The generator stored `tokens=[CA]` on a plate but its composition prose said "the ring" or "the
band" or "one camp figure" and never wrote `@CAMP`. The token-clause builder still injected
`@CAMP stays in the frame...` into every VARIANT of that plate, so 11 variants named a character
their own base plate never contained. This is project 8's "variant names a token its source
lacks" defect with a new cause: not a terse variant, but a plate whose prose describes the cast
in words instead of by token. **A plate must write the `@TOKEN` into its own composition prose,
not merely carry it in a data field.** Audit: for every VARIANT, its tokens must be a subset of
its PLATE's prose tokens, unless the delta text itself introduces the new one (the deliberate
"@FRIEND appears in the call bubble" case is fine because the delta names @FRIEND). Two beats
also placed @CAMP on another character's card (@YOU's counselor card, Lee's notebook card); the
ring got its own PLATE and Lee's camp became generic untokenised sketch figures.

### The on-screen-text budget needs a keeper allowlist, not per-beat judgement

First assembly carried text on 163 of 273 beats, 60 percent, against the 25 to 35 target, because
almost every card and label beat got a caption. The fix was a `KEEP_TEXT` allowlist of ~80
timestamps limited to verdicts, numbers, researcher and concept names, and the shift's key
instruction words, with a one-line guard in the beat builders that nulls text off any beat not in
the set. Landed at 28.6 percent. **Decide the keeper set as a list up front rather than judging
"does this beat need text" 273 times; the second method always drifts high.**

### A CapCut beat sharing a break-opening plate's timestamp trips the break-opens-PLATE check

The Step 3 break check maps `asset` by timestamp, last row wins. A CapCut beat given the same
`[M:SS]` as the PLATE a break precedes overwrites the plate's asset in that map, so the check
reports "break opens CAPCUT" even though the break correctly precedes the plate's prompt (CapCut
makes no prompt). Nine such collisions appeared. **Never give a CapCut beat the same timestamp as
a break-opening PLATE.** Either retime the CapCut to the previous cue or drop it. Dropped all
nine here, which left cadence at 28.1 per minute, still in band.

### Honest deviations, reported not padded

- Surfaces story 44 vs 35 target, tinted 13 vs 20: the script's spine is sustained scenes (the
  hook bedroom, the Kalahari camp, the mismatch room, the ending), same shape as project 7's 46.
- Registers SPLIT_OR_SCALE 14.7 over its 5 to 10 band, DIAGRAM and HYBRID both 6.2 under theirs:
  the script is built on self-versus-other and modern-versus-ancestral contrasts, which are
  splits and scales, and its mechanism is a single vantage flip rather than a multi-node
  flowchart, so there is little to diagram. Same class of script-driven skew as projects 5 to 7.
- Assets VARIANT 67 high, PLATE 29 low, CAPCUT 3.9 low, CALLBACK 0: deliberate. The window and
  the camp ring are long continuous metaphor scenes, so composition-preserving variants carry
  them, which also minimises character drift. The only reprise is the ending, handled as two
  PLATEs with Motif CALLBACK per the project 8 pattern so the hook echo gets a clean chain.

## Project 10 (2026-08-25), third vs second: 304 prompts, 348 plan beats, 89 breaks

Clean on every mechanical check. 304 cues to 304 prompts, V2 anchor and lock on all 304 with zero
V1 strings, timestamps an exact diff apart from the two documented remaps, zero stray tokens, zero
non-prompt lines, zero adjacent pairs without a blank line, 785 lines, 119 plates, tier counts equal
to plan exactly (117 CLEAN / 177 LAYERED / 10 ATMOSPHERIC), surfaces summing to 304 with exactly one
phrase per prompt, zero mixed-surface plates, every break opening a PLATE, no em dash. Built
data-first with the generator method: plan rows as python data, budgets rebalanced as data, 119
plate compositions written as prose, variants and callbacks derived mechanically.

Motif: **the near span**, a short charcoal measuring bracket between two marks. The script contrasts
an ancestral system against a modern one, so per the project 8 rule I looked for the drawing they
share instead of inventing two. The ancestral half is a short span the camp's hands push closed; the
modern half is the same span with a lavender phantom on the far end and an endless supply of them.
One glyph covers 198 of 304 beats and carries the podium, the airport, the band, the camp, the feed
and the ending.

Final budgets. Registers STORY 33.6, CARD 19.1, DIAGRAM 18.4, HYBRID 12.2, PORTRAIT 11.2,
SPLIT_OR_SCALE 5.6, **all six inside their bands**, second time that has happened after project 8.
Surfaces story 39.5, cream 27.6, tinted 16.4, white 10.9, cobalt 5.6, all inside the 5-point
tolerance. Tiers CLEAN 38.5, LAYERED 58.2, ATMOSPHERIC 3.3. Assets over 348 beats VARIANT 50.0,
PLATE 34.2, CAPCUT 12.6, CALLBACK 3.2. Text 29.9 percent. Cadence 30.4 beats per minute. Length
drift first-50 to last-50 was 7.0 percent, but the two ends differ by register (dense story plates
at the hook, terse card variants at the outro), so compare like for like before reading it as decay.

### Writing 119 plate compositions is the whole job; variants are then free

The 304 prompts cost 119 pieces of prose, not 304. Every VARIANT is generated as
"preserve the attached source plate, keeping the same `<verbatim surface phrase>`, the same camera
axis, cast placement, environment geometry, object positions, palette and line hierarchy" plus the
propagated token clauses plus one named delta. Every CALLBACK is emitted with its plate prose
rebuilt in full, which is project 8's prescribed fix applied by construction rather than by hand, so
a severed lineage cannot happen. **The verbatim surface phrase goes into the variant string at
generation time**, which is project 5's 157-variant repair avoided entirely.

### The project 9 token trap fired again, and the subset check caught it

Two plates carried `@YOU` in their token data while their own composition prose never wrote the
token: P034, the two identical scene boxes for the travellers, and P108, the four-second timing
diagram. The token-clause builder then injected "@YOU stays in the frame..." into their variants,
naming a character the base plate never contained. The audit that catches it is one line and should
run before every assembly:

    for every non-PLATE beat, plate_tokens[plate] must be a subset of the @TOKENs
    found by regex in that plate's own prose string

Both were fixed by putting the figure into the plate composition rather than by deleting the token,
because in both cases the viewer genuinely belongs in the frame. **A plate whose meaning includes a
character must draw that character, not merely declare it.**

### Chapter tint is named in the plate prose, the surface phrase stays verbatim

Three chapter colours means three different tinted cards, but the grep needs the exact string
`light tinted chapter card`. The working shape is to emit the verbatim phrase in the surface slot and
let the plate prose say "on the tinted lavender card" or "on the tinted tan card" as ordinary
description. Both the check and the renderer get what they need.

### One grammar slip that only a read catches

The surface slot was emitted as "a `<surface phrase>`", which produced "a illustrated story
environment" on 120 prompts. Every mechanical check passed: the phrase was present, the count was
one per prompt, the sum was 304. **Read one prompt of each asset type end to end before reporting.**
Fixed with a single sed, and the surface counts were re-verified afterwards because a sed inside the
phrase would have broken them.

## Project 5 rebuilt as V2 (2026-08-04), 293 prompts, 340 plan beats, 41 chain breaks

The numbered folder changed identity: the old project 5 was deleted and
`5-why-do-people-follow-the-crowd` replaced it with a cast file that states
`Visual style version: V2`. The SKILL's "projects 1 through 5 are frozen V1" line lost to its own
more specific rule: an existing artifact that explicitly identifies a version wins when redoing one
stage. **Check the cast file's version line before assuming the project number decides the
version.**

Clean on every mechanical check after two scripted passes: 293 cues to 293 prompts with one
documented `[5:15]` to `[5:16]` remap, V2 anchor and lock on all 293 and zero V1 strings, tier
counts equal plan exactly, surfaces summing 293 with one per prompt, zero mixed-surface plates,
zero stray tokens, 667 lines.

### The variant surface-phrase fault happens at scale, not once

Project 6 lost one surface phrase; this run lost 157, every variant written as "Preserve the
attached source plate of the cream card" style shorthand. The per-prompt surface count caught all
of them and one mechanical pass inserted `keeping the same <verbatim surface phrase>` before each
`the single delta is` clause. **Write the verbatim surface phrase into every variant while
drafting**, or plan on the repair pass.

### Placeholder assembly guarantees the verbatim strings

Prompts were drafted in 12 chunk files with `{{A}}`/`{{L}}` placeholders and joined by a script
that substitutes the strings sourced from `.agents/bin/style-strings.sh` and inserts the break
lines from a checked list. Byte-identical anchor and lock on all 293 by construction, and the
break placement was validated against the plan (every break opens a PLATE) before the file
existed. Same trick for the plan: write generated-only rows 1:1 with cues so beat number equals
cue number, then a script inserts the CAPCUT rows, renumbers, and remaps Source references.
Hand-numbering 340 rows with interleaved capcut beats is where the errors would have lived.

### Budgets: the same four first-pass errors as project 6, plus two honest deviations

First pass: CARD 26 and DIAGRAM 30 percent against 15 to 20 bands, PORTRAIT 6 and HYBRID 3 against
10 to 15, CLEAN 54 against 40. One scripted register-and-tier pass fixed most of it. Final:
STORY 27.3, CARD 23.9, DIAGRAM 22.2, PORTRAIT 9.6, HYBRID 10.2, SPLIT 6.8. STORY sits under its
band and CARD/DIAGRAM over because the script's spine is Asch numbers, fMRI regions, and cascade
mechanics; inventing scenes to pad STORY would be the wrong conversion. Callbacks landed at 8 rows,
2.4 percent of beats, under the 5 to 10 band, but 8 of 113 plates is 7 percent, inside the
cadence rule's "reuse 5 to 8 percent of plates near the ending". The callbacks concentrate in five
reprises (dial, case file, lab row, rule tablet, theater) whose follow-on beats are variants of
the reprised plate; relabeling those variants as callbacks would fake the band.

### Characters are .png, format says .jpeg

`characters/` holds `YOU.png` and friends. `file-formats.md` says sheets are `.jpeg`. Flagged in
the report rather than silently renamed; binding works either way in Flow, `/check` will complain.

## Project 7 hook rebuilt (2026-08-07), and the import bug that was hiding in the whole file

The user rejected `[0:00]` to `[0:35]` as duplicated, off-transcript, and not attractive for a
hook. Only that range was rebuilt. What the range looked like before is worth recording as a
failure signature, because the same signature runs through the rest of project 7's file:

- **21 consecutive cues on one plate** with `Delta: expression change` on all 20 variants, and
  only 6 distinct prompt bodies across the 21, so seven cues in a row generated the identical
  image. A delta that says "expression change" and nothing else is not a delta. If the plan's
  Delta column repeats one phrase down a whole act, the prose above it has already collapsed.
- **Every one of the 297 plan rows said `medium`**, and the register column held zero
  `PORTRAIT` and zero `SPLIT_OR_SCALE`. The shot-grammar rule (four of seven tasks per 30
  second block) is the check that catches this, and it was never run.
- **The tier string was written `LAYERED render tier,` with a comma**, so
  `grep -c "$tier render tier:"` returned 0 on all 297 and the tier check silently passed as
  "nothing to compare". Rule 14 says colon. Grep for the colon form, and treat a zero count as
  a failure rather than an absence.
- **`Source` held plate IDs (`P002`), not beat IDs.** The Step 3 awk resolves Source against
  `seen[beat]`, so every non-plate row in the untouched part of the file reports `bad source`.
  `file-formats.md`'s own example is `| VARIANT | P001 | B001 |`: Plate is a plate ID, Source is
  a beat ID. They are different columns and different namespaces.

### The file had no blank lines between prompts, so it would have imported as 26 records

271 of the 296 adjacent prompt pairs had no blank line between them. Only the 25 `---` breaks
carried blank lines. Google Flow splits the pasted text on blank lines, so CREATE would have
read **26 images, not 297**, and every one of them would have been a 10-prompt run-on. This is
invisible to the prompt count, the timestamp diff, the anchor and lock counts, and the
prompts-only grep. All five passed. Add the adjacent-pair check to every run:

```bash
awk 'p ~ /^\[/ && $0 ~ /^\[/ {c++} {p=$0} END{print c+0}' "$F"   # must be 0
```

The repair is mechanical and safe: keep only non-blank lines, then rejoin with `\n\n`.

### Rebuilding one range without renumbering the plan

The hook needed 8 plates where the old plan had 1, and plate IDs `P001` to `P026` were already
taken by later beats. Renumbering the whole file to make the hook's plates sequential would
have rewritten 276 rows the user did not ask about. **Plate IDs only have to be unique, not
sequential**, so the new plates took `P001` plus `P027` to `P033`. Nothing outside `[0:00]` to
`[0:35]` moved.

Same reasoning killed the CapCut rows. The hook's 21 cues over 35 seconds is 36 beats per
minute against the 45 to 60 the cadence rule wants for the first 15 seconds, and the honest fix
is CapCut-only beats. But inserting them renumbers every beat after B021, and the plan carries
zero CAPCUT rows over all 297 rows anyway, so adding them to the hook alone would have been
inconsistent with the rest of the file. Reported as a deviation instead. The three build chains
were written so CapCut can subdivide them (advisors filling chairs one at a time, the
MOMENT/FORCE/AUDIENCE diagram build, the balance tipping inside the thought bubble) without any
new generation.

### Rule 12 forces a split frame, and the split is the better hook anyway

`[0:14]` "They needed you to get angry" wants @YOU and the ancestors in one frame, which rule 12
forbids outside a deliberate then-versus-now split. Writing it as an actual split frame, tan
ground and @BAND around the fire on the left, cream modern room and a red-headed @YOU on the
right, is stronger than the "faint ancestral silhouette" the old pass used, and it is the only
`SPLIT_OR_SCALE` beat the plan had anywhere.

### The three advisors stay untokenised

The therapist, the boss and the mother appear across five beats of one plate chain and nowhere
else in the video, so they are unnamed scene figures, not cast. To keep them from drifting they
are seen from behind in the wide shots, and the one close-up on the mother crops her to a
shoulder and a pointing hand with no face. A recurring-looking figure that never recurs does
not need a sheet; it needs a composition that never asks for one.

## Project 7, ranges two and three (2026-08-07): the mechanism act, then a simplicity correction

`[0:38]` to `[1:59]`, 37 cues, and `[2:03]` to `[2:22]`, 9 cues. Same collapse as the hook:
37 cues on 2 plates, 9 on 1, `Delta: expression change` on every variant. Rebuilt to 67 beats
across 25 plates total for `[0:00]` to `[2:22]`.

### Give a mechanism act one physical object and let it recur

The recalibrational theory is a welfare tradeoff ratio, which is a comparison, which is a
**two-pan balance**. Introducing it in the hook as a thought bubble at `[0:28]`, formalising it
at `[0:59]` as the diagram @YOU stands beside, clamping its beam at `[1:41]` for "hold your
welfare hostage", levelling it at `[1:53]` for "the negotiation ending", and reducing it to the
one thing under the line at `[2:20]` for "the underlying mechanism does not vary" costs five
plates and carries the entire act. The old pass spent those same 46 cues on the phrase "a
simple diagram of the negotiation model" and drew nothing. **Pick the object the mechanism
already is, plant it early, and pay it off.** Abstract acts do not need abstract frames, they
need one prop that survives the whole act.

### The user's word for the old frames was "complex", and the cause was on-screen prose

`[2:03]` to `[2:22]` was rejected as too complex to absorb in a couple of seconds. Every frame
carried a full sentence of generated lettering: "bold charcoal text reading recalibrational
theory of anger", "bold charcoal text reading the negotiation signal underneath". Those are 4
to 6 words the viewer has to read while the narration is already moving, and the image model
renders long strings unreliably anyway. The rebuild caps the whole range at three single words,
`EVERYWHERE`, `VARY`, `SAME`, and moves the meaning into the drawing.

**Density lives in the count of marks, not the count of ideas.** `[2:06]` is two figures and one
block on an empty card. The next three beats add one thing each: three smaller identical pairs,
a check beside each, a bracket under the group. Nothing is ever removed and nothing is ever
redrawn. A viewer who read frame one can read frame four at a glance, which is the actual
definition of absorbable. The text budget rule already says 1 to 5 words; treat 1 to 2 as the
default and 5 as the exception.

### The above-the-line / below-the-line card

"The specific rules vary widely, but the mechanism underneath does not" is one composition, not
six: a horizontal line, variable shapes above it, one invariant object below it. Build it in
four beats (tablets clustered, tablets spread apart under a double arrow, the balance appears
below, a bracket closes with `SAME`) and the sentence draws itself. Worth reaching for any time
the script contrasts a varying surface with a constant underneath.

### Splicing a range: the boundary break is part of the slice

Replacing records `i` through `j-1` silently swallowed the `---` that sat immediately before the
untouched `[2:26]`, because that break was the last record of the removed slice. The break count
still moved in the right direction (42 to 43) so nothing looked wrong. **After any splice, print
the two records on each side of both seams and look at them**, or the chain quietly re-wires a
hard cut. Check the seam before the first new record and after the last one, both.

### Registers land naturally when the plan is written per-cue

Across the 67 rebuilt beats: CARD 17, STORY 16, DIAGRAM 14, HYBRID 9, SPLIT_OR_SCALE 8,
PORTRAIT 3. Assets 25 plates to 42 variants, 37 percent plates, inside the 35 to 45 band without
a rebalancing pass. Shot tasks reached 4 to 7 per 30 second block in every block. Projects 5 and
6 both needed a scripted rebalance after the first pass; the difference here is that every row
was written against its own transcript cue instead of an act label repeated down a column. A
Meaning column that repeats one phrase for 37 rows is the tell that no per-cue planning happened.

## Project 7 full rebuild (2026-08-07): 297 prompts, 297 plan rows, 106 plates, 95 breaks

The user committed `remove scenes project 7` (deleting image-prompts.md, visual-plan.md, and
all scene images) and asked for a from-scratch rebuild with three constraints: best-ever hook,
no duplication, simple absorbable frames that still describe the transcript perfectly. The four
ranges already rebuilt and accepted this session were kept verbatim as the spine ([0:00]-[0:35],
[0:38]-[1:59], [2:03]-[2:22], [2:59]-[3:08]); the other 226 cues were designed fresh. Clean on
every mechanical check on the first assembly pass.

### From-scratch at this scale is a data problem, not a prose problem

The order that worked: (1) write all 226 plan rows as python data with per-cue meanings copied
against the transcript, (2) machine-verify the row timestamps equal the transcript exactly and
tally registers, tiers, assets before any prose exists, (3) write prose chunk files of about 25
cues with {{A}}/{{L}} placeholders and inline `---` breaks, (4) assemble with a script that
substitutes the sourced verbatim strings and asserts prompt count, timestamp diff, break shape.
Variant Source columns computed as previous-beat-of-same-plate by the generator, which makes
the source-points-backward check pass by construction. Zero of the four classic first-pass V2
budget errors survived to the prompt file because the plan was rebalanced as data first.

### Visual language reuse is what kills duplication at scale

The rebuild leaned on a small set of recurring devices, each introduced once and then quoted:
the two-pan balance (worth), the orange arc/ring (the signal), identical thought bubbles over
every watcher (shared updating), tiny up/down arrows in witness bubbles (credibility updates),
the orange body-fill (the flood), the red X (negation), check-mark trails (track record).
Because each device has one meaning, a new cue can be drawn as a one-delta variation of a known
composition instead of a brand-new invention, which is simultaneously simpler for the viewer
and immune to the copy-paste duplication the old file died of. Rule of thumb: if a script idea
recurs, give it a glyph; if a glyph exists, never invent a second drawing for the same idea.

### Honest deviations, reported not padded

- Text beats 47 of 297, 16 percent, versus the 25 to 35 band: deliberate, the user asked for
  low reading load; single words only, red reserved for negation and verdicts.
- STORY 29 / CARD 24 / DIAGRAM 22 / PORTRAIT 7 / HYBRID 5 percent: evidence-heavy script, same
  shape and same justification as projects 5 and 6.
- Surfaces: story environments 46 percent versus 35 target, cream 20 versus 30; the script's
  spine is scenes (band life, office life, the ending room) and converting them to cards would
  fight the ask.
- Three 30-second blocks under four shot tasks: 5:30 (one sustained cobalt build), 9:00 (dense
  card/diagram evidence run), 11:00 (5-beat outro, arithmetic limit). Three other short blocks
  were fixed by honest relabeling (a split scene is wide, cupped hands are pov).
- First-50 versus last-50 word count 152 to 127, 17 percent drift, but the composition differs
  by design: the hook is dense story prose, the outro is terse cards. Compare like-for-like
  registers before treating this as chunking decay.

### The ending must land the hook and the next video at once

[9:57]-[10:06] replays the hook literally (rewind card quoting the three-chairs thumbnail, the
advice trio crossed out behind @YOU). [10:29]-[10:34] is the thesis hero frame (EVERYONE ring).
[10:36]-[11:09] then inverts the thesis (you are also the crowd) and hands off to project 5's
topic with a FOLLOW THE CROWD teaser card. That three-beat ending shape (callback, thesis hero,
inversion-teaser) is reusable for any episode that has a named next video.

## Project 11 (2026-08-28), REJECTED as "really bad and unattractive", then rebuilt

**Read this before the section below it.** The 332-prompt artifact described in the next section
passed all 21 mechanical checks and the user rejected the whole set on sight. Everything in that
section about method (data-first assembly, the Text-column defect, the token traps) still holds.
Its *content* is the counter-example. The rebuild is at the end of this file.

### THE DEFECT: every surface check passed while every story environment was empty

The budget said `illustrated story environment` on 35 percent of prompts. The prose delivered
"the room behind them is only a chair back and a plain wall edge" and "one plain doorframe stands
behind him at frame left". So 35 percent of the video was nominally a place and actually a blank
card with one prop, and the finished contact sheet read as wall-to-wall empty cards.

**Every check in Step 3 counts the surface *phrase*. Not one of them asks whether the prose
describes a place.** This is invisible to surface totals, per-prompt surface counts, the
mixed-surface check, tier equality, prompt count, timestamps, anchor and lock counts, and the
prompts-only grep. It is the same class as project 8's missing tokens and the Text column below:
a column the checks confirm the *presence* of but never the *content* of.

Rule now applied at authoring time: **a story-environment plate must name the place and at least
three objects that belong to it**, and must never be described as "an ordinary room", "a plain
wall edge", or "nothing else in the frame". Cheap check:

```bash
# story-environment prompts that never name a place-defining noun
grep '^\[' "$F" | grep 'illustrated story environment' | grep -cvE \
  'room|kitchen|study|camp|mall|concourse|road|landscape|podium|tavern|compound'
```

### Abstract glyph inflation: the script hands over concrete nouns and the plan ignored them

The rejected plan was built out of memory blocks, routes, markers, spans, two dials, a tape reel
and a doorway-with-a-block. The script supplies a 1974 projector and rows of chairs, broken glass
on a road, canoes and seal hunts turning into boats and fishing, a 1990s mall and a stranger's
flannel shirt, a gusle, spears, a river that shifted course, a group chat. Rule 7 says never
render an abstraction as an abstraction, and this was breaking it for roughly half the file with
nothing to catch it. **When a script is location-rich, list its concrete nouns first and check how
many reach the prompt file.** A plan whose plate keys are mostly shapes (`twoshelf`, `orderstrip`,
`twodials`, `notape`, `routes`) has already lost.

### Pick the motif from the script's own closing image, and prefer one a cast sheet already locks

Old motif: "an open doorway with one fragment passing through it", which degenerated into "a
charcoal doorway shape with one small block". New motif: **a flat broken glass shard**. It is the
script's own last image ("the broken glass was never in the film, it was in the question"), it is
already a locked prop in `@CLASS`'s reference sheet so the design is fixed, and the same drawing
*is* a fragment, so it carries the band pooling ten viewpoints, Bartlett's chain, the planted mall
detail, the modern feed and the ending. 102 beats, four acts, one glyph.

### Surface belongs to the plate, not the beat

Storing surface on the plate composition rather than on each beat makes a mixed-surface plate
structurally impossible instead of merely checked. Ten fewer things to verify. Tier still varies
per beat, which is legal when the delta justifies it.

### Cue gaps are bimodal, so a single CapCut threshold cannot hit the band

`gap >= 3.0` produced 92 CapCut beats (21.7 percent, cadence 35.3/min). `gap >= 3.5` produced 16
(4.6 percent, cadence 28.9). Nothing lands in between, because most cues in this transcript sit
exactly 3.0 seconds apart. Loosening and tightening the number is a dead end. **Make the rule
chain-aware instead:** always subdivide a hold of 3.5s or more, and add a 3.0s subdivision only
where the beat sits in a chain of 3 or more beats on one plate, which is where the video is
actually static. Landed 49 beats, 12.9 percent, cadence 31.7/min. Check the gap histogram before
picking any threshold.

### BREAK DENSITY IS A QUALITY LEVER, AND 25 WAS AN OUTLIER. Measure it every run.

The user rejected the rebuild's break count on the same grounds as the prose: "the fewer `---` in
prompts the fewer scenes the video is". That is exactly right and Step 3 never measures it. The
Step 3 note only says "zero breaks in a multi-act episode is not a pass", which 25 clears easily
while still being four times too few.

Every accepted project restarts the chain every 2.6 to 3.5 prompts:

| project | breaks / prompts | one fresh start every |
| ------- | ---------------: | --------------------: |
| 6       |        113 / 303 |          2.7 prompts  |
| 8       |        104 / 268 |          2.6 prompts  |
| 9       |         78 / 273 |          3.5 prompts  |
| 10      |         89 / 304 |          3.4 prompts  |
| **11 first pass** |  **15 / 332** | **22.1 prompts**  |
| **11 rebuild, before this fix** | **25 / 332** | **13.3 prompts** |

**Compute breaks-per-prompt and compare against that table before reporting.** Anything past about
4 prompts per break means long stretches are inheriting one frame and the video goes flat.

### The rule that produces the right density: break at every PLATE except real continuations

Placing breaks only at act boundaries and hard cuts is what produced 25. A `PLATE` is by definition
a complete new composition, so the default must be inverted: **break before every plate-opening
prompt, and keep a whitelist of plates that deliberately inherit** because they are a closer view or
the next step of one build on the same surface and the same subject (`face1` inside the same kitchen,
`empty1` as the same room emptied, `edited1` as the same block with pen marks). 128 plates minus 29
whitelisted continuations gave **99 breaks, one every 3.35 prompts**, longest inherited run 9,
mean 3.3. Rule 16 holds by construction: a break only ever lands immediately before a PLATE's first
prompt, so no variant or callback is ever severed from the plate above it.

### A callback landing between a plate and its continuation inherits the wrong frame

`P071` (the close on @SINGER) was whitelisted as continuing the Yugoslav tavern, but the prompt
directly above it is a `CALLBACK` to the cream overhead of two tape spools. So it would have
inherited a spools card, not the room, which is the contamination rule 16 exists to prevent. A
whitelisted continuation is only valid if the frame *immediately above it* shares its surface, and
callbacks reorder what that frame is. Guard, worth keeping in any re-break pass:

```python
if plate_not_in_CONTINUE or surface(prompts[i-1]) != surface(prompts[i]):
    cut = True
```

Two other whitelist entries were dropped because their runs reached 9 and 11 prompts (`ribbons`,
`honest1`); both fully describe themselves, so the cut costs nothing. The three runs that stay long
(8 to 9) each end in a callback that cannot legally be broken before, which is projects 6 and 8's
documented situation, and each callback rebuilds its composition in full.

### Re-placing breaks does not require the generators

Only break lines move, so the pass is: keep the lines starting with `[`, read `asset` and `Plate`
per timestamp out of `visual-plan.md`, re-insert `---`, re-assert shape. Prose, surfaces, tiers and
budgets come out byte-identical. Confirmed here: surfaces still 132/108/54/21/17 and tiers still
139/163/30 after the rewrite.

### The scratchpad is wiped mid-session, so "keep the generators" is not a plan

`/tmp/claude-1000/.../scratchpad` was emptied between two turns of one session, taking `plan11.py`,
`comps11.py`, `build11.py` and the earlier session's `plan_p11.py` with it. The previous entry's
advice to keep generators in the scratchpad until the video ships is therefore unreliable. What
survived is what was written into the project: `image-prompts.md` plus `visual-plan.md` together
carry the prose, the per-beat asset, plate, register, shot, tier, delta, motif and text, and the
surface is recoverable from each prompt's own phrase. **Treat those two files as the recovery pair,
and if a generator must survive a session, write it under the project rather than the scratchpad.**

### Rebuild numbers (2026-08-28): 332 prompts, 381 plan beats, 128 plates, 99 breaks

Clean on all 22 checks. V2 anchor and lock on all 332 with zero V1, timestamps exact, zero
non-prompt lines, first byte `[`, zero adjacent pairs without a blank line, 713 lines, tier plan
equal to prompts exactly, one surface phrase per prompt, zero mixed-surface plates, all 25 breaks
opening a PLATE, every source pointing backward, no em dash, no yellow.

Registers STORY 30.4, CARD 18.7, DIAGRAM 18.7, HYBRID 13.0, PORTRAIT 10.5, SPLIT_OR_SCALE 8.7,
**all six in band**, reached in one rebalancing pass by honest relabeling only (a room with two
people is STORY not SPLIT; booklets on a table are CARD not DIAGRAM). Surfaces story 39.8, cream
32.5, tinted 16.3, cobalt 6.3, white 5.1, all inside tolerance. Tiers CLEAN 41.9, LAYERED 49.1,
ATMOSPHERIC 9.0. Assets VARIANT 49.1, PLATE 33.6, CAPCUT 12.9, CALLBACK 4.5. Text 31.0 percent.

Plates went 130 to 128 but the *chain* shape changed, which is what the user was reacting to: the
rejected file ran 53 percent variants with deltas like "a bracket measures the gap between the two
blocks". Chain lengths are now capped at 4 and every delta is a story event.

@YOU 69 prompts, 20.8 percent of all and **42.0 percent of the 162 eligible cues**, the highest
recorded (project 6 was 36, project 8 35.8). The lift came from project 8's rule applied
deliberately: a second-person script puts the viewer inside his own hands rebuilding the fragments,
his own phone, his own palm holding the shard, and one of the two people remembering it
differently. Adding him to those plates took him 45 to 69 without inventing a frame.

One 30 second block carries fewer than four shot tasks: the `12:00` block, one beat, the last cue.
Arithmetic limit. Two others were real and fixed by re-shotting three plates.

## Project 11 first pass (2026-08-28), the REJECTED artifact: 332 prompts, 370 plan beats, 130 plates, 15 breaks

Clean on every mechanical check. 332 cues to 332 prompts, V2 anchor and lock on all 332 with zero
V1 strings, timestamps an exact diff match with no duplicate stamps anywhere in the transcript,
zero non-prompt lines, first byte `[`, zero adjacent pairs without a blank line, 693 lines, tier
counts equal to plan exactly (152 CLEAN / 160 LAYERED / 20 ATMOSPHERIC), surfaces summing to 332
with exactly one phrase per prompt, zero mixed-surface plates, all 15 breaks opening a PLATE, no
em dash, no yellow text.

Motif: **an open doorway with one fragment passing through it**, on 92 beats. Per the project 8
rule I looked for the drawing both halves share instead of inventing two, and this script hands it
over explicitly: "a second reason to leave the door open", then "the door is still wide open, it
has never closed". The ancestral half is witnesses carrying fragments through it; the modern half
is the identical door with lawyers, headlines and feeds coming through. It also carries the
psychology act (the word walks through it) and the echo (the glass came through it). One glyph,
four acts.

Final budgets. Registers STORY 29.7, CARD 19.2, DIAGRAM 15.7, SPLIT_OR_SCALE 12.4, PORTRAIT 11.9,
HYBRID 11.1 percent, five of six inside their bands. Surfaces story 34.9, cream 29.8, tinted 19.9,
white 8.4, cobalt 6.9, **every one within a point of target**, the closest the channel has come.
Tiers CLEAN 45.8, LAYERED 48.2, ATMOSPHERIC 6.0. Assets over 370 beats VARIANT 53.0, PLATE 35.1,
CAPCUT 10.3, CALLBACK 1.6. Text 26.5 percent (88 of 332). Cadence 30.8 beats per minute. Cast
@YOU 77, @CLASS 18, @BAND 15, @SINGER 10, @BARTLETT 8; tokens on 127 of 332 prompts. @YOU is 23
percent of all prompts and **40.3 percent of the 191 cues where rule 12 allows him**, above
project 6's 36 and project 8's 35.8. The three other-era acts that bar him are `[1:00]` to
`[2:52]`, `[4:49]` to `[7:47]`, and `[10:39]` to `[10:50]`, 141 cues. Exactly one `@YOU` frame
sits inside one of them, `[7:47]`, and it is an explicit ancestral-left / modern-right split
composition, which is the deliberate then-versus-now case rule 12 permits.

One 30 second block carries fewer than four shot tasks: the `12:00` block, which holds a single
beat because it is the last cue. Arithmetic limit, not a defect, same as project 6's 5 second
final block.

Two plates span two render tiers, `mall` and `wordforword`. Both are justified by the delta: the
mall callback drops the atmospheric fog to rebuild as LAYERED, and the wordforword variants strip
to locking blocks and lines, which is a CLEAN diagram move. **A plate chain may change tier when
the delta is the reason; only a plate chain that changes SURFACE is a contradiction.** Zero plates
have mixed surfaces.

### THE DEFECT WORTH REMEMBERING: the plan's Text column never reached the prompts

First assembly passed **every** mechanical check in Step 3 while on-screen text sat at **25 of 332
prompts, 8 percent**, against a plan that assigns text to 88 beats and a V2 band of 25 to 35.

Cause: text was only present where I happened to write it into a PLATE's composition prose. Every
VARIANT and CALLBACK is generated from the plate prose plus a delta, and the delta clause says
nothing about text, so 63 beats that the plan marks as carrying text rendered none. This is
invisible to prompt count, timestamps, anchor and lock counts, surface counts, tier equality, the
prompts-only grep, and the adjacent-pair check. It is the same shape as project 8's missing-token
defect, one column over.

**Fix: emit the plan's Text column in the assembler, not in the prose.** Three lines:

```python
txt = beat["text"]
if txt != "-" and txt not in scene:
    scene += f' Bold {"red" if txt in NEG else "charcoal"} ALL CAPS text reads {txt} in the upper frame.'
```

with `NEG` an explicit negation allowlist so rule 9's red-only-for-negation holds by construction.
That took text from 8 to **26.5 percent, 88 of 332, zero yellow.** **Generalise: every plan column
that carries information must be read by the assembler. A column the generator never reads is a
column the plan is lying about.**

### The obvious check for that defect is itself wrong, and it under-reports

The equality check first written here was `grep -c 'ALL CAPS text reads' "$F"` against the plan's
text-beat count. **It reads 62, not 88, on a file that is correct.** The `txt not in scene` guard
means the assembler appends its clause only where the plate prose has not already written the
string, so 26 of the 88 carry their text inside the composition prose in some other wording and
the grep cannot see them. A re-verification run reported a false 62-versus-88 failure on a clean
file and nearly triggered a repair of something that was never broken.

The check has to compare **the plan's text string against its own prompt**, not one phrasing:

```python
missing = [b["ts"] for b in gen if b["text"] != "-" and b["text"] not in prompts[b["ts"]]]
```

Zero missing, and text coverage is then `len(withtext)/len(gen)`. The 62 figure is still worth
printing as a breakdown (11 red, 51 charcoal come from the assembler clause) but it is not the
coverage number. **Generalise the generalisation: a check written against the fix rather than
against the requirement inherits the fix's blind spots.**

Same class of error one column over: the plan table has **no Surface column** at all. Its header is
`Beat | Time | Meaning | Register | Shot | Tier | Asset | Plate | Source | Delta | Motif | Text`,
so a mixed-surface check that splits the markdown row on `|` and reaches for a surface index is
really reading Tier and will report tier spans as surface contradictions. Surface lives in the beat
data only. **Run the mixed-surface check against `beats.json`, never against the plan table.**

### Deletion and rebuild: data-first assembly reproduced the artifact byte for byte

`image-prompts.md` and `visual-plan.md` were both removed from the project after acceptance, and
project 11 is untracked so git held no copy. Re-running `plan_p11.py` then `assemble.py` restored
both exactly: 332 prompts, 15 breaks, 693 lines, identical cast distribution, identical tier and
surface totals, every Step 3 check green again. **The generator scripts are the real artifact; the
markdown is an output.** Keep the scratchpad generators for a project until the video ships, and
prefer re-running them over recovering the markdown from anywhere else.

### Second deletion, and the generators were in a SIBLING session's scratchpad

Both files were removed again and rebuilt a third time from `plan_p11.py` plus `assemble.py`,
reproducing every number exactly: 332 prompts, 15 breaks, 693 lines, 130 plates, 370 plan beats,
identical tier, surface, register and cast totals, all 21 checks green. The note above is now
confirmed twice over.

The trap is where the generators live. **The scratchpad is session-scoped**
(`/tmp/claude-1000/<project>/<session-uuid>/scratchpad`), so "keep the generators until the video
ships" does not mean they are in *this* session's scratchpad. They were in `5f4c353a`'s while the
run was happening in `3755bad7`. Before rebuilding any stage from scratch, search every sibling
session directory first:

```bash
find /tmp/claude-1000/<project-slug> -maxdepth 3 -name 'plan_p*.py' -o -maxdepth 3 -name 'assemble.py'
```

Copy what you find into the current scratchpad and re-run it there rather than editing another
session's directory. Rewriting 130 plate compositions by hand because the generator looked missing
is the expensive version of this mistake.

### The eligible-share denominator needs stating, not just the number

The entry above records @YOU at 40.3 percent of eligible cues; recomputing gives 39.8. Both are
right: 77 of 191 counts the `[7:47]` split frame that sits inside a barred act, 76 of 191 excludes
it. A one-frame difference is noise, but **write which denominator the figure used**, or a later
re-verification reads a convention change as drift.

### Length drift 2.3 percent, the lowest the channel has recorded

First 50 prompts 137 words, last 50 134. Projects 8 and 10 recorded 5.2 and 7.0 percent. The
difference is not discipline, it is that only 130 pieces of prose were hand-written and the other
202 prompts were generated from them, so there is nothing to decay. Variants-only comparison was
0.9 percent. **Data-first assembly makes the chunking-decay metric almost meaningless; read it as
a check on the plate prose, not on the whole file.**

### Reading one prompt of each asset type caught nothing this time, and still earned its place

Project 10 lost 120 prompts to "a illustrated story environment". Emitting the surface as
`Render on the <phrase>.` avoids the article problem entirely for all five phrases, and the
end-to-end read of one PLATE, one VARIANT and one CALLBACK confirmed it. The VARIANT does name its
surface twice, once in the preserve clause and once in the render clause; that is deliberate, it is
what makes the per-prompt surface count pass, and project 10 shipped the same shape.

## 2026-08-29 - Two standing rules from user feedback

### Scene density: the script decides, the numbers are only a sanity anchor

Confirmed directly: "chia phân cảnh trong image prompts khá tốt" for projects 7 through 11,
"đừng chia ít phân cảnh quá sẽ bị nhàm chán và cũng đừng chia nhiều phân cảnh quá sẽ bị rời rạc".
Each stretch between two `---` is one phân cảnh. Too few is boring, too many is rời rạc.

**Corrected by the user immediately after I first wrote this note.** I had turned the observed
2.6 to 3.5 range into a hard pass/fail gate in Step 3. The user's correction: "scene density
không phải lúc nào cũng cứng nhắc ... quan trọng là nó phải phù hợp với phân cảnh và nội dung
của script, tất cả là để biểu đạt script một cách tốt nhất có thể." So the range is a reference,
not a threshold. Most episodes land in it, up to about 4.5 is fine when the script carries long
sustained scenes, and the check now prints "in the usual range" or "REVIEW" instead of FAIL.

**The generalisable mistake is mine, not the rule's: I converted a descriptive observation into
a prescriptive gate.** Five projects landing between 2.6 and 3.5 is evidence about what those
scripts needed, not a constraint the next script must satisfy. Cut where the meaning changes.
A number that is unexplained is the failure; a number that is justified and reported is fine.

The two real defects the figure exists to surface, and they are asymmetric in how they look:
a long stretch of unrelated frames all inheriting one image (project 11's rejected 13.28), and
a chain cut so often that no build survives to its payoff. Project 11 shipped at 3.32, 100
breaks over 332 prompts.

The generating rule matters more than the number: **default to breaking at every `PLATE`**, and
whitelist only the plates that genuinely continue the frame above them. Placing breaks at act
boundaries alone undershoots by about four times.

### A real named person needs a real likeness and a one-time name caption

When the script names a real scientist, psychologist, or public figure who appears on screen,
the audience has to recognise them and be told who they are. Two halves, in two skills, because
`scenes` rule 5 forbids re-describing a cast member:

- **`/cast` builds the likeness.** Two or three recognisable features locked into the sheet,
  carried by hair shape, facial hair, eyewear, headgear, and era clothing, never by realistic
  anatomy. A generic sheet makes that person generic for the whole video.
- **`/scenes` captions and introduces.** The name in bold charcoal ALL CAPS on the **first**
  frame the person appears in and nowhere after it, because the audience already knows them by
  the second frame and the repeat wastes the text budget. Where the script introduces someone
  before showing their work, spend one generation on a portrait beat with the name over it, then
  cut to the action. Two people introduced together can share one portrait frame with both
  names, which hands the next scene two known faces.

Stay flexible: this is not a template to apply on every mention. A researcher named once and
never depicted still stays a diagram, per the project 2 note above. The style lock is unchanged,
so this is a recognisable doodle likeness, never a rendered face. A genuine photograph, if ever
wanted, is a CapCut overlay at edit time, not a generation prompt.
