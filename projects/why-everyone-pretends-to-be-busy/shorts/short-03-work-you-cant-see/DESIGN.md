# Short 03 — The Work You Can't See (vertical)

Composition: `Short03Hidden` · 1080×1920 (9:16) · duration `20.4s` (audio `19.072s` + ~1.3s payoff hold)
Port: `localhost:1103`
Source: `why-everyone-pretends-to-be-busy` Section 2 (trimmed).

## Voiceover
- `voiceover/short-03.mp3` — regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us`.
- `voiceover/short-03-word-timings.json` — whisper-tiny.en; tail capped to audio length.

## Structure (4 scenes, real photo bases, NO CTA)
1. **Hook** `0–3.46` — hands typing (the look of work). `THE LOOK OF WORK`. WIT typing.
2. **Thinking = nothing** `3.46–8.56` — lightbulb in darkness. `THINKING = LOOKS LIKE NOTHING`. WIT thinking.
3. **We trust what we see** `8.56–15.12` — office/glass meeting rooms. Staggered `MEETINGS` / `FAST TYPING` / `A SERIOUS FACE`. WIT typing.
4. **Payoff** `15.12–20.4` — lightbulb callback (bookends scene 2). Ends on `REAL WORK HIDES WHERE YOU CAN'T SEE IT` card + deadpan WIT. Complete ending, no CTA.

## Checks
- `lint`: 0 errors. snapshot QA at `1.4 / 6.5 / 11.5 / 17.5s`.
- Caption fix applied (see below): opening caption now renders.
- Rules: safe zone, big WIT (face above caption), centered distinct subtitles, lightbulb bookend metaphor, no CTA.

## Bug fixed during build (also patched S01, S02; recorded in skill memory)
First caption (show time 0.0) never appeared because `opacity:0` and `opacity:1` were set at the SAME time 0 and cancelled. Fix: `const st = Math.max(s, 0.05)` so show != hide-init. NOTE: the already-exported VIDEO-2 shorts (`why-cheap-products`) have this bug in their opening caption and should be re-exported.
