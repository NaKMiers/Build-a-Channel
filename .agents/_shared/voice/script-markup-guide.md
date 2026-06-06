# Script Markup Guide

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
prepare future `Why It Works` scripts for clear, dry, learner-friendly narration before generating voiceover.

This guide applies after the script is revised for tone and before any full voiceover generation.

## Core Rule

Markup should protect rhythm, clarity, and joke timing.

It should not decorate every line.

Use tags only where the voice, pause, emphasis, or visual timing would otherwise be ambiguous.

## Approved Tags

| Tag | Meaning | Use when |
| --- | --- | --- |
| `[pause]` | short listening pause | the next line changes idea or needs a tiny breath |
| `[beat]` | punchline/reaction beat | a joke, WIT reaction, red correction, or hard cut needs space |
| `[deadpan]` | flatter delivery | a funny line should sound like a normal fact |
| `[slower]` | extra learner clarity | a dense explanation, key term, or final insight needs space |
| `[emphasis]` | light stress on a key word | the word must match an on-screen label or idea |

Optional specific form:

```text
[emphasis: attention]
```

Use this when only one word inside a line should be stressed.

## Tag Meanings

### `[pause]`

Use for a short pause between related ideas.

Best for:

- after a setup line
- before a reframe
- before a concrete example
- after a repeated phrase

Example:

```text
Free apps are not lying. [pause]
They are just very patient.
```

Do not use `[pause]` after every sentence. That makes the voice sound robotic.

### `[beat]`

Use for the joke landing space.

Best for:

- after a punchline
- before a hard cut
- when WIT needs a silent reaction
- after a red correction or visual reveal

Example:

```text
The subscription is only five dollars. [pause]
Which is how they get you twelve times. [beat]
```

`[beat]` should usually be longer than `[pause]`.

### `[deadpan]`

Use when a line should be flatter and less sincere.

Best for:

- fake-serious definitions
- absurd lines stated like facts
- dry corrections
- lines where overacting would ruin the joke

Example:

```text
[deadpan] This is technically called convenience.
```

Do not use `[deadpan]` to make the whole video lifeless. Use it on selected lines.

### `[slower]`

Use when comprehension matters more than pace.

Best for:

- the main thesis
- new terms
- numbers
- cause-and-effect lines
- final insight
- English learner pressure points

Example:

```text
[slower] If you are not paying with money first, the app may be charging you with attention.
```

Do not use `[slower]` to rescue an over-dense sentence. Shorten the sentence first.

### `[emphasis]`

Use for light stress, not dramatic shouting.

Best for:

- a repeated keyword
- a title/thumbnail promise word
- a label that appears on screen
- a contrast word such as `free`, `attention`, `rent`, `habit`, or `lock-in`

Example:

```text
The important word is not [emphasis] free.
It is [emphasis] later.
```

If a word is emphasized in voice, the visual should usually support it with a label, underline, highlight, or red correction.

## Markup Workflow

Use this pass order:

1. Read the script aloud once without tags.
2. Mark only the hook, reframe, punchlines, key terms, and final insight.
3. Add `[pause]` before idea turns.
4. Add `[beat]` after punchlines that need WIT, red markup, or silence.
5. Add `[deadpan]` only to lines that should be flatter.
6. Add `[slower]` to dense or important lines.
7. Add `[emphasis]` to words that need visual sync.
8. Read it aloud again and remove any tag that feels fussy.

## Line Rules

Keep narration lines short.

Preferred:

```text
The app is free. [pause]
The patience is not. [beat]
```

Avoid:

```text
The app is free, but the patience, monetization strategy, long-term behavioral loop, and eventual payment path are all designed to extract value from you later.
```

Before adding markup, fix sentences that are:

- too long
- too abstract
- too idiom-heavy
- too full of commas
- too dependent on native cultural knowledge
- hard to picture as a board

## Visual Sync Rules

Every `[emphasis]` tag should answer:

- What appears on screen?
- Does the label arrive on the word or just before it?
- Does the viewer have enough time to read it?

Every `[beat]` tag should answer:

- What is the visual payoff?
- Does WIT react during the silence?
- Is the joke spoiled by appearing too early?

Every `[slower]` tag should answer:

- What might an English learner miss?
- Can the sentence be split instead?
- Does the board stay calm enough to follow?

## Example Marked Script

```text
Free apps are amazing. [pause]
They help you talk to friends, learn a language, order food, and lose an entire evening by accident.

[deadpan] Very generous behavior from a rectangle.

But the important word is not [emphasis] free. [pause]
It is [emphasis] later. [beat]

[slower] If the app does not charge you with money first, it usually charges you with attention, habits, or time.
```

## Markup Checklist

A script is ready for a voice test when:

- the first `45-60` seconds have clear pause and beat tags
- every punchline has either `[beat]` or an intentional immediate cut
- every dense explanation has been shortened or marked `[slower]`
- every key on-screen word has an `[emphasis]` plan
- no paragraph has become tag soup
- the script still sounds like a person when read aloud

If the script needs tags on every line to work, the writing is not ready.
