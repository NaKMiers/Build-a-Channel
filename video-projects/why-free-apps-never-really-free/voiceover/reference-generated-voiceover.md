# Reference-Generated Voiceover

Status: `Generated`

Date: `2026-05-31`

Purpose:
replace the previous `George` narration with a local reference-voice generation based on:

```text
video-projects/why-free-apps-never-really-free/voiceover/reference/reference-voiceover.m4a
```

## Output

Archive/source output:

```text
video-projects/why-free-apps-never-really-free/voiceover/reference-generated/
```

Active HyperFrames output:

```text
video-projects/why-free-apps-never-really-free/hyperframes/assets/voiceover/
```

The active HyperFrames audio files keep the same filenames as the previous George clips, so the existing HTML layout and audio references were not rewritten.

## Scene Files

| Scene | Target duration | MP3 duration |
|---|---:|---:|
| `free-gifts.mp3` | `23.17s` | `23.23s` |
| `pricing-reframe.mp3` | `43.65s` | `43.70s` |
| `attention-ads.mp3` | `38.77s` | `38.83s` |
| `behavior-habit.mp3` | `28.24s` | `28.30s` |
| `freemium-pain.mp3` | `21.21s` | `21.26s` |
| `lock-in.mp3` | `21.26s` | `21.31s` |
| `label-stack.mp3` | `22.39s` | `22.44s` |
| `hidden-checkout.mp3` | `41.22s` | `41.28s` |

Note:
the `~0.05s` difference is MP3 encoder padding. The audio was generated and stretched to the original target durations before MP3 encoding.

## Workflow Note

Generation used local Chatterbox TTS with the reference recording as the voice prompt. No HyperFrames layout HTML was edited for this voice replacement.
