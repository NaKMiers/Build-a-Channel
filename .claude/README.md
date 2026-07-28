# .claude - Claude compatibility layer

This project is shared by **Codex** and **Claude Code**. To avoid two diverging copies of
the rules, skills, and self-improving memory, there is exactly **one source of truth**,
and it lives under `.agents/`.

```text
.agents/
  rules/     the channel brain, read by both tools          (canonical)
  skills/    canonical skill definitions: SKILL.md + references/ + agents/openai.yaml
.claude/
  skills/    thin discovery wrappers that delegate to .agents/skills (this folder)
```

## How the two tools load instructions

| Concern | Codex | Claude |
| --- | --- | --- |
| Root instructions | `AGENTS.md` | `CLAUDE.md`, which imports `AGENTS.md` |
| Skill discovery | `.agents/skills/*/agents/openai.yaml` + `SKILL.md` | `.claude/skills/*/SKILL.md` wrapper |
| Skill logic + memory | `.agents/skills/*/SKILL.md` + `references/` | same canonical files, via the wrapper |
| Channel rules | `.agents/rules/` | `.agents/rules/` read directly |

## Why wrappers instead of symlinks

At the machine level (`~/.codex/skills` -> `~/.claude/skills`) skills can be mirrored with
symlinks because that directory is local and never committed. Inside a project that is
committed to git and may travel to Windows, symlinks are fragile, so the project mirror
uses thin wrapper files instead.

Claude only auto-discovers skills under `.claude/skills/`. Each wrapper carries the
matching `name` and `description` frontmatter so Claude can find and select the skill,
then delegates to the canonical `.agents/skills/<name>/SKILL.md` for the actual
instructions. Nothing else is duplicated: rules, and each skill's self-improving
`references/memory.md`, stay single-sourced under `.agents/`, so a lesson learned in a
Claude session and a Codex session lands in the same file.

## Keeping things in sync

Run the **skill-sync** skill, or `bash .agents/skills/skill-sync/gen-claude-wrappers.sh`,
whenever you add, edit, or remove a skill. It regenerates the wrappers from the canonical
definitions and reports orphans. It never deletes your work. Manual only.

Rules it enforces:

- Edit skill logic, workflow, and memory **only** under `.agents/skills/`.
- Root instructions stay single-sourced: edit `AGENTS.md`, `CLAUDE.md` imports it.
- A new canonical skill needs a matching wrapper here, plus `agents/openai.yaml` for
  Codex.
