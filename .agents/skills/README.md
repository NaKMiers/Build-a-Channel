# Skills

This folder stores executable project-local Codex skills.

## Existing Skills

- [Browse](browse/SKILL.md)
  Project-local vendored gstack browse skill for web and YouTube reference research when global gstack skills are missing.

- [Topic Intake](topic-intake/SKILL.md)
  Generates scored next-video angle candidates, reads the shared channel brain, and keeps topic-intake-specific memory.

- [Research Pack](research-pack/SKILL.md)
  Creates step 2 evidence packs for selected video projects, including sources, explanation spine, visual reference leads, and fact-safety notes.

- [Script Draft](script-draft/SKILL.md)
  Creates step 3 sectioned working scripts from a selected project's topic intake and research pack.

- [WIW Take Note](wiw-take-note/SKILL.md)
  Captures useful review and production feedback into the right project memory files.

## Remaining Future Skills

`Topic Intake`, `Research Pack`, and `Script Draft` are the first sequential video-production skills.

When the user asks for the next skill-creation phase, create the remaining skills for the 10-step lifecycle:

1. voice revision and voiceover
2. title and thumbnail
3. visual plan
4. HyperFrames build
5. review
6. upload
7. self-learning

Each future skill should read from `.agents/_shared/`, write to `projects/<slug>/`, and keep skill-specific memory inside its own skill folder when useful.
