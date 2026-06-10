# Section 1 Render Implementation

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 1: Hook`

Status:
`rebuilt for review`

## Result

- Preview project: `projects/why-everyone-pretends-to-be-busy/section-previews/section-01-hook`
- Source: section script, section voice timing, user feedback, WIT asset library, new reference review
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `24.085s`
- Voiceover: `assets/voiceover/section-01-hook-young-fast-am_adam-1.05.mp3`
- Visual plan: intentionally skipped because the user identified it as the likely failure source

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source |
|---|---:|---|---|---|---|
| 1 | `0.000-2.263` | `Here is something weird about modern life.` | Modern life label, suspicious WIT, weird label | none | new override |
| 2 | `2.263-4.510` | `The less time you have to do real work` | tiny clock, real-work paper being squeezed | none | new override |
| 3 | `4.510-6.058` | `the more professional you look` | output card points to professional badge | none | new override |
| 4 | `6.058-8.498` | `calendar is full, inbox is exploding` | full calendar plus exploding inbox | none | new override |
| 5 | `8.498-10.638` | `phone keeps making tiny panic noises` | panic phone plus channel WIT phone-panic pose | none | new override |
| 6 | `10.638-12.351` | `people assume you are important` | VIP badge, medal, awkward WIT celebration | none | new override |
| 7 | `12.351-15.086` | `sit quietly and think about one hard problem` | thinking WIT, desk, hard problem box | none | new override |
| 8 | `15.086-19.855` | `lazy... unemployed... small spiritual crisis` | defeated WIT under public judgment stamps | none | new override |
| 9 | `19.855-21.275` | `everyone becomes busy` | busy label, stacked app windows, typing WIT | none | new override |
| 10 | `21.275-24.085` | `good at looking busy` | trapped WIT behind fake busy screen and curtain | none | new override |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.926` | `weird` | `something weird` | already visible | aligned |
| `2.481` | `less` | `LESS TIME` | hard-cut board visible | aligned |
| `3.783` | `real work` | `real work` label and task paper | already visible | aligned |
| `4.961` | `professional` | `PRO` badge | hard-cut board visible | aligned |
| `6.464` | `calendar` | full calendar | hard-cut board visible | aligned |
| `7.582` | `inbox` | inbox card | already visible | aligned |
| `8.949` | `phone` | phone card and phone-panic WIT | hard-cut board visible | aligned |
| `9.942` | `panic` | `tiny panic noises` label | already visible | aligned |
| `11.601` | `important` | VIP badge and medal | already visible | aligned |
| `13.178` | `quietly` | quiet thinking board | hard-cut board visible | aligned |
| `16.266` | `lazy` | `LAZY?` stamp | already visible | aligned |
| `17.114` | `unemployed` | `UNEMPLOYED?` stamp | already visible | aligned |
| `18.879` | `spiritual crisis` | crisis stamp | already visible | aligned |
| `20.600` | `busy` | `BUSY` board | already visible | aligned |
| `23.266` | `looking busy` | `LOOKING BUSY` board | already visible | aligned |

## Transition Plan

| From | To | Transition | Reason | Decision |
|---|---|---|---|---|
| all boards | next board | hard cut | user requested no transitions | keep static |

## Assets

- Shared asset folder: `projects/why-everyone-pretends-to-be-busy/assets`
- WIT source copied from: `projects/why-cheap-products-keep-getting-worse/assets/wit`
- Section runtime asset path: preview-local `assets` junction
- Font: `assets/fonts/patrick-hand-latin.woff2`, downloaded from Google Fonts and stored locally so MP4 rendering does not fall back to a document-style font.
- No new generated image was needed for this pass; all non-WIT visuals are CSS illustrations.

## Verification

- lint: passes with one accepted dense-track warning
- validate: passes with non-blocking AudioContext and contrast warnings
- inspect: passes, `0` layout issues across `9` samples
- render: completed at `renders/section-01-hook/section-01-hook-remake.mp4`

## Notes

The board count is intentionally higher than the rejected version because the voiceover contains several quick visual concepts in 24 seconds. Each board is static and sparse, so the section should feel like illustrated beats rather than presentation slides.
