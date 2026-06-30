# 06 Production Board

Video: `Why The Internet Is Full Of Garbage Now`

Status: `all sections rendered (Sections 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 built, ready for review)`

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
| Section 4: The Machine That Feeds Itself | 1004 | http://localhost:1004/#project/Build%20a%20Channel | http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html | running, built |
| Section 5: It Already Got Out | 1005 | http://localhost:1005/#project/Build%20a%20Channel | http://localhost:1005/api/projects/Build%20a%20Channel/preview/comp/index.html | running, built |
| Section 6: It's Not AI's Fault | 1006 | http://localhost:1006/#project/Build%20a%20Channel | http://localhost:1006/api/projects/Build%20a%20Channel/preview/comp/index.html | running, built |
| Section 7: Payoff - Attention In, Garbage Out | 1007 | http://localhost:1007/ | http://localhost:1007/api/projects/section-07-attention-in-garbage-out/preview/comp/index.html | running, built |
| Section 8: Outro - Like, Share, Subscribe | 1008 | http://localhost:1008/ | http://localhost:1008/api/projects/section-08-outro-like-share-subscribe/preview/comp/index.html | running, built |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook: Is Any Of This Real? | built, ready for review | 1001 | `section-previews/section-01-hook/` | visual-plan S1 + word timings | lint 0 err (1 warn); validate 0 err (15 contrast warns); 9-frame snapshot QA done | none (preview only) | 9 scenes, voice-timed to real word timings |
| 2 | It Has A Name: Slop | built, ready for review | 1002 | `section-previews/section-02-it-has-a-name-slop/` | visual-plan S2 + word timings | lint 0 err (1 warn); validate 0 err (45 contrast warns); 8-frame snapshot QA done | none (preview only) | 8 scenes, voice-timed to real word timings |
| 3 | What Slop Actually Is | built (v2 generate-forward rebuild), ready for review | 1003 | `section-previews/section-03-what-slop-actually-is/` | visual-plan S3 v2 + word timings | lint 0 err; validate 0 err (contrast warns are false positives); 9-frame snapshot QA + scenes 6/7 re-snap done | none (preview only) | 9 scenes, voice-timed; 10 generated heroes + 7 fresh bases; SLOP MACHINE motif (no sludge) |
| 4 | The Machine That Feeds Itself | built, ready for review | 1004 | `section-previews/section-04-the-machine-that-feeds-itself/` | visual-plan S4 + GENERATED word timings | lint 0 err (2 warns: reused-media); validate 0 err (150 contrast warns); 18-frame snapshot QA + scenes 3/4/9 re-snap done | none (preview only) | 9 scenes, voice-timed to real word timings; 8 generated heroes + 7 fresh bases; SELF-FEEDING ENGINE motif + loop-ring HUD |
| 5 | It Already Got Out | built, ready for review | 1005 | `section-previews/section-05-it-already-got-out/` | visual-plan S5 + GENERATED word timings | lint 0 err (1 warn: reused-media); validate 0 err (75 contrast warns); per-scene snapshot QA + 24.5s/29.5s SLOP re-snap done | none (preview only) | 7 scenes, voice-timed to real word timings; 6 generated heroes + 4 fresh bases + 2 reuse bases; rising GREY-SLUDGE FLOOD motif (13->66%) |
| 6 | It's Not AI's Fault (And Not A Plot) | built, ready for review | 1006 | `section-previews/section-06-its-not-ais-fault/` | visual-plan S6 + GENERATED word timings | lint 0 err (1 warn: reused-media); validate 0 err (20 contrast warns); 12-frame snapshot QA + 6.5/6.6/6.7 re-snap done | none (preview only) | 7 scenes, voice-timed to real word timings; 4 generate props + 4 fresh bases + 2 reuse bases; the fair/calm turn (CSS argument graphics; conspiracy named then crossed out) |
| 7 | Payoff: Attention In, Garbage Out | built, ready for review | 1007 | `section-previews/section-07-attention-in-garbage-out/` | visual-plan S7 + GENERATED word timings | lint 0 err (3 warns: reused-media); validate 0 err (115 contrast warns); 18-frame inspect + per-scene snapshot QA + 1.3s/14.2s re-snap done | none (preview only) | 7 scenes, voice-timed to real word timings; 1 generate prop + recurring slop-engine motif + 4 bases; the thesis-landing payoff (recap -> answer -> ATTENTION IN/GARBAGE OUT -> WORKING PERFECTLY -> THE TELLS -> empower/sign-off) |
| 8 | Outro: Like, Share, Subscribe | built (v2 gamified CTA rebuild), ready for review | 1008 | `section-previews/section-08-outro-like-share-subscribe/` | visual-plan S8 + GENERATED word timings | lint 0 err (6 warns: intentional boing/click GSAP overlaps); validate 0 err (5 contrast warns); 7-frame inspect + 6-beat snapshot QA done | none (preview only) | 1 continuous scene, voice-timed; no new assets (CSS/SVG fake-YouTube card + cursor + confetti); cursor clicks LIKE/SHARE/SUBSCRIBE on cue, buttons boing + flip to Liked/Subscribed, bell rings, confetti |

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

## Section 4 Notes (2026-06-30)

Build (`section-previews/section-04-the-machine-that-feeds-itself/index.html`), composition
`Section04Machine`, 1920x1080, 52.971s, audio `section-04.mp3`. See the section `IMPLEMENTATION.md`
for the full per-scene cue table.

- GENERATED real word timings first (plan was estimated): `voiceover/.../section-04-word-timings.json`
  (transformers.js / whisper-tiny.en). Every `data-start` + GSAP reveal pinned to actual word starts.
- 9 connected big scenes, one per beat, each its own track + crossfade. Section motif = THE
  SELF-FEEDING ENGINE (`slop-engine-loop.png`): dormant/silhouette 4.1 -> lit + roaring 4.8 -> labeled
  "THE WHOLE ENGINE" 4.9. `dark-machine-hall-1.jpg` is the shared motif base (dark -> lit callback).
- Continuity device: a small top-right loop-ring HUD that lights one node per Step (6.04 / 15.38 /
  25.86 / 33.88 / 40.58) and shows a green check on "the machine feeds itself" (44.64).
- 8 generated heroes + 7 fresh real bases + 9 distinct WIT poses (giant, varied side/pose per scene).
  `slop-clone.png` reused from S3, tiled 6x as the "flood the zone" barrage.
- Motion: ordinary labels + the writer/camera/musician/time and clicks/likes/time lists hard-show on
  their words; impact reserved for STEP pops, `$0`, `ATTENTION`, `FLOOD THE ZONE`, the payoff, and the
  SERVED + verdict stamps. 4.9 ends with a grey sludge overflow (deliberate S1-S2 flood callback /
  Section 5 setup).
- Brand safety: engagement=generic slot machine, attention=generic balance scale (no real logos). The
  incidental DELL logo on the 4.3 desk base is covered with a black bezel-matching CSS patch.
- Post-snapshot fixes: 4.4 "PAID for ENGAGEMENT" reduced 120->74px and moved left of the boss WIT
  (was overflowing the right edge / colliding with WIT); 4.9 "THE WHOLE ENGINE" given a dark shadow
  for contrast over the bright pipes; 4.3 DELL logo covered.
- Owner review fix (2026-06-30): at 0:44 the "slop -> money" / "-> MORE slop" labels were white text
  lying on the white WIT mascot (vague). Rebuilt them as dark gold-bordered "loop flow" chips moved to
  the clear top-center band (above WIT's head, between the STEP chip and the HUD) - high contrast, no
  longer covering WIT's face.

## Section 5 Notes (2026-06-30)

Build (`section-previews/section-05-it-already-got-out/index.html`), composition `Section05GotOut`,
1920x1080, 53.739s, audio `section-05.mp3`. See the section `IMPLEMENTATION.md` for the full
per-scene cue table.

- GENERATED real word timings first (plan was estimated): `voiceover/.../section-05-word-timings.json`
  (159 words; whisper tail "inbox." 56.52 clamped to the real 53.739s audio). Every `data-start` +
  GSAP reveal pinned to actual word starts.
- 7 connected big scenes, one per domain beat (music / books / kids / six-legged horse / job / payoff),
  each its own track + crossfade. Section motif = THE GREY-SLUDGE FLOOD (`grey-sludge-flood-1.jpg`
  callback from S1/S2): the `.flood` waterline rises 13 -> 19 -> 27 -> 35 -> 43 -> 53 -> 66 % across the
  7 scenes, peaking at 5.7 with WIT drowning while holding one real photo above the water.
- 6 generated heroes + 4 fresh real bases + 2 reuse bases (S1 scroll -> 5.1; S1/S2 flood -> 5.7) + 7
  distinct WIT poses (giant, varied side/pose per scene). `living-room-tv-1.jpg` reused 5.4/5.5.
- Motion: domain chips pop, ordinary labels hard-show; impact reserved for "it got out.", the
  "1,000,000 LISTENERS" card + "0 REAL MEMBERS", "KILL you.", "40%" + the 4-stamp SLOP barrage,
  "6 LEGS?!", "WORKSLOPPED" + "~2 HOURS", and the "congratulations." + domain-icon payoff.
- Asset fixes during render: 3 generated heroes (`mushroom-guide-book`, `six-legged-horse-cartoon`,
  `real-photo-lifeline`) were delivered as opaque RGB with a baked transparency-checkerboard; keyed
  the checkerboard out to true alpha (tone-mask + scipy connected-components + 1px dilation), originals
  backed up to `assets/_raw-checkerboard/`. The 5.4 SLOP-stamp GSAP selector was fixed
  (`:nth-of-type` -> `:nth-child(2/4/6/9) .ss`, `.ss` default `opacity:0`), clearing 2 validate warnings.
- Brand safety: AI band = non-existent uncanny people (no real artist); the incidental Apple logo on
  the 5.6 `office-desk-inbox-1.jpg` base is covered by the workslop-document hero composited over it.

## Section 6 Notes (2026-06-30)

Build (`section-previews/section-06-its-not-ais-fault/index.html`), composition `Section06NotFault`,
1920x1080, 38.933s, audio `section-06.mp3`. See the section `IMPLEMENTATION.md` for the full per-scene
cue table.

- GENERATED real word timings first (plan was estimated): `voiceover/.../section-06-word-timings.json`
  (123 words; whisper tail "incentive." end 47.96 clamped to the real 38.933s, its start 38.32 is
  correct). Every `data-start` + GSAP reveal pinned to actual word starts.
- 7 connected big scenes, one per beat (fair intro / good-AI examples / formula / conspiracy / reject /
  empty-villain / payoff), each its own track + crossfade. This is the calm/fair turn, so it leans on
  real bases + CSS "argument graphics" (level balance scale, two green NOT SLOP checks, SLOP = LOW
  EFFORT x HIGH VOLUME formula, DEAD INTERNET THEORY title, big red X, glowing $) rather than loud
  kinetic devices.
- Continuity: the S2 conspiracy corkboard returns for 6.4 (dead internet theory) and is crossed out
  with a giant red X in 6.5 ("name it, then puncture it"). 6.7 reuses the S4.5 dark stage.
- 4 generate props + 4 fresh real bases (courtroom / clinic / workbench / boardroom) + 2 reuse bases
  (corkboard S2, dark stage S4.5) + 7 distinct WIT poses (giant, varied side/pose per scene).
- Asset fixes during render: 3 of the 4 generate props (`artist-easel`, `empty-villain-throne`,
  `uncuffable-incentive`) were delivered as opaque RGB with a baked transparency-checkerboard (the
  `tinfoil-hat` was real RGBA); keyed the checkerboard out to true alpha (same S5 tone-mask + scipy
  connected-components + 1px dilation; interior whites like the easel canvas and the coin glow/sparkles
  survive). Originals backed up to `assets/_raw-checkerboard/`.
- Three WIT-collision fixes after first snapshot QA: (6.5) moved the giant red X off WIT's deadpan face
  onto the board; (6.6) moved "the money rewards it." off WIT's white body to the dark floor center;
  (6.7) shifted the 3 payoff lines + coin clear of WIT's face on the left.
- Brand/safety: AI shown as a genuine helper (doctor scan, artist tool) so it isn't anti-AI; the
  conspiracy is the abstract "dead internet theory" + an empty tinfoil hat (no real person/official);
  the villain throne is deliberately EMPTY; the edge stays on the incentive (a gold $).

## Section 7 Notes (2026-06-30)

Build (`section-previews/section-07-attention-in-garbage-out/index.html`), composition
`Section07Payoff`, 1920x1080, 43.413s, audio `section-07.mp3`. See the section `IMPLEMENTATION.md` for
the full per-scene cue table.

- GENERATED real word timings first (plan was estimated): `voiceover/.../section-07-word-timings.json`.
  Every `data-start` + GSAP reveal pinned to actual word starts; root clamped to the real 43.413s.
- 7 connected big scenes, one per payoff beat (recap WHY? / the answer + trophy / ATTENTION IN -
  GARBAGE OUT / not broken - WORKING PERFECTLY / THE TELLS checklist / empowerment / sign-off), each its
  own track + crossfade. Motif = the recurring `slop-engine-loop` (7.1/7.3/7.4/7.7) + the
  `slop-wins-trophy` podium (7.2). Bases graded dark -> bright across the section (flood -> clarity).
- NEW whisper artifact handled: a chunk-boundary REORDER glitch pulled the closing phrases out of order
  ("you keep your eyes open" mistimed to ~35s). Real order is the weird-machine line (~41.9s) then the
  sign-off; the single final cue "keep your eyes open." is pinned to 42.00 from the audio tail - the one
  deliberately estimated cue, documented in IMPLEMENTATION.md.
- Asset fix during render: `slop-wins-trophy.png` was delivered as opaque RGB with a baked
  transparency-checkerboard; keyed the checkerboard out to true alpha (same tone-mask + scipy
  connected-components + 1px dilation; cleared 60.2%, interior trophy shine + mascot eyes/teeth survive).
  Original backed up to `assets/_raw-checkerboard/`.
- The argument graphics (struck AI IS EVIL / CONSPIRACY / BROKEN with red strikethrough, the gold
  ATTENTION chip, the green WORKING PERFECTLY check, in/out big words, THE TELLS checklist with 2 real
  AI-tell thumbnails + 1 CSS headline tile, the receding flood band) are CSS over real bases.
- Snapshot QA: verified "WHY?" lands top-left clear of WIT (1.3s) and "slop wins." sits top-right clear
  of WIT (14.2s); no collisions.
- Brand/safety: AI is never called evil (that frame is literally struck through); the edge stays on the
  incentive; no real person/company named; the trophy podium uses the abstract slop mascot.

## Section 8 Notes (2026-06-30)

Build (`section-previews/section-08-outro-like-share-subscribe/index.html`), composition
`Section08Outro`, 1920x1080, 7.957s, audio `section-08.mp3`. See the section `IMPLEMENTATION.md` for the
full choreography table. REBUILT v2 (2026-06-30) after the owner found the flat static CTA boring - now a
loud, gamified fake-YouTube end-card.

- GENERATED real word timings: `voiceover/.../section-08-word-timings.json`. The cursor clicks land on
  their spoken words (LIKE 2.24, SHARE 3.14, SUBSCRIBE 5.22); root clamped to the real 7.957s.
- 1 continuous scene holding a fake YouTube video page (parody UI, our own WhyTube/Why It Works branding,
  all CSS/SVG - no screen-grab; uses the REAL channel avatar + a "5:00" duration). An inline-SVG mouse
  cursor flies in and CLICKS each button: LIKE boings + flips to blue "Liked" (247->248); SHARE boings +
  "Link copied!" toast; a gold glow ring pulses on SUBSCRIBE then it boings + morphs red "SUBSCRIBE" ->
  grey "SUBSCRIBED" + ringing bell, confetti bursts (12 CSS squares). NO fake subscriber count - the
  channel line reads "Subscribe for more" -> "Welcome to the channel!" with a floating green "Thanks!".
  WIT cross-fades from enthusiastic-point to calm peace sign for the "see you in the next one." + WHY IT
  WORKS sign-off.
- Assets: `channel-avatar.png` copied in from `.agents/_shared/assets/brand/`; everything else is CSS/SVG
  + reuse (`bright-window-calm-1` base, poses `enthusiastic_point_big_smile` + `peace_sign_calm_open_mouth`).
- Icons (filled thumbs-up / share-arrow / notification bell) + cursor are inline SVG, NOT emoji (emoji do
  not render in snapshot Chromium).
- Build fix: confetti pieces and the thumb-icon cuff both used class `.cf`, so confetti color rules bled
  into the thumb (green cuff) - renamed confetti to `.cfp`.
- Lint warnings (6) are all `overlapping_gsap_tweens` on the intentional boing/click micro-sequences
  (they carry `overwrite:"auto"`); non-blocking. 0 errors.
- Brand/safety: parody YouTube UI with our own branding only; no real channel/person.

## Stale / Regeneration Notes

- Lint warning `duplicate_media_discovery_risk`: S1 reuses (`shrimp-jesus.jpg` S5+S8, `grey-sludge-flood-1.jpg` S8+S9), S3 `slop-clone.png` tile reuse, S4 reuses `slop-engine-loop.png` (3.x motif 4.1/4.8/4.9) + `slop-clone.png` tiled 6x (4.6 barrage), S5 reuses `living-room-tv-1.jpg` (5.4/5.5), S6 reuses `corkboard-redstring-1.jpg` (6.4/6.5), S7 reuses `slop-engine-loop.png` (7.1/7.3/7.4/7.7) + `dark-machine-hall-1.jpg` (7.1/7.3/7.4) + `bright-window-calm-1.jpg` (7.6/7.7) - all intended; non-blocking. (S8 v2 is a single continuous scene with one base, so no reuse warning; its 6 lint warnings are intentional boing/click GSAP-tween overlaps.)
- Checkerboard-keyout originals kept in `assets/_raw-checkerboard/`: S5 (book / horse / polaroid), S6 (artist-easel / empty-villain-throne / uncuffable-incentive), and S7 (slop-wins-trophy) in case a re-key is needed.
- S3 v1 assets orphaned by the v2 rebuild (kept unless removed on request): `gallery-wall-1.jpg`, `ai-face-does-not-exist.png`, `holiday-bokeh-red-1.jpg`, `hourglass-time-1.jpg` (see `assets/ATTRIBUTION.md`).
- No `06-review.md` / `07-upload.md` / `08-self-learning.md` yet - nothing downstream stale.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
