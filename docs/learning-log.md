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

### Production Lesson: More Visual Beats Per Minute

Lesson:
a `3-4 minute` explainer should not mean only a few large scenes.

Even when the visual style stays simple, quality depends on having many small visual beats:

- object changes
- quick reactions
- label swaps
- simple transitions
- repeated motifs
- small character actions
- punchline visuals
- visual examples that match individual script lines

Reason:
the reference channels often use many visual changes inside short videos.
The production can stay simple, but the screen should keep evolving so the viewer is not watching a static slide for too long.

Working rule:

`Simple style, many beats.`

For future videos, plan both:

- macro-scenes: the main sections of the explanation
- micro-scenes: the smaller screen changes inside each section

Scope note:
this is an operational production lesson, not a core strategy change.

### Voice Test Lesson: Runtime Before Production

Lesson:
run a short voice test before building the full Remotion cut.

For `Why Free Apps Are Never Really Free`, the opening/reframe voice test used `George` and suggested a pacing of about `165 words per minute`.
At that pace, the current `745` word script is likely around `4:30`, which is longer than the intended `3-4 minute` range.

Working rule:

`Test voice pacing before full production.`

For future `3-4 minute` videos, use rough word targets:

- `3:30`: about `575-590` words at this pacing
- `4:00`: about `660` words at this pacing

Scope note:
this is an operational production lesson, not a core strategy change.

### Voice Decision: Keep George For Now

Decision:
use `George` as the working narrator while the video production flow is still being shaped.

Context:
Anh Khoa recorded a reference voice sample for possible future cloning.
The local workflow is prepared, but ElevenLabs instant voice cloning requires a plan upgrade.

Current approach:

- continue with `George`
- keep Anh Khoa's reference recording in the project
- revisit voice cloning after the overall channel workflow is stable

Scope note:
this is an operational production decision, not a locked brand voice decision.

### Full Voiceover Generated

Operational update:
generated the full `George` voiceover for `Why Free Apps Are Never Really Free`.

Result:

- scene count: `8`
- total audio duration: `239.91s`
- runtime: `3:59.91`

This confirms the trimmed script fits the intended `3-4 minute` target.

Next production step:
build Remotion scene data around the generated macro-scene audio files.

### Remotion Scene Data Created

Operational update:
created Remotion scene data for `Why Free Apps Are Never Really Free`.

Result:

- macro-scenes: `8`
- first-pass micro-beats: `64`
- voiceover IDs match the generated George MP3 files
- Remotion still render check passed

Production note:
the plan originally discussed around `100` micro-beats, but the first implementation uses `64` stronger beats to keep the rough cut realistic.
More beats should be added only after watching the rough cut and identifying static sections.

### Prototype Before Full Cut

Operational decision:
build a `45-60s` visual prototype before implementing the full `Why Free Apps Are Never Really Free` rough cut.

Reason:
the channel is still shaping its visual language.
A short prototype makes it easier to test style, motion density, Wit usage, text readability, and voiceover pacing before spending time on the entire video.

Working rule:

`Prototype the first minute before building the full cut.`

---

## 2026-05-22

### First 45s Prototype Rendered

Operational update:
rendered the first `45s` visual prototype for `Why Free Apps Are Never Really Free`.

Output:

- [prototype-first-45s.mp4](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\renders\prototype-first-45s.mp4)

What it tests:

- opening hook clarity
- simple visual style
- first use of the hidden checkout metaphor
- whether Wit supports the dry humor
- whether the screen changes often enough for the narration

Production caveat:
the prototype reuses existing `George` scene voiceovers and is clipped at exactly `45s`.
ElevenLabs quota was exhausted, so a custom shortened prototype-only voiceover was not generated.

### Wit Creator-Inspired Reference V1

Experiment:
created a first creator-inspired visual reference for `Wit` / `WIT`.

Output:

- [wit-character-reference-v1.png](C:\ME\THINGS\Build a Channel\common\assets\wit\wit-character-reference-v1.png)
- [asset notes](C:\ME\THINGS\Build a Channel\common\assets\wit\README.md)

Direction:

- cute and handsome character inspired by Anh Khoa's reference image
- round black glasses, soft dark parted hair, pale blue striped shirt
- receipt-like tie kept as the channel-specific signature
- warm 2D mascot style, simple enough to simplify for animation later

Scope note:
this remains a visual identity `experiment`, not a locked core brand decision.

### Wit Real-Life Reference V2

Experiment:
created a second `Wit` / `WIT` reference using Anh Khoa's real-life photo as the stronger likeness reference.

Output:

- [wit-character-reference-v2.png](C:\ME\THINGS\Build a Channel\common\assets\wit\wit-character-reference-v2.png)
- [asset notes](C:\ME\THINGS\Build a Channel\common\assets\wit\README.md)

Direction:

- closer to Anh Khoa's real-life look than v1
- black round-square glasses, curtain-parted dark hair, slim face, clean white shirt
- cute and handsome, but less plush-like and less childish
- keeps the receipt-like tie as the channel-specific WIT signature

Scope note:
this remains a visual identity `experiment`, not a locked core brand decision.

### Wit Cute Short Reference V3

Experiment:
created a third `Wit` / `WIT` reference by improving the original cute v1 direction.

Output:

- [wit-character-reference-v3-cute-short.png](C:\ME\THINGS\Build a Channel\common\assets\wit\wit-character-reference-v3-cute-short.png)
- [asset notes](C:\ME\THINGS\Build a Channel\common\assets\wit\README.md)

Direction:

- keeps the original v1 charm but makes Wit shorter and cuter
- slightly larger simple glitter eyes with clean highlights
- softer/fluffier hair while preserving the recognizable dark parted shape
- keeps the striped shirt, black glasses, dark shorts, and receipt-like tie

Current preference:
use v3 as the preferred WIT visual reference for the next simplification and pose-set step.

Scope note:
this remains a visual identity `experiment`, not a locked core brand decision.

### WIT Core 12 Pose Set

Experiment:
created the first reusable `Core 12` WIT pose set for Remotion production.

Output:

- [pose system](C:\ME\THINGS\Build a Channel\common\assets\wit\pose-system.md)
- [core-12 pose folder](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-12)
- [core-12 contact sheet](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-12\core-12-contact-sheet.png)

What it includes:

- neutral front
- talking front
- pointing left
- pointing right
- confused
- shocked
- deadpan
- thinking
- holding phone
- holding receipt
- money panic
- tiny defeated

Production note:
the transparent PNG files are ready for prototype use in Remotion, while the `*-chroma.png` files are kept as generation sources in case transparency needs to be reprocessed.

Scope note:
this remains a visual identity and production workflow `experiment`, not a locked final WIT model sheet.

---

## 2026-05-23

### Audience Direction Update

Classification: `Core`

Decision:
make English learners the main audience lens for `Why It Works`.

What stays the same:

- English-first channel
- no-face explainer format
- core lane: money, internet, society, business, and modern life
- tone: smart, simple, funny, dry
- Deewas should not be pushed early

What changes:

- scripts should be more intentionally learner-friendly
- simple English becomes a product feature, not only a style preference
- future videos should include clearer structure, visible keywords, repeated key phrases, and humor that works from context
- the channel should feel like interesting English-native YouTube that English learners can actually follow

Working rule:

`Teach the topic first. Make the English learner-friendly by design.`

### Reference Lesson: Casually Explained English Video

Reviewed:
`Casually Explained: The English Language`

Source:
https://www.youtube.com/watch?v=9_RxaeN0FGw

Observed from the YouTube page:

- title: `Casually Explained: The English Language`
- channel: `Casually Explained`
- published: `2019-10-15`
- runtime: `5:17`
- visible chapters: intro, language difficulty, English quirks, pronunciation, dialects

Lesson:
language itself can be a funny explainer topic when it is treated as a weird human system, not a classroom lecture.

Use for `Why It Works`:

- keep English simple and spoken
- use language confusion as a joke source when natural
- make subtitles and visible words part of the experience
- avoid becoming a formal English teaching channel

### Production Decision: Handwritten Text In Remotion

Classification: `Core`

Decision:
use handwritten-looking text as the default on-screen text style for `Why It Works` videos.

Reason:
the channel is moving toward a simpler Casually Explained-inspired production style where script, jokes, voiceover, and English learner clarity matter more than full animation.
Handwritten labels make the videos feel more human, casual, and joke-friendly while staying cheap to produce in Remotion.

Implementation:

- Remotion remains the final renderer
- use static scenes, WIT poses, hard cuts, and voiceover
- render handwritten-looking labels, captions, arrows, cross-outs, corrections, and punchline text through Remotion
- use handwritten fonts, SVG text, rough shapes, or exported hand-drawn text images

Working rule:

`Handwritten text is the main visual language.`
