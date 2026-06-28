# Section 7 Visual Plan

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 7: Replacement Becomes Normal`

Status:
`planned and rendered - ready for review`

## Section Goal

Explain why replacement becomes the default even when people dislike waste - not by blaming the buyer, but by showing the *system* making replacement easier than repair. Land the recurring motif as a dry punchline: the cheap product quietly becomes `a subscription with extra steps`.

## Source Inputs

- Script: `02-script.md`, `Section 7: Replacement Becomes Normal`
- Voiceover: `voiceover/section-07-replacement-becomes-normal/scratch-audio/section-07-replacement-becomes-normal-david23-am_eric-0.84.mp3`
- Marked script: `voiceover/section-07-replacement-becomes-normal/section-07-replacement-becomes-normal-marked-script.md`
- Section duration: `29.312s`

## Timing Source

`estimated` - no `section-07-word-timings.json` exists, and word timings could not be generated in this environment (`hyperframes transcribe` requires whisper-cpp, which is not installed; no Python/faster-whisper). All cue times below are estimated proportionally from the marked script (word counts + `[pause]`/`[beat]` markers) against the `29.312s` audio. Structure is correct; fine sync may drift by a few tenths and should be confirmed in Studio against the audio (or re-pinned precisely if word timings are generated later).

## Narration

```text
When repair gets slow, confusing, or expensive, replacement starts looking normal.
Not because people love throwing things away.
Most people do not wake up and say, "Today I would like to create a small landfill with my headphones."
They replace things because the system makes replacement feel easier.
The repair quote is high.
The spare part is missing.
The product is already out of support.
The new one arrives tomorrow.
So WIT buys the product again.
The price tag smiles again.
The receipt prints again.
And the cheap product quietly becomes a subscription with extra steps.
```

## Visual Direction

- Big-scene/cue rhythm: `3 persistent big scenes, 7 cue states over 29.312s`
- Big scene rhythm: `replacement feels normal (e-waste) -> the system makes it easier (fulfillment) -> the re-buy loop (checkout/subscription)`
- Main metaphor: `the system quietly turns a one-time purchase into a repeating subscription`
- WIT path: `resigned (facepalm at the trash) -> [no WIT while the system explains itself] -> tired re-buyer holding a fresh receipt -> warm-deadpan at the "subscription" punchline`
- WIT density: `3 beats; Scene 1: 1 (held cues 1-2), Scene 2: 0 (breathing for the reasons list), Scene 3: 2 (re-buy + payoff)`
- Motion density: `hard cuts between big scenes; labels hard-show on the spoken beat; the only timed reveals are the landfill joke, the four staggered reasons, the price-tag "smile", and the deadpan payoff`
- Real-life texture: `real e-waste pile (Scene 1 base) and real fulfillment-warehouse boxes (Scene 2 base), both used clean (no gray wash)`
- Self-made base: `Scene 3 is a justified self-made CSS checkout/receipt scene - the channel builds receipts in CSS (Sections 1-2), the joke needs custom repeating "AGAIN" text, and clean brand-free real checkout/receipt photos were not available on Commons (all candidates were store-branded or contained people)`
- Retention strategy: `open on a literal pile of discarded gadgets (the result), explain the system as a fulfillment line, then pay off with a receipt that prints "AGAIN" three times`
- Do-not: `do not blame the buyer; the system, not the person, makes replacement easy`

## Big Scene Plan

| Big Scene | Local Time (est) | Voice Range | Persistent Base | Why This Scene | Cut Away When | Base Asset |
|---|---:|---|---|---|---|---|
| 1. Replacement Feels Normal | `0:00-11.74` | `When repair gets slow...` -> `...a small landfill with my headphones.` | Real e-waste pile (old keyboards/mice/cables) | Shows the end result of the loop and grounds "throwing things away" | On `They replace things because the system...` | `assets/section-07/ewaste-pile-photo-base.jpg` |
| 2. The System Makes It Easier | `11.74-21.14` | `They replace things because the system...` -> `The new one arrives tomorrow.` | Real fulfillment-warehouse boxes (replacement supply) | Turns "the system" into a literal replacement line; holds the four friction reasons | On `So WIT buys the product again.` | `assets/section-07/fulfillment-boxes-photo-base.jpg` |
| 3. The Re-Buy Loop | `21.14-29.312` | `So WIT buys the product again...` -> `...a subscription with extra steps.` | Real warm cherry-wood surface + CSS objects (new box, smiling price tag, re-buy receipt) | Lands the loop + the `subscription with extra steps` punchline | End hold to `29.312s` | `assets/section-07/checkout-wood-photo-base.jpg` (Dietmar Rabich, CC BY-SA 4.0) |

## Cue State Timeline

| Cue | Local Time (est) | Voice Cue | Scene | What Changes | Motion | WIT | Label / Markup |
|---|---:|---|---|---|---|---|---|
| 1 | `0:00-3.93` | `...replacement starts looking normal.` | 1 | Hard cut to e-waste; `REPLACEMENT FEELS NORMAL` title; resigned WIT rises lower-right | hard-show + scene in | `facepalm` giant lower-right `width 1080px` | `REPLACEMENT FEELS NORMAL` |
| 2 | `3.93-11.74` | `Not because people love throwing things away... small landfill with my headphones.` | 1 | `NOT BECAUSE WE LOVE WASTE`; on the joke (`~5.79`) the red `A SMALL LANDFILL OF HEADPHONES` hard-shows | hard-show + delayed note | `facepalm` held | `NOT BECAUSE WE LOVE WASTE`; red `A SMALL LANDFILL OF HEADPHONES` |
| 3 | `11.74-14.84` | `They replace things because the system makes replacement feel easier.` | 2 | Hard cut to fulfillment boxes; `THE SYSTEM MAKES IT EASIER` | hard-show | none | `THE SYSTEM MAKES IT EASIER` |
| 4 | `14.84-21.14` | `The repair quote is high. / spare part is missing. / out of support. / new one arrives tomorrow.` | 2 | Four friction rows appear one per spoken reason; the 4th (`NEW ONE ARRIVES TOMORROW`) is green = the easy path | hard-show staggered | none (list breathes) | `REPAIR QUOTE: HIGH` / `SPARE PART: MISSING` / `OUT OF SUPPORT` / green `NEW ONE ARRIVES: TOMORROW` |
| 5 | `21.14-24.51` | `So WIT buys the product again. The price tag smiles again.` | 3 | Hard cut to checkout; `BUY AGAIN` stamp; tired WIT holding a fresh receipt; the smiling price tag appears on `~23.18` | hard-show + delayed price tag | `holding-receipt-evidence` giant lower-right `width 1320px` | `BUY AGAIN` |
| 6 | `24.51-26.22` | `The receipt prints again.` | 3 | The `RE-BUY RECEIPT` prints: `same product / shipping / your time -> AGAIN x3` | hard-show | none | receipt rows |
| 7 | `26.22-29.312` | `[deadpan] And the cheap product quietly becomes a subscription with extra steps.` | 3 | On the deadpan beat (`~26.7`) the payoff `SUBSCRIPTION WITH EXTRA STEPS` + deadpan WIT hard-show | hard-show payoff reveal | `deadpan-side-eye` giant lower-right `width 1440px` | red `SUBSCRIPTION WITH EXTRA STEPS` (underlined) |

## WIT Pose Plan

| Cue | Time (est) | Emotion | Pose File | Placement / Scale | Safe Crop | Why |
|---|---:|---|---|---|---|---|
| 1-2 | `0:00-11.74` | resigned, "here we go again" | `wit-pose-facepalm.png` | lower-right giant, `width 1080px` (`right:-150 / bottom:-300`) | face/head/shoulders clear; only lower body cropped by edge | a human reacting to the pile of discarded gadgets |
| 5 | `21.14-24.51` | tired re-buyer | `wit-pose-holding-receipt-evidence.png` | lower-right giant, `width 1320px` (`right:-360 / bottom:-360`) | face + receipt-in-hand clear; lower body cropped by edge | "buys the product again" made physical |
| 7 | `26.22-29.312` | warm-deadpan | `wit-pose-deadpan-side-eye.png` | lower-right giant, `width 1440px` (`right:-380 / bottom:-470`) | face/head/shoulders clear; lower body cropped by edge | carries the "subscription with extra steps" punchline |

WIT density note: 3 total beats; Scene 1 = 1 (held cues 1-2), Scene 2 = 0 (the four reasons must read), Scene 3 = 2 (re-buy reaction + deadpan payoff). No big scene exceeds 2.

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety |
|---|---|---|---|---|
| e-waste pile | `real image` | Wikimedia Commons, Reconrabbit, `CC0`, inspected | Scene 1 base | `safe direct asset`; no people, no brand logo (a baked-in "ALL TRASH" arrow is generic and on-theme) |
| fulfillment boxes | `real image` | Wikimedia Commons, WillNemoy, `CC BY-SA 4.0`, inspected | Scene 2 base | `safe direct asset`; no people, no brand (bin codes only) |
| checkout counter / card reader / new box / price tag / re-buy receipt | `self-made CSS` | built in `index.html` | Scene 3 base + objects | `safest route`: brand-free, exact repeating "AGAIN" text control |
| WIT poses | `local channel asset` | project `assets/wit/manifest.json` | cues 1-2, 5, 7 | `safe channel asset` |
| payment terminal / supermarket checkout / store receipt photos | `real image` | Wikimedia Commons | `reject for direct use` | all candidates were store-branded (WAON, Publix, Top1Toys, etc.) or contained real people; kept as inspiration only |

## Render Handoff

- Composition: `Section07ReplacementBecomesNormal`, `1920x1080`, `data-duration 29.312`, font `PatrickHandLocal`
- Scene clips (track 1): `scene-ewaste` 0/11.74, `scene-system` 11.74/9.4, `scene-subscription` 21.14/8.172
- Cue clips (track 2): 7 cues with the starts/durations above; the four reasons stagger via GSAP opacity sets inside `cue-four-reasons`
- Timed reveals (GSAP, estimated): landfill note `5.79`; reasons `16.17 / 17.5 / 19.36`; price-tag smile `23.18`; deadpan payoff `26.7`
- WIT-bearing cues carry `data-layout-allow-overflow` + `overflow:visible` (intentional off-canvas giant WIT)
- Motion: hard-show default; no impact/transition effects; payoff underline is a `border-bottom` on the text span (full text width, one line)
- Suggested inspect / snapshot timestamps: `2, 8, 13, 18, 20, 22.5, 25, 28`
- Must not invent: the 3 scene bases, the 7 cue beats, the four-reason stagger, the receipt "AGAIN" loop, the WIT poses/placements, the payoff text

## Review-Prevention Checklist

- voice sync mapped to phrases: `yes (estimated times; confirm in Studio)`
- big-scene rhythm: `yes - 3 persistent scenes, hard cuts at 11.74 / 21.14`
- cue density: `yes - 7 cue states over 29.312s; the 4 reasons are one staggered cue, not four cuts`
- motion density: `yes - hard-show default`
- WIT rhythm: `yes - 3 beats, Scene 2 WIT-free`
- WIT size/crop: `verify at QA - all three are giant lower-right; faces clear on the contact sheet`
- real scene base per scene: `yes - 2 real photos + 1 justified self-made CSS scene; no flat-gradient-only beat`
- brand/people safety: `yes - bases are brand-free and people-free`
- subtitle-safe lower third: `payoff sits at top:812 (above the subtitle zone); confirm at QA`

## Approval Checks

- script promise paid off: `yes - "subscription with extra steps" lands as the payoff`
- safe for English learners: `yes - short labels, one idea per beat, a clear 4-item reason list`
- does not blame the buyer: `yes - the system makes replacement easy; WIT is tired, not foolish`
- ready for render: `yes - already rendered to section-previews/section-07-replacement-becomes-normal/`
