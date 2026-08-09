---
name: thumbnail
description: Create five self-contained HumanPrice thumbnail prompts from a finished script, research brief, and cast. Use for thumbnails, thumbnail concepts, cover art prompts, click-through packaging, or A/B concepts.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# thumbnail

Produces five conceptually different thumbnail prompts. It does not generate images.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md`
- `.agents/rules/cast-identity.md`
- `.agents/rules/thumbnail-rules.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/thumbnail/references/memory.md`

## Inputs

Resolve one project and require `script_*.md`, `research/research-brief.md`, and
`prompts/character-prompts.md`. Use `outputs/metadata.md` if it exists so thumbnail copy
complements rather than repeats the recommended title.

## Create five concepts

Use the five angles in `thumbnail-rules.md`: opening transaction, unit economics,
behavioral mechanism, hidden system, and final human price. Each concept must contain one
human decision, one economic object, and one visual contradiction.

For every concept provide:

- concept name and one-sentence click hypothesis;
- optional copy of zero to four words;
- exact cast handles and facial reaction;
- foreground, midground, background, and negative-space plan;
- palette emphasis and lighting;
- the complete generation prompt;
- a one-line mobile legibility check.

At least one concept uses `@YOU`; another may use the most specific supporting character.
Every exact number must be cleared for thumbnail use in the research brief. Every prompt
must include the exact style and generation strings from `visual-style.md`.

Write `prompts/thumbnail-prompts.md` using `file-formats.md`. Recommend one concept based
on clarity and curiosity, not personal taste alone.

## Self-improvement

Record a lesson in `references/memory.md` only after explicit feedback or performance
data. Store evidence, not guesses.
