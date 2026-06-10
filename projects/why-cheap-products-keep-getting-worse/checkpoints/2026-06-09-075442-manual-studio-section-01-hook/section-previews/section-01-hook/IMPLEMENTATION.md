# Section 1 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 1: Hook`

Status:
`review-adjusted connected-scene preview and MP4 render ready for review`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-01-hook/`
- Source: `02-script.md` + `04-voiceover.md` + real WIT manifest + user reviews on connected big-scene pacing, fewer cues, meaningful markup, larger WIT, and exact callout alignment
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `21.205s`
- Voiceover: `section-01-hook-david23-am_eric-0.84.mp3`
- Visual plan: old visual plan explicitly skipped by user request; current revision follows the user-reviewed big-scene/small-cue mechanism with reduced cue count
- Render file: `projects/why-cheap-products-keep-getting-worse/renders/section-01-hook/section-01-hook-remake.mp4`
- MP4 frame check sheet: `projects/why-cheap-products-keep-getting-worse/renders/section-01-hook/mp4-check-frames/contact-sheet.png`

## Big Scene Plan Implemented

| Big Scene | Local Time | Base Visual | Purpose |
|---:|---:|---|---|
| 1 | `0.000-8.400` | Same chair photo holds through setup, product details, purchase, and first week. | Introduce the object without rushing through unrelated boards. |
| 2 | `8.400-16.400` | Same broken-leg close-up holds through legal creak, loose screw, and career-options leg. | Let the failure escalate inside one connected scene without a washed overlay. |
| 3 | `16.400-21.205` | Same desk/tag/receipt board holds through true-cost and final payoff. | Land the cost reveal and `FUTURE NOT INCLUDED` without a new visual reset. |

## Cue Plan Implemented

| Cue | Local Time | Voice Cue | Visual Change | Key Animation | Source |
|---:|---:|---|---|---|---|
| 1 | `0.000-2.200` | `I find a chair for nine dollars.` | Chair base plus `$9` tag and larger WIT. | none | script + WIT manifest |
| 2 | `2.200-5.350` | `four legs... a seat... confidence` | Same chair; labels only, no meaningless red leg marks. | none | script + WIT manifest |
| 3 | `5.350-8.400` | `So he buys it. For the first week... fine.` | Same chair; `SOLD`, hidden future tag, first-week mini calendar, fine label. | none | script |
| 4 | `8.400-11.250` | `noise that sounds like legal advice` | Broken-leg close-up with no white overlay; legal-ish creak and suspicious WIT. | none | script + WIT manifest |
| 5 | `11.250-16.400` | `screw gets loose... one leg begins exploring other career options` | Same broken-leg close-up; circle/arrow aligned to the actual screw and career-options label. | none | script + WIT manifest |
| 6 | `16.400-18.850` | `the cheap chair was not really cheap` | Desk/cost board; true-cost receipt and evidence WIT. | none | script + WIT manifest |
| 7 | `18.850-21.205` | `future not included` | Same desk/cost board; final large tag covers the board. | none | script |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `chair for nine dollars` | chair + `$9` tag | cue visible | matched |
| `2.200` | `four legs... seat... confidence` | product-detail labels | cue visible on same chair | matched |
| `5.350` | `buys it... first week` | sold/future tag/calendar | cue visible on same chair | matched |
| `8.400` | `legal advice` | `LEGAL-ISH CREAK` | new big scene base | matched |
| `11.250` | `screw... seat... one leg` | screw circle + career-options label | cue visible on same close-up | matched |
| `16.400` | `not really cheap` | true-cost receipt | new big scene base | matched |
| `18.850` | `future not included` | final tag | cue visible on same cost board | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| cue | next cue in same big scene | hard cut overlay change | user asked for no transitions; continuity comes from persistent base scene | low | keep |
| big scene | next big scene | hard cut | voiceover moves to a new idea | low | keep |

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-01-hook/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `thinking`, `price-tag-suspicion`, `suspicious`, `betrayed`, `holding-receipt-evidence`
- Review fixes applied: removed meaningless leg marks, removed failure-scene white overlay, enlarged WIT, reduced cue count from `12` to `7`, and aligned the screw circle to the actual screw in exported MP4 frames
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: pass with 2 non-blocking warnings: repeated media reference from reused static assets, and dense cue track
- validate: pass, no console errors, 220 text elements pass WCAG AA
- inspect: pass, 0 layout issues at `1.1,3.8,6.9,9.8,13.4,17.5,20.2`
- render: pass, standard MP4 rendered at `1920x1080`, `30fps`, H.264 video with AAC audio
- ffprobe: pass, MP4 duration `21.248s`, video stream duration `21.221s`, audio stream duration `21.248s`
- exported frame check: pass, 7 key frames extracted from MP4 and reviewed in `mp4-check-frames/contact-sheet.png`; screw callout checked in `frame-05.png`

## Notes

This revision keeps the approved real-WIT static render direction, but fixes the user's pacing and markup reviews by using three persistent big scenes with only seven cue states. No transitions or element animations are included.
