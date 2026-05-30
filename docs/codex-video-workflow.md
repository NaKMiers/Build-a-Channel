# Codex Video Workflow

This document turns the `Why Free Apps Are Never Really Free` example into a reusable operating workflow for `Why It Works`.

It is an execution workflow, not a change to channel strategy.

Use it when turning a topic idea into:

- a research pack
- a script draft
- packaging options
- a production checklist
- short-form cutdowns
- a post-upload review

## Default Production Stack

The current default production path for `Why It Works` is:

- per-video planning in `video-projects/<slug>/`
- reusable tools, templates, and local project skills in `common/`
- HyperFrames scene assembly in `video-projects/<slug>/hyperframes/`
- per-video `DESIGN.md`, `index.html`, local audio, and local assets under the HyperFrames project
- HyperFrames timing driven by audio clips, `data-start`, `data-duration`, and GSAP timelines
- handwritten-looking text rendered in HyperFrames for labels, captions, arrows, corrections, and punchlines

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

Create or update the active video folder before moving through the workflow:

```text
video-projects/<video-slug>/
```

Use [video-projects/_template](C:\ME\THINGS\Build a Channel\video-projects\_template) for the standard files.

## The 8-Stage Workflow

### 1. Topic Intake

Goal:
Turn a messy list of possible ideas into ranked video candidates.

Codex does:

- cleans rough topic notes
- converts vague ideas into specific video angles
- scores each idea for brand fit, curiosity, clarity, thumbnail potential, and production difficulty
- ranks the shortlist

Creator does:

- confirms which topic feels strongest right now
- rejects ideas that feel correct on paper but wrong in instinct

Output:

- one ranked list
- one recommended next topic
- a short reason for the recommendation

Why this helps:

- reduces random topic picking
- keeps uploads aligned with the channel
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

## 2. Research Pack

Goal:
Compress scattered research into one useful explanation brief.

Codex does:

- gathers the core business logic behind the topic
- separates facts, interpretations, examples, and analogies
- identifies the simplest explanation structure
- collects supporting examples that are easy to visualize

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
- writes the reframe
- builds the explanation in 3 to 5 chunks
- inserts humor beats
- keeps the English clear enough for intermediate learners
- marks 3 to 5 useful phrases that can become on-screen keywords
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

Creator does:

- protects humor taste
- keeps only the lines that feel authentic
- rewrites anything that feels too clever or too fake

Output:

- one revised script that is cleaner, drier, and more human

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

## 6. Production Checklist

Goal:
Turn the script into a no-face execution plan and a render-ready HyperFrames build.

Codex does:

- breaks the script into scenes
- maps each section to mostly static visuals
- suggests humor beats through handwritten labels, WIT poses, arrows, cross-outs, simple props, and hard cuts
- creates an asset checklist
- creates or updates the HyperFrames composition
- copies or generates voiceover assets into the HyperFrames project
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
3. add handwritten-looking labels, captions, arrows, and punchline text
4. create or update `video-projects/<slug>/hyperframes/DESIGN.md`
5. create or update `video-projects/<slug>/hyperframes/index.html`
6. copy voiceover and WIT/media assets into `video-projects/<slug>/hyperframes/assets/`
7. run `npm run check`
8. preview timing with `npm run dev`
9. render the review or final export with `npm run render`

This keeps visual source, voice timing, scene duration, and export logic inside the active video project.

HyperFrames should act as a video compiler and motion layer, not an excuse for heavy animation.
Use board scenes, WIT poses, transitions, simple GSAP entrances, cue-timed emphasis, and handwritten text as the main visual language.

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

## 7. Shorts Extraction

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

## 8. Post-Upload Review

Goal:
Turn one upload into learning for the next one.

Codex does:

- logs the topic, title, hook, runtime, and thumbnail direction
- reviews what likely helped or hurt performance
- compares the video against prior uploads
- writes the lesson back into project memory

Creator does:

- adds human judgment that analytics alone cannot capture
- decides whether a lesson is real or just noise

Output:

- one short review note
- one list of lessons
- one recommendation for the next topic or packaging test

Why this helps:

- makes the channel compound instead of restart every week
- prevents the same mistakes from repeating
- improves future choices with evidence

Example review:

- Upload:
  `Why Free Apps Are Never Really Free`
- Likely strength:
  strong hidden-system promise
- Likely risk:
  retention dip if the business-model explanation gets too dense
- Likely lesson:
  viewers may respond well to internet topics where the hidden mechanism is simple and universal

## Default Deliverables Per Video

For one chosen topic, Codex should aim to produce:

1. `00-idea.md`: topic scorecard and decision
2. `01-research.md`: research brief
3. `02-script.md`: draft and revised script
4. `03-packaging.md`: title and thumbnail decision
5. `04-visual-plan.md`: scene-level visual plan
6. `05-production-board.md`: render-ready production plan
7. HyperFrames source, local assets, and voiceover files
8. 3 or more short-form cutdowns
9. `06-review.md`: render and post-upload review

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
- script draft
- voice revision
- title and thumbnail options
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
