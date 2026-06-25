# Short 01 — The $9 Chair (vertical)

Composition: `Short01Chair` · 1080×1920 (9:16) · duration `28.4s` (audio `26.901s` + ~1.5s CTA hold)
Port: `localhost:1101`
Source: main video Section 1 (body) + condensed Section 8 (button).

## Voiceover
- `voiceover/short-01.mp3` — regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us` (`hyperframes tts`).
- `voiceover/short-01-word-timings.json` — whisper-tiny.en word timings; tail (button line) re-timed monotonically by hand (chunk-boundary glitch).

## Structure (4 big scenes + button, all on real photo bases)
1. **Setup** `0–7.74` — `chair-price-tag` photo. Kicker `$9 CHAIR`, joke `CONFIDENCE: EXPENSIVE`, `FIRST WEEK ✓ FINE`. WIT thinking (curious).
2. **Failure** `7.74–14.12` — `wobbly-leg-loose-screw` photo (real loose screw = evidence). `A NOISE LIKE LEGAL ADVICE`, `SCREW: LOOSE` + arrow, `EXPLORING CAREER OPTIONS`. WIT shocked.
3. **Reveal** `14.12–20.04` — `hidden-future-tag` photo; the hanging tag becomes the `FUTURE NOT INCLUDED` card; `NOT REALLY CHEAP` stamp. WIT betrayed.
4. **Payoff** `20.04–28.4` — `price-tag-receipt` photo (dimmed). Ends on the `HOW MUCH FUTURE?` card + deadpan WIT. No CTA — this is a complete standalone short, not a hook/teaser (owner note 2026-06-22).

## Platform-safe zone (owner note 2026-06-22)
All readable content (labels, captions, CTA, WIT face) is kept inside the box `x[60..880] · y[220..1490]`.
Outside that box the platform UI covers content: top title, **right action rail** (like/comment/share/menu),
and **bottom** caption + subscribe + progress bar. WIT may extend its body off the bottom/side edges, but its
FACE stays inside the box. Captions and CTA raised to `bottom:470px` (out of the bottom-UI band). Verified with a
temporary safe-guide overlay, then removed.

## Vertical layout rules applied
- Full-bleed real photo per scene + top/bottom scrim for text legibility (matches Section-1 overlay style, not a letterboxed crop).
- WIT enlarged to ≈⅓ frame, face kept above the caption band; body may sit behind captions (face never covered).
- Captions = distinct SUBTITLE style (white text on a translucent dark pill), centered VERTICALLY, voice-synced. Deliberately not the cream handwritten label look. WIT face kept below the caption; in-scene labels above it; captions timed to clear before the reveal/question cards so they never overlap WIT, labels, or cards. The "future not included" and final question lines are carried by the cards (no duplicate caption).
- CTA raised above the caption band; appears only after the spoken captions clear.

## Checks
- `lint`: 0 errors (2 non-blocking warnings: track density, a 0–0.2s tween overlap).
- `validate`: 0 errors; 5 contrast warnings = known dark-label-over-photo false positives.
- snapshot QA at `1 / 9 / 19 / 24.5s`: scenes render with real bases, WIT scale/crop OK, captions sync, reveal lands on the tag, CTA clean.
- No MP4 export yet (export happens after all 3 shorts are approved).
