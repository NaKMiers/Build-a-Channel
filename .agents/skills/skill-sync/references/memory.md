# Skill Sync — Memory

Operational lessons for keeping Codex (`.agents/`) and Claude (`.claude/`) in lockstep.
This memory is about the sync tooling only; it never holds channel strategy.

## Model (current)

- Single source of truth = `.agents/skills/<name>/` (logic + `references/`).
- `.claude/skills/<name>/SKILL.md` = delegating wrapper (frontmatter + delegation only).
- Codex discovery = `.agents/skills/<name>/agents/openai.yaml`.
- Root docs `AGENTS.md` (Codex) and `CLAUDE.md` (Claude) mirror shared sections.

## Things that can drift (watch these)

- Wrapper `name`/`description` vs canonical frontmatter.
- Wrapper reference bullets vs files actually in `references/`.
- Missing `agents/openai.yaml` for a new canonical skill.
- A canonical skill with no Claude wrapper, or a wrapper with no canonical skill.
- Skill-list bullets in `AGENTS.md` vs `CLAUDE.md` vs the real inventory.

## Exemptions (do not require wrappers / do not delete)

- `browse` skill (`.agents/skills/browse/`): vendored from gstack, git-ignored, optional.

## Resolution rules learned

- (none yet — add when the user corrects a conflict resolution)
