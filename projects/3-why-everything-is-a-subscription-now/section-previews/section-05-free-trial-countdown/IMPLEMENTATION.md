# Section 5 The Free Trial Is A Countdown - Implementation Notes (2026-06-23)

## Build

- Created on the S1–S4 pattern + CSS kit (scenes on tracks 1/3/4/5/6/7 with cross-fades, cues on track 2, audio track 10, GSAP show/hide/smash/pop/reveal, `window.__timelines["Section05Trial"]`).
- The most real-UI-heavy section: FREE splash, credit card, FREE-TRIAL→$2.99 flip, Day-7 notification, translucent ghost charges, bank statement - all CSS over real photo bases (owner-preferred).
- 6 distinct vivid bases (gift, desk, hourglass, busydesk, wallet, piggy) - all unique, no media reuse.
- Assets materialized as a local working set under `assets/`.

## Review fix (2026-06-23, round 2)

- Owner: the blank white-screen phone (BS1 + BS4) read as a placeholder and the same image was reused for two scenes. Replaced BS1 with a pink gift box (`base-gift.jpg`, "free = a gift") and BS4 with an everyday desk (`base-busydesk.jpg`, "forget / life is loud"). All 6 scene bases are now distinct; the phone bases were removed. CSS devices (FREE splash, Day-7 reminder) unchanged. Re-checked lint/validate/inspect clean; snapshots 4.0/27.0 verified.

## Word timings

- None existed → GENERATED via transformers.js whisper-tiny.en. 159 words, clean/monotonic; tail "expired." ends ~54.62 → composition capped at 53.867.

## Build gotchas

- Removed a 👍/👻 emoji glyph plan - emoji don't render in snapshot Chromium; the "ghost" is a translucent CSS card, not an emoji.
- Replaced a fragile GSAP `className` swap (notification grey-out) with a simple opacity dim to 0.32 ("forgotten").
- The S6 red ring needed two nudges to land on the exact `?? UNKNOWN −$3.00` row (my row-height estimate was low) - final `top:462`; snapshot-verified it rings that row, not "Electric bill".
- Moved the `$3 every month` label below the statement (was under the left WIT/receipt).

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`: 6 cues on track 2).
- `validate`: 0 errors, 0 warnings, ~60 non-blocking contrast advisories.
- `inspect --at 4.0,10.8,17.0,19.6,27.0,35.0,44.0,51.5`: 0 layout issues.
- `snapshot` (same + 47.0/51.5): all beats verified - distinct bases, real-UI devices, giant WIT, no collisions, ring on the correct row.

## Server

- `http://localhost:1005/#project/Build%20a%20Channel`
- `http://localhost:1005/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).
