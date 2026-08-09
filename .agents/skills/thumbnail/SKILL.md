---
name: thumbnail
description: Create five self-contained, reference-backed HumanPrice thumbnail prompts from a finished script, research brief, and cast. Every prompt binds the bundled finance-board image as its dominant style and layout-density reference. Use for thumbnails, thumbnail concepts, cover art prompts, click-through packaging, or A/B concepts.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# thumbnail

Produces five conceptually different thumbnail prompts. It does not generate images.
Every prompt binds the bundled finance-board asset as Image 1 so the downstream image
generator receives the approved reference instead of reconstructing the style from prose.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md`
- `.agents/rules/cast-identity.md`
- `.agents/rules/thumbnail-rules.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/thumbnail/references/memory.md`
- `.agents/skills/thumbnail/references/style-spec.json`

## Required reference asset

Require this file before writing any prompt:

`.agents/skills/thumbnail/assets/finance-board-reference.jpg`

Stop if it is missing or is not a readable 16:9 image. Treat it as Image 1 and the
dominant style and layout-density reference. Character sheets remain identity references
and never replace Image 1.

Include this exact binding sentence in every generated prompt line:

`Use .agents/skills/thumbnail/assets/finance-board-reference.jpg as Image 1, the dominant finance-board style and layout-density reference. Match its oversized black two-line headline, thin red underline, bright white ground, detailed central economic environment, small handwritten edge callouts, thin arrows, hand-inked linework, and dense-center-with-white-margins hierarchy. Do not copy its hardware-store subject, wording, logo, branded objects, or exact composition.`

## Inputs

Resolve one project and require `script_*.md`, `research/research-brief.md`, and
`prompts/character-prompts.md`. Use `outputs/metadata.md` if it exists so thumbnail copy
complements rather than repeats the recommended title.

## Create five concepts

Use the five angles in `thumbnail-rules.md`: opening transaction, unit economics,
behavioral mechanism, hidden system, and final human price. Each concept must contain one
human decision, one economic object, and one visual contradiction.

Apply the default finance-board system in `thumbnail-rules.md` to every concept. Each
prompt has a bright white or warm-paper board, an oversized four-to-nine-word top
headline with one terracotta underline, a detailed coherent central transaction
environment, and four to six short handwritten margin callouts connected by thin arrows.
The headline must be either a series or topic statement such as `THE ECONOMICS OF
TIPPING`, or a full curiosity or consequence question such as `WHY DOES TIPPING FEEL
REQUIRED?`. Never use a one-word headline or an elliptical two-to-three-word fragment.
Change the claim and transaction across the five concepts, not the channel's thumbnail
grammar.

The approved treatment follows Image 1: a bold two-line-or-fewer black headline, one long
red underline, a richly detailed central business or transaction scene, small characters
inside that system, and handwritten economic callouts around the margins. Concentrate
detail in the center while keeping clean white zones around callouts. Avoid sparse icon
bubbles, oversized character portraits, glossy 3D rendering, and unrelated clutter.

For every concept provide:

- concept name and one-sentence click hypothesis;
- the mandatory four-to-nine-word top headline, in no more than two lines;
- exact cast handles and facial reaction;
- central-environment density and negative-space plan;
- top headline, underline, central transaction, and margin-callout plan;
- palette emphasis and lighting;
- the complete generation prompt;
- a one-line mobile legibility check.

At least one concept uses `@YOU`; another may use the most specific supporting character.
Every exact number must be cleared for thumbnail use in the research brief. Every prompt
must include the exact style and generation strings from `visual-style.md`.

Use Image 1 as the approved reference for hierarchy, density, linework, annotation style,
and central-scene emphasis. Do not borrow its subject, logo, name, character, branded
object, wording, or exact composition.

Write `prompts/thumbnail-prompts.md` using `file-formats.md`. Keep each complete prompt,
including the exact Image 1 binding sentence, on one physical line. Recommend one concept
in chat based on clarity and curiosity, not personal taste alone.

## Self-improvement

Record a lesson in `references/memory.md` only after explicit feedback or performance
data. Store evidence, not guesses.
