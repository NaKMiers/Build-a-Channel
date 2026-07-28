# skill-sync - memory

Self-improving notes for keeping the two-tool mirror honest. Single canonical copy.

## The contract

Nine canonical skills under `.agents/skills/`, nine thin wrappers under `.claude/skills/`,
six rule files under `.agents/rules/` read directly by both tools. `AGENTS.md` is the only
root doc, `CLAUDE.md` is just `@AGENTS.md`.

## Lessons

- Wrappers are thin by design, about 20 lines. If `wc -l .claude/skills/*/SKILL.md` shows one
  much longer than the others, someone put logic in a wrapper. Move it to the canonical file
  and regenerate.
- Adding or removing a skill needs `AGENTS.md` edited in two places: the pipeline block and
  the skill routing list. The generator script does not touch `AGENTS.md`, so check it by hand.
- The project mirror uses wrapper files rather than symlinks because this repo is committed to
  git and may travel to Windows. Machine-level `~/.codex/skills` to `~/.claude/skills` mirroring
  can still use symlinks since that directory is never committed.
