# Short 01 — Busy Is Not An Emotion (vertical)

Composition: `Short01Busy` · 1080×1920 (9:16) · duration `24.9s` (audio `23.68s` + ~1.2s payoff hold)
Port: `localhost:1101`
Source: `why-everyone-pretends-to-be-busy` Section 3 (trimmed).

## Voiceover
- `voiceover/short-01.mp3` — regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us`.
- `voiceover/short-01-word-timings.json` — whisper-tiny.en; tail ("...proving you're near the work") re-timed monotonically.

## Structure (4 scenes, real photo bases, NO CTA — complete short)
1. **Hook** `0–5.88` — busy-desk photo. `"I'M SO BUSY"` kicker + `= NOTICE I'M IMPORTANT`. WIT talking-front.
2. **Not an emotion** `5.88–10.6` — laptop-on-concrete (negative space). `BUSY ≠ AN EMOTION` card. WIT deadpan-side-eye.
3. **Status / fill the day** `10.6–18.64` — gold-trophy photo (busy = status). `SOUNDS RESPONSIBLE` / `SOUNDS NEEDED` / `MEETINGS ABOUT MEETINGS`. WIT awkward-celebration.
4. **Payoff** `18.64–24.9` — empty conference-room photo. Ends on `PROVING YOU'RE NEAR THE WORK` card + tiny-defeated WIT. Complete ending, no CTA.

## Rules applied
- Platform-safe zone `x[60..880] · y[220..1490]`; WIT body bleeds off edges, face inside.
- WIT big (≈⅓ frame), face above the centered caption.
- Captions = distinct white-on-translucent-dark subtitle, centered VERTICALLY; "not an emotion" + "proving you're near the work" carried by the cards (no duplicate caption, timed to clear before each card pops).
- No CTA.

## Checks
- `lint`: 0 errors (2 non-blocking warnings).
- snapshot QA at `4.5 / 9.6 / 13 / 16 / 22s`: real bases, WIT scale/crop OK, captions centered & clear, trophy + conference-room metaphors land, payoff complete.
- No MP4 export yet (after all 3 shorts approved).
