# Common

This folder stores reusable systems for the `Why It Works` channel.

Use this folder for things that should improve multiple videos, not just one video.

## Folders

```text
common/
  assets/       shared brand assets, sound beds, reusable graphics
  assets/comedy/
                reusable funny objects, red markup, WIT props, and running motifs
  hook-templates/
                reusable first-10-seconds hook boards and scorecards
  hyperframes/  HyperFrames conventions and shared production notes
  reference-boards/
                reusable reference-board templates, category folders, and source-note rules
  sound-effects-library/
                reusable channel-wide sound effect families and source rules
  topic-angle-selection-system.md
                channel-wide system for turning raw topic ideas into sharp video angles
  topic-angle-scorecard.md
                reusable `40` point topic angle scorecard and production threshold
  english-learner-clarity-system.md
                channel-wide English learner clarity standards for scripts, boards, useful phrases, humor, and review gates
  publishing-feedback-loop.md
                channel-wide system for turning upload metrics, comments, retention, and production effort into next-video rules
  post-upload-review-template.md
                reusable blank post-upload review template for future published videos
  channel-learning-rules.md
                rules for deciding which upload lessons become reusable channel memory
  reference-board-system.md
                channel-wide rules for topic-specific visual and comedy reference research
  real-life-visual-asset-system.md
                channel-wide rules for real-life and real-looking assets
  scene-grammar-system.md
                channel-wide scene grammar, board density, and paused-frame gate
  visual-humor-patterns.md
                reusable visual joke patterns for simple explainer boards
  voice/       David23 voice notes, narration rules, markup guide, and voice tests
  remotion/     legacy Remotion notes kept temporarily for reference
  skills/       local project skills and repeatable Codex workflows
  templates/    reusable templates for video projects and production docs
  thumbnail-templates/
                reusable thumbnail briefs, visual patterns, and wireframes
  tools/        reusable tool notes and scripts
```

## Channel-Wide Systems

- [topic-angle-selection-system.md](topic-angle-selection-system.md)
  Channel-wide workflow for turning raw topic ideas into sharp, clickable, visual, creator-led angles before scripting.
- [topic-angle-scorecard.md](topic-angle-scorecard.md)
  Reusable `40` point gate for scoring curiosity, relatability, visual motif, WIT humor, learner fit, explanation depth, packaging strength, and production feasibility.
- [hook-system.md](hook-system.md)
  Reusable first `10` seconds hook system for future video openings.
- [hook-templates](hook-templates)
  Channel-wide hook board template and hook scorecard.
- [reference-board-system.md](reference-board-system.md)
  Channel-wide reference-board workflow for finding real-life texture, UI references, visual metaphors, thumbnail tension, WIT emotion, and source notes before production.
- [reference-boards](reference-boards)
  Reusable reference-board template folders and category instructions for future video projects.
- [real-life-visual-asset-system.md](real-life-visual-asset-system.md)
  Channel-wide system for mixing WIT, handwritten text, and real-life visual evidence.
- [scene-grammar-system.md](scene-grammar-system.md)
  Channel-wide grammar for turning explanations into simple funny boards.
- [visual-humor-patterns.md](visual-humor-patterns.md)
  Reusable visual humor patterns such as red cross-outs, fake diagrams, suspicious asterisks, and WIT suffering.
- [music-and-sound-system.md](music-and-sound-system.md)
  Channel-wide music, sound effect, track-selection, ducking, and source-safety rules.
- [sound-effects-library](sound-effects-library)
  Reusable sound effect families, naming rules, source-note expectations, and usage limits.
- [audio-mixing-checklist.md](audio-mixing-checklist.md)
  Channel-wide audio clarity and mix quality gate before review or final renders.
- [english-learner-clarity-system.md](english-learner-clarity-system.md)
  Channel-wide clarity system for keeping future videos understandable for intermediate English learners without becoming lessons.
- [english-learner-script-checklist.md](english-learner-script-checklist.md)
  Reusable script gate for structure, sentence clarity, key terms, useful phrases, idioms, humor clarity, and voice readiness.
- [english-learner-visual-checklist.md](english-learner-visual-checklist.md)
  Reusable visual gate for one-thought boards, readable labels, WIT emotion, learner timing, cultural-reference clarity, and rough-cut checks.
- [english-learner-useful-phrase-rules.md](english-learner-useful-phrase-rules.md)
  Rules for choosing `3-5` useful phrases per video and repeating them naturally without classroom interruptions.
- [english-learner-humor-clarity-rules.md](english-learner-humor-clarity-rules.md)
  Rules for dry, visible, learner-friendly humor that does not hide the explanation.
- [publishing-feedback-loop.md](publishing-feedback-loop.md)
  Channel-wide publishing feedback loop for reviewing metrics, retention, comments, and production effort after future uploads.
- [post-upload-review-template.md](post-upload-review-template.md)
  Reusable blank post-upload review template for future published videos.
- [channel-learning-rules.md](channel-learning-rules.md)
  Rules for promoting upload observations into reusable channel lessons without overreacting to one video.
- [hyperframes/board-grammar.md](hyperframes/board-grammar.md)
  HyperFrames board naming, timing, cue, motion, and paused-frame review rules.
- [voice/narration-system.md](voice/narration-system.md)
  Channel-wide narration direction, David23 speed rules, delivery rules, and timing standards.
- [voice/script-markup-guide.md](voice/script-markup-guide.md)
  Reusable script tags for pauses, deadpan delivery, learner clarity, and emphasized cue words.
- [voice/voice-test-protocol.md](voice/voice-test-protocol.md)
  Required short voice-test workflow before full voiceover generation.
- [thumbnail-packaging-system.md](thumbnail-packaging-system.md)
  Reusable title, thumbnail, and packaging workflow.
- [packaging-scorecard.md](packaging-scorecard.md)
  Channel-wide quality gate for title-thumbnail pairs.
- [thumbnail-templates](thumbnail-templates)
  Reusable packaging templates and thumbnail wireframes.
- [assets/real-life](assets/real-life)
  Reusable real-life objects, paper textures, receipt patterns, cutouts, and physical contexts.
- [assets/ui-mockups](assets/ui-mockups)
  Reusable fictional app, browser, payment, subscription, feed, and notification mockups.
- [assets/comedy](assets/comedy)
  Reusable comedy object library for hidden payments, internet traps, modern-life pain, red markup, WIT props, contact sheets, and source notes.
- [assets/source-note-template.md](assets/source-note-template.md)
  Source-note template and safety checklist for reusable and future per-video assets.

## Rule

If something belongs to one video, put it in:

```text
video-projects/<slug>/
```

If something should help many videos, put it in:

```text
common/
```

## Current Production App

The current production renderer is HyperFrames.

Per-video HyperFrames projects live at:

```text
video-projects/<slug>/hyperframes/
```

The old Remotion app still lives at:

```text
remotion-studio/
```

Keep it there for now because the user asked to delete it later, not during the migration.
Use `common/hyperframes/` for the active production conventions.

Do not move or delete legacy Remotion code unless the user explicitly requests it.
