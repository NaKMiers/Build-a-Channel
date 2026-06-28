---
name: skill-sync
description: Manually synchronize the Codex (.agents) and Claude (.claude) configuration for the Why It Works workspace so both tools stay in lockstep. Use when the user asks to sync skills, sync Codex and Claude, reconcile skill wrappers, sync AGENTS.md and CLAUDE.md, propagate a skill improvement to the other tool, after creating editing or deleting a skill, or after editing a root instruction file; it reconciles the skill inventory, regenerates or updates Claude delegating wrappers and Codex openai.yaml from the canonical .agents/skills definitions, syncs name and description frontmatter plus reference lists, aligns the shared sections and skill lists of AGENTS.md and CLAUDE.md, and reports orphans or conflicts for the user to resolve instead of deleting work; manual only, never auto-run.
---

# Skill Sync (Claude wrapper)

This is the Claude discovery wrapper for the **skill-sync** skill. The canonical
definition - full purpose, source-of-truth model, workflow, templates, and self-improving
memory - lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/skill-sync/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/skill-sync/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/skill-sync/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/skill-sync/SKILL.md` wins.
