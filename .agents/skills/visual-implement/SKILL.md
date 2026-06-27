---
name: visual-implement
description: Run step 4.5 of the Why It Works workflow — turn a completed visual plan into actual assets. Use when the user asks to implement the visual plan, create the assets, generate the scene images, build the assets folder, prep assets for render, or run visual-implement. It reads each scene's ASSET list in the section visual plan and, per asset, EITHER writes a detailed image-generation prompt and creates an isolated element (generate), OR browses for a license-safe real photo / captures a real public screenshot (browse), OR copies a pose from the library, and it REUSES any asset already produced (by filename) instead of recreating it. All assets are saved as isolated elements (transparent/plain background, never a pre-composed scene) into the project assets/ library, tracked in assets/asset-manifest.md with prompt/source/license/status. Requires a completed 04-visual-plan.md and the selected section's visual-plan folder; requires one project and an explicit section selection with All first. Runs after visual-plan and before render.
---

# Visual Implement

## Purpose

Run step `4.5` of the `Why It Works` video workflow.

Take the scenes described by `visual-plan` and **produce the actual assets** so that `render` only has
to composite them. This skill is the bridge between description and pixels.

Core idea (do not break it): assets are **isolated elements** — one character, one object, one UI card,
on a transparent/plain background — created or fetched **once per filename and reused everywhere**.
Never generate a full pre-composed scene, because a recurring subject would look different every time.
Reuse keeps every character identical across scenes; `render` composites the isolated assets into each
scene's layout.

## Division Of Labour

- `visual-plan` described scenes and listed ASSETS (type + description + filename + layout). It wrote
  NO prompts.
- `visual-implement` (this skill) turns each asset description into reality: writes prompts for
  `generate` assets, browses for `browse`/`screenshot` assets, copies `pose` assets, and skips
  `reuse` assets that already exist. It saves everything to `assets/`.
- `render` pulls assets from `assets/` by filename and composites them per the plan's layout.

## Pipeline Position

Required previous outputs:

- `projects/<slug>/04-visual-plan.md`
- the selected section's `visual-plan/section-XX-*/section-XX-*-visual-plan.md` (with an ASSET list)

Write or update:

- `projects/<slug>/assets/<asset-files>` (and `projects/<slug>/assets/poses/<pose-files>` for poses)
- `projects/<slug>/assets/asset-manifest.md`
- `projects/<slug>/assets/ATTRIBUTION.md` (for browsed/real assets with license/source)

If `04-visual-plan.md` or the selected section plan is missing, empty, or stale, stop and tell the user
to run/rerun `visual-plan` first. When this skill creates/updates assets for a section, that section's
`render` output becomes stale — list it.

## Required Context

Read before implementing:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/learning-log.md` (confirmed tone + safety rules)
8. `.agents/_shared/channel/brand-system.md`
9. `.agents/_shared/systems/visual-production.md`
10. `references/memory.md`
11. the mascot pose library: `.agents/_shared/assets/wit/poses/` (+ `analysis/vuive poses/pose.md` when present)
12. the chosen project's `04-visual-plan.md` and the selected section visual-plan file(s)

## Gates

- **Project Selection Gate**: name > current chat > the single project with a completed visual plan and
  missing/partial assets > otherwise ask. Do not create a new project here.
- **Section Selection Gate**: explicit `All` or a specific section, `All` first; never infer.

```markdown
Choose visual-implement target:
0. All sections
1. Section 1: <name>
   ...
```

## Asset Style Contract (for every produced asset)

- **Isolated element**, transparent or plain background — never a full composed scene.
- **Channel flat-cartoon style** for drawn assets: thick uniform black outline, flat fills, matching
  the mascot. When a generated asset must match the mascot character, attach/reference the relevant
  pose file from the library so style/proportions stay consistent.
- **Consistency by filename**: one subject = one file, reused across scenes. Before producing anything,
  check whether the filename already exists in `assets/`; if it does, skip (reuse).
- **Safety bound** (copyright / law / YouTube community standards): public figures only as
  transformative caricature / obvious parody, punching up, never false-as-fact; no slurs; no real
  private data; prefer caricature or licensed/PD over raw copyrighted media. Browsed real photos must
  be license-safe (CC0/CC/PD) with attribution recorded.

## Per-Asset Procedure

Walk every scene's ASSET list in the selected section(s). For each asset, branch on `type`:

### `reuse`
The file should already exist from an earlier scene/section. Verify it exists in `assets/`. If yes,
do nothing (this is the consistency mechanism). If it is missing, treat it as its original type and
produce it once, then it is reused thereafter.

### `pose`
Copy the referenced pose PNG from the library (`.agents/_shared/assets/wit/poses/<name>.png`, or the
project WIT folder) into `projects/<slug>/assets/poses/<filename>`. If the plan invented a NEW pose
(it will be marked `generate` with a pose-style description), produce it like a `generate` asset and,
when useful, also copy it back into the pose library so future videos can reuse it.

### `generate`
1. Write a **detailed image-generation prompt** from the plan's description. The prompt must specify:
   isolated single element, transparent/plain background, channel flat-cartoon style + thick black
   outline (for mascot/caricature assets), exact subject details, framing (full upper body / object
   only), and "no background scene, no extra elements". For a caricature of a real public figure,
   phrase it as an obvious parody caricature (and provide a name-free fallback description in case the
   image tool refuses a named figure).
2. Produce the image:
   - If an image-generation capability is connected, generate it and save to
     `projects/<slug>/assets/<filename>`.
   - If no image-generation tool is connected (current default on this workspace), write the prompt
     into `asset-manifest.md`, set the asset's status to `prompt-ready / awaiting generation`, and
     tell the user to generate it (e.g. paste the prompt into ChatGPT, attach the relevant pose file
     for style) and drop the result into `assets/<filename>`. Track which assets are still awaiting a
     dropped file. Do NOT claim an image exists when only a prompt was written.

### `browse-real-photo`
Use the project-local `/browse` skill to find a **license-safe** real photo (Openverse CC0/CC, or
Wikimedia Commons / public-domain — e.g. official government portraits are PD). Verify the actual
pixels (brand-free / people-appropriate per the scene), download to `assets/<filename>`, and record
source URL + creator + license in `ATTRIBUTION.md`. If the only safe option is risky for mockery,
fall back to a `generate` caricature and note the switch.

### `screenshot/web-capture`
Use `/browse` to open the public page/app and capture the needed UI/screenshot to `assets/<filename>`.
Prefer the user's own account / a public page; never capture private data. When a clean recreation is
safer, build a CSS/mockup target instead and note it.

## Asset Manifest

Maintain `projects/<slug>/assets/asset-manifest.md` as the source of truth render reads. One row per
asset filename:

| Filename | Type | Used in scenes | Description | Prompt (if generate) | Source/License (if browse) | Status |
|---|---|---|---|---|---|---|

Status values: `done` (file present), `prompt-ready / awaiting generation`, `awaiting drop`, `reused`,
`fallback (caricature)`. The manifest must list every asset referenced by the plan for the selected
section(s), with no duplicate filenames for the same subject.

## Workflow

1. Project Selection Gate.
2. Section Selection Gate.
3. Read context, skill memory, the master plan, and the selected section plan(s) + their ASSET lists.
4. Build the de-duplicated asset worklist across the selected section(s) (group by filename; reused
   subjects appear once).
5. For each asset, run the Per-Asset Procedure (reuse-check first; never recreate an existing file).
6. Save all produced/fetched assets into `assets/` (poses into `assets/poses/`).
7. Write/update `asset-manifest.md` and `ATTRIBUTION.md`.
8. Report: assets done, assets awaiting generation/drop (with their prompts), assets reused, any
   fallbacks. Run the Downstream Stale Gate (render for affected sections).
9. Stop before render unless explicitly asked.

## Quality Bar

- every asset the selected section(s) reference exists in `assets/` OR is tracked with a ready prompt /
  awaiting-drop status (no silent gaps)
- all produced assets are isolated elements (transparent/plain bg), not composed scenes
- a repeated subject has exactly one file, reused by filename
- generated prompts specify isolated element + channel style; caricatures are obvious parody with a
  name-free fallback
- browsed assets are license-safe with attribution recorded
- the manifest is complete and matches the plan's filenames
- nothing is claimed generated when only a prompt was written

## Hard Fails

- a required upstream visual plan is missing/stale, or the section was inferred
- producing a full pre-composed scene instead of isolated elements
- recreating an asset that already exists (breaks consistency / wastes work)
- a duplicate filename for the same subject, or a filename that does not match the plan
- a real raw copyrighted photo used for mockery, a real person made to state something false, private
  data captured, or a slur/again-policy-violating asset
- a browsed asset saved without recording license/source
- claiming an image was generated when only a prompt exists
- creating render/preview files or any downstream output

## Self-Improvement

Read `references/memory.md` every run. Update it when the user approves/rejects an asset style, a
generation prompt pattern, a sourcing approach, a reuse/dedupe decision, or the awaiting-drop handoff.
Promote channel-wide lessons into `.agents/_shared/channel/learning-log.md`, classified `Core` /
`Experiment` / `Operational lesson` / `Reject`.
