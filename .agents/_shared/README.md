# Shared Brain

This folder is the shared memory and reusable production system for `Why It Works`.

Use it for knowledge that should improve many videos, not just one video.

## Structure

```text
.agents/_shared/
  channel/              core strategy, guardrails, references, learning log
  assets/               reusable WIT, comedy, real-life, and UI mockup assets
  voice/                narration systems, voice tests, voice notes
  hyperframes/          HyperFrames conventions and board grammar
  workflows/            non-executable reusable workflows
  templates/            reusable production templates
  tools/                reusable tool notes and scripts
  reference-boards/     reusable reference-board template
  thumbnail-templates/  reusable packaging templates
```

## Important Files

- [channel/current-state.md](channel/current-state.md)
  Fastest session rehydration file.
- [channel/channel-foundation.md](channel/channel-foundation.md)
  Stable strategy, positioning, audience, tone, pillars, and channel promise.
- [channel/channel-guardrails.md](channel/channel-guardrails.md)
  Safety gate for deciding whether an idea is `Core`, `Experiment`, or `Reject`.
- [channel/learning-log.md](channel/learning-log.md)
  Reusable lessons, operational discoveries, experiments, and dated decisions.
- [topic-angle-selection-system.md](topic-angle-selection-system.md)
  System for turning raw ideas into sharp video angles.
- [reference-board-system.md](reference-board-system.md)
  System for collecting visual, real-life, UI, WIT, and thumbnail references.
- [voice/narration-system.md](voice/narration-system.md)
  Channel-wide voice direction and pacing rules.
- [hyperframes/board-grammar.md](hyperframes/board-grammar.md)
  Board timing, cue, motion, and review rules.
- [publishing-feedback-loop.md](publishing-feedback-loop.md)
  Post-upload learning loop.

## Rules

- Put one-video work in `projects/<slug>/`.
- Put reusable memory and production systems here.
- Put executable skills in `.agents/skills/`, not in this folder.
- Put operating rules in `.agents/rules/`.
- Promote a lesson into shared memory only when it can improve future videos.
- Keep historical lessons concise; do not paste long chat transcripts.

## Relationship To Skills

Future sequential video skills should read from this folder before producing output.

Each future skill may also keep its own local memory inside its skill folder, but reusable channel-level lessons should still be promoted here.
