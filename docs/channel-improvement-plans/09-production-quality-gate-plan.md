# Plan 09: Production Quality Gate

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide production quality gate that prevents future videos from entering full production when packaging, hook, humor, or visual identity is not strong enough.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable production gate for the entire channel. It must not audit any specific video.

Allowed outputs:

- `common/production-quality-gate.md`
- `common/pre-production-checklist.md`
- `common/final-review-checklist.md`

Forbidden outputs:

- no audit of any existing video project
- no edits to `video-projects/<slug>/`

## Problem

A video can be technically finished but still not feel like a strong YouTube upload.

Recent production reviews showed this risk:

- clear explanation
- clean visuals
- usable voice
- but not enough click tension, rough humor, or real-life texture

## Gate Order

Do not produce in this order:

`script -> full render -> thumbnail`

Use this order:

`package -> hook -> motif -> script -> board plan -> prototype -> full render`

## Gate 1: Packaging

Required before scripting:

- final or near-final title
- thumbnail concept
- first `10` second promise
- recurring visual motif

Pass criteria:

- thumbnail creates curiosity
- title is not generic
- WIT has a strong emotion
- the concept is not only educational

## Gate 2: Hook

Required before full script lock:

- first `10` second board plan
- hook narration
- visual contradiction
- WIT reaction

Pass criteria:

- topic is clear without audio
- contradiction appears by second `5`
- the viewer has a reason to continue

## Gate 3: Script

Required before voiceover:

- one main metaphor
- one repeated phrase
- one visual joke per section
- learner-friendly clarity pass

Pass criteria:

- each section has explanation and visual joke
- the ending lands a real insight
- no section sounds like a generic lesson

## Gate 4: Visual Board

Required before animation/render:

- board list
- WIT role per board
- real-life asset per section
- timing cues
- on-screen labels

Pass criteria:

- one thought per board
- no overloaded screens
- real-life texture appears regularly
- red markup has a purpose

## Gate 5: Prototype

Required before full render:

- first `30-60` seconds rendered
- thumbnail mockup visible beside it
- voice test synced

Pass criteria:

- first `10` seconds strong
- WIT is funny or useful
- voice sounds deadpan enough
- visuals are not too clean
- captions/text are readable

## Gate 6: Full Cut Review

Required before final polish:

- full rough cut
- paused-frame review
- mobile readability check
- audio clarity check

Pass criteria:

- every `5-10` seconds has a reason to watch
- every section has a visual idea
- no long dead clean-board stretches
- final insight is memorable

## Final Upload Checklist

Before upload, confirm:

- title and thumbnail match
- first `10` seconds pays off thumbnail
- WIT has multiple memorable reactions
- real-life assets appear
- music supports, not dominates
- video remains learner-friendly
- no copied reference material
- no unsafe copyrighted assets

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/09-production-quality-gate-plan.md.
Create or update the channel-wide production quality gate.
Allowed outputs are common/production-quality-gate.md, common/pre-production-checklist.md, and common/final-review-checklist.md.
Do not edit video-projects.
Do not audit a specific video unless I explicitly ask.
```
