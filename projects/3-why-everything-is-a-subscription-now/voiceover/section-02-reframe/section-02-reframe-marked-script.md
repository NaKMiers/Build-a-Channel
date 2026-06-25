# Section 2 Marked Script — Reframe: You Stopped Buying, You Started Renting

Marked for delivery only. The `**bold**` joke markers and `[beat]/[deadpan]/[slower]`
cues are NOT spoken — they are stripped before TTS. Real audio pacing is created by
shaping the line breaks in `tts-inputs/section-02-reframe-tts.txt` (Kokoro has no SSML).

```text
Now — this is not a video about how subscriptions are evil and you should throw your phone in a lake. Some are genuinely useful. Calm down.

This is about something weirder.

We used to own things. You paid once, the thing was yours, the end. A beautiful, boring transaction.

A subscription is different. You don't buy the thing. You rent access to it. Pay every month, the screen turns on. Miss a payment, and your own device does this — [beat] — a little padlock appears, and it looks at you like a disappointed parent.

So here's the real question. How did almost everything — your apps, your shows, your software, even buttons inside your car — quietly turn into stuff you rent instead of stuff you own?
```

## Delivery intent (from 02-script.md voice revision notes)

- `[beat]` before "a little padlock appears" so the visual lands first.
- Keep "Some are genuinely useful. Calm down." light and quick — it defuses the "subscriptions are evil" reaction.
- The closing line is the real question the rest of the video answers; let it breathe.

## How the intent is realized in the TTS input (Kokoro technique)

MEASURED on this build (2026-06-23): line breaks and commas do NOT create pauses — newlines are
flattened before synthesis. Pause strength: ellipsis `...` > period `.` > em dash `—` > comma ≈ none.
The line layout is for readability only; the real pauses come from periods and the ellipsis.

- An ellipsis on "...does this..." holds before the padlock reveal (realizes the `[beat]`) — this is
  the lever that actually works.
- Periods give the sentence stops; commas and line breaks do not add timing.
- For a longer/dramatic silence, add it at the render stage — text punctuation can't.
