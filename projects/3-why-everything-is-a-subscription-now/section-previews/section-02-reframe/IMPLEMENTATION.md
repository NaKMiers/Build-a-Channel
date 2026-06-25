# Section 2 Reframe — Implementation Notes (REMADE 2026-06-23)

## Review fixes (2026-06-23, round 2)

- BS1 background swapped: aurora night-phone → `base-apps-phone.jpg` (hands on a phone full of app icons; CC0 rawpixel). `base-night-phone.jpg` retired (unused, kept on disk).
- Text-on-text fixed: BS3 `OWN`(struck) now sits ABOVE `RENT` (vertical stack, both readable); BS5 the 4 RENT tags are hidden at 36.26 when the `RENT — NOT OWN` payoff smashes in, so nothing overlaps it.
- WIT enlarged to giant on all 4 beats (width 1200–1300, ≈1/2+ frame, anchored bottom:-320 so head+torso are in frame, legs cropped). Labels re-arranged to the side WIT does not use (facepalm R → labels left; thinking L → labels right; betrayed CENTER → banner top + card/aside far-left; suspicious R → headline/tags/payoff left).
- Re-checked: lint 0 err, validate 0 err (55 contrast advisories), inspect 0 issues; snapshots at 6.0/11.6/18.6/23.8/36.8 confirm new bg, giant WIT, and no collisions.


## Build

- Same HyperFrames pattern + CSS kit as approved S1 (scenes on tracks 1/3/4/5/6, cues on track 2, audio track 10, GSAP show/reveal/smash, `window.__timelines["Section02Reframe"]`).
- VARIED idea-devices over real photo bases (not repeated cream boxes): struck `RANT` banner + app tiles w/ green ✓; green OWN stamp + paper receipt; CSS subscription paywall + OWN→RENT stamp swap + "screen ON" toggle; red MISS A PAYMENT system banner + CSS lock-screen card; kinetic headline + RENT tags + kinetic payoff. The cream `.aside` is used for only 2 short handwritten asides.
- 5 distinct vivid object bases (phone / vinyl / phone-rent / padlock / flat-lay). The phone returns in BS3 as a non-consecutive device callback (the script's "same device, now rented"); a separate filename `base-phone-rent.jpg` avoids the duplicate-media lint warning.
- Assets materialized as a local working set under `assets/` (junctions 404 with the CLI on this box).

## Word timings

- `voiceover/section-02-reframe/section-02-word-timings.json` (transformers.js whisper-tiny.en). Word STARTS are clean and used; the tail overshoots to 39.16 (whisper chunk glitch) so the composition uses the authoritative TTS duration 37.909 and the payoff is pinned to 36.26.

## Build gotchas fixed

- The shared `smash`/`reveal` helper only maps `x/y/scale/opacity` to its end-state — a `{scaleX:0}` fed to it animates nothing (stays 0, invisible). The "rant" strike is therefore drawn with an explicit `tl.to(..., {scaleX:1})` tween + `transform-origin:left center`, not `smash`.
- All smashed/scaled elements (OWN/RENT stamps, betrayed WIT, payoff) use explicit `left`/`top` (no percentage translate, which GSAP scale would drop).
- No emoji glyphs — the lock icon is the CSS `.lockicon` shape; the green checks are CSS `::after` ticks; the warn is a CSS `!` circle.

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`: 5 cues on track 2 — same as approved S1).
- `validate`: 0 errors, 0 warnings, 45 non-blocking contrast advisories (colored text/borders over photos).
- `inspect --at 1.4,6.0,11.6,18.6,23.8,27.9,33.6,36.8`: 0 layout issues.
- `snapshot` (same timestamps): every beat verified — distinct bases per scene, varied idea-devices, struck banner reads as "NOT a rant", OWN→RENT swap reads, betrayed WIT giant + clear at the padlock peak, RENT tags + payoff clear of WIT.

## Server

- `http://localhost:1002/#project/Build%20a%20Channel`
- `http://localhost:1002/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).
