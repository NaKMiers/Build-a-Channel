# Short 02 - You Own Me, But Not Enough To Open Me (vertical)

Composition: `Short02Repair` · 1080×1920 (9:16) · duration `26.6s` (audio `25.515s` + ~1.1s payoff hold)
Port: `localhost:1102`
Source: main video Section 6 (trimmed - drops the policy sentence + the "can you replace the battery / buy the part / local shop" list to fit short length).

## Voiceover
- `voiceover/short-02.mp3` - regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us`.
- `voiceover/short-02-word-timings.json` - whisper-tiny.en; tail ("...please have a future") re-timed monotonically.

## Structure (4 scenes, real photo bases, NO CTA - complete short)
1. **Lock-out** `0–10.82` - repair-bench photo. `HARDER TO FIX THAN REPLACE` kicker, staggered barriers `PART: NOT AVAILABLE` / `SPECIAL TOOL` / `COST ≈ A NEW ONE`. WIT suspicious.
2. **Punchline** `10.82–15.94` - padlock photo. Speech bubble `"YOU OWN ME, BUT NOT ENOUGH TO OPEN ME"` (product speaking) + deadpan `very healthy relationship.` WIT trapped-in-phone.
3. **Definition** `15.94–20.82` - disassembled-phone photo. `REPAIRABILITY = how easy it is to fix` card (the learner phrase). No WIT (calm beat).
4. **Payoff** `20.82–26.6` - phone-on-table photo. Ends on `PLEASE HAVE A FUTURE` card + deadpan WIT. Complete ending, no CTA.

## Rules applied (inherited from S01 review)
- Platform-safe zone `x[60..880] · y[220..1490]`; WIT body may bleed off edges, face stays inside.
- WIT big (≈⅓ frame), face above the centered caption.
- Captions = distinct white-on-translucent-dark subtitle, centered VERTICALLY; punchline/definition/payoff lines carried by the bubble/cards (no duplicate caption, no overlap).
- No CTA - complete standalone short, not a hook/teaser.

## Checks
- `lint`: 0 errors (2 non-blocking warnings: track density, 0–0.2s tween overlap).
- snapshot QA at `5 / 8.5 / 13.5 / 18.5 / 24s`: real photo bases, WIT scale/crop OK, captions centered & clear, bubble + cards land, payoff complete.
- No MP4 export yet (after all 3 shorts approved).
