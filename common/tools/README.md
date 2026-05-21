# Tools

This folder documents reusable tools used by the channel.

Tool rules:

- keep video-specific inputs inside `video-projects/<slug>/`
- keep reusable scripts, prompts, and operating notes here
- never store API keys here
- document command inputs and outputs clearly

## Current Tools

| Tool | Current Location | Purpose |
|---|---|---|
| ElevenLabs voiceover generator | `remotion-studio/scripts/generate-voiceover.mjs` | Generate MP3 narration per scene |
| ElevenLabs voice list | `remotion-studio/scripts/list-elevenlabs-voices.mjs` | Inspect available narrator voices |
| Remotion render commands | `remotion-studio/package.json` | Preview and render video compositions |

## Tool Notes

- [voiceover.md](C:\ME\THINGS\Build a Channel\common\tools\voiceover.md)
- [image-generation.md](C:\ME\THINGS\Build a Channel\common\tools\image-generation.md)
- [video-generation.md](C:\ME\THINGS\Build a Channel\common\tools\video-generation.md)

## Future Tool Slots

- image generation workflow
- thumbnail generation workflow
- local asset optimization
- script-to-scene conversion
- video QA checklist runner
