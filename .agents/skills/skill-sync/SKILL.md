---
name: skill-sync
description: Manually synchronize the Codex (.agents) and Claude (.claude) configuration for the Why It Works workspace so both tools stay in lockstep. Use when the user asks to sync skills, sync Codex and Claude, reconcile skill wrappers, sync AGENTS.md and CLAUDE.md, propagate a skill improvement to the other tool, after creating editing or deleting a skill, or after editing a root instruction file; it reconciles the skill inventory, regenerates or updates Claude delegating wrappers and Codex openai.yaml from the canonical .agents/skills definitions, syncs name and description frontmatter plus reference lists, aligns the shared sections and skill lists of AGENTS.md and CLAUDE.md, and reports orphans or conflicts for the user to resolve instead of deleting work; manual only, never auto-run.
---

# Skill Sync

## Purpose

Keep the Codex and Claude configurations of this workspace in lockstep so a skill or
instruction improved for one tool is automatically reflected for the other.

This skill is the maintenance tool for the dual-tool layout described in
`.claude/README.md`. It does not invent or rewrite skill logic; it reconciles the two
tools' entry points around the single source of truth.

## Source-Of-Truth Model

Read and respect this model before changing anything:

- **Canonical skill logic + memory** live once under `.agents/skills/<name>/`
  (`SKILL.md`, `references/`). Both tools use these files.
- **Claude discovery wrappers** live under `.claude/skills/<name>/SKILL.md`. A wrapper is
  thin: it carries the matching `name` + `description` frontmatter and delegates to the
  canonical `.agents/skills/<name>/SKILL.md`. It contains no real skill logic.
- **Codex discovery metadata** lives under `.agents/skills/<name>/agents/openai.yaml`.
- **Root instructions**: `AGENTS.md` (Codex) and `CLAUDE.md` (Claude) mirror each other on
  the shared sections (startup routine, browsing rule, memory/persistence rules, skill
  list, pipeline gate, workspace boundaries, safety gate, identity, goal).

Invariant this skill enforces: logic and self-improving memory stay single-sourced in
`.agents/`; `.claude/skills/` holds only wrappers; both root docs agree on shared content.

## Manual Only

Run this skill only when the user explicitly asks for a sync. Never trigger it
automatically from another skill or as a side effect.

## Exemptions

- The `browse` skill (`.agents/skills/browse/`) is vendored from gstack, git-ignored, and
  optional/local-only. Do not require a Claude wrapper for it and do not delete it. If
  present, leave it untouched unless the user asks.
- Never touch `.agents/_shared/`, `.agents/rules/`, `projects/`, `.gstack/`, or any binary
  asset during a sync. Those are not part of the Codex/Claude entry-point layer.

## Required Context

Read before syncing:

1. `.claude/README.md` (the dual-tool layout and sync rules)
2. `AGENTS.md`
3. `CLAUDE.md`
4. `.agents/rules/README.md`
5. `references/memory.md`

## Wrapper Template

When creating or restubbing a Claude wrapper, use exactly this shape (frontmatter copied
verbatim from the canonical skill; reference bullets listing every file in the canonical
`references/` folder):

```markdown
---
name: <name>
description: <verbatim copy of the canonical .agents/skills/<name>/SKILL.md description>
---

# <Title> (Claude wrapper)

This is the Claude discovery wrapper for the **<name>** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/<name>/SKILL.md` exactly.
2. Read the references it points to, including <list each `.agents/skills/<name>/references/*.md`>.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/<name>/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/<name>/SKILL.md` wins.
```

## Codex Metadata Template

When a canonical skill is missing `agents/openai.yaml`, generate one from its frontmatter:

```yaml
interface:
  display_name: "<Title Case name>"
  short_description: "<one-line summary derived from the description>"
  default_prompt: "Use $<name> to <short action>."
```

## Workflow

Work in this order and report every action.

### 1. Build the inventory

- Canonical skills = every subdirectory of `.agents/skills/` that contains a `SKILL.md`,
  minus the exemptions.
- Claude wrappers = every subdirectory of `.claude/skills/` that contains a `SKILL.md`.
- Record each skill's canonical `name` + `description` and the files in its `references/`.

### 2. Reconcile each canonical skill (agents -> claude)

For every canonical skill:

1. If no `.claude/skills/<name>/SKILL.md` exists, create it from the Wrapper Template.
2. If it exists and is a proper delegating wrapper:
   - If the wrapper `name`/`description` differs from canonical, update the wrapper
     frontmatter to match canonical exactly.
   - If the reference bullets do not list every current `references/*.md`, update them.
3. If the Claude file is **not** a wrapper (it holds real instructions / lacks the
   delegation pointer), treat it as a Claude-side improvement:
   - Show the user a clear summary/diff of what the Claude file contains that the canonical
     file does not.
   - On confirmation, merge those improvements into `.agents/skills/<name>/SKILL.md`
     (and `references/` as appropriate), then restub the Claude file as a wrapper.
   - Do not overwrite canonical logic without showing the change first.

### 3. Reconcile Codex metadata

For every canonical skill, ensure `agents/openai.yaml` exists. If missing, generate it
from the Codex Metadata Template and report it. If present, leave hand-tuned values alone.

### 4. Handle orphans (claude -> agents)

For every Claude wrapper with no matching canonical skill:

- Report it as an orphan. Do **not** auto-delete.
- Offer two resolutions for the user to choose: (a) remove the orphan wrapper, or
  (b) promote it into a new canonical `.agents/skills/<name>/` skill (logic + references +
  `openai.yaml`) and restub the wrapper.

### 5. Sync root instruction docs (AGENTS.md <-> CLAUDE.md)

- Regenerate/verify the **skill-list bullets** in both `AGENTS.md` and `CLAUDE.md` so they
  list exactly the canonical skills with trigger phrasing consistent with each skill's
  description. Production-pipeline skills keep their pipeline order; utility skills like
  `skill-sync` are listed as manual and outside the pipeline gate.
- Diff the other **shared sections** (startup routine, browsing rule, memory/persistence
  rules, pipeline gate, workspace boundaries, safety gate, identity, goal). If they match
  in substance, leave them. If they genuinely diverge, **stop and ask the user which side
  is authoritative** before overwriting hand-written instructions — do not guess.

### 6. Report

Print a summary table of actions: created, updated, generated, flagged, and items awaiting
a user decision. If nothing was out of sync, say so explicitly.

## Output Format

```markdown
## Skill Sync Report

### Inventory
- Canonical skills: <list>
- Claude wrappers: <list>

### Actions Taken
| Item | Type | Action |
| ---- | ---- | ------ |

### Needs Your Decision
- <orphans, content-bearing Claude files to migrate, divergent doc sections>

### Result
- In sync: <yes/no>. <one-line summary>
```

## Safety

- Manual only; never auto-run.
- Never delete user work silently — orphans and conflicts are reported, not removed.
- Never overwrite canonical skill logic or root-doc prose without showing the change and
  getting confirmation.
- Never touch `.agents/_shared/`, `.agents/rules/`, `projects/`, assets, or the vendored
  `browse` skill.
- Keep edits scoped to the entry-point layer: wrappers, `openai.yaml`, and the shared
  sections of the two root docs.

## Self-Improvement

Read `references/memory.md` every run. Update it when:

- the sync model changes (new file type to keep in lockstep, new exemption)
- a recurring drift pattern appears (e.g. a section that keeps diverging)
- the user corrects how a conflict should be resolved

Do not promote sync-tooling lessons into the channel learning log; they are operational,
not channel strategy.
