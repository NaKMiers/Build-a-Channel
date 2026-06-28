# Section 1 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 1: Hook: Is Any Of This Real?`

Status:
`built, ready for review`

## Result

- Preview project: `section-previews/section-01-hook/`
- Source: `04-visual-plan.md` Section 1 + real word timings
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `31.253s` (matches voiceover)
- Voiceover: `section-01-hook.mp3` (am_eric / 0.80)
- Visual plan: `visual-plan/section-01-hook/section-01-hook-visual-plan.md`

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue (word @ s) | Big Scene | What Changes | Motion | WIT Placement / Crop Guard | Label / Markup | Sync |
|---:|---:|---|---|---|---|---|---|---|
| S1 | 0.00 | "scroll" @3.28 | couch + phone | WIT in; label | hard-show | right, ~1180px, legs crop only | "scroll for 10 seconds..." | pinned |
| S2 | 4.84 | "be honest" @5.22; "human" @7.12 | dark room | question; chip | smash; pop | center giant ~1150px | "how much is REAL?"; "% human?" | pinned |
| S3 | 8.58 | "all of it" @10.48 | laptop desk | stamp | smash | left ~1080px | "3 years ago"; green "100% HUMAN" | pinned |
| S4 | 11.62 | "good luck" @11.88 | phone on table | 2-word deadpan | hard-show | center ~1240px, head clear | "today..." / "good luck." | pinned |
| S5 | 12.70 | "a photo of a shrimp" @14.52; "Jesus" @15.92 | living room | Shrimp post; caption | pop; smash | right ~1150px | post "AMEN 47K"; "...a shrimp. as Jesus." | pinned |
| S6 | 16.56 | "a new story" @16.84; "never happened" @18.24 | newsroom | news card; markup | pop; smash | left ~1100px | fake-news card; red "DIDN'T HAPPEN" | pinned |
| S7 | 19.08 | "a hit song" @19.40; "does not exist" @20.74 | studio console | band card; caption | pop; smash | right ~1110px | fake-band card; "0 real members" | pinned |
| S8 | 21.76 | "garbage" @23.38; chips @24.66/24.98/25.40; "nobody" @28.40 | grey-sludge flood | GARBAGE; chips; sink | smash; pop | center GIANT ~1240px (drowning) | "GARBAGE"; "cheap./fake./mass-produced."; "...nobody told it to." | pinned |
| S9 | 30.00 | "why" @30.82 | settled sludge | WHY | smash | center ~1120px | "WHY?" | pinned |

## Render Review-Prevention Pass

- voice cue map completed: yes (from `section-01-word-timings.json`, whisper-tiny.en)
- big-scene sanity checked: yes (one idea per scene; sludge motif births S8, returns S9)
- cue density checked: yes (one hero + at most one caption per scene)
- motion density checked: yes (hard-show ordinary labels; smash/pop only on emphasis/reveals)
- WIT density: one WIT per scene, varied side/scale/pose
- WIT crop/collision checked: faces/heads uncropped in snapshot; WIT clear of labels
- markup target checked: red "DIDN'T HAPPEN" on the fake-news card (note: slightly cramped, optional nudge)
- scene differentiation checked: distinct base per scene (sludge reused S8->S9 as deliberate continuity)
- HyperFrames mechanics checked: per-scene tracks, audio clip, deterministic GSAP, registered timeline
- render decisions beyond plan: substituted 2 poses to real library names; chroma-keyed green poses; clip-path crop on band card; estimated->replaced with real word timings

## Assets

- Shared asset folder: `../../assets` (junction `./assets`)
- Section assets: 10 image files + 2 pre-made cards (owner-generated) + 9 transparent poses (`assets/poses/`)
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: 0 errors, 1 warning (`duplicate_media_discovery_risk` - intended image reuse)
- validate: 0 errors, 15 WCAG AA contrast warnings (stylized emphasis text; reads fine in snapshot)
- inspect: package `check` script set with `--at` cue mid-points
- snapshots: 9-frame contact sheet at 3.6/6.5/10.8/12.4/15.5/18.6/21.0/25.8/30.9s -> `snapshots/contact-sheet.jpg`
- export/render: not requested (preview only)

## Notes

- Tooling on this box: no ffmpeg/whisper-cpp on PATH; used a temp static ffmpeg (`@ffmpeg-installer/ffmpeg`)
  to chroma-key poses and decode audio, and `@xenova/transformers` whisper-tiny.en for word timings.
- Manual-edit preservation: if the owner edits this `index.html` in Studio, treat it as canonical next run.
