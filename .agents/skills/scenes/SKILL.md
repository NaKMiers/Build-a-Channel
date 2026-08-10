---
name: scenes
description: Turn a timestamped HumanPrice transcript and locked cast into a visual plan plus one detailed image prompt per timestamp. Use for scenes, image prompts, visual planning, or prompts for every narration cue.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# scenes

Creates the HumanPrice visual plan and the generation-ready prompt file. This is the
largest text stage in the pipeline: one planned generated beat and one prompt for every
timestamped transcript cue, plus optional edit-only beats in the visual plan.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md` - the whole file, including palette, surfaces,
  density tiers, registers, frame grammar, pacing, and prohibited defaults
- `.agents/rules/cast-identity.md`
- `.agents/rules/file-formats.md` - the `prompts/visual-plan.md` and
  `prompts/image-prompts.md` contracts
- `.agents/rules/image-generation.md` - the Google Flow chain and the `---` break
- `.agents/skills/scenes/references/memory.md`
- the selected project's `prompts/character-prompts.md`; its cast table is the only
  legal source of `@TOKEN` handles

## Resolve one project and validate the gates

Resolve exactly one `projects/<n>-<slug>/`. Never mix inputs from two projects.

```bash
P="projects/<n>-<slug>"
T="$P/transcribes/transcript.md"
C="$P/prompts/character-prompts.md"

test -f "$T" && grep -cE '^\[[0-9]+:[0-5][0-9]\] .+' "$T"
test -f "$C" && grep -oE '@[A-Z][A-Z0-9_]*' "$C" | sort -u
grep -nvE '^\[[0-9]+:[0-5][0-9]\] .+' "$T"
awk '{stamp=$1; gsub(/\[|\]/,"",stamp); split(stamp,a,":"); now=a[1]*60+a[2]
      if(NR>1 && now<=prior) print NR ": non-increasing timestamp " $1
      prior=now}' "$T"
```

Hard gates:

- No transcript: stop and say to run `/transcript`.
- No cast file: stop and say to run `/cast`. Never invent a cast inline.
- Any nonblank transcript line outside `[M:SS] narration`: stop and repair the
  transcript stage first.
- Fewer than 20 cues: stop and report that the transcript looks incomplete. A normal
  8 to 12 minute HumanPrice recording usually has 180 to 320 cues, but the recording
  controls the final count.
- Duplicate or decreasing timestamps: stop and run `/transcript`; scene prompts must copy
  the transcript timestamps exactly and scene filenames cannot safely collide.
- If the cast uses `@YOU`, require `brand/PROTAGONIST.jpeg`. Stop if it is missing.

Inventory the source before planning:

```bash
wc -l "$T"
awk '{print $1}' "$T" | sort | uniq -d
grep -oE '@[A-Z][A-Z0-9_]*' "$C" | sort -u
```

Record the cue count and cast handles for the final report.

## Load the current style strings

```bash
source .agents/bin/style-strings.sh
test -n "$STYLE_STRING" && test -n "$GENERATION_STRING"
```

HumanPrice has one active visual system: `HumanPrice current`. Do not introduce legacy
visual-version names, retired channel identities, or retired character systems. Never
hard-code a second copy of either canonical string in this skill or in a validator.

## Step 1 - Read the transcript as an episode

Read the whole transcript before writing rows. Map the reveal ladder, not isolated lines:

- the familiar transaction and participant point of view;
- the hidden economic mechanism and behavioral engine;
- evidence, scale, boundary conditions, and counterargument;
- the full human price and the ending reframe.

When multiple cues split one spoken sentence, understand the full sentence first. Each cue
still receives its own beat, but its visual claim must be a concrete step in the sentence's
larger idea rather than a vague picture of a fragment.

Choose before writing:

- one visual thesis;
- the chapter color extension from the cast header;
- one recurring economic motif, such as a receipt, clock, cart, phone, price tag, scale,
  funnel, queue, or energy bar;
- 4 to 7 build chains and the base plate for each;
- where hard cuts require a Flow chain break;
- which factual labels or exact numbers must remain edit-only because generated text is
  unreliable.

## Step 2 - Write the visual plan first

Write `prompts/visual-plan.md` in the exact table format from `file-formats.md`. Finish and
verify the plan before writing prompt prose. It is cheaper and safer to rebalance table rows
than to rewrite hundreds of prompts.

Planning rules:

1. Create one generated row for every transcript cue in exact timestamp order. Optional
   `CAPCUT` rows may add an edit-only reveal but never replace a generated cue.
2. Give every row a unique beat ID. Give every new composition a unique plate ID.
3. Assign one register, shot, density tier, surface family, asset type, source, delta,
   motif, and text decision before prose begins.
4. Use only current enums from `file-formats.md`. `TRANSACTION` is especially useful for
   the visible exchange; `HYBRID` should make a human action and an economic mechanism
   readable in one frame.
5. Keep `ATMOSPHERIC` at or below 10 percent. Aim for roughly 40 percent `CLEAN` and 50
   percent `LAYERED`, adjusting honestly to the script.
6. Treat 35 to 45 percent new `PLATE` rows as a useful review band, not a quota. Use
   `VARIANT` rows for one-step builds and holds, and `CALLBACK` rows when an earlier image
   returns with changed meaning.
7. Every non-plate points backward to an existing source beat and names exactly one
   information-changing delta. `expression change` alone is not a delta. Name the visible
   change, such as `receipt length doubles` or `scale tips toward time`.
8. A plate and all of its variants keep the same surface, camera axis, cast placement,
   environment geometry, major props, palette, and line hierarchy. Change one meaningful
   element at a time.
9. Rotate registers and shot tasks after two or three beats unless a valid build chain is
   intentionally holding the composition. Avoid a whole section of medium shots.
10. Use `CLEAN` for a single idea, `LAYERED` for a mechanism with two to four explanatory
    elements, and `ATMOSPHERIC` only for an emotional turn that needs an environment.
11. Keep on-screen words optional, short, and non-load-bearing. Prefer one or two words;
    five is an exception. Mission-critical numbers, names, and labels belong in editing.
12. Give recurring abstract mechanisms one stable physical device. Reuse the same scale,
    funnel, queue, receipt, ring, or gauge instead of inventing a new metaphor every time.
13. Plan intentional negative space around the focal action. Density is the number of
    competing marks, not the number of ideas.
14. Give the ending a visual callback to the hook when the script supports it, then land
    the HumanPrice reframe on one simple final claim.
15. Mark chain breaks only before new `PLATE` rows whose composition must not inherit the
    previous frame. Never put a break inside a build, hold, variant, or callback lineage.

Target 180 to 320 meaningful visual states for a normal 8 to 12 minute episode, including
generated variants and useful edit-only builds. The recording and explanation control the
honest count; do not add decorative states to hit a number.

## Step 3 - Write the image prompts in internal chunks

Write `prompts/image-prompts.md`. The file is prompts only. Its first byte is `[` and it
contains only prompt lines, one blank separator between records, and legal `---` breaks.
Never write a header, title, cast list, source note, generation note, or commentary into it.

Work in internal chunks of about 25 cues. Do not pause for user approval between chunks.
Before each chunk after the first, re-read the last three prompts and the corresponding
plan rows so plate continuity, density, and prompt detail do not drift.

Every generated prompt must follow this order on one physical line:

```text
[M:SS] Narration cue context only, render none of these words: <exact narration text> <register, tier, surface, visual claim, composition, cast actions, props, lighting, negative space, text policy, and build delta> <STYLE_STRING> <GENERATION_STRING>
```

Prompt rules:

1. Copy the timestamp character for character from the transcript. Never re-pad, renumber,
   or silently remap it.
2. Copy the narration text after the timestamp exactly, introduced by `Narration cue
   context only, render none of these words:`. Derive the visual claim from that cue in
   context. The timestamp and narration are source context, never visible image text.
3. End with `STYLE_STRING` immediately followed by `GENERATION_STRING`, both copied
   verbatim from `.agents/bin/style-strings.sh`.
4. Name the row's register, density tier, and surface family explicitly. Use the canonical
   enum and surface wording from the current rules.
5. State one visual claim. Translate abstraction into a concrete human action, transaction,
   spatial mechanism, comparison, or stable recurring symbol.
6. Refer to cast members only by exact handles from the cast table. Put the `@TOKEN` at the
   start of that character's clause.
7. Never re-describe a cast member's face, hair, clothing, body proportions, or color lock.
   The bound reference sheet carries identity. Describe only action, expression, posture,
   position, interaction, and story-relevant props.
8. Never invent a token. If a genuinely recurring new character is required, stop and
   return to `/cast`. One-off background figures may be unnamed, minimal, and secondary.
9. A new `PLATE` prompt describes the complete composition. A `VARIANT` begins its scene
   clause with `Preserve the attached source plate` and names the one visible delta. A
   `CALLBACK` names the earlier plate and explains the changed meaning.
10. Keep the plate's surface family and composition stable through every variant. A variant
    prompt must still repeat the canonical surface-family wording so validation can count it.
11. Use saturated Toss blue only for `@YOU` or one semantic diagram signal. Olive indicates
    choices, systems, or positive economic emphasis. Terracotta indicates price, friction,
    urgency, or human cost. Do not flood generic crowds or backgrounds with brand blue.
12. Use generated text only when optional and short. Explicitly say `no generated labels or
    factual tiny text` when the meaning lives in editing.
13. Keep faces and hands readable at phone size, leave intentional negative space, and use
    soft directional lighting appropriate to the selected surface.
14. No photorealism, 3D render, CGI, realistic faces, anime, logos, watermarks, floating icon
    soup, decorative charts, wall of numbers, or literal coin mascot.
15. Never wrap a prompt across two lines. Downstream Flow parsing treats a wrapped line as a
    separate record.
16. Separate adjacent prompt records with exactly one blank line.
17. Insert a line containing exactly `---`, with one blank line above and below, when a new
    plate must not inherit the preceding frame. A break creates no prompt and no image.
18. Never break between a variant or callback and its lineage, never at the first or last
    line, and never place two breaks in a row.

## Step 4 - Verify mechanically

Run these checks before reporting. Fix every failure in this stage.

```bash
source .agents/bin/style-strings.sh
F="$P/prompts/image-prompts.md"
V="$P/prompts/visual-plan.md"
N=$(grep -c '^\[' "$F")
CUES=$(grep -cE '^\[[0-9]+:[0-5][0-9]\] .+' "$T")

printf 'cues: %s  prompts: %s\n' "$CUES" "$N"
test "$CUES" -eq "$N"

# Prompts only. Blank separators and exact chain breaks are the only exceptions.
head -c1 "$F"
grep -vE '^(\[|---$|$)' "$F"

# Every adjacent prompt pair must have a blank separator. Must print 0.
awk 'p ~ /^\[/ && $0 ~ /^\[/ {c++} {p=$0} END{print c+0}' "$F"
awk 'NR==1 && $0=="" {print "leading blank"}
     $0=="" && p=="" {print NR ": repeated blank"}
     {p=$0}
     END {if(p=="") print "trailing blank"}' "$F"

# Prompt timestamps must exactly match transcript timestamps and order.
diff <(awk '{print $1}' "$T") <(grep -o '^\[[0-9:]*\]' "$F")

# Every prompt preserves its exact narration source text.
while IFS= read -r cue; do
  timestamp=${cue%% *}
  narration=${cue#*] }
  grep -Fq "$timestamp Narration cue context only, render none of these words: $narration" "$F" || \
    printf 'missing exact narration context: %s\n' "$cue"
done < "$T"

# Every prompt carries the one current pair of canonical strings.
printf 'style: %s  generation: %s\n' \
  "$(grep -cF "$STYLE_STRING" "$F")" \
  "$(grep -cF "$GENERATION_STRING" "$F")"
test "$(grep -cF "$STYLE_STRING" "$F")" -eq "$N"
test "$(grep -cF "$GENERATION_STRING" "$F")" -eq "$N"

# No token outside the cast table.
comm -13 \
  <(grep -oE '@[A-Z][A-Z0-9_]*' "$P/prompts/character-prompts.md" | sort -u) \
  <(grep -oE '@[A-Z][A-Z0-9_]*' "$F" | sort -u)

# House-rule contamination checks.
grep -n "$(printf '\u2014')" "$F" && echo 'FAIL: em dash' || true
test "$(grep -c '^Visual style: HumanPrice current$' "$V")" -eq 1

# Chain-break shape: exact, separated, not leading, trailing, or doubled.
grep -c '^---$' "$F"
awk '{L[NR]=$0} END {for(i=1;i<=NR;i++) if(L[i]=="---") {
  if(i==1 || L[i-1]!="") print i ": break needs one blank line above"
  if(i==NR || L[i+1]!="") print i ": break needs one blank line below"
  if(i>2 && L[i-2]=="---") print i ": doubled break"
}}' "$F"

# Plan rows: generated rows equal prompts; all non-plates source a prior beat and one delta.
grep -c '^| B[0-9][0-9][0-9] ' "$V"
test "$(grep '^| B[0-9][0-9][0-9] ' "$V" | grep -vc ' | CAPCUT |')" -eq "$N"
awk -F'|' '
  /^\| B[0-9][0-9][0-9] / {
    for (i=2;i<=11;i++) gsub(/^ +| +$/, "", $i)
    beat=$2; asset=$8; source=$10; delta=$11
    if (asset != "PLATE" && (source == "-" || !(source in seen)))
      print "bad source at " beat ": " source
    if (asset != "PLATE" && delta == "-") print "missing delta at " beat
    seen[beat]=1
  }
' "$V"

# Every break must open a PLATE row.
awk -F'|' '
  NR==FNR {
    if ($0 ~ /^\| B[0-9][0-9][0-9] /) {
      t=$3; a=$8; gsub(/^ +| +$/, "", t); gsub(/^ +| +$/, "", a); asset[t]=a
    }
    next
  }
  {L[FNR]=$0}
  END {for(i=1;i<=FNR;i++) if(L[i]=="---")
    for(j=i+1;j<=FNR;j++) if(L[j] ~ /^\[/) {
      match(L[j], /^\[[0-9:]+\]/); t=substr(L[j],1,RLENGTH)
      if(asset[t] != "PLATE") print "break before " t " opens " asset[t]
      break
    }}
' "$V" "$F"
```

Also review, do not merely count:

- every plan timestamp matches its transcript cue;
- every prompt implements its plan row;
- register, shot, tier, surface, and cast choices remain coherent through the episode;
- `ATMOSPHERIC` stays at or below 10 percent;
- no build chain changes surface or composition accidentally;
- deltas do not collapse into repeated generic wording;
- every hard change of place, time, cast, or surface has a justified break;
- no break destroys a variant, callback, or hold;
- the first 15 seconds are visually faster than the mechanism sections;
- the ending pays off the visual thesis and human price.

Zero breaks in a multi-act episode is usually a failure. Excessive breaks are also a
failure because they discard useful inheritance. Use the judgment rule from
`image-generation.md`: break when bleed would hurt, keep the chain when inheritance helps.

## Step 5 - Report and hand off

Report:

- paths to `prompts/visual-plan.md` and `prompts/image-prompts.md`;
- cue count against prompt count;
- cast handles with their `.jpeg` filenames;
- chapter colors and recurring motif;
- register, tier, surface, asset, and CapCut totals;
- new plates, variants, callbacks, and build-chain count;
- chain-break count, each opening timestamp, and its reason;
- any honest deviation from the target bands;
- the first three prompts as a sample;
- confirmation that the Flow CREATE button must show the prompt count, because `---`
  records generate nothing.

Tell the user to bind each `characters/NAME.jpeg` under its exact `@TOKEN`, paste the whole
prompt file into IMAGE PROMPTS, and save generated images under `scenes/` with `:` replaced
by `-`, such as `[3:20]` to `[3-20].jpg`.

End with exactly: `Next: generate the scene images, then run /scene-polish.`

## Guardrails

- Never skip, reorder, or silently rewrite a transcript timestamp.
- Never generate image prompts before the cast is locked.
- Never write prompt prose before the visual plan is complete enough to verify.
- Never write a header or commentary into `image-prompts.md`.
- Never wrap a prompt or omit the single blank separator.
- Never invent or re-describe a cast identity.
- Never mix legacy channel instructions into current HumanPrice artifacts.
- Never use a chain break to hide a continuity problem that the plan should solve.

## Self-improvement

Read `references/memory.md` at the start of every run. Append only durable lessons about
prompt quality, planning, Flow inheritance, continuity, or validation. Do not append project
status, retired channel rules, or one-off production notes.
