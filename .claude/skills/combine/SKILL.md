---
name: combine
description: Project-level assembly + export step. Combine all completed section renders of one Why It Works video project into a single unified HyperFrames preview on localhost:1000 with one continuous combined voiceover, then export the final full video (MP4) to the project's output/ folder. Use when the user asks to combine, combine sections, unify, assemble the full video, build the full render, merge sections into one video, make the whole video, export the final video, or run on localhost:1000. Requires every section already rendered (one preview per script section); refuses to run if any section is missing. Reuses the existing per-section renders and assets and only assembles them - it never re-renders, edits, or creates section content. The final video is rendered through renders/ as a staging area, then moved to output/, and renders/ is removed if it is left empty. Requires one project; use the project the user names, or smart-select the unambiguous active project, otherwise ask.
---

# Combine (Claude wrapper)

This is the Claude discovery wrapper for the **combine** skill. The canonical
definition - full purpose, gates, build mechanics, workflow, self-check, and
self-improving memory - lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/combine/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/combine/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/combine/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/combine/SKILL.md` wins.

Key guarantees this skill must honor:

- Run only when ALL sections of the chosen project are rendered (refuse otherwise).
- Reuse existing section renders + assets; never change or create section content.
- Always run the unified preview on `localhost:1000`.
- Export the final video (MP4) to `projects/<slug>/output/`: render into `renders/` as staging, then MOVE the result to `output/<slug>.mp4`. After the move, remove `renders/` only if it is left empty; never touch files in `renders/` this run did not create. On render failure, leave `renders/` untouched and report.
- `output/` is the single home for all final deliverables.
