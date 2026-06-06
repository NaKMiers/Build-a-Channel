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

## 2026-06-06

### David23 HyperFrames Direct Voice ID

Classification: `Operational lesson`

Context:
while generating Section 1 voiceover for `Why Cheap Products Keep Getting Worse`, the short HyperFrames voice list did not show `am_eric`, which led to an initial scratch `am_adam` generation.

Lesson:
`hyperframes@0.6.76` can accept the direct Kokoro voice ID `am_eric` even when the short voice list does not display it.

Working command pattern:

```text
npx hyperframes@0.6.76 tts <input.txt> --output <output.mp3> --voice am_eric --speed 0.84 --lang en-us --json
```

Operating rule:
before declaring `David23` unavailable, test `am_eric` directly. Do not silently fall back to scratch voices when the user asks for the approved brand voice.

Scope note:
this is a voiceover tooling lesson, not a change to the approved narrator identity.

### Voiceover Skill Created

Classification: `Core operational capability`

Created the fourth sequential project-local video-production skill:

- [Voiceover](C:\ME\THINGS\Build a Channel\.agents\skills\voiceover\SKILL.md)

Purpose:
turn a selected project's `02-script.md` into section-level voiceover outputs.

Operating rules:

- require `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`
- if script is missing, tell the user to run `script-draft` first
- if upstream files are newer than the script, treat voiceover as blocked until `script-draft` is rerun
- require an explicit user selection of `All` or a specific script section before creating voiceover files
- ask which script section to create voiceover for when the target is not explicit
- never infer the section from active project state, prior chat context, missing outputs, or the next likely section
- offer `All` as the first option, followed by each script section
- interpret `All` as separate section voiceover outputs, not one stitched full-video file
- write only `projects/<slug>/03-voiceover.md` and section-local files under `projects/<slug>/voiceover/`
- keep one useful MP3 preview per section by default
- label alternate local voices as scratch timing audio when the approved `David23 / am_eric` voice is unavailable
- list stale downstream files after creating or updating voiceover outputs
- keep voiceover-specific learning in `.agents/skills/voiceover/references/memory.md`

Workflow decision:
after script drafting, production may branch by section. Each section can get voiceover, visual implementation, preview, review, and approval before final assembly.

Scope note:
no packaging, visual plan, HyperFrames build, render, upload, or self-learning skill was created in this pass.

### Project-Local Browse Vendored

Classification: `Core operational capability`

Vendored the gstack `browse` skill into the project at:

- [Browse](C:\ME\THINGS\Build a Channel\.agents\skills\browse\SKILL.md)

Reason:
project-local skills should not depend only on global skills installed on one machine.

Operating rule:

- use `.agents/skills/browse/` first for web and YouTube browsing
- fall back to global gstack `/browse` only if the project-local skill or binary is missing or cannot run
- keep `topic-intake` reference research portable by preferring the project-local browse skill

### Influence-First Channel Boundary

Classification: `Core`

Decision:
remove product-specific funnel framing from the channel memory.

Working rule:

`Why It Works` should build internet influence through useful, funny, learner-friendly explainers, not through direct app or product promotion.

Implication:
future topics, scripts, packaging, and skills should optimize for audience trust, public perspective, topic clarity, and creator influence first.

### Topic Intake Skill Created

Classification: `Core operational capability`

Created the first sequential project-local video-production skill:

- [Topic Intake](C:\ME\THINGS\Build a Channel\.agents\skills\topic-intake\SKILL.md)

Purpose:
generate next-video topic candidates as scored angle packages, not generic idea lists.

Operating rules:

- read `.agents/_shared/` and the topic-angle systems before suggesting topics
- read the skill-specific memory at `.agents/skills/topic-intake/references/memory.md`
- shape candidates as `topic + contradiction + visual metaphor + viewer pain`
- score candidates with the channel-wide topic angle scorecard
- create `projects/<slug>/00-topic-intake.md` only after the user chooses a candidate or explicitly asks to start a project
- update skill memory after user review so the next topic pass improves
- promote reusable lessons back into shared memory only when they improve the whole channel

Scope note:
no other sequential production skills were created in this pass.

### Research Pack Skill Created

Classification: `Core operational capability`

Created the second sequential project-local video-production skill:

- [Research Pack](C:\ME\THINGS\Build a Channel\.agents\skills\research-pack\SKILL.md)

Purpose:
turn a selected project topic intake into a sourced evidence pack before script drafting.

Operating rules:

- select or ask for the target project before researching
- read the chosen `projects/<slug>/00-topic-intake.md` and the shared channel brain
- browse current web or YouTube sources before writing the pack
- prefer the project-local `browse` skill, then fall back to global gstack browse only if needed
- write only `projects/<slug>/01-research-pack.md`
- include source map, explanation spine, visual reference leads, English learner support, safe claims, claims to avoid, and open questions
- do not write script, packaging, visual plan, HyperFrames, or upload files in this skill
- keep research-pack-specific learning in `.agents/skills/research-pack/references/memory.md`

Scope note:
no other sequential production skills were created in this pass.

### Script Draft Skill Created

Classification: `Core operational capability`

Created the third sequential project-local video-production skill:

- [Script Draft](C:\ME\THINGS\Build a Channel\.agents\skills\script-draft\SKILL.md)

Purpose:
turn a selected project's topic intake and research pack into a sectioned working script before voice revision.

Operating rules:

- select or ask for the target project before drafting
- require both `projects/<slug>/00-topic-intake.md` and `projects/<slug>/01-research-pack.md`
- read the shared channel brain, hook system, narration system, English learner clarity system, scene grammar, and the skill's own memory
- use `projects/why-everyone-pretends-to-be-busy/02-script.md` as the current structural reference when available
- copy the reference script's discipline, not its topic, jokes, or wording
- write only `projects/<slug>/02-script.md`
- include section summary, section narration, visual goals, approval checks, claim safety notes, English learner notes, and next-step boundary
- do not write voiceover, packaging, visual plan, HyperFrames, render, upload, or self-learning files in this skill
- keep script-draft-specific learning in `.agents/skills/script-draft/references/memory.md`

Scope note:
no other sequential production skills were created in this pass.

### Sequential Skill Pipeline Gate Added

Classification: `Operational lesson`

Decision:
sequential video-production skills must require previous step outputs before running.

Operating rules:

- `research-pack` requires `projects/<slug>/00-topic-intake.md`
- `script-draft` requires `projects/<slug>/00-topic-intake.md` and `projects/<slug>/01-research-pack.md`
- future skills should follow the same `1 -> 2 -> 3 -> ...` dependency chain
- if a required previous output is missing, the skill stops and tells the user which earlier skill to run first
- if an earlier step is rerun, every downstream output in that project becomes stale
- stale downstream files should be removed only by explicit user request or regenerated by rerunning downstream skills in order

Reason:
the channel workflow should behave like a production pipeline, not a loose pile of files. Later steps must not silently build from missing or outdated earlier work.

## 2026-06-05

### Source Structure Refactor: Agents, Shared Brain, Projects

Classification: `Core operational structure`

Refactored the workspace around the future sequential video-production skill system.

New structure:

- `.agents/_shared/` is the shared channel brain for strategy, learning, systems, assets, templates, tools, voice, HyperFrames notes, and non-executable workflows
- `.agents/rules/` stores operating rules for Codex and future skills
- `.agents/skills/` stores executable Codex skills only
- `projects/` stores one folder per video

What changed:

- moved old `docs/` content into `.agents/_shared/channel/`
- moved old `common/` content into `.agents/_shared/`
- moved old `video-projects/` content into `projects/`
- renamed old conceptual shared `skills` notes to `.agents/_shared/workflows/`
- preserved existing `WIW Take Note` as the only executable project-local skill
- upgraded `projects/_template/` to match the 10-step video lifecycle

Scope note:
no new sequential production skills were created in this pass.

Verification:
HyperFrames checks pass from the new `projects` paths for the canonical active project and all three section preview projects.

## 2026-06-04

### HyperFrames Section Review Lesson: One Section, One Port

Classification: `Operational lesson`

Context:
while reviewing `Why Everyone Pretends To Be Busy`, the user saw both Section 1 and Section 2 as Section 2 when using one shared HyperFrames Studio project.
The issue came from the default Studio route pointing at the active `index.html`, which made section switching ambiguous.

Lesson:
during section-by-section production, run each section as a separate HyperFrames preview project on its own port.
Do not combine sections or rely on one Studio project to switch between sections until all sections are approved and the user explicitly asks for assembly.

Working rules:

- one section equals one preview project folder, one `index.html`, and one port
- use separate Studio URLs for review, not query params on a shared Studio URL
- keep canonical section sources saved separately so accepted sections do not get overwritten by the next draft
- assemble sections into one long composition only after the user asks
- write the active ports and section URLs into the current video review notes

Applied to current video:

- Section 1 runs on `http://localhost:3021/#project/section-01-hook`
- Section 2 runs on `http://localhost:3022/#project/section-02-reframe`
- active preview folders live under [section-previews](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\section-previews)

---

### Section 1 Review Lesson: Simpler Static Boards Beat Dense Micro-Animation

Classification: `Operational lesson`

Context:
while reviewing Section 1 of `Why Everyone Pretends To Be Busy`, the user approved the simpler remake after rejecting a busier pass that had too many transitions, cue-level pop-ins, disappearing elements, and moving objects inside a `24.085s` hook.

Lesson:
for short Casually Explained-inspired hook sections, do not try to make every spoken phrase trigger a new visual event.
The section should feel like rough annotated real-life boards, not a small animated dashboard.

Working rules:

- for a `20-30s` hook, start with `6-8` static boards before adding any in-board animation
- use hard cuts by default; add transition overlays only after timing and paused-frame clarity are approved
- one board should usually have one real-life image, one WIT reaction, one main label, and at most one support prop
- do not animate calendar, inbox, phone, labels, stamps, and WIT all within the same few seconds
- do not make labels appear and disappear rapidly just because the voice says related words
- when referencing `Casually Explained`, prefer simple still-frame joke clarity over production polish
- generated or real-world images should describe the idea, but they should not become a busy collage
- verify short sections with a board-level contact sheet first; use cue-frame checks only for specific timing bugs

Applied to current video:

- `projects/why-everyone-pretends-to-be-busy/hyperframes/index.html` was remade as `8` static boards with no transition overlays
- [Section 01 Simple Remake](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\08-section-01-simple-remake.md) records the accepted approach
- [Section 01 Review](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\06-review.md) records the current approved direction

---

## 2026-06-02

### Original WIT 24 Pose Replacement

Classification: `Core`

Replaced the previous WIT direction with the user-approved `original-wit` character.

Output:

- [Original WIT 24 pose set](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\original-wit-24)
- [Original WIT 24 contact sheet](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\original-wit-24\original-wit-24-contact-sheet.png)

Direction:

- completely new WIT, not based on the older cute/polished WIT
- rougher, funny-stupid, awkward, and unserious
- closer in comedy function to a simple explainer visual punching bag, without copying any stickman style
- keeps the channel signature through the long receipt-like tie

Production status:

- generated `24` source chroma PNGs
- converted all `24` to transparent production PNGs
- copied transparent PNGs into the pose-set root for direct HyperFrames use
- older `core-24` and `comedy-core` assets are now superseded source/history
- no `projects/` files were edited or updated

---

### Channel-Wide Publishing Feedback Loop

Classification: `Core`

Implemented Plan 14 as a channel-wide publishing feedback loop.

What changed:

- added [Publishing Feedback Loop](C:\ME\THINGS\Build a Channel\.agents_shared\publishing-feedback-loop.md)
- added [Post-Upload Review Template](C:\ME\THINGS\Build a Channel\.agents_shared\post-upload-review-template.md)
- added [Channel Learning Rules](C:\ME\THINGS\Build a Channel\.agents_shared\channel-learning-rules.md)
- updated channel foundation, current state, README, common index, Codex collaboration notes, Codex video workflow, pre-production checklist, production quality gate, and final review checklist to route future uploads through the reusable feedback system

Core rule:

`Measure the upload. Learn one useful thing. Change the next video.`

System decision:

- every future upload should produce one short post-upload review when analytics or qualitative feedback are available
- track impressions, CTR, views after `24h` and `7d`, average view duration, average percentage viewed, first `30s` retention, retention dips, traffic source, comments, repeated reactions, questions, confusion, subs gained, and production effort when available
- when analytics are too small, use qualitative signals such as thumbnail comparison, first `10` seconds strength, viewer feedback, learner clarity, and production difficulty
- diagnose weak CTR through packaging first, weak first `30s` retention through hooks first, mid-video dips through abstraction and visual clarity, viewer confusion through learner clarity, and slow production through reusable assets and simpler boards
- label lessons as `High`, `Medium`, or `Low` confidence before turning them into next-video rules
- write only reusable lessons into `.agents/_shared/channel/learning-log.md` as `Operational lesson`, `Experiment result`, `Packaging lesson`, or `Audience insight`
- do not rewrite `.agents/_shared/channel/channel-foundation.md` from one upload without explicit confirmation

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no post-upload review was created for any existing video.

---

### Channel-Wide Topic Angle Selection System

Classification: `Core`

Implemented Plan 13 as a channel-wide topic angle selection upgrade.

What changed:

- added [Topic Angle Selection System](C:\ME\THINGS\Build a Channel\.agents_shared\topic-angle-selection-system.md)
- added [Topic Angle Scorecard](C:\ME\THINGS\Build a Channel\.agents_shared\topic-angle-scorecard.md)
- added [Topic Angle Scorecards](C:\ME\THINGS\Build a Channel\.agents_shared\channel\topic-angle-scorecards)
- updated channel foundation, current state, README, common index, Codex collaboration notes, Codex video workflow, pre-production checklist, and production quality gate to route future topics through angle scoring before scripting

Core rule:

`Do not choose a topic. Choose an angle.`

System decision:

- shape future topic candidates as `topic + contradiction + visual metaphor + viewer pain`
- require a reusable angle package before future topics move into research, packaging, hooks, scripts, or production
- score each angle across curiosity, relatability, visual motif, humor potential, English learner fit, explanation depth, packaging strength, and production feasibility
- require `30/40` or higher for normal long-form production
- require `Curiosity`, `Visual motif`, `Explanation depth`, and `Packaging strength` to each score at least `3/5`
- reject or revise angles that are generic education, mostly text thumbnails, missing WIT roles, missing real-life objects, missing repeated visual motifs, obvious in final insight, or weak for English learners

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no angle package was created for any existing video.

---

### Channel-Wide English Learner Clarity System

Classification: `Core`

Implemented Plan 12 as a channel-wide English learner clarity upgrade.

What changed:

- added [English Learner Clarity System](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-clarity-system.md)
- added [English Learner Script Checklist](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-script-checklist.md)
- added [English Learner Visual Checklist](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-visual-checklist.md)
- added [English Learner Useful Phrase Rules](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-useful-phrase-rules.md)
- added [English Learner Humor Clarity Rules](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-humor-clarity-rules.md)
- updated the channel foundation, current state, common index, README, Codex collaboration notes, Codex video workflow, script tone system, pre-production checklist, and final review checklist to route future work through the reusable learner clarity system

Core rule:

`Teach the topic first. Make the English learner-friendly by design.`

System decision:

- keep `Why It Works` as an explainer channel, not an English lesson channel
- treat English learner clarity as a product feature
- require future scripts to pass structure, sentence clarity, useful phrase, idiom/reference, humor clarity, and voice-readiness checks before full voiceover or board planning
- require future boards and rough cuts to pass one-thought, label readability, WIT emotion, learner timing, cultural-reference clarity, mobile-size, subtitle, and paused-frame checks
- allow `3-5` useful phrases per video only when they help the topic, joke, structure, or payoff
- keep humor dry and rough, but make jokes visible from context before making them clever

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no existing video script was audited or rewritten.

---

### Channel-Wide Comedy Asset Library

Classification: `Core`

Implemented Plan 11 as a channel-wide comedy asset library upgrade.

What changed:

- added [Comedy Asset Library](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy)
- added [Comedy Asset Inventory](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy\asset-inventory.md)
- added [Comedy Source Note Template](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy\source-note-template.md)
- added category rules and seed folders for `hidden-payment`, `internet-traps`, `modern-life-pain`, `red-markup`, and `wit-props`
- added [Comedy Asset Contact Sheets](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy\contact-sheets)
- updated channel foundation, current state, common indexes, Codex collaboration notes, and Codex video workflow to route future videos through the reusable comedy asset system

Core rule:

`Comedy assets should make the explanation clearer, not just busier.`

System decision:

- start the reusable comedy library with `25` seed asset targets, `5` per category
- require every promoted comedy asset to have a source note, safe-use decision, contact-sheet/readability check, and clear comedy job
- for future videos, choose `1` main recurring motif, `2-4` supporting comedy objects, `1` red markup style, and `1-2` WIT props
- avoid real logos, private data, unclear copyrighted images, overly polished stock assets, and one-video-only jokes in the reusable library
- treat this first pass as a reusable inventory and structure, not as a video-specific asset selection

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no comedy assets were selected for any existing video.

---

### Channel-Wide Reference Board And Research System

Classification: `Core`

Implemented Plan 10 as a channel-wide reference-board and research upgrade.

What changed:

- added [reference-board-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\reference-board-system.md)
- added [reference-boards/README.md](C:\ME\THINGS\Build a Channel\.agents_shared\reference-boards\README.md)
- added reusable reference-board template folders under [reference-boards/_template](C:\ME\THINGS\Build a Channel\.agents_shared\reference-boards_template)
- updated the channel foundation, current state, common index, README, Codex collaboration notes, and Codex video workflow to route future videos through the reusable reference-board system

Core rule:

`What does this topic look like in real life, and what would make it funny if paused?`

System decision:

- collect `20-30` useful references before future videos lock script, packaging, hook, or production choices
- include real-life objects, UI or screenshot patterns, visual metaphors, thumbnail tension, WIT emotion, and color/contrast references
- separate references into `safe asset`, `mockup target`, `inspiration only`, and `reject`
- require source notes before any saved, generated, or external reference influences production
- avoid copying another creator's exact frame, thumbnail, screenshot, or joke layout

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no reference board was created for any existing video.

---

## 2026-06-01

### Channel-Wide Music And Sound System

Classification: `Core`

Implemented Plan 08 as a channel-wide music and sound upgrade.

What changed:

- added [music-and-sound-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\music-and-sound-system.md)
- added [sound-effects-library/README.md](C:\ME\THINGS\Build a Channel\.agents_shared\sound-effects-library\README.md)
- added [audio-mixing-checklist.md](C:\ME\THINGS\Build a Channel\.agents_shared\audio-mixing-checklist.md)
- updated the channel foundation, current state, common index, HyperFrames notes, README, Codex collaboration notes, and Codex video workflow to point future videos through the reusable music and sound system

Core rule:

`Narration is the product. Music and sound effects are support.`

System decision:

- use light, simple, low-drama, loopable music that leaves room for David23 and English learner clarity
- choose `3` candidate tracks for each future video and test them under the first `30` seconds plus one dense explanation section
- reject corporate explainer music, cinematic trailer music, motivational tracks, heavy bass, sudden drops, and emotional scoring
- treat silence and near-silence as valid punchline tools
- use short, quiet sound effects only for useful joke, reveal, red marker, receipt, phone, lock, timer, paper, tiny payment, or fake-system moments
- run the reusable audio mixing checklist before review or final renders

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no music direction was created for any existing video.

---

### Channel-Wide Voice And Narration System

Classification: `Core`

Implemented Plan 07 as a channel-wide voice and narration upgrade.

What changed:

- added [narration-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\voice\narration-system.md)
- added [script-markup-guide.md](C:\ME\THINGS\Build a Channel\.agents_shared\voice\script-markup-guide.md)
- added [voice-test-protocol.md](C:\ME\THINGS\Build a Channel\.agents_shared\voice\voice-test-protocol.md)
- updated the channel foundation, current state, common index, HyperFrames notes, voiceover tool notes, README, Codex collaboration notes, and Codex video workflow to point future videos through the reusable narration system

Core direction:

`a calm person explaining something ridiculous while refusing to act surprised`

System decision:

- keep `David23` as the default narrator
- use `am_eric` speed `0.84` as the first long-form candidate
- use speed `0.78` as the careful learner-friendly test variant when jokes, labels, or dense explanations need more room
- keep speed `0.76` as the slower learner-paced fallback
- mark future narration with `[pause]`, `[beat]`, `[deadpan]`, `[slower]`, and `[emphasis]` before generation
- run a `45-60` second voice test and first `10` seconds visual hook check before full voiceover generation
- treat voiceover as the HyperFrames timing source, with punchline labels appearing on or just before the spoken cue

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no existing voiceover was generated or changed.

---

### Channel-Wide Scene Grammar And Visual Humor System

Classification: `Core`

Implemented Plan 06 as a channel-wide scene grammar upgrade.

What changed:

- added [scene-grammar-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\scene-grammar-system.md)
- added [visual-humor-patterns.md](C:\ME\THINGS\Build a Channel\.agents_shared\visual-humor-patterns.md)
- added [board-grammar.md](C:\ME\THINGS\Build a Channel\.agents_shared\hyperframes\board-grammar.md)
- updated the channel foundation, current state, common index, HyperFrames notes, README, Codex collaboration notes, and Codex video workflow to point future videos through the reusable scene grammar system

Core rule:

`Static drawing -> narration twist -> red markup or hard cut -> next static drawing.`

System decision:

- every future board should carry one thought, one joke or evidence object, one WIT reaction or real-life anchor, one readable label, and one clean timing beat
- use repeated visual humor patterns such as red cross-outs, bad arrows, fake diagrams, real objects with stupid labels, WIT suffering, hidden reveals, suspicious asterisks, impossible receipts, and before/after contradictions
- HyperFrames should prioritize mostly static boards, hard cuts, cue-timed labels, red markup, and paused-frame readability over decorative motion
- rough cuts should pass paused-frame review: every sampled frame should have joke value or clear evidence, WIT should be doing a job, and cue-critical text should be readable on the spoken beat

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no existing script was turned into boards.

---

### Channel-Wide Real-Life Visual Asset System

Classification: `Core`

Implemented Plan 05 as a channel-wide real-life visual asset upgrade.

What changed:

- added [real-life-visual-asset-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\real-life-visual-asset-system.md)
- added [real-life asset library](C:\ME\THINGS\Build a Channel\.agents_shared\assets\real-life)
- added [UI mockup asset library](C:\ME\THINGS\Build a Channel\.agents_shared\assets\ui-mockups)
- added [source-note-template.md](C:\ME\THINGS\Build a Channel\.agents_shared\assets\source-note-template.md)
- updated the channel foundation, current state, common index, README, Codex collaboration notes, and Codex video workflow to point future videos through the reusable asset system

Core rule:

`Use real-life assets as evidence, not decoration.`

System decision:

- mix WIT, handwritten text, and real or real-looking assets so videos feel like rough drawings commenting on real life
- use self-shot, generated, public-domain, licensed, self-made mockup, scanned texture, or recreated mockup assets with source notes
- prefer fake UI and fictional data over real screenshots, real private information, or real app logos
- test meaningful assets at `1920x1080` and mobile scale before use
- keep one-off video assets out of `.agents/_shared/` unless they are genuinely reusable

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no asset board was created for any existing video.

---

### Channel-Wide First 10 Seconds Hook System

Classification: `Core`

Implemented Plan 04 as a channel-wide hook upgrade.

What changed:

- added [hook-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\hook-system.md)
- added [first-10-seconds-board-template.md](C:\ME\THINGS\Build a Channel\.agents_shared\hook-templates\first-10-seconds-board-template.md)
- added [hook-scorecard.md](C:\ME\THINGS\Build a Channel\.agents_shared\hook-templates\hook-scorecard.md)
- updated the channel foundation, current state, common index, README, and Codex video workflow to point future videos through the reusable hook system

Core rule:

`Open with a situation, not an introduction.`

System decision:

- use `normal thing -> suspicious detail -> WIT reaction -> bigger question`
- show the topic by second `3`
- show the contradiction by second `5`
- show WIT's emotional position by second `8`
- pay off the title-thumbnail promise by second `10`
- score future hooks before full production using the reusable hook scorecard

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no opening was designed for any existing video.

---

### Channel-Wide Thumbnail Packaging System

Classification: `Core`

Implemented Plan 03 as a channel-wide packaging upgrade.

What changed:

- added [thumbnail-packaging-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\thumbnail-packaging-system.md)
- added [packaging-scorecard.md](C:\ME\THINGS\Build a Channel\.agents_shared\packaging-scorecard.md)
- added [thumbnail-visual-rules.md](C:\ME\THINGS\Build a Channel\.agents_shared\channel\branding\thumbnail-visual-rules.md)
- added [thumbnail template folder](C:\ME\THINGS\Build a Channel\.agents_shared\thumbnail-templates)
- updated channel foundation and current state to point to the reusable packaging system

Core rule:

`The thumbnail shows the weird situation. The title names the hidden logic.`

System decision:

- use `one real object + one contradiction + one WIT emotion + one short label`
- keep thumbnail labels to `1-3` words
- use strong WIT emotion in thumbnails, never neutral presenter WIT
- score future title-thumbnail pairs before scripting or production
- make the first `10` seconds pay off the thumbnail promise

Scope note:
this was applied only to reusable channel-wide docs and common files.
No `projects/` files were edited and no packaging was created for any existing video.

---

### Channel-Wide WIT Comedy System

Classification: `Core`

Implemented Plan 01 as a channel-wide WIT upgrade.

What changed:

- added [wit-channel-system.md](C:\ME\THINGS\Build a Channel\.agents_shared\channel\branding\wit-channel-system.md)
- added [usage-rules.md](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\usage-rules.md)
- added [comedy-core pose folder](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\comedy-core)
- added [comedy-core contact sheet](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\comedy-core\contact-sheet.png)
- updated the main WIT asset README to point future sessions to the channel-wide WIT system
- updated the channel foundation and current state with the reusable WIT comedy rule

Core rule:

`WIT is funniest when the system is happening to him.`

System decision:

- keep `Clean WIT` for title cards, calm explanations, and channel identity
- use `Suffering WIT` for hooks, punchlines, thumbnails, and retention beats
- use WIT as a funny reaction device and modern-life victim, not only as a cute presenter

Asset status:

- `12` comedy-core poses were seeded from compatible `core-24` assets
- `4` Plan 01 poses remain draw-required targets: `holding-red-marker`, `dragging-data-box`, `trapped-in-app`, and `receipt-printer-victim`

Scope note:
this was applied only to reusable channel-wide docs and common assets.
No `projects/` files were edited and no existing video was changed.

---

## 2026-05-30

### Renderer Migration: HyperFrames First

Classification: `Operational decision`

Decision:
migrate active video production from Remotion to HyperFrames.

What changed:

- HyperFrames is now the default renderer for new and active `Why It Works` video work
- active video source belongs in `projects/<slug>/hyperframes/`
- each HyperFrames project should keep `DESIGN.md`, `index.html`, and local assets under `hyperframes/assets/`
- review and final MP4 files still belong in `projects/<slug>/renders/`
- `remotion-studio/` is kept temporarily as legacy reference and should not be edited or deleted unless the user asks

Applied to current video:

- created `projects/why-free-apps-never-really-free/hyperframes/`
- migrated the rough cut into a HyperFrames board composition using existing George voiceover and Core 24 WIT assets
- rendered a draft MP4 at `projects/why-free-apps-never-really-free/renders/why-free-apps-hyperframes-migration-draft.mp4`

Verification:

- `npm run check` passes in the HyperFrames project with no errors and no layout issues
- draft render required adding the local `ffmpeg-static` path because global FFmpeg was not installed

Scope note:
this is an operational production migration, not a change to channel strategy.

---

## 2026-05-31

### Permanent Voice Candidate: WIW Dry Clear

Classification: `Experiment`

Created a new reusable voice candidate for `Why It Works` based on the channel voice brief.

Output:

- [voice candidate folder](C:\ME\THINGS\Build a Channel\.agents_shared\voice\why-it-works-permanent-candidate)
- sample MP3: `why-it-works-michael-dry-clear-sample.mp3`

Direction:

- calm, clear, dry, lightly skeptical, learner-friendly narration
- TTS voice: `am_michael`
- speed: `0.92`

Scope note:
this does not replace or delete existing George/reference voices.
Promote only after listening review and explicit approval.

Follow-up review:
the first sample sounded too raspy and deep.
Created a second variant using `am_adam` at speed `1.08` for a younger, slightly higher-feeling, faster narrator direction.

Second follow-up review:
the `am_adam` variant still sounded too old.
Created a third variant using `am_puck` at speed `1.12` for a brighter young male narrator direction, closer to age `23`.

Third follow-up review:
the `am_puck` variant was acceptable but still slightly raspy.
Created a fourth variant using `am_eric` at speed `1.10` to keep the age `23` direction while making the voice clearer and less raspy.

Final decision:
promote the `am_eric` variant to the permanent channel voice named `David23`.

Classification: `Core`

Approved default voice:

- Name: `David23`
- Location: [David23 voice folder](C:\ME\THINGS\Build a Channel\.agents_shared\voice\david23)
- Sample: `.agents/_shared/voice/david23/david23-sample.mp3`
- Settings: `am_eric`, speed `1.10`, `en-us`
- Direction: young male narrator around age `23`, clear, bright, fast enough, less raspy, not too deep

George and prior candidate voices remain available as fallback/reference voices.

### Active Video Voice Replacement: Why Free Apps

Classification: `Operational update`

Replaced the active `Why Free Apps Are Never Really Free` HyperFrames narration with `David23`.

What changed:

- generated 8 David23 scene MP3 files under `voiceover/david23/`
- copied active audio into `hyperframes/assets/voiceover/david23/`
- updated HyperFrames audio paths away from `george-restored/`
- proportionally adjusted part starts, part durations, board starts, board durations, and timed reveal cues to match the faster David23 voiceover
- rendered a draft MP4 at `projects/why-free-apps-never-really-free/renders/why-free-apps-david23-timed-draft.mp4`

Verification:

- `npm run check` passes with `0` errors and `0` layout issues
- remaining warnings are pre-existing style/structure warnings: handwritten font fallback, dense timelines, duplicate media discovery, and contrast warnings
- draft render completed with runtime `2:44.01`

Follow-up pacing fix:
the first David23 full-video pass was too fast for English learners and produced a `2:44.01` video.
Regenerated David23 at speed `0.76`, retimed the HyperFrames boards to the slower audio, and rendered:

```text
projects/why-free-apps-never-really-free/renders/why-free-apps-david23-learner-paced-draft.mp4
```

New runtime:
`3:50.99`

Working rule:
speed `0.76` is useful when the user wants a clearly slower learner-paced cut.

Second pacing fix:
the `0.76` learner-paced cut was slower than the requested range.
Regenerated David23 at speed `0.84`, retimed the HyperFrames boards again, and rendered:

```text
projects/why-free-apps-never-really-free/renders/why-free-apps-david23-balanced-paced-draft.mp4
```

New runtime:
`3:12.39`

Working rule:
for this script length, use David23 balanced long-form speed `0.84` when targeting about `3:10-3:30`; keep `0.76` available as the slower learner-paced fallback.

Third pacing fix:
the `0.84` balanced-paced cut was still fast in some sections and the user requested a slower version around `3:45`.
Generated a new David23 pass at speed `0.78`, retimed the active HyperFrames boards from the balanced-paced timeline using exact new segment durations, and rendered:

```text
projects/why-free-apps-never-really-free/renders/why-free-apps-david23-slow-careful-draft.mp4
```

New runtime:
`3:44.62`

Working rule:
for this script length, use David23 speed `0.78` when targeting about `3:45` and when only some sections feel rushed; it is slower than balanced-paced without becoming as slow as the `0.76` learner-paced fallback.

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

### Influence-First Positioning Note

Do not lead with app or product promotion.

Build trust first through broad explainer content, audience understanding, and a strong creator point of view.

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

Added [codex-video-workflow.md](C:\ME\THINGS\Build a Channel\.agents_shared\channel\codex-video-workflow.md) as the main execution reference for turning a topic into:

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

- [why-it-works-character.md](C:\ME\THINGS\Build a Channel\.agents_shared\channel\branding\why-it-works-character.md)

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
standardized the workspace around per-video project folders and reusable shared systems.

Added:

- [projects](C:\ME\THINGS\Build a Channel\projects)
- [projects/_template](C:\ME\THINGS\Build a Channel\projects_template)
- [projects/why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\projects\why-free-apps-never-really-free)
- [.agents/_shared](C:\ME\THINGS\Build a Channel\.agents_shared)

Why:

- each video needs its own persistent working memory
- future videos should learn from previous videos
- reusable tools, templates, workflows, assets, and production conventions should not be mixed into one-off video folders

Current rule:

- `projects/<slug>/` is the source of truth for active video work
- `.agents/_shared/` stores reusable production systems
- `.agents/_shared/channel/` stores channel-level strategy and long-term memory

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

- [prototype-first-45s.mp4](C:\ME\THINGS\Build a Channel\projects\why-free-apps-never-really-free\renders\prototype-first-45s.mp4)

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

- [wit-character-reference-v1.png](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\wit-character-reference-v1.png)
- [asset notes](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\README.md)

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

- [wit-character-reference-v2.png](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\wit-character-reference-v2.png)
- [asset notes](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\README.md)

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

- [wit-character-reference-v3-cute-short.png](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\wit-character-reference-v3-cute-short.png)
- [asset notes](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\README.md)

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

- [pose system](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\pose-system.md)
- [core-12 pose folder](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\core-12)
- [core-12 contact sheet](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\core-12\core-12-contact-sheet.png)

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
- direct product promotion should not lead the channel

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

- [core-24 pose folder](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\core-24)
- [core-24 contact sheet](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\core-24\wit-core-24-separated-contact-sheet.png)

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

## 2026-06-03

### Voice Test Lesson: Keep One Useful Audio Preview

Classification: `Operational lesson`

Context:
while remaking the Section 1 hook voice test for `Why Everyone Pretends To Be Busy`, the user clarified that future voice-test passes should not keep both MP3 and WAV outputs.

Lesson:
for voice previews, create and keep only the one audio file that is most useful for review.
Use temporary intermediate files only when needed for conversion, then remove them.

Working rules:

- prefer MP3 for lightweight voice-test review unless a renderer specifically needs WAV
- do not leave duplicate MP3/WAV versions of the same scratch voice in the project folder
- choose the single best-fitting voice variant instead of preserving multiple variants by default when the user asks for one that works
- document the selected voice, speed, duration, and file path

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
