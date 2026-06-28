# 06 Production Board

Video: `Why The Internet Is Full Of Garbage Now`

Status: `section render in progress (Sections 1 + 2 + 3 built, ready for review)`

Source skill: `render`

Source files:

- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 |  |  | reserved |
| Section 1: Hook | 1001 | http://localhost:1001/#project/section-01-hook | http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html | running, built |
| Section 2: It Has A Name: Slop | 1002 | http://localhost:1002/#project/section-02-it-has-a-name-slop | http://localhost:1002/api/projects/section-02-it-has-a-name-slop/preview/comp/index.html | running, built |
| Section 3: What Slop Actually Is | 1003 | http://localhost:1003/#project/section-03-what-slop-actually-is | http://localhost:1003/api/projects/section-03-what-slop-actually-is/preview/comp/index.html | running, built |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook: Is Any Of This Real? | built, ready for review | 1001 | `section-previews/section-01-hook/` | visual-plan S1 + word timings | lint 0 err (1 warn); validate 0 err (15 contrast warns); 9-frame snapshot QA done | none (preview only) | 9 scenes, voice-timed to real word timings |
| 2 | It Has A Name: Slop | built, ready for review | 1002 | `section-previews/section-02-it-has-a-name-slop/` | visual-plan S2 + word timings | lint 0 err (1 warn); validate 0 err (45 contrast warns); 8-frame snapshot QA done | none (preview only) | 8 scenes, voice-timed to real word timings |
| 3 | What Slop Actually Is | built (v2 generate-forward rebuild), ready for review | 1003 | `section-previews/section-03-what-slop-actually-is/` | visual-plan S3 v2 + word timings | lint 0 err; validate 0 err (contrast warns are false positives); 9-frame snapshot QA + scenes 6/7 re-snap done | none (preview only) | 9 scenes, voice-timed; 10 generated heroes + 7 fresh bases; SLOP MACHINE motif (no sludge) |
| 4-7 | - | not rendered | - | - | - | - | - | - |

## Shared Asset Rules

- Video-level assets: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section asset junction rule: `section-previews/section-01-hook/assets` -> junction to `../../assets` (verified resolves)
- Attribution file: `assets/ATTRIBUTION.md` (all bases CC0/PD; Shrimp Jesus + AI hand are Public Domain)
- WIT poses: transparent cutouts copied from the (now pre-keyed) shared library into `assets/poses/`; HTML references `./assets/poses/*.png`. No per-render keying, no `poses-keyed` folder.

## Active Section Notes

Section 1 build (`section-previews/section-01-hook/index.html`), composition `Section01Hook`, 1920x1080,
duration 31.253s, audio `section-01-hook.mp3`.

- 9 scenes, each its own clip/track, reveals pinned to REAL word timings
  (`voiceover/section-01-hook/section-01-word-timings.json`, whisper-tiny.en):
  - S1 0.00 couch + WIT holding phone, "scroll for 10 seconds" on "scroll" (3.28)
  - S2 4.84 dark room + WIT side-eye, "how much is REAL?" on "be honest" (5.22), "% human?" chip on "human" (7.12)
  - S3 8.58 laptop desk + WIT OK-sign, "3 years ago", green "100% HUMAN" stamp smash on "all of it" (10.48)
  - S4 11.62 phone-on-table + WIT deadpan, "today..." / "good luck." on "good luck" (11.88)
  - S5 12.70 living room + Shrimp Jesus post (AMEN 47K) on "a photo of a shrimp" (14.52), WIT cringe, caption on "Jesus" (15.92)
  - S6 16.56 newsroom + fake-news card on "a new story" (16.84), WIT pondering, red "DIDN'T HAPPEN" on "never happened" (18.24)
  - S7 19.08 studio console + fake-band card on "a hit song" (19.40), WIT surprised, "0 real members" on "does not exist" (20.74)
  - S8 21.76 grey-sludge flood + giant WIT drowning, "GARBAGE" smash on "garbage" (23.38), "cheap./fake./mass-produced." chips (24.66/24.98/25.40), "nobody told it to" on "nobody" (28.40)
  - S9 30.00 settled sludge + WIT pointing up, "WHY?" on "why" (30.82)
- WIT varied per scene (side/scale/pose): right / center / left / center / right / left / right / center / center; all giant (~1080-1240px), high-anchored, faces uncropped.
- Bright bases (no heavy dark scrim; light edge vignette only). Varied idea-devices per beat.

Owner review fixes applied (2026-06-28, ending region):
- S8/S9 contrast: "GARBAGE" + "WHY?" recolored to bold yellow with a dark outline; "cheap/fake/mass-produced" chips outlined; sludge bases darkened (S8 brightness 0.48, S9 0.38) so the white mascot reads.
- S8 slop bits (`shrimp-jesus`, `ai-extra-fingers-hand`) raised up and moved ABOVE the sludge overlay (z-index 7, repositioned) so they are no longer hidden.

Review nudges (optional, for owner pass):
- S6: red "DIDN'T HAPPEN" markup is slightly cramped over the busy newspaper base; could nudge lower/left.
- S7: faint SSL "Oxford" branding visible on the console base (dark/blurred); swap to a brand-free music base if it bothers.
- Band card had an orange-hatch artifact below it; cropped out via `clip-path` (not visible).
- Timing is from real word-timings (not estimated). Contrast warnings are on stylized emphasis text and read fine in the snapshot.

## Section 3 Notes (v2 generate-forward rebuild, 2026-06-28)

Build (`section-previews/section-03-what-slop-actually-is/index.html`), composition `Section03Slop`,
1920x1080, 40.704s, audio `section-03.mp3`. Rebuilt from scratch after the owner rejected v1 for
over-reusing `grey-sludge-flood` and leaning on old browsed photos.

- GENERATE-FORWARD: 10 bespoke generated heroes + 7 fresh real bases + 9 transparent WIT poses. NEW
  section motif = THE SLOP MACHINE (opens 3.1, stamps shut 3.8); NO sludge in this section.
- 9 scenes pinned to real word-timings: machine intro -> influencer bait -> six-finger meltdown ->
  gibberish sign -> "Coca-Coola" ad fail -> cost-crush avalanche (WIT flattened) -> firehose of
  identical fake-post clones -> "CERTIFIED SLOP" stamp -> screaming masked robot "AT FULL VOLUME".
- Compositing: white-bg heroes framed as `.post` cards; stamp + firehose via `multiply`; black-bg
  robot via `screen` on the dark stage (watermark masked); grey-bg crush pile radial-masked; clones
  as white post tiles (multiply made bare clones vanish on the busy pipe base).
- Post-snapshot polish: 3.7 clones -> white post tiles (8) so the torrent reads; 3.6 crushed WIT
  raised into frame + time/attention/trust labels repositioned off the edges.
- Safety: "Coca-Coola" = generic parody (no real logo); AI influencer = non-existent person.

## Stale / Regeneration Notes

- Lint warning `duplicate_media_discovery_risk`: S1 reuses (`shrimp-jesus.jpg` S5+S8, `grey-sludge-flood-1.jpg` S8+S9) and S3 `slop-clone.png` tile reuse - all intended; non-blocking.
- S3 v1 assets orphaned by the v2 rebuild (kept unless removed on request): `gallery-wall-1.jpg`, `ai-face-does-not-exist.png`, `holiday-bokeh-red-1.jpg`, `hourglass-time-1.jpg` (see `assets/ATTRIBUTION.md`).
- No `06-review.md` / `07-upload.md` / `08-self-learning.md` yet - nothing downstream stale.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
