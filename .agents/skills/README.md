# Skills

This folder stores executable project-local Codex skills.

## Existing Skills

- [WIW Take Note](wiw-take-note/SKILL.md)
  Captures useful review and production feedback into the right project memory files.

## Future Skills

The sequential video-production skills are intentionally not created in this refactor.

When the user asks for the skill-creation phase, create skills for the 10-step lifecycle:

1. topic intake
2. research pack
3. script draft
4. voice revision and voiceover
5. title and thumbnail
6. visual plan
7. HyperFrames build
8. review
9. upload
10. self-learning

Each future skill should read from `.agents/_shared/`, write to `projects/<slug>/`, and keep skill-specific memory inside its own skill folder when useful.
