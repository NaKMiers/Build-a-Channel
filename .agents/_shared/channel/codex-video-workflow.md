# Codex Video Workflow

This document turns the `Why Free Apps Are Never Really Free` example into a reusable operating workflow for `Why It Works`.

It is an execution workflow, not a change to channel strategy.

Use it when turning a topic idea into:

- a research pack
- a script draft
- packaging options
- a first `10` seconds hook board
- a production checklist
- short-form cutdowns
- a post-upload review

## Default Production Stack

The current default production path for `Why It Works` is:

- per-video planning in `projects/<slug>/`
- reusable tools, templates, and local project workflows in `.agents/_shared/`
- HyperFrames scene assembly in `projects/<slug>/hyperframes/`
- per-video `DESIGN.md`, `index.html`, local audio, and local assets under the HyperFrames project
- HyperFrames timing driven by audio clips, `data-start`, `data-duration`, and GSAP timelines
- narration prepared through [narration-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\voice\narration-system.md), [script-markup-guide.md](C:\ME\THINGS\Build a Channel\.agents\_shared\voice\script-markup-guide.md), and [voice-test-protocol.md](C:\ME\THINGS\Build a Channel\.agents\_shared\voice\voice-test-protocol.md)
- handwritten-looking text rendered in HyperFrames for labels, captions, arrows, corrections, and punchlines
- topic angle selection planned through [topic-angle-selection-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-selection-system.md), [topic-angle-scorecard.md](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-scorecard.md), and [topic-angle-scorecards](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\topic-angle-scorecards) before research, packaging, hooks, scripts, or production choices are locked
- reference-board research planned through [reference-board-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\reference-board-system.md) and [reference-boards](C:\ME\THINGS\Build a Channel\.agents\_shared\reference-boards) before scripting, packaging, hook, and production choices are locked
- real-life or real-looking visual assets planned through [real-life-visual-asset-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\real-life-visual-asset-system.md)
- reusable comedy objects, red markup, WIT props, and running motifs planned through [comedy assets](C:\ME\THINGS\Build a Channel\.agents\_shared\assets\comedy) and [comedy asset inventory](C:\ME\THINGS\Build a Channel\.agents\_shared\assets\comedy\asset-inventory.md)
- scene grammar planned through [scene-grammar-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\scene-grammar-system.md), [visual-humor-patterns.md](C:\ME\THINGS\Build a Channel\.agents\_shared\visual-humor-patterns.md), and [board-grammar.md](C:\ME\THINGS\Build a Channel\.agents\_shared\hyperframes\board-grammar.md)
- music, sound effects, and mix checks planned through [music-and-sound-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\music-and-sound-system.md), [sound-effects-library/README.md](C:\ME\THINGS\Build a Channel\.agents\_shared\sound-effects-library\README.md), and [audio-mixing-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\audio-mixing-checklist.md)
- English learner clarity planned through [english-learner-clarity-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-clarity-system.md), [english-learner-script-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-script-checklist.md), [english-learner-visual-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-visual-checklist.md), [english-learner-useful-phrase-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-useful-phrase-rules.md), and [english-learner-humor-clarity-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-humor-clarity-rules.md)
- post-upload review and next-video learning planned through [publishing-feedback-loop.md](C:\ME\THINGS\Build a Channel\.agents\_shared\publishing-feedback-loop.md), [post-upload-review-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\post-upload-review-template.md), and [channel-learning-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel-learning-rules.md)

Default local commands:

- `npm run dev`
- `npm run check`
- `npm run render`

## Purpose

The goal is to use Codex as much as possible for structure, speed, and consistency while keeping final taste in human hands.

Codex should help reduce:

- random topic selection
- messy research
- blank-page scripting
- weak packaging
- avoidable production friction
- forgotten lessons after upload

The creator should still make the final call on:

- whether the topic is worth making
- whether the humor feels right
- which title and thumbnail actually win
- whether the final script sounds like `Why It Works`

## Before Starting

Before using this workflow, Codex should reload the core project docs and keep these decisions locked:

- Channel: `Why It Works`
- Language: `English`
- Format: `no-face explainer`
- Main audience lens: `English learners`
- Main lane: `money, internet, society, business, and modern life`
- Tone: `smart, simple, funny, dry`

If a workflow output starts pushing the channel outside those boundaries, stop and correct it before moving on.

Learner-friendly rule:

`Teach the topic first. Make the English easy to follow by design.`

Each script should use simple sentence structure, clear section signposts, visible keywords, and jokes that work from context. Do not turn the video into a grammar lesson unless the topic itself is language.

Before approving any future script, board plan, rough cut, or final review, use the channel-wide [English Learner Clarity System](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-clarity-system.md).

Create or update the active video folder before moving through the workflow:

```text
projects/<video-slug>/
```

Use [projects/_template](C:\ME\THINGS\Build a Channel\projects\_template) for the standard files.

## The Topic-To-Upload Workflow

### 1. Topic Intake

Goal:
Turn a messy list of possible ideas into sharp, scored angle candidates.

Use the project-local [Topic Intake skill](C:\ME\THINGS\Build a Channel\.agents\skills\topic-intake\SKILL.md) when the user asks for topic intake, next-video ideas, scored video angles, or step 1 of the workflow.

Codex does:

- cleans rough topic notes
- converts vague ideas into specific video angles using [topic-angle-selection-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-selection-system.md)
- writes a reusable angle package with topic, sharp angle, contradiction, recurring metaphor, thumbnail tension, first `10` seconds, WIT role, real-life objects, final insight, why now, and why this channel
- scores each candidate with [topic-angle-scorecard.md](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-scorecard.md)
- rejects or revises angles under `30/40` unless the user explicitly wants an experiment
- checks that `Curiosity`, `Visual motif`, `Explanation depth`, and `Packaging strength` are each at least `3/5`
- ranks the shortlist

Creator does:

- confirms which topic feels strongest right now
- rejects ideas that feel correct on paper but wrong in instinct

Output:

- one ranked list of scored angle candidates
- one recommended next angle
- one angle package for the chosen candidate after explicit video-project permission
- a short reason for the recommendation

Why this helps:

- reduces random topic picking
- keeps uploads aligned with the channel
- prevents scripting from starting from a broad, generic topic
- gives a repeatable way to choose what to make next

Example:

Input notes:

- free apps
- subscriptions
- people feel broke
- food delivery fees
- productivity scams

Codex output:

- `Why Free Apps Are Never Really Free`
  Strong hidden-system topic, high relevance, easy thumbnail promise, good English-first fit.
- `Why Everyone Feels Broke Now`
  Big emotional topic, broad appeal, but harder to explain cleanly in one video.
- `Why Productivity Content Never Fixes Your Life`
  Strong voice fit, high humor potential, slightly more opinion-sensitive.

Recommended choice:
`Why Free Apps Are Never Really Free`

Do not continue into research, packaging, hook writing, or scripting until the angle passes the scorecard or is explicitly labeled as an experiment.

## 2. Research Pack

Goal:
Compress scattered research into one useful explanation brief.

Codex does:

- gathers the core business logic behind the topic
- separates facts, interpretations, examples, and analogies
- identifies the simplest explanation structure
- collects supporting examples that are easy to visualize
- builds or prepares the future video reference board from [reference-board-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\reference-board-system.md) after explicit permission to work inside the video project
- lists real-life object, UI, visual metaphor, thumbnail tension, WIT emotion, and color/contrast references
- marks each saved reference as `safe asset`, `mockup target`, `inspiration only`, or `reject`
- writes source notes before using any saved, generated, or external reference in production

Creator does:

- checks whether the argument feels true and interesting
- removes examples that feel weak, dated, or overly niche

Output:

- one research brief with:
  - what people think
  - what is actually happening
  - why it keeps happening
  - useful examples
  - possible jokes or analogies
- one reference-board direction with:
  - main contradiction
  - recurring motif
  - thumbnail object
  - first `10` seconds visual clue
  - at least `5` possible visual jokes
  - source-note and safe-use decisions

Why this helps:

- avoids tab chaos
- makes the script easier to write
- reduces the chance of building the video around weak reasoning

Example:

Working thesis:
`Free apps rarely cost zero. They usually charge through attention, behavior, lock-in, ads, or delayed payment.`

Research pack structure:

- What people think:
  `Free apps are generous software products.`
- What is actually happening:
  `Free is often the entry price, not the real price.`
- Main business models:
  ad-supported, freemium, in-app purchases, subscriptions, data/network effects, lock-in
- Example products:
  YouTube, TikTok, Duolingo, mobile games, delivery apps
- Useful framing line:
  `If you are not paying money first, the app is probably charging you in behavior.`

## 3. Script Draft

Goal:
Turn the research into a usable first draft in the `Why It Works` structure.

Codex does:

- writes the hook
- keeps the first `10` seconds aligned with [hook-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\hook-system.md)
- writes the reframe
- builds the explanation in 3 to 5 chunks
- inserts humor beats
- keeps the English clear enough for intermediate learners
- marks `3-5` useful phrases using [english-learner-useful-phrase-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-useful-phrase-rules.md)
- checks script clarity with [english-learner-script-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-script-checklist.md)
- checks humor clarity with [english-learner-humor-clarity-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-humor-clarity-rules.md)
- lands on a clear payoff

Creator does:

- decides whether the draft feels sharp enough to keep
- marks boring sections, weak jokes, or missing insight

Output:

- one first-pass long-form script draft

Why this helps:

- kills blank-page paralysis
- keeps structure consistent
- moves effort from "starting" to "improving"

Example opening:

`Free apps are amazing. They help you chat, learn languages, order food, waste time, lose time, ruin your attention span, and occasionally pretend to improve your life. All for zero dollars. Which is either a miracle of modern technology or a sign that you are the product.`

Example reframe:

`This is not really a story about free software. It is a story about how the internet got very good at charging you without asking for money first.`

Example core structure:

1. Free usually means ad-supported
2. If ads are not enough, the app changes your behavior
3. The real business is habits, lock-in, and upsells

## 4. Voice Revision

Goal:
Make the script sound like `Why It Works`, not like a generic AI explainer.

Codex does:

- removes robotic phrasing
- shortens over-explained lines
- sharpens jokes
- removes unnecessary idioms or explains them through context
- checks that important terms are repeated and visually label-friendly
- checks tone against the channel rules
- tightens the payoff
- marks the narration copy with `[pause]`, `[beat]`, `[deadpan]`, `[slower]`, and `[emphasis]` where needed
- prepares the first `45-60` seconds for the channel voice test before full voiceover generation

Creator does:

- protects humor taste
- keeps only the lines that feel authentic
- rewrites anything that feels too clever or too fake
- listens to the short voice test and approves the pace before full generation

Output:

- one revised script that is cleaner, drier, and more human
- one marked narration test section when the script is ready for voiceover

Why this helps:

- protects brand voice
- avoids AI slop
- makes the channel feel authored

Example:

Weak version:
`Applications that use a freemium model often monetize users through premium feature conversion.`

Better version:
`The app is free right up until you want it to do something useful.`

## 5. Title And Thumbnail Flow

Goal:
Create packaging options before production is finished.

Codex does:

- generates several title angles
- pairs each title with a thumbnail concept
- explains why each combination might earn a click
- removes clever-but-unclear options

Creator does:

- chooses the title and image direction that feel strongest
- checks whether the promise matches the video honestly

Output:

- a title matrix
- thumbnail concepts
- a recommended packaging direction

Why this helps:

- improves click potential
- reduces last-minute guessing
- keeps packaging tied to the actual idea

Example title options:

- `Why Free Apps Are Never Really Free`
- `The Real Price Of Free Apps`
- `Free Apps Cost You More Than You Think`
- `Why "Free" On The Internet Is Usually Fake`

Example thumbnail concepts:

- phone screen with `FREE` peeling away to reveal `PAY HERE`
- app icons draining `time`, `attention`, and `money` through pipes
- a giant install button leading into a tunnel labeled `ads`, `subscriptions`, `data`

Recommended direction:
Use the clearest hidden-cost angle, not the most abstract one.

## 6. First 10 Seconds Hook Board

Goal:
Make sure the video opens as a curiosity event that pays off the chosen title-thumbnail pair.

Codex does:

- identifies the dominant object from the package
- identifies the main contradiction
- chooses WIT's emotional position
- fills a first `10` seconds hook board using [first-10-seconds-board-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\hook-templates\first-10-seconds-board-template.md)
- scores the hook with [hook-scorecard.md](C:\ME\THINGS\Build a Channel\.agents\_shared\hook-templates\hook-scorecard.md)
- rejects openings that start with branding, definitions, or neutral WIT

Creator does:

- confirms whether the opening feels immediately interesting
- rejects hooks that are clear but too calm

Output:

- one approved first `10` seconds hook board
- one hook score and required fixes

Working rule:

`Open with a situation, not an introduction.`

## 7. Production Checklist

Goal:
Turn the script into a no-face execution plan and a render-ready HyperFrames build.

Codex does:

- breaks the script into scenes
- maps each section to mostly static visuals
- suggests humor beats through handwritten labels, WIT poses, arrows, cross-outs, simple props, and hard cuts
- applies the channel scene grammar: one thought, one joke or evidence object, one WIT reaction or real-life anchor, one readable label, and one clean timing beat
- chooses reusable visual humor patterns before writing detailed boards
- creates an asset checklist
- checks board readability, WIT emotion, label timing, and cultural-reference clarity with [english-learner-visual-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\english-learner-visual-checklist.md)
- chooses from the reusable comedy asset inventory when the video needs hidden-payment objects, internet traps, modern-life pain props, red markup, WIT props, or a running motif
- checks the approved reference board for the recurring motif, real-life texture, UI mockup targets, thumbnail tension, WIT emotion, and at least `5` paused-frame jokes
- plans the real-life asset pass using [real-life-visual-asset-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\real-life-visual-asset-system.md)
- documents asset sources with [source-note-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\assets\source-note-template.md) or [comedy source-note-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\assets\comedy\source-note-template.md)
- creates or updates the HyperFrames composition
- runs the channel voice test before full voiceover generation
- copies or generates approved voiceover assets into the HyperFrames project
- selects `3` candidate music tracks and tests them under the first `30` seconds plus one dense explanation section
- adds only essential sound effects that support jokes, reveals, or system actions
- runs the audio mix checklist so narration stays clear for English learners
- creates a render checklist

Creator does:

- decides what is realistic to produce this week
- chooses or revises the preferred narrator voice
- trims visual ambition if it threatens consistency

Output:

- scene-by-scene plan
- HyperFrames source files
- voiceover files
- render-ready composition
- asset list
- edit checklist

Why this helps:

- makes no-face production less chaotic
- reduces time wasted figuring out visuals during editing
- improves repeatability

### Default HyperFrames Flow

Once the scene plan is approved:

1. turn the script into scene-level narration blocks
2. convert each narration block into static visual beats
3. choose one board function and one visual humor pattern per visual beat
4. use the approved reference board to list the recurring real-life objects, UI mockups, paper textures, thumbnail tension, WIT emotion, physical consequences, and reusable comedy motif candidates
5. choose `1` main comedy motif, `2-4` supporting comedy objects, `1` red markup style, and `1-2` WIT props from [comedy assets](C:\ME\THINGS\Build a Channel\.agents\_shared\assets\comedy)
6. add handwritten-looking labels, captions, arrows, red corrections, and punchline text
7. create or update `projects/<slug>/hyperframes/DESIGN.md`
8. create or update `projects/<slug>/hyperframes/index.html`
9. mark the narration copy using [script-markup-guide.md](C:\ME\THINGS\Build a Channel\.agents\_shared\voice\script-markup-guide.md)
10. run the first `45-60` seconds voice test using [voice-test-protocol.md](C:\ME\THINGS\Build a Channel\.agents\_shared\voice\voice-test-protocol.md)
11. generate full voiceover only after the voice test passes
12. copy voiceover, WIT, and approved media assets into `projects/<slug>/hyperframes/assets/`
13. choose `3` candidate music tracks using [music-and-sound-system.md](C:\ME\THINGS\Build a Channel\.agents\_shared\music-and-sound-system.md)
14. add only essential sound effects from safe sources or the reusable [sound-effects-library](C:\ME\THINGS\Build a Channel\.agents\_shared\sound-effects-library)
15. document asset and audio sources with safe-use decisions
16. run `npm run check`
17. preview timing with `npm run dev`
18. run the paused-frame review from [board-grammar.md](C:\ME\THINGS\Build a Channel\.agents\_shared\hyperframes\board-grammar.md)
19. run the audio clarity gate from [audio-mixing-checklist.md](C:\ME\THINGS\Build a Channel\.agents\_shared\audio-mixing-checklist.md)
20. render the review or final export with `npm run render`

This keeps visual source, voice timing, scene duration, and export logic inside the active video project.

HyperFrames should act as a video compiler and motion layer, not an excuse for heavy animation.
Use board scenes, WIT poses, hard cuts, simple GSAP entrances, cue-timed emphasis, red markup, real-life evidence objects, and handwritten text as the main visual language.

Example:

Scene 1:

- Voice:
  `Free apps are amazing...`
- Visual:
  cheerful app icons raining from the sky
- Joke beat:
  one icon lands on a person's head

Scene 2:

- Voice:
  `Which is either a miracle...`
- Visual:
  split screen between an angelic app and a shady salesman

Scene 3:

- Voice:
  `You are not paying with money first.`
- Visual:
  fake checkout page listing `attention`, `habits`, and `personal data`

## 8. Shorts Extraction

Goal:
Turn one long-form video into multiple short-form assets.

Codex does:

- finds the strongest short segments
- rewrites them so they stand alone
- creates short hooks and punchier endings
- formats them for shorts, reels, or clips

Creator does:

- decides which clips feel most native to short-form
- rejects clips that only make sense with long-form context

Output:

- 3 or more short-form scripts or cut candidates

Why this helps:

- increases output from the same research
- gives more surface area for growth
- makes the long video work harder

Example short angles:

- `Free apps are not free. They just bill you in weird currencies.`
- `If an app says free, it usually means we will charge you later when leaving becomes annoying.`
- `The internet's favorite trick is pretending the product is software when the real product is your behavior.`

## 9. Post-Upload Review

Goal:
Turn one upload into learning for the next one.

Codex does:

- uses [publishing-feedback-loop.md](C:\ME\THINGS\Build a Channel\.agents\_shared\publishing-feedback-loop.md)
- creates one short review from [post-upload-review-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\post-upload-review-template.md) for a future published video after explicit per-video permission
- logs the topic angle, title, thumbnail, hook promise, runtime, WIT role, and main visual motif
- tracks available metrics: impressions, CTR, views after `24h`, views after `7d`, average view duration, average percentage viewed, first `30s` retention, retention dips, traffic source, comments, repeated reactions, questions, confusion, and subs gained
- tracks qualitative signals when analytics are too small: thumbnail comparison, first `10` seconds strength, viewer feedback, English learner clarity, and production effort
- applies the Plan 14 decision rules for weak CTR, weak first `30s` retention, mid-video dips, viewer confusion, and production time
- labels lessons as `High`, `Medium`, or `Low` confidence
- promotes only reusable lessons through [channel-learning-rules.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel-learning-rules.md)
- writes channel-level lessons to `.agents/_shared/channel/learning-log.md` only when they are reusable beyond one video
- recommends one to three concrete next-video rules

Creator does:

- adds human judgment that analytics alone cannot capture
- decides whether a lesson is real or just noise
- confirms whether any low-confidence lesson should become an experiment
- confirms any core strategy change before `.agents/_shared/channel/channel-foundation.md` is touched

Output:

- one short review note
- one list of lessons
- one to three next-video rules
- optional reusable learning-log entry if the lesson is channel-wide

Why this helps:

- makes the channel compound instead of restart every week
- prevents the same mistakes from repeating
- improves future choices with evidence
- keeps weak signals from becoming strategy too early

Example review:

- Upload:
  `Why Free Apps Are Never Really Free`
- Likely strength:
  strong hidden-system promise
- Likely risk:
  retention dip if the business-model explanation gets too dense
- Likely lesson:
  viewers may respond well to internet topics where the hidden mechanism is simple and universal

Working rule:

`Measure the upload. Learn one useful thing. Change the next video.`

## Default Deliverables Per Video

For one chosen topic, Codex should aim to produce:

1. `00-idea.md`: topic scorecard and decision
2. `01-research.md`: research brief
3. `reference-board/`: topic-specific reference board copied from [.agents/_shared/reference-boards/_template](C:\ME\THINGS\Build a Channel\.agents\_shared\reference-boards\_template) after explicit permission
4. `02-script.md`: draft and revised script
5. `03-packaging.md`: title and thumbnail decision
6. `04-visual-plan.md`: scene-level visual plan
7. `05-production-board.md`: render-ready production plan
8. HyperFrames source, local assets, and voiceover files
9. 3 or more short-form cutdowns
10. `06-review.md`: render review and post-upload review using [post-upload-review-template.md](C:\ME\THINGS\Build a Channel\.agents\_shared\post-upload-review-template.md)

## Recommended Working Standard

Use this rule:

`Codex owns structure, speed, formatting, and reuse.`

`The creator owns taste, truth, and final judgment.`

If a draft is efficient but bland, it is not finished.

If a draft is polished but off-brand, it is not finished.

If a draft is smart but boring, it is not finished.

## Reusable Prompt Frame

When starting a new topic, use this exact production frame:

`Use the Why It Works workflow.`

`Topic: [insert topic]`

`Need:`

- topic angle check
- research brief
- reference-board direction
- script draft
- voice revision
- title and thumbnail options
- first `10` seconds hook board
- production checklist
- short-form cutdowns

`Keep it aligned with Why It Works: English-first, no-face, smart, simple, funny, dry.`

`Main audience lens: English learners who want interesting real-world English, not boring lessons.`

## First Suggested Use

This workflow is immediately useful for:

- `Why Everyone Feels Broke Now`
- `Why Free Apps Are Never Really Free`
- `Why Productivity Content Never Fixes Your Life`

These three topics already match the current channel foundation and are good candidates for testing the workflow end to end.
