---
name: render
description: Build or update step 5 section HyperFrames previews for a Why It Works video project. Use when the user asks for Render, HyperFrames build, create video from visual-plan, build a section preview, run section localhost, start preview servers, or run step 5; export MP4/WebM only when the user explicitly asks to export video; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 03-voiceover.md, 04-visual-plan.md, selected section voiceover, selected section visual plan, ALL of the selected section's assets ready in assets/ (per assets/asset-manifest.md; render stops if any are missing or awaiting generation/drop rather than sourcing them itself), explicit project selection, and explicit section selection with All as the first option; creates 05-production-board.md, section-previews/ section HyperFrames projects, and hyperframes/ review copies while using port 1000 for unified preview and port 1000 plus section number for section previews.
---

# Render

## Purpose

Run step `6` of the `Why It Works` video workflow.

Use HyperFrames to convert one selected section visual plan into an editable, previewable video section.

This skill is section-first:

```text
Voiceover S1 -> Visual Plan S1 -> Render S1 -> Review S1
Voiceover S2 -> Visual Plan S2 -> Render S2 -> Review S2
...
```

Do not build every section inside one localhost. Each section gets its own HyperFrames preview project and its own port.

## Port Contract

Use these fixed localhost ports:

```text
Unified/final preview: http://localhost:1000
Section 1 preview:     http://localhost:1001
Section 2 preview:     http://localhost:1002
Section 3 preview:     http://localhost:1003
...
Section N preview:     http://localhost:1000 + N
```

Examples:

- `Section 1: Hook` -> `1001`
- `Section 2: Reframe` -> `1002`
- `Section 7: Payoff` -> `1007`

If the required port is occupied by the correct existing preview server, reuse it and document it.
If the required port is occupied by an unrelated process, stop and report the conflict. Do not silently choose a random port.

Port `1000` is reserved for the unified/final preview after sections are approved. Do not use port `1000` for section work.

## Pipeline Position

This is step `6` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`
- `projects/<slug>/03-voiceover.md`
- `projects/<slug>/04-visual-plan.md`
- selected section voiceover under `projects/<slug>/voiceover/`
- selected section visual plan under `projects/<slug>/visual-plan/`
- the selected section's implemented assets in `projects/<slug>/assets/` (produced by `visual-implement`; see `assets/asset-manifest.md`)

Packaging now runs after caption and writes `output/packaging.md`; it is not a render prerequisite. Do not require packaging for render.

### Asset Consumption (post-`visual-implement`)

As of `2026-06-28`, `visual-implement` runs between `visual-plan` and `render` and produces the
scene assets as ISOLATED elements (generated images, browsed real photos, pose PNGs) into the project
`assets/` library, tracked in `assets/asset-manifest.md`. Render's job is to **composite** the mascot +
these pre-made assets into each scene's layout described by the visual plan - pull each asset by the
filename the plan/manifest specifies and place it per the scene's layout. The same subject uses the
same file across scenes, so a recurring character stays identical.

Do not re-source or regenerate an asset that the manifest already provides, and do not silently fill
gaps. Render REQUIRES every one of the selected section's assets to be ready before it builds anything
(see the All Section Assets Ready Gate). If any asset is missing on disk or is marked `prompt-ready /
awaiting generation` / `awaiting drop`, STOP and tell the user to finish `visual-implement` for those
assets, then rerun render. Produce a missing asset yourself only when the user explicitly asks for that
specific asset this run, and document it in `IMPLEMENTATION.md` and `05-production-board.md`.

Write or update:

- `projects/<slug>/05-production-board.md`
- `projects/<slug>/section-previews/section-XX-kebab-section-name/`
- `projects/<slug>/hyperframes/review/section-XX.html`
- `projects/<slug>/hyperframes/index.html` only as the current active mirror when useful
- `projects/<slug>/renders/section-XX-kebab-section-name/` only when the user explicitly asks to export an MP4/WebM

When this skill creates, updates, or reruns section preview files, every later output for the affected section becomes stale.

List stale downstream files in chat. Do not silently delete them.

## Required Context

Read these before rendering:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`
9. `.agents/_shared/channel/production-workflow.md`
10. `.agents/_shared/channel/brand-system.md`
11. `.agents/_shared/systems/visual-production.md`
12. `.agents/_shared/systems/audio-feedback-quality.md`
13. `references/memory.md`
14. `references/render-motion-rules.md`
15. `references/output-formats.md` before writing outputs
16. the chosen project files:
    - `02-script.md`
    - `03-voiceover.md`
    - `04-visual-plan.md`
    - the selected section's `voiceover/section-XX-*/section-XX-word-timings.json` when present (word-level voice timing; the source of truth for cue `data-start` values)

Also read active HyperFrames implementation guidance when available:

- the bundled `hyperframes` skill for composition rules
- the bundled `hyperframes-cli` skill for CLI commands
- existing project `section-previews/` and `hyperframes/` files when updating an existing section

Use the HyperFrames skill for core composition mechanics: HTML as source of truth, layout before animation, deterministic GSAP timelines, correct `data-start` / `data-duration` / `data-track-index`, audio as an `<audio>` clip, synchronous timeline registration, and CLI validation.

For `Why It Works` board-video style, channel review rules override generic decorative motion defaults: a cue can intentionally hard-show on the spoken beat when that improves readability and voice sync. Do not add animation merely to satisfy a generic "everything enters" instinct.

## Project Selection Gate

Always resolve the target project before rendering.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `04-visual-plan.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find render candidates.

A render candidate has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `03-voiceover.md`
- non-empty `04-visual-plan.md`
- at least one section voiceover folder
- at least one section visual-plan folder

When multiple candidates exist or context is unclear, ask the user to choose before writing files.

Do not create a new project folder in this skill.

## Required Inputs Gate

Before section selection or writing files, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `03-voiceover.md`
- non-empty `04-visual-plan.md`

If `02-script.md` does not contain parsable sections in the form:

```text
## Section N: Section Name
```

stop and ask the user to rerun `script-draft` or fix the script structure first.

If `03-voiceover.md` is missing, empty, or older than `02-script.md`, stop and ask the user to run or rerun `voiceover`.

If `04-visual-plan.md` is missing, empty, or older than `03-voiceover.md`, stop and ask the user to run or rerun `visual-plan`.

## Section Selection Gate

Render must get an explicit target section before writing files.

The target must be selected by the user as `All` or as a specific section number/name in the current request or in the section-choice response.

If no explicit section target is present, ask and stop before file edits, HyperFrames commands, server starts, or renders.

Do not infer the target section from:

- active project state
- latest reviewed section
- next unfinished section
- existing section preview
- missing preview output
- prior chat context

Preferred option order:

1. `All`
2. `Section 1: <name>`
3. `Section 2: <name>`
4. Continue through the section list

Important:

- `All` means build each section as its own preview project and start each on its own section port.
- `All` does not mean one unified preview on port `1000`.
- Unified/final assembly is a separate mode and should run only when the user explicitly asks to unify approved sections.

Fallback selection text:

```markdown
Choose render target:

0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

## Section Readiness Gate

For each selected section, verify:

- matching section voiceover folder exists under `voiceover/`
- matching section visual-plan folder exists under `visual-plan/`
- section visual-plan file exists and is non-empty
- section voiceover includes an audio file or clearly documented TTS status
- EVERY asset the section needs is ready (see the All Section Assets Ready Gate below)

If selected section voiceover is stale versus `02-script.md`, stop and ask the user to rerun `voiceover`.

If selected section visual plan is stale versus the section voiceover or `04-visual-plan.md`, stop and ask the user to rerun `visual-plan`.

## All Section Assets Ready Gate (hard requirement)

Render is a compositor, not an asset producer. Do NOT build, update, or render a section until
**100% of that section's assets are ready**. Producing assets is `visual-implement`'s job.

Before writing any HTML, starting a server, or rendering for a selected section:

1. Open `projects/<slug>/assets/asset-manifest.md` and collect every asset the selected section
   references (match the section's scenes / the section visual-plan asset list to manifest rows). If
   the manifest is missing or does not list the section's assets, STOP and tell the user to run
   `visual-implement` for the section first.
2. For EACH referenced asset, confirm it is in a render-ready state:
   - `browse-real-photo` / `generate` / `reuse`: the file exists at `projects/<slug>/assets/<filename>`
     (manifest status `done` or `reused`). Verify the file is actually present on disk, not just listed.
   - `pose`: the pose PNG exists at `projects/<slug>/assets/poses/<filename>`.
   - render-built CSS construct: only ready if the manifest EXPLICITLY marks it as built in render (no
     file needed). A plan/manifest note like "render-CSS preferred" counts as ready; a bare missing
     file does not.
3. If ANY referenced asset is missing on disk, or its manifest status is `prompt-ready / awaiting
   generation`, `awaiting drop`, or otherwise not-yet-produced, STOP. Do not source, generate,
   screenshot, substitute, or placeholder it yourself, and do not build a partial section. Report the
   exact list of not-ready assets (filename + status) and tell the user to finish `visual-implement`
   for those assets (generate the prompts in ChatGPT / drop the files into `assets/` / source the
   photos), then rerun `render`.
4. Proceed only when every one of the section's assets is ready (file present, or explicitly
   render-CSS). Exception: if the user EXPLICITLY asks render, this run, to create or substitute a
   specific named missing asset, that single asset may be produced as a documented fallback (note it in
   `IMPLEMENTATION.md` and `05-production-board.md`). The default with any gap is to STOP, not to
   silently fill it.

For `All`, run this gate per section; build only the sections whose assets are fully ready, and list
the blocked sections with their missing assets.

## Request Modes

### Manual Studio Edit Preservation Mode

Use when the user says they edited the localhost/HyperFrames Studio preview manually, asks to save those edits, or asks for a future update without overwriting their changes.

Rules:

- Treat the live section preview `section-previews/section-XX-*/index.html` as canonical before any automated rewrite.
- Read and diff the current preview file before editing. Do not copy from `hyperframes/review/section-XX.html`, an older visual plan, or a previous generated draft over the live preview.
- Remove only the specific accidental artifact the user named or the evidence clearly identifies, such as an unreferenced VFX registry composition, a duration extension, or a duplicate effect layer.
- If Studio added `data-hf-studio-*` positioning attributes, preserve them unless they are part of the accidental artifact.
- After cleanup, verify root `data-duration` matches the section voiceover duration unless the user explicitly approved extra silent visual time.
- Record the preservation note in the section `IMPLEMENTATION.md` and `05-production-board.md`.

### Section Remake / Quality Recovery Mode

Use when the user rejects an existing section render as low quality, messy, slide-like, mismatched to voiceover, or using fake/non-channel WIT.

In this mode:

- remove only the failed section preview/render artifacts the user explicitly asks to remove
- keep upstream script, voiceover, project assets, and attribution files
- treat the selected section visual plan as stale when the user says it caused the bad result
- rebuild from `02-script.md`, the selected section voiceover timing, the channel WIT manifest, real/local assets, and approved reference style notes
- start with static hard-cut boards only
- do not add transitions, element entrance animation, or decorative motion unless the user asks after approving the static version
- use one main visual idea per big scene, then add small voice-timed cue changes inside that big scene
- avoid replacing the entire frame for every sentence when the spoken idea is still part of the same object, place, or mechanism
- use WIT only for emotional beats, not every scene
- write the override reason into `IMPLEMENTATION.md` and `05-production-board.md`

Good remake pattern:

```text
script line -> voice timing -> persistent big scene -> small cue overlay/change -> optional real WIT emotional reaction
```

For short hooks, a good structure is usually:

```text
big scene A for setup -> small cue changes for details
big scene B for problem/escalation -> small cue changes for consequences
big scene C for payoff -> small cue changes for final label
```

The viewer should feel the scene evolving, not sprinting through unrelated slides.

Approved short-hook quality pattern from `why-cheap-products-keep-getting-worse` Section 1:

- For a `20-25s` hook, target about `3` big scenes and `6-8` cue states unless the script clearly needs more.
- Start by choosing the big scenes, then decide which words need cue overlays inside each big scene.
- Combine related sentence beats into one cue state when they describe the same object or situation.
- Use labels first when the image already proves the point; do not draw extra marks just to repeat something obvious.
- Red circles/arrows are for exact evidence or correction only. If the mark does not explain the voiceover, remove it.
- Check callout placement using Studio/direct preview screenshots during normal render work. Use exported MP4 frames only when the user explicitly asked for video export.
- WIT should be visibly readable as the emotional audience surrogate. If the face/expression is small in Studio or contact sheet, enlarge WIT.
- WIT-heavy beats should use the funniest approved pose that fits the emotion. Do not settle for a neutral corner pose when a panic, facepalm, suspicious, betrayed, or payoff pose exists.
- Do not overuse WIT. In short sections, WIT is emotional punctuation; default to about `1-2` WIT beats per persistent big scene unless the voice rhythm clearly needs more.
- Guard WIT crops: face, head, shoulders, and important props must not look accidentally cut off. Intentional edge-peek crops are allowed only when the expression still reads clearly.
- Ordinary sequential labels should hard-show on the spoken beat. Reserve smash/pop/stamp/slide motion for emphasized words, proof marks, or payoff labels.
- Avoid translucent white wash overlays on real/object photos unless they are required for readability and documented. Real texture should stay visible.
- Keep static hard cuts; no transitions or animation until the static version is approved.

Approved explanatory-list recovery pattern from `why-cheap-products-keep-getting-worse` Section 4:

- For a `30-45s` section that lists many small parts/features/support details, target about `3` big background scenes and `5-8` cue states unless the script has separate mechanisms.
- Use a few strong real/object backgrounds as the base. Let the photo texture do work instead of adding many small images.
- Compress lists into memory labels. Example: `FABRIC + STITCHING + HINGE`, `REPAIRABLE`, `SPARE PART STILL EXISTS`, `LESS FUTURE BUILT IN`.
- Use generic CSS overlays for risky mockup targets such as phones, printers, branded devices, UI screens, or people; do not use cluttered/risky references directly.
- Make WIT a giant emotional read on only the major beats, roughly one beat per big scene. Keep no-WIT beats for explanatory labels and object evidence.
- Reject scattered product-part trays, piles of mini cards, many floating images, and paragraphs of labels. If a paused frame cannot be read in about one second, simplify before adding motion.

Approved synthetic-failure recovery pattern from `why-cheap-products-keep-getting-worse` Section 5:

- If the user rejects a section because it has no real image, looks too normal, uses boring WIT, or feels like many small boring things combined, do not polish the same CSS-only mockup.
- Treat the existing visual plan/render as stale for that section unless the user explicitly says to preserve it.
- Rebuild from the script, voice timing, approved reference sections, real/local image assets, and the WIT manifest.
- Choose one real/object texture or generated-real support base per big scene before adding labels.
- Keep the big scene count small and persistent; for `30-45s` explanatory sections, default near `3` big scene bases and `5-8` cue states.
- Replace neutral WIT poses with emotionally specific approved poses tied to the joke, such as suspicion, panic, trapped, betrayed, evidence, or money panic.
- Compress feature lists into one or two readable labels. Do not make a separate prop, mini card, or floating image for every noun in the sentence.
- Verify the recovery with a direct preview screenshot/contact sheet and ask: does each frame have a real texture anchor, a clear main idea, and a WIT pose that feels intentionally funny?
- Record the rejected pattern and the new recovery source in `IMPLEMENTATION.md`, `05-production-board.md`, and `references/memory.md`.

Do not keep polishing a visual plan after the user identifies that plan as the failure source.

### Section Preview Build Mode

Default mode.

Create or update:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/
projects/<slug>/section-previews/section-XX-kebab-section-name/index.html
projects/<slug>/section-previews/section-XX-kebab-section-name/DESIGN.md
projects/<slug>/section-previews/section-XX-kebab-section-name/package.json
projects/<slug>/section-previews/section-XX-kebab-section-name/hyperframes.json
projects/<slug>/section-previews/section-XX-kebab-section-name/assets -> junction to ../../assets
projects/<slug>/hyperframes/review/section-XX.html
projects/<slug>/05-production-board.md
```

Start or reuse the section preview server on port `1000 + section number`.

### Section MP4 Render Mode

Use only when the user explicitly asks to export video, render an MP4, render a WebM, create a video file, or produce a final/draft export file.

Do not create MP4/WebM files during normal render, preview, animation, timing, QA, or review-fix work. Use HyperFrames Studio, direct composition URLs, screenshots, snapshots, contact sheets from screenshots, and `lint` / `validate` / `inspect` checks instead.

Run HyperFrames checks first:

```text
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
```

Then render to:

```text
projects/<slug>/renders/section-XX-kebab-section-name/
```

Use draft quality for iteration unless the user asks for final quality.

After rendering:

- run `ffprobe` on the exported MP4 and record duration, video size, fps, video codec, and audio codec
- delete stale `frame-*.png` files before extracting new QA frames
- extract key frames from the exported MP4 at current cue timestamps, not old timestamps
- create a contact sheet from the extracted frames
- inspect any user-reviewed/problem frame individually at full resolution
- if a contact sheet contains stale frames from an earlier cue count, regenerate it before handoff

### All Sections Mode

Use when the user chooses `All`.

Build each section as a separate section preview project.
Start each selected section on its own port:

```text
Section 1 -> 1001
Section 2 -> 1002
Section 3 -> 1003
```

Do not combine sections into one preview.

### Unified Preview Mode

Use only when the user explicitly asks to unify, assemble, combine, or preview the whole video.

Prerequisites:

- all required section previews exist
- sections intended for assembly are approved or the user explicitly asks for a rough assembly

Use port `1000`.

Do not run unified preview on any section port.

### Improve Memory Mode

Use when the user reviews render/build behavior and gives reusable lessons.

Update in this order:

1. affected project `05-production-board.md` or section implementation notes
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

## HyperFrames Build Rules

Use the active `hyperframes` skill guidance as the source of truth for composition HTML.

Core rules:

- HTML is the source of truth.
- Use simple board scenes first.
- Build the static hero frame before animation.
- Wire voiceover audio as a proper `<audio>` clip.
- Use `data-start`, `data-duration`, and `data-track-index` correctly.
- Register GSAP timelines synchronously.
- Keep all motion deterministic.
- Do not use `Math.random()`, `Date.now()`, async timeline construction, or infinite repeats.
- Do not call media `play()`, `pause()`, or `seek()`.
- Do not hide standalone compositions inside `<template>`.
- Do not use real private data, real app logos, or unsafe copyrighted screenshots.

Channel-specific rules:

- Use WIT as the audience surrogate, not a presenter.
- Use only real channel WIT PNG poses from the current project `assets/wit/manifest.json` or approved shared WIT manifest.
- Do not draw, approximate, SVG-build, CSS-build, or generate random WIT when real WIT pose PNGs exist.
- Reserve WIT for emotional beats: suspicion, betrayal, panic, confusion, judgment, evidence, trapped, or payoff.
- Do not put WIT in every board if the object or evidence carries the narration better.
- When WIT appears in a 1080p section, scale it large enough that facial emotion reads in normal Studio and screenshot review. A full-body WIT reaction is usually too small if it is below roughly one-third of the frame height.
- For every emotional WIT beat, the visible WIT character footprint must occupy at least `1/3` of the frame in the actual preview screenshot/contact sheet. Measure the visible character, face, body, and props, not the transparent PNG bounds or CSS box.
- For strong emotional beats, target `1/3` to `1/2` visible frame presence by default, or more when it improves the joke and does not block text/evidence.
- Do not default WIT to a full-body lower-corner sticker. For strong reaction/payoff beats, actively consider Section-1-style giant placements: oversized behind-layer WIT, half-body rising from the bottom edge, side peeks, corner peeks, upside-down top entrances, looming faces, WIT tucked behind/around the main object, or WIT hiding behind a wardrobe/product/tag/box/screen. Lower-body or side body crop is acceptable when it makes the emotion bigger.
- Verify WIT safe crop in direct preview screenshots. Avoid accidental cuts through the face, head, shoulders, or important props; if it looks broken rather than intentionally peeking, reposition or scale before handoff.
- WIT size + vertical anchor default (owner-confirmed 2026-06-22): make WIT BIG (≈`1/3`–`1/2` frame) AND HIGH. For a bottom-edge peek, anchor around `bottom:-250…-340px` (not `-540…-600px`, which bleeds the body off-canvas and reads as "too low / covered by the frame") so head+glasses+torso+arms are inside the frame and only the legs crop. If a bigger WIT would cover a label/board/chat bubble/UI, RE-ARRANGE those other items (opposite side / up / down) instead of shrinking or lowering WIT - WIT is the emotional subject and content makes room for it. Confirm head clears the top edge too.
- Ground UI scenes on real photos: do not ship a section of full-frame CSS UI / labels on flat gradients - it reads as "not lively / no background." Float the crisp real-UI (chat, Meet grid, Trello, spreadsheet, calendar) as a drop-shadowed `.screen` over a real, people-free photo (light scrim), and prefer a photo that echoes the line. Stylized scenes (e.g. a CSS stage) also get a real photo base (e.g. a real red-curtain stage).
- STANDING VIVID-HOOK TEMPLATE (owner-confirmed 2026-06-23, from the `why-everything-is-a-subscription-now` Section 1 remake): build every section to `vivid on-topic OBJECT photo bases -> VARIED CSS idea-devices per beat -> giant WIT that VARIES per scene`. Vary the idea-device per beat (app-grid tiles, kinetic number/counter, notification toasts, free-trial countdown, full-width EXPIRED/system banner, padlock wall, bold kinetic headline, badges) - do NOT reuse one handwritten cream label box for every idea. VARY WIT across scenes in side (left/center/right), scale, vertical anchor, and pose - never park WIT on the same side with text always opposite; flip the text/UI to the side WIT isn't using and rearrange around WIT. A reusable CSS kit lives in `projects/3-why-everything-is-a-subscription-now/section-previews/section-01-hook/index.html` (tiles, toasts, countdown, banner modal, padlock, counter, payoff) - copy/adapt it. Current WIT poses are TRANSPARENT RGBA cutouts (keyed in place 2026-06-28) - composite them directly from `assets/poses/`, NO chroma-key step and NO `poses-keyed` folder; always VIEW a pose before first use.
- BUILD TO THIS BAR ON THE FIRST PASS - do not render a plain version and wait for rejection (owner-confirmed 2026-06-24). On `why-buy-1-get-1-beats-50-off` the owner rejected plain first passes three times before each was rebuilt to this template. Hard requirements every section:
  - base grade: keep the photo BRIGHT and VISIBLE - `filter: saturate(~1.1) contrast(~1.06) brightness(~0.7–0.85)`. Do NOT cover it with a heavy dark overlay (owner rejected "dark areas overlay"). Use AT MOST a subtle edge vignette (`radial-gradient(... rgba(4,5,10,0) 54%, rgba(4,5,10,0.38) 100%)`) or a light text-side gradient that fades to transparent before mid-frame; never a full-frame dark scrim. Get text contrast from text-shadow + the device cards' own backgrounds. Still never ship a bare/flat base (plain wood, objects-on-white, a dim antique) - that reads as "backgrounds too simple."
  - a GIANT kinetic NUMBER (`font-size ~250–320px`, the `.bignum` device) is the hero for any money/count beat; a plain receipt/label card is only a small supporting strip. Flat CSS label-cards as the main element read as "texts/items too simple."
  - WIT giant: `width ~1120–1300px` at 1920×1080 (was rejected at ~780px as "too small"); anchor high (`bottom ~ -300…-340px`), legs-only crop; vary side/scale/pose per scene; arrange every device OPPOSITE the WIT and fix any device-over-WIT-face overlap before handoff.
  - ~5 scenes for a ~30s section (not 3); lots of pop/smash/stamp motion.
  - if the owner asks to make a section "funnier," do NOT swap in a cute mascot prop (a piggy bank was rejected as "even worse") - keep the literal-but-vivid base and amplify the giant WIT pose + dry labels + kinetic devices.
  - second reusable kit to copy: `projects/4-why-buy-1-get-1-beats-50-off/section-previews/section-03-the-receipt-knows/index.html` (bignum `$5→$10`, stamp, toast, banner, glowing `payoff` FREE, giant WIT across 5 scenes).
  - FRESH bases per section (don't be lazy): do NOT reuse the same photo files (cash/coins/curtain) across sections - the owner rejected that ("you reuse too many images from other sections"). Each section gets its own distinct sourced bases; a recurring motif must use different photos + distinct grades.
  - NO stacked/overlapping text: one hero device + at most one short caption per scene, vertically spaced (≥~150px), revealed sequentially on their words, all OPPOSITE the giant WIT, with a side-gradient scrim on the text half. The owner rejected a section because "texts are covered by many texts." Verify the contact sheet shows no text-near-text crowding before handoff.
- A full-screen "system" message reads best as a TOP BANNER (z above WIT); HIDE the underlying toast/UI column when it takes over, or the banner sits over those boxes (reads as text-covering-boxes).
- Intentional WIT crop must never cut the face, glasses, head, shoulders, mouth, key prop, or readable emotion. If a contact sheet shows face/head/shoulder crop, treat it as a blocking layout bug and adjust before handoff.
- Protect WIT's emotion from text too. In payoff/reaction beats, final tags, stamps, labels, and cards must not cover WIT's face, eyes, mouth, or key prop. Create separate text and WIT zones instead of relying on z-index or partial overlap.
- Protect lower-third readability from subtitles too. Important labels, receipts, stamps, arrows, boxes, and payoff props near the bottom edge should be nudged upward into a subtitle-safe zone unless they are intentionally background-only.
- If the current approved WIT library lacks a pose that expresses the beat, create or request a new approved WIT pose asset and save it in the shared/project WIT asset library before using it.
- Use real-life assets as evidence, not decoration.
- When the visual plan includes real-world references, inspect those images and source notes before using generated support assets.
- Treat generated images as support or clean production bases unless the visual plan explicitly approves them as the primary asset.
- Before using any planned image as a direct scene base, compare it against adjacent big scenes. If a non-callback scene repeats the same background, object setup, camera language, or material mood as another scene, rebuild it as a more distinct CSS/self-made/generated scene and document the change.
- Do not force every collected reference image into the render. Inspect each planned asset, use it only if it improves the end viewer result, and mark skipped images as reference-only in attribution/implementation notes.
- Use hard cuts by default.
- Do not animate every cue element. For normal labels, notes, and supporting props, use hard-show timing exactly on the spoken beat.
- Use impact motion such as smash, stamp, shake, snap, or pop only for emphasized spoken words, evidence marks, or payoff labels.
- Use red markup for corrections and punchlines.
- Tie an underline/emphasis bar to its text, not to fixed coordinates. Use a `border-bottom` (or `::after`) on the inline-block text span so the underline always equals the text width, stays centered, and rotates with the label. Do not place a separate absolutely-positioned fixed-width underline `div` under text - it drifts and mismatches the text width when the text or font changes.
- Keep short payoff phrases on one line: size the card to fit and add `white-space: nowrap` to the text span so a payoff tag never wraps awkwardly mid-phrase.
- Red markup must point to or change a specific meaningful object; do not add decorative circles, rectangles, or marks that do not explain the narration.
- Do not mark obvious details with meaningless graphics. Example: do not draw four random red leg marks over a chair just because the voice says `four legs`; a clear label is enough unless a specific leg matters.
- Labels must be readable when paused.
- Cue-critical visuals must be readable on the cue frame.
- Callout circles, arrows, stamps, and labels must align to the exact object they reference in direct preview screenshots. Check exported frames only for explicit video export requests.
- Do not wash out real object/failure photos with a white overlay by default. Preserve the photo texture unless text readability requires a local label background.
- Voice sync comes first.
- Cue-critical visuals must be fully readable on the cue frame, not still traveling into place.
- For rejected/remade sections, prefer sparse illustrative boards over slide layouts: one object, one joke/evidence point, one short label.
- For rejected/remade explanatory-list sections, prefer a few real/object photo backgrounds with compressed category labels over separate cards for each listed item.
- Use a local font file for handwritten labels when possible so preview/export output does not fall back to an ugly default font.

If HyperFrames global guidance conflicts with the current channel rules, preserve the channel's approved simple-board style unless the user explicitly asks for a different render style.

### HyperFrames Implementation Pattern For WIW

Before writing GSAP:

- build the most readable static/end-state layout for every big scene and cue
- place WIT, labels, price tags, receipts, callouts, and props where they should land at full readability
- verify that WIT does not cover text/evidence and that payoff text/stamps/cards do not cover WIT's face/expression in the static layout
- decide whether each cue element is `static`, `hard-show`, `impact`, or `transition`

For ordinary delayed cue elements, prefer this pattern:

```js
const show = (target, hideAt, at) => {
  tl.set(target, { opacity: 0 }, hideAt);
  tl.set(target, { opacity: 1 }, at);
};
```

For emphasized beats only, use a small helper such as:

```js
const smash = (target, hideAt, at) => {
  reveal(target, hideAt, at, { y: 24, scale: 1.2, opacity: 0 }, { duration: 0.18, ease: "back.out(1.9)" });
};
```

Do not rely on delayed `gsap.from()` to hide cue elements before they enter. Set the hidden state at the cue start, then show or animate at the intended spoken beat.

### Render Review-Prevention Pass

Run this pass after reading the visual plan and before writing or editing HTML:

- Voice cue map: build it from the section `section-XX-word-timings.json` when present; list the exact word/phrase (with its timestamp) that triggers each label, prop, WIT, and markup, and pin cue `data-start` + every staggered reveal to those timestamps. Re-pin all downstream cues/scenes/reveals whenever one cue moves.
- Big-scene sanity: keep persistent scenes while the voice describes the same object or mechanism.
- Cue density: each cue should add only one or two meaningful changes.
- List compression: when a section names many related parts/features, group them into a small number of memory labels and background scenes before writing HTML.
- Motion density: ordinary labels and notes should hard-show; only emphasized beats get impact motion.
- WIT density: count WIT appearances per big scene; reduce if WIT reacts to every cue.
- WIT scale/placement/crop: if WIT is an emotion beat, verify visible WIT footprint reaches at least `1/3` of the frame; avoid tiny corner placement; test giant/behind-layer, corner-peek, upside-down top, object-hiding, side-peek, or lower-edge half-body placement while keeping labels/evidence readable.
- WIT safe-crop: check face/head/shoulders, glasses, mouth, and important props before handoff; only lower body/edge crop is acceptable.
- WIT/text collision: check both directions. WIT must not cover text/proof/payoff, and text/proof/payoff must not cover WIT's face/expression.
- Subtitle-safe lower area: check lower-third labels, receipts, arrows, boxes, and payoff props; move cue-critical elements slightly upward when YouTube subtitles would likely cover them.
- Markup meaning: every circle/arrow/underline must point to the exact object it explains.
- Scene differentiation: direct scene bases should not repeat adjacent visual language unless intentional.
- Real texture anchor: if a rejected/remade section felt synthetic, boring, or "too normal", each big scene needs a real/object texture or generated-real base unless there is a documented reason not to.
- HyperFrames mechanics: data attributes, audio, deterministic GSAP, and timeline registration must follow the HyperFrames skill.

If the visual plan is missing one of these decisions, render must make the decision explicitly and document it in `IMPLEMENTATION.md` / `05-production-board.md`; do not blindly build a weak plan.

## Voice Sync And Motion Rules

Read `references/render-motion-rules.md` before implementing animation or transitions.

Non-negotiable summary:

- everything on screen must describe the voiceover at that moment
- build a hard-cut timing pass before adding transitions
- choose transitions per scene boundary, not one default effect everywhere
- remove or simplify transitions that damage voice sync
- design every meaningful element's entrance, hold, emphasis, and exit against spoken cues

### Voice-Sync Timing Contract (word-timings-first)

Timing mistakes are the most common review failure. Pin every time value to the actual narration, never to estimates or copied prior values.

- Before assigning any `data-start`, look for the section's word-level timing file:
  `projects/<slug>/voiceover/section-XX-*/section-XX-word-timings.json` (faster-whisper `words[]` + `segments[]` with `start`/`end` seconds). If it exists, it is the source of truth - build the voice cue map from it.
- If the word-timings JSON is missing, GENERATE it from the section audio before timing cues - do not default to estimating. Estimating is a last resort and reliably drifts (a Section 4 estimated pass landed the parts list ~4s late). Estimate only if generation truly fails, and then label every cue time `estimated`.
- Working generation recipe on this Windows box (no whisper-cpp, no Python - so `hyperframes transcribe` fails): use Whisper via `transformers.js` (WASM, no native deps).
  1. `npm.cmd install --prefix %TEMP%/wiw-whisper --no-save @xenova/transformers@2.17.2`
  2. decode the mp3 to 16 kHz mono f32 with the static ffmpeg: `ffmpeg -i <mp3> -ar 16000 -ac 1 -f f32le out.raw`
  3. Node ESM: read `out.raw` into a `Float32Array`; `const t = await pipeline('automatic-speech-recognition','Xenova/whisper-tiny.en'); const o = await t(audio,{return_timestamps:'word',chunk_length_s:30,stride_length_s:5});` → `o.chunks` is `[{text, timestamp:[start,end]}]`.
  4. write `voiceover/section-XX-*/section-XX-word-timings.json` with `{transcript, words:[{word,start,end}]}` and pin every cue/reveal to it. `whisper-tiny.en` aligns clean TTS narration well and runs in ~1 min.
- Pin each cue's `data-start` to the word that triggers it. The bill shows on "the repair costs"; the stamp on "almost as much"; "NEW ONE" on "buying a new one". Do not start a cue several seconds before or after its words.
- Stagger within-cue reveals to each spoken phrase. A cue that contains several labels, a quote, or a list (policy rows, checklist questions) must reveal each item on its word via GSAP `tl.set(target,{opacity:0},cueStart); tl.set(target,{opacity:1},wordStart)`, not all at cue start. "Show each item when the voice says it" is the default for any on-screen list.
- Cascade on every move: when one cue's start changes, re-pin every downstream cue `data-start`, every scene-clip cut, and every GSAP reveal so the whole chain stays aligned. A late cue silently pushes all later cues late.
- Final/payoff reveals: bring an emotional WIT in slightly before the punchline line if it helps comedic timing, but land the spoken tag/quote on its actual words.
- After timing, set the section `package.json` `inspect --at` (and your snapshot `--at`) to the new cue mid-points, then regenerate snapshots - stale QA timestamps hide drift.

### Timing Mechanics That Block Validation

- Accumulating elements that must stay visible together (e.g. three barrier trays that build up) cannot overlap on one track - `overlapping_clips_same_track` is a hard error. Put each on its own `data-track-index` and give it `class="... clip"` plus a stable `id`. (A bare timed `<div>` with no `clip` class shows for the whole composition.)
- Guard floating-point cue boundaries: `5.3 + 4.56 = 9.860000000000001` overlaps a clip starting at `9.86`. Trim the duration (e.g. `4.55`) so each clip ends at or before the next start.
- Intentional off-canvas elements (e.g. a giant WIT at `right:-420px`) trip `clipped_text` / `text_box_overflow` / `canvas_overflow`. Marking the image with `data-layout-allow-overflow` is not enough - add `data-layout-allow-overflow=""` AND `style="overflow: visible;"` to the wrapping cue `div`; the composition root still clips at the canvas edge so the visual is unchanged.
- Verify timing with `hyperframes snapshot --at <one timestamp per cue, including each staggered reveal just after it fires>`; read the contact sheet, confirm each element is present exactly when its words are spoken, and that nothing is still flying in on its cue frame.

## Asset Rules

Use one video-level shared asset library:

```text
projects/<slug>/assets/
```

Each section preview project should expose that folder through a local `assets` junction:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/assets
```

Do not copy the full assets folder into each section preview.

On Windows, create a junction only after verifying the target path resolves inside the current project:

```powershell
New-Item -ItemType Junction -Path ".\assets" -Target "..\..\assets"
```

If a local `assets` path already exists:

- if it is the correct junction, keep it
- if it is a wrong junction or copied folder, stop and report it before changing

Document every production asset in:

```text
projects/<slug>/assets/ATTRIBUTION.md
```

Before direct production use, read the selected section's visual reference board and `assets/visual-references/.../source-notes.md` when present.

Use real-image references as follows:

- `safe asset`: may be used directly with required attribution/source notes
- `mockup target`: use as a model for a recreated/cropped/covered asset; do not expose risky source text
- `inspiration only`: inspect for texture/composition, but do not copy into the final render
- `reject`: do not use

If the section has a `real-world/` reference folder, inspect those assets before generating or choosing replacement visuals.

If a real source has attribution, share-alike, logo, private-data, or unclear-copyright risk, either handle the requirement in `ATTRIBUTION.md` or use a generated/self-made replacement that preserves the real-world texture without copying unsafe material.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Parse `02-script.md` sections.
4. Run the Section Selection Gate.
5. Run the Section Readiness Gate AND the All Section Assets Ready Gate for selected sections; stop (or skip a blocked section in `All` mode) if any of a section's assets are not ready.
6. Read required shared context, skill memory, output formats, and HyperFrames guidance.
7. For each selected section:
   - compute the fixed port: `1000 + section number`
   - create or update the section preview project
   - create or verify the local `assets` junction
   - inspect the active WIT manifest before using WIT
   - create a voice cue map from the section voiceover and either the section visual plan or, in remake mode, the script plus approved reference style
   - run the Render Review-Prevention Pass
   - decide the big-scene count and cue-state count before writing HTML
   - create a big-scene/cue plan where each big scene holds one main visual idea and cue overlays add only meaningful labels, props, or WIT reactions
   - count WIT appearances per big scene and reduce them before implementation if the rhythm is dense
   - classify each cue element as `static`, `hard-show`, `impact`, or `transition` before implementing motion
   - implement `index.html` from the section visual plan, or from the script/voice timing when remake mode explicitly skips the visual plan
   - wire selected voiceover audio
   - implement a hard-cut timing pass first
   - add per-boundary transitions only after voice sync is working
   - design element entrances, holds, emphasis, and exits against spoken cues
   - verify WIT-heavy and emphasis-heavy beats with direct preview screenshots or a contact sheet from runtime seek
   - create or update `DESIGN.md`
   - create or update `package.json` and `hyperframes.json`
   - copy or mirror the canonical standalone section into `hyperframes/review/section-XX.html`
   - run `lint`, `validate`, and `inspect`
   - fix blocking issues
   - if WIT, labels, or callouts were materially changed, create direct preview screenshots or a contact sheet from runtime seek
   - do not render MP4/WebM or create video export files unless the user explicitly asks to export video
   - when the user explicitly asks for video export, run `ffprobe`; clear stale extracted frames; extract key frames from the exported MP4; inspect a contact sheet; inspect any problem frames individually
   - start or reuse the preview server on the fixed section port
   - record Studio and direct composition URLs
8. Write or update `projects/<slug>/05-production-board.md`.
9. Run the Downstream Stale Gate.
10. Respond with the Chat Response Format.
11. Stop before review, upload, or learning unless explicitly asked.

## Server Rules

Preview servers are long-running processes.

When starting a server on Windows, use a hidden background process and keep it alive:

```powershell
Start-Process -WindowStyle Hidden -FilePath "powershell" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"Set-Location '<section-preview-dir>'; npx --yes hyperframes@<version> preview --port <port> *> preview.log`""
```

Use the HyperFrames version already used by the project when present. If no project precedent exists, use the currently available HyperFrames CLI and record the version.

After starting, verify the server responds and report:

```text
http://localhost:<port>/#project/<section-preview-folder-name>
http://localhost:<port>/api/projects/<section-preview-folder-name>/preview/comp/index.html
```

Do not leave an interactive foreground server blocking the turn.

## Output Formats

Use `references/output-formats.md` for:

- `05-production-board.md`
- section implementation notes
- chat response

## Downstream Stale Gate

After creating, updating, or rerunning a section preview, check for downstream files:

- `06-review.md`
- `07-upload.md`
- `08-self-learning.md`
- unified preview/render files when they exist

If any exist for the affected section or full video, list them as stale in chat.

Do not delete downstream files unless the user explicitly asks.

## Quality Bar

A section render is ready for review when:

- the selected section was explicitly chosen
- section voiceover and visual plan are current
- every asset the section references is ready before build: each file present in `assets/` (or `assets/poses/`), or explicitly marked render-CSS in the manifest; none `prompt-ready / awaiting generation` or `awaiting drop`
- section preview project exists separately from other sections
- section uses fixed port `1000 + section number`
- `index.html` implements the visual plan without requiring review to infer missing boards
- audio is wired and synchronized to visual cues
- every visible scene and element matches the current voiceover beat
- short hooks use connected big scenes with small cue changes when several lines describe the same object or situation
- short hooks have an intentional cue count; for `20-25s`, prefer `6-8` cue states over many rapid micro-scenes
- transitions are chosen per boundary and do not damage voice sync
- key labels enter/emphasize on the spoken word they support
- `lint`, `validate`, and `inspect` pass, or remaining warnings are documented and non-blocking
- exported MP4/WebM frames are checked only for explicit video export requests; normal render/preview work should not create video files
- extracted MP4 frame folders are cleaned before regeneration only when an explicit export request required an MP4/WebM
- if WIT appears, it is a real pose PNG from the approved WIT manifest
- the first `3` seconds show the topic object or situation
- the first `5-6` seconds show the contradiction or hidden detail when the hook depends on one
- labels are readable
- WIT emotion is visible and useful
- WIT density follows the voice rhythm; short sections should normally stay around `1-2` WIT beats per big scene
- emotional WIT visibly occupies at least `1/3` of the frame in Studio, direct preview screenshots, and screenshot contact sheets; transparent PNG padding or CSS box size does not count
- strong WIT emotion beats do not look like small full-body corner stickers; if needed, WIT uses a giant behind-layer, side-peek, lower-edge half-body, or oversized-face placement
- WIT face/head/shoulders and important props do not look accidentally cropped
- WIT does not cover labels, proof objects, or payoff text
- payoff text, stamps, and final cards do not cover WIT's face/expression when WIT is carrying the emotional beat
- lower-third cue-critical elements are not parked in the likely YouTube subtitle zone
- ordinary labels hard-show on beat unless they are true emphasis moments
- impact animation is reserved for emphasized words, proof marks, contradiction labels, or payoff text
- red circles, arrows, and marks point to the intended object, not nearby empty space
- decorative marks that do not clarify the voiceover have been removed
- real/object photos keep their natural texture unless a local label background is needed for readability
- assets are referenced through the shared project asset library
- source notes and attribution are updated
- `05-production-board.md` records paths, commands, checks, and URLs
- preview server is running or a clear failure reason is reported

## Hard Fails

Reject or stop before finishing if:

- the project lacks `04-visual-plan.md`
- the selected section lacks voiceover
- the selected section lacks visual plan
- a section is built/rendered while ANY of its assets are missing on disk or still `prompt-ready / awaiting generation` / `awaiting drop` in `assets/asset-manifest.md` (render must stop per the All Section Assets Ready Gate, not build a partial section)
- render silently sources, generates, screenshots, substitutes, or placeholders a missing asset instead of stopping (allowed only when the user explicitly asks for that specific asset this run, documented)
- the user has not explicitly selected `All` or a specific section
- the target section is inferred instead of selected
- scene content does not match the current voiceover beat
- the render uses fake, random, drawn, SVG, or CSS WIT when approved WIT PNGs exist
- WIT is used as filler in every scene instead of only where it clarifies emotion
- WIT appears on every cue or more than `2` times in a short-section big scene without a clear voice-rhythm reason
- a user-rejected visual plan keeps controlling the remake after the user explicitly said to skip it
- a user-rejected synthetic/CSS-only section is merely polished instead of rebuilt around real/object texture, stronger WIT, and fewer cue ideas
- a short remake resets to a completely unrelated full-frame scene on every voice cue when the narration is still describing the same object or situation
- a list-style section turns into scattered mini cards, many floating images, or too many independent labels instead of a few persistent backgrounds and cue changes
- a remade hook fails to show the topic object or contradiction in the first few seconds
- red markup is decorative, meaningless, or misaligned with the object it claims to identify
- WIT is too small to read the emotion at normal preview size
- emotional WIT occupies less than `1/3` visible frame presence without an explicit user-approved tiny/background reason
- WIT is a small lower-corner sticker on a beat where WIT is supposed to carry the main emotion
- WIT face/head/shoulders are accidentally cropped, WIT covers the main label/proof/payoff, or payoff text covers WIT's face/expression
- ordinary labels repeatedly fly/smash in and make the section visually dense
- cue-critical elements appear early because delayed animation did not hide them at cue start
- a `section-XX-word-timings.json` exists but cue `data-start` values were estimated or copied from a prior build instead of pinned to the word timings
- a multi-element beat or an on-screen list dumps all items at cue start instead of revealing each on its spoken word
- one cue's timing was changed without cascading the downstream cue/scene/reveal times
- accumulating same-track clips overlap, a floating-point boundary overlaps the next clip, or intentional off-canvas cues are not marked allow-overflow + `overflow:visible` on the cue div
- a real/object photo is globally washed out with a white overlay without a documented readability reason
- explicit-export MP4 QA uses a contact sheet that still contains stale frames from an older cue count or render
- transitions are added before hard-cut timing works
- the same transition effect is applied everywhere without per-boundary reasoning
- emphasized spoken words have no visual emphasis when the section depends on that cue
- the section preview tries to share one localhost with all sections
- a section uses port `1000`
- a section uses a random fallback port without explicit user approval
- unified preview is built when the user only asked for a section
- an MP4/WebM is created without the user explicitly asking to export video or render a video file
- assets are copied into each section instead of linked/junctioned without a reason
- HyperFrames checks fail with blocking errors
- the preview server is claimed running without verification
- generated or browsed assets are used without source notes
- the skill creates review, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- a port rule changes
- HyperFrames CLI commands or versions change
- section preview structure changes
- a render later fails review because of sync, labels, WIT, assets, or server setup
- a transition choice causes voiceover mismatch
- a repeated animation pattern makes the video feel boring or disconnected from narration
- the user approves or rejects a build pattern

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify promoted lessons as `Core`, `Experiment`, `Operational lesson`, or `Reject`.
