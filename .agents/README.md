# .agents - canonical HumanPrice agent layer

This directory is the source of truth for both Codex and Claude.

```text
.agents/
  rules/     HumanPrice editorial, evidence, visual, and artifact contracts
  skills/    canonical project skills
    <name>/
      SKILL.md
      references/memory.md
      agents/openai.yaml
```

`.claude/skills/` contains generated thin wrappers. It never contains independent skill
logic or memory.

## Editing contract

- Edit skill workflows and memory only under `.agents/skills/<name>/`.
- Edit channel rules only under `.agents/rules/`.
- Run `/skill-sync` after adding, renaming, removing, or changing the frontmatter of a
  canonical skill.
- The exact HumanPrice style strings live only in `rules/visual-style.md`; project prompt
  artifacts may copy them verbatim.
- Historical competitor research is evidence, not active channel instruction.

The current pipeline is topic, research, script, transcript, cast, metadata, scenes,
thumbnail, and check. Research is a required gate before scriptwriting.
