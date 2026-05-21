# Learning Log

This is a living log for `Why It Works`.

Use it to record:

- decisions
- experiments
- lessons
- strategy changes
- audience insights
- production discoveries

---

## 2026-05-19

### Session Summary

Initial strategy discussion for building a YouTube channel around a no-face explainer format.

### Key Decisions

- Channel name chosen: `Why It Works`
- Primary language chosen: `English`
- Creator does not want a face-led channel
- Preferred format is `informative + funny + no-face`
- Main content lane chosen:
  `money, internet, society, business, and modern life`

### Strategic Insight

The channel should not try to become a generic coding channel or generic finance channel.

The strongest identity is:

`A funny English explainer channel about money, the internet, and modern life.`

### Reference Channels Chosen

- Mèo Giải Thích
- Lóng
- Vui Vẻ
- Half as Interesting
- Casually Explained
- OverSimplified

### Strongest Style Blend

- `Half as Interesting` for topic selection
- `Casually Explained` for voice
- `Mèo Giải Thích` for structure
- `Vui Vẻ` for packaging and energy
- `OverSimplified` for payoff and pacing

### First Recommended Launch Topics

- `Why Everyone Feels Broke Now`
- `Why Free Apps Are Never Really Free`
- `Why Productivity Content Never Fixes Your Life`

### Deewas Positioning Note

Do not lead with Deewas.

Build trust first through broad explainer content, then connect the channel to money behavior and eventually to Deewas later.

### Operational Note

This workspace is now being used as long-term memory for the project. Future important strategy and learnings should be written back into these docs instead of left only in chat history.

### Protection Note

A guardrail system was added so future ideas must be treated as one of:

- `core`
- `experiment`
- `reject`

This is meant to prevent impulsive or harmful ideas from being written into the official channel strategy by accident.

---

## 2026-05-20

### Session Summary

Created a reusable Codex-first video workflow document for the workspace based on the `Why Free Apps Are Never Really Free` example.

### Operational Decision

Added [codex-video-workflow.md](C:\ME\THINGS\Build a Channel\docs\codex-video-workflow.md) as the main execution reference for turning a topic into:

- research
- script drafts
- title and thumbnail options
- production checklists
- short-form cutdowns
- post-upload review notes

### Why This Matters

This gives future Codex sessions a consistent production pipeline instead of relying on ad hoc prompting or chat memory.

### Scope Note

This was treated as an operational workflow addition, not a change to the core channel strategy.

### First Video Pack

Created the first full video pack for:

- `Why Free Apps Are Never Really Free`

The pack includes:

- topic scorecard
- research brief
- long-form script draft
- title and thumbnail options
- production checklist
- shorts cutdowns
- post-upload review template

This gives the project its first real example of the Codex workflow applied end to end.

### Visual Identity Experiment

Experiment:
explore a signature drawn character for `Why It Works`

Current recommendation:

- test `The Modern Life Victim` as the leading character concept

Reason:

- strong fit for the channel's dry humor
- flexible across money, internet, and modern-life topics
- easier to draw and animate consistently than more complex mascot concepts

This remains an `experiment`, not a locked core visual identity decision yet.

### Character Draft

Wrote a first concrete character brief for the current leading mascot direction:

- [why-it-works-character.md](C:\ME\THINGS\Build a Channel\docs\branding\why-it-works-character.md)

Working name:

- `Wit`

Core idea:

- a deadpan audience-surrogate character with a receipt-like tie or scarf that visually represents hidden costs, subscriptions, and modern systems

---

## 2026-05-21

### Session Summary

Set up the first working Remotion-based production app and connected it to ElevenLabs voiceover generation.

### Operational Decision

Added [remotion-studio](C:\ME\THINGS\Build a Channel\remotion-studio\README.md) as the default local video production app for:

- scene-based animation assembly
- AI voiceover generation
- auto-timed scene duration
- sample render export

### What Was Added

- ElevenLabs voiceover scripts for listing voices and generating scene MP3s
- a starter Remotion composition for `Why Free Apps Are Never Really Free`
- sample scene data in JSON form
- automatic scene timing based on generated voiceover files
- a sample render export path in `remotion-studio/out/`

### Scope Note

This is an operational workflow upgrade, not a change to core channel strategy.

### Voice Experiment

Experiment:
use `George` as the starting narration voice for `Why It Works`

Reason:

- strong storyteller tone
- clear enough for explainers
- good fit for dry but accessible delivery

This is an `experiment`, not a locked brand voice decision yet.

### First Rendered Cut

Operational update:
created a first rendered MP4 cut for `Why Free Apps Are Never Really Free`.

Output:

- [why-free-apps-never-really-free.mp4](C:\ME\THINGS\Build a Channel\remotion-studio\out\why-free-apps-never-really-free.mp4)

What changed:

- expanded the Remotion scene data from a short sample into a 12-scene first cut
- generated fresh ElevenLabs narration for all scenes using the current George voice experiment
- added a simple reusable `Wit` visual treatment with the receipt tie
- disabled remote sound effects for this cut so rendering works without network access

Scope note:
this is an operational production milestone, not a core strategy change.

### Workspace Standardization

Operational decision:
standardized the workspace around per-video project folders and reusable common systems.

Added:

- [video-projects](C:\ME\THINGS\Build a Channel\video-projects)
- [video-projects/_template](C:\ME\THINGS\Build a Channel\video-projects\_template)
- [video-projects/why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free)
- [common](C:\ME\THINGS\Build a Channel\common)

Why:

- each video needs its own persistent working memory
- future videos should learn from previous videos
- reusable tools, templates, skills, assets, and Remotion conventions should not be mixed into one-off video folders

Current rule:

- `video-projects/<slug>/` is the source of truth for active video work
- `common/` stores reusable production systems
- `docs/` stores channel-level strategy and long-term memory

Scope note:
this is an operational structure change, not a core channel strategy change.
