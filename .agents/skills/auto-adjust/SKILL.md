---
name: auto-adjust
description: Post-render Auto Adjust for Why It Works HyperFrames sections. Use after Render or when the user asks to auto-adjust, audit, QA, automatically fix a rendered section, preserve manual Studio edits, apply Section 1/2 review lessons, improve WIT scale/placement/rhythm, reduce animation density, sync cue reveals to voiceover, protect WIT/text/subtitle layout, or prepare one selected rendered section for review; requires one explicit or unambiguous project and one explicit or unambiguous section, never All.
---

# Auto Adjust

## Purpose

Run the post-render QA and fix pass for one `Why It Works` section.

This skill runs after `render` and before human review. It reads the current rendered section, prior review lessons, `visual-plan` memory, `render` memory, shared production knowledge, and previous approved sections in the same project. Then it applies targeted fixes and returns a clear issue/fix/verification report.

The job is not to create a new visual plan or full rebuild by default. The job is to preserve what is good, find review-risk problems, fix what is safe to fix, verify the result, and document what changed.

## Pipeline Position

Main workflow:

```text
topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> auto-adjust -> review -> upload -> learning
```

Auto Adjust writes only post-render section artifacts:

- `projects/<slug>/section-previews/section-XX-kebab-section-name/index.html`
- `projects/<slug>/section-previews/section-XX-kebab-section-name/IMPLEMENTATION.md` or existing section notes
- `projects/<slug>/hyperframes/review/section-XX.html`
- `projects/<slug>/06-production-board.md`
- skill/shared memory only when a reusable lesson is found

Do not create `07-review.md`, `08-upload.md`, `09-self-learning.md`, MP4/WebM exports, or unified preview files unless the user explicitly asks for those separate steps.

## Input Contract

Require exactly one project and exactly one section.

Project resolution order:

1. Use the project slug/path named by the user.
2. Use the active project only when the current project context is unambiguous and the folder exists.
3. If exactly one project has a matching rendered section preview for the requested section, smart-select it and say so.
4. Otherwise ask the user to choose a project before editing.

Section resolution order:

1. Use the section number/name named by the user.
2. Use the section implied by the current request only when it is unambiguous and its preview exists.
3. Otherwise ask the user to choose one section before editing.

Hard rule:

- There is no `All` option for this skill.
- If the user asks for all sections, stop and ask for one section.
- Never infer a target from "next section" if more than one rendered section exists.

## Required Context

Read these before editing:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/rules/memory.md`
5. `.agents/_shared/channel/current-state.md`
6. `.agents/_shared/channel/channel-foundation.md`
7. `.agents/_shared/channel/channel-guardrails.md`
8. `.agents/_shared/channel/learning-log.md`
9. `.agents/_shared/channel/codex-collaboration.md`
10. `.agents/_shared/channel/production-workflow.md`
11. `.agents/_shared/channel/brand-system.md`
12. `.agents/_shared/systems/visual-production.md`
13. `.agents/skills/visual-plan/SKILL.md`
14. `.agents/skills/visual-plan/references/memory.md`
15. `.agents/skills/render/SKILL.md`
16. `.agents/skills/render/references/memory.md`
17. `references/memory.md`
18. the selected project's `02-script.md`, `04-voiceover.md`, `05-visual-plan.md`, and `06-production-board.md`
19. the selected section visual plan, implementation notes, and current `section-previews/.../index.html`
20. previous approved or recently adjusted section previews in the same project, especially their `index.html`, `IMPLEMENTATION.md`, and review mirrors

Load the active WIT manifest before changing WIT:

- prefer `projects/<slug>/assets/wit/manifest.json`
- otherwise use `.agents/_shared/assets/wit/poses/manifest.json`

Use HyperFrames skills as needed for composition mechanics, CLI validation, and browser/preview inspection.

## Manual Edit Preservation

Treat the current section preview `index.html` as canonical.

Before changing any rendered section:

- read the current `index.html`
- check `06-production-board.md`, `IMPLEMENTATION.md`, and `current-state.md` for manual Studio preservation notes
- compare against `hyperframes/review/section-XX.html` only to understand drift, not to overwrite the preview
- create a timestamped backup under `section-previews/section-XX-*/manual-saves/auto-adjust-YYYYMMDD-HHMMSS-index.html`
- preserve `data-hf-studio-*` attributes unless the exact artifact being removed owns them

Do not regenerate a whole section from `05-visual-plan.md` or an older review mirror when a targeted patch can fix the issue.

If the user names an accidental artifact, such as a VFX block or duration extension, remove only that artifact and verify root duration against the voiceover duration unless the user approved extra silent time.

## Auto-Fix Checklist

Run every category below. Deduplicate overlapping findings before editing.

### Voice Sync

- Every visible element must describe the voiceover beat at that moment.
- Tags, labels, props, WIT reactions, and callouts appear when the voice reaches the matching phrase, not early or late.
- Cue-critical visuals are already readable on the cue frame, not still flying into place.
- Delayed GSAP elements must be hidden at cue start before their phrase reveal.

Fix by building or correcting a voice cue map, then adjusting `data-start`, timeline `set`, `show`, `smash`, and cleanup timings.

### Motion Density

- Keep the approved scene/transition count unless the user asks for structural change.
- Ordinary labels, notes, and supporting props should hard-show on the spoken beat.
- Use smash, stamp, shake, snap, or pop only for emphasized spoken words, proof marks, contradiction labels, prices, and payoff text.
- Remove repeated decorative fly-ins that make the section feel visually noisy.

Fix by converting unnecessary animations to hard-show and reserving impact motion for the few strongest beats.

### Big Scene Rhythm

- Short `20-30s` sections should usually feel like about `3` persistent big scenes with `6-8` cue states, unless the voiceover truly needs more.
- Do not cut to a disconnected full-frame board for every sentence when the same object, place, or mechanism is still being described.
- Each cue should add one or two meaningful changes, not a pile of labels and props.

Fix by grouping related cue states, removing duplicate overlays, or simplifying scene changes without destroying approved timing.

### WIT Emotion, Scale, Placement, And Density

- WIT is the emotional subject when it appears, not filler.
- Strong emotion beats should use large WIT placements: roughly `1/3` to `1/2` of the frame, or larger if it improves the joke and does not block evidence.
- Avoid tiny full-body lower-corner WIT on suspicion, panic, betrayal, confusion, payoff, or "viewer victim" beats.
- Treat a lower-right or lower-left standing full-body WIT as suspicious by default. It passes only when the visible character is genuinely dominant and interacts with the scene; otherwise it is still a corner sticker.
- Use creative placements when useful: giant behind-layer face, side peek, lower-edge half-body rise, looming face, hiding behind the object, edge spy peek, or object-interaction pose.
- Use fewer WIT beats if the section feels dense. For short sections, default to about `1-2` WIT appearances per persistent big scene.
- Keep WIT large when it appears; reduce frequency before reducing emotion.
- CSS `width` is not enough. Many WIT PNGs include transparent padding, so a `650px` image can render as a `230px` visible character. Audit the visible alpha/screenshot size, not just the CSS box.
- Intentional crop is allowed only through lower body, legs, or non-emotional edges. Never crop through face, glasses, head, shoulders, mouth, key prop, or readable expression.
- WIT must not cover labels, proof, or payoff. Payoff cards, stamps, and tags must not cover WIT's face, eyes, mouth, or key prop when WIT carries the emotion.
- If no current pose expresses the beat, create or request a new approved WIT PNG pose in shared/project assets and update the manifest before using it.

Fix by resizing, repositioning, changing pose, reducing WIT count, creating separate WIT/text zones, or adding a new approved pose when necessary.

#### WIT Dominance Gate

Before claiming WIT was fixed, create a WIT audit table for every WIT cue:

- cue id and timestamp
- pose filename
- CSS box width/height
- alpha bounding box ratio when the pose is a PNG with transparency
- estimated rendered visible character width/height in the `1920x1080` frame
- screen region, such as `corner`, `side peek`, `bottom half-body`, `behind object`, `center/looming`
- pass/fail reason

Fail the cue and fix it again when any of these are true:

- emotional WIT renders as a small full-body sticker in a corner
- rendered visible character width is below about `25%` of frame width on a strong emotion beat
- WIT face/glasses/mouth read smaller than the main label or payoff text
- the pose is only made bigger by scaling the transparent canvas while the character itself remains small
- WIT sits at `right/bottom` or `left/bottom` without a deliberate Section-1-style composition such as half-body crop, side peek, looming face, or object interaction

For strong emotion beats, prefer fixing with one of these patterns before accepting a corner composition:

- crop into a close-up or upper-body WIT so the face dominates
- move WIT partly behind the main object while keeping the face visible
- let WIT rise from the bottom edge with the lower body intentionally off-screen
- use a side peek where the face/upper body occupies a large emotional zone
- switch to a pose that reads better at giant scale

The final report must not say WIT is "no longer tiny" unless the contact sheet or direct screenshot proves the visible WIT, not only the CSS box, is large.

### Text, Labels, And Subtitle-Safe Layout

- Labels must be short, readable, and useful when paused.
- Text blocks must not hide WIT emotion or critical objects.
- Important lower-third labels, receipts, stamps, arrows, boxes, and payoff props must sit above the likely YouTube subtitle zone.
- If WIT rises from the bottom edge, move nearby text/props upward instead of stacking them into the subtitle area.

Fix by nudging bottom-edge cue-critical elements upward, resizing labels, shortening text only when meaning is preserved, and separating text/WIT zones.

### Markup And Callouts

- Red circles, arrows, underlines, and marks must point to the exact object they explain.
- Remove decorative, obvious, or meaningless marks.
- If the image already proves the detail, a label is usually enough.

Fix by aligning callouts in direct preview screenshots, changing the target, or deleting the markup.

### Assets And Scene Differentiation

- Use real-life assets as evidence, not decoration.
- Preserve real/object photo texture; do not wash out the whole image with white overlays unless local readability requires it.
- Compare adjacent big scenes. Non-callback scenes should not reuse the same background, camera language, tabletop, tag, or material mood by accident.
- Do not force every collected reference into production. Skip weak references and document the skip.

Fix by adjusting overlays locally, replacing a too-similar base with a distinct CSS/self-made/generated scene, or documenting a reference-only decision.

### HyperFrames Mechanics

- HTML is the source of truth.
- Audio must be wired as a proper clip.
- `data-start`, `data-duration`, `data-track-index`, and root duration must be coherent.
- GSAP timeline registration must be synchronous and deterministic.
- Do not use `Math.random()`, `Date.now()`, async timeline construction, infinite repeats, or media `play/pause/seek`.
- Use `npm.cmd run check` on Windows.
- Do not export MP4/WebM for Auto Adjust unless explicitly requested.

Fix blocking lint/validate/inspect errors before handoff.

## Workflow

1. Resolve exactly one project and one section. Reject `All`.
2. Verify the section has current upstream outputs and a rendered preview:
   - `02-script.md`
   - `04-voiceover.md`
   - `05-visual-plan.md`
   - selected section voiceover folder
   - selected section visual-plan folder
   - `06-production-board.md`
   - `section-previews/section-XX-*/index.html`
3. Read required context and this skill memory.
4. Read previous sections in the same project and identify approved style patterns worth preserving.
5. Snapshot the current section preview before editing.
6. Build a short voice cue map from the section script, voiceover notes, and current HTML timings.
7. Run the Auto-Fix Checklist and write a compact issue list before editing.
8. If the request or issue list mentions WIT size, corner placement, crop, or emotional read, run the WIT Dominance Gate before editing and again after editing.
9. Apply targeted fixes with the smallest safe diff.
10. Run verification:
   - `npm.cmd run check` from the section preview when available
   - HyperFrames lint/validate/inspect when the project uses separate commands
   - direct preview or Studio screenshots/contact sheets for WIT, text collision, callouts, and subtitle-zone fixes
   - HTTP check on `localhost:1000 + section number` when a preview server should be running
11. If verification creates many new errors, revert only Auto Adjust's changes from the backup and report the blocker.
12. Sync `hyperframes/review/section-XX.html` from the canonical preview after successful fixes.
13. Update `IMPLEMENTATION.md` and `06-production-board.md` with the issues fixed, commands run, and any residual risks.
14. Update `references/memory.md` when the run teaches this skill something reusable.
15. Promote only channel-wide reusable lessons into `.agents/_shared/`, classified as `Core`, `Operational lesson`, `Experiment`, or `Reject`.
16. Respond with the Auto Adjust report.

## Output Report

Keep the final response concise but include:

```markdown
Auto Adjust target: `<project>` / `<section>`

Fixed:

| Issue | Evidence | Fix | Verification |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

Preserved:
- <manual edits, approved style, or files preserved>

Checks:
- <command or screenshot/preview check>: <result>

WIT audit, when WIT was checked:

| Cue | Pose | Visible Size | Region | Pass/Fail | Fix |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

Residual risks:
- <none or concrete risk>
```

Do not paste the full HTML diff unless the user asks.

## Hard Fails

Stop before editing if:

- project or section is not explicit or unambiguous
- the user asks for `All`
- selected section has no rendered preview
- required upstream files are missing
- the current preview cannot be read
- manual Studio edits are known but not preserved first
- the fix would require a full creative rebuild not implied by the request
- a new WIT pose is required but image generation or approved asset creation is unavailable
- WIT size/corner placement is the named issue and the post-fix WIT Dominance Gate still fails
- the section would need MP4/WebM export and the user did not explicitly request export
- verification fails with blocking errors and quick targeted fixes do not resolve them

If a hard fail happens, report the exact blocker and the safest next action.

## Self-Improvement

Read `references/memory.md` every run.

Update this skill memory when:

- Auto Adjust misses a review issue the user later catches
- a fix pattern works repeatedly
- a fix pattern causes new errors
- a manual Studio preservation case appears
- a recurring WIT, motion, subtitle, markup, or voice-sync rule needs sharper wording

Update `visual-plan` memory only when the problem should have been prevented before render.

Update `render` memory only when the problem came from HyperFrames implementation behavior.

Update `.agents/_shared/` only for reusable channel-wide lessons. Keep one-video details in `projects/<slug>/`.

Do not rewrite core channel identity or strategy from one Auto Adjust run.
