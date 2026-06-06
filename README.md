# Why It Works

This workspace is the operating memory for building the `Why It Works` YouTube channel.

It stores the channel brain, Codex rules, reusable production systems, and per-video project work so future sessions can continue from context instead of starting from zero.

## Source Structure

```text
.agents/
  _shared/      channel brain, reusable systems, assets, templates, tools, workflows
  rules/        Codex operating rules and future skill-routing rules
  skills/       executable Codex skills only
projects/       one folder per video
AGENTS.md       required startup instructions for Codex
README.md       source map for humans and future agents
```

## Main Folders

- [.agents/_shared](C:\ME\THINGS\Build a Channel\.agents\_shared)
  The shared brain of the channel: strategy, learning, reusable production systems, WIT assets, voice notes, templates, and workflow docs.
- [.agents/rules](C:\ME\THINGS\Build a Channel\.agents\rules)
  Rules for Codex, memory, and the video production workflow.
- [.agents/skills](C:\ME\THINGS\Build a Channel\.agents\skills)
  Executable project-local skills. Current skills include `browse`, `topic-intake`, `research-pack`, and `wiw-take-note`; the remaining sequential video production skills will be created later.
- [projects](C:\ME\THINGS\Build a Channel\projects)
  Per-video work. Each video keeps its own script, packaging, voiceover, HyperFrames source, renders, review notes, upload notes, and lessons.

## Shared Memory

Read these first when making strategy or production decisions:

1. [current-state.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\current-state.md)
2. [channel-foundation.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\channel-foundation.md)
3. [channel-guardrails.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\channel-guardrails.md)
4. [reference-channels.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\reference-channels.md)
5. [learning-log.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\learning-log.md)
6. [codex-collaboration.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\codex-collaboration.md)

## Video Lifecycle

The channel uses a 10-step production flow:

1. Topic intake
2. Research pack
3. Script draft
4. Voice revision and voiceover
5. Title and thumbnail packaging
6. Visual plan
7. HyperFrames build
8. Review
9. Upload
10. Self-learning

Future skills should run in this order and write their outputs into the relevant `projects/<slug>/` folder.

## Current Direction

- Channel name: `Why It Works`
- Primary language: `English`
- Format: `no-face explainer channel`
- Main audience lens: `English learners`
- Core lane: `money, internet, society, business, and modern life`
- Tone: `smart, simple, funny, dry`
- Default video text style: `handwritten labels and captions rendered through HyperFrames`

## Core Rule

If something belongs to one video, put it in `projects/<slug>/`.

If something should improve many videos, put it in `.agents/_shared/`.

If it is an executable Codex skill, put it in `.agents/skills/`.

If it is a rule for how Codex or future skills should behave, put it in `.agents/rules/`.

Before writing any core strategy change, use [channel-guardrails.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\channel-guardrails.md) and classify the change as `Core`, `Experiment`, or `Reject`.
