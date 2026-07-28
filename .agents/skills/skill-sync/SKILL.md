---
name: skill-sync
description: Reconcile the canonical .agents/skills definitions with the thin .claude/skills wrappers and the Codex agents/openai.yaml metadata for this repo. Run after adding, renaming, or removing a skill, or after editing a skill's name or description. Use when the user says "skill-sync", "sync skills", or "regenerate wrappers". Manual only.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# skill-sync

Keeps the two-tool setup honest. `.agents/skills/` is canonical. `.claude/skills/` holds
thin wrappers that Claude discovers and that delegate back. This skill regenerates the
wrappers from the canonical definitions and reports anything it cannot resolve safely.

Manual only. Never run automatically as a side effect of another skill.

## Read first

- `.agents/README.md` and `.claude/README.md` - the contract this skill enforces
- `.agents/skills/skill-sync/references/memory.md`

## Step 1 - Run the deterministic half

```bash
bash .agents/skills/skill-sync/gen-claude-wrappers.sh
```

For each canonical skill it copies the exact `name` and `description` frontmatter into the
wrapper, lists every `references/*.md` file in the wrapper's step 2, and writes the standard
delegation body. Idempotent. It never deletes a canonical skill, and it reports orphan
wrappers rather than removing them.

On Windows or any shell where that script cannot run, do the same work model-driven: read
each `.agents/skills/*/SKILL.md` frontmatter and write the matching wrapper by hand in the
same shape.

## Step 2 - Codex metadata

Every canonical skill needs `agents/openai.yaml` for Codex discovery:

```yaml
interface:
  display_name: "Title Case Name"
  short_description: "One line, under about 60 characters"
  default_prompt: "Use $name to <do the thing>."
```

```bash
for d in .agents/skills/*/; do
  n=$(basename "$d")
  [ -f "$d/agents/openai.yaml" ] || echo "MISSING openai.yaml: $n"
done
```

Write any missing file. Keep `short_description` consistent with the SKILL.md
`description`, shortened, not contradicting it.

## Step 3 - Memory files

Every canonical skill needs `references/memory.md`, the single canonical copy of its
self-improving notes.

```bash
for d in .agents/skills/*/; do
  n=$(basename "$d")
  [ -f "$d/references/memory.md" ] || echo "MISSING memory.md: $n"
done
```

## Step 4 - Verify the contract

```bash
# every canonical skill has a wrapper, and vice versa
comm -3 <(ls -d .agents/skills/*/ | xargs -n1 basename | sort) \
        <(ls -d .claude/skills/*/ 2>/dev/null | xargs -n1 basename | sort)

# frontmatter matches between canonical and wrapper
for d in .agents/skills/*/; do
  n=$(basename "$d")
  w=".claude/skills/$n/SKILL.md"
  [ -f "$w" ] || continue
  a=$(awk '/^description:/{sub(/^description:[[:space:]]*/,"");print;exit}' "$d/SKILL.md")
  b=$(awk '/^description:/{sub(/^description:[[:space:]]*/,"");print;exit}' "$w")
  [ "$a" = "$b" ] || echo "DRIFT in $n description"
done

# no wrapper may contain skill logic: they should all be about the same short length
wc -l .claude/skills/*/SKILL.md

# root docs single-sourced
cat CLAUDE.md   # must be exactly: @AGENTS.md
```

The `comm -3` output must be empty. Any description drift must be fixed by re-running the
generator, never by editing the wrapper's twin.

## Step 5 - Check AGENTS.md is current

If a skill was added or removed, `AGENTS.md` needs updating in two places: the pipeline
block and the skill routing list. Verify every canonical skill appears in both.

## Step 6 - Report

List created, updated, and unchanged wrappers, any orphans, any missing `openai.yaml` or
`memory.md`, and whether `AGENTS.md` needed an edit. Never delete anything without asking.

## Guardrails

- **Skill logic lives only in `.agents/skills/`.** If a wrapper contains instructions
  beyond the delegation body, that is the bug. Move the content to the canonical file and
  regenerate.
- If a wrapper and its canonical file disagree, the canonical file wins.
- Never copy `.agents/rules/` into `.claude/`. Both tools read the rules directly.
- Never create a Claude-side `memory.md`. There is one canonical copy per skill so a lesson
  from a Codex session and a Claude session land in the same file.
- Never delete an orphan wrapper automatically. Report it.

## Self-improvement

Read `.agents/skills/skill-sync/references/memory.md` at the start of every run. Append when
a host or platform needs different handling, or when a new per-skill file becomes part of
the contract.
