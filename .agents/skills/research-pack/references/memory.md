# Research Pack Skill Memory

This file stores memory specific to the `research-pack` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about how this skill should select projects, research topics, verify sources, and produce useful evidence packs.

## Current Skill Standard

- Select the project before researching.
- Smart-select a project only when context is clear or exactly one unfinished research-pack candidate exists.
- Ask the user to choose from unfinished projects when context is unclear.
- Prefer Codex option UI (`request_user_input` / AskUserOptions style) when available.
- Browse the web or YouTube every run because research facts and reference signals can change.
- Prefer the project-local vendored Browse skill at `.agents/skills/browse/`; fall back to global gstack browse only if needed.
- Write only `projects/<slug>/01-research-pack.md`.
- Do not write script, packaging, visual plan, HyperFrames, voiceover, render, upload, or self-learning files.
- Treat research as evidence and specificity, not a link dump.
- Label facts, inferences, examples, and open questions clearly.
- Collect visual evidence and real-life objects, not only factual sources.
- Keep the channel influence-first and learner-friendly.

## Research Pack Output Standard

A good research pack should make the next script easy without writing it.

It should include:

- one working thesis
- source map with confidence and links
- `what people think`
- `what is actually happening`
- `why it keeps happening`
- explanation spine
- useful examples
- visual reference leads
- jokes and analogies
- English learner support
- safe claims, claims to avoid, and open questions
- clear next step boundary

## Project Selection Lesson

The user wants this skill to require a project before implementation.

Apply every run:

- If the active context clearly points to a project, use it and say why.
- If not, scan `projects/` for unfinished candidates.
- Ask the user to choose from candidate projects before browsing.
- Do not guess between multiple plausible projects.

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `research-pack` as step 2 of the sequential Why It Works video-production skill system.

Initial rules:

- select project first
- browse current sources
- write only `01-research-pack.md`
- include factual evidence, visual reference leads, English learner support, and safety notes
- keep skill-specific learning here and promote only reusable channel-wide lessons upward

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Research pack lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
