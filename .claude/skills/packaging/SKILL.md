---
name: packaging
description: Create or update YouTube packaging for a Why It Works video project. Use when the user asks for Packaging, title and thumbnail, YouTube description, upload metadata, tags, hashtags, thumbnail concepts, thumbnail images, A/B thumbnail testing, A/B title testing, or packaging; this is the packaging step that runs after caption and requires completed 00-topic-intake.md, 01-research-pack.md, and 02-script.md (it does not require voiceover/render to be finished, but its recommended position is after caption so it can also package shorts and use real chapters). Produces 5 LOCKED title+thumbnail A/B pairs for the main video (title N is coupled to thumbnail N — editing one rewrites the other), plus the YouTube description and tags; when built shorts are available it also creates one title, description, and thumbnail per short. Writes everything to ONE file, projects/<slug>/output/packaging.md (titles, descriptions, AND the thumbnail generation prompts folded in), and saves all thumbnail images under projects/<slug>/output/thumbnails/. It no longer creates 03-packaging.md or a separate PROMPTS.md.
---

# Packaging (Claude wrapper)

This is the Claude discovery wrapper for the **packaging** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/packaging/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/packaging/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/packaging/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/packaging/SKILL.md` wins.
