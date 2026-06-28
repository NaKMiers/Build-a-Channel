# Section 3 Visual Plan

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 3: The Receipt Knows`

Status:
`REMADE 2026-06-24 to subscription-style (see IMPLEMENTATION.md for the as-built)`

> Remake note: owner rejected the first pass (plain wood/white bases, all-CSS receipts, small WIT) as "too simple." Rebuilt to the standing vivid-hook template: 5 scenes, vivid dark money bases (cash → coins → basket → red curtain → cash), giant kinetic numbers ($5 → $10), popping stamps/toast/banner, a glowing FREE payoff, and GIANT WIT (~1120–1200px) varied per scene. The big kinetic number is the hero; the receipt is now a small supporting strip. The scene/cue tables below describe the original 3-scene plan; the as-built 5-scene version is documented in `section-previews/.../IMPLEMENTATION.md`.

## Section Goal

Show the part the sign hides - what you actually SPEND. The receipt is the hero: 50% off = one item, total $5; BOGO = full $10 and a second item you didn't need. Land "smaller price vs bigger basket," then "half price was the better deal" and hand off to the magic word.

## Source Inputs

- Script: `02-script.md` → Section 3
- Voiceover: `voiceover/section-03-the-receipt-knows/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-03-the-receipt-knows/section-03-word-timings.json`
- Section duration: `32.235s`

## Narration

```text
Here is the part the sign hides: what you actually spend.
Fifty percent off, you wanted one thing, you paid five, done.
Buy one, get one free? To get the "free" one, you first coughed up the full ten. You spent twice as much. In one trip. And you carried home a second one you did not need.
That is the whole game. Fifty percent off is a smaller price. Buy one, get one free is a bigger basket.
One saves your money. The other spends it, and smiles at you while it robs you.
If you only wanted one, half price was the better deal. You walked right past it, because the other sign said the magic word.
```

## Visual Direction

- Big-scene/cue rhythm: 3 big scenes, ~9 cue beats
- Big scene rhythm: receipts on the counter (spend) → overflowing basket (bigger basket / robbed) → the two signs (better deal / magic word)
- Cue-state count: 9
- Main visual metaphor: the receipt total ($5 vs $10) and the basket size; the recurring "FREE/50% OFF" signs return as the hand-off
- WIT emotional path: holding-receipt suspicion → empty-wallet betrayal → facepalm
- WIT density: 3 beats (1 per scene)
- Motion density: hard-show receipt lines on their words; impact on the $10 total, the "twice as much" stamp, the "ROBBED" stamp, and the magic-word glow
- Real-life texture: real wood counter, real overflowing veg basket
- Real image references: 2 CC0 bases; receipts CSS
- Generated/support assets: none
- Viewer attention strategy: the receipts build the contrast; the basket makes "bigger basket" literal
- Retention risk: "$5 vs $10" can blur; fix by printing the two receipts with clear TOTALs and a "×2 = twice as much" stamp
- Visual fix: two receipts side by side, TOTAL $5 (1 item) vs TOTAL $10 (2 items)
- Red markup: a red ring/underline on the $10 TOTAL and a "ROBBED" stamp; a check on the 50%-off sign as "better deal"
- Motion rule: hard-show; impact for the $10 total, stamps, magic-word glow

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path |
|---|---:|---|---|---|---|---|---|
| A - The receipts (what you spend) | 0.0–15.12 | "the part the sign hides…" → "a second one you did not need." | Dark wood counter + two CSS receipts | show $5 (1 item) vs $10 (2 items) - you spent twice as much | at "That is the whole game" | wood CC0 + CSS receipts | `base-a-wood-table.jpg` |
| B - Bigger basket / robbed | 15.12–25.32 | "the whole game… smaller price… bigger basket… robs you." | Overflowing veg basket | "smaller price vs BIGGER BASKET"; the deal robs you while smiling | at "If you only wanted one" | veg basket CC0 | `base-c-veg-basket.jpg` |
| C - Half price was better / magic word | 25.32–32.235 | "half price was the better deal… the magic word." | Wood counter (cooler) + two CSS signs | half price was the better deal; you walked past it for the magic word | end | wood CC0 (callback) + CSS signs | `base-a-wood-table.jpg` (cooler) |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion | WIT Pose / Size / Crop | Label / Markup | Why |
|---|---:|---|---|---|---|---|---|---|
| A1 | 1.78 | "what you actually spend" | A | hand label + receipt slot | hard-show | `holding-receipt-evidence` RIGHT ~1/3 | "what you actually spend" | open on the receipt |
| A2 | 3.20 | "Fifty percent off… paid five, done" | A | Receipt #1 prints: TOTAL $5 (1 item) | hard-show | holding-receipt | receipt-50 | the smaller spend |
| A3 | 6.86 | "Buy one, get one free" | A | Receipt #2 starts beside it | hard-show | - | receipt-bogo header | the other deal |
| A4 | 8.78 | "coughed up the full ten" | A | Receipt #2 TOTAL $10 + red ring | impact | - | "$10" red ring | the real spend |
| A5 | 10.62 | "twice as much. In one trip." | A | "×2 - TWICE AS MUCH" stamp | impact | - | "×2" stamp | the punch |
| A6 | 12.82 | "a second one you did not need" | A | "+1 you didn't need" tag on receipt #2 | hard-show | - | "+1 unwanted" | the hidden cost |
| B1 | 16.32 | "smaller price… bigger basket" | B | cut to basket; "50% OFF = smaller price" vs "BOGO = BIGGER BASKET" | transition + hard-show | - | two labels | the reframe |
| B2 | 22.20 | "spends it… robs you while smiling" | B | "ROBBED" stamp + WIT | impact | `empty-wallet` LEFT ~1/2 | "robs you (with a smile)" | the betrayal |
| C1 | 25.32 | "half price was the better deal" | C | cut to signs; check on 50% OFF sign | transition + impact | - | "✓ better deal" | fairness: 50% off wins if you want one |
| C2 | 29.78 | "the other sign said the magic word" | C | FREE sign glows; WIT facepalm | impact | `facepalm` RIGHT ~1/2 | "the magic word →" | hand-off to Section 4 |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop | Why |
|---|---:|---|---|---|---|---|
| A | 1.78–15 | suspicion | `wit-pose-holding-receipt-evidence.png` | RIGHT ~1/3, anchored high | face/glasses/shoulders in; legs crop | "the receipt knows" - WIT studies it |
| B2 | 22.20 | betrayal | `wit-pose-empty-wallet.png` | LEFT ~1/2 | face clear; labels cleared RIGHT | robbed while smiling |
| C2 | 29.78 | facepalm | `wit-pose-facepalm.png` | RIGHT ~1/2 | face clear; signs cleared LEFT | walked right past the better deal |

WIT density note:

- Total: 3 (1 per scene)
- Above 2 in any scene: no
- No-WIT beats: A3–A6, B1, C1

## Markup And Label Plan

| Cue | Time | Markup | Motion | Target | Why |
|---|---:|---|---|---|---|
| A4 | 8.78 | red ring on "$10" | impact | receipt #2 total | the real spend lands |
| A5 | 10.62 | "×2 TWICE AS MUCH" stamp | impact | between receipts | the punch |
| B2 | 22.20 | "ROBBED" stamp | impact | over basket | the betrayal |
| C1 | 25.32 | green check on 50% OFF sign | impact | the 50% sign | 50% off is the better deal for one |

## Reference And Asset Plan

| Asset | Type | Source | Use | Path |
|---|---|---|---|---|
| Wood table | real photo CC0 | StockSnap | A + C base | `base-a-wood-table.jpg` |
| Veg basket | real photo CC0 | rawpixel | B base | `base-c-veg-basket.jpg` |
| Receipts / signs / stamps | CSS | self-made | A/C devices | n/a |
| WIT poses | local PNG | shared | A/B/C | shared poses |

## HyperFrames Guidance

- Composition target: `Section03Receipt`, 1920x1080, total `32.235s`
- Big scene count: 3; cue count: 9
- Scene components: real photo base + scrim + CSS receipts (thermal-paper look, monospace) + CSS signs + stamps + WIT
- Timing: pinned to `section-03-word-timings.json` (word starts cited per cue)
- Motion density: hard-show receipt lines; impact on $10 total, ×2 stamp, ROBBED stamp, magic-word glow
- WIT: 3 beats (holding-receipt R, empty-wallet L, facepalm R); anchored high, legs-only crop; labels cleared opposite WIT
- No-WIT breathing beats: the receipt-build cues, B1, C1
- Suggested QA timestamps: 4.5 (receipt $5), 9.2 ($10 ring), 11 (×2 stamp), 14 (+1 unwanted), 20.5 (bigger basket), 23.5 (ROBBED + WIT), 27 (better-deal check), 31.5 (magic word + facepalm)
- Build risks: keep receipts legible (monospace, big TOTAL); wood reused for A+C must be graded cooler in C; basket-on-white is bright → darken
- Must not invent: scene order, the $5-vs-$10 receipt contrast, word-pinned reveals, WIT poses/sides, label text, impact beats

## Review-Prevention Checklist

- voice sync mapped to phrase cues: yes (word-timings cited)
- big-scene rhythm: 3 scenes; A is the receipt build (many reveals keep it alive)
- cue density readable: yes
- motion density hard-show default: yes
- impact reserved for totals/stamps/glow: yes
- WIT rhythm not overused: yes (3)
- WIT size readable / crop safe: yes
- WIT vs text both ways: yes
- red markup targets exact object: yes ($10 total, signs)
- scene bases differentiated: yes (wood receipts / veg basket / wood signs callback)
- render needs to invent nothing: yes

## Approval Checks

- visual reference pass completed: yes
- big scenes grouped: yes
- cue count fits 32.235s: yes (9 / 3 scenes)
- label readable: yes
- WIT pose files named: yes
- WIT crop safe: yes
- red markup points to exact object: yes
- real-life asset explains not decorates: yes (basket = literal bigger basket)
- title-thumbnail promise paid off: yes (you spend more with BOGO)
- safe for English learners: yes (one clean $5-vs-$10 contrast)
- ready for HyperFrames: yes
