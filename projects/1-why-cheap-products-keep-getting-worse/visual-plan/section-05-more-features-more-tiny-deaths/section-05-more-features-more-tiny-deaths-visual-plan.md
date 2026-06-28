# Section 5 Visual Plan

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 5: More Features, More Tiny Deaths`

Status:
`remade from scratch 2026-06-21 - planned and rendered, ready for review`

## Section Goal

Explain fairly that more features are not automatically bad, then show how every extra feature is one more thing that can break - using one fridge that visibly grows from "be cold" into a "small technology committee," and pay off with a tiny failed part that is hard and expensive to fix.

## Source Inputs

- Script: `02-script.md`, `Section 5: More Features, More Tiny Deaths`
- Voiceover: `voiceover/section-05-more-features-more-tiny-deaths/scratch-audio/...david23-am_eric-0.84.mp3` (actual duration `34.704s`)
- Marked script: `voiceover/section-05-more-features-more-tiny-deaths/section-05-more-features-more-tiny-deaths-marked-script.md`

## Timing Source

`whisper-derived` - audio transcribed with Whisper (`transformers.js` / `@xenova/whisper-tiny.en`, WASM, no native deps) and saved to `voiceover/section-05-.../section-05-word-timings.json`. Every scene cut and reveal below is pinned to real word timings. Key anchors: "not automatically bad" `3.04` / safer `6.22` / better battery `7.46` / phone-survives-gravity `8.86` / "but every extra feature... break" `11.86` / "simple fridge... be cold" `15.04` / screens `18.44` / sensors `19.26` / water lines `19.68` / ice dispenser `20.24` / software `21.44` / "and opinions" `21.66` / "not just a product" `22.78` / "technology committee" `26.82` / "one tiny part fails" `30.32` / "more expensive to fix" `33.22`.

## Visual Direction

- Big-scene/cue rhythm: `2 persistent big scenes, 5 cue states over 34.704s`
- Big scene rhythm: `one fridge that evolves simple -> overloaded -> "committee" (0-29.52), then a failed control board (29.52-34.704)`
- Main metaphor: `the same fridge gains feature labels until it is a "small technology committee in your kitchen"; then one tiny part fails`
- WIT path: `mild approval that features can be good -> overwhelmed/confused at the committee -> money-panic at the expensive repair`
- WIT density: `3 beats; awkward-celebration (cues 1-2), confused (committee reveal), money-panic (circuit payoff); the turn and the feature pile-up are WIT-free so the labels read`
- Motion density: `hard cut only at 29.52; labels hard-show; the only timed reveals are the good-feature checks, the staggered feature pile, the committee label, and the payoff`
- Real-life texture: `2 real photo bases used clean - a real kitchen fridge and a real appliance control board`
- Intentional clutter: `the 6 feature tags accumulate around the fridge - the "too many labels" IS the technology-committee joke (per the channel's Section-5 note)`
- Fairness: `do not imply features are bad or that old products were always better; "features can be good" is shown with green checks before the turn`

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base | Why | Base Asset |
|---|---:|---|---|---|---|
| 1. The Fridge (simple → committee) | `0:00-29.52` | `The second reason... products can get more complicated.` -> `...living in your kitchen.` | Real kitchen fridge photo | The fridge gains feature labels until it is an overloaded "committee" | `assets/section-05/fridge.jpg` |
| 2. The Failed Part | `29.52-34.704` | `And when one tiny part fails...` -> `...harder and more expensive to fix.` | Real appliance control board photo | One tiny component = a hard, expensive repair | `assets/section-05/circuit-board.jpg` |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Scene | What Changes | Motion | WIT | Label / Markup |
|---|---:|---|---|---|---|---|---|
| 1 | `0:00-3.04` | `The second reason... more complicated.` | 1 | Fridge in; `2ND REASON: MORE FEATURES`; approving WIT | hard-show + scene in | `awkward-celebration` giant lower-right `width 1040px` | `2ND REASON: MORE FEATURES` |
| 2 | `3.04-11.86` | `This is not automatically bad... a phone that survives gravity is basically a public service.` | 1 | green `FEATURES CAN BE GOOD` + checks `SAFER` / `BETTER BATTERY` (7.46) / `TOUGHER PHONE` (8.86) | hard-show staggered | `awkward-celebration` held | green checks |
| 3 | `11.86-15.04` | `But every extra feature is also one more thing that can break.` | 1 | red `EVERY FEATURE = ONE MORE THING TO BREAK` | hard-show | none (the turn reads) | red turn label |
| 4 | `15.04-29.52` | `A simple fridge has one main job: be cold. A modern fridge may have screens, sensors, water lines, ice dispensers, software, and opinions... a small technology committee living in your kitchen.` | 1 | `ONE JOB: BE COLD :)`, then 6 feature tags pile on (screens 18.44 / sensors 19.26 / water lines 19.68 / ice 20.24 / software 21.44 / + opinions 21.66), then `A SMALL TECHNOLOGY COMMITTEE IN YOUR KITCHEN` (26.82) + confused WIT | hard-show staggered pile | `confused` (reveal 26.82) | feature tags; yellow committee label |
| 5 | `29.52-34.704` | `And when one tiny part fails... harder and more expensive to fix.` | 2 | Hard cut to control board; `ONE TINY PART FAILS`; payoff `HARDER + MORE EXPENSIVE TO FIX` (33.22) + money-panic WIT | hard-show payoff reveal | `money-panic` giant lower-right `width 1320px` | red `ONE TINY PART FAILS`; payoff (underlined) |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Why |
|---|---:|---|---|---|---|
| 1-2 | `0:00-11.86` | mild approval (features can be good) | `wit-pose-awkward-celebration.png` | lower-right giant `width 1040px` (`right:-160 / bottom:-300`) | keeps the section fair, not anti-technology |
| 4 | `~26.82-29.52` | overwhelmed/confused | `wit-pose-confused.png` | lower-right giant `width 1280px` (`right:-340 / bottom:-360`) | reacts to the "technology committee" pile-up |
| 5 | `29.52-34.704` | money-panic | `wit-pose-money-panic.png` | lower-right giant `width 1320px` (`right:-340 / bottom:-400`) | "more expensive to fix" |

WIT density: 3 beats; the turn (cue 3) and the feature pile (cue 4 before 26.82) are WIT-free so the clutter joke reads.

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety |
|---|---|---|---|---|
| Kitchen fridge | `real image` | Wikimedia Commons, Infrogmation of New Orleans, `CC BY-SA 4.0` | Scene 1 base | `safe asset`; generic fridge texture, no people; no claim this model failed |
| Appliance control board | `real image` | Wikimedia Commons, Phiarc, `CC BY-SA 4.0` | Scene 2 base | `safe asset`; no people, no brand |
| WIT poses | `local channel asset` | project `assets/wit/manifest.json` | cues 1-2, 4, 5 | `safe channel asset` |

Note: the 2 real bases are retained from the prior approved Section 5 sourcing (already in `assets/ATTRIBUTION.md`); the composition was rebuilt from scratch and voice-synced.

## Render Handoff

- Composition: `Section05MoreFeaturesMoreTinyDeaths`, `1920x1080`, `data-duration 34.704`, font `PatrickHandLocal`
- Scene clips: `scene-appliance` 0/29.52, `scene-circuit` 29.52/5.184
- Cue clips: 5 cues with the starts/durations above; good-feature checks + the feature pile + committee + payoff stagger via GSAP opacity sets pinned to word timings
- WIT-bearing cues carry `data-layout-allow-overflow` + `overflow:visible`
- Motion: hard-show default; payoff underline = `border-bottom` on the text span (one line)
- Suggested inspect / snapshot timestamps: `1.5, 8, 13, 19, 22.5, 27.5, 31, 34`
- Must not invent: the 2 scene bases, the 5 cue beats, the feature pile-up, the WIT poses/placements, the payoff text

## Review-Prevention Checklist

- voice sync mapped to phrases: `yes - pinned to whisper word timings (section-05-word-timings.json)`
- big-scene rhythm: `yes - one evolving fridge + one failed-part scene, hard cut at 29.52`
- cue density: `yes - 5 cues; the 6-item feature list is one staggered pile, not six cuts`
- intentional clutter justified: `yes - the pile-up IS the technology-committee joke`
- WIT rhythm: `yes - 3 beats; turn + pile are WIT-free`
- fairness: `yes - features shown as good first (green checks) before the turn`
- real scene base per scene: `yes - 2 real photos, no flat-gradient beat`
- subtitle-safe lower third: `payoff at top:812; confirm at QA`

## Approval Checks

- more features != better product: `yes - features good first, then "one more thing to break"`
- does not imply old products were better: `yes`
- technology-committee joke visible through too many labels: `yes`
- WIT overwhelmed, not anti-technology: `yes`
- ready for render: `yes - rendered to section-previews/section-05-more-features-more-tiny-deaths/ on port 1005`
