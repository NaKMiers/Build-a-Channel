---
name: voiceover
description: Create or update step 3 section voiceover for a Why It Works video project. Use when the user asks for Voiceover, section voiceover, generate audio for a script section, create narration audio, run step 3, or create all section voiceovers; requires completed project 00-topic-intake.md, 01-research-pack.md, and 02-script.md first, asks which script section to generate with All as the first option, then writes only the project's 03-voiceover.md plus section-local files under voiceover/.
---

# Voiceover (Claude wrapper)

This is the Claude discovery wrapper for the **voiceover** skill. The canonical
definition - full purpose, workflow, output format, and self-improving memory - lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/voiceover/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/voiceover/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/voiceover/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/voiceover/SKILL.md` wins.
