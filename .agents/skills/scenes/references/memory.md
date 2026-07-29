# scenes - memory

Self-improving notes for image prompts. Single canonical copy.

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

| | project 2 first pass | project 1 accepted |
| --- | --- | --- |
| plain white | 37 percent | **58 percent** |
| cobalt + solid blue | **40 percent** | 18 percent |

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
