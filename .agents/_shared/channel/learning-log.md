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
- Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> review -> upload -> learning`.
- Packaging is a side branch from `research-pack`: it requires only `00-topic-intake.md` and `01-research-pack.md`.
- Packaging does not block script, voiceover, visual plan, render, review, upload, or learning.
- After voiceover, production branches by section. `visual-plan` requires the selected section voiceover and creates section-level plans before render.
- `render` uses one HyperFrames preview project and one localhost per section. Unified/final preview is reserved for `localhost:1000`; section `N` uses `localhost:1000 + N`.
- Current WIT source is the draft simple white round-headed pose set in `.agents/_shared/assets/wit/poses/`.
- Do not use the removed older WIT directions as current channel WIT.
- Default final narrator is `David23 / am_eric / 0.84 / en-us`; test `am_eric` directly before declaring it unavailable.

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
