# Section 5 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 5: More Features, More Tiny Deaths`

Status:
`remade from scratch 2026-06-21 (voice-synced) - preview on port 1005, ready for review`

## Remake From Scratch (2026-06-21)

Rebuilt fresh and voice-synced. 2 big scenes: a real fridge (`fridge.jpg`) persisting 0-29.52 that gains a staggered feature pile-up into "A SMALL TECHNOLOGY COMMITTEE", then a real control board (`circuit-board.jpg`) for the failure payoff. 5 cues; 3 WIT beats (`awkward-celebration` / `confused` / `money-panic`); turn + pile WIT-free so the clutter joke reads. Payoff `HARDER + MORE EXPENSIVE TO FIX` (one line, span border-bottom underline). Removed an unneeded stray brand-mask. `dev` patched to `preview --port 1005`.

Timing is `whisper-derived`: transcribed with `transformers.js` (`@xenova/whisper-tiny.en`, WASM - no native deps) → `voiceover/section-05-.../section-05-word-timings.json`; every cut + reveal pinned to real word times (feature pile screens 18.44 / sensors 19.26 / water 19.68 / ice 20.24 / software 21.44 / opinions 21.66; committee 26.82; payoff 33.22). Verified: lint 0 / validate 0 / inspect 0 (8 samples); snapshot QA confirms the pile builds in sync. Synced to review mirror + unified full video (audio stripped; duration unchanged so unified offsets unaffected).

## Result

- Preview project: `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-05-more-features-more-tiny-deaths/`
- Source: `02-script.md` + approved voiceover timing + Section 1 / Section 8 render grammar + Section 5 reference assets
- Rejected source: the earlier visual-plan-driven CSS-only Section 5 mockup is superseded
- Port: `1005`
- Studio URL: `http://localhost:1005/#project/section-05-more-features-more-tiny-deaths`
- Direct composition URL: `http://localhost:1005/api/projects/section-05-more-features-more-tiny-deaths/preview/comp/index.html`
- Runtime: `34.645s`
- Voiceover: `section-05-more-features-more-tiny-deaths-david23-am_eric-0.84.mp3`
- Latest contact sheet: `snapshots/remake-real-photo-20260613/contact-sheet-section-05-remake.png`

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Source |
|---:|---:|---|---|---|
| 1 | `0.000-3.790` | `products can get more complicated / not automatically bad` | Real fridge/kitchen base, giant price-tag-suspicion WIT, `COMPLICATED IS NOT BAD`. | script + Section 1/8 style reference |
| 2 | `3.800-8.890` | `Useful features... safer appliance... better battery` | Same real fridge base, sparse `USEFUL FEATURES ARE USEFUL`, `SAFER`, `BETTER BATTERY`. | script + real fridge photo |
| 3 | `8.900-10.590` | `phone that survives gravity` | Giant phone-panic WIT and `SURVIVES GRAVITY`. | script + approved WIT |
| 4 | `10.600-14.190` | `one more thing that can break` | Closer real fridge crop, red `EVERY FEATURE = BREAK POINT` mark. | script + real fridge photo |
| 5 | `14.200-17.590` | `A simple fridge... be cold` | Same real fridge crop with `ONE JOB: BE COLD`. | script + real fridge photo |
| 6 | `17.600-25.790` | `screens... software... and opinions` | Feature list reduced to one readable panel, huge trapped-by-app-screen WIT, `SOFTWARE HAS OPINIONS`. | script + approved WIT |
| 7 | `25.800-29.990` | `small technology committee` | Real appliance circuit-board photo, `TECHNOLOGY COMMITTEE`. | script + real circuit-board photo |
| 8 | `30.000-34.645` | `one tiny part fails... expensive to fix` | Real circuit-board photo, red tiny-part target, giant money-panic WIT, `WHOLE THING HARD TO FIX`. | script + real circuit-board photo |

## Review-Prevention

- Real image texture is now on screen for all big scenes.
- The old normal WIT set (`thinking`, `confused`, `facepalm`) was replaced with stronger approved poses.
- Feature nouns are grouped into one readable label and one software-opinion bubble, not scattered cards.
- Labels stay above the lower subtitle zone.
- Real fridge photo is used only as generic appliance/kitchen texture, not as a claim about that real model.

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Sync Status |
|---:|---|---|---|
| `0.000` | `complicated... not automatically bad` | `COMPLICATED IS NOT BAD` and skeptical WIT | matched |
| `3.800` | `Useful features... safer... better battery` | `USEFUL FEATURES ARE USEFUL`, `SAFER`, `BETTER BATTERY` | matched |
| `8.900` | `survives gravity` | `SURVIVES GRAVITY`, phone-panic WIT | matched |
| `10.600` | `one more thing that can break` | `EVERY FEATURE = BREAK POINT` | matched |
| `14.200` | `be cold` | `ONE JOB: BE COLD` | matched |
| `17.600` | `screens... software... and opinions` | feature panel, `SOFTWARE HAS OPINIONS`, trapped WIT | matched |
| `25.800` | `technology committee` | `TECHNOLOGY COMMITTEE` | matched |
| `30.000` | `one tiny part fails` | `TINY PART FAILS`, red target, money-panic WIT | matched |

## Assets

- Direct real background: `assets/section-05/fridge.jpg`
- Direct real failure texture: `assets/section-05/circuit-board.jpg`
- WIT poses used: `wit-pose-price-tag-suspicion.png`, `wit-pose-holding-phone-panic.png`, `wit-pose-trapped-by-app-screen.png`, `wit-pose-money-panic.png`
- Reference-only assets not used directly: water-dispenser refrigerator and control-panel photos
- Review mirror: `hyperframes/review/section-05.html` synced from this preview source
- Attribution: `projects/1-why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass with 2 non-blocking warnings: duplicate media discovery risk from repeated real-photo sources and one dense timed cue track`
- validate: `pass; no console errors; 80 text elements pass WCAG AA`
- inspect: `pass; 0 layout issues at 0.8, 4.8, 9.8, 12.6, 16.2, 22.6, 27.4, 31.8, and 34.1`
- snapshot: `pass via direct-composition contact sheet at 0.8, 4.8, 9.8, 12.6, 16.2, 22.6, 27.4, 31.8, and 34.1`
- preview server: `running on port 1005; Studio and direct composition URLs returned HTTP 200`
- render: `not requested`

No MP4/WebM export was created.
