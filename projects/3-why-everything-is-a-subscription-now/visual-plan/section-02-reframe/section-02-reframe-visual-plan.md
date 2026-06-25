# Section 2 Visual Plan (REMADE 2026-06-23 — to the Section 1 standing template)

Video:
`Why Everything Is a Subscription Now`

Section:
`Section 2: Reframe: You Stopped Buying, You Started Renting`

Status:
`remade to S1 template + review fixes applied (2026-06-23) — built + previewing on localhost:1002`

## Review fixes (2026-06-23, round 2)

Owner review of the remake asked for three things, all applied:
1. BS1 background "not suitable" → replaced the aurora night-phone with `base-apps-phone.jpg` (hands on a
   phone full of glowing app icons — clearly on-topic: the apps are the subscriptions).
2. "Some texts cover other texts" → BS3 `OWN`(struck) and `RENT` are now stacked vertically (no
   text-on-text); BS5 the 4 RENT tags are HIDDEN when the `RENT — NOT OWN` payoff lands, so nothing overlaps it.
3. "WIT too small / make it giant" → all 4 WIT beats enlarged to width ~1200–1300 (≈1/2+ frame), anchored
   high (head+torso in frame, only legs cropped), with labels re-arranged to the side WIT is not using.

## Why remade

The owner asked to remake Section 2 completely, based on the approved Section 1. The previous build
broke the standing vivid-hook template in exactly the ways Section 1 was rejected for:

- ONE base photo (night-phone) reused across 4 scenes with only colour grades — reads as a repeated frame
- repeated handwritten CREAM LABEL BOXES carrying nearly every idea (the rejected "boring, repetitive" device)
- WIT small (~880–940px), full-body, parked low with text always on the opposite side

This remake applies `vivid on-topic OBJECT photo bases -> VARIED CSS idea-devices per beat -> giant WIT
that VARIES per scene`.

## Source Inputs

- Voiceover: `voiceover/section-02-reframe/scratch-audio/section-02-reframe-david23-am_eric-0.8.mp3`
  copied to `section-previews/section-02-reframe/section-02-reframe-david23-am_eric-0.8.mp3`
- Authoritative duration: `37.909s` (TTS `scratch-results.json`). The `section-02-word-timings.json`
  tail overshoots to 39.16s (whisper-tiny chunk-boundary glitch); word STARTS are clean and used; the
  final payoff is pinned to ~36.26 and the composition ends at 37.909.
- Word timings: `voiceover/section-02-reframe/section-02-word-timings.json`

## Narration

```text
Now — this is not a video about how subscriptions are evil and you should throw your phone in a lake. Some are genuinely useful. Calm down.
This is about something weirder.
We used to own things. You paid once, the thing was yours, the end. A beautiful, boring transaction.
A subscription is different. You don't buy the thing. You rent access to it. Pay every month, the screen turns on. Miss a payment, and your own device does this — a little padlock appears, and it looks at you like a disappointed parent.
So here's the real question. How did almost everything — your apps, your shows, your software, even buttons inside your car — quietly turn into stuff you rent instead of stuff you own?
```

## Visual Direction

- 5 big scenes, ~10 cue states for 37.9s; one fresh vivid object base per scene
- VIVID OBJECT BASES (vary per scene): glowing phone (defuse) -> crate of vinyl records (own) ->
  glowing phone w/ paywall (rent) -> a real padlock (lock) -> a flat-lay of devices (the question)
  - the phone returns in BS3 as a deliberate, non-consecutive device callback — the script's own
    "one device shown two ways" motif (OWN -> RENT -> locked). Vinyl sits between BS1 and BS3, and
    BS3 is heavily re-dressed (cool grade + paywall card + RENT stamp), so it does not read as a repeat.
- VARIED idea-devices per beat (NOT a repeated cream box): struck-through "ANTI-SUBSCRIPTION RANT"
  banner + green-check app tiles (defuse); green OWN stamp + a paper receipt card (own); a real-UI
  subscription PAYWALL card + OWN->RENT stamp swap + a "screen ON" toggle (rent); a red MISS A PAYMENT
  system banner + a CSS lock-screen card (lock); a kinetic headline + RENT tags + a kinetic payoff (question).
  The handwritten cream label is reserved for two short asides only.
- GIANT WIT, varied per scene in side + scale + pose: facepalm RIGHT (defuse) -> thinking LEFT (own)
  -> [no WIT, the stamp swap carries it] (rent) -> betrayed CENTER, giant, the peak (lock) ->
  suspicious RIGHT (question). 4 WIT beats, <=1 per scene, BS3 breathes.
- Viewer attention strategy: a fair, funny defuse ("calm down"), then one strong transformation
  (OWN -> RENT -> locked device), then the open question the rest of the video answers.
- Retention risk: reading as an anti-subscription rant. Fix: the struck "RANT" banner + "some are
  useful" land the defuse; the lock is the SYSTEM acting on WIT, never preaching.
- Motion density: hard-show by default; impact only on the OWN stamp, the OWN->RENT swap, the betrayed
  WIT entrance ("a little padlock appears"), and the closing payoff.

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base (vivid object) | Why This Scene | Cut When | Base file |
|---|---:|---|---|---|---|---|
| BS1 defuse | 0.0–9.30 | "Now…something weirder" | hands on a phone full of app icons (apps grade) | disarm the "evil" reaction; the phone full of apps = the subscriptions | "We used to own things" | base-apps-phone.jpg |
| BS2 OWN | 9.30–14.80 | "We used to own things…boring transaction" | crate of vinyl records (warm) | the old world: physical things you paid once for and kept | "A subscription is different" | base-vinyl.jpg |
| BS3 RENT | 14.80–20.52 | "A subscription is different…screen turns on" | glowing phone (cool grade) + CSS paywall | the reframe: you rent access, not own — same device, now rented | "Miss a payment" | base-phone-rent.jpg |
| BS4 LOCK | 20.52–27.44 | "Miss a payment…disappointed parent" | a real padlock on a metal gate (dark) | the device locks; emotional peak | "So here's the real question" | base-padlock.jpg |
| BS5 question | 27.44–37.909 | "the real question…stuff you own?" | flat-lay of devices on wood (empty right) | land the question across every device | end | base-devices-flatlay.jpg |

## Cue State Timeline (pinned to word-timings; starts are clean)

| Cue | Time | Voice Cue | Scene | What changes | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0.40 | "this is not a video…subscriptions are evil" | BS1 | "AN ANTI-SUBSCRIPTION RANT" banner appears, then a red strike crosses it out @1.0 | hard-show + impact (strike) | — |
| C2 | 3.62 | "throw your phone in a lake" | BS1 | WIT facepalm RIGHT; cream aside `(don't throw it in a lake)` @4.04 | hard-show | facepalm R, big |
| C3 | 5.32 | "Some are genuinely useful. Calm down." | BS1 | green `SOME ARE GENUINELY USEFUL` + 3 app tiles, 2 with green ✓ badges | hard-show | facepalm holds |
| C4 | 9.30 | "We used to own things" | BS2 | cut to vinyl; `WE USED TO OWN THINGS` headline (right); WIT thinking LEFT | transition + hard-show | thinking L |
| C5 | 10.78 | "You paid once, the thing was yours" | BS2 | green `OWN` stamp SLAMS on the records; receipt card `PAID ONCE ✓ / YOURS — FOREVER` | impact (stamp) | thinking holds |
| C6 | 13.00 | "A beautiful, boring transaction" | BS2 | cream aside `a beautiful, boring transaction` | hard-show | — |
| C7 | 14.80 | "A subscription is different" | BS3 | cut to phone (cool); `A SUBSCRIPTION IS DIFFERENT` headline | transition + hard-show | — |
| C8 | 16.16→16.46 | "You don't buy the thing. You rent access" | BS3 | real-UI paywall card on the phone (`Subscribe · $9.99/mo`); small faded `OWN` stamp | hard-show | — |
| C9 | 17.24 | "rent" | BS3 | red `RENT` stamp SLAMS over `OWN` + red strike crosses OWN | impact (swap) | — |
| C10 | 18.40 | "Pay every month, the screen turns on" | BS3 | `PAY MONTHLY → SCREEN ON` toggle indicator (green) | hard-show | — |
| C11 | 20.52 | "Miss a payment" | BS4 | cut to padlock; red `MISS A PAYMENT` top banner; lock-screen card builds @22.92 | transition + hard-show | — |
| C12 | 23.44 | "a little padlock appears" | BS4 | giant betrayed WIT SMASHES in (center); `LOCKED` pops on the lock-screen card | impact | betrayed CENTER, giant |
| C13 | 26.40 | "like a disappointed parent" | BS4 | cream aside `…like a disappointed parent` (upper-left, clear of WIT) | hard-show | betrayed holds |
| C14 | 27.44 | "So here's the real question" | BS5 | cut to flat-lay; `SO… HOW DID EVERYTHING` headline; WIT suspicious RIGHT | transition + hard-show | suspicious R |
| C15 | 31.04 / 31.58 / 32.24 / 33.26 | "your apps / your shows / your software / buttons inside your car" | BS5 | a red `RENT` tag pops on each device, one per spoken item (staggered) | hard-show (staggered) | suspicious holds |
| C16 | 36.26 | "rent instead of stuff you own" | BS5 | kinetic payoff `RENT — NOT OWN` | impact | suspicious holds |

## WIT Pose Plan (BIG + HIGH, varied per scene)

| Cue | Time | Emotion | Pose File | Side / Scale / Anchor | Cleared zone for content | Why |
|---|---:|---|---|---|---|---|
| C2–C3 | 3.62–9.30 | exasperated | wit-pose-facepalm.png | RIGHT, giant, width 1300, right:-180, bottom:-320 | banner/labels/tiles on LEFT third | "calm down, don't throw your phone" |
| C4–C6 | 9.45–14.80 | reflective | wit-pose-thinking.png | LEFT, giant, width 1300, left:-260, bottom:-320 | headline/receipt/stamp on RIGHT | "we used to own things" |
| C12–C13 | 23.44–27.44 | betrayed | wit-pose-betrayed.png | CENTER, giant, width 1200, left:400, bottom:-320 | banner TOP; lock card + aside on far-LEFT | the device locks on you — the peak |
| C14–C16 | 27.64–37.9 | suspicious | wit-pose-suspicious.png | RIGHT (empty wood), giant, width 1300, right:-200, bottom:-320 | headline/tags/payoff LEFT + center | "the real question" |

WIT density note: 4 beats across 5 scenes, <=1 per scene; BS3 (RENT) intentionally has NO WIT — the
OWN->RENT stamp swap + paywall carry it. `wit-pose-money-panic.png` avoided (baked black bg).

## Markup And Label Plan

- C1 red diagonal STRIKE crosses out the "ANTI-SUBSCRIPTION RANT" banner — the only red mark in BS1, and it means "this is NOT that video."
- C5 green `OWN` stamp on the vinyl; C9 a red `RENT` stamp + strike crosses `OWN` — the stamps ARE the reframe, not decoration.
- C12 the CSS lock-screen card / `LOCKED` is the device acting (the padlock), not a decorative circle.
- C15 each `RENT` tag points at a specific device on the flat-lay as the voice names it.
- Payoff `RENT — NOT OWN` and the BS4 asides are kept clear of WIT's face and lifted out of the subtitle zone.

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Saved Path |
|---|---|---|---|---|
| base-night-phone.jpg | real CC0 | safe asset | BS1 defuse (normal grade) | assets/visual-references/section-02-reframe/base-night-phone.jpg |
| base-phone-rent.jpg | real CC0 (copy of phone) | safe asset | BS3 rent (cool grade) — separate filename avoids duplicate-media lint | …/base-phone-rent.jpg |
| base-vinyl.jpg | real CC0 | safe asset | BS2 own (warm) | …/base-vinyl.jpg |
| base-padlock.jpg | real CC0 | safe asset | BS4 lock (dark) | …/base-padlock.jpg |
| base-devices-flatlay.jpg | real CC0 | safe asset | BS5 question | …/base-devices-flatlay.jpg |
| paywall card / OWN-RENT stamps / receipt / lock-screen card / RENT tags / app tiles / payoff | self-made CSS | build in render (adapt S1 kit) | the reframe idea-devices | render CSS |
| WIT poses (facepalm, thinking, betrayed, suspicious) | local PNG | shared manifest | emotion | assets/wit/ |

All bases sourced via Openverse and VIEWED before selection; brand-free, people-free. Rejected:
two laptop/code photos (Apple logos + a person), a Master-Lock branded combination-lock photo, a
sterile vinyl-on-white stack. See `reference-board.md` + `ATTRIBUTION.md`.

## HyperFrames Guidance

- Composition: `Section02Reframe`, 1920x1080, duration `37.909s`, port `1002`
- Scene cuts (cross-fades, word-pinned): 9.30, 14.80, 20.52, 27.44
- Scenes on separate tracks (1,3,4,5,6) for cross-fade overlap; cues sequential on track 2
- Any element you SMASH/scale (OWN stamp, RENT stamp, betrayed WIT, payoff) must be positioned with
  explicit `left`/`top` — GSAP scale drops a percentage `translateX(-50%)`
- A full-screen "system" feel (MISS A PAYMENT) is a TOP BANNER above WIT z
- No emoji glyphs — the padlock/lock icon is a CSS shape (reuse S1 `.lockicon`)
- Pin every reveal to the word starts above; staggered RENT tags at 31.04 / 31.58 / 32.24 / 33.26
- Suggested snapshot QA: 1.4 (struck banner), 6.0 (useful+facepalm), 11.6 (OWN stamp), 18.6 (RENT swap),
  23.8 (betrayed smash + LOCKED, just AFTER the 23.44 impact), 33.6 (RENT tags), 36.8 (payoff)
- Must not invent: scene order/grades, base images, WIT poses/sides, label/stamp text, cue/stagger timing, motion types

## Review-Prevention Checklist

- voice sync pinned to word starts: yes
- vivid distinct object base per scene (no base reused on adjacent scenes; phone is a non-consecutive callback): yes
- varied idea-devices, not repeated cream boxes (cream used for 2 asides only): yes
- giant WIT, varied side/scale/pose (R / L / center / R): yes
- WIT/text collisions cleared (content moved to the side WIT is not using): yes
- impact reserved for stamps, betrayed entrance, payoff: yes
- subtitle-safe lower margin: yes
- markup means something (strike, stamps, lock, RENT tags): yes
