# Why It Works Narration System

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
make every future `Why It Works` narration pass sound clear, dry, human, and easy for English learners without turning the channel into a lesson.

This system applies to future scripts, voice tests, and voiceover generation. It does not rewrite any existing video and does not require regenerating old voiceover.

## Core Target

Narration should feel like:

`a calm person explaining something ridiculous while refusing to act surprised`

The narrator is not a teacher, announcer, trailer voice, comedian, or corporate explainer.

The narrator is a clear young creator who has noticed that modern life is quietly absurd and is explaining it with controlled disappointment.

## Default Voice

Default narrator:

- Name: `David23`
- Voice source: `common/voice/david23/`
- Base TTS voice: `am_eric`
- Language: `en-us`
- Default long-form speed: `0.84`
- Careful learner test speed: `0.78`
- Slower learner-paced fallback: `0.76`
- Audition/sample speed: `1.10`

Use `0.84` as the first full-video candidate unless the voice test says the script needs more space.
Use `0.78` as the careful test variant when jokes or dense explanations feel rushed.
Use `0.76` only when clarity is more important than pace or the user explicitly asks for a slower learner-friendly cut.
Do not use `1.10` for full videos unless the user explicitly asks for a fast version.

Keep George and older candidate voices as fallback/reference voices. They are not the default channel voice.

## Priority Order

When tradeoffs appear, use this order:

1. Clear pronunciation
2. Learner-friendly pace
3. Deadpan joke timing
4. Natural human rhythm
5. Runtime target
6. Voice novelty

Do not speed up a script just to hit a runtime if the result becomes harder for English learners to follow.

## Delivery Shape

Most lines should follow this rhythm:

```text
setup -> small pause -> dry turn -> enough silence for the joke to land
```

Use this delivery map:

| Script moment | Delivery |
| --- | --- |
| Hook situation | clear, direct, slightly suspicious |
| Contradiction | slower, flatter, more precise |
| Explanation | clean and moderate, no fake excitement |
| Punchline | pause before it, say it plainly, do not overact |
| Key term | slight emphasis, not a dramatic hit |
| Final insight | slower and more grounded |
| Outro | short, dry, no big YouTuber energy |

## What The Voice Should Do

Use:

- calm confidence
- clean consonants
- short sentences
- plain English
- dry pauses
- mild skepticism
- underplayed punchlines
- clear section signposts
- repeated keywords that match on-screen labels

Avoid:

- sounding amazed by every point
- smiling through painful or absurd lines
- dramatic trailer energy
- overly sincere helpful-explainer tone
- fast native-speaker-only delivery
- dense idioms without context
- old, raspy, deep, or theatrical voice choices unless explicitly approved
- copying Casually Explained's exact voice or persona

## Deadpan Rules

Deadpan does not mean bored.

Deadpan means:

- the line is funny because the situation is ridiculous
- the narrator says it like a normal fact
- the visual and pause carry the joke
- the voice does not explain that it is a joke

Good delivery:

```text
The app is free. [pause]
Which is nice, because apparently your attention has a payment plan. [beat]
```

Bad delivery:

```text
The app is FREE! And now here comes the hilarious twist!
```

## Learner Clarity Rules

For English learners:

- prefer `common word -> useful term`, not `useful term -> explanation later`
- repeat key nouns exactly when they matter
- avoid long noun stacks
- keep one sentence to one idea
- slow down when introducing a new abstract word
- let labels stay visible long enough to read
- do not bury the main meaning inside sarcasm

Working rule:

`The viewer should understand the point even if they miss one joke.`

## Narration-To-Board Timing Rules

Voiceover is the timing source for HyperFrames boards.

Use these defaults unless a specific scene needs different timing:

- A key joke label appears on the punchline word or up to `0.15s` before it.
- A visual punchline should not appear more than `0.25s` before the spoken punchline.
- Cue-critical text must be readable on the spoken cue frame, not merely beginning an animation.
- A board cut should not interrupt a key word, phrase, or final insight.
- A `[pause]` should create enough space for the next visual idea to register.
- A `[beat]` should create enough space for WIT, red markup, or a hard cut to land.
- Dense explanation sections need fewer competing visual changes.
- Final insight lines need extra breathing room; do not rush the last `10-15` seconds.

When in doubt:

`late but readable` is better than `early and spoiled`.

## Full Voiceover Gate

Do not generate full voiceover until:

- the script is locked enough for narration
- the script has been marked with [script-markup-guide.md](script-markup-guide.md)
- the first `45-60` seconds have passed [voice-test-protocol.md](voice-test-protocol.md)
- the first `10` seconds still work against the hook board
- the chosen pace leaves room for labels and punchlines

## Acceptance Criteria

Narration is ready when:

- the voice is easy to understand without subtitles
- the first `30` seconds feels like a real creator, not a tutorial
- jokes have breathing room
- punchlines sound underplayed, not performed
- dense points are slower and cleaner
- board cuts can follow the voice naturally
- on-screen labels can be read by intermediate English learners
- the voice never sounds corporate, old, raspy, or overly dramatic

If the voice fails, fix the markup, pace, or script before generating the full video.
