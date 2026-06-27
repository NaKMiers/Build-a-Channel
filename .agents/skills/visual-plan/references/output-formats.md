# Visual Plan Output Formats

Use these exact shapes when running the `visual-plan` skill. The master `04-visual-plan.md` and each
section file must stay in sync (the section file = video-level direction summary + that section's
scenes, identical to the master's slice).

## Master `04-visual-plan.md`

Write or update `projects/<slug>/04-visual-plan.md`.

````markdown
# 04 Visual Plan (master)

Video: `<title>`
Status: `master visual plan in progress`
Source skill: `visual-plan`
Source files: `02-script.md`, `03-voiceover.md`

## Video-Level Direction

- Audience: `A2–C1 English learners (interesting-English advantage)`
- Renderer: `HyperFrames (composited from pre-made assets)`
- Visual grammar: `real / real-looking base + mascot drawn on top; new scene ~per sentence; vary everything`
- Mascot character: `<colorful, expressive WIT — big and high, real personality>`
- Tone on screen: `savage-but-clean; edge aimed at the system/the viewer's own wallet, never slurs`
- Recurring motif:
- Scene-type rotation in use:
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; new poses may be invented)

## Section Index

| # | Section | Status | Duration | Scenes | Assets named | Section file |
|---:|---|---|---:|---:|---:|---|

## All Sections (scenes)

> Each section below is identical to its `visual-plan/section-XX-*/` file. Keep them in sync.

### Section 1: <name>
<paste the full section block — see "Section File" template, scenes only>

### Section 2: <name>
...

## Cross-Section Continuity

- Reused assets (filename -> scenes):
- Recurring motif / callback scenes:
- Mascot emotional arc across the video:

## Stale / Regeneration Notes

## Next Step Boundary

Next workflow step: `visual-implement` (creates the assets named here), then `render`.
````

## Section File

Write `projects/<slug>/visual-plan/section-XX-kebab-section-name/section-XX-kebab-section-name-visual-plan.md`.

````markdown
# Section X Visual Plan — <name>

Video: `<title>`
Section: `Section X: <name>`
Status: `draft visual plan for approval`

## Video-Level Direction (for context — keep identical to master)

<short copy of the master Video-Level Direction so this section is never read in isolation>

## Section Overview

- Section goal:
- Duration:
- Scene count:
- Scene-type rotation:
- Mascot arc in this section:

## Scenes

### Scene X.1 — "<exact script line/beat>"

- **Local time:** `0:00–0:00`
- **Role:** <what this beat does; link to prev/next>
- **Composition / layout:** <frame; element positions in %; crop; z-order; horizon line>
- **Elements:**
  - *Left (~x%–x%):* <detailed description of the element and its contents/treatment>
  - *Right / center / etc.:* <...>
- **Mascot:** pose `<pose_filename OR NEW: described>`; placement `<side, scale as frame fraction, crop>`; facing `<dir>`; expression `<...>`
- **On-screen text:** `"<exact words>"` — <handwritten style, position, color, tilt, when it appears>
- **Emotion:** <...>
- **Insight / joke:** <...>
- **Linkage / eye path:** <why elements sit together; left→right etc.>
- **Show-as-you-say:** <element-by-element entrance/hold tied to spoken words; hard-show vs impact>
- **Sound:** <SFX + ducking>
- **Color / contrast:** <palette; what pops>

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `mck-face-distorted.png` | browse-real-photo | real MCK photo, chin/neck stretched funhouse-style, vertical phone frame | left 13–40%, float w/ shadow | new |
| `pose_cheerful_presenting_open_mouth.png` | pose | mascot presenting toward left | right, half-body crop | reuse (library) |

### Scene X.2 — "..."
...

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|

## Approval Checks

- each scene picturable from text alone:
- ~one scene per sentence, scene-types varied:
- every scene has a real/real-looking base:
- mascot big/high with a specific pose+expression per scene:
- show-as-you-say timeline present per scene:
- every asset has type + description + filename + layout:
- repeated subjects reuse the same filename:
- public figures handled as caricature/parody, punching up:
- no image-generation prompts written here:
- in sync with master `04-visual-plan.md`:
````

## Chat Response

````markdown
Done. Master + section visual plan:

[04-visual-plan.md](<absolute path>)

Section target: `<All or Section X: name>`
Status: `<status>`

| Section | Status | Scenes | Assets named | Section file |
|---|---|---:|---:|---|

Notes:
- <line 1>
- <line 2>

Next: run `visual-implement` to create the named assets, then `render`.

Stale downstream:
- <files or none>
````
