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
