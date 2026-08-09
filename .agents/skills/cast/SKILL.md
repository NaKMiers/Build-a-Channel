---
name: cast
description: Derive the 2 to 6 character cast for a HumanPrice episode and write reference-sheet prompts with a stable recurring protagonist. Use for cast, characters, character sheets, or locking visual identities from a finished script.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# cast

Builds the visual cast after the narration is finished.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md`
- `.agents/rules/cast-identity.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/cast/references/memory.md`

## Inputs

Resolve one project and read its single `script_*.md`. If
`research/research-brief.md` exists, use it to avoid visually overstating claims.

## Select the cast

Choose 2 to 6 entries whose roles are necessary to the story. Include `@YOU` whenever
the audience participates in the behavior. Supporting roles may include a worker,
partner, seller, platform operator, expert, or observer. Do not turn a company, market,
or coin into a cute mascot.

If `brand/PROTAGONIST.jpeg` exists, state that it is the locked reference for `@YOU`. If
it does not, include the complete creation prompt from `cast-identity.md` first and add a
blocking note that this reference must be generated and saved before scene generation.

## Write prompts

For each entry, define the narrative role, identity lock, turnaround views, six useful
expressions, three story-specific poses, and story props. Include a scale lineup when
characters share frames. Every prompt must be self-contained and end with the exact style
and generation strings from `visual-style.md`.

Write `prompts/character-prompts.md` using `file-formats.md`. Do not generate images.

## Completion

Report the cast handles and saved path. If the protagonist reference is missing, make that
the only prerequisite. Otherwise say: `Next: run /scenes or /thumbnail.`

## Self-improvement

Append only durable character-consistency lessons to `references/memory.md`.
