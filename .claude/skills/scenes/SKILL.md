---
name: scenes
description: Turn a timestamped HumanPrice transcript and locked cast into a visual plan plus one detailed image prompt per timestamp. Use for scenes, image prompts, visual planning, or prompts for every narration cue.
---

# Scenes (Claude wrapper)

This is the Claude discovery wrapper for the **scenes** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/scenes/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/scenes/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/scenes/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/scenes/SKILL.md` wins.
