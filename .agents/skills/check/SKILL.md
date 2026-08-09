---
name: check
description: Validate a HumanPrice project against research, script, transcript, cast, scene, metadata, and thumbnail contracts, then report failures and the next pipeline step. Use to check, validate, audit, or find what a project is missing.
allowed-tools:
  - Bash
  - Read
  - Glob
---

# check

Read-only validator for one HumanPrice project.

## Read first

- every file in `.agents/rules/`
- `.agents/skills/check/references/memory.md`

## Resolve and inspect

Resolve exactly one `projects/<n>-<slug>/`. Never create or repair files during a check.
Classify each artifact as `PASS`, `FAIL`, `WARN`, or `NOT READY`.

## Checks

### Research

- `research/research-brief.md` exists before a script.
- 6 to 10 sources and at least 3 primary or official sources are declared.
- Claims carry `FACT`, `ESTIMATE`, `INFERENCE`, or `ILLUSTRATION` labels.
- Exact title or thumbnail numbers have explicit clearance.

### Script

- Exactly one `script_*.md` exists.
- Word count is 1,150 to 1,850, with 1,250 to 1,750 preferred.
- No headings, timestamps, citations, stage directions, or em dash character appear in
  spoken narration.
- The four HumanPrice layers and 14-step reveal ladder are represented.
- Material claims and numbers exist in the research brief.

### Transcript and audio

- Every nonblank transcript line matches `[M:SS] narration`.
- Timestamps are strictly increasing and the final time is plausibly 8 to 12 minutes.
- Multi-part audio, when present, follows the transcript skill's combined-audio contract.

### Cast and scenes

- Cast has 2 to 6 unique handles and follows `cast-identity.md`.
- `@YOU` uses `brand/PROTAGONIST.jpeg` when required.
- One image prompt exists for every transcript timestamp in exact order.
- Every prompt contains the exact current style and generation strings.
- Register, tier, surface, and build-chain rules are valid.

### Metadata and thumbnail

- Metadata has five title candidates, one recommendation, 4 to 6 chapters, 12 to 20
  hashtags, and 25 to 40 tags.
- Titles use the HumanPrice series logic and no uncleared number.
- Thumbnail file has five distinct concepts, zero to four words of copy, at least one
  human anchor, and no unsupported numeric claim.

### Active-system contamination

Fail any current project artifact that refers to a retired channel identity, a removed
character system, a superseded editorial framing, or a legacy visual version. Historical
competitor research is outside this check.

## Report

Give a compact table with artifact, status, and evidence. Then list blocking failures in
pipeline order and name exactly one next command. Do not claim a complete project when a
downstream artifact is merely not ready.

## Self-improvement

Append only recurring validator blind spots to `references/memory.md`.
