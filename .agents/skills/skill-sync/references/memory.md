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

- Phantom skill in docs (a skill named in `AGENTS.md`/`README.md`/`current-state.md`/
  `.agents/skills/README.md` but with no `.agents/skills/<name>/` directory and no wrapper):
  ask the user before acting. On 2026-06-18 the user chose "remove stale references" for
  `wiw-take-note` — strip the bullet/mention from every doc so all docs match the real
  canonical inventory, rather than scaffolding the skill. Confirm scope before building.
- When removing such references, sweep ALL docs (`AGENTS.md`, `README.md`,
  `.agents/skills/README.md`, `.agents/_shared/channel/current-state.md`) — the phantom
  tends to appear in several at once. `CLAUDE.md` may already be clean.
