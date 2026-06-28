# Section 1 Marked Script - Hook: It's More Than You Think

Marked for delivery only. The `**bold**` joke markers and `[beat]/[deadpan]/[slower]`
cues are NOT spoken - they are stripped before TTS. Real audio pacing is created by
shaping the line breaks in `tts-inputs/section-01-hook-tts.txt` (Kokoro has no SSML).

```text
Quick question. [beat] How many subscriptions are you paying for right now?

[beat] Whatever number you guessed... it's higher. It's always higher.

Right now, money is quietly leaving your account every month - for stuff you forgot you own. An app. A "free" trial that stopped being free. A show you watched once.

[deadpan] Your free trial of owning things just expired.

You don't buy things anymore. [slower] You rent your whole life. One payment at a time.
```

## Delivery intent (from 02-script.md voice revision notes)

- `[beat]` after "Quick question." and before "Whatever number you guessed" so the question hangs.
- `[deadpan]` flat on the pop-up joke line "Your free trial of owning things just expired."
- `[slower]` on the final two short lines so the thesis lands.

## How the intent is realized in the TTS input (Kokoro technique)

MEASURED on this build (2026-06-23): line breaks and commas do NOT create pauses - newlines are
flattened before synthesis. Pause strength: ellipsis `...` > period `.` > em dash `-` > comma ≈ none.
So the line layout below is for human readability; the actual pauses come from the periods and the
ellipsis.

- An ellipsis `...` before "it's higher" holds the punchline (the strongest text pause available).
- Periods between the short lines give the natural sentence stops.
- For a longer/dramatic silence, add it at the render stage - text punctuation can't.
- Em dash converted to a comma in the input for clean TTS phrasing.
