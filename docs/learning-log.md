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

## 2026-05-30

### Renderer Migration: HyperFrames First

Classification: `Operational decision`

Decision:
migrate active video production from Remotion to HyperFrames.

What changed:

- HyperFrames is now the default renderer for new and active `Why It Works` video work
- active video source belongs in `video-projects/<slug>/hyperframes/`
- each HyperFrames project should keep `DESIGN.md`, `index.html`, and local assets under `hyperframes/assets/`
- review and final MP4 files still belong in `video-projects/<slug>/renders/`
- `remotion-studio/` is kept temporarily as legacy reference and should not be edited or deleted unless the user asks

Applied to current video:

- created `video-projects/why-free-apps-never-really-free/hyperframes/`
- migrated the rough cut into a HyperFrames board composition using existing George voiceover and Core 24 WIT assets
- rendered a draft MP4 at `video-projects/why-free-apps-never-really-free/renders/why-free-apps-hyperframes-migration-draft.mp4`

Verification:

- `npm run check` passes in the HyperFrames project with no errors and no layout issues
- draft render required adding the local `ffmpeg-static` path because global FFmpeg was not installed

Scope note:
this is an operational production migration, not a change to channel strategy.

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

---

## 2026-05-24

### WIT Core 24 Replacement

Classification: `Experiment`

Operational update:
created and separated a funnier, cuter `Core 24` WIT pose set for channel video production.

Output:

- [core-24 pose folder](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-24)
- [core-24 contact sheet](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-24\wit-core-24-separated-contact-sheet.png)

Direction:

- keep the creator-inspired dark parted hair, black glasses, white shirt, and receipt motif
- make WIT less serious, more cute, sarcastic, and mockery-friendly
- use pose filenames based on the emotion/action so future videos can reference them easily

Remotion update:
the active Remotion WIT components now load from:

- `remotion-studio/public/assets/wit/poses/core-24`

Scope note:
this replaces the active video-facing WIT assets as an experiment, but does not lock final channel character identity yet.

---

## 2026-05-28

### First-Minute Review Lesson: Voice Sync Comes First

Classification: `Operational lesson`

Context:
while reviewing the first `1:00` Remotion preview for `Why Free Apps Are Never Really Free`, several fixes were needed because board changes were visually acceptable but not tightly synced to the narration.

Lesson:
for board-based Remotion videos, exact voice-to-scene sync is the highest priority.
Do not rely on approximate scene timing when the user reviews by timestamp.

Working rules:

- when a board contains a spoken phrase, set the board start close to the actual voice cue, not merely near the right sentence block
- if the user says a section is approved or says to keep a range unchanged, do not alter that range while fixing later scenes
- prefer hard cuts for board-style review so timeline scrubbing shows one clean board at a time
- avoid crossfade overlap between boards unless the transition itself is being reviewed
- match WIT pose emotion to the exact beat: do not use panic poses before the script introduces danger, cost, or pressure
- make WIT face or gesture toward the relevant text/object whenever WIT is used as a reaction anchor
- on-screen text must include the actual keyword being spoken when the beat depends on that word, such as `FREE`
- check text/card bounds at the reviewed timestamp; labels and invoice cards must not overflow their intended object or frame
- for short reviewed ranges, verify with still frames at exact cue timestamps before saying the fix is done

Applied to current video:

- `00:00-00:36` should now be treated as the currently preserved opening range unless the user asks to change it
- `00:36-01:00` was remade as smaller cue-matched boards after the user identified drift around `this video is not about software`
- continue reviewing the first minute by exact timestamp and keep MP4 export blocked until the user explicitly asks

### Board Review Lesson: Layout Margin And Text Emphasis Need Explicit Checks

Classification: `Operational lesson`

Context:
while reviewing `Part02TheSuspicion`, several issues repeated across WIT placement, text emphasis, and card sizing even after the broad timing was fixed.

Lesson:
for board-based Remotion scenes, passing the rough composition is not enough.
Each reviewed board needs an explicit margin, emphasis, and readability check at the exact user timestamp.

Working rules:

- do not let WIT hair or props sit flush against the selected composition bounds; leave visible headroom and side breathing room
- if a keyword will be emphasized in the next board, remove duplicate emphasis from the current board unless the repetition is clearly intentional
- when underlining a word or phrase, make the underline span the readable width of that phrase, not a shorter decorative segment
- invoice cards, labels, and mini UI elements must be checked for inner text overflow, not only outer frame overflow
- when the narration lands on a payoff phrase such as `second one`, promote that exact phrase with larger size, contrast color, or timing emphasis
- center and enlarge sentence-level boards when a supporting prop is removed, so the board still feels balanced
- verify reviewed boards with still frames before closing the fix, especially for crop issues that may not be obvious from code alone

### Part Boundary Review Lesson: Local Time Must Be Preserved

Classification: `Operational lesson`

Context:
while reviewing `Part05Method1Ads`, the scene originally cut off while the voice was still saying `then sells pieces of that attention`.
The first fix extended the part too far; the user then specified that Part 5 should finish at local `00:19.15`.

Lesson:
when the user gives a part-local end time, preserve that local timestamp exactly as the source of truth, then convert it to the full-video global timeline.

Working rules:

- for part compositions, calculate `global end = part start + requested local end`
- update both the part composition boundary and the next board's global `at` timestamp
- expect Remotion composition output to round to whole frames, so `19.15s` at `30fps` may display as `19.17s`
- if extending a board to finish a voice line, trim it back to the user's requested end time once they provide one
- still check layout fixes separately from timing fixes; in this pass, the sell-board arrow was moved below the labels and the `your attention` underline was delayed to the spoken cue

---

## 2026-05-29

### Retention Scene Review Lesson: Text Motion Belongs On The Spoken Beat

Classification: `Operational lesson`

Context:
while reviewing `Part06Retention`, the board content existed but several moments landed late or animated early:
`retention` underline timing, `Your boredom is inventory`, and the `check one notification / 20 minutes gone` scene.

Lesson:
when a reviewed cue names both a spoken phrase and a visual action, align the animation itself to the spoken phrase, not only the board's visibility.

Working rules:

- if a word is already visible before the voice says it, delay its underline, wiggle, pop, or emphasis to the exact spoken cue
- when the user gives part-local timestamps, convert them from the part start before editing global board times
- punchline boards should appear when the punchline phrase is spoken, even if the surrounding sentence begins earlier
- small motion such as a wiggle is useful for phrases like `20 minutes gone`, but it should stay subtle and readable
- verify both the frame before and after a cue when checking delayed emphasis, especially for underlines

### Part Tail Review Lesson: Do Not Over-Split Short End Sections

Classification: `Operational lesson`

Context:
while reviewing `Part07Method2Behavior`, the section from local `00:22.11` to the part end was first remade as multiple boards.
The user clarified that this created too many scenes for a short final idea and asked for one scene instead.

Lesson:
for a short timestamp-to-part-end tail, use one combined board when the remaining narration is one connected idea.
Do not split every phrase into a separate board if that makes the scene feel over-described.

Working rules:

- when the user asks to remake from a late timestamp to the end, check whether the remaining line is one visual idea before adding multiple boards
- prefer one strong summary board for short tail sections unless the voice has distinct cue changes that need separate visuals
- keep still-frame verification, but judge whether the board count itself feels natural for the remaining narration length

### Part08 Review Lesson: Fewer Boards, More Cue-Accurate Emphasis

Classification: `Operational lesson`

Context:
the Part08 review exposed a timing/layout pattern that should be reused for later Remotion board passes.
A short `~21s` part felt too busy when every phrase became its own scene, and several emphasis elements landed before or after the spoken word.

Lesson:
for short parts, keep fewer boards and put timed popup text, underlines, and card emphasis inside the same scene.
Exact spoken cues matter more than rough sentence starts.

Working rules:

- do not split every short phrase into a separate board; use one strong board when the narration is one connected idea
- in Remotion Studio, timestamps like `00:10.14` mean `10 seconds + 14 frames`, not decimal `10.14s`
- popup elements should appear on the spoken word, especially payoff words like `PAY`
- scene transitions should not arrive before the phrase they represent
- underlines need correct width and position; they should cover the emphasized phrase without interfering with the next line
- leave enough vertical spacing between split sentence lines so underlines do not collide
- arrows should stop near a card edge or empty area, not cover label text
- when multiple popup cards share one board, check collision after each new cue appears
- remove props if they compete with key emphasis text
- verify exact cue frames and one frame before/after important popups before calling a timing/layout fix done

### Part10 Review Lesson: Cue Frame Must Be Readable, Not Merely Started

Classification: `Operational lesson`

Context:
while reviewing `Part10YouAreTheProduct`, pop-in cards and drawn underlines were technically scheduled at the right timestamps, but their animation began at zero opacity, tiny scale, or zero width on the exact cue frame.

Lesson:
when the user cares about timing, the element must be visibly readable on the spoken cue frame, not only beginning its animation there.

Working rules:

- for cue-critical popups, do not start the cue frame at zero opacity or unreadably tiny scale
- for cue-critical underlines, give the underline a small visible stroke on the cue frame, then finish the draw animation after it
- still check one frame before the cue to confirm the element does not arrive early
