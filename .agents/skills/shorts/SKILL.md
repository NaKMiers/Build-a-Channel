---
name: shorts
description: Side sub-workflow after combine. Turn one finished Why It Works long video into 2-4 COMPLETE vertical short videos (1080x1920, 9:16) for YouTube Shorts / TikTok / Reels, then export each to MP4. Use when the user asks for shorts, vertical shorts, YouTube Shorts, TikTok/Reels clips, cut shorts from the main video, portrait clips, or "split the video into shorts". Has three modes — plan (pick clippable moments, write shorts/shorts-plan.md), build (native portrait HyperFrames rebuild per short on port 1100+N with regenerated voiceover + burned centered subtitles), and export (render approved shorts to projects/<slug>/output/shorts/*.mp4). Each short is a COMPLETE standalone short, NOT a hook/teaser, and carries NO "watch the full video" CTA. Requires one project whose sections are already built (combine done, or every section rendered). Reuses each source section's real photos, WIT poses, and font; never edits the long-form sections. Requires one project (named or smart-selected) and an explicit short selection with All as the first option.
---

# Shorts

## Purpose

Run the `shorts` side sub-workflow of the `Why It Works` channel: derive 2-4 **complete vertical short videos** (1080x1920) from ONE finished long video and export each to MP4.

Each short is its own little story (hook -> beats -> payoff), carries channel identity (big WIT, real photo bases, handwritten labels), and is built as a **native portrait composition**, never a crop/letterbox of the 16:9 master. Each short stands alone — it is NOT a trailer for the long video and carries NO call-to-action card.

This skill REUSES each source section's approved assets (photos, WIT poses, font) and the script wording. It never edits, re-renders, or restyles the long-form sections.

## Pipeline Position

Side sub-workflow, branches from `combine`. It runs after the long video is assembled and does NOT block `caption`, `upload`, or `learning`.

```text
... -> render -> review (per section) -> combine -> caption -> upload -> learning
                                                          \-> shorts (side sub-workflow: plan -> build -> export)
```

Writes only:

- `projects/<slug>/shorts/shorts-plan.md` (the menu + per-short plan; the approval artifact)
- `projects/<slug>/shorts/short-0N-<kebab>/` (one portrait HyperFrames project per short: `index.html`, `package.json`, `hyperframes.json`, `assets/`, `voiceover/`, `tts-inputs/`, `DESIGN.md`, `snapshots/`)
- `projects/<slug>/output/shorts/short-0N-<kebab>.mp4` (the deliverables)

Never modifies `section-previews/`, `hyperframes/`, `02-script.md`, `04-voiceover.md`, `05-visual-plan.md`, or any long-form section content. It only reads them.

## Port Contract

Shorts use fixed preview ports **`1100 + short number`** (S01 -> `1101`, S02 -> `1102`, S03 -> `1103`, ...), kept clear of the long-form range `1000`-`100N`. Reuse the correct existing server on a port; stop and report an unrelated process holding it. Never use a random fallback port.

## Input Contract

Require exactly one project.

Resolution order: (1) the slug/path the user names; (2) the unambiguous active project in chat; (3) the single project under `projects/` (excluding `_template`) whose sections are all built; else ask.

Readiness: the project's sections must be built — `combine` done (`hyperframes/full-video/`) OR every `## Section N` in `02-script.md` has an approved build (`hyperframes/review/section-XX.html` or `section-previews/section-XX-*/index.html`) plus its section voiceover. If sections are missing, STOP and tell the user to finish the main pipeline first.

## Required Context

Read before working:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`, `channel-foundation.md`, `channel-guardrails.md`, `learning-log.md`
4. `.agents/_shared/systems/topic-packaging-hooks.md` (hook discipline) and `audio-feedback-quality.md`
5. `references/memory.md` (this skill's proven toolchain + locked rules) — every run
6. the chosen project's `02-script.md`, `04-voiceover.md`, `06-production-board.md`, the approved section builds, and `voiceover/combined-word-timings.json` when present
7. the `render` skill's WIT/safe-layout guidance for HyperFrames composition mechanics

## Locked Channel Rules For Shorts (owner-confirmed 2026-06-22)

These came out of the first run (`why-cheap-products-keep-getting-worse`) and are non-negotiable unless the owner changes them:

- **Native portrait rebuild**, never a crop/letterbox of the 16:9 master. New 1080x1920 composition per short; root `data-width="1080" data-height="1920"`.
- **Complete short, not a hook/teaser. NO CTA.** Never add a "FULL VIDEO ON THE CHANNEL" / "watch the full video" / subscribe card. End on the short's own payoff beat.
- **Platform-safe zone `x[60..880] · y[220..1490]`.** Keep all readable content (labels, captions, payoff cards, WIT face) inside it. Outside it the platform UI covers content: top title, right action rail (like/comment/share/menu), bottom caption + subscribe + progress bar. WIT body may bleed off the bottom/side edges, but its FACE stays inside. Verify with a temporary dashed safe-guide overlay (+ a center line), then REMOVE the guide before handoff.
- **WIT big** (≈1/3-1/2 of the frame), face kept ABOVE the centered caption so the caption never covers it. Reuse approved WIT pose PNGs only.
- **Captions = distinct SUBTITLE style**, NOT the cream handwritten label look: white text on a translucent dark pill (`rgba(16,12,9,0.5)` + dark text-stroke shadow), centered VERTICALLY (`top:50%`), 2-4 words, voice-synced. Punchline/definition/payoff lines are carried by the on-screen cards/bubbles and are NOT duplicated in a caption; captions are timed to clear before a card pops so they never overlap WIT, labels, or cards.
- **Reuse the source section's real photo bases + WIT poses + font.** Copy a minimal working set into the short's `assets/photos`, `assets/wit`, `assets/fonts` (junctions fail on this Windows HyperFrames setup). Every scene has a real photo base + a top/bottom scrim.
- **Voiceover regenerated per short** from the trimmed/assembled script via `hyperframes tts` in the approved voice `David23 / am_eric / 0.84 / en-us` — see memory for the Python/kokoro toolchain. Same words, same voice, only the subset the short needs.
- **Captions timed from real word-level timings** (whisper-tiny.en) of the short's own audio; re-time the tail monotonically (whisper end-of-audio glitch). Never estimate.

## Modes

### Plan mode

Use first, or when the user asks to plan shorts / pick moments / "which clips".

- Scan `02-script.md` + approved section builds for self-contained, clippable moments (a complete idea with a fast hook and a payoff). Score each for standalone short strength (fast hook, payoff, humor, one clear idea, strong WIT/visual).
- Present a ranked menu (Tier 1/2/3) and let the user choose 2-4 (ideally 3). Do not invent moments not in the script.
- Write `projects/<slug>/shorts/shorts-plan.md`: the locked decisions (above), per-short cold-open, trimmed/assembled VO lines, scene-by-scene portrait layout + WIT placement, caption source, payoff (no CTA), target duration, and the source section(s) + assets reused.
- Get owner approval before building.

### Build mode

Use to build one selected short (or `All`). One short at a time review is the default (matches the section discipline).

Per short:
1. Write the trimmed/assembled TTS input; generate `voiceover/short-0N.mp3` (approved voice).
2. Generate `voiceover/short-0N-word-timings.json` (whisper-tiny.en); re-time the tail monotonically.
3. Copy the minimal asset working set (photos, WIT poses, font) from the source section.
4. Build `index.html` (1080x1920): real photo scene bases + scrims; big high WIT (face in safe zone); handwritten labels in the upper third; payoff card/bubble for the punchline; distinct centered subtitles voice-synced; NO CTA. Scenes on their own track indices, cues sequential on one track (trim cue durations by 0.01 to avoid float overlap).
5. `package.json` (`dev: preview --port 110N`) + `hyperframes.json`.
6. `lint` + `validate` (0 errors); `snapshot --at` the key cue frames; verify with the safe-guide overlay, then remove it.
7. Write `DESIGN.md`; start the preview server on `110N`; hand off for review.

### Export mode

Use only after the short(s) are approved.

- `npx hyperframes render --output projects/<slug>/output/shorts/short-0N-<kebab>.mp4` (needs Chrome + ffmpeg; see memory).
- Verify each MP4 with `ffprobe`: `1080x1920`, h264 + aac, duration == composition duration.
- Record the deliverables in `shorts/shorts-plan.md` (and `06-production-board.md` if useful). Do not continue into upload/learning.

## Workflow

1. Resolve one project (Input Contract) and confirm sections are built.
2. Read required context + this skill's memory.
3. Plan mode -> ranked menu -> owner picks 2-4 -> write `shorts-plan.md` -> approval.
4. Build mode per selected short (VO -> timings -> assets -> portrait comp -> checks -> snapshot/safe-guide QA -> preview -> review/edit loop).
5. Export mode once approved -> MP4 to `output/shorts/` -> ffprobe verify.
6. Update memory with any new lesson. Stop before upload/learning.

## Self-Check (before handoff)

- one project; explicit short selection (All first).
- each short: 1080x1920; native portrait (not a crop); real photo base per scene.
- NO CTA / "watch full video" card anywhere; short ends on its own payoff.
- all readable content + WIT face inside the safe zone `x[60..880] y[220..1490]`; safe-guide overlay removed.
- WIT big (≈1/3-1/2 frame), face above the centered caption; approved pose PNG only.
- captions = distinct centered subtitle style; voice-synced; punchline/payoff carried by cards, not duplicated; no overlap with WIT/labels/cards.
- VO is the approved voice; timings from real transcription with the tail re-timed.
- `lint`/`validate` 0 errors (document non-blocking warnings); snapshot QA done.
- export: MP4 in `output/shorts/`, ffprobe confirms 1080x1920 + h264/aac + correct duration.

## Hard Fails

- a CTA / "watch the full video" / subscribe card on any short (this is a complete short, not a teaser).
- a crop/letterbox of the 16:9 master instead of a native portrait rebuild.
- content or WIT face outside the safe zone, or the safe-guide overlay left in the shipped file.
- captions styled like the cream scene labels, not centered, estimated timing, or covering WIT face / labels / cards.
- tiny corner WIT, fake/drawn/CSS WIT, or a non-approved pose.
- editing or re-rendering long-form section content.
- a short on the long-form port range or a random port.
- exporting before approval, or shipping an MP4 that is not 1080x1920 / wrong duration.

## Self-Improvement

Read `references/memory.md` every run; update it when the TTS/whisper/render toolchain changes, a layout rule is refined by review, or the owner approves/rejects a pattern. Promote to `.agents/_shared/channel/learning-log.md` only when the lesson is channel-wide.
