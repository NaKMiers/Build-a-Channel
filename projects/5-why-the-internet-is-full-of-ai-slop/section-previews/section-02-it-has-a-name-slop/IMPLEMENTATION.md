# Section 2 Render Implementation

Video: `Why The Internet Is Full Of Garbage Now`
Section: `Section 2: It Has A Name: Slop`
Status: `built, ready for review`

## Result

- Preview project: `section-previews/section-02-it-has-a-name-slop/`
- Composition: `Section02Slop` (1920x1080, 36.715s)
- Port: `1002` - Studio: `http://localhost:1002/#project/section-02-it-has-a-name-slop`
- Direct: `http://localhost:1002/api/projects/section-02-it-has-a-name-slop/preview/comp/index.html`
- Audio: `section-02.mp3` (am_eric / 0.80)
- Source: `visual-plan/section-02-it-has-a-name-slop/...` + real word timings

## Big Scene / Cue Plan Implemented (8 scenes, pinned to word timings)

| Scene | Start | Voice cue (word @ s) | Base | WIT (side/pose) | Device |
|---|---:|---|---|---|---|
| 2.1 | 0.00 | "slop" @2.86 | sludge (dark) | right / presenting | "SLOP" stamp smash |
| 2.2 | 3.50 | "grey mush" @4.28; "pig trough" @5.64 | pig | left / disgust | "grey mush" + red arrow; "(yes pig slop)" |
| 2.3 | 6.20 | "not an insult" @6.76; "word of the year" @9.66 | dictionary | right / proud | CSS dict entry + gold WotY badge |
| 2.4 | 11.98 | "AI is evil" @15.84; "robots coming" @17.16 | toy robot | left / dismiss | "AI = EVIL ROBOTS" + red strike + "nope" |
| 2.5 | 18.30 | "different video" @18.64 | sludge (very dark) | center / deadpan | caption (mascot-only focus) |
| 2.6 | 19.48 | "quieter+dumber" @20.64; "master plan" @25.24 | corkboard | left / skeptical | pinned "A MASTER PLAN" note + red strike |
| 2.7 | 26.22 | "almost free" @29.18; "attention" @32.12; "quality" @32.96 | coins | right / lecturing | "almost FREE"; ATTENTION=PAID gold chip; QUALITY greyed |
| 2.8 | 33.34 | "flood started" @34.04; "still rising" @35.74 | sludge (rising) | center giant / uneasy | "a flood started"; "STILL RISING" smash |

## Render Review-Prevention Pass

- voice cue map: built from `voiceover/section-02-it-has-a-name-slop/section-02-word-timings.json` (whisper-tiny.en)
- contrast: sludge scenes darkened; big words yellow + dark outline; markup/notes/chips have own backgrounds (applies the S1 ending-contrast fix up front)
- WIT: one per scene, varied side/scale/pose; faces uncropped (verified in snapshot)
- motif: sludge reused 2.1/2.5/2.8 as the slop/flood motif (graded differently); pig/dictionary/robot/corkboard/coins are distinct bases
- HyperFrames mechanics: per-scene tracks, audio clip, deterministic GSAP, registered timeline

## Verification

- lint: 0 errors, 1 warning (`duplicate_media_discovery_risk` - intended sludge reuse)
- validate: 0 errors, 45 WCAG contrast warnings (stylized emphasis text; reads fine in snapshot)
- snapshots: 8-frame contact sheet at 2.9/5.6/10.0/17.3/18.9/25.7/32.5/35.9s -> `snapshots/contact-sheet.jpg`
- export: not requested (preview only)

## Notes

- Poses copied directly from the now-transparent shared library (no chroma-key step).
- Toy-robot + dictionary bases are CC BY-SA (credited in `assets/ATTRIBUTION.md`).
- Manual-edit preservation: if the owner edits this `index.html` in Studio, treat it as canonical next run.
