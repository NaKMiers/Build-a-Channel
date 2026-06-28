# Short 01 - "You're The Rabbit" (DESIGN)

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Type: vertical short (1080x1920), native portrait rebuild
Source: Section 1 (hook) + one compressed Section 2 math beat
Composition id: `Short01` · Port: `1101`
Status: `built, ready for review`

## Spec compliance

- Native 1080x1920 rebuild (not a crop). Root `data-duration="19.5"` (VO 18.155s + ~1.3s payoff hold).
- COMPLETE standalone short - **NO CTA**. Ends on the "YOU'RE THE RABBIT" payoff hold.
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed overlay (since removed): all cards, captions, and the WIT face sit inside; WIT body fills down toward the bottom.
- WIT big (~980px square box, ~half frame), face ~y750 ABOVE the centered caption (y960); `transform-origin:center bottom`. Approved pose PNGs only.
- Captions = distinct subtitle style (white on `rgba(16,12,9,0.5)` pill, centered vertically). Payoff lines carried by cards, not duplicated; captions clear before each card pops.
- Real photo base per scene + top/bottom scrims; bases kept bright.

## Scenes / beats (word-pinned to short-01-word-timings.json)

Beat logic mirrors the source Section 1: the **magic-hat scene lands on the word "magic,"** and **WIT sprouts CSS bunny ears on the word "rabbit"** (same device as the long-form S1).

| Scene | Base | t | Hero card(s) | WIT | Captions |
|---|---|--:|---|---|---|
| A | greengrocer store | 0.0 | "FREE vs ½ OFF?" | price-tag-suspicion | "Sounds impossible…" (0.36) · "Free - and earns MORE" (3.36) · "than half price" (5.18) |
| B | profit-coins | 6.52 | "SAME $5 / item" → "…but FREE doubles the store's profit" (10.66) → math: "50% off: keeps $1" (12.02) · "FREE: keeps $2" (13.70) · "DOUBLE" stamp (14.66) | shocked | (none - cards carry the math) |
| C | magic-hat | 14.94 | "A MAGIC TRICK" (16.52, on the word "magic") | betrayed, emerging from the hat | "That's not generosity" (14.96, clears 16.40) |
| D | red-curtain | 17.45 | "YOU'RE THE RABBIT" (17.84, holds) | betrayed + **bunny ears pop on "rabbit"** (17.84) | (none - card carries the payoff) |

The betrayed WIT spans scenes C+D in one `.witwrap` (so the ears sprout on the same continuous figure = "you ARE the rabbit"). Bunny ears are CSS (`.ear.left/.right`), ported from the long-form S1.

## Assets reused (from Section 1 library)

- photos: `store.jpg` (greengrocer), `profit-coins.jpg`, `magic-hat.jpg`, `red-curtain.jpg`
- WIT: `price-tag-suspicion`, `shocked`, `betrayed` (2048×2048)
- font: `patrick-hand-latin.woff2`

## Voiceover

- `voiceover/short-01.mp3` - am_eric / 0.84 / en-us, 18.155s. Input: `tts-inputs/short-01.txt`.
- `voiceover/short-01-word-timings.json` - whisper-tiny.en; final word "rabbit." tail re-timed 19.88 → 18.15 (monotonic to audio end).

## Checks

- lint: 0 errors, 1 advisory (`overlapping_gsap_tweens` 0–0.42s on pop fromTo - cosmetic).
- validate: 0 console errors, 10 text elements pass WCAG AA.
- snapshot QA: `snapshots/contact-sheet.jpg` at 1.0/4.0/7.0/12.6/14.8/17.9 - WIT big & face above caption, cards spaced, captions distinct, payoff holds, no CTA. Safe-guide overlay verified then removed (0 refs remain).

## Notes

- Emoji avoided (snapshot Chromium); the rabbit gag is carried by the CSS bunny ears + "YOU'RE THE RABBIT" text card.
- Short resolves the hook internally (the double-profit math) so it stands alone rather than teasing the long video.
- 2026-06-24 remake (owner feedback): original v1 opened on the magic hat for "sounds impossible" and used a flat rabbit card. Owner: "show scene of magic when voice says magic, show rabbit ears when voice says rabbit, as the origin video." Rebuilt to 4 scenes with the magic-hat scene synced to "magic" and CSS bunny ears sprouting on "rabbit" - matching the long-form S1 beat logic.
