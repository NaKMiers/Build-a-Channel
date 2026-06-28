# Short 03 - A Subscription With Extra Steps (vertical)

Composition: `Short03Sub` · 1080×1920 (9:16) · duration `21.4s` (audio `20.203s` + ~1.2s payoff hold)
Port: `localhost:1103`
Source: main video Section 7 (re-ordered so the landfill joke is the cold open).

## Voiceover
- `voiceover/short-03.mp3` - regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us`.
- `voiceover/short-03-word-timings.json` - whisper-tiny.en; tail capped to audio length.

## Structure (4 scenes, real photo bases, NO CTA - complete short)
1. **Landfill hook** `0–4.82` - e-waste pile photo (has a real "ALL TRASH" arrow). Caption = the landfill joke. WIT facepalm (reluctant).
2. **The system** `4.82–12.3` - fulfillment-boxes photo. Staggered barriers `REPAIR QUOTE: HIGH` / `SPARE PART: MISSING` / `NEW ONE: TOMORROW`.
3. **Receipt loop** `12.3–16.54` - cherry-wood checkout photo. `PRICE TAG: SMILES AGAIN` / `RECEIPT: PRINTS AGAIN`. WIT holding a long receipt.
4. **Payoff** `16.54–21.4` - e-waste pile callback (dimmed; bookends the hook). Ends on `A SUBSCRIPTION WITH EXTRA STEPS` card + deadpan WIT. Complete ending, no CTA.

## Rules applied (inherited from S01/S02 review)
- Platform-safe zone `x[60..880] · y[220..1490]`; WIT body may bleed off edges, face stays inside.
- WIT big (≈⅓ frame), face above the centered caption.
- Captions = distinct white-on-translucent-dark subtitle, centered VERTICALLY; barriers/loop carried by labels, payoff carried by the card (no duplication, no overlap).
- No CTA - complete standalone short, not a hook/teaser.

## Checks
- `lint`: 0 errors (3 non-blocking warnings: track density, 0–0.2s tween overlaps).
- snapshot QA at `3 / 11 / 15 / 19s`: real photo bases, WIT scale/crop OK, captions centered & clear, barriers staggered, payoff bookend complete.
- Open note: scene-3 cherry-wood base is plainer than the others; the receipt-holding WIT carries it. Swap if owner wants a busier base.
- No MP4 export yet (after all 3 shorts approved).
