# Section 3 The Spread — Implementation Notes (2026-06-23)

## Build

- Created on the S1/S2 pattern + CSS kit (scenes on tracks 1/3/4/5/6 with cross-fades, cues on track 2, audio track 10, GSAP show/hide/smash/pop/reveal, `window.__timelines["Section03Spread"]`).
- 5 distinct vivid object bases (desk / tv-room / cash / jail / car), varied CSS idea-devices per beat, 4 giant WIT beats varied by side/pose.
- Assets materialized as a local working set under `assets/` (junctions 404 with the CLI on this box): fonts, 4 WIT PNGs, 5 bases, the section mp3.

## Word timings

- None existed → GENERATED via transformers.js `Xenova/whisper-tiny.en` (decoded the mp3 to 16k mono f32 with the static ffmpeg). 168 words, clean/monotonic; tail "expired." overshoots to 55.42 (whisper chunk glitch) so the composition caps at the authoritative TTS duration 54.165 and the gag is pinned to 50.90.

## Build gotchas

- WIT `typing-on-laptop.png` has a baked BLACK background (like `money-panic`) — unusable on photo scenes; swapped to `hidden-fee-panic` for the software beat.
- Float overlap on track 2: cue-d `35.20 + 6.20 = 41.4000000006` overlapped cue-e at 41.4 → trimmed cue-d duration to 6.18.
- Car base has a small "Blaupunkt" head-unit logo — covered by the CSS heated-seat/price panel and the giant deadpan WIT (which sits on the right over the head unit). Classified mockup target.
- EXPIRED banner is a top banner; the BS5 headline hides at 50.90 so it doesn't sit under the banner.

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`: 5 cues on track 2 — same as approved S1/S2).
- `validate`: 0 errors, 0 warnings, 40 non-blocking contrast advisories.
- `inspect --at 6.0,11.5,18.5,23.0,29.5,37.0,40.0,47.0,52.5`: 0 layout issues.
- `snapshot` (same + 23.8): all beats verified — distinct bases, varied idea-devices, giant WIT, no collisions.

## Server

- `http://localhost:1003/#project/Build%20a%20Channel`
- `http://localhost:1003/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).
