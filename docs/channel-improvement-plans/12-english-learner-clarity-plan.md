# Plan 12: English Learner Clarity

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide English learner clarity system so humor and roughness never break the channel's main audience lens: English learners who want interesting real-world English.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable English learner clarity system for the entire channel. It must not audit or rewrite any specific video script.

Allowed outputs:

- `common/english-learner-clarity-system.md`
- `common/english-learner-script-checklist.md`
- `common/english-learner-visual-checklist.md`

Forbidden outputs:

- no edits to `video-projects/<slug>/`
- no audit of a specific video script unless explicitly requested

Source insight:
The channel should borrow Casually Explained's roughness, deadpan rhythm, visual jokes, and real-world texture, but not its most native-speaker-dependent density. The viewer should come for the topic and leave with better English.

## Problem

When improving humor, the channel can accidentally become:

- too fast
- too slang-heavy
- too culturally obscure
- too visually chaotic
- too dependent on sarcasm
- too hard to follow without native-level listening

That would damage the channel's actual position.

The channel is not a formal English lesson, but English learner clarity is a product feature.

## Target

Every video should feel like:

`interesting English-native YouTube that an intermediate learner can actually follow`

not:

`an English lesson`

and not:

`a native-speaker meme video that learners cannot decode`

## Script Rules

Use:

- short sentences
- common words first
- repeated key phrases
- concrete examples
- clear section transitions
- jokes that work from the visible situation
- occasional useful phrases naturally repeated

Avoid:

- stacked idioms
- long abstract sentences
- joke references that require deep US/UK internet context
- sarcasm where the literal meaning says the opposite of the real point
- fast pivots with no signposting
- unexplained acronyms

## Useful Phrase Layer

Each video may highlight `3-5` useful phrases naturally.

Examples:

- `not really free`
- `hidden cost`
- `easy entry`
- `the long game`
- `somewhere less visible`
- `part of your day`
- `moving house`

Rules:

- Do not stop the video to teach vocabulary.
- Put the phrase on screen when it helps the joke or structure.
- Repeat important phrases in different sections.
- Keep the phrase useful outside the video.

## Visual Clarity Rules

For English learners, visuals should carry meaning.

Use:

- one main idea per board
- short labels
- visible arrows
- repeated symbols
- clear WIT emotion
- real-life objects that explain the context

Avoid:

- dense screens
- tiny labels
- multiple jokes competing at once
- fast text changes during difficult narration
- visual references that require cultural explanation

## Voice And Pacing Rules

Narration should:

- be clear before it is stylish
- use moderate speed
- pause before key ideas
- leave time to read short labels
- pronounce key terms cleanly

For full videos:

- test the first `45-60` seconds before full voice generation
- check whether the pace still works at `0.9x` viewer comprehension, not only native-speed listening
- avoid speeding up just to hit runtime

## Humor Clarity Rules

Good learner-friendly jokes:

- come from visible contradiction
- use simple words
- rely on the situation
- repeat a phrase with a twist
- make WIT's reaction obvious

Risky jokes:

- mostly wordplay
- mostly slang
- mostly references
- mostly sarcasm without visual support
- too many ideas in one sentence

## Review Checklist

For every script:

- Can the main point be understood without the joke?
- Does each section have one simple label?
- Are key phrases repeated?
- Are any sentences longer than needed?
- Are jokes visible, not only verbal?
- Would an intermediate learner understand the final lesson?

For every rough cut:

- Watch without subtitles.
- Watch with subtitles.
- Watch at mobile size.
- Pause every `10` seconds and check if the visual helps the spoken idea.
- Mark moments where the viewer must understand a hidden cultural reference.

## Acceptance Criteria

English learner clarity passes if:

- the topic is understandable on first watch
- the final insight is easy to repeat
- on-screen labels support listening
- jokes do not hide the explanation
- voice remains clear
- the video still feels entertaining, not like a class

## Do Not Do

- Do not make the channel a grammar lesson.
- Do not explain every joke.
- Do not remove all personality for clarity.
- Do not use advanced vocabulary just to sound smart.
- Do not copy native-speaker sarcasm if learners cannot decode it from visuals.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/12-english-learner-clarity-plan.md.
Create or update the channel-wide English learner clarity system.
Allowed outputs are common/english-learner-clarity-system.md and common learner checklists.
Do not edit video-projects.
Do not audit a specific script unless I explicitly ask.
```
