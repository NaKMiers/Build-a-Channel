# .claude - Claude compatibility layer

This workspace is shared by **Codex** and **Claude**. To avoid two diverging copies of
the channel brain and self-improving skill memory, there is exactly one source of truth:

```text
.agents/
  _shared/   channel brain + reusable production systems + assets   (canonical)
  rules/     operating rules for all agents and skills              (canonical)
  skills/    canonical skill definitions: SKILL.md + references/    (canonical)
.claude/
  skills/    thin discovery wrappers that delegate to .agents/skills (this folder)
```

## How the two tools load instructions

| Concern              | Codex                         | Claude                                  |
| -------------------- | ----------------------------- | --------------------------------------- |
| Root instructions    | `AGENTS.md`                   | `CLAUDE.md`                             |
| Skill discovery      | `.agents/skills/*/agents/openai.yaml` + `SKILL.md` | `.claude/skills/*/SKILL.md` (wrapper)   |
| Skill logic + memory | `.agents/skills/*/SKILL.md` + `references/` | same canonical files, via the wrapper   |
| Channel brain        | `.agents/_shared/`            | `.agents/_shared/` (read directly)      |

## Why wrappers instead of a full clone

Claude only auto-discovers skills under `.claude/skills/`. Each wrapper here carries the
matching `name` + `description` frontmatter so Claude can find and select the skill, then
delegates to the canonical `.agents/skills/<name>/SKILL.md` for the actual instructions.

Nothing else is duplicated. The channel brain, rules, binary assets, and each skill's
self-improving `references/memory.md` stay single-sourced under `.agents/`, so lessons
learned in a Claude session and a Codex session land in the same place.

## Keeping things in sync

Run the **skill-sync** skill (canonical: `.agents/skills/skill-sync/`) whenever you add,
edit, or remove a skill, or edit a root doc. It reconciles the inventory, wrapper
frontmatter, reference lists, `openai.yaml`, and the shared sections of `AGENTS.md` /
`CLAUDE.md`, and reports orphans/conflicts instead of deleting work. It is manual only.

The rules it enforces, for reference:

- Edit skill logic, workflow, and memory **only** under `.agents/skills/`.
- If you change a skill's `name` or `description` in `.agents/skills/<name>/SKILL.md`,
  copy the new frontmatter into the matching `.claude/skills/<name>/SKILL.md` wrapper.
- If you change the startup routine or workflow rules, update both `AGENTS.md` and
  `CLAUDE.md`.
- New canonical skill → add a matching wrapper here and a bullet in `CLAUDE.md`.
