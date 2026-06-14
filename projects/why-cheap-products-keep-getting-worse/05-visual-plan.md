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
| 4 | The Boring Parts Disappear | `remake planned - simple Section 1 style` | `37.867s` | 3 | 6 | `visual-plan/section-04-the-boring-parts-disappear/section-04-the-boring-parts-disappear-visual-plan.md` | `visual-plan/section-04-the-boring-parts-disappear/reference-board.md` | Replaces the rejected crowded cutaway/card direction. Use 3 real photo backgrounds, sparse labels, and 3 giant WIT emotional beats; phone/printer references remain mockup-only. |
| 5 | More Features, More Tiny Deaths | `planned - commons reference pass / generic mockup build` | `34.645s` | 3 | 8 | `visual-plan/section-05-more-features-more-tiny-deaths/section-05-more-features-more-tiny-deaths-visual-plan.md` | `visual-plan/section-05-more-features-more-tiny-deaths/reference-board.md` | Uses 3 persistent scenes, 4 saved Wikimedia references as mockup targets, generic no-logo HyperFrames appliance graphics, and 3 giant WIT emotional beats. |
| 6 | Repair Gets A Security System | `planned - repair-door / repairability mockup pass` | `42.816s` | 4 | 8 | `visual-plan/section-06-repair-gets-a-security-system/section-06-repair-gets-a-security-system-visual-plan.md` | `visual-plan/section-06-repair-gets-a-security-system/reference-board.md` | Uses 4 persistent scenes, 3 giant WIT emotional beats, a repair-door lock motif, and a simplified no-logo repairability label; saved real references are mostly mockup targets. |
| 7 | Replacement Becomes Normal | `not planned` | `29.312s` | 0 | 0 | `not created` | `not created` | Wait for visual-plan request for this section. |
| 8 | Payoff | `planned - local sourced-reference fallback` | `29.141s` | 3 | 8 | `visual-plan/section-08-payoff/section-08-payoff-visual-plan.md` | `visual-plan/section-08-payoff/reference-board.md` | Uses 3 held payoff scenes, 3 giant WIT emotional beats, copied sourced local references, and a calm final question frame. |

## Cross-Section Continuity

- Recurring object: `yellow or blank price tag that turns into a hidden-future object`
- Recurring label: `FUTURE NOT INCLUDED`, with Section 2 using `MISSING TOMORROW` as the reframe label
- WIT emotion arc: `happy bargain hunter -> suspicious/fair inspector -> betrayed owner -> locked-out repairer -> tired repeat buyer -> deadpan evaluator`
- Color/texture notes: `real tag paper/string, plain boxes, worn chair leather/fabric, receipt paper, sale yellow, red handwritten markup`
- Asset reuse notes: `Use the Section 1 real-image-first bar as the baseline. Section 2 adds generated support bases only where render previously had to invent scene structure. Section 4 uses real material references plus CSS cutaways because labels, missing slots, and WIT zones need tight control. Section 5 uses Wikimedia appliance references as mockup targets and should build no-logo generic fridge/control/circuit-board graphics in HyperFrames. Section 6 follows the same safe generic-mockup rule for repair doors, locks, phone labels, bills, and policy proof. Do not return to the rejected vector/SVG reference style.`

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
- Section 6 visual plan was created after project-level downstream file `06-production-board.md`, `hyperframes/`, `renders/`, and `section-previews/` already existed for other sections.
- No Section 6 preview folder, review HTML, MP4 render, `07-review.md`, `08-upload.md`, or `09-self-learning.md` was found at visual-plan time.
- Next regeneration action for this branch is to run `Render` for Section 6; do not delete earlier section artifacts unless explicitly requested.

## Next Step Boundary

Next workflow step: `Render`

Do not continue into render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.
