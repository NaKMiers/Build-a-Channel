# .agents - canonical agent layer (Codex + Claude source of truth)

This folder is the single source of truth for how AI agents operate in this project.
Both **Codex** and **Claude** read from here. `.claude/skills/` holds only thin wrappers
that delegate back (see `.claude/README.md`).

```text
.agents/
  rules/     the channel brain. Six files, read the focused one before acting:
             house-rules, channel-dna, visual-style, mascot-toss,
             thumbnail-rules, file-formats.
  skills/    executable project-local skills. Each skill is:
               <name>/
                 SKILL.md              full logic, workflow, self-check
                 references/memory.md  self-improving notes (single canonical copy)
                 agents/openai.yaml    Codex discovery metadata
```

## What lives where

The nine skills are the pipeline. The six rule files are the channel knowledge that used
to sit inside `prompts/master-prompt.md`. Skills read the rule files at run time rather
than restating them, so a rule is edited in exactly one place.

This matters because it already bit us: the style anchor and style lock strings were
re-typed 7 times each across the old prompt files, and a thumbnail rule was fixed in one
copy while two others still contradicted it. Those four strings now live once, in
`rules/visual-style.md`, and the `check` skill greps for them.

## Editing rules

- Skill logic, workflow, and self-improving memory are edited **only** here, under
  `.agents/skills/<name>/`.
- After adding, renaming, or removing a skill, or changing its frontmatter, run the
  **skill-sync** skill to regenerate the Claude wrappers.
- Rules in `.agents/rules/` are read directly by both tools. Never copy them into
  `.claude/`.
- The retired `prompts/master-prompt.md` and `prompts/character-prompt.md` are kept
  under `prompts/retired/` as the provenance record. If a rule here looks wrong or thin,
  check it against those files before changing it.
