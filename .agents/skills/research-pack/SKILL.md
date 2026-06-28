---
name: research-pack
description: Create or update the step 1 research pack for a Why It Works video project. Use when the user asks for research pack, research step, evidence pack, source gathering, reference research, factual grounding, visual references, or step 1 of the Why It Works video workflow; requires a completed project 00-topic-intake.md first, stops and asks for Topic Intake if it is missing, reads the shared channel brain, browses web or YouTube for credible sources and visual/reference evidence, then writes only the project's 01-research-pack.md file.
---

# Research Pack

## Purpose

Run step `1` of the `Why It Works` video workflow.

Turn a selected `00-topic-intake.md` into a clean evidence pack that makes the next script obvious without writing the script yet.

## Pipeline Position

This is step `1` of the video workflow.

Required previous output:

- `projects/<slug>/00-topic-intake.md`

Do not run research without a real, non-empty topic intake file. If it is missing or empty, stop and tell the user to run `topic-intake` first.

When this skill creates, updates, or reruns `projects/<slug>/01-research-pack.md`, every later output in the same project becomes stale. List stale downstream files in chat. Do not silently delete them. Remove stale downstream files only when the user explicitly asks; otherwise downstream skills must be rerun in order.

## Required Context

Read these before creating or updating a research pack:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`
9. `.agents/_shared/channel/production-workflow.md`
10. `.agents/_shared/systems/topic-packaging-hooks.md`
11. `.agents/_shared/systems/visual-production.md`
12. `.agents/_shared/systems/script-learner-voice.md`
13. `references/memory.md`
14. the chosen project file: `projects/<slug>/00-topic-intake.md`

Load additional shared systems only when needed:

- `.agents/_shared/systems/topic-packaging-hooks.md` when shaping thumbnail tension or checking first `10` seconds evidence
- `.agents/_shared/systems/visual-production.md` when research needs boardable visual jokes, real-life assets, or reference-board support

## Project Selection Gate

Always resolve the target project before researching.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with `00-topic-intake.md` and no `01-research-pack.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find unfinished research-pack candidates.

An unfinished research-pack candidate is usually:

- a folder with `00-topic-intake.md`
- and no `01-research-pack.md`, or an empty/stub `01-research-pack.md`
- and not obviously already beyond research unless the user asks to update it

Projects without `00-topic-intake.md` are not research-pack candidates. If the user selects or implies a project without `00-topic-intake.md`, stop and ask them to run `topic-intake` first.

When multiple candidates exist or context is unclear, ask the user to choose before doing any research.

Preferred selection UI:

- If Codex option UI is available, use `request_user_input` / AskUserOptions style.
- Show `2-3` best unfinished candidates when the UI limits choices.
- Put the recommended/current-context candidate first.
- Each option should include the project slug and current status.

Fallback selection UI:

- If option UI is unavailable or there are more than `3` candidates, list numbered project slugs and stop.
- Do not research until the user chooses.

Do not create a new project folder in this skill. New projects come from `topic-intake`.

## Required Inputs Gate

Before browsing or writing, verify the chosen project has:

- `00-topic-intake.md`

The file must exist and be non-empty.

If `00-topic-intake.md` is missing or empty, stop and respond with:

- missing output: `00-topic-intake.md`
- required previous skill: `Topic Intake`
- next action: run `topic-intake`, then rerun `research-pack`

Do not create a placeholder topic intake from this skill.

If `01-research-pack.md` exists but `00-topic-intake.md` has a newer modified time, treat the research pack as stale and run Update Mode if the user asked for research. Do not trust the old research pack as current.

## Browsing Requirement

Research requires current web or YouTube browsing, and it should browse the internet across **several
passes**, not one: (1) a facts/explanation pass for credible sources; (2) a demand/reference pass for
how others cover this topic and how engaging videos on it are MADE (hooks, structure, pacing, jokes,
visuals worth learning from); (3) a visual-evidence pass for real-life objects, UI, and reference-board
leads. Gather concrete, linked resources the script and visual plan can actually reference - the goal
is a strong, accurate, *engaging* video for A2–C1 English learners (the channel's "interesting English"
advantage), not a link dump.

Use the project-local Browse skill first:

```text
.agents/skills/browse/SKILL.md
.agents/skills/browse/dist/browse.exe
```

If the project-local browse skill is missing or cannot run, fall back to global gstack `/browse`.

Do not use other browser tools in this workspace unless the user explicitly approves a fallback.

For every research pack, collect enough sources to support script writing:

- `5-8` factual or explanatory sources from credible outlets, official pages, research papers, consumer organizations, company docs, industry reports, or reputable explainers
- `2-4` YouTube/video references with visible demand, packaging, structure, or risk signals
- `2-3` engagement-study references: how the best videos on this topic stay engaging (hook, structure, pacing, humor, visual ideas) - record what to learn without copying
- `10-20` visual/reference-board leads as descriptions and source links, with real internet image leads prioritized when the topic has real-world objects

If browsing fails, write `Reference confidence: low`, record what failed, and do not invent source details.

## Source Rules

Use sources as evidence, not script material.

For each useful source, record:

- title
- creator/publisher
- URL
- date or age if visible
- source type
- what it supports
- confidence
- what not to copy

Separate:

- `Fact`: directly supported by a source
- `Inference`: a reasonable conclusion from multiple sources
- `Example`: a useful concrete illustration
- `Open question`: needs more verification before scripting

Avoid:

- unsupported statistics
- rage-bait framing
- copying another creator's premise, thumbnail, joke, or script structure
- brand accusations without solid sourcing
- real private data
- real logos/screenshots as planned production assets unless there is a specific approved reason

Prefer:

- simple facts
- concrete objects
- real object/material/image leads with source pages and visible license/source status
- credible explanations
- safe generic examples
- self-made or mockup-ready visual ideas

## Request Modes

### Create Mode

Use when the chosen project has no `01-research-pack.md`.

Write:

```text
projects/<slug>/01-research-pack.md
```

### Update Mode

Use when the user asks to improve, refresh, expand, or fix an existing research pack.

Read the existing `01-research-pack.md`, preserve useful decisions, and update only the necessary sections.

### Improve Memory Mode

Use when the user reviews the research pack and gives reusable lessons.

Update in this order:

1. the project `01-research-pack.md`
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

## Downstream Stale Gate

After creating, updating, or rerunning `01-research-pack.md`, check the same project for downstream files (new-project numbering; legacy projects use the old numbers - resolve by suffix per `.agents/rules/video-workflow.md`):

- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`
- `05-production-board.md`
- `06-review.md`
- `07-upload.md`
- `08-self-learning.md`
- `output/packaging.md` (+ `output/thumbnails/`)

If any exist, list them as stale in chat and tell the user they should be removed or regenerated by rerunning downstream skills in order, starting with `script-draft`.

Do not delete downstream files unless the user explicitly asks for removal.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Read the required context and the chosen `00-topic-intake.md`.
4. Extract the chosen angle:
   - working title
   - sharp angle
   - contradiction
   - recurring motif
   - WIT role
   - real-life objects
   - final insight
   - score and risks
5. Turn the angle into research questions:
   - What do people think?
   - What is actually happening?
   - Why does it keep happening?
   - Who benefits?
   - What does the viewer feel in daily life?
   - What can be shown on screen?
6. Browse for credible factual/explanatory sources.
7. Browse YouTube for adjacent high-view or high-signal references.
8. Gather visual/reference-board leads:
   - real-life objects
   - real internet image leads that make the topic feel close to the viewer
   - UI or paper evidence
   - visual metaphors
   - thumbnail tension
   - WIT emotions
   - color and contrast
   - source/license notes when visible
9. Convert research into a simple explanation spine:
   - hook evidence
   - reframe
   - `3-5` explanation chunks
   - final payoff
10. Add English learner support:
   - useful vocabulary
   - simple phrase candidates
   - words to define simply
   - cultural or jargon risks
11. Add fact safety:
   - safe claims
   - avoid claims
   - open questions
12. Write or update `projects/<slug>/01-research-pack.md`.
13. Run the Downstream Stale Gate.
14. Stop. Do not write script, packaging, voice, visual plan, HyperFrames, renders, or upload notes.

## Output File Format

Use this structure for `projects/<slug>/01-research-pack.md`:

```markdown
# 01 Research Pack

Video: `<title>`

Status: `draft research pack`

Date: `YYYY-MM-DD`

Source skill: `research-pack`

## Topic Intake Snapshot

- Working title:
- Sharp angle:
- Main contradiction:
- Recurring motif:
- WIT role:
- Final insight:
- Main risk:

## Working Thesis

One clear paragraph.

## Research Questions

1.
2.
3.

## Source Map

| Source | Type | Publisher / Creator | URL | What it supports | Confidence | Use / Do not copy |
|---|---|---|---|---|---|---|

## What People Think

## What Is Actually Happening

## Why It Keeps Happening

## Explanation Spine

| Section | Job | Evidence | Visual anchor | WIT state |
|---|---|---|---|---|

## Useful Examples

| Example | What it shows | Source support | Visual use |
|---|---|---|---|

## Visual Reference Leads

### Real-Life Objects

### UI Or Paper Mockup Targets

### Visual Metaphors

### Thumbnail Tension

### WIT Emotions

### Color And Contrast

## Jokes And Analogies

## English Learner Support

- Useful words:
- Useful phrases:
- Jargon to explain simply:
- Phrases to avoid:

## Safe Claims

## Claims To Avoid

## Open Questions

## Research Decision

What is strong enough to move into script?

## Next Step Boundary

Next workflow step: `Script draft`

Do not continue into script until the user asks for the script skill or explicitly requests script drafting.
```

## Quality Bar

A research pack is ready when:

- the thesis is clear in one paragraph
- every major claim has a source or is labeled as an inference
- the script structure is obvious but not written yet
- the recurring motif became more concrete
- there are at least `5` boardable visual ideas
- WIT has a clear emotional path
- English learner vocabulary is practical and not school-like
- risky claims are marked before scripting
- sources are linked and not copied

## Hard Fails

Reject or revise the research pack before finishing if:

- it is just a link dump
- the project is missing `00-topic-intake.md`
- it has no clear hidden system
- it cannot support the chosen angle
- it contradicts the `00-topic-intake.md` without saying why
- it depends on one weak source
- it includes unsupported accusations
- it turns the channel into direct product promotion
- it plans to copy another creator's visual or script
- it has no real-life objects or visual evidence
- it moves into full script writing

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user says the research was too broad, too shallow, too academic, too unsafe, or not visual enough
- a source type repeatedly proves useful or weak
- a later script step exposes missing evidence
- a visual plan fails because the research did not collect enough objects
- a factual claim needs correction

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify promoted lessons as `Core`, `Experiment`, `Operational lesson`, or `Reject`.
