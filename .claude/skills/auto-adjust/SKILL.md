---
name: auto-adjust
description: Post-render Auto Adjust for Why It Works HyperFrames sections. Use after Render or when the user asks to auto-adjust, audit, QA, automatically fix a rendered section, preserve manual Studio edits, apply Section 1/2 review lessons, improve WIT scale/placement/rhythm, reduce animation density, sync cue reveals to voiceover, protect WIT/text/subtitle layout, or prepare one selected rendered section for review; requires one explicit or unambiguous project and one explicit or unambiguous section, never All.
---

# Auto Adjust (Claude wrapper)

This is the Claude discovery wrapper for the **auto-adjust** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/auto-adjust/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/auto-adjust/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/auto-adjust/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/auto-adjust/SKILL.md` wins.
