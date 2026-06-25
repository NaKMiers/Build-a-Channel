---
name: script-draft
description: Create or update the step 2 sectioned script draft for a Why It Works video project. Use when the user asks for script draft, write the script, draft video script, sectioned script, script step, or step 2 of the Why It Works workflow; requires completed project 00-topic-intake.md and 01-research-pack.md first, stops and asks for Topic Intake or Research Pack if either is missing, reads the shared channel brain, then writes only the selected project's 02-script.md with a sectioned learner-friendly no-face explainer script.
---

# Script Draft

## Purpose

Run step `2` of the `Why It Works` video workflow.

Turn a selected `00-topic-intake.md` and `01-research-pack.md` into a sectioned working script that is ready for voiceover.

## Pipeline Position

This is step `2` of the video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`

Do not draft without real, non-empty topic intake and research pack files.

If both are missing, stop and tell the user to run `topic-intake` first, then `research-pack`, then rerun `script-draft`.

If `00-topic-intake.md` is missing, stop and tell the user to run `topic-intake`.

If `01-research-pack.md` is missing, stop and tell the user to run `research-pack` after topic intake exists.

If `01-research-pack.md` is older than `00-topic-intake.md`, treat the research pack as stale and stop. Tell the user to rerun `research-pack`.

When this skill creates, updates, or reruns `projects/<slug>/02-script.md`, every later main-pipeline output in the same project becomes stale. Do not mark packaging stale. List stale downstream files in chat. Do not silently delete them. Remove stale downstream files only when the user explicitly asks; otherwise downstream skills must be rerun in order.

## Required Context

Read these before creating or updating a script:

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
11. `.agents/_shared/systems/script-learner-voice.md`
12. `.agents/_shared/systems/visual-production.md`
13. `references/memory.md`
14. `projects/2-why-everyone-pretends-to-be-busy/02-script.md` when available, as the current sectioned script reference
15. the chosen project files:
    - `projects/<slug>/00-topic-intake.md`
    - `projects/<slug>/01-research-pack.md`

Load additional shared systems only when needed:

- `.agents/_shared/systems/topic-packaging-hooks.md` when a section needs to preserve title-thumbnail tension
- `.agents/_shared/channel/brand-system.md` when WIT behavior needs stronger guidance
- `.agents/_shared/systems/script-learner-voice.md` when choosing phrase highlights

## Project Selection Gate

Always resolve the target project before writing.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with `00-topic-intake.md` and `01-research-pack.md` but no completed `02-script.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find unfinished script candidates.

An unfinished script candidate is usually:

- a folder with `00-topic-intake.md`
- and `01-research-pack.md`
- and no `02-script.md`, or an empty/stub `02-script.md`
- and not obviously already beyond script unless the user asks to update it

Projects without both `00-topic-intake.md` and `01-research-pack.md` are not script candidates. If the user selects or implies a project missing either file, stop and ask them to run the missing previous skill.

When multiple candidates exist or context is unclear, ask the user to choose before writing.

Preferred selection UI:

- If Codex option UI is available, use `request_user_input` / AskUserOptions style.
- Show `2-3` best unfinished candidates when the UI limits choices.
- Put the recommended/current-context candidate first.
- Each option should include the project slug and current status.

Fallback selection UI:

- If option UI is unavailable or there are more than `3` candidates, list numbered project slugs and stop.
- Do not draft until the user chooses.

Do not create a new project folder in this skill. New projects come from `topic-intake`.

## Required Inputs Gate

Do not draft a script unless the chosen project has:

- `00-topic-intake.md`
- `01-research-pack.md`

Both files must exist and be non-empty.

If both files are missing or empty, stop and tell the user to run `topic-intake`, then `research-pack`, then rerun `script-draft`.

If `00-topic-intake.md` is missing or empty, stop and tell the user to run `topic-intake` first.

If `01-research-pack.md` is missing or empty, stop and tell the user to run `research-pack` after topic intake exists.

Do not create placeholder topic intake or research pack files from this skill.

If `01-research-pack.md` has an older modified time than `00-topic-intake.md`, treat the research pack as stale. Stop and tell the user to rerun `research-pack` before drafting.

If `02-script.md` exists but any prerequisite has a newer modified time, treat the script as stale and use Update Mode when the user asks for script drafting.

If the research pack marks `Reference confidence: low`, contains unresolved blocking open questions, or lacks safe claims, either:

- stop and ask for research improvement, or
- continue only with claims clearly labeled as inference and list the risk in `Claim Safety Notes`

## Request Modes

### Create Mode

Use when the chosen project has no usable `02-script.md`.

Write:

```text
projects/<slug>/02-script.md
```

### Update Mode

Use when the user asks to improve, rewrite, shorten, expand, restructure, or fix an existing script.

Read the existing `02-script.md`, preserve useful approved structure, and update only the requested sections unless the whole script is clearly affected.

### Improve Memory Mode

Use when the user reviews the script and gives reusable lessons.

Update in this order:

1. the project `02-script.md` if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves scripts across the whole channel

## Downstream Stale Gate

After creating, updating, or rerunning `02-script.md`, check the same project for downstream files:

- `04-voiceover.md`
- `05-visual-plan.md`
- `06-production-board.md`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`

If any exist, list them as stale in chat and tell the user they should be removed or regenerated by rerunning downstream skills in order, starting with `voiceover`.

Do not delete downstream files unless the user explicitly asks for removal.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Read the required context and the chosen project files.
4. Draft or update only `projects/<slug>/02-script.md`.
5. Run the Downstream Stale Gate.
6. Respond with the Chat Response Format.
7. Stop before voiceover, visual plan, render, review, upload, or learning.

## Script Model

Use the `Why Everyone Pretends To Be Busy` script as the current structural reference:

- a short header with status, estimated runtime, and source notes
- a `Section Summary` table
- numbered sections
- each section has:
  - estimate
  - word count
  - purpose
  - visual goal
  - narration block
  - approval checks
- sectioned production discipline: one section can later be implemented, previewed, adjusted, and approved before moving on

Do not copy its topic, jokes, section names, wording, or exact count. Copy the discipline, not the content.

## Drafting Rules

Use the research pack as the source of truth.

The script should:

- open with a situation, not an introduction
- make the title promise visible in the first `10` seconds
- use simple spoken English for intermediate learners
- sound like a calm person explaining something ridiculous
- use dry humor and concrete objects
- keep WIT as the audience surrogate, not a presenter beside text
- explain through `what people think -> what is actually happening -> why it keeps happening -> payoff`
- include only claims supported by `01-research-pack.md` or clearly labeled as inference
- avoid brand accusations unless the research pack explicitly supports them
- avoid direct product promotion
- create boardable moments without writing a full visual plan

Prefer:

- short lines
- concrete nouns
- repeated key phrases
- one clear section job
- one recurring motif
- a joke every `20-40` seconds when natural
- section endings that feel like mini-payoffs

Avoid:

- academic paragraphs
- dense statistics
- unsupported claims
- native-only slang
- long idiom chains
- moralizing at the viewer
- writing a documentary essay
- turning visual notes into full HyperFrames boards
- voiceover markup overload in the first draft

## Section Shape

Choose the section count from the research, usually `6-8` sections:

1. `Hook`
2. `Reframe`
3. `Point 1`
4. `Point 2`
5. `Point 3`
6. optional `Point 4` or `Example Loop`
7. `Payoff`
8. optional short `Outro`

Good section names should be specific to the video, such as:

```text
The Visible Price Wins
The Future Gets Removed
Repair Becomes A Door With Locks
Replacement Becomes Normal
```

Runtime guidance:

- respect any runtime target in the project
- if no target exists, aim for a first draft around `5-7` minutes
- write an estimated runtime and estimated words
- do not make the script longer just to sound more complete

## Claim Safety

Every script draft must include a short claim safety section.

Classify claims as:

- `Safe`: directly supported by the research pack
- `Inference`: reasonable synthesis from the research pack
- `Avoid`: tempting but unsafe, too broad, too accusatory, or unsupported

If a line depends on an inference, keep the wording softer:

- use `can`, `often`, `some`, `many`, `may`
- avoid `always`, `every`, `all`, `secretly`, `proves`

## Output File Format

Use this structure for `projects/<slug>/02-script.md`:

````markdown
# 02 Script

Video: `<title>`

Status: `draft script`

Estimated runtime: `<mm:ss>`

Estimated words: `<number>`

Source skill: `script-draft`

Source files:

- `00-topic-intake.md`
- `01-research-pack.md`

## Draft Strategy

- Core thesis:
- Recurring motif:
- WIT arc:
- Script risk:

## Section Summary

|   # | Section | Estimate | Words | Purpose |
| --: | ------- | -------: | ----: | ------- |

## Section 1: Hook

Estimated time: `0:00-0:__`

Words: `__`

Purpose:

Visual goal:

Narration:

```text
...
```
````

Approval check:

-

Voice revision notes:

-

## Section 2: ...

## Claim Safety Notes

### Safe Claims

### Inferences Used Carefully

### Claims Avoided

## English Learner Notes

- Useful words:
- Useful phrases:
- Terms to explain simply:
- Lines that may need slower delivery:

## Next Step Boundary

Next workflow step: `Voiceover`

Do not continue into voiceover, visual plan, render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.

```

## Chat Response Format

After creating or updating `02-script.md`, respond in chat with a short review summary.

Do not paste the full script into chat unless the user asks.

Use this structure:

```markdown
Done. I created/updated:

[02-script.md](<absolute path>)

Status: `<script status>`

Estimated duration: `<mm:ss>`

Brief:
- <line 1>
- <line 2>
- <line 3>

Section summary:

| # | Section | Estimate | Words | Purpose |
|---:|---|---:|---:|---|
```

Brief rules:

- Use `3-5` lines.
- Summarize the whole script, not the workflow.
- Mention the core thesis, recurring motif, WIT arc, and final payoff when useful.
- Keep it concise enough for the user to judge whether they want a review or revision.

## Quality Bar

A script draft is ready when:

- the first `10` seconds creates a concrete curiosity event
- the script has a clean section summary
- each section has one clear purpose
- the recurring motif appears in the hook, middle, and payoff
- WIT has a clear emotional arc
- the language is simple without becoming childish
- jokes support the explanation
- major claims trace back to the research pack
- approval checks are useful for later visual planning
- the next step boundary is clear

## Hard Fails

Reject or revise the script before finishing if:

- it writes without a research pack
- it writes without a topic intake
- it copies another creator's title, structure, joke, or frame
- it becomes a lecture instead of a funny explainer
- the hook starts with branding, definitions, or `In today's video`
- WIT is only decorative
- the script blames viewers for normal behavior
- it says all cheap/free/productivity/etc. things are bad
- it uses unsupported accusations
- it is too abstract to board
- it writes full visual plan, HyperFrames implementation, voiceover files, packaging, renders, or upload notes

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user says the script is too broad, too long, too academic, too serious, too weak, too generic, or not funny enough
- the user asks for a different chat response shape after script creation
- a later voice revision exposes awkward phrasing
- a visual plan fails because sections are not boardable
- a later review shows the hook, WIT arc, learner clarity, or claim safety was weak
- the user approves a script pattern that should become the default

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify promoted lessons as `Core`, `Experiment`, `Operational lesson`, or `Reject`.
```
