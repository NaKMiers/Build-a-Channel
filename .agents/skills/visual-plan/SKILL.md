---
name: visual-plan
description: Create or update step 5 section visual plans for a Why It Works video project. Use when the user asks for Visual Plan, visual planning, section scene plan, reference board, real-life visual references, generated visual assets, HyperFrames build guidance, run step 5, or plan visuals for one section or all sections; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 04-voiceover.md, explicit project selection, and explicit section selection with All as the first option, then writes only the project's 05-visual-plan.md, visual-plan/ section folders, and visual reference assets.
---

# Visual Plan

## Purpose

Run step `6` of the `Why It Works` video workflow.

Turn approved script and section voiceover into a section-level visual blueprint for HyperFrames.

This skill is section-first. After voiceover, production branches by section:

```text
Voiceover S1 -> Visual plan S1 -> Render S1 -> Review S1
Voiceover S2 -> Visual plan S2 -> Render S2 -> Review S2
...
```

Use `All` only when the user explicitly selects `All`.

## Pipeline Position

This is step `5` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`
- `projects/<slug>/04-voiceover.md`
- selected section voiceover output under `projects/<slug>/voiceover/`

Write or update:

- `projects/<slug>/05-visual-plan.md`
- `projects/<slug>/visual-plan/section-XX-kebab-section-name/`
- `projects/<slug>/assets/visual-references/section-XX-kebab-section-name/` when useful

If a required upstream file is missing or empty, stop and tell the user which previous skill to run.

If `01-research-pack.md` is older than `00-topic-intake.md`, treat the research pack as stale and stop. If `02-script.md` is older than topic intake or research pack, treat the script as stale and stop. If `04-voiceover.md` or a selected section voiceover output is older than script, treat voiceover as stale and stop or ask whether to regenerate the affected section.

When this skill creates, updates, or reruns `05-visual-plan.md` or any file under `visual-plan/`, every later output for the affected section becomes stale.

List stale downstream files in chat. Do not silently delete them.

## Required Context

Read these before creating or updating visual plans:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/reference-channels.md`
8. `.agents/_shared/channel/learning-log.md`
9. `.agents/_shared/channel/codex-collaboration.md`
10. `.agents/_shared/channel/production-workflow.md`
11. `.agents/_shared/channel/brand-system.md`
12. `.agents/_shared/systems/topic-packaging-hooks.md`
13. `.agents/_shared/systems/script-learner-voice.md`
14. `.agents/_shared/systems/visual-production.md`
15. `.agents/_shared/systems/audio-feedback-quality.md`
16. `references/memory.md`
17. `references/output-formats.md` before writing outputs
18. the chosen project files:
    - `00-topic-intake.md`
    - `01-research-pack.md`
    - `02-script.md`
    - `04-voiceover.md`

Load additional files only when needed:

- `.agents/_shared/assets/wit/poses/manifest.json` when choosing WIT poses
- existing section visual plans from `projects/why-everyone-pretends-to-be-busy/` when the user asks to follow that reference style
- existing project `visual-plan/` section folders when updating a section

## Project Selection Gate

Always resolve the target project before planning visuals.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `04-voiceover.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find visual-plan candidates.

A visual-plan candidate has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`
- at least one section voiceover output under `voiceover/`

When multiple candidates exist or context is unclear, ask the user to choose before writing.

Do not create a new project folder in this skill.

## Required Inputs Gate

Before section selection or writing files, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`

If `02-script.md` does not contain parsable sections in the form:

```text
## Section N: Section Name
```

stop and ask the user to rerun `script-draft` or fix the script structure first.

If `01-research-pack.md` is older than `00-topic-intake.md`, stop and ask the user to rerun `research-pack`.

If `02-script.md` is older than `00-topic-intake.md` or `01-research-pack.md`, stop and ask the user to rerun `script-draft`.

If `04-voiceover.md` is missing, empty, or older than `02-script.md`, stop and ask the user to run or rerun `voiceover`.

## Section Selection Gate

Visual Plan must get an explicit target section before writing files.

The target must be selected by the user as `All` or as a specific section number/name in the current request or in the section-choice response.

Do not infer the target section from:

- active project state
- latest reviewed section
- next unfinished section
- existing visual plans
- missing visual-plan outputs
- prior chat context

Preferred option order:

1. `All`
2. `Section 1: <name>`
3. `Section 2: <name>`
4. Continue through the section list

Important:

- `All` means create or update each section as a separate visual-plan output.
- `All` does not mean one giant full-video visual plan unless the user explicitly asks for a macro plan.
- If option UI is available, show `All` first, then section choices.
- If option UI is unavailable, list numbered choices in chat and stop. Do not guess.

Fallback selection text:

```markdown
Choose visual plan target:

0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

## Section Voiceover Gate

For each selected section, verify section voiceover exists before planning visuals.

Acceptable evidence:

- a matching section folder under `voiceover/section-XX-kebab-section-name/`
- and a clean script or marked script file
- and either an audio file or `scratch-results.json` that honestly records `tts not generated`
- and an entry in `04-voiceover.md`

If a selected section is missing voiceover output, stop and ask the user to run `voiceover` for that section first.

If the selected section voiceover files are older than `02-script.md`, treat that section voiceover as stale. Stop and ask the user to rerun `voiceover` for the selected section.

If the user selected `All` and some sections are missing voiceover, stop and list the missing sections.

## Request Modes

### Section Create Mode

Use when the chosen section has no existing section visual plan.

Create:

```text
projects/<slug>/visual-plan/section-XX-kebab-section-name/
projects/<slug>/visual-plan/section-XX-kebab-section-name/README.md
projects/<slug>/visual-plan/section-XX-kebab-section-name/section-XX-kebab-section-name-visual-plan.md
projects/<slug>/visual-plan/section-XX-kebab-section-name/reference-board.md
projects/<slug>/assets/visual-references/section-XX-kebab-section-name/
projects/<slug>/05-visual-plan.md
```

### Section Update Mode

Use when the user asks to revise, simplify, add real-life images, change WIT actions, adjust timing, improve HyperFrames guidance, or fix a plan after review.

Read the existing section visual-plan folder first. Preserve approved decisions unless the user explicitly asks to replace them.

### All Sections Mode

Use when the user chooses `All`.

Create each section as its own output using Section Create or Section Update rules.

Do not collapse the whole video into one board table unless the user explicitly asks for a macro visual plan.

### Improve Memory Mode

Use when the user reviews a visual plan and gives reusable lessons.

Update in this order:

1. the project `05-visual-plan.md` or section visual plan if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

Promote shared lessons with a clear classification such as `Operational lesson` or `Core production system`.

## Browsing And Asset Rules

Use the project-local `browse` skill for web or YouTube browsing when available.

Browse or search only when the section needs real-life evidence, real object references, UI/reference patterns, or a visual benchmark.

For each selected section, create a small reference board:

- real-life objects that explain the section
- possible safe assets
- generated-image ideas
- self-made UI/mockup targets
- inspiration-only references
- rejected references
- source notes

Classify every reference as:

- `safe asset`
- `mockup target`
- `inspiration only`
- `reject`

Do not copy another creator's exact frame, thumbnail, joke layout, screenshot, or visual composition.

Prefer:

- self-shot images
- generated images
- licensed/public-domain images
- self-made UI mockups
- simple object cutouts
- paper, receipts, phones, desks, product boxes, calendars, bills, or other lived-in objects

Avoid:

- private data
- unclear copyrighted images
- real app logos unless explicitly approved
- real screenshots copied into production
- generic stock images that do not explain the section

When image generation is available, generate or request section-specific reference images only when they materially improve the plan. Save generated references or returned image paths under:

```text
projects/<slug>/assets/visual-references/section-XX-kebab-section-name/
```

If generation is unavailable, write reusable generation prompts and mark status as `prompt only / image not generated`.

## Visual Planning Rules

Use the channel grammar:

```text
static drawing -> narration twist -> red markup or hard cut -> next static drawing
```

Each board should carry:

- one thought
- one joke or evidence object
- one WIT reaction or real-life object
- one readable label
- one clean timing beat

Visual plans should guide HyperFrames implementation, not replace it.

For each selected section, plan:

- section goal
- narration beats
- board list with approximate local timing
- visual job per board
- real-life or generated asset needs
- WIT pose/emotion per board
- labels and handwritten captions
- red markup or joke beat
- motion notes
- voice-sync cues
- asset/source safety notes
    - render / HyperFrames implementation guidance
- approval checks

Keep boards simple. When a section gets abstract, return to a concrete object.

Use WIT as the audience surrogate. WIT should usually be affected by the system, not lecturing from outside it.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Parse `02-script.md` sections.
4. Run the Section Selection Gate.
5. Run the Section Voiceover Gate for selected sections.
6. Read required shared context and skill memory.
7. For each selected section:
   - extract section narration from `02-script.md`
   - read the matching section voiceover files
   - inspect voiceover duration or timing notes when available
   - identify the section goal, contradiction, visual metaphor, and WIT emotion
   - browse for real-life reference images or reference patterns when useful
   - generate image prompts or generated references when useful and available
   - write `reference-board.md`
   - write `section-XX-kebab-section-name-visual-plan.md`
   - write or update the section `README.md`
8. Write or update `projects/<slug>/05-visual-plan.md` as the section visual-plan index.
9. Run the Downstream Stale Gate.
10. Respond with the Chat Response Format.
11. Stop before render, review, upload, or learning unless explicitly asked.

## Output Folder Standard

Section folder naming:

```text
visual-plan/section-XX-kebab-section-name/
```

Examples:

```text
visual-plan/section-01-hook/
visual-plan/section-02-cheap-is-not-the-villain/
visual-plan/section-06-repair-gets-a-security-system/
```

File naming:

```text
section-XX-kebab-section-name-visual-plan.md
reference-board.md
README.md
```

Use lowercase kebab-case.

## Output Formats

Use `references/output-formats.md` for the exact templates for:

- `05-visual-plan.md`
- section visual-plan files
- section `reference-board.md`
- section `README.md`
- chat response

If only one section has been planned, include remaining sections in `05-visual-plan.md` as `not planned`.

## Downstream Stale Gate

After creating, updating, or rerunning `05-visual-plan.md` or any section visual plan, check the same project for downstream files:

- `06-production-board.md`
- `hyperframes/`
- `renders/`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`

If any exist, list them as stale in chat and tell the user they should be removed or regenerated by rerunning downstream skills in order, starting with `Render`.

Do not delete downstream files unless the user explicitly asks.

For section-level projects, note whether the stale output affects the selected section, all sections, or is unclear.

## Chat Response Format

After creating or updating visual plans, respond with a short summary.

Do not paste the full visual plan unless the user asks.

Use this structure:

```markdown
Done. I created/updated:

[05-visual-plan.md](<absolute path>)

Section target: `<All or Section X: name>`

Status: `<status>`

Generated:

| Section | Status | Boards | Reference assets | Section plan |
| ------- | ------ | -----: | ---------------- | ------------ |

Notes:

- <line 1>
- <line 2>
- <line 3>

Stale downstream:

- <file or none>
```

## Quality Bar

A section visual plan is ready when:

- selected section was explicitly chosen
- selected section has matching voiceover output
- section goal is clear
- board list maps to narration beats
- each board has one thought and one visual job
- WIT emotion supports the viewer's feeling
- labels are short and readable
- real-life references are classified with source notes
- generated images or prompts are marked honestly
- HyperFrames guidance is concrete enough to build from
- script promise is paid off in the section when relevant
- stale downstream files are listed
- no render, review, upload, or learning files are created

## Hard Fails

Reject or stop before finishing if:

- the project lacks `04-voiceover.md`
- the selected section lacks voiceover output
- the user has not explicitly selected `All` or a specific section
- the section target is inferred instead of selected
- the skill plans a section from stale script or voiceover
- the visual plan copies another creator's frame or thumbnail structure
- real private data or unclear copyrighted screenshots are treated as production assets
- generated images are described as existing when they were only prompted
- WIT is decorative and has no emotional job
- labels are too long for a paused board
- boards are too crowded to understand
- the skill creates render, review, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user approves or rejects a visual-plan style
- a reference-board approach works or fails
- generated images help or hurt clarity
- a later HyperFrames build exposes missing planning details
- a review shows recurring timing, label, WIT, or asset problems
- the user clarifies how section branching should behave

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify each promoted lesson as `Core`, `Experiment`, `Operational lesson`, or `Reject` according to `.agents/_shared/channel/channel-guardrails.md`.

Do not rewrite channel foundation, audience, tone, WIT direction, or product-promotion boundary from one visual-plan run without explicit user confirmation.
