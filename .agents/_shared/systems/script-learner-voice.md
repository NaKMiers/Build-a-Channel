# Script, Learner, And Voice System

Classification: `Core production system`

Scope: `CHANNEL_WIDE`

Use this file for script drafting, English learner clarity, useful phrase choices, narration markup, and voiceover generation.

## Core Rule

Teach the topic first. Make the English learner-friendly by design.

The viewer should come for the topic and leave with better English.

## Script Shape

Default long-form structure:

1. Hook
2. Reframe
3. Explain in `3-5` chunks
4. Add humor throughout
5. Reinforce a few useful English phrases naturally
6. End with the real payoff

## Voice

The voice should be:

- clear
- conversational
- easy to follow for intermediate English learners
- lightly dry
- slightly skeptical
- funny without trying too hard
- smart without sounding elite

Avoid:

- academic tone
- too much slang
- dense idioms without context
- fake-deep statements
- motivational shouting
- corporate explainer language

Narration direction:

`a calm person explaining something ridiculous while refusing to act surprised`

## Sentence Rules

Use:

- short sentences
- common words before fancy words
- clear signposts
- repeated key phrases
- concrete examples from daily life
- visible keywords on screen

Avoid:

- long abstract explanations
- fast topic jumps
- jokes that only work for native cultural knowledge
- vocabulary-teaching interruptions that break entertainment flow

## Humor Rules

Good joke sources:

- suspicious normal things
- fake serious labels
- WIT suffering from invisible systems
- red corrections
- literal diagrams of dumb incentives
- everyday examples becoming absurd

The joke must support clarity.

Working rule:

`The viewer should understand the point even if they miss one joke.`

## Useful Phrase Layer

Optional target: `3-5` useful phrases per video.

Good phrases:

- are natural in the script
- help explain the topic
- are useful outside the video
- are easy to show on screen

Bad phrases:

- interrupt the story
- feel like vocabulary homework
- are too rare or academic
- are only included because they sound advanced

## Script Approval Checks

Before approving a script, check:

- one clear topic question
- one clear contradiction
- one clean section structure
- every section has a visual job
- important claims are safe and sourceable
- jokes work from context
- key terms are introduced simply
- dense lines have `[pause]`, `[beat]`, or `[slower]`

## Narration Markup

Use markup sparingly:

- `[pause]` for real breathing room
- `[beat]` before or after a joke
- `[deadpan]` for dry lines
- `[slower]` for dense explanations
- `[emphasis]` for important words

Do not over-mark normal sentences.

## Default Narrator

Default channel narrator:

- Name: `David23`
- Voice ID: `am_eric`
- Language: `en-us`
- Balanced speed: `0.84`
- Careful learner speed: `0.78`
- Slower fallback: `0.76`

Use `am_eric` directly even if a short voice list does not show it.

Working command pattern:

```text
npx hyperframes@0.6.76 tts <input.txt> --output <output.mp3> --voice am_eric --speed 0.84 --lang en-us --json
```

## Voiceover Rules

- Test the first `45-60` seconds before full generation.
- Prefer section-level voiceover files.
- When the user asks for `All`, generate separate section outputs, not one stitched full-video file.
- Keep one useful MP3 preview per section by default.
- Use temporary files only when needed, then remove them.
- Do not silently fall back to another voice when David23 is requested.

