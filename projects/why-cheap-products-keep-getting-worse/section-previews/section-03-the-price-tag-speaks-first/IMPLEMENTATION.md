# Section 3 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 3: The Price Tag Speaks First`

Status:
`auto-adjusted WIT-dominance preview running on fixed section port`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-03-the-price-tag-speaks-first/`
- Source: `02-script.md` + `04-voiceover.md` + `05-visual-plan.md` + Section 3 visual plan and reference board
- Port: `1003`
- Studio URL: `http://localhost:1003/#project/section-03-the-price-tag-speaks-first`
- Direct composition URL: `http://localhost:1003/api/projects/section-03-the-price-tag-speaks-first/preview/comp/index.html`
- Runtime: `33.429s`
- Voiceover: `section-03-the-price-tag-speaks-first-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-03-the-price-tag-speaks-first/section-03-the-price-tag-speaks-first-visual-plan.md`
- Latest Auto Adjust backup: `manual-saves/auto-adjust-wit-dominance-20260612-151120-index.html`
- Latest Auto Adjust backup SHA256: `284B6B85B4C5525FCF92B264684BD83E3F7E1A8460CD5FD2768D5C250A4CF1DE`
- Latest Auto Adjust contact sheet: `snapshots/auto-adjust-wit-dominance-20260612-latest/contact-sheet-after.png`

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source Plan |
|---:|---:|---|---|---|---|
| 1 | `0.000-2.500` | `price tag speaks first` | Generated hidden-tag base, big tag speech label, suspicion WIT. | static hard cut | visual plan cue 1 |
| 2 | `2.500-5.500` | `price is easy to understand` | Same base, `$9`, `EASY TO READ`, check mark. | static hard cut | visual plan cue 2 |
| 3 | `5.500-8.400` | `wallet can read that very quickly` | Same base, wallet approval prop, empty-wallet WIT. | static hard cut | visual plan cue 3 |
| 4 | `8.400-10.900` | `future cost is quiet` | Same base and quiet hidden-tag label; no WIT so the hidden future-cost cue can breathe. | static hard cut | visual plan cue 4, auto-adjust WIT-density pass |
| 5 | `10.900-14.900` | `replacement you will buy in three months` | Same base, polite future-cost speech bubble and shocked WIT. | static hard cut | visual plan cue 5 |
| 6 | `14.900-17.200` | `helpful... very bad marketing` | Same base, `BAD MARKETING` stamp and deadpan WIT. | static hard cut | visual plan cue 6 |
| 7 | `17.200-21.900` | `Low price. Fast delivery.` | CSS-built checkout promise arena and first two promise signs; no WIT so the visible-promise list reads cleanly. | static hard cut | user revision of visual plan cue 7, auto-adjust WIT-density pass |
| 8 | `21.900-24.500` | `New color. Extra feature.` | Same checkout arena, two more promise signs and feature sparkle; no WIT so the list can stack without corner-sticker clutter. | static hard cut | user revision of visual plan cue 8, auto-adjust WIT-density pass |
| 9 | `24.500-26.700` | `sale sticker... saved your life` | Same checkout arena, large sale burst and hero joke, deadpan WIT. | static hard cut | user revision of visual plan cue 9 |
| 10 | `26.700-33.429` | `visible price... tomorrow` | Return to hidden-tag base, hidden future labels, final `TOMORROW` stamp, defeated WIT. | static hard cut | visual plan cue 10 |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `price tag speaks first` | `PRICE TAG SPEAKS FIRST` | visible immediately | matched |
| `2.500` | `price is easy to understand` | `$9`, `EASY TO READ` | cue visible | matched |
| `5.500` | `wallet can read` | wallet approval prop | cue visible | matched |
| `8.400` | `future cost is quiet` | quiet hidden tag | cue visible | matched |
| `10.900` | `replacement... three months` | future-cost speech bubble | cue visible | matched |
| `14.900` | `bad marketing` | red `BAD MARKETING` stamp | cue visible | matched |
| `17.200` | `Low price. Fast delivery.` | first visible promise signs on checkout board | cue visible | matched |
| `21.900` | `New color. Extra feature.` | second visible promise signs on checkout board | cue visible | matched |
| `24.500` | `sale sticker... saved your life` | sale burst and hero joke | cue visible | matched |
| `26.700` | `something is tomorrow` | hidden future tags and final stamp | cue visible | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| cue | next cue in same big scene | hard cut / overlay replacement | approved channel style; base scene provides continuity | low | keep |
| big scene | next big scene | hard cut | narration moves to a new mechanism beat | low | keep |

## Element Motion Notes

- Entrances: `none`
- Holds: `each cue is readable as a static paused frame`
- Emphasis: `speech burst, wallet stamp, quiet tag, bad marketing stamp, checkout promise signs, final tomorrow stamp`
- Exits: `none before cue replacement`
- Repeated effects avoided: `no repeated pop-in animation or default scene transition`

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-03-the-price-tag-speaks-first/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used after Auto Adjust: `price-tag-suspicion`, `empty-wallet`, `shocked`, `deadpan-side-eye`, `tiny-defeated`
- WIT layout update: WIT was reduced from every cue to selected emotional beats, then enlarged using visible alpha size rather than CSS box size. The remaining WIT poses now read around `32-36%` of frame width in the viewport on emotional beats, with lower-edge / side emotional placements and intentional lower-body overflow marked via `data-layout-allow-overflow`; faces, heads, shoulders, mouths, glasses, and props were checked in the latest seeked contact sheet.
- Direct generated support assets used: `price-tag-hiding-future-tags-generated.png`
- Reference-only generated support assets: `visible-shopping-promises-generated.png`, inspected and skipped because it repeated the same tabletop/tag language as Scene 1
- Reference-only real assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass with 4 non-blocking warnings: duplicate media discovery risk from repeated static base images, and dense tracks from 4 timed scene clips plus 10 timed cue clips`
- validate: `pass; no console errors; 30 WCAG contrast warnings remain from the sampler measuring span text against photo edges/hidden cue state contexts`
- inspect: `pass; 0 layout issues at 0.4, 2.8, 5.8, 8.8, 11.6, 15.6, 18.3, 22.6, 25.5, 28.5, 31.8, 33.0` after intentional lower-body WIT overflow markers
- render: `not requested`
- preview server: `running on port 1003; direct composition URL returned HTTP 200`
- visual snapshot check: `snapshots/auto-adjust-wit-dominance-20260612-latest/contact-sheet-after.png` was created from real Studio progress-bar seeks and inspected at `0.4`, `2.8`, `5.8`, `8.8`, `11.6`, `15.6`, `18.3`, `22.6`, `25.5`, `28.5`, `31.8`, and `33.0`; WIT is no longer a tiny corner sticker, nonessential WIT beats were removed, and faces/heads/shoulders remain readable

## Notes

This preview follows the revised Section 3 user feedback: Scene 3 should not feel like another version of Scene 1. The generated visible-promises image was inspected and intentionally skipped for direct use. Scene 3 is now a CSS-built checkout promise arena, while the final remembered frame remains a large visible price tag hiding smaller future-cost tags. Contrast warnings were not ignored blindly: risky label styles were tightened, then fresh Scene 3 snapshots were inspected. The remaining warnings are non-blocking validation sampler artifacts, not visible unreadable labels in the inspected frames.

Auto Adjust update:
The latest post-render pass preserved the current preview as canonical, created a fresh backup under `manual-saves/`, then fixed the remaining review risk: WIT still looked small because transparent PNG padding made large CSS boxes render as small visible characters. The pass removed the duplicate WIT from `cue-easy-price`, scaled WIT by viewport-clipped visible alpha size, moved nearby text blocks away from WIT instead of shrinking WIT, and kept intentional crop limited to lower body / edge peeking. No timing, audio, scene bases, or MP4/WebM export were changed.
