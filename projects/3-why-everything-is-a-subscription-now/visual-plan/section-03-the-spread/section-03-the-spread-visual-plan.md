# Section 3 Visual Plan (built to the Section 1 standing template, 2026-06-23)

Video: `Why Everything Is a Subscription Now`
Section: `Section 3: The Spread: From Apps To Your Car`
Status: `built + previewing on localhost:1003`

## Source Inputs

- Voiceover: `voiceover/section-03-the-spread/scratch-audio/section-03-the-spread-david23-am_eric-0.8.mp3`
- Duration: `54.165s` (TTS `scratch-results.json`)
- Word timings: `voiceover/section-03-the-spread/section-03-word-timings.json` - GENERATED this run via
  transformers.js whisper-tiny.en (none existed). Word starts clean/monotonic; the tail "expired."
  overshoots to 55.42 (whisper chunk glitch) so the composition caps at 54.165 and the gag is pinned to 50.90.

## Narration

```text
It started quietly, with software. The program you used to buy once, in a box, became a monthly plan. Same program. Now it just... holds itself hostage. Stop paying, and it greys out, like, "pay me, or the document gets it."
Then your screens joined the party. Music, movies, shows - you don't own a single song or film. You rent a giant library, and the second you stop paying, the whole thing vanishes. Poof. POV: you own nothing.
And it's never one subscription. It's five. One for shows, one for movies, one for the other shows, one for music, and one for the app that organizes your other apps. Each one is small. Together? Bigger than the old cable bill everyone was running from. We escaped one dungeon and built five smaller ones.
And it didn't stop at screens. Some carmakers have tried putting heated seats - seats already sitting in the car you bought - behind a monthly fee.
Your free trial of a warm bottom has expired.
```

## Visual Direction

- 5 big scenes for 54s (~10s each), one fresh vivid OBJECT base per scene; the model spreads software → screens → many subs → trap → hardware.
- VIVID OBJECT BASES (vary per scene): a laptop on a desk (software) → a real living room with a TV (streaming) → a spread of euro cash (five subscriptions) → a jail corridor of cells (five smaller dungeons) → a modern car interior (heated seats).
- VARIED idea-devices per beat (not cream boxes): a CSS software window that greys out + padlock + a red ransom note; a colorful CSS streaming-tile wall that VANISHES + a "POV: YOU OWN NOTHING" card; five CSS subscription tiles popping one-per-item; a "five subs > OLD CABLE BILL" comparison + "escaped 1 dungeon / built 5 smaller ones"; a CSS heated-seat button + padlock + "$9.99/mo" + an EXPIRED system banner (running-gag callback). Cream label used for 0 asides here (all devices are real-UI/labels).
- GIANT WIT, varied side + pose (4 beats; S3 cash breathes): hidden-fee-panic CENTER-RIGHT (software) → shocked LEFT (vanish) → [no WIT] (five subs) → trapped-by-app-screen CENTER (dungeon) → deadpan-side-eye RIGHT (warm-bottom gag).
- Retention: each scene escalates the spread; the running-gag EXPIRED banner pays off the absurd peak (heated seats).

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Vivid base | Why | Base file |
|---|---:|---|---|---|---|
| BS1 software | 0.0–13.10 | "It started…document gets it." | laptop on a desk (desk grade) | software was the first to flip to monthly + hold itself hostage | base-desk.jpg |
| BS2 streaming | 13.10–24.70 | "Then your screens…you own nothing." | living room + TV (room grade) | music/movies/shows: rent a library that vanishes | base-tv-room.jpg |
| BS3 five subs | 24.70–35.20 | "never one…each one is small." | spread of euro cash (cash grade) | it's never one - five small subscriptions | base-cash.jpg |
| BS4 dungeon | 35.20–41.40 | "Together…five smaller ones." | jail corridor of cells (jail grade) | five subs cost more than cable; "five smaller dungeons" | base-jail.jpg |
| BS5 car | 41.40–54.165 | "didn't stop at screens…warm bottom expired." | modern car interior (car grade) | the model reached hardware: heated seats behind a fee | base-car.jpg |

## Cue State Timeline (pinned to word starts)

| Cue | Time | Voice | Scene | What changes | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0.30 | "It started with software" | BS1 | headline | hard-show | hidden-fee-panic CR @1.0 |
| C2 | 2.60 | "buy once, in a box" | BS1 | software window + green `BUY ONCE` tag | hard-show | - |
| C3 | 4.80 | "became a monthly plan" | BS1 | tag flips to red `$9.99/mo` | impact | - |
| C4 | 8.00 | "holds itself hostage" | BS1 | window GREYS out | hard-show | - |
| C5 | 10.30 | "it greys out" | BS1 | CSS padlock slams on the window | impact | - |
| C6 | 11.30 | "pay me, or the document gets it" | BS1 | red ransom note | impact | - |
| C7 | 13.50 | "music, movies, shows" | BS2 | streaming-tile wall pops in (staggered) | hard-show | - |
| C8 | 16.10 / 18.30 | "don't own a song / rent a giant library" | BS2 | two labels | hard-show | - |
| C9 | 21.80 | "the whole thing vanishes" | BS2 | wall VANISHES; shocked WIT enters | impact | shocked LEFT |
| C10 | 23.70 | "POV: you own nothing" | BS2 | big POV card | impact | shocked holds |
| C11 | 24.70 | "never one. it's five." | BS3 | headline | hard-show | - |
| C12 | 27.60–31.90 | "one for shows/movies/…/music/apps" | BS3 | 5 subscription tiles pop one-per-item | hard-show (staggered) | - |
| C13 | 34.00 | "each one is small" | BS3 | label | hard-show | - |
| C14 | 35.50 | "bigger than the old cable bill" | BS4 | `five subs > OLD CABLE BILL` comparison | impact | trapped CENTER @36.1 |
| C15 | 38.30 / 39.70 | "escaped one dungeon / built five smaller ones" | BS4 | two labels (L + R), trapped WIT | hard-show / impact | trapped holds |
| C16 | 41.60 | "didn't stop at screens" | BS5 | headline | hard-show | - |
| C17 | 45.40 / 46.70 | "heated seats / seats you already bought" | BS5 | heated-seat button + label | impact / hard-show | - |
| C18 | 49.00 | "behind a monthly fee" | BS5 | padlock + `$9.99/mo` over the seat button | impact | - |
| C19 | 50.90 | "free trial of a warm bottom has expired" | BS5 | EXPIRED system banner; deadpan WIT enters (headline hidden) | impact | deadpan-side-eye RIGHT |

## WIT Pose Plan (giant, varied)

| Time | Pose | Side / scale | Why | Note |
|---:|---|---|---|---|
| 1.0–13.1 | wit-pose-hidden-fee-panic.png | CENTER-RIGHT, width 1280, bottom:-320 | software holds itself hostage | verified transparent |
| 21.8–24.7 | wit-pose-shocked.png | LEFT, width 1280, bottom:-320 | the library vanishes | |
| 36.1–41.4 | wit-pose-trapped-by-app-screen.png | CENTER, width 1160, bottom:-320 | five smaller dungeons (the pose's screen-frame doubles as a cell) | |
| 50.9–54.1 | wit-pose-deadpan-side-eye.png | RIGHT, width 1250, bottom:-320 | dry reaction to the warm-bottom gag; also covers the car's head-unit | |

WIT density: 4 beats / 5 scenes; BS3 (five subs) intentionally has no WIT - the 5 tiles + counter carry it.
NOTE: `wit-pose-typing-on-laptop.png` and `wit-pose-money-panic.png` both have a baked BLACK background - do not use on photo scenes.

## Reference And Asset Plan

| Asset | Type | Source / status | Use |
|---|---|---|---|
| base-desk.jpg | real CC0 | safe asset; StockSnap (Openverse) "Top Workspace" - silver laptop, no visible logo | BS1 |
| base-tv-room.jpg | real CC0 | safe asset; rawpixel (Openverse) "Living room modern" - TV in a real room | BS2 |
| base-cash.jpg | real CC0 | safe asset; rawpixel (Openverse) euro banknotes spread | BS3 |
| base-jail.jpg | real CC0 | safe asset; rawpixel (Openverse) jail-cell corridor | BS4 |
| base-car.jpg | real CC0 | mockup target; rawpixel (Openverse) modern car interior - small "Blaupunkt" head-unit logo is covered by the CSS seat panel + the giant WIT | BS5 |
| software window / streaming wall / sub tiles / cost-compare / heated-seat / padlock / EXPIRED banner | self-made CSS | build in render | the idea-devices |
| WIT poses | local PNG | shared manifest | emotion |

All bases sourced via Openverse + viewed before selection. Rejected: branded MacBook/iMac laptops, an MG-logo car with people, a Blaupunkt-only console, sterile cash-on-white - see `reference-board.md`.

## HyperFrames Guidance

- Composition `Section03Spread`, 1920x1080, 54.165s, port 1003.
- Scenes on tracks 1/3/4/5/6 (cross-fades at 13.10/24.70/35.20/41.40); cues on track 2 (cue-d trimmed to 6.18 to avoid the 41.4 float overlap).
- Any smashed element uses explicit left/top. No emoji glyphs (CSS lock/check/warn shapes). EXPIRED banner is a top banner; the headline hides when it takes over.
- Snapshot QA: 6.0 / 11.5 / 18.5 / 23.8 / 29.5 / 37.0 / 40.0 / 47.0 / 52.5.
- Must not invent: scene order/bases, WIT poses/sides, label/device text, cue + stagger timing, motion types.

## Review-Prevention Checklist

- voice sync pinned to generated word starts: yes
- 5 distinct vivid object bases, ~10s each (no static 15s+ base): yes
- varied idea-devices, no repeated cream boxes: yes
- giant WIT, varied side/pose (CR / L / C / R), 4 beats, BS3 breathes: yes
- no text-on-text; EXPIRED banner hides the headline: yes
- impact reserved for flips/slams/vanish/payoff: yes
- car logo covered (seat panel + WIT): yes
