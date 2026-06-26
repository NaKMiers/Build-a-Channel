# Production Workflow

Classification: `Core operational structure`

Scope: `CHANNEL_WIDE`

This is the compact workflow source of truth for `Why It Works`.

## Folder Rule

- Channel-wide memory and reusable systems live in `.agents/_shared/`.
- Executable skills live in `.agents/skills/`.
- One video project lives in one folder under `projects/<slug>/`.
- Active production decisions belong in the relevant `projects/<slug>/` file before moving to the next step.

## Naming & Path Rule (keep paths short)

This is a Windows repo (`MAX_PATH` ≈ 260 chars). Long nested paths break `git add` with `Filename too long`. Keep paths short and never commit generated caches.

- Keep filenames short and kebab-case. For asset files, prefer `<subject>-<n>.jpg` (e.g. `cardboard-boxes-1.jpg`), not long descriptive + attribution strings in the filename. Put photographer/source/license in the section `ATTRIBUTION.md`, not the filename.
- Do not repeat the long `section-XX-kebab-section-name` more than once in a single path. Asset trees that nest the section slug inside another section slug folder (and then again inside a cache) are what overflow the limit.
- Never commit generated/derived files. These are regenerable and must stay out of git (already in `.gitignore`):
  - `.thumbnails/` — HyperFrames thumbnail caches (they mirror the whole asset tree under the preview folder, creating the deepest paths in the repo)
  - `node_modules/`, `.cache/`, `*.raw`/`*.tmp` decode artifacts
- Commit only source + deliverables: scripts/markdown, section `index.html` + `DESIGN.md`/`IMPLEMENTATION.md`, the shared `assets/` library, voiceover audio + timings, and the `output/` deliverables. Preview/cache byproducts stay ignored.
- `git config core.longpaths true` is set on this repo as a safety net, but the real fix is short paths + ignoring caches.

## Sequential Pipeline

The main video pipeline is:

```text
00-topic-intake.md
01-research-pack.md
02-script.md
03-voiceover.md
04-visual-plan.md
05-production-board.md
06-review.md
07-upload.md
08-self-learning.md
```

Numbering note: the above is the NEW-project numbering (packaging left the numbered set on `2026-06-26`, so voiceover→render shifted up by one). Existing projects keep the old numbers (`04-voiceover` … `09-self-learning`, `03-packaging`). All skills resolve a step file by its name SUFFIX, never a hard-coded prefix — see `.agents/rules/video-workflow.md`.

Packaging (after caption, not numbered):

```text
caption -> packaging -> output/packaging.md (+ output/thumbnails/)
```

Current executable steps:

- `topic-intake` creates or updates `00-topic-intake.md`.
- `research-pack` requires `00-topic-intake.md` and writes `01-research-pack.md`.
- `script-draft` requires `00-topic-intake.md` and `01-research-pack.md`, then writes `02-script.md`.
- `voiceover` requires `02-script.md`, then writes the voiceover index (`03-voiceover.md`; legacy `04`) and section voiceover files.
- `visual-plan` requires the voiceover index and selected section voiceover, then writes the visual-plan index (`04-visual-plan.md`; legacy `05`) and section visual-plan files.
- `render` requires the visual-plan index and selected section visual plan, then writes the production board (`05-production-board.md`; legacy `06`) and section HyperFrames preview files.
- `combine` (after all sections) unifies the project on `localhost:1000` with one combined voiceover and exports the full MP4 to `output/`.
- `caption` (after combine) transcribes the full combined audio for real word timings and exports `output/captions.srt`.
- `shorts` (side sub-workflow from `combine`) turns the finished long video into 2-4 COMPLETE vertical shorts (`1080x1920`) on ports `1100 + short number` via native portrait HyperFrames rebuilds — reusing each source section's real assets, regenerating a per-short voiceover, and burning centered subtitles — then exports to `output/shorts/`. Each short carries NO CTA, never edits the long-form sections, and does not block caption, upload, or learning.

Packaging rule:

Packaging runs after `caption` and requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`. It writes `output/packaging.md` (+ `output/thumbnails/`). Rerunning packaging makes only `upload`/`learning` potentially stale, not earlier production outputs.

Pipeline rules:

- Step `N` requires all previous step outputs.
- If a required output is missing, stop and tell the user which skill to run first.
- Rerunning an earlier step makes later outputs stale.
- Remove stale downstream outputs only by explicit user request, or regenerate them by rerunning later skills in order.

After the voiceover index (`03-voiceover.md`; legacy `04`), production branches by section. A selected section should move through visual plan, render, and review as its own branch. `All` means every section gets separate outputs, not one stitched planning artifact.

Render port rule:

- unified/final preview uses `localhost:1000`
- section `N` preview uses `localhost:1000 + N`
- do not put all sections in one localhost during section review
- render uses visual-plan as the main handoff, but must still run its own HyperFrames/review-prevention pass before building HTML

## Startup Read Set

Before strategy, production, or persistent memory changes, read:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`

For production work, also use the four compact systems:

- `.agents/_shared/systems/topic-packaging-hooks.md`
- `.agents/_shared/systems/script-learner-voice.md`
- `.agents/_shared/systems/visual-production.md`
- `.agents/_shared/systems/audio-feedback-quality.md`

## Quality Gates

Use lightweight gates instead of many separate checklists:

- Topic angle: the angle must combine topic, contradiction, visual metaphor, and viewer pain.
- Packaging: title and thumbnail must create curiosity without fake claims.
- Hook: the first `10` seconds must show the situation, contradiction, WIT emotion, and bigger question.
- Script: the script must teach the topic first and stay learner-friendly by design.
- Visuals: each board must carry one thought, one readable label, and one clear joke or evidence job.
- Visual motion: ordinary cue labels should hard-show on the spoken beat; impact animation belongs only on emphasized words, evidence, or payoff.
- WIT QA: when WIT appears, its emotion must read clearly, the face/head/shoulders must not look accidentally cropped, WIT should not appear so often that it fights the voice rhythm, and text/payoff/stamps must not cover WIT's face/expression.
- Pre-review QA: before review, sweep the rendered section for voice sync, motion density, WIT scale/rhythm/crop, text/WIT collision, subtitle-safe lower layout, meaningful markup, asset differentiation, manual edit preservation, and HyperFrames validation.
- Audio: narration is the product; music and sound effects are support.
- Review: paused frames should be understandable, readable, and worth looking at.
- Learning: after publishing, record only reusable lessons.

## Render Rule

HyperFrames is the active render path.

Use simple board scenes, WIT poses, voiceover, hard cuts, cue-timed labels, red markup, and handwritten-looking text. Prefer clear static boards before adding motion.

During normal preview/review fixes, use HyperFrames checks plus direct preview screenshots/contact sheets. Do not export MP4/WebM unless the user explicitly asks for a video file.

Each rendered section should live in its own HyperFrames preview project under `projects/<slug>/section-previews/section-XX-kebab-section-name/`.

Manual Studio edit rule: if Anh Khoa edits a localhost/HyperFrames Studio section manually, the live `section-previews/.../index.html` becomes canonical for the next update. Future agents must read and diff it before editing, must not restore from `hyperframes/review/` or older visual plans, and should remove only the specific accidental effect/duration artifact that was identified.

Legacy Remotion notes are historical only. Do not revive Remotion production unless the user explicitly asks.

## Browsing Rule

Use the project-local `browse` skill for web or YouTube browsing when available. Fall back to global gstack `/browse` only if the project-local skill cannot run. Do not use other browser tools unless the user explicitly approves a fallback.
