# Section 1 Visual Plan

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 1: Hook: You're The Rabbit`

Status:
`draft visual plan for approval`

## Section Goal

Land the impossible-sounding claim in the first ~5s (a store can give it FREE and still beat half price), then frame the whole thing as a magic trick the viewer is the victim of — "you are the rabbit." Make the title promise visible fast and set the magic-show motif that pays off in the final beat.

## Source Inputs

- Script: `02-script.md` → Section 1
- Voiceover: `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.82.mp3`
- Script promise: "free" beats "50% off" — a trick, not generosity
- Section duration: `23.019s` (David23 / am_eric / 0.82)

## Narration

```text
Here is something that sounds impossible.
A store can give you a product for free, and still make more money than if it sold it at half price.
Same product. Same shelf. You pay five bucks an item either way.
But one of these signs doubles the store's profit. And, surprise, it is the "free" one.
Yeah. Stores would rather hand you a freebie than knock fifty percent off. That is not generosity. That is a magic trick. And you are the rabbit.
```

## Visual Direction

- Big-scene/cue rhythm: 3 big scenes, 7 cue states (hook standard)
- Big scene rhythm: store (claim) → cash (profit reveal) → magic stage (rabbit payoff)
- Cue-state count: 7
- Main visual metaphor: the store as a stage magician; the shopper as the rabbit pulled from the hat
- WIT emotional path: suspicion → shock/panic → betrayed (the rabbit)
- WIT density: 3 beats, 1 per big scene
- Motion density: mostly hard-show; impact reserved for the FREE sticker, the profit doubling, and the rabbit payoff
- Real-life texture: real store, real cash, real magic hat/curtain
- Real image references: shopping cart (CC0), USD cash (CC0), red curtain (CC0), magic hat (CC BY-SA 3.0)
- Generated/support assets: none
- Viewer attention strategy: open on a flat contradiction ("free earns MORE than half price"), make the two signs visible by ~3s, pay off with the rabbit joke by ~22s
- Retention risk: the store-side claim can feel abstract; fix with concrete signs + a 2-bar profit meter, not narration alone
- Visual fix: show "$5 / item" on BOTH signs and a literal 1-bar vs 2-bar profit doubling
- Red markup: one circle/arrow on the FREE sign as the "surprise" culprit; nothing decorative
- Motion rule: ordinary labels hard-show on beat; impact only on FREE sticker, the doubling, the rabbit reveal

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| A — Store & two signs | 0.0–8.5s | "Here is something..." → "...at half price." | Shopping cart in a store (real photo) | Ground the claim in a real store; present the two competing signs | When voice moves to the per-item price / profit | shopping cart CC0 | `assets/visual-references/section-01-hook/base-a-shopping-cart.jpg` |
| B — The profit reveal | 8.5–17.5s | "Same product..." → "...the 'free' one." | USD cash pile (real photo) | Show same $5 to you, but FREE doubles the store's take | When voice names it "a magic trick" | USD cash CC0 | `.../base-b-cash-usd.jpg` |
| C — Magic trick / rabbit | 17.5–23.019s | "Yeah. Stores would rather..." → "...the rabbit." | Red curtain + black magic top hat (real photos) | Pay off the magic-trick frame; the shopper IS the rabbit | end of section | red curtain CC0 + magic hat CC BY-SA 3.0 | `.../base-c-red-curtain.jpg`, `.../base-c-magic-hat.jpg` |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| A1 | 0.0–3.0 | "...sounds impossible." | A | Cart base in; small handwritten label top-left | cart base | hard-show | `price-tag-suspicion` RIGHT, ~1/3 frame, head+torso in frame | label: "Sounds impossible." | base-a | open on the contradiction, WIT already suspicious |
| A2 | 3.0–8.5 | "for free... than at half price." | A | Two signs hard-show: LEFT card "50% OFF · $5/item", RIGHT giant red "FREE!" sticker "$5/item"; FREE pops | cart base, WIT | impact (FREE sticker pops) | WIT stays RIGHT, suspicious | signs: "50% OFF $5/item" / "FREE! $5/item" | CSS signs | make the two-sign claim visible by ~3s |
| B1 | 8.5–11.5 | "Same product. Same shelf. $5 either way." | B | Cut to cash base; centered strip "Same product · same shelf · $5 each" | cash base | transition + hard-show | (no WIT — breathing beat) | strip label | base-b | establish you pay the same either way |
| B2 | 11.5–15.0 | "one of these signs doubles the store's profit." | B | Profit meter: "50% OFF → +$1" one short bar; "FREE → +$2" two-tall bar grows; ×2 stamp | cash base, profit meter | impact (bar doubles, ×2 stamp) | (no WIT) | meter labels "+$1" / "+$2", "×2" stamp | CSS meter | show the doubling literally, not just spoken |
| B3 | 15.0–17.5 | "surprise, it is the 'free' one." | B | Red circle snaps around the FREE bar; WIT panics | cash base, meter | impact (red circle) | `hidden-fee-panic` LEFT, ~1/2 frame, head+torso in; meter stays RIGHT | red circle on FREE bar | WIT panic | name the culprit; WIT feels it |
| C1 | 17.5–20.0 | "That is not generosity. A magic trick." | C | Cut to red curtain; magic hat lands center-low; "MAGIC TRICK" kinetic headline top | curtain base | transition + impact (headline) | (WIT enters next beat) | headline "NOT GENEROSITY — A MAGIC TRICK" | base-c curtain + hat | flip frame to the magic show |
| C2 | 20.0–23.019 | "And you are the rabbit." | C | Giant WIT rises FROM the hat as the rabbit; payoff headline "YOU ARE THE RABBIT" lands above | curtain + hat | impact (WIT rise + headline stamp) | `betrayed` CENTER, ~1/2 frame, rising from hat, face fully clear, headline ABOVE (not over face) | "YOU ARE THE RABBIT" | base-c + WIT | the punchline; WIT is the emotional subject |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| A1–A2 | 0.0–8.5 | suspicion | `wit-pose-price-tag-suspicion.png` | RIGHT, ~1/3 frame, anchored high (legs may crop) | face/glasses/shoulders fully in; signs cleared to LEFT | the viewer's "wait, what?" at the two signs |
| B3 | 15.0–17.5 | panic | `wit-pose-hidden-fee-panic.png` | LEFT, ~1/2 frame, anchored high | face/glasses/shoulders in; profit meter cleared to RIGHT | the gut-punch when FREE is the winner |
| C2 | 20.0–23.0 | betrayed | `wit-pose-betrayed.png` | CENTER, ~1/2 frame, rising from the hat mouth | face fully clear; headline sits ABOVE the head, never over the face | the rabbit reveal — WIT is the joke |

WIT density note:

- Total WIT beats: 3
- WIT beats per big scene: A=1 (held A1→A2), B=1 (B3), C=1 (C2)
- Any big scene above `2` WIT beats, and why: none
- Cue states intentionally without WIT: B1, B2, C1 (let the signs/meter/headline carry these beats)

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| A1 | 0.0 | "Sounds impossible." | hard-show | top-left, over cart | sets the contradiction tone | no extra labels |
| A2 | 3.0 | "50% OFF · $5/item" / "FREE! · $5/item" | hard-show + FREE pop | two signs | the whole claim in one frame | don't animate both equally — only FREE pops |
| B1 | 8.5 | "Same product · same shelf · $5 each" | hard-show | center strip | you pay the same either way | keep above subtitle zone |
| B2 | 11.5 | "+$1" / "+$2" / "×2" | impact | profit bars | the doubling is the point | no extra numbers |
| B3 | 15.0 | red circle | impact | FREE bar | marks the culprit ("the free one") | no decorative red marks elsewhere |
| C1 | 17.5 | "NOT GENEROSITY — A MAGIC TRICK" | impact | top headline | reframes to the trick | keep clear of where WIT enters |
| C2 | 20.0 | "YOU ARE THE RABBIT" | impact stamp | top headline, above WIT | the punchline | must NOT cover WIT's face |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| Shopping cart | real photo | Wikimedia CC0 | Scene A base | brand/people-free, viewed | `base-a-shopping-cart.jpg` |
| USD cash | real photo | rawpixel CC0 | Scene B base | brand/people-free, viewed | `base-b-cash-usd.jpg` |
| Red curtain | real photo | Wikimedia CC0 | Scene C base | clean, viewed | `base-c-red-curtain.jpg` |
| Magic hat | real photo | Wikimedia CC BY-SA 3.0 | Scene C hero | no face; CREDIT "Magicianidris, CC BY-SA 3.0" | `base-c-magic-hat.jpg` |
| Euro cash | real photo | rawpixel CC0 | fallback money | safe | `alt-cash-euro.jpg` |
| WIT poses | local PNG | shared library | A/B/C reactions | approved channel WIT | `.agents/_shared/assets/wit/poses/` |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| base-a-shopping-cart.jpg | A / A1–A2 | "real store" grounding | 0.0–8.5 | full-frame cover, slight dark scrim for label contrast | persistent base | direct asset |
| base-b-cash-usd.jpg | B / B1–B3 | money / profit context | 8.5–17.5 | full-frame cover, light scrim | persistent base | direct asset |
| base-c-red-curtain.jpg | C / C1–C2 | magic-show backdrop | 17.5–23.0 | full-frame cover | persistent base | direct asset |
| base-c-magic-hat.jpg | C / C1–C2 | the hat WIT emerges from | 17.5–23.0 | center-low, ~440px wide | hero prop; WIT rises from its mouth | direct asset (credit) |
| price-tag-suspicion PNG | A / A1–A2 | suspicion read | 0.0–8.5 | RIGHT ~1/3 | giant WIT | direct asset |
| hidden-fee-panic PNG | B / B3 | panic read | 15.0–17.5 | LEFT ~1/2 | giant WIT | direct asset |
| betrayed PNG | C / C2 | rabbit reveal | 20.0–23.0 | CENTER ~1/2 | giant WIT from hat | direct asset |

## HyperFrames Guidance

- Composition target: `Section01Hook`, 1920x1080, total `23.019s` from the section MP3
- Big scene count: 3
- Cue state count: 7
- Scene components: real photo base (object-fit cover) + light scrim where labels sit + CSS price signs / profit meter / headlines + WIT PNG layer
- Timing notes: timing is `estimated` from the 23.019s audio + marked-script beats (no word-timings JSON). Re-align cue starts after a runtime listen.
- Motion density rule: hard-show for the cart label, "same product" strip, headline text; impact only on the FREE sticker (A2), the bar doubling + ×2 stamp (B2), the red circle (B3), and the rabbit reveal (C2)
- Text style: handwritten labels (channel font); the price signs read like real store tags; headlines bold
- Asset paths: see Visual Resource Usage Map (bases under `assets/visual-references/section-01-hook/`; WIT under shared poses)
- Audio sync notes: WIT enters on the suspicious/“surprise”/“rabbit” words
- WIT pose files: `wit-pose-price-tag-suspicion.png`, `wit-pose-hidden-fee-panic.png`, `wit-pose-betrayed.png`
- WIT density: 3 beats, 1 per scene
- WIT scale and crop guards: A1 ~1/3 RIGHT; B3 ~1/2 LEFT; C2 ~1/2 CENTER. Anchor high (`bottom ≈ -250…-320px`), only legs crop; never crop face/glasses/shoulders. Avoid `money-panic`/`typing-on-laptop` (baked black bg).
- No-WIT breathing beats: B1, B2, C1
- Suggested inspect timestamps: 2.5s, 5.5s, 10s, 13s, 16s, 18.5s, 21.5s
- Suggested screenshot/contact-sheet QA timestamps: 5.5s (two signs readable), 13s (profit doubling), 16s (WIT panic + red circle), 21.5s (rabbit reveal, headline not covering face)
- Suggested MP4 QA frame timestamps: only if export is explicitly requested
- Build risks: cash/cart bases are ~1024px — keep a dark scrim + large overlays so softness reads as styling; magic hat is 565x850, keep it ≤~480px wide; ensure "YOU ARE THE RABBIT" sits above WIT's head
- Must not invent: scene order, base images, the two-sign claim, the profit-doubling device, WIT poses/sides/scale, label text, which beats use impact motion

## Review-Prevention Checklist

- voice sync mapped to phrase cues: yes (each cue cites its trigger phrase)
- big-scene rhythm avoids unrelated rapid boards: yes (3 scenes, grouped)
- cue density stays readable: yes (1–2 changes per cue)
- motion density uses hard-show by default: yes
- impact motion reserved for emphasis: yes (FREE, doubling, circle, rabbit)
- WIT rhythm not overused: yes (3 beats)
- WIT size readable: yes (1/3–1/2)
- WIT crop safe: yes (anchor high, legs only)
- WIT does not cover text/evidence: yes (signs/meter on the opposite side; headline above face)
- red markup targets exact objects: yes (FREE bar only)
- scene bases visually differentiated: yes (store / cash / curtain) — curtain is an intentional magic-frame payoff, not a repeat
- render does not need to invent timing/layout/assets: yes

## Approval Checks

- visual reference pass completed: yes (Openverse + Wikimedia)
- what/when/how clear: yes
- big scenes grouped, not one full scene per sentence: yes
- cue states low enough for section duration: yes (7 / 23s)
- attention reason per big scene / cue state: yes
- label readable: yes
- WIT has a clear job: yes
- WIT pose files named: yes
- WIT facial emotion large enough: yes
- WIT face/head/shoulder crop safe: yes
- WIT density counted and justified: yes
- no-WIT breathing beats planned: yes (B1, B2, C1)
- red markup points to exact object: yes
- ordinary labels hard-show unless emphasis needs impact motion: yes
- impact animation reserved for emphasized spoken beats: yes
- real-life asset explains, not decorates: yes
- title-thumbnail promise still being paid off: yes (FREE > 50% off)
- safe for English learners: yes (short lines, one number pair)
- ready for HyperFrames: yes
