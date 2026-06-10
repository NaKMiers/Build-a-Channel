# Visual Plan Output Formats

Use these exact shapes when running the `visual-plan` skill.

## 05 Visual Plan

Write or update:

```text
projects/<slug>/05-visual-plan.md
```

````markdown
# 05 Visual Plan

Video: `<title>`

Status: `section visual plan in progress`

Source skill: `visual-plan`

Source files:

- `02-script.md`
- `04-voiceover.md`

## Visual Direction

- Renderer: `HyperFrames`
- Format:
- Main grammar:
- Script promise:
- Main motif:
- WIT role:
- Real-life texture:
- Editor intent:
- Reference standard:
- Red markup style:
- Motion rule:

## Section Visual Plan Index

| # | Section | Status | Duration | Big Scenes | Cue States | Section plan | Reference board | Notes |
|---:|---|---|---:|---:|---:|---|---|---|

## Cross-Section Continuity

- Recurring object:
- Recurring label:
- WIT emotion arc:
- Color/texture notes:
- Asset reuse notes:

## Stale / Regeneration Notes

## Next Step Boundary

Next workflow step: `Render`

Do not continue into render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.
````

## Section Visual Plan

````markdown
# Section X Visual Plan

Video:
`<title>`

Section:
`Section X: <name>`

Status:
`draft visual plan for approval`

## Section Goal

## Source Inputs

- Script:
- Voiceover:
- Script promise:
- Section duration:

## Narration

```text
...
```

## Visual Direction

- Big-scene/cue rhythm:
- Big scene rhythm:
- Cue-state count:
- Main visual metaphor:
- WIT emotional path:
- Real-life texture:
- Real image references:
- Generated/support assets:
- Viewer attention strategy:
- Retention risk:
- Visual fix:
- Red markup:
- Motion rule:

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | WIT Pose / Size | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Why WIT Is Needed |
|---|---:|---|---|---|---|

## Markup And Label Plan

| Cue | Time | Text / Markup | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|

## HyperFrames Guidance

- Composition target:
- Big scene count:
- Cue state count:
- Scene components:
- Timing notes:
- Text style:
- Asset paths:
- Audio sync notes:
- WIT pose files:
- Suggested inspect timestamps:
- Suggested MP4 QA frame timestamps:
- Build risks:
- Must not invent:

## Approval Checks

- visual reference pass completed:
- what/when/how clear:
- big scenes grouped, not one full scene per sentence:
- cue states low enough for section duration:
- attention reason per big scene / cue state:
- label readable:
- WIT has a clear job:
- WIT pose files named:
- red markup points to exact object:
- real-life asset explains, not decorates:
- title-thumbnail promise still being paid off:
- safe for English learners:
- ready for HyperFrames:
````

## Reference Board

````markdown
# Section X Reference Board

## Reference Pass Status

- Status:
- Browsed references:
- Real images saved:
- Generated images:
- Inspected local assets:
- Prompt-only fallbacks:
- Fallback reason:

## Search / Browse Notes

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|

## Image Generation Prompts

### Prompt 1

```text
...
```

Negative prompt:

```text
...
```

## Rejected References
````

## Section README

````markdown
# Section X Visual Plan

Video:
`<title>`

Section:
`Section X: <name>`

Status:

## Files

- Visual plan:
- Reference board:
- Asset folder:

## Build Notes

- Big scene count:
- Cue state count:
- Main motif:
- WIT emotion:
- Key labels:
- Reference pass:
- Key assets:
- HyperFrames readiness:
````

## Chat Response

````markdown
Done. I created/updated:

[05-visual-plan.md](<absolute path>)

Section target: `<All or Section X: name>`

Status: `<status>`

Generated:

| Section | Status | Big Scenes | Cue States | Reference assets | Section plan |
|---|---|---:|---:|---|---|

Notes:

- <line 1>
- <line 2>
- <line 3>

Visual reference pass:

- <browsed/generated/local/prompt-only status>

Stale downstream:

- <file or none>
````
