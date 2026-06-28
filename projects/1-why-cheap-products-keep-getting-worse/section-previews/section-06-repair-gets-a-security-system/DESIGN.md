# Section 6 Design - Repair Gets A Security System

Duration: `42.816s` · 4 big scenes · 8 cue states · 3 WIT beats

## Concept

Repair is staged as a literal **security checkpoint** the product must pass - the section title made visible. Barriers become airport-style security trays; ownership turns into a locked product; the fix is a plain-English definition + a 4-question test; the payoff is a warm `PLEASE HAVE A FUTURE` that calls back the video's `future not included` motif.

## Scenes

1. `Repair Checkpoint` (`0–12.0`) - real phone-repair-bench photo (graded, brand-masked) + CSS belt/scanner/board-phone + `BUY NEW` shortcut lane. Barriers land as trays: `NO PART`, `SPECIAL TOOL`, `NO MANUAL`.
2. `Cost + Ownership Lock` (`12.0–21.8`) - repair bill vs new box + `ALMOST NEW PRICE`; then a locked product + padlock + `YOU OWN ME... NOT ENOUGH TO OPEN ME` + `VERY HEALTHY RELATIONSHIP`.
3. `Repairability Test` (`21.8–34.8`) - real precision-screwdriver photo + `REPAIRABILITY = EASY TO FIX` definition + checklist `BATTERY? / PART? / LOCAL SHOP? / MYSTERY MACHINE?` + `LOCKED ROOM?`.
4. `Future Label` (`34.8–42.816`) - generic `FUTURE LABEL` policy card + `PLEASE HAVE A FUTURE` payoff.

## WIT

- `wit-pose-suspicious` - held across the checkpoint (cues 1–3), giant lower-left.
- `wit-pose-trapped-by-app-screen` - behind glass on the ownership lock (cue 5), giant lower-right.
- `wit-pose-deadpan-side-eye` - warm-deadpan payoff (cue 8, reveal at 39.8), giant lower-right.
- Scene 3 (definition + checklist) is intentionally WIT-free.

## Build approach

Restored 1:1 from the approved review mirror (`hyperframes/review/section-06.html`). HTML is the source of truth; 2 real graded photo bases + self-made CSS objects; handwritten labels via local Patrick Hand font; deterministic GSAP timeline with two `tl.set` opacity reveals (19.55, 39.8). Hard cuts between scenes; impact reserved for the price stamp and the two payoff reveals.
