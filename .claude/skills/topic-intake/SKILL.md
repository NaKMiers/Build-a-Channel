---
name: topic-intake
description: Generate and evaluate next-video topic ideas for the Why It Works YouTube channel, sourced from what the world is ACTUALLY curious about right now. Use when the user asks for topic intake, next video ideas, trending topics, raw topic candidates, scored video angles, or step 0 of the Why It Works workflow. It reads the shared channel brain, BROWSES the web for trending / high-interest topics (Google Trends, high-view recent videos, search and news interest) and gathers real EVIDENCE of demand for every candidate (never fabricated), then shapes ideas into angle packages scored for an A2–C1 English-learner audience whose advantage is "interesting English" (entertainment-first so learners stay and learn). Optionally writes a project topic-intake file when a candidate is chosen.
---

# Topic Intake (Claude wrapper)

This is the Claude discovery wrapper for the **topic-intake** skill. The canonical
definition - full purpose, workflow, output format, and self-improving memory - lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/topic-intake/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/topic-intake/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/topic-intake/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/topic-intake/SKILL.md` wins.
