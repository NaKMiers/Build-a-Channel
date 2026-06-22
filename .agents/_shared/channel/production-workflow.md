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
04-voiceover.md
05-visual-plan.md
06-production-board.md
07-review.md
08-upload.md
09-self-learning.md
```

Post-render `auto-adjust` runs between `06-production-board.md` and `07-review.md`. It fixes the selected rendered section in place and does not create a new numbered project output by default.

Packaging side branch:

```text
01-research-pack.md -> 03-packaging.md
```

Current executable steps:

- `topic-intake` creates or updates `00-topic-intake.md`.
- `research-pack` requires `00-topic-intake.md` and writes `01-research-pack.md`.
- `script-draft` requires `00-topic-intake.md` and `01-research-pack.md`, then writes `02-script.md`.
- `packaging` is a side branch from `research-pack`; it requires `00-topic-intake.md` and `01-research-pack.md`, then writes `03-packaging.md`.
- `voiceover` requires `02-script.md`, then writes `04-voiceover.md` and section voiceover files.
- `visual-plan` requires `04-voiceover.md` and selected section voiceover, then writes `05-visual-plan.md` and section visual-plan files.
- `render` requires `05-visual-plan.md` and selected section visual plan, then writes `06-production-board.md` and section HyperFrames preview files.
- `auto-adjust` requires a rendered selected section, then audits and fixes that one section preview before review. It reads `visual-plan` memory, `render` memory, shared production rules, and previous sections in the same project. It has no `All` option.

Packaging side-branch rule:

Packaging does not block script, voiceover, visual plan, render, review, upload, or learning. Rerunning packaging does not make main pipeline outputs stale.

Pipeline rules:

- Step `N` requires all previous step outputs.
- If a required output is missing, stop and tell the user which skill to run first.
- Rerunning an earlier step makes later outputs stale.
- Remove stale downstream outputs only by explicit user request, or regenerate them by rerunning later skills in order.

After `04-voiceover.md`, production branches by section. A selected section should move through visual plan, render, auto-adjust, and review as its own branch. `All` means every section gets separate outputs, not one stitched planning artifact. Auto Adjust is the exception: it requires one section only and has no `All` option.

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
- Auto Adjust: before review, run a one-section post-render sweep for voice sync, motion density, WIT scale/rhythm/crop, text/WIT collision, subtitle-safe lower layout, meaningful markup, asset differentiation, manual edit preservation, and HyperFrames validation.
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
