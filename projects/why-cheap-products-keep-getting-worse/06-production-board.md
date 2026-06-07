# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section 1 preview ready for review`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 |  |  | reserved |
| Section 1 Hook | 1001 | `http://localhost:1001/#project/section-01-hook` | `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html` | running |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Render file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook | `preview ready for review` | 1001 | `section-previews/section-01-hook/` | `02-script.md` + `04-voiceover.md` + `05-visual-plan.md` | `lint: warn-only (composition_file_too_large)`; `validate: pass`; `inspect: pass` | `not rendered` | `8-board static-first build. Preview-local assets use minimal hardlinks because HyperFrames CLI did not serve the original junction-backed folder on this machine.` |

## Shared Asset Rules

- Video-level assets: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section asset rule: keep the project asset library as source of truth; current Section 1 preview materializes a minimal hardlinked working set under `section-previews/section-01-hook/assets/` because HyperFrames CLI checks returned asset 404s when the local `assets/` path was a junction
- Attribution file: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Active Section Notes

- Section 1 composition id: `Section01Hook`
- Runtime: `21.605s`
- Voiceover runtime: `21.205s`
- Final hold: `0.400s`
- Board grammar: `deal -> confidence -> hidden tag -> calm week -> legal creak -> loose screw -> receipt evidence -> future not included`
- Real direct-use assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`
- Generated support assets: `chair-price-tag`, `hidden-future-tag`, `wobbly-leg-loose-screw`, `price-tag-receipt`

## Stale / Regeneration Notes

- No downstream files were present during this render run: `07-review.md`, `08-upload.md`, `09-self-learning.md`
- If Section 1 is rerendered later, any future review, upload, learning, unified preview, or final render outputs for this section become stale and must be regenerated in order

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
