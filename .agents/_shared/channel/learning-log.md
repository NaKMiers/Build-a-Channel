# Learning Log

Reusable lessons for `Why It Works`.

Keep this short. Current rules belong in `current-state.md`, `production-workflow.md`, `brand-system.md`, or the compact `systems/` docs. One-video details belong in `projects/<slug>/`.

## Core Decisions

- English learners are the main audience lens, but the channel is still an explainer channel, not an English class.
- Working rule: `Teach the topic first. Make the English learner-friendly by design.`
- Handwritten-looking labels, captions, arrows, red corrections, and punchline text are part of the default visual language.
- Topic selection should use angle thinking: `topic + contradiction + visual metaphor + viewer pain`.
- Publishing learning rule: `Measure the upload. Learn one useful thing. Change the next video.`

## Current Operational Decisions

- `.agents/_shared/` is now intentionally compact: use `channel/production-workflow.md`, `channel/brand-system.md`, and the four docs in `systems/` as the shared production brain.
- Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> review -> combine -> caption -> packaging -> upload -> learning`.
- Packaging (as of 2026-06-26) runs after `caption`, requires `00-topic-intake.md` + `01-research-pack.md` + `02-script.md`, and writes `output/packaging.md` (+ `output/thumbnails/`); it is no longer the numbered `03-packaging.md`.
- New-project file numbering shifted up by one (voiceover `03` … self-learning `08`); existing projects keep old numbers and skills resolve step files by name suffix (`.agents/rules/video-workflow.md`).
- After voiceover, production branches by section. `visual-plan` requires the selected section voiceover and creates section-level plans before render.
- `render` uses one HyperFrames preview project and one localhost per section. Unified/final preview is reserved for `localhost:1000`; section `N` uses `localhost:1000 + N`.
- Current WIT source is the draft simple white round-headed pose set in `.agents/_shared/assets/wit/poses/`.
- Do not use the removed older WIT directions as current channel WIT.
- Default final narrator is `David23 / am_eric / 0.84 / en-us`; test `am_eric` directly before declaring it unavailable.

## Experiments

- `Experiment` (owner-requested 2026-06-23, `why-everything-is-a-subscription-now`): denser, trend-aware
  humor. Owner said "I love joking in the video" and asked for dad jokes, currently-trending internet
  joke/meme formats, and harmless dark jokes (self-aimed/absurd, never targeting a person or group).
  Hypothesis: higher joke density (~every 15-25s) + a recognized meme format adapted as a running gag
  (e.g. "your free trial of ___ has expired") raises retention/shares without hurting learner clarity.
  Guardrails: every trending/slang line needs an on-screen visual + a one-line learner gloss (the
  channel bans native-only-knowledge jokes); jokes must still support clarity. Concrete device/object
  motifs (phone, laptop, monitor, car screen) preferred over abstract symbols. NOT a voice/tone
  foundation change — validate against real retention before promoting to `channel-foundation.md`.

## Production Lessons

- For `20-30s` hooks, start with `6-8` simple static boards before adding motion.
- One board should usually carry one thought, one readable label, and one clear joke or evidence job.
- Use hard cuts by default; add motion only when it improves clarity, timing, or the joke.
- Sequential cue timing does not require animating every block. Ordinary labels should hard-show on the spoken beat; reserve smash/pop/stamp motion for emphasized words, proof marks, and payoff phrases.
- WIT is the emotional subject when it appears. Use large, goofy, readable poses for emotional beats and verify face/head/shoulder crop with runtime screenshots or contact sheets.
- Text/WIT collision must be checked both ways. WIT should not cover labels or proof, and payoff text/stamps/cards should not cover WIT's face or expression when WIT is carrying the emotion.
- Do not overuse WIT. For short sections, start with about `1-2` WIT beats per persistent big scene and let labels, props, and markup carry explanatory cues between WIT moments.
- During section-by-section HyperFrames production, preview one section per project/port and assemble only after approval.
- If the user manually edits a HyperFrames Studio/localhost preview, preserve the current section `index.html` as canonical. Future updates must read and diff that file first, never overwrite it from an older review mirror or visual plan, and remove only targeted accidental artifacts.
- Voice sync comes first: board changes, labels, underlines, and emphasis should land on the spoken cue.
- Cue-critical visuals must be readable on the cue frame, not merely beginning animation there.
- Visual references should start from real internet, self-shot, or local images when the topic has real-world objects. Generated images are support, cleanup, or controlled mockups after real texture is understood.
- Keep only one useful audio preview per voice test unless the user asks for variants.
- Prototype `45-60s` before building a full rough cut when testing a new visual language.
- `Core` (owner-confirmed 2026-06-22, `why-everyone-pretends-to-be-busy` S5–S7): EVERY scene needs a real, people-free photo background — including real-UI scenes (chat/Meet/Trello/spreadsheet/calendar) and stylized CSS constructs (shield/stage). Float the UI as a drop-shadowed `.screen` on a real desk; back a CSS construct with a real photo. All-CSS-on-flat-gradient reads as "not lively / no background" and gets rejected. Prefer a base that echoes the line; hands-at-keyboard photos are fine (no-face allows hands).
- `Core` (owner-confirmed 2026-06-22): WIT default is BIG and HIGH — roughly `1/3`–`1/2` of the frame, anchored so head+glasses+torso+arms are inside the frame (only legs cropped), not a low bottom-edge peek showing just the head. When a big WIT would cover a label/board/UI, RE-ARRANGE the other items (opposite side / top / bottom); never shrink or lower WIT to fit. Design label/UI positions around a big, high WIT from the start.
- Operational: generate the section `section-XX-word-timings.json` from the audio (whisper) before timing cues; inspect the tail for both duplication AND backward-jump (chunk-boundary) glitches and re-time monotonically before pinning cues.
