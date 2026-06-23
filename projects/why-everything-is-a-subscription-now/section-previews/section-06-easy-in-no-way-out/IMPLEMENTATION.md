# Section 6 Easy In, No Way Out — Implementation Notes (2026-06-23)

## Build

- Created on the S1–S5 pattern + CSS kit (scenes on tracks 1/3/4/5/6 with cross-fades, cues on track 2, audio track 10, GSAP show/hide/smash/pop/reveal, `window.__timelines["Section06Easy"]`).
- 3 distinct vivid bases (stopwatch, wooden maze, contract). The maze + stopwatch each return once as a deliberate darker thematic callback (BS4/BS5) — sourcing of distinct tail-beat objects ("burden/−1000 aura", "part-time job no salary") failed this session; documented + swappable. Each callback uses a 2nd filename to avoid `duplicate_media_discovery_risk`.
- Hero device: a 7-step CSS menu breadcrumb trail (the real cancel steps) winding through the maze, each chip popping on its spoken step.
- Assets materialized as a local working set under `assets/`.

## Word timings

- None existed → GENERATED via transformers.js whisper-tiny.en. 163 words, clean/monotonic; tail ends ~56.12 → capped at the 53.013 audio.

## Build gotchas

- Float overlap on track 2: cue-d `33.7 + 8.6 = 42.3000004` overlapped cue-e at 42.3 → trimmed cue-d to 8.58.
- The S2 running-away WIT first covered the right-side menu chips → moved all 7 chips into the left 2/3 and WIT to the right edge (verified clean @23.0s).
- The ☎ phone symbol renders fine as text (not an emoji glyph); other icons are CSS/labels.

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`).
- `validate`: 0 errors, 0 warnings, 25 non-blocking contrast advisories.
- `inspect --at 4,8,12,19,24,28,32,38,45,51`: 0 layout issues.
- `snapshot` (10 frames + 23.0 recheck): all beats verified — distinct bases, the menu maze reads, callbacks look distinct (dark + HUD + defeated WIT), no collisions.

## Server

- `http://localhost:1006/#project/Build%20a%20Channel`
- `http://localhost:1006/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).
