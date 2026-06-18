---
name: research-pack
description: Create or update the step 1 research pack for a Why It Works video project. Use when the user asks for research pack, research step, evidence pack, source gathering, reference research, factual grounding, visual references, or step 1 of the Why It Works video workflow; requires a completed project 00-topic-intake.md first, stops and asks for Topic Intake if it is missing, reads the shared channel brain, browses web or YouTube for credible sources and visual/reference evidence, then writes only the project's 01-research-pack.md file.
---

# Research Pack (Claude wrapper)

This is the Claude discovery wrapper for the **research-pack** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/research-pack/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/research-pack/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/research-pack/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/research-pack/SKILL.md` wins.
