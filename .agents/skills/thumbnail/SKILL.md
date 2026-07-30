---
name: thumbnail
description: Create self-contained cinematic TossExplains thumbnail prompts from a finished script and cast. Supports one or more copyable chat prompts and the default five-prompt prompts/thumbnail-prompts.md workflow. Use when the user asks for a thumbnail, thumbnail prompt, thumbnail concept, alternate thumbnail, or YouTube packaging image.
---

# thumbnail

Create high-click thumbnail prompts from the video's strongest drawable moments. Preserve
the TossExplains cast while using the thumbnail-only cinematic style.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/thumbnail-rules.md`
- `.agents/skills/thumbnail/references/style-spec.json`
- `.agents/rules/visual-style.md` for cast identity and palette context, not its scene prompt
  STYLE ANCHOR or STYLE LOCK
- `.agents/rules/file-formats.md`
- `.agents/skills/thumbnail/references/memory.md`

Never require competitor thumbnails, research thumbnails, or external style images. The
style specification is self-contained.

## Preconditions

```bash
P="projects/<n>-<slug>"
ls "$P"/script_*.md
grep -oE '@[A-Z]+' "$P"/prompts/character-prompts.md | sort -u
```

The script and cast file are required. The transcript is not. If the cast file is missing,
stop and say to run `/cast`.

## Step 1 - Determine the requested output

Follow the user's explicit count and destination:

- `one prompt`, `another one`, or a number: create exactly that many.
- `in chat`, `block to copy`, or equivalent: return prompts in fenced text blocks and do
  not write a file.
- `save`, `update the prompts`, or no destination: write the default five prompts to
  `prompts/thumbnail-prompts.md`.

The saved artifact always contains exactly five prompts. If the user requests fewer than five
and also asks to save them, return them in chat unless they explicitly ask to replace the
five-prompt artifact with an incomplete set.

## Step 2 - Mine the script

Read the full script and record:

- physical objects, animals, places, and actions
- numbers and useful comparisons
- the opening physical situation
- the named experiment or mechanism made visible
- the ancestral scene
- the modern-versus-ancestral contrast
- the strongest consequence or counterintuitive fact
- the video title, so the headline does not repeat it

If the script has no drawable physical problem, stop and explain that the script needs a
stronger visual hook.

## Step 3 - Draft concepts before prompts

For every requested prompt, define:

1. headline
2. main character
3. dominant emotion
4. visible physical problem
5. supporting subject
6. setting
7. warm light source
8. unresolved moment

Run the rejection gate in `thumbnail-rules.md`. Rewrite any concept that fails.

Headline rules:

- 1 to 4 uppercase words, with 2 to 3 preferred
- one straight line at the top
- a second hook, never a restatement of the title
- connected to something visible
- question or short statement
- no abstract jargon or complete explanation

When creating multiple concepts, use different script moments. Default to single cinematic
stories. Use a split comparison only for a real numeric, era, temperature, or state contrast.

## Step 4 - Build each prompt

Use the single-scene or split template in `thumbnail-rules.md`. Fill every slot with script
and cast details.

Every prompt must:

- open with `Create a beautiful, high-impact YouTube thumbnail illustration in 16:9 format,
  1280x720.`
- reference only cast tokens whose project sheets will be attached
- preserve attached character identity exactly
- render one exact headline in large yellow type at the top
- reserve the top 22 percent as the darkest and least cluttered zone
- show one dominant emotional face and one visible physical problem
- capture the instant before the consequence
- use a cool environment and one warm visible light source
- use expressive doodle characters inside a richly painted cinematic 2D environment
- allow controlled gradients, soft shadows, painted texture, and atmospheric depth
- leave the bottom-right corner visually quiet
- render no extra text, logo, or watermark
- reject photorealism, 3D, anime, generic stock art, flat lighting, and empty backgrounds

Do not add the scene STYLE ANCHOR, STYLE LOCK, or GENERATION LINE. They prohibit the
thumbnail-only depth and lighting.

## Step 5A - Chat-only output

For each prompt:

1. Outside the code block, list the exact `characters/NAME.jpeg` files to attach.
2. State that no competitor or research images are needed.
3. Put only the complete generation prompt inside one fenced `text` block.

Do not write or update `thumbnail-prompts.md`.

When the user says `another one`, select a different script moment, headline, physical
problem, and composition from the previous concept.

## Step 5B - Saved five-prompt artifact

Write:

`projects/<n>-<slug>/prompts/thumbnail-prompts.md`

The file contains exactly five complete unbroken prompt lines separated by exactly one blank
line. No header, title, labels, attachment directions, file names, dimensions, or commentary.
Human-only attachment instructions remain in chat.

## Step 6 - Verify a saved artifact

```bash
F="$P/prompts/thumbnail-prompts.md"
wc -l < "$F"                                                        # 9
grep -cve '^$' "$F"                                                # 5
grep -c '^$' "$F"                                                  # 4
grep -c '^Create a beautiful, high-impact YouTube thumbnail' "$F"  # 5
grep -c 'Reserve the top 22 percent' "$F"                          # 5
grep -c 'very thick smooth black outline' "$F"                     # 5
grep -c 'richly painted cinematic 2D' "$F"                         # 5
grep -c 'bottom-right corner visually quiet' "$F"                  # 5
grep -c 'render no other text' "$F"                                # 5

# all must be 0
grep -ciE 'competitor thumbnail|research thumbnail|style reference image' "$F"
grep -ciE 'no gradients, no shadows, no textures|educational YouTube explainer doodle style' "$F"
grep -cE '^#|^\[thumb-|^Cast:|^Attach only|^Add the channel logo' "$F"
grep -n "$(printf '\u2014')" "$F"
```

Also verify:

- every `@TOKEN` exists in `character-prompts.md`
- every headline is uppercase and no more than four words
- each prompt names a different script moment
- no more than one concept uses a split comparison unless the script strongly justifies it
- no leading, trailing, or consecutive blank lines

## Step 7 - Handoff

For a saved set, list the headline and attachment files for each concept. Recommend the
strongest one and explain the choice in one sentence.

Tell the user:

- attach only the named project character sheets
- no competitor or research images are needed
- export at 1280x720 and under 2 MB
- add the channel logo in an editor at bottom-left
- test at 120 pixels wide
- if the model garbles the headline, regenerate the art without text and add the headline
  in an editor

Save generated candidates as `outputs/thumbnail-1.jpg` through `thumbnail-5.jpg`. Rename the
winner with an `-accepted` suffix, then run `/check`.

## Self-improvement

After the user reports a generated result, append only the durable lesson to
`references/memory.md`: accepted concept, failed concept, and observable failure mode. Do
not add external image dependencies or source-specific style references.
