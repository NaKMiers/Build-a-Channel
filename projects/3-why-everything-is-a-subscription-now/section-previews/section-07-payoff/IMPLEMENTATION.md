# Section 7 Payoff — Implementation Notes (2026-06-23) — FINAL SECTION

## Build

- Created on the S1–S6 pattern + CSS kit (scenes on tracks 1/3/4/5/6 with cross-fades, cues on track 2, audio track 10, GSAP show/hide/smash/pop/reveal, `window.__timelines["Section07Payoff"]`).
- 4 distinct vivid bases (2 different money shots, a phone, a coin jar). The phone returns once (non-adjacent, 2nd filename) for the script's literal final image — the bank-app salary screen.
- The closer recaps the money/device motif and resolves on the bank-app salary card.
- Idea-devices built in CSS: crossed chips, `YOUR FORGETTING`, a barcode `PRODUCT: YOU` tag, green/red worth-vs-design labels, a bank statement (keep green / ghost rows struck), the bank-app salary card, the `your salary. (for now.)` payoff.
- Assets materialized as a local working set under `assets/`.

## Word timings

- None existed → GENERATED via transformers.js whisper-tiny.en. 173 words, clean/monotonic; tail ends ~55.42 → capped at the 54.101 audio.

## Build gotchas

- Float overlap on track 2: cue-c `18.6 + 8.8 = 27.4000002` overlapped cue-d at 27.4 → trimmed cue-c to 8.78.
- The S5 `your salary (for now)` payoff first sat too close to the right-side WIT → centered the payoff (left:600, text-align:center) and pushed WIT further right (right:-230); verified clear @53.2s.

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`).
- `validate`: 0 errors, 0 warnings, 40 non-blocking contrast advisories.
- `inspect --at 5,11.5,17,22,25.5,30,35,39,45,53`: 0 layout issues.
- `snapshot` (10 frames + 53.2 recheck): all beats verified — distinct bases, the reveal/insight/action/close arc reads, the final salary screen + dry "for now" lands, no collisions.

## Server

- `http://localhost:1007/#project/Build%20a%20Channel`
- `http://localhost:1007/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).

## Project status

- This is the FINAL section. All 7 sections (1001–1007) are now built and previewing, awaiting review.
- Next step after review: `combine` (assemble all sections into one video on localhost:1000).
