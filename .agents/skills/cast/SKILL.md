---
name: cast
description: Derive the 2 to 6 entry character cast for a TossExplains video from its script, then write one reference sheet prompt per cast member into prompts/character-prompts.md. Solves character drift. Use when the user says "cast", "characters", "reference sheets", or "lock the cast".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# cast

Stage 3 of the TossExplains pipeline, and the one that prevents the channel's worst visual
failure. Without a locked cast, every generated image invents a slightly different person
and the video looks like it was drawn by five people. Here the cast is defined once, given
names, and every later image prompt refers to those names instead of re-describing the
character.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/mascot-toss.md` - **the whole file.** Toss's identity lock, the sheet
  template, the ABSOLUTELY NO TEXT block, and the resolved hand-shape conflict.
- `.agents/rules/visual-style.md` - the palette and the REFERENCE SHEET OPENING LINE
- `.agents/rules/file-formats.md` - the `prompts/character-prompts.md` section
- `.agents/skills/cast/references/memory.md`

## Preconditions

```bash
ls projects/<n>-<slug>/script_*.md
```

The script is required. The transcript is not. If there is no script, stop and say to run
`/script` first.

## THE CAST IS DERIVED, NEVER TEMPLATED

Read the actual script, find who is actually on screen in it, and build only those. **Two
scripts should almost never produce the same cast.** Do not carry a cast over from a
previous video and do not reach for a default set of characters.

- **There is no default ancestor.** A prehistoric figure appears **only if** the script's
  anthropology section is actually set in prehistory. If that section is about a modern
  Japanese office, a monastery, a village market, a WEIRD-versus-small-scale-society
  comparison, or a 1960s lab, then the character is an office worker, a monk, a market
  trader, a villager, or a lab subject. Not a caveman.
- **Never default to the early-Neolithic farmer, the brown tunic, the hoe, or the stalk of
  wheat.** Those belong to one specific example script. Era, occupation, clothing, and
  prop must all be re-derived every time.
- **No character exists to fill a slot.** If the script never puts a second person on
  screen, the cast is `YOU` plus a prop or a group. A 2-entry cast is better than an
  invented character.

## Step 1 - The derivation procedure, before writing anything

1. Scan the script and list every entity that is physically depictable on screen.
2. Keep only those appearing in **2 or more distinct moments**, or carrying the video's
   emotional weight. Drop the rest. One-off figures are handled as generic background
   figures by the `scenes` skill.
3. For each keeper, pull straight from the script: their era and setting, their role, the
   2 to 4 moments they appear in, the object they physically interact with most, and the
   emotions the script asks of them.
4. **Only then** write their sheet. Every visual decision must trace back to something in
   step 3.

## Step 2 - Cast selection rules

- Cast size is 2 to 6 entries. Fewer is better. Never exceed 6.
- Every cast list contains the viewer stand-in, always named `YOU`. This is the only
  mandatory entry and the character on screen most often. **`YOU` is always Toss**, whose
  design is fixed channel-wide and is NOT derived from the script. The only thing you
  decide for him is which costume the script's setting puts him in. Everything about
  derivation applies to the OTHER cast members, never to him.
- Everything else is conditional on the script. Common shapes, to recognize, not to fill
  in:
  - The figure carrying the anthropology section, whoever and whenever the script says
    that is: `HUNTER`, `MONK`, `VILLAGER`, `WORKER`, `ELDER`, `MOTHER`, `SOLDIER`,
    `TRADER`.
  - The other person in the modern scenes, if the script has one: `FRIEND`, `BOSS`,
    `STRANGER`, `PARTNER`.
  - A named researcher, only if the script describes their experiment in a way that puts
    them on screen: `DUNBAR`, `MILGRAM`, `ASCH`.
  - A recurring group. Treat a repeatedly used ring or crowd as ONE entry: `TRIBE`,
    `CROWD`, `CLASS`, `OFFICE`, `BAND`.
  - A personified concept or signature object that recurs: `PHONE`, `BRAIN`, `FIRE`,
    `MIRROR`, `CLOCK`.
- If the script names a person, use that name (`ALAN`, `MAYA`). Otherwise use the role the
  script gives them.

## Step 3 - Naming rules, strict

- One word, ALL CAPS, letters A to Z only. No spaces, hyphens, digits, or accents.
- Each name unique. The file name is exactly that name plus `.jpeg`: `YOU.jpeg`,
  `ALAN.jpeg`, `DOCTOR.jpeg`, `TRIBE.jpeg`.
- The reference token used everywhere afterwards is `@` plus the name.
- **Names are permanent for this video.** Never rename, never re-case, never add a new
  name after this stage. Once this file is written, the cast table is the single source of
  truth.

## Step 4 - Write the file

Path: `projects/<n>-<slug>/prompts/character-prompts.md`, shaped exactly as
`.agents/rules/file-formats.md` specifies.

**Part 1, the cast table.** The Era / setting column exists to force the derivation: if
you cannot point to the line in the script that puts that character in that time and
place, the character does not belong in the cast.

**Part 2, one reference sheet prompt per cast member**, each inside its OWN fenced code
block, immediately preceded by a bold label of the file name. One code block equals one
image generation, so never merge two characters into one block.

Build each sheet from the template in `.agents/rules/mascot-toss.md`: the opening line,
BODY CONSTRUCTION, RENDERING QUALITY, REFERENCE LAYOUT, ABSOLUTELY NO TEXT, CONSISTENCY,
NEGATIVE, plus that character's own CHARACTER, GARMENT, POSES, and PROP blocks.

Per-character requirements:

- **CHARACTER** is the full visual identity in one dense paragraph, with an exact hex color
  from the palette. Every choice justified by the script's own setting. Be decisive: this
  paragraph is the character's DNA and will be re-read by every later generation.
- **POSES and EXPRESSIONS** name the exact 4 and 4, taken from what THIS character actually
  does and feels in THIS script. Do not reuse a generic set and do not reuse another
  character's set. If the video is about social fear, the sheet needs embarrassed,
  watched, shrinking, relieved. If the character's script moments are all waiting and
  refreshing a screen, the poses are waiting and refreshing a screen.
- **PROP** is the object THIS script actually puts in their hands. If the script gives them
  no object, use a close-up of their hands and head instead. Never invent a prop, and
  never inherit one from another video.
- **Group entries** get a group sheet. **Prop entries** get 3 angles, 4 emotional face
  states, and 4 states of use. Both variations are specified in `mascot-toss.md`.
- **The `YOU` sheet** copies Toss's identity lock verbatim and writes ONLY the costume
  fresh. Include the instruction to attach `brand/MASCOT.jpeg` as a reference for that
  generation.

## Step 5 - Re-read before finishing

Re-read each sheet and check every visual detail against the script: era, clothing, prop,
expressions, poses. **If any detail came from habit rather than from the script, rewrite
it.** Then verify mechanically:

```bash
F="projects/<n>-<slug>/prompts/character-prompts.md"
grep -c '^```' "$F"                              # even number, 2 per character
grep -oE '@[A-Z]+' "$F" | sort -u                # tokens, all ALL CAPS single words
grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"

# 'mitten' as a POSITIVE instruction must be 0. Every sheet's NEGATIVE block says
# "no mitten hands", so a bare `grep -c mitten` counts the fix as the fault.
grep -oiE '(no|never|not) +mittens?|mittens?' "$F" | grep -civE '^(no|never|not) '

# every garment colour distinct, and nothing off palette or muted
for t in $(grep -oE '^\| @[A-Z]+' "$F" | tr -d '| @'); do
  printf '%-10s %s\n' "@$t" "$(sed -n "/^## $t.jpeg/,/^## [A-Z]*.jpeg/p" "$F" \
    | grep -oE '(hoodie|shirt|parka|tunic|robe|vest|wrap|coat|dress|casing ring)[^,]*\(#[0-9A-F]{6}\)' \
    | head -1)"
done
grep -oE '#[0-9A-F]{6}' "$F" | sort -u           # cross-check against the palette
grep -ciE 'muted|desaturated|washed.out|pale (grey|slate)' "$F"   # design language, aim for 0
```

The garment grep has to name the garment word, so **extend that alternation whenever a cast
introduces a new one.** A word it does not know prints an empty line, which looks like "no colour
assigned" rather than "the grep cannot see it", and a silent blank is how two characters end up
sharing a colour.

The design-language count is **not** expected to be 0 in a finished file: every NEGATIVE block
carries `no pale washed-out fills` and `no muted palette`, so a 6-entry cast reads 6. What must be
0 is any such word describing a garment positively. Check where the hits sit before acting.

Two expectations that differ from a naive count:

- **The `@YOU` block does NOT contain the REFERENCE SHEET OPENING LINE.** It is an edit prompt
  against `brand/MASCOT.jpeg` and opens with the preservation instruction instead. Expect that
  line in the other sheets only, so 5 in a 6-entry cast, not 6.
- **Every sheet needs `no pale washed-out fills` in its NEGATIVE.** A muted garment is the fault
  that got three separate sheets rejected in project 2. When you find one, audit all of them in
  the same pass.

## Step 6 - Report and hand off

Print only the cast table in chat, plus the list of `.jpeg` files to generate. Do not paste
the full sheet prompts into chat, they live in the file. Then:

> Cast locked in `<path>`.
>
> Generate one image per code block, attaching `brand/MASCOT.jpeg` for the `YOU` sheet,
> and save each as `characters/NAME.jpeg`.
>
> In your image tool: Nano Banana or Gemini take the sheets as reference images directly.
> Midjourney uses `--cref [sheet URL]`. ChatGPT or DALL-E 3 need "match the attached
> character reference exactly". Stable Diffusion uses the sheet as an IP-Adapter or
> reference-only ControlNet input.
>
> Next: **`/scenes`** once the transcript exists, or **`/thumbnail`** now.

## Guardrails

- Never exceed 6 cast entries. Never fewer than 2.
- Never let Toss play a second character. The figure carrying the script's other era is a
  genuinely different person with its own head shape, hair, build, and clothing.
- Never restyle Toss's head, hair, face, or proportions to suit a costume.
- Never add a cast member after this file is written. If a later stage genuinely needs
  one, say which line needs it and add it here with its own sheet first.
- Two characters must never be distinguishable by facial detail alone. Give each a
  different clothing color plus one silhouette difference.

## Self-improvement

Read `.agents/skills/cast/references/memory.md` at the start of every run. Append when a
sheet generates badly and you learn the wording that fixes it, when the user corrects a
derivation, or when an image model needs a new explicit negative.
