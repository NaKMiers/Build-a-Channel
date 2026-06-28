# Section 1 Hook - Implementation Notes

## Build

- Modeled on the approved `why-everyone-pretends-to-be-busy` Section 1 structure (scenes on tracks 1/3/4, cues on track 2, audio track 10, GSAP `show/reveal/smash` helpers, `window.__timelines["Section01Hook"]`).
- Real-UI illustration (standing preference): bank statement + subscription cards built in CSS over real CC photo bases; no real brand logos used (fake service names).
- Assets materialized as a local working set under `assets/` (font, 4 WIT poses, 2 base photos) instead of a junction - junctions 404 with the HyperFrames CLI on this Windows box (documented precedent).

## Word timings

- Generated `voiceover/section-01-hook/section-01-word-timings.json` via transformers.js `Xenova/whisper-tiny.en` (WASM) + ffmpeg-static decode. Tail ("One payment at a time") jumped backward (chunk-boundary glitch) and was hand-re-timed monotonically to the 23.509s end.

## Review-prevention fixes applied during build

- GSAP overwrites percentage `translateX` on smashed elements → removed `translateX(-50%)` from the `−$2.99` chip and the EXPIRED pop-up; positioned with explicit `left`.
- C6 collision: deadpan WIT on the right covered the EXPIRED pop-up + items → moved deadpan WIT to the LEFT, pop-up to open center-top, items to the right column. Verified at 18.3s.
- Duplicate-media lint warning from reusing `base-desk-devices.jpg` in scenes B and C → scene C uses a separate `base-desk-devices-dim.jpg` copy. Lint now 0/0.

## Checks

- `lint`: 0 errors, 0 warnings.
- `validate`: 0 errors, 0 warnings, 80 non-blocking contrast warnings (white UI text / photo bases - expected; 0 errors is the gate).
- `snapshot --at`: verified all 7 cues (2.5/6.0/8.5/13.0/17.9/18.3/21.0).

## Server

- `http://localhost:1001/#project/Build%20a%20Channel`
- `http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Project id resolves to `Build a Channel` (workspace root), not the section folder - known HyperFrames behavior on this setup.

## Not done (by rule)

- No MP4/WebM export (not requested).
