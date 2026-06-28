# 05 Visual Plan

Video: `Why Cheap Products Keep Getting Worse`

Status: `section visual plan in progress`

Source skill: `visual-plan`

Source files:

- `02-script.md`
- `04-voiceover.md`

## Visual Direction

- Renderer: `HyperFrames`
- Format: `section-first 16:9 no-face explainer`
- Main grammar: `real web-photo texture -> generated support base when needed -> WIT reaction -> handwritten correction label -> hard cut or small cue reveal`
- Script promise: `Cheap can look like saving money now while hiding the future cost later.`
- Main motif: `future not included / missing tomorrow`
- WIT role: `WIT is the buyer and inspector who experiences the hidden future cost without blaming affordable shopping.`
- Real-life texture: `blank price tags, receipt paper, plain product boxes, jacket fabric, damaged chair and loose-screw texture from Section 1, generic appliance/fridge/control-panel/circuit-board texture for Section 5, phone repair workbench, precision screwdriver, and repairability-label reference for Section 6`
- Editor intent: `keep the explanation fair, object-driven, and close to ordinary shopping life while giving render exact scene bases`
- Reference standard: `real-image-first, then generated support bases for scene gaps that render should not invent`
- Red markup style: `one meaningful red correction or target mark per cue; no decorative circles`
- Motion rule: `hard cuts between persistent big scenes; cue changes should be small label, WIT, markup, or object-state reveals`

## Section Visual Plan Index

| # | Section | Status | Duration | Big Scenes | Cue States | Section plan | Reference board | Notes |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | Hook | `planned - real-image-first reference pass` | `21.205s` | 8 | 8 | `visual-plan/section-01-hook/section-01-hook-visual-plan.md` | `visual-plan/section-01-hook/reference-board.md` | Legacy board plan already rendered separately; Section 1 render later used 3 persistent big scenes and 7 voice-timed cue overlays by explicit user review. |
| 2 | Cheap Is Not The Villain | `replanned - real plus generated support pass` | `22.315s` | 3 | 9 | `visual-plan/section-02-cheap-is-not-the-villain/section-02-cheap-is-not-the-villain-visual-plan.md` | `visual-plan/section-02-cheap-is-not-the-villain/reference-board.md` | Replanned after self-check: real images were not enough for the two-box comparison and missing-tomorrow cutaway; generated support bases now fill those gaps. |
| 3 | The Price Tag Speaks First | `render-revised - scene 3 rebuilt after review` | `33.429s` | 4 | 10 | `visual-plan/section-03-the-price-tag-speaks-first/section-03-the-price-tag-speaks-first-visual-plan.md` | `visual-plan/section-03-the-price-tag-speaks-first/reference-board.md` | Uses a generated hidden-future-tag base for Scenes 1, 2, and 4. Scene 3 was rebuilt as a CSS checkout promise arena after review because the generated visible-promise base was too similar to Scene 1. |
| 4 | The Boring Parts Disappear | `remade from scratch 2026-06-21 - rendered, ready for review` | `37.92s` | 3 | 6 | `visual-plan/section-04-the-boring-parts-disappear/section-04-the-boring-parts-disappear-visual-plan.md` | `visual-plan/section-04-the-boring-parts-disappear/reference-board.md` | Rebuilt composition from scratch (also fixed the missing assets folder). 3 real photo bases (fabric / repair-tools / sealed box), a staggered repairable-parts list that builds one row per spoken item, payoff `LESS FUTURE BUILT IN`, 3 WIT beats (thinking / deadpan / betrayed). Timing `whisper-derived` (transcribed with transformers.js whisper-tiny.en → `section-04-word-timings.json`; every cut/reveal pinned to real word times). Rendered on port 1004; synced to review mirror + unified full video. |
| 5 | More Features, More Tiny Deaths | `remade from scratch 2026-06-21 - rendered, ready for review` | `34.704s` | 2 | 5 | `visual-plan/section-05-more-features-more-tiny-deaths/section-05-more-features-more-tiny-deaths-visual-plan.md` | `visual-plan/section-05-more-features-more-tiny-deaths/reference-board.md` | Rebuilt composition from scratch. One real fridge that gains a feature pile-up into "a small technology committee", then a real control-board failure payoff `HARDER + MORE EXPENSIVE TO FIX`; 3 WIT beats (celebration / confused / money-panic). Timing `whisper-derived` (transformers.js whisper-tiny.en → `section-05-word-timings.json`). Rendered on port 1005; synced to review mirror + unified full video. |
| 6 | Repair Gets A Security System | `plan reconstructed from approved render - needs re-render` | `42.816s` | 4 | 8 | `visual-plan/section-06-repair-gets-a-security-system/section-06-repair-gets-a-security-system-visual-plan.md` | `visual-plan/section-06-repair-gets-a-security-system/reference-board.md` | Visual-plan folder was missing on disk while the approved render survived at `hyperframes/review/section-06.html`. Rebuilt 1:1 on `2026-06-18` to match the approved build: `REPAIR CHECKPOINT` airport-security metaphor, real repair-bench + precision-screwdriver graded photo bases, security trays for the barrier list, 3 giant WIT beats (suspicious / trapped-behind-glass / deadpan), and a WIT-free definition+checklist scene. The `section-previews/section-06-.../` working preview is missing, so Render must rebuild it. |
| 7 | Replacement Becomes Normal | `planned and rendered - ready for review` | `29.312s` | 3 | 7 | `visual-plan/section-07-replacement-becomes-normal/section-07-replacement-becomes-normal-visual-plan.md` | `visual-plan/section-07-replacement-becomes-normal/reference-board.md` | `subscription with extra steps` payoff. 2 real Wikimedia bases (e-waste CC0, fulfillment boxes CC BY-SA 4.0) + 1 justified self-made CSS checkout/receipt scene; 3 WIT beats (facepalm / holding-receipt / deadpan), Scene 2 WIT-free; 4 friction reasons staggered. Timing `estimated` (no word-timings file; whisper-cpp unavailable) - confirm sync in Studio. Rendered to `section-previews/section-07-replacement-becomes-normal/` on port 1007. |
| 8 | Payoff | `planned - local sourced-reference fallback` | `29.141s` | 3 | 8 | `visual-plan/section-08-payoff/section-08-payoff-visual-plan.md` | `visual-plan/section-08-payoff/reference-board.md` | Uses 3 held payoff scenes, 3 giant WIT emotional beats, copied sourced local references, and a calm final question frame. |

## Cross-Section Continuity

- Recurring object: `yellow or blank price tag that turns into a hidden-future object`
- Recurring label: `FUTURE NOT INCLUDED`, with Section 2 using `MISSING TOMORROW` as the reframe label
- WIT emotion arc: `happy bargain hunter -> suspicious/fair inspector -> betrayed owner -> locked-out repairer -> tired repeat buyer -> deadpan evaluator`
- Color/texture notes: `real tag paper/string, plain boxes, worn chair leather/fabric, receipt paper, sale yellow, red handwritten markup`
- Asset reuse notes: `Use the Section 1 real-image-first bar as the baseline. Section 2 adds generated support bases only where render previously had to invent scene structure. Section 4 uses real material references plus CSS cutaways because labels, missing slots, and WIT zones need tight control. Section 5 uses Wikimedia appliance references as mockup targets and should build no-logo generic fridge/control/circuit-board graphics in HyperFrames. Remade Section 6 should build no-logo generic repair-checkpoint, repair bill, locked product, repairability checklist, and future-label graphics in HyperFrames from the saved reference board. Do not return to the rejected vector/SVG reference style or the deleted old Section 6 preview.`

## Stale / Regeneration Notes

- Section 2 render was regenerated after the revised Section 2 visual plan; the previous stale Section 2 note is no longer current.
- Section 3 visual plan was created after project-level downstream file `06-production-board.md` already existed.
- No Section 3 downstream preview, review HTML, render, `07-review.md`, `08-upload.md`, or `09-self-learning.md` was found at visual-plan time.
- Next regeneration action for this branch is to run `Render` for Section 3; do not delete downstream artifacts unless explicitly requested.
- Section 4 visual plan was created after project-level downstream file `06-production-board.md`, `hyperframes/`, `renders/`, and `section-previews/` already existed for earlier sections.
- No Section 4 preview folder, review HTML, MP4 render, `07-review.md`, `08-upload.md`, or `09-self-learning.md` was found at visual-plan time.
- Next regeneration action for this branch is to run `Render` for Section 4; do not delete earlier section artifacts unless explicitly requested.
- Section 4 visual plan was remade after the first Section 4 render attempt was rejected as too crowded. The current Section 4 render preview and review mirror should be regenerated from the simplified Section 1-style plan.
- Section 8 visual plan was created after project-level downstream file `06-production-board.md`, `hyperframes/`, `renders/`, and `section-previews/` already existed for earlier sections.
- No Section 8 preview folder, review HTML, MP4 render, `07-review.md`, `08-upload.md`, or `09-self-learning.md` was found at visual-plan time.
- Next regeneration action for this branch is to run `Render` for Section 8; do not delete earlier section artifacts unless explicitly requested.
- Section 5 visual plan was created after project-level downstream file `06-production-board.md`, `hyperframes/`, `renders/`, and `section-previews/` already existed for other sections.
- No Section 5 preview folder, review HTML, MP4 render, `07-review.md`, `08-upload.md`, or `09-self-learning.md` was found at visual-plan time.
- Next regeneration action for this branch is to run `Render` for Section 5; do not delete earlier section artifacts unless explicitly requested.
- Section 6 was completely removed and remade by request on `2026-06-15`. Old Section 6 visual-plan/reference/render artifacts are no longer canonical.
- On `2026-06-18`, the Section 6 visual-plan markdown folder was found missing on disk, while the approved render survived at `hyperframes/review/section-06.html` plus `hyperframes/review/assets/section-06/repair-checkpoint-photo-base.jpg` and `precision-screwdriver-photo-base.jpg`. The 4 saved references under `assets/visual-references/section-06-repair-gets-a-security-system/` also survived.
- The Section 6 visual plan, reference board, and README were reconstructed from that approved render on `2026-06-18` so they match the build 1:1 (4 scenes, 8 cues, 3 WIT beats, scene cuts at 12.0 / 21.8 / 34.8, timed reveals at 19.55 and 39.8).
- The `section-previews/section-06-repair-gets-a-security-system/` working preview is missing (only the `hyperframes/review/section-06.html` mirror remains), and `06-production-board.md` is not present on disk.
- Next regeneration action for this branch is to rerun `Render` for Section 6 to rebuild the section preview on `localhost:1006` and recreate `06-production-board.md` from the surviving review-mirror HTML and this reconstructed plan. Do not delete the review mirror.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
