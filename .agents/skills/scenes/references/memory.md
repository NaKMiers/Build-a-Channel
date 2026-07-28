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
