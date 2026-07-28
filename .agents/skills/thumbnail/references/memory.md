# thumbnail - memory

Self-improving notes for thumbnail concepts. Append after **every** generation round, even
when the failure seems obvious. This file is the mechanism that produced rules A to F in
`.agents/rules/thumbnail-rules.md`. Single canonical copy, no Claude-side duplicate.

## Round history

### 2026-07-28, project 1, round 1 (v1) - rejected

One concept generated: `LONELY IN CROWDS?`, arced yellow text, mascot centered and small
among 20 grey crowd figures on flat cobalt blue.

Why it failed: head only about 25 percent of frame height, dead-center symmetry so the eye
had nowhere to land, 20 fully drawn mid-grey figures reading as mush against blue, mild
expression, and the question paraphrased the title so it added no information.

### 2026-07-28, project 1, round 2 (v2) - rejected before generation

Added giant numerals and extreme close-ups. The user rejected the questions themselves as
incomprehensible: `WHY THE HOLLOW?`, `A 200,000-YEAR BUG?`, `WHO KNOWS YOU?`. Nothing in the
frame told the viewer what the question was about.

**Lesson that became rule C:** every noun in the question must be a physical object drawn in
the frame.

### 2026-07-28, project 1, round 3 (v3) - `[thumb-d]` accepted

Accepted: the split comparison, `LOST 110 PEOPLE?`, `150` over a fire circle on the left and
`40` over the lone mascot on the right. Saved as
`projects/1-*/outputs/thumbnail-3-accepted.jpg`.

The four rejects each produced a permanent rule:

| Concept | Failure mode | Rule |
| --- | --- | --- |
| `WHY NO BALL?` | flat two-tone background left huge void areas; the yellow ball merged into the yellow lettering and read as a sun | D: never a flat single-color background, and no prop in `#F5C518` |
| `40 FRIENDS?` | the hole through the chest rendered as a dark stain on the hoodie; `40` appeared both as text and as a numeral; black featureless crowd became a smear | E: no body modification, no repeated number, no silhouette crowds |
| `ONLY 5 REAL?` | asked for five figures and got four, which broke the text; every face smiled so there was no tension | E: never an exact count above five |
| `WHO ARE THEY?` | "blank white heads with no features" became a field of 20 giant white eggs that ate the frame; also self-contradictory, a featureless head cannot make eye contact | E: never faceless or blank crowds |

## Standing observations

- The accepted frame is the one that came closest to the competitor pattern: warm orange
  fire, brown skin tones, visible small faces, real ground and horizon. The rejects were all
  flatter and emptier.
- The user's own verdict on the winner was "not very good but the best of all". The remaining
  gap is that `@SticklyExplains` renders co-stars with shading and volume against a
  deliberately crude stick figure, and our style lock forbids shading. **Open question the
  user has not ruled on:** whether to allow thumbnail-only co-star shading, which would break
  style continuity with the video but match the 2M-view reference.
- The straight full-bleed text worked at 120 px in all five generations. The arc is gone for
  good.

## Competitor reference

`research/thumbnail-swipe/` holds 40 thumbnails and `ANALYSIS.md`. Metadata came from
YouTube's InnerTube endpoint because youtube.com is network-blocked on this machine; see the
project memory note about that if the swipe file ever needs refreshing.
