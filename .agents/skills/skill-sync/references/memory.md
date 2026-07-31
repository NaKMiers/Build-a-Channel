# skill-sync - memory

Self-improving notes for keeping the two-tool mirror honest. Single canonical copy.

## The contract

One canonical skill under `.agents/skills/` per one thin wrapper under `.claude/skills/`, and
six rule files under `.agents/rules/` read directly by both tools. `AGENTS.md` is the only
root doc, `CLAUDE.md` is just `@AGENTS.md`.

Do not record a skill count here. It was written as "nine" and was stale within two skill
additions, in three files at once. `ls -d .agents/skills/*/ | wc -l` is the answer, and
Step 4's `comm -3` is the check that matters. As of the `scene-polish` rename there are 11:
eight pipeline skills (`topic`, `script`, `transcript`, `cast`, `scenes`, `metadata`,
`thumbnail`, `check`) plus `scene-polish`, `video-swipe`, and `skill-sync`.

## Lessons

- Wrappers are thin by design, about 20 lines. If `wc -l .claude/skills/*/SKILL.md` shows one
  much longer than the others, someone put logic in a wrapper. Move it to the canonical file
  and regenerate.
- Adding or removing a skill needs `AGENTS.md` edited in two places: the pipeline block and
  the skill routing list. The generator script does not touch `AGENTS.md`, so check it by hand.
- The project mirror uses wrapper files rather than symlinks because this repo is committed to
  git and may travel to Windows. Machine-level `~/.codex/skills` to `~/.claude/skills` mirroring
  can still use symlinks since that directory is never committed.

## Renaming a skill

Do it in this order, and the generator has nothing to complain about:

1. `git mv .agents/skills/<old> .agents/skills/<new>` **and** `git mv .claude/skills/<old>
   .claude/skills/<new>`. Moving the wrapper too is what keeps Step 4's `comm -3` empty and
   stops the generator reporting an orphan you would then have to delete by hand.
2. Inside the canonical `SKILL.md`, update three things, not one: the frontmatter `name`, the
   `# <name>` heading, and **every `.agents/skills/<old>/` path in the body**. Skills that ship
   a script reference their own directory in each command block, so a rename that only touches
   the frontmatter leaves commands pointing at a directory that no longer exists.
3. `agents/openai.yaml` carries the name twice, in `display_name` and in the `$name` inside
   `default_prompt`. A grep for the old slug catches the second one, an eyeball usually does not.
4. `references/memory.md` starts with `# <name> - memory`.
5. `AGENTS.md` in two places, then run the generator, then Step 4.

A per-skill script keeps its own filename when the filename names its subject rather than the
skill. `scene-polish` kept `scripts/scene_images.py` because it still operates on scene image
files, and renaming it would have churned history for nothing.
