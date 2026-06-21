# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section render in progress — Section 6 rebuilt and live for review`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

Reconstruction note:
`06-production-board.md` was missing on disk on `2026-06-18` and is reconstructed here. Section 6 was rebuilt today from the surviving approved review mirror. Earlier sections (1–5, 8) have preview projects and review-mirror HTML on disk, but their preview servers are not currently running; their per-section status below reflects on-disk artifacts, not live servers.

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview (full video, 8 sections, ONE voiceover) | 1000 | `http://localhost:1000` | `http://localhost:1000/api/projects/Build%20a%20Channel/preview/comp/index.html` | running — assembled 2026-06-21 at `hyperframes/full-video/` (`UnifiedWhyCheapProducts`, 251.184s ≈ 4:11); single combined voiceover, per-section audio removed |
| Section 1: Hook | 1001 | `http://localhost:1001` |  | preview project on disk; server not running |
| Section 2: Cheap Is Not The Villain | 1002 | `http://localhost:1002` |  | preview project on disk; server not running |
| Section 3: The Price Tag Speaks First | 1003 | `http://localhost:1003` |  | preview project on disk; server not running |
| Section 4: The Boring Parts Disappear | 1004 | `http://localhost:1004` | `http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html` | running — remade from scratch 2026-06-21, ready for review |
| Section 5: More Features, More Tiny Deaths | 1005 | `http://localhost:1005` | `http://localhost:1005/api/projects/Build%20a%20Channel/preview/comp/index.html` | running — remade from scratch 2026-06-21, ready for review |
| Section 6: Repair Gets A Security System | 1006 | `http://localhost:1006` | `http://localhost:1006/api/projects/Build%20a%20Channel/preview/comp/index.html` | running — rebuilt 2026-06-18, ready for review |
| Section 7: Replacement Becomes Normal | 1007 | `http://localhost:1007` | `http://localhost:1007/api/projects/Build%20a%20Channel/preview/comp/index.html` | running — rendered 2026-06-21, ready for review |
| Section 8: Payoff | 1008 | `http://localhost:1008` |  | preview project on disk; server not running |

Preview-server project-id note: on this HyperFrames version the preview server resolves a port's project id/title as the workspace/git root name (`Build a Channel`) while `dir` correctly points to the section folder. Each section runs on its own port, so the shared id is cosmetic. Open `http://localhost:1006` and the only project on that port is Section 6.

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook | preview on disk | 1001 | `section-previews/section-01-hook/` | visual plan + manual Studio edits | prior | none | Manual Studio edits are canonical; preserve `index.html`. |
| 2 | Cheap Is Not The Villain | preview on disk | 1002 | `section-previews/section-02-cheap-is-not-the-villain/` | visual plan + manual Studio edits | prior | none | Manual Studio edits are canonical; backup under `manual-saves/`. |
| 3 | The Price Tag Speaks First | preview on disk | 1003 | `section-previews/section-03-the-price-tag-speaks-first/` | visual plan | prior | none | Scene 3 rebuilt as CSS checkout arena. |
| 4 | The Boring Parts Disappear | remade from scratch — live, ready for review | 1004 | `section-previews/section-04-the-boring-parts-disappear/` | fresh visual plan + render (2026-06-21) | lint 0 err / validate 0 err / inspect 0 issues (7 samples); snapshot QA | none | Rebuilt composition + restored its assets folder (was missing). 3 real photo bases (fabric / repair-tools / sealed box), staggered repairable-parts list, payoff `LESS FUTURE BUILT IN`, 3 WIT beats. Timing `whisper-derived` (transformers.js whisper-tiny.en → `section-04-word-timings.json`; cuts/reveals pinned to real word times after an estimated pass mismatched the voice). Synced to review mirror + unified full video (port 1000). |
| 5 | More Features, More Tiny Deaths | remade from scratch — live, ready for review | 1005 | `section-previews/section-05-more-features-more-tiny-deaths/` | fresh visual plan + render (2026-06-21) | lint 0 / validate 0 / inspect 0 (8 samples); snapshot QA | none | Rebuilt + voice-synced. One real fridge gaining a feature pile-up → "technology committee", then a real control-board failure payoff; 3 WIT beats. Timing `whisper-derived` (`section-05-word-timings.json`). Synced to review mirror + unified full video (port 1000). |
| 6 | Repair Gets A Security System | auto-adjusted (3 review passes) — live, ready for review | 1006 | `section-previews/section-06-repair-gets-a-security-system/` | restored from mirror, re-timed to word timings, all beats grounded with real photos | lint 0 err / validate 0 err / inspect 0 issues (8 samples); snapshot QA (`2026-06-21`) | none | REPAIR CHECKPOINT metaphor; 5 scene clips each on a real photo bg (repair / euro-money / padlock / opened-phone-repair / phone), 8 cues, 3 WIT beats; cues + list items voice-synced. |
| 7 | Replacement Becomes Normal | rendered — live, ready for review | 1007 | `section-previews/section-07-replacement-becomes-normal/` | visual plan (`2026-06-21`) | lint 0 err / validate 0 err / inspect 0 issues (9 samples); snapshot QA (`2026-06-21`) | none | `subscription with extra steps`; 3 scene clips, each on a real photo base (e-waste / fulfillment-boxes / cherry-wood checkout), 7 cues, 3 WIT beats; 4 friction reasons staggered; timing `estimated` (no word-timings file). Scene-3 background swapped from flat CSS to real wood on `2026-06-21` after review. |
| 8 | Payoff | preview on disk | 1008 | `section-previews/section-08-payoff/` | payoff plan | prior | none | Calm final question frame. |

## Shared Asset Rules

- Video-level assets: `projects/why-cheap-products-keep-getting-worse/assets/` (references + thumbnails). Section previews use self-contained working sets.
- Section asset junction rule: junctions failed on this Windows HyperFrames setup, so each section preview uses a minimal copied/hardlinked `assets/` working set (only the files that section uses). Section 6's set was copied from the approved review mirror.
- Attribution file: the canonical `assets/ATTRIBUTION.md` already records Section 6 direct-use bases — `repair-checkpoint-photo-base.jpg` (Wikimedia Commons, `SHIFT6mq Repair.jpg`, Triskal, CC BY-SA 4.0, graded + brand-masked) and `precision-screwdriver-photo-base.jpg` (Wikimedia Commons, `Precision Screwdriver Set 2.jpg`, oomlout, CC BY-SA 2.0). The EU repairability label and airport-security images are inspiration only. Note: the older `hyperframes/review/assets/ATTRIBUTION.md` mirror is still scoped to Sections 1–5 and is stale.

## Active Section Notes

Section 6 — `Repair Gets A Security System` (rebuilt `2026-06-18`):

- Rebuilt because the `section-previews/section-06-.../` working folder and this production board were missing while the approved render survived at `hyperframes/review/section-06.html`. Restored the preview 1:1 from that mirror; reconstructed the visual plan first.
- Build: 5 scene clips on track 1 — repair-checkpoint (`0/9.86`), cost (`9.86/2.78`, paper bg), ownership-lock (`12.64/5.34`, real padlock photo), repairability-test (`17.98/12.92`), future-label (`30.9/11.916`); 8 cue states; cuts at 9.86 / 12.64 / 17.98 / 30.9. Timed reveals: bill stamp 10.94, NEW ONE 11.8, quote 14.46, relationship note 16.2, deadpan WIT 38.9, PLEASE HAVE A FUTURE tag 41.5. Re-timed 2026-06-21 from the original 12.0 / 21.8 / 34.8 cuts to match the faster-whisper word timings.
- WIT: 3 giant beats (`suspicious` checkpoint, `trapped-by-app-screen` behind glass, `deadpan-side-eye` payoff); Scene 3 WIT-free.
- Checks: `lint` 0 errors (3 non-blocking warnings), `validate` 0 errors (35 contrast warnings from the dark-label-over-photo style), `inspect` 0 layout issues at `1,4.5,9,14,20,24,31,40.5`.
- Auto Adjust pass (`2026-06-18`): backed up to `manual-saves/auto-adjust-20260618-194852-index.html`; verified against `snapshots/` (real composited frames). WIT Dominance Gate passes on all 3 beats; both flagged collisions (cue 5 trapped-WIT vs quote/note, cue 8 deadpan-WIT vs `PLEASE HAVE A FUTURE`) are clear in the render. One fix applied: patched the `dev` script to `preview --port 1006`. The 35 validate contrast warnings are false positives (dark labels read crisply). No `index.html` change, no MP4 export.
- Auto Adjust pass (`2026-06-21`): backed up to `manual-saves/auto-adjust-20260621-124928-index.html`. Addressed 4 review notes: (1+3) removed the gray photo-wash overlay + desaturating filters (backgrounds left as-is per the user); (2+4) the ownership-lock beat is spoken at `12.64s` but the cue was pinned at `16.8s` — moved it to `12.64` and cascaded all downstream cues, scene cuts, and reveals to the faster-whisper word timings. Track fix: the 3 accumulating barrier trays moved to tracks 3/4/5 (added `clip` class + ids) to clear same-track overlaps. Manual Studio edits preserved (tray box-size, future-cue path-offset). Verified: lint 0 err, validate 0 err, inspect 0 issues (9 samples), snapshots at the new cue times confirm voice sync + clean photos. Review mirror re-synced. No MP4 export.
- Auto Adjust pass 5 (`2026-06-21`, fifth review): fixed the `PLEASE HAVE A FUTURE` payoff tag — it wrapped to two lines and its separate underline bar was misaligned. Forced one line (font 82→60, width 820, repositioned clear of WIT) and moved the underline into the text span as a `border-bottom` so it's always exactly the text width and aligned; deleted the orphaned `.red-underline` div/CSS. lint 0 / validate 0 / inspect 0 (9 samples); mirror synced. Restore point `manual-saves/auto-adjust-pass5-*-index.html`.
- Auto Adjust pass 4 (`2026-06-21`, fourth review): restore point `manual-saves/auto-adjust-pass4-*-index.html`. Replaced the repairability-test background (0:18) — the sterile screwdrivers-on-white — with a real opened-phone/battery/repair-tools bench photo `assets/section-06/repairability-photo-base.jpg` (Wikimedia, Peretz Partensky, CC BY-SA 2.0; people-free, brand-free). Higher-res alternatives were rejected for containing real people (channel guardrail). Verified lint 0 / validate 0 / inspect 0 (9 samples); mirror + image synced; ATTRIBUTION updated. The old `precision-screwdriver-photo-base.jpg` is superseded. No MP4 export.
- Auto Adjust pass 3 (`2026-06-21`, third review): restore point `manual-saves/auto-adjust-pass3-*-index.html`. Grounded the two remaining gradient beats with real photos: cost beat (`scene-cost`) now uses euro banknotes (Wikimedia, Images Money, CC BY 2.0) and the future beat (`scene-future-label`) now uses a phone-on-table photo (Wikimedia, Santeri Viinamäki, CC BY-SA 4.0; chosen over a CC0 desk shot that contained a recognizable laptop). Future-label rows now stagger to the words (REPAIR INFO 31.94 / SPARE PARTS 33.02 / BATTERY LIFE 33.72 / REPAIRABILITY 34.52). Also fixed a stray line-break in the BUY NEW `rotate` and annotated the two WIT cues with `data-layout-allow-overflow` + `overflow:visible`. Verified lint 0 / validate 0 / inspect 0 (8 samples); mirror + 2 images synced; ATTRIBUTION.md updated. All four non-checkpoint beats now have real photographic backgrounds. No MP4 export.
- Auto Adjust pass 2 (`2026-06-21`, second review): restore point `manual-saves/auto-adjust-pass2-20260621-131905-index.html`. Addressed 4 Scene-2 notes: (1+2) split `scene-cost-lock` into `scene-cost` (paper bg) + `scene-ownership-lock` using a real graded padlock photo `assets/section-06/ownership-lock-photo-base.jpg` (Wikimedia, Nino Barbieri, CC BY-SA 2.5) as both background and locked-product depiction — CSS lock-icon removed; (3) Scene 2 text now staggers to the words (stamp 10.94, NEW ONE 11.8, quote 14.46); (4) removed the empty `mystery-machine`. Verified: lint 0 / validate 0 / inspect 0 (9 samples), contrast warnings 35→30; snapshots confirm staggered reveals + padlock bg + clean scene 3. Mirror + image re-synced; ATTRIBUTION.md updated. Open follow-ups (awaiting user): `fake-phone` slab in Scene 4 is a similar empty element; checklist could be staggered. No MP4 export.

## Stale / Regeneration Notes

- Section 6 visual plan, reference board, README were reconstructed on `2026-06-18`; the section preview was then rebuilt 1:1 from the approved review mirror.
- No `07-review.md`, `08-upload.md`, or `09-self-learning.md` exist for Section 6 (or the project), so there are no downstream review/upload/learning files to mark stale.
- The surviving `hyperframes/review/section-06.html` mirror is consistent with the rebuilt preview; keep it unless explicitly asked to remove it.
- Section 7 `visual-plan` + `render` completed `2026-06-21` (live on 1007). Timing is `estimated` (no `section-07-word-timings.json`; whisper-cpp/Python unavailable to generate one) — confirm voice sync in Studio, or re-pin precisely if word timings are generated later.

## Unified Full Video (port 1000)

Produced by the `combine` skill (final workflow step; assembly-only, no MP4 export). Last run `2026-06-21`: precondition passed (all 8 sections built + audio), self-check passed (lint 0, 1 audio clip, parent = combined mp3 = 251.184s, server HTTP 200 on 1000).

Assembled `2026-06-21` at `hyperframes/full-video/`. Plays all 8 sections back-to-back as one timeline with **one continuous voiceover** (`UnifiedWhyCheapProducts`, `251.184s` ≈ `4:11`). Rebuilt `2026-06-21` after all sections were approved — all 8 section comps re-copied from the review mirror (audio-stripped), consolidated assets + all 26 WIT poses refreshed, including the remade Sections 4 & 5. Self-check: 1 audio clip (index), 0 in sub-comps, parent = combined mp3 = 251.184s, lint 0 errors, snapshot per section verified.

Build mechanics (for re-sync):
- One combined voiceover: the 8 section mp3s were concatenated in order (ffmpeg concat, stream-copy) into `combined-voiceover.mp3` (`251.184s`) at the project root. It is the only `<audio>` in the project, mounted in `index.html` at `data-start 0`, `data-duration 251.184`, `data-track-index 10`.
- The per-section `<audio>` elements were stripped from each `compositions/section-0X.html` copy, so the sections are silent visuals only (this fixed the earlier "messy voice" where 8 audios overlapped).
- Visual mount offsets = cumulative **actual** mp3 durations (probed with ffprobe; each real mp3 runs ~0.05s longer than the documented voiceover duration, so using the documented values would drift ~0.4s by section 8). Offsets: `0 / 21.264 / 43.632 / 77.112 / 115.032 / 149.736 / 192.600 / 221.976`; mount durations = actual section mp3 durations `21.264 / 22.368 / 33.480 / 37.920 / 34.704 / 42.864 / 29.376 / 29.208`. Because the combined audio is a stream-copy concat, each section's voice begins at exactly its mount offset.
- `index.html` parent: 8 `data-composition-src="compositions/section-0X.html"` host clips, each with a unique `data-composition-id` and `data-track-index`; registers an empty `window.__timelines["UnifiedWhyCheapProducts"]`.
- `compositions/section-0X.html` are copies of the approved section builds (from `hyperframes/review/section-0X.html`) with audio removed. Asset resolution is **project-root-relative**: sub-comps resolve `./assets/...` against the project root, so the consolidated `assets/` lives at `hyperframes/full-video/` root.
- Checks: `lint` 0 errors (16 non-blocking warnings). Exactly 1 audio clip; parent/audio/combined-mp3 durations all = `251.184`. Snapshot QA at `10/32/62/96/132/171/207/236s` confirms every section renders at its offset with its real photo bases, WIT, and labels.
- ffmpeg/ffprobe: not on PATH; installed `ffmpeg-static` + `ffprobe-static` into `%TEMP%/wiw-ffmpeg-static` for the concat/probe.
- To re-sync after editing a section: re-copy `hyperframes/review/section-0X.html` → `compositions/section-0X.html`, strip its `<audio>`, copy new assets into `assets/`, regenerate `combined-voiceover.mp3`, and re-derive offsets from the new actual durations. Section 7's internal timing is `estimated` (no word-timings).
- This is a preview, not an MP4 export (export not requested).

## Next Step Boundary

Next workflow step: `Review` (Section 6 is auto-adjusted and verified).

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
