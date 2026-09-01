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

Stage 4 of the TossExplains pipeline, and the largest artifact: one generated prompt per
transcript cue, typically 230 to 270 for V1 and 300 to 330 for V2, plus optional V2 CapCut-only
beats in the visual plan.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md` - **the whole file.** Both style versions, the current V2
  render tiers, registers, shot grammar, palette, cadence, and the legacy V1 rules.
- `.agents/rules/file-formats.md` - the `prompts/visual-plan.md` and
  `prompts/image-prompts.md` sections
- `.agents/rules/image-generation.md` - the chain workflow this file feeds, and the `---`
  chain break it must carry
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
- Transcript under 20 lines: stop and say "This looks incomplete. A normal 10 to 14 minute
  TossExplains video should have hundreds of timestamp lines."

## Step 1 - Inventory the transcript

```bash
T="$P/transcribes/transcript.md"
grep -c . "$T"                           # total cues
awk '{print $1}' "$T" | sort | uniq -d   # duplicate timestamps
```

Record the totals for the final chat report and mechanical verification.

## Style version selection

Source `.agents/bin/style-strings.sh` before planning.

- Projects 1 through 5 are frozen V1. A redo keeps V1 even if its prompt file is missing.
- Project 6 and later use V2.
- If an existing `character-prompts.md`, `visual-plan.md`, or `image-prompts.md` explicitly
  identifies a version, keep that version when redoing only this stage.
- Never mix V1 and V2 anchors or locks inside one project.

V1 follows the legacy path below and does not receive `visual-plan.md`. V2 completes the lean
planning pass before writing prompt prose.

## V2 lean planning pass

Write `prompts/visual-plan.md` in the exact format from `file-formats.md`.

1. Copy the three chapter colors from the V2 cast header. Choose one recurring concrete motif.
2. Create one generated beat for every transcript cue. Extra CapCut-only beats may subdivide a
   long cue or create a meaningful diagram build without adding a generation.
3. Assign register, shot, tier, asset type, plate, source, delta, motif, and text before writing
   any full image prompt.
4. Target 35 to 45 percent new `PLATE` rows, 30 to 40 percent `VARIANT`, 10 to 15 percent
   `CAPCUT`, 5 to 10 percent `CALLBACK`, and 5 to 10 percent text or diagram update beats.
   **`VARIANT` is the share that drifts, and it drifts upward.** Project 12 planned inside this
   budget and shipped 63 percent variants against the 40 percent ceiling, roughly 70 surplus
   beats, because nothing measured the mix until Step 3 was taught to. Count the mix while
   planning, not after writing 300 prompts. Every beat that wants to be a variant but has no
   legible delta under rule 18 becomes a `PLATE`, which is what brings the share back down.
5. **Fill the continuity ledger before assigning beats.** Walk the script for every non-cast
   object drawn in two or more separated scenes: the balance, the ladder, the chart, the camp
   ring, the recurring diagram. Give each one a canonical first timestamp, a locked one-phrase
   description, and the list of timestamps it returns at. Anything named, spoken about, or
   treated as a participant is not a ledger object, it is a cast member, so stop and add it to
   `/cast` instead. Every return listed here becomes an `@[timestamp]` in Step 2 under rule 19.
6. **Compose every build-opening plate around the space its deltas will need.** A plate that
   arrives full cannot carry a build, and its variants degrade into attribute changes, which is
   the rule 18 failure. Decide the empty regions at plan time, in the plate's `Meaning` cell.
7. Keep `ATMOSPHERIC` at or below 10 percent. Use `CLEAN` near 40 percent and `LAYERED` near
   50 percent.
8. Rotate registers after two or three beats. A longer run is legal only when every beat shares
   one plate and forms a valid build.
9. In each 30 second block, plan at least four shot tasks from the V2 shot grammar.
10. Every variant points backward to an earlier source beat and names exactly one meaningful
    delta that satisfies rule 18. Every callback points backward and states the changed meaning.
11. Add CapCut-only events where required so no ordinary unchanged hold exceeds 4 seconds and
    whole-video rhythm reaches 28 to 32 meaningful visual states per minute.
12. Plan 5 to 8 build chains and an ending callback to the hook for a normal 10 to 12 minute
    episode.
13. Mark where the generation chain gets cut. A cut belongs at a chapter or act boundary and at
    any hard cut in place, era, cast, or surface register. It may only land on a `PLATE` row,
    never on a `VARIANT`, a `CALLBACK`, or a hold, and never between a variant and its source.
    These become the `---` lines in `image-prompts.md`. See prompt rule 16.

## The prompt rules

1. **Every prompt begins with its timestamp, copied character for character from the
   transcript.** `[0:00]` stays `[0:00]`, `[00:00]` stays `[00:00]`. Never reformat,
   re-pad, or renumber a timestamp. When saving the image, replace its colon with a
   hyphen so the filename works on Windows: `[0:00]` becomes `[0-00].jpg`.
2. **The `[MM:SS]` prefix and every `@TOKEN` are instructions for the human and the file
   system, not visual content.** They must never appear as rendered text in the generated
   image: no timestamp, clock, or counter burned into a corner, no literal "@NAME" caption
   anywhere in the frame. This is why every prompt's STYLE LOCK explicitly repeats that
   negative. **Never drop it.**
3. **Every prompt opens with the selected version's STYLE ANCHOR** from `visual-style.md`,
   copied character for character. V1 uses `V1_STYLE_ANCHOR`; V2 uses `V2_STYLE_ANCHOR`.
4. **Every prompt ends with the same version's STYLE LOCK**, copied character for character.
   V1 uses `V1_STYLE_LOCK`; V2 uses `V2_STYLE_LOCK`.
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
8. **For V1, match background color to tone** using the legacy tone map in
   `visual-style.md`, and respect the
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
   - **For V2, use exactly one planned surface family per generated prompt:** `warm cream or
off-white card`, `light tinted chapter card`, `illustrated story environment`, `cobalt mind
interior`, or `pure white card`. Follow the V2 budget and selected chapter palette. Reserve
     saturated channel blue for Toss or one semantic diagram signal. A generic crowd may use dusty
     blue, but not saturated channel blue when Toss wears his default blue hoodie.
9. **On-screen text is charcoal or black by default, red only for danger, threat, failure, or
   negation.**
   Never yellow on a white background, it is unreadable.
10. **Emotion lives first in the eyebrows, mouth line, body posture, and head color.** V1 never
    places emotion in background detail. V2 may use one supporting environment contrast, such as
    a warm party around a cool isolated Toss, but the character must still read without it.
11. **Hold plates across consecutive timestamps.** If 3 lines describe the same moment,
    keep the same scene, the same cast members, and the same background, and only adjust
    their expression or add one new element. In V2, encode the chain in `visual-plan.md` and
    preserve camera axis, cast placement, environment geometry, major objects, palette, and line
    hierarchy. **Do not generate a brand new scene every 5 seconds.**
12. **Keep the cast internally logical.** `@YOU` carries the modern-life frames. The cast
    member from the script's other era or setting carries those frames. The two appear
    together only in a deliberate then-vs-now split frame. Do not swap who plays which
    role mid-video, and never place a character in an era their reference sheet was not
    drawn for.
13. **Use the nine proven frame types** from `visual-style.md` when appropriate. V2 also rotates
    the six named registers and the seven shot tasks instead of repeating one layout.
14. **Every V2 prompt names its render tier in this exact form:** `CLEAN render tier:`,
    `LAYERED render tier:`, or `ATMOSPHERIC render tier:`. Follow only the permissions for that
    tier. Do not let an atmospheric effect leak into CLEAN.
15. **Every V2 prompt implements one visual-plan row.** A new plate describes a complete
    composition. A variant begins its scene clause with `Preserve the attached source plate`
    and names the single delta. A callback names the earlier plate and its changed meaning.
16. **Cut the chain with a `---` line wherever a frame must not inherit the frame before it.**
    The generation tool wires every card to the previous card, so prompt N is generated from
    prompt N-1's image unless a break stops it. Read `.agents/rules/image-generation.md` for
    the full rule.

    **Each stretch between two `---` lines is one phân cảnh, one scene, and the user judges
    the video by how those scenes are divided.** Too few and long stretches all inherit one
    frame and the video is boring. Too many and it is rời rạc, disjointed, with nothing
    holding together.

    **The real criterion is the script, not a number.** The division has to suit the scenes and
    the content, because the only job here is to express the script as well as possible. A
    sustained metaphor scene, a long camp sequence, or one continuous room legitimately runs
    longer; a dense run of cards, numbers, and diagrams legitimately runs shorter. Cut where
    the meaning changes, not on a quota.

    Projects 7 through 11 are the observed range, useful as a sanity anchor:

    | project | breaks / prompts | one fresh start every |
    | ------- | ---------------: | --------------------: |
    | 7       |         95 / 297 |           3.1 prompts |
    | 8       |        104 / 268 |           2.6 prompts |
    | 9       |         78 / 273 |           3.5 prompts |
    | 10      |         89 / 304 |           3.4 prompts |
    | 11      |        100 / 332 |           3.3 prompts |

    Most episodes land near one break every 2.6 to 3.5 prompts, and up to about 4.5 is fine
    when the script genuinely carries long sustained scenes. **Treat that as a reference, not a
    gate.** Compute the figure, and if it sits outside, decide whether the script justifies it:
    if it does, say so with the reason in the Step 4 report; if it does not, re-place the
    breaks. What is never acceptable is a count nobody looked at. The signature of the real
    defect is a long stretch of unrelated frames all inheriting one image, which is how project
    11's 13.3 prompts per break got rejected, and its opposite is a chain cut so often that a
    build never survives to pay off.
    - **The default at a `PLATE` is to break.** A plate is by definition a complete new
      composition, so placing breaks only at act boundaries and hard cuts undershoots badly:
      that approach gave project 11 twenty-five breaks, one every 13.3 prompts, and the user
      rejected it. Instead break before every plate-opening prompt and keep an explicit
      whitelist of plates that deliberately inherit, being a closer view or the next step of
      one build on the same surface and the same subject.
    - A whitelisted continuation is only valid if the frame **immediately above it** shares its
      surface. A `CALLBACK` can land between a plate and its intended continuation, so the
      continuation would inherit the callback's frame instead. Guard it:
      `if plate not in CONTINUE or surface(prev) != surface(this): cut = True`.
    - **Never break between a `VARIANT` or `CALLBACK` and the plate it points back to.** The
      chain is linear, so cutting it there destroys the lineage the plan just declared. Never
      break inside a hold either. Those beats depend on inheritance.
    - Format is exactly `---` alone on a line, one blank line above and one below, never the
      first or last line of the file, never two in a row.
    - A break creates no record and no scene image. Prompt count, timestamps, and file names
      are untouched by it.

17. **When the script names a real person who appears on screen, the viewer must be able to
    recognise them and be told who they are.** A generic doodle for Einstein, Tesla, Loftus, or
    Bartlett wastes the one moment the audience can attach a face to a name.
    - **The likeness lives in the cast sheet, never here.** Rule 5 forbids re-describing a cast
      member, so `scenes` cannot make a figure look like anyone. If a real named person appears
      on screen, `/cast` must build their sheet from the person's documented appearance, and
      `scenes` refers to them by `@TOKEN` as with any other member. If the sheet is generic,
      stop and fix the cast, do not compensate with description here.
    - **Caption the name on the first frame the person appears in, and only there.** Bold
      charcoal ALL CAPS, upper frame, the name alone. Later frames of the same person carry no
      caption: the audience already knows them, and repeating it burns the text budget.
    - **An introduction beat is often worth one generation.** Where the script introduces a
      person before showing what they did, a portrait frame with the name over it, followed by
      the action scene, reads far better than dropping a stranger into an experiment. Where the
      script introduces two people at once, one frame holding both portraits with both names
      hands the next scene two known faces.
    - **Be flexible.** Neither shape is mandatory. A person named once in passing and never
      depicted stays a diagram or a generic figure, per the researcher-not-depicted rule in
      `references/memory.md`. Fit the script rather than applying a template.
    - The style lock still holds: no photorealism, no 3D, no CGI. A recognisable doodle
      likeness, not a rendered face. If a genuine photograph of the person is wanted, that is
      an overlay decision for CapCut at edit time, not an image-generation prompt.

18. **A delta must be legible as presence, absence, position, or count, at the size it is
    drawn.** This is the rule that separates a real variant from a duplicate.

    Project 12 shipped both shapes and the difference is visible in the finished images.
    `[0:29]` to `[0:35]` works: the plate plants three panels and leaves two of them **empty**,
    then panel 2 fills, panel 3 fills, and a figure walks out of panel 3. Every delta claims a
    different region that was reserved for it. `[1:41]` to `[1:48]` fails: the plate draws
    three cards with their shapes already in them, and the delta at `[1:43]` is "the angular
    shape on the right thickens and turns hard edged". Nothing appears, nothing moves, no
    region is claimed. The model can only ignore it, which leaves generator noise as the sole
    difference, or redraw, which changes the frame for the wrong reason. `[10:50]`'s "every one
    of those faces is calm and settled", on nine figures a few pixels wide, fails the same way:
    the delta sits below the scale it is drawn at.

    - **Attribute-only deltas are banned.** Thicker, harder, softer, calmer, tenser, warmer,
      more hostile, more crowded. If the change is an adjective applied to something already on
      screen, it is not a delta.
    - **Check the scale before writing the delta.** A change to a face, a label, or a texture
      inside an element drawn small is not legible no matter how it is worded. Either the plate
      draws that element large enough, or the delta belongs somewhere else.
    - **Reserve the space in the plate.** When the plan opens a build chain, the plate must be
      composed with the empty regions its coming deltas will occupy. A plate that arrives full
      has nowhere to put its own build.
    - **When a beat has no legible delta available, promote it to a `PLATE`.** Never write a
      variant you know will not read. Do not drop the generation and do not merge it into a
      neighbour: one transcript cue is always exactly one prompt, and `CAPCUT` beats are extra
      beats, never replacements. The escape hatch is a genuinely new composition on the same
      meaning, a different register, shot, or angle, which is also how the variant share stays
      inside its budget.

19. **Use `@[timestamp]` to hold a recurring non-cast object consistent across a chain break.**
    Read the `@[timestamp]` section of `.agents/rules/image-generation.md` for the tool
    contract. The chain reaches one card back and a `---` severs it, so an object introduced at
    `[0:38]` and drawn again at `[10:12]` is otherwise redrawn from words alone and returns a
    different colour. That inconsistency is what this syntax exists to fix.

    - **Write `@[M:SS]`, colon and all**, copied from the target prompt's own leading
      timestamp. `@[0:38]`, never `@[0-38]`.
    - **Point at the object's canonical first appearance, never at its most recent one.**
      Chained hops re-generate from a copy and compound the drift. The canonical timestamp is
      the one recorded in the continuity ledger.
    - **Backward only**, and never at the prompt's own timestamp.
    - **Two per prompt is the ceiling in practice.** More are legal but the model starts
      blending the referenced compositions into the new frame.
    - **Every prompt containing an `@[timestamp]` also carries the V2 SCENE REFERENCE LIMIT**
      from `visual-style.md`, copied character for character, placed after the scene clause and
      before the STYLE LOCK. Without it the tool hands over a whole image and the model takes
      the whole image. The limit is what makes it a design source instead of a composition
      source, which is the exact opposite of a `VARIANT`'s
      `Preserve the attached source plate`.
    - **Put the reference at the start of the clause about that object**, the same way a
      `@TOKEN` opens its character's clause: `@[0:38] the same charcoal beam balance returns,
      now tipped the other way`.
    - **Do not reference a cast member's timestamp.** Characters are held by their bound sheet.
      A `@[timestamp]` aimed at a character competes with the sheet instead of helping it.
    - **Do not reference across a hold or inside a build chain.** Consecutive frames already
      inherit each other; a reference there is noise.

## Step 2 - Generate in internal chunks

**Write NO header. The file contains prompts, blank separators, and `---` chain breaks, and
nothing else.** The first byte of the file is the `[` of the first prompt. No title, no cast
line, no source-transcript line, no attachment note, no GENERATION LINE, no commentary
anywhere. `image-prompts.md` is imported wholesale into an image tool that treats every line as
a prompt, so a header becomes a junk generation. The cast list, cue counts,
duplicate-timestamp note and GENERATION LINE all go in the **chat report** at Step 4 instead,
where the human reads them and the tool never sees them.

Work through the transcript in **internal chunks of 25 cues**, appending each chunk to the
file. Do not ask the user between chunks. Before each chunk after the first, re-read the
last 3 prompts you wrote so the scene-holding rule survives the chunk boundary, re-check
the tone map so the background palette does not drift, and **re-read the continuity ledger** so
a returning object still gets its `@[canonical]` reference. The ledger matters most exactly
where chunking hurts most: an object introduced in chunk 1 and returning in chunk 11 is the
case the whole reference syntax exists for, and it is the case a single forward pass forgets.

Chunking is not cosmetic. A single uninterrupted pass over 250 prompts degrades: scenes stop
holding, backgrounds drift toward white, and the last 50 prompts get shorter than the first 50. Chunk, re-anchor, continue.

## Step 3 - Verify mechanically

```bash
source .agents/bin/style-strings.sh
F="$P/prompts/image-prompts.md"
T="$P/transcribes/transcript.md"
N=$(grep -c '^\[' "$F")

# One prompt per cue. CapCut-only plan rows do not create prompt records.
echo "cues: $(grep -c . "$T")  prompts: $N"

# PROMPTS ONLY: no header, no title, no commentary. Only '---' breaks are allowed. Must be 0.
grep -vE '^(\[|---$)' "$F" | grep -c .
head -c1 "$F"   # must be [

# Chain breaks: exactly '---', blank line each side, never first or last, never doubled.
B=$(grep -c '^---$' "$F")
awk '{L[NR]=$0} END{for(i=1;i<=NR;i++) if(L[i]=="---"){
  if(i==1||L[i-1]!="") print i": break needs one blank line above"
  if(i==NR||L[i+1]!="") print i": break needs one blank line below"
  if(i>2&&L[i-2]=="---") print i": two breaks in a row"}}' "$F"

# SCENE DENSITY, rule 16. Advisory, not a gate: the script decides. Outside the reference
# range, either justify it in the Step 4 report or re-place the breaks.
awk -v b="$B" -v n="$N" 'BEGIN{
  d=n/b
  printf "  breaks %d / prompts %d = one scene every %.2f prompts\n", b, n, d
  if (d>=2.6 && d<=3.5) print "  in the usual range"
  else if (d<=4.5 && d>3.5) print "  above usual: OK only if the script carries long sustained scenes, say which"
  else if (d>4.5) print "  REVIEW likely too few scenes; check for unrelated frames inheriting one image"
  else print "  REVIEW likely too many scenes; check that builds still survive to a payoff"}'
# Longest inherited run. A run past about 10 prompts is one frame carrying too much.
awk '/^---$/{if(r>m){m=r;t=s}; r=0; next} /^\[/{if(r==0)s=$1; r++}
     END{if(r>m){m=r;t=s}; print "  longest inherited run "m" prompts, starting "t}' "$F"

# Timestamps identical and in order.
diff <(awk '{print $1}' "$T") <(grep -o '^\[[0-9:]*\]' "$F") && echo "timestamps match"

# Exactly one style version must cover every prompt.
V1A=$(grep -cF "$V1_STYLE_ANCHOR" "$F"); V1L=$(grep -cF "$V1_STYLE_LOCK" "$F")
V2A=$(grep -cF "$V2_STYLE_ANCHOR" "$F"); V2L=$(grep -cF "$V2_STYLE_LOCK" "$F")
printf 'V1 anchor/lock %s/%s  V2 anchor/lock %s/%s\n' "$V1A" "$V1L" "$V2A" "$V2L"

# No token outside the cast table.
comm -13 <(grep -oE '@[A-Z]+' "$P"/prompts/character-prompts.md | sort -u) \
         <(grep -oE '@[A-Z]+' "$F" | sort -u)

grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"

# V1 background budget. Run only when V1A equals N.
S=0
for pat in 'plain white background' 'cobalt blue' 'tan #C4965A' 'orange #F5820D' 'grass green #3A9E3A'; do
  c=$(grep -ci "$pat" "$F"); S=$((S+c)); printf '  %-26s %3s  %2s%%\n' "$pat" "$c" "$((c*100/N))"
done
echo "  sum $S of $N"
for col in black red yellow; do printf '  text %-7s %3s\n' "$col" "$(grep -c "bold $col ALL CAPS" "$F")"; done
grep '^\[' "$F" | grep 'plain white background' | grep -c 'bold yellow'   # must be 0

# V2 plan and prompt budgets. Run only when V2A equals N.
V="$P/prompts/visual-plan.md"
grep -c '^Style version: V2$' "$V"          # exactly 1
grep -c '^| B[0-9][0-9][0-9] ' "$V"        # all planned visual states
grep '^| B[0-9][0-9][0-9] ' "$V" | grep -vc ' | CAPCUT |'  # must equal N
for tier in CLEAN LAYERED ATMOSPHERIC; do
  printf '  tier %-12s plan %3s prompts %3s\n' "$tier" \
    "$(grep '^| B[0-9][0-9][0-9] ' "$V" | grep -v ' | CAPCUT |' | grep -c " | $tier |")" \
    "$(grep -c "$tier render tier:" "$F")"
done
for surface in 'warm cream or off-white card' 'light tinted chapter card' \
  'illustrated story environment' 'cobalt mind interior' 'pure white card'; do
  printf '  surface %-34s %3s\n' "$surface" "$(grep -ci "$surface" "$F")"
done

# Variant, callback, and CapCut sources must point backward and carry one delta.
awk -F'|' '
  /^\| B[0-9][0-9][0-9] / {
    gsub(/^ +| +$/, "", $2); beat=$2
    gsub(/^ +| +$/, "", $8); asset=$8
    gsub(/^ +| +$/, "", $10); source=$10
    gsub(/^ +| +$/, "", $11); delta=$11
    if (asset != "PLATE" && (source == "-" || !(source in seen)))
      print "bad source at " beat ": " source
    if (asset != "PLATE" && delta == "-") print "missing delta at " beat
    seen[beat]=1
  }
' "$V"

# A chain break may only open a new PLATE, never a variant, callback, or hold.
awk -F'|' '
  NR==FNR { if ($0 ~ /^\| B[0-9][0-9][0-9] /) {
      t=$3; a=$8; gsub(/^ +| +$/, "", t); gsub(/^ +| +$/, "", a); asset[t]=a } ; next }
  { L[FNR]=$0 }
  END { for (i=1;i<=FNR;i++) if (L[i]=="---")
          for (j=i+1;j<=FNR;j++) if (L[j] ~ /^\[/) {
            match(L[j], /^\[[0-9:]+\]/); t=substr(L[j], 1, RLENGTH)
            if (asset[t] != "" && asset[t] != "PLATE")
              print "break before " t " opens a " asset[t] ", not a PLATE"
            break } }
' "$V" "$F"

# ASSET MIX, rule 18 and planning step 4. Advisory, like scene density: print it and judge it.
# VARIANT is the share that drifts upward. Project 12 shipped 63% against a 40% ceiling.
awk -F'|' '
  /^\| B[0-9][0-9][0-9] / { a=$8; gsub(/^ +| +$/, "", a); n[a]++; t++ }
  END {
    lo["PLATE"]=35;    hi["PLATE"]=45
    lo["VARIANT"]=30;  hi["VARIANT"]=40
    lo["CALLBACK"]=5;  hi["CALLBACK"]=10
    lo["CAPCUT"]=10;   hi["CAPCUT"]=15
    printf "  asset mix over %d planned beats\n", t
    split("PLATE VARIANT CALLBACK CAPCUT", k, " ")
    for (i=1; i<=4; i++) { a=k[i]; p=n[a]*100/t
      printf "    %-9s %3d  %5.2f%%  target %d to %d%s\n", \
        a, n[a], p, lo[a], hi[a], (p<lo[a]||p>hi[a]) ? "   REVIEW" : "" } }
' "$V"

# @[timestamp] references: resolve backward to a real earlier prompt, never to self.
awk '
  /^\[/ { match($0, /^\[[0-9:]+\]/); ts=substr($0, 1, RLENGTH); seen[ts]=1
    n=split($0, part, /@\[/)
    for (i=2; i<=n; i++) if (match(part[i], /^[0-9]+:[0-9]+\]/)) {
      r="[" substr(part[i], 1, RLENGTH); refs++
      if (r == ts) print "  " ts " references itself"
      else if (!(r in seen)) print "  " ts ": @" r " does not resolve to an earlier prompt" } }
  END { print "  @[timestamp] references: " refs+0 }
' "$F"

# Every prompt carrying a reference also carries the V2 SCENE REFERENCE LIMIT. Must be 0.
grep '@\[[0-9]' "$F" | grep -cvF "$V2_SCENE_REF_LIMIT"

# Continuity ledger: every listed return actually carries @[canonical] in its prompt.
awk -F'|' '
  NR==FNR {
    if ($0 ~ /^\| B[0-9][0-9][0-9] /) next
    if ($0 !~ /^\| *[A-Za-z]/ || $0 ~ /^\| *Object/) next
    if ($3 !~ /\[[0-9]+:[0-9]+\]/) next
    c=$3; gsub(/[^0-9:]/, "", c); canon="[" c "]"
    n=split($5, parts, ",")
    for (i=1; i<=n; i++) { t=parts[i]; gsub(/[^0-9:]/, "", t)
      if (t != "") need["[" t "]"]=canon }
    next }
  /^\[/ { match($0, /^\[[0-9:]+\]/); ts=substr($0, 1, RLENGTH)
    if (ts in need && index($0, "@" need[ts]) == 0)
      print "  ledger: " ts " returns " need[ts] " but carries no @" need[ts] }
' "$V" "$F"
```

For V1, fail if white is under 55 percent, cobalt is over 15 percent, any `solid blue`
background appears, any yellow caption appears, or any yellow caption sits on a white
background.

For V2, fail if the plan is missing, generated plan rows do not equal prompt count, tier counts
or surface counts do not equal prompt count, ATMOSPHERIC exceeds 10 percent, cobalt mind
interiors exceed 10 percent, pure white cards exceed 15 percent, a source points forward or
nowhere, a non-plate delta is missing, or both V1 and V2 strings appear.

**The `@[timestamp]` checks are hard failures.** A reference that points forward, at itself, or
at a timestamp no prompt carries is a reference the tool cannot resolve, so it silently does
nothing and the inconsistency it was placed to fix ships anyway. A prompt carrying a reference
without the V2 SCENE REFERENCE LIMIT is worse than no reference at all: the tool attaches a
whole frame and the model copies its composition into a scene that was supposed to be new. A
ledger return with no `@[canonical]` in its prompt means the ledger is describing an intent the
file does not implement. Fix all three before reporting.

**The asset mix is advisory, exactly like scene density.** Print it, then judge it against the
script. A dense card and diagram act legitimately runs variant-heavy; a fast-cutting act
legitimately runs plate-heavy. What is not acceptable is a `VARIANT` share above its ceiling
that nobody looked at, because every surplus variant is a beat whose delta was too thin to
justify a plate, which is precisely the rule 18 defect. When `VARIANT` prints `REVIEW`, re-read
rule 18 against the offending beats and promote the ones with no legible delta to `PLATE`. If
the share is genuinely justified, say why in the Step 4 report.

Either version fails if a `---` line is malformed, doubled, leading, or trailing, or if any
other non-prompt line survives. For V2 it also fails if a break opens anything but a `PLATE`.

**Scene density is measured every run, but it is judged against the script rather than against
a threshold.** Print the figure and look at it. Inside the reference range, carry on. Outside
it, ask whether the script's own shape explains it: long sustained scenes justify a higher
number, a dense card and diagram act justifies a lower one, and either way the reason goes in
the Step 4 report. What does fail is a figure nobody examined, and the two defects the figure
exists to surface: unrelated frames inheriting one image over a long stretch, which is why
project 11's 13.3 prompts per break was rejected, and a chain cut so often that no build
survives to a payoff. If the number is unexplained rather than justified, re-read prompt rule
16, invert the default so every `PLATE` breaks unless whitelisted, and place them again.

Sourcing `.agents/bin/style-strings.sh` extracts the anchor and lock from
`.agents/rules/visual-style.md` at run time. Never hard-code them into a grep pattern here:
a hard-coded pattern can drift from the definition it is meant to be checking, which defeats
the purpose.

Prompt count must equal cue count. Exactly one version's anchor and lock counts must both equal
prompt count while the other version counts remain zero. The `comm` output must be empty except
for `@[name]`, which is part of the style lock. Fix anything that fails before reporting.

## Step 4 - Report and hand off

**The chat report carries everything the header used to.** Since the file is prompts only,
this is the only place the human gets it, so do not abbreviate it. Give the prompt count
against the cue count, the cast list with its `.jpeg` file names, any duplicate timestamps
with the file-naming workaround, the background budget table, the chain-break count together
with the **scene density figure and the longest inherited run**, the name-caption frames for
any real named people, and the first 3 prompts as a sample. At the target density there are
around 100 breaks, so give the density number and the act boundaries rather than annotating
every break. For V2, also report style version, chapter colors, motif, register totals, tier totals,
surface totals, new plates, variants, callbacks, CapCut-only beats, hero frames, longest planned
hold, and planned beats per minute. Also report **the asset mix as percentages against its
targets**, with a reason for anything marked `REVIEW`, and **the continuity ledger**: each
recurring non-cast object, its canonical timestamp, and how many `@[timestamp]` references
point back at it. Those two lines are what tell the human that the near-duplicate and
cross-scene-drift defects were actually addressed on this run. Then quote the selected version's GENERATION LINE from
`visual-style.md` verbatim so the human can copy it:

> Image prompts saved to `<path>`. The file is prompts only, so it imports directly.
>
> In the Flow chain workflow: bind every `characters/NAME.jpeg` under its exact `@TOKEN`, set
> the model and 16:9, then paste the whole file into IMAGE PROMPTS. The CREATE button must
> read `<N>` images, the same `<N>` as the prompt count above. The `<B>` `---` lines are chain
> breaks and generate nothing. Add this line to every generation:
> `<GENERATION LINE, verbatim>`
>
> One prompt at a time in Nano Banana, Gemini, Midjourney, DALL-E 3, or Stable Diffusion also
> works. There, attach only the `.jpeg` sheets for the `@` tokens each prompt contains, and
> carry the previous image forward as a reference except where a `---` says not to.
>
> **Pro tip:** generate the 3 or 4 frames where your main character is most visible first.
> If any drifts from the reference sheet, fix it before generating the rest. Drift
> compounds.
>
> Save each image to `scenes/` using the timestamp with its colon replaced by a hyphen,
> such as `[3:20]` to `[3-20].jpg`, then run **`/check`**.

## Guardrails

- Never skip a timestamp. One timestamp equals one prompt.
- Never output prompts out of chronological order.
- Never wrap a prompt across two lines. Downstream tools split this file on newlines, so a
  wrapped prompt becomes two broken prompts.
- Never write a header, a title, a cast line, or any commentary into the file. Every line is
  either a prompt, a `---` chain break, or one of the single blank separators between them.
  The file is imported wholesale, so a header line becomes a junk image.
- Never put a blank second line between prompts. Exactly one blank line separates them, and a
  chain break sits as blank, `---`, blank.
- Never cut the chain between a variant or a callback and the plate it points back to, and
  never inside a hold. Those beats exist because they inherit the frame before them.
- Never ship a break count that only covers act boundaries, and never ship one you have not
  looked at. Measure prompts per break, then judge it against what the script needs rather than
  against the reference range in rule 16, and report the reason whenever it sits outside.
- Never leave a real named person on screen as a generic doodle, and never caption their name
  more than once. The likeness is a `/cast` obligation; the caption and the introduction beat
  are this skill's.
- Never write a delta that is only an attribute change on something already drawn, and never
  write one below the scale it is drawn at. If the beat has no legible delta, it is a `PLATE`.
- Never solve a thin delta by dropping the generation or merging it into a neighbour. One cue
  is always one prompt, and `CAPCUT` beats are extra beats, never replacements.
- Never open a build chain on a plate that arrives full. Reserve the space the deltas will need.
- Never point an `@[timestamp]` forward, at itself, or at a timestamp no prompt carries.
- Never write an `@[timestamp]` without the V2 SCENE REFERENCE LIMIT in the same prompt. Without
  it the model copies the referenced frame's composition instead of just its object design.
- Never chain references. Every appearance points at the object's canonical first timestamp, not
  at the previous appearance, or the drift compounds hop by hop.
- Never aim an `@[timestamp]` at a cast member. The bound sheet holds characters, and a
  reference competes with it.
- Never ship a `VARIANT` share above its ceiling without looking at it. Every surplus variant is
  a beat whose delta was too thin to earn a plate.
- Never re-describe a cast member. Never invent a token.

## Self-improvement

Read `.agents/skills/scenes/references/memory.md` at the start of every run. Append when a
prompt shape generates badly, when a scene-holding decision was wrong, or when the user
corrects a background choice.
