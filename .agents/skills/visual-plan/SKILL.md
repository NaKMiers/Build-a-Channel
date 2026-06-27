---
name: visual-plan
description: Create or update the step 4 visual plan for a Why It Works video project — the detailed, imagination-led blueprint of every scene. Use when the user asks for visual plan, scene plan, scene-by-scene screen direction, describe the visuals, plan the visuals, or step 4 of the Why It Works workflow. It builds ONE master plan per video and synced per-section copies, breaks the script into per-sentence (or few-sentence) scenes, and describes each scene in extreme detail (composition, every element, mascot pose, on-screen text, emotion, insight, element linkage, show-as-you-say timing, sound, color) plus an ASSET list per scene (type generate/browse/screenshot/reuse, filename, layout). visual-plan DESCRIBES only — it never writes image-generation prompts (that is visual-implement's job) and is not limited to the existing pose library (it may invent new poses/scenes if good, within copyright/law/YouTube community standards). Requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 03-voiceover.md and an explicit section selection with All first; writes only 04-visual-plan.md and the visual-plan/ section folders.
---

# Visual Plan

## Purpose

Run step `4` of the `Why It Works` video workflow.

The visual plan is the **backbone of the video's illustration**. It describes, scene by scene, exactly
what the viewer sees, so that a person (or a later skill) can imagine ~99% of every frame from the
text alone, then build it.

Two hard principles define this skill:

1. **DESCRIBE only — never write image-generation prompts.** This skill paints the scene in words and
   lists which ASSETS each scene needs (type + filename + layout). Turning an asset description into an
   image-generation prompt, and actually creating/finding the asset, is `visual-implement`'s job.
2. **Imagination is not limited.** Within copyright, law, and YouTube community standards, anything the
   plan describes must be buildable by all means — so describe whatever is funniest/clearest. The plan
   MAY invent brand-new mascot poses or whole new scene ideas; it is NOT restricted to the existing
   pose library. The library (`.agents/_shared/assets/wit/poses/`) is a starting palette, not a cage.

## One Master Plan, Synced Section Copies

There is exactly **one master visual plan per video**: `04-visual-plan.md`. It holds the video-level
direction plus every scene of every section.

Each section also gets its own file under `visual-plan/section-XX-*/`. A section file is an **exact
copy of that section's slice of the master**, prefixed with the video-level direction summary, so each
section "sees the whole video" and is never read in isolation.

Sync rule: the master and the section copies must ALWAYS agree. Whenever you create or edit a section's
scenes, write the same content into both the master `04-visual-plan.md` and that section's file in the
same run. Never let them drift.

## Scene Granularity

Cut scenes **per sentence, or a few sentences per scene** — never one static frame per whole section.
The reference standard (the Vui Vẻ-style explainer the owner studied) changes the visual on almost
every sentence: a new photo, a new mascot pose, or a clean mascot-only focus frame. The eye never
habituates. Target a visible change every few seconds, synced to the spoken line.

A few sentences MAY share one scene when they describe the same object/situation, but the default is a
new scene per sentence/beat.

## Pipeline Position

This is step `4` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`
- `projects/<slug>/03-voiceover.md`
- selected section voiceover output under `projects/<slug>/voiceover/`

Write or update:

- `projects/<slug>/04-visual-plan.md` (master)
- `projects/<slug>/visual-plan/section-XX-kebab-section-name/` (synced section copy + notes)

Downstream: `visual-implement` (creates the assets this plan names), then `render` (composites them).

If a required upstream file is missing, empty, or stale (older than its own upstream), stop and tell
the user which previous skill to run. When this skill creates/updates a section plan, the section's
implemented assets and render become stale — list them.

## Required Context

Read before planning:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/reference-channels.md`
8. `.agents/_shared/channel/learning-log.md`
9. `.agents/_shared/channel/brand-system.md`
10. `.agents/_shared/systems/visual-production.md`
11. `.agents/_shared/systems/script-learner-voice.md`
12. `references/memory.md`
13. `references/output-formats.md` before writing outputs
14. the mascot pose library: `.agents/_shared/assets/wit/poses/` and any pose reference notes (e.g. `analysis/vuive poses/pose.md` when present) so you can name exact poses
15. the chosen project files: `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`, `03-voiceover.md`

## Project Selection Gate

Resolve the target project before planning, in this order:

1. If the user names a slug/path, use it.
2. If the current chat clearly selected a project and it exists, use it.
3. If exactly one project has a completed `03-voiceover.md` and no/partial visual plan, smart-select and say so.
4. Otherwise list candidates and ask.

A candidate has non-empty `00`/`01`/`02`/`03` files and at least one section voiceover. Do not create
a new project here.

## Section Selection Gate

Get an explicit target section before writing files. Offer `All` first, then each section. Never infer
the target from active state, latest section, next-unfinished, or prior chat.

- `All` means produce each section as its own synced output (and the full master), NOT one giant
  collapsed scene table.

```markdown
Choose visual plan target:
0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

For each selected section, confirm the matching section voiceover exists and is not older than the
script; if word-level timing exists (`voiceover/section-XX-*/section-XX-word-timings.json`), prefer it
for scene timestamps.

## The Scene-Detail Standard (the core of this skill)

Every scene must be described at the depth where a reader can imagine the frame with no image. Use ALL
of these fields for every scene. "Too little detail to picture the frame" is a defect — fix it before
handoff.

For each scene:

1. **Line / beat** — the exact script text for this scene + local time range (from section voiceover).
2. **Role** — what this beat does in the video and how it links to the previous/next scene.
3. **Composition / layout** — the frame: background; positions of every element in approximate %;
   crop; z-order; which side each element sits; the thin gray horizon line if used.
4. **Elements (one block each)** — describe every visual element in concrete detail: what it is, what
   is inside it (for a photo/UI: the contents, framing, lighting, grade), size, treatment (float,
   drop-shadow, distortion, etc.).
5. **Mascot** — exact pose name (from the library) OR a clearly-marked NEW invented pose described in
   full; placement, scale (as fraction of frame), crop (what is intentionally cut), facing direction,
   expression. The mascot is a real character (color + personality), big and high — the soul of the
   scene; do not park it tiny in a corner.
6. **On-screen text** — exact words (channel language = English for WIW), handwritten style, position,
   color, tilt, underline/scribble, and when it appears. Edge/tone may be savage-but-clean per the
   channel tone rule.
7. **Emotion** — what the scene should make the viewer feel.
8. **Insight / joke** — the point or the gag this scene carries.
9. **Linkage** — why the elements sit together; the intended eye path (left→right, etc.).
10. **Show-as-you-say timeline** — element-by-element entrance/hold tied to the spoken words/syllables
    (e.g. "on 'thirty songs' → zoom the '30 songs' label"); mark hard-show vs impact (pop/smash/stamp).
11. **Sound** — any short SFX cue and where it ducks under narration.
12. **Color / contrast** — palette and what should pop on a phone.

Then list the scene's **ASSETS** (the handoff to visual-implement) — see below.

## Asset Listing Rule (handoff to visual-implement)

For each scene, list every asset it needs. For each asset record:

- `type`: `generate` | `browse-real-photo` | `screenshot/web-capture` | `reuse` | `pose`
- exact **description** (what it depicts) — detailed, but **NO image-generation prompt** (implement writes that)
- **filename** (kebab-case, `.png`) — the canonical name in `assets/`. If the same subject already
  appeared in an earlier scene, REUSE the same filename (`type: reuse`) so the character stays
  identical; do not invent a new file for the same thing.
- **layout/position** in the scene (left/right/center, crop, float) so render can place it
- isolated-element note: generated/browsed assets are ISOLATED elements (transparent/plain background),
  never a pre-composed full scene — render composites them.

Poses come from the library where one fits (`type: pose`, reference the pose filename). When the plan
invents a NEW pose, mark it `type: generate` with a vivid description and a new filename; visual-implement
will create it (and it can be added back to the library).

Safety bound on imagination: copyright, law, and YouTube community standards only. Public-figure
mockery is allowed as transformative caricature / obvious parody, punching up, never false-as-fact;
keep real private data and real raw copyrighted media out (prefer caricature or licensed/PD). See
`learning-log.md` for the confirmed tone + safety rules.

## Channel Visual Grammar (apply by default)

- **Real photo / real-looking asset as evidence + mascot drawn on top** is the channel signature
  (real photo base or floating real-UI, with the mascot reacting). A bare flat-gradient scene reads as
  "no background" — give every scene a real or real-looking base unless a deliberately blank beat is justified.
- **Vary everything across scenes**: scene-type, composition, mascot side/scale/pose, idea-device.
  Rotate scene types (wide gag / close-up reaction / full-screen text payoff / diagram-or-receipt /
  object hero / mascot-only focus beat). No two consecutive scenes should share a layout.
- **Mascot-only focus beats**: occasionally an empty frame with just the mascot centered, to land a line.
- **One clean hero per beat, no stacked text**: reveal labels sequentially on their words, well spaced,
  on the side opposite a big mascot.
- **Recognizable + relatable**: open and punctuate with things the global English-learner audience
  recognizes (universal money/internet pain; for public figures use GLOBAL ones, not local-only).
- Audience = A2–C1 English learners; the product advantage is "interesting English". When useful, a
  scene's on-screen text can gloss a spicy/idiomatic phrase so edge doubles as learning.

## Workflow

1. Project Selection Gate.
2. Verify required inputs and freshness.
3. Parse `02-script.md` sections.
4. Section Selection Gate.
5. Confirm section voiceover (+ word timings if present) for each selected section.
6. Read required context, skill memory, output formats, and the pose library.
7. For each selected section:
   - split the section narration into per-sentence/per-beat scenes (map to voiceover timing).
   - for EACH scene, write all Scene-Detail fields at full depth.
   - for EACH scene, list its ASSETS (type, description, filename, layout), reusing filenames for
     repeated subjects; mark new invented poses as `generate`.
   - run the Quality Check below and deepen any thin scene.
   - write the section file under `visual-plan/section-XX-*/` (video-level direction summary + the
     section's full scene list) and keep it identical to the master slice.
8. Write/update the master `04-visual-plan.md` (video-level direction + all planned sections), synced
   with the section files.
9. Build/refresh the `assets/asset-manifest.md` stub list of every asset filename the plan references
   (so visual-implement and render can resolve them) — or leave that to visual-implement if it does not
   yet exist; at minimum, the plan's asset filenames must be unambiguous.
10. Run the Downstream Stale Gate (visual-implement + render for affected sections).
11. Respond with the chat summary. Stop before visual-implement/render unless explicitly asked.

## Quality Check (run before handoff; fix any weak answer)

- Could a reader picture each frame with no image? If not, the scene is too thin.
- Is there a new scene roughly per sentence/beat, with varied scene-types and varied mascot use?
- Does every scene name a real/real-looking base (not a bare gradient)?
- Is the mascot a real character, big and high, with a specific pose/expression per scene?
- Does every scene have a show-as-you-say timeline tied to the words?
- Does every asset have a `type`, a clear description (no prompt), a `filename`, and a layout?
- Are repeated subjects reused by the SAME filename (consistency), not regenerated?
- Are public figures handled as transformative caricature / obvious parody, punching up?
- Master and every section file in sync?

## Output Formats

Use `references/output-formats.md` for the exact templates of `04-visual-plan.md`, the section file,
and the chat response. If only some sections are planned, mark the rest `not planned` in the master.

## Downstream Stale Gate

After creating/updating a section plan or the master, list stale downstream for the affected
section(s): the section's implemented assets (`assets/`), `05-production-board.md`, `hyperframes/`,
`renders/`, `06-review.md`, `07-upload.md`, `08-self-learning.md`. Do not delete unless asked.

## Hard Fails

Stop or rework before finishing if:

- a required upstream file is missing or stale, or the section was inferred instead of explicitly chosen
- scenes are too sparse to picture, or the section is one static frame instead of per-sentence scenes
- the plan writes image-generation prompts (that belongs to visual-implement)
- an asset lacks a `type`, a clear description, a `filename`, or a layout
- a repeated subject is given a new filename instead of being reused (breaks character consistency)
- a scene relies on a bare flat gradient with no real/real-looking base
- the mascot is tiny/cornered or has no specific pose/expression
- a public figure is used as a raw copyrighted photo for mockery or made to state something false-as-fact
- the master and section files disagree
- the skill creates assets/images, renders, or downstream files itself

## Self-Improvement

Read `references/memory.md` every run. Update it when the user approves/rejects a planning style, a
scene-detail depth, an asset-listing convention, or a reuse/imagination decision. Promote channel-wide
lessons into `.agents/_shared/channel/learning-log.md`, classified `Core` / `Experiment` /
`Operational lesson` / `Reject`. Do not rewrite channel foundation, audience, tone, or the
product-promotion boundary from one run without explicit user confirmation.
