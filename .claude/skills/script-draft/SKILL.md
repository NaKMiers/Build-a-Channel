---
name: script-draft
description: Create or update the step 2 sectioned script draft for a Why It Works video project. Use when the user asks for script draft, write the script, draft video script, sectioned script, script step, or step 2 of the Why It Works workflow; requires completed project 00-topic-intake.md and 01-research-pack.md first, stops and asks for Topic Intake or Research Pack if either is missing, reads the shared channel brain, then writes only the selected project's 02-script.md with a sectioned learner-friendly no-face explainer script.
---

# Script Draft (Claude wrapper)

This is the Claude discovery wrapper for the **script-draft** skill. The canonical
definition - full purpose, workflow, output format, and self-improving memory - lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/script-draft/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/script-draft/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/script-draft/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/script-draft/SKILL.md` wins.
