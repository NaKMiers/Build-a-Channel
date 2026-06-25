# Section 2 Visual Plan

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 2: Same To You, Not To Them`

Status:
`draft visual plan for approval`

## Section Goal

Make the store-side math impossible to miss: show the subtraction ON SCREEN, in step with the spoken numbers, so a learner sees "$5 paid − $4 cost = $1 kept" and "$10 − $8 = $2 = DOUBLE." Then land the verdict (same $5 to you, double to the store, sign never moved) and the Wedgwood roast.

## Source Inputs

- Script: `02-script.md` → Section 2 (rev 2.1, math spoken aloud)
- Voiceover: `voiceover/section-02-same-to-you-not-to-them/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-02-same-to-you-not-to-them/section-02-word-timings.json`
- Section duration: `40.469s`

## Narration

```text
Stand behind the counter for a second. Look at the store's side.
A product sells for ten dollars. It costs the store four dollars to make.
Fifty percent off. You pay five. The store spent four to make it. Five minus four — the store keeps one dollar.
Buy one, get one free. You pay ten and take two. Those two cost the store eight to make. Ten minus eight — the store keeps two dollars. Double.
So it is the same five dollars an item for you. But double the profit for the store. And the sign never changed — it still says ten. You paid full price and felt clever doing it.
Oh, and this trick is old. A pottery guy named Wedgwood ran it back in the seventeen hundreds. So no — you are not the first sucker. You are just the latest.
```

## Visual Direction

- Big-scene/cue rhythm: 5 big scenes, ~11 cue beats
- Big scene rhythm: counter (setup) → cash (50% math) → coins (BOGO double) → counter callback (verdict) → Wedgwood (old trick)
- Cue-state count: 11
- Main visual metaphor: the spoken subtraction rendered as an on-screen math card; rising coins = double
- WIT emotional path: thinking → (math, no WIT) → shocked → awkward "felt clever" → defeated
- WIT density: 4 beats across 5 scenes (Scene B is a no-WIT math beat)
- Motion density: hard-show each math line on its spoken number; impact only on "$1"/"$2" results, the DOUBLE stamp, and the Wedgwood sucker ticket
- Real-life texture: real register, real cash, real coins, real Wedgwood jasperware
- Real image references: 4 CC bases (register CC BY, cash CC0, coins CC0, Wedgwood CC0)
- Generated/support assets: none
- Viewer attention strategy: the math is the retention risk and the payoff — reveal it one number at a time, exactly as spoken
- Retention risk: number overload / confusion (the very thing the script rewrite fixed)
- Visual fix: one subtraction card per deal, each line appearing on its word; the result ($1 / $2) lands as an impact
- Red markup: a red box/underline on the result number and the DOUBLE stamp only
- Motion rule: hard-show math lines; impact for results + DOUBLE + sucker ticket

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path |
|---|---:|---|---|---|---|---|---|
| A — Behind the counter | 0.0–7.48 | "Stand behind the counter… $10 sells… $4 to make." | Vintage cash register | put us on the store's side; set $10 sell / $4 cost | at "Fifty percent off" | register CC BY | `base-a-counter-register.jpg` |
| B — 50% off math | 7.48–13.86 | "Fifty percent off… five minus four… keeps one dollar." | USD cash pile | show $5 − $4 = $1 | at "Buy one, get one free" | cash CC0 | `base-b-cash-usd.jpg` |
| C — BOGO doubling | 13.86–22.72 | "Buy one get one free… ten minus eight… two dollars. Double." | Rising coin stacks | show $10 − $8 = $2 = DOUBLE | at "So it is the same five dollars" | coins CC0 | `base-c-coins-rising.jpg` |
| D — The verdict / unchanged sign | 22.72–32.08 | "same five for you… double for the store… sign never changed… felt clever." | Cash register (callback) | same $5 to you vs 2× to store; $10 sign never moved | at "this trick is old" | register CC BY (callback) | `base-a-counter-register.jpg` (`reg2` grade) |
| E — Wedgwood / old trick | 32.08–40.469 | "this trick is old… Wedgwood… seventeen hundreds… just the latest." | Wedgwood blue jasperware | the trick is ~250 years old; you're just the latest sucker | end | Wedgwood CC0 | `base-e-wedgwood.jpg` |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes | What Stays | Motion | WIT Pose / Size / Crop | Label / Markup | Why |
|---|---:|---|---|---|---|---|---|---|---|
| A1 | 0.30 | "Stand behind the counter" | A | "the STORE's side" hand label | register | hard-show | `thinking` RIGHT ~1/3, legs crop only | "the store's side" | put us behind the counter |
| A2 | 4.46 | "$10" (sells) | A | green "SELLS $10" tag | register | hard-show | thinking | "SELLS $10" | the price |
| A3 | 6.06 | "$4 to make" | A | gray "COSTS $4 to make" tag | register | hard-show | thinking | "COSTS $4" | the cost |
| B1 | 7.62 | "Fifty percent off" | B | math card header "50% OFF" + cut to cash | — | transition + hard-show | (no WIT) | "50% OFF" | open deal 1 |
| B2 | 8.66 | "you pay five" | B | line "You pay $5" | card | hard-show | — | "You pay $5" | first number |
| B3 | 9.88 | "spent four to make" | B | line "− Cost $4" | card | hard-show | — | "− Cost $4" | subtract cost |
| B4 | 12.62 | "keeps one dollar" | B | result "= keeps $1" + red box | card | impact | — | "= $1" red box | the result lands |
| C1 | 13.90 | "Buy one, get one free" | C | math card header "BUY 1 GET 1 FREE" + cut to coins | — | transition + hard-show | (no WIT) | "BUY 1 GET 1 FREE" | open deal 2 |
| C2 | 15.38 | "you pay ten and take two" | C | line "You pay $10 (for 2)" | card | hard-show | — | "You pay $10" | first number |
| C3 | 17.08 | "cost the store eight" | C | line "− Cost $8" | card | hard-show | — | "− Cost $8" | subtract cost |
| C4 | 20.52 | "keeps two dollars" | C | result "= keeps $2" + red box | card, coins | impact | — | "= $2" red box | result lands |
| C5 | 21.94 | "Double." | C | "DOUBLE" stamp over rising coins | coins | impact | `shocked` CENTER ~1/2 | "DOUBLE" stamp | the punch; WIT reacts |
| D1 | 23.28 | "same five dollars… for you" | D | split card: "YOU: $5 / item" | register | transition + hard-show | (WIT enters D3) | "YOU: $5/item" | your side unchanged |
| D2 | 25.24 | "double the profit for the store" | D | "STORE: 2× profit" half + arrow | split card | hard-show | — | "STORE: 2× profit" | store's side doubled |
| D3 | 27.24 | "the sign never changed… still says ten" | D | big "$10" price tag stamps, "never moved" | split card | impact | — | "$10 — never moved" | anchor: price never drops |
| D4 | 30.70 | "felt clever doing it" | D | WIT awkward-celebration | register | hard-show | `awkward-celebration` LEFT ~1/2 | — | the dry joke on the shopper |
| E1 | 32.42 | "this trick is old" | E | cut to Wedgwood; "≈ 250 years old" | jasperware | transition + hard-show | (WIT enters E3) | "≈ 250 years old" | reframe to history |
| E2 | 34.42 | "Wedgwood… seventeen hundreds" | E | "Josiah Wedgwood · 1700s" caption | jasperware | hard-show | — | "Wedgwood · 1700s" | name the originator |
| E3 | 38.32 | "not the first sucker… just the latest" | E | "SUCKER #—— you're just the latest" ticket | jasperware | impact | `facepalm` RIGHT ~1/2 | sucker ticket | the roast button |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop | Why |
|---|---:|---|---|---|---|---|
| A | 0.30–7.48 | thinking | `wit-pose-thinking.png` | RIGHT ~1/3, anchored high | face/glasses/shoulders in; legs crop | calm "let's do the store's math" |
| C5 | 21.94 | shocked | `wit-pose-shocked.png` | CENTER ~1/2 | face fully clear; math card cleared to upper-left | reacts to "Double" |
| D4 | 30.70 | awkward-celebration | `wit-pose-awkward-celebration.png` | LEFT ~1/2 | face clear; split card cleared RIGHT | "felt clever" while being fooled |
| E3 | 38.32 | facepalm | `wit-pose-facepalm.png` | RIGHT ~1/2 | face clear; ticket cleared LEFT | "just the latest sucker" |

WIT density note:

- Total WIT beats: 4
- Per big scene: A=1, B=0, C=1, D=1, E=1
- Above 2 in any scene: no
- Intentional no-WIT beats: all of Scene B and the math-reveal cues in C/D (let the numbers carry it)

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion | Target | Why | Avoid |
|---|---:|---|---|---|---|---|
| B4 | 12.62 | red box on "$1" | impact | the result number | the kept profit lands | no marks on the setup lines |
| C4 | 20.52 | red box on "$2" | impact | the result number | the doubled profit lands | — |
| C5 | 21.94 | "DOUBLE" stamp | impact | over coins | the punch | — |
| D3 | 27.24 | "$10 never moved" | impact | the price tag | anchoring: price never drops | — |
| E3 | 38.32 | sucker ticket | impact | over jasperware | the roast | keep off WIT face |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Path |
|---|---|---|---|---|---|
| Cash register | real photo | Wikimedia CC BY 2.0 | A + D base | credit "Old cash register, CC BY 2.0" | `base-a-counter-register.jpg` |
| USD cash | real photo | rawpixel CC0 | B base | safe | `base-b-cash-usd.jpg` |
| Rising coins | real photo | Wikimedia CC0 | C base | safe | `base-c-coins-rising.jpg` |
| Wedgwood jasperware | real photo | Wikimedia CC0 | E base | safe | `base-e-wedgwood.jpg` |
| WIT poses | local PNG | shared library | A/C/D/E | approved | shared poses |

## HyperFrames Guidance

- Composition target: `Section02Counter`, 1920x1080, total `40.469s`
- Big scene count: 5 (register / cash / coins / register-callback / Wedgwood)
- Cue state count: 11 beats (some with staggered sub-reveals on each spoken number)
- Scene components: real photo base (object-fit cover) + scrim + CSS math card (one subtraction per deal) + CSS tags/stamps + WIT layer
- Timing notes: pinned to `section-02-word-timings.json` (real word starts cited in the cue table). Final word "latest" tail-glitched in the JSON → use ~40.0s.
- Motion density: hard-show every math line on its number; impact for the $1/$2 results, DOUBLE, $10-never-moved, sucker ticket
- Text style: math card in bold Segoe (numbers must read instantly); handwritten asides in PatrickHandLocal
- WIT pose files: thinking, shocked, awkward-celebration, facepalm
- WIT density: 4 beats; Scene B has none
- WIT scale/crop: ~1/3 (A) to ~1/2 (C/D/E), anchored high, legs-only crop; math card/labels always cleared to the side WIT is not on
- No-WIT breathing beats: B1–B4, C2–C4, D1–D3, E1–E2
- Suggested inspect timestamps: 3.0, 6.5, 9.0, 12.8, 16.0, 19.5, 22.0, 26.0, 28.5, 35.0, 39.0
- Suggested screenshot QA timestamps: 6.5 (sells/cost tags), 12.9 ($1 result), 21.0 ($2 result), 22.3 (DOUBLE + shocked WIT), 29.6 ($10 never moved), 31.2 (felt-clever WIT), 39.0 (Wedgwood + sucker)
- Build risks: keep numbers large/high-contrast; do not let the math card cover WIT; coins base is bright (dark grade); register reused for D must be graded cooler to read as a callback not a repeat
- Must not invent: scene order, the subtraction reveals + their word timings, base images, WIT poses/sides, label text, which beats use impact

## Review-Prevention Checklist

- voice sync mapped to phrase cues: yes (word-timings cited per cue)
- big-scene rhythm avoids unrelated rapid boards: yes (5 scenes, ~6–9s each)
- cue density readable: yes (one math line per beat)
- motion density hard-show default: yes
- impact reserved for results/DOUBLE/ticket: yes
- WIT rhythm not overused: yes (4 beats, Scene B none)
- WIT size readable: yes
- WIT crop safe: yes
- WIT vs text both ways: yes (card cleared opposite WIT)
- red markup targets exact object: yes (result numbers only)
- scene bases differentiated: yes (register/cash/coins/Wedgwood; register reused only as a non-consecutive callback)
- render needs to invent nothing: yes

## Approval Checks

- visual reference pass completed: yes
- what/when/how clear: yes
- big scenes grouped, not one scene per sentence: yes
- cue count fits 40.469s: yes (11 beats / 5 scenes)
- attention reason per cue: yes
- label readable: yes
- WIT has a clear job: yes
- WIT pose files named: yes
- WIT facial emotion large enough: yes
- WIT crop safe: yes
- WIT density counted: yes
- no-WIT breathing beats planned: yes
- red markup points to exact object: yes
- ordinary labels hard-show: yes
- impact reserved for emphasis: yes
- real-life asset explains not decorates: yes (real Wedgwood = the named maker)
- title-thumbnail promise paid off: yes (store-side math behind the same price)
- safe for English learners: yes (subtraction spoken AND shown, one number at a time)
- ready for HyperFrames: yes
