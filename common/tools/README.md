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
| HyperFrames CLI | `video-projects/<slug>/hyperframes/package.json` | Preview, check, and render video compositions |
| HyperFrames source | `video-projects/<slug>/hyperframes/index.html` | HTML/CSS/GSAP video source |
| HyperFrames design brief | `video-projects/<slug>/hyperframes/DESIGN.md` | Visual identity source for the composition |
| Legacy ElevenLabs voiceover generator | `remotion-studio/scripts/generate-voiceover.mjs` | Generate MP3 narration per scene until a new voice pipeline replaces it |

## Tool Notes

- [voiceover.md](C:\ME\THINGS\Build a Channel\common\tools\voiceover.md)
- [image-generation.md](C:\ME\THINGS\Build a Channel\common\tools\image-generation.md)
- [video-generation.md](C:\ME\THINGS\Build a Channel\common\tools\video-generation.md)

## Future Tool Slots

- image generation workflow
- thumbnail generation workflow
- local asset optimization
- script-to-HyperFrames conversion
- video QA checklist runner
