# Tools

This folder documents reusable tools used by the channel.

Tool rules:

- keep video-specific inputs inside `projects/<slug>/`
- keep reusable scripts, prompts, and operating notes here
- never store API keys here
- document command inputs and outputs clearly

## Current Tools

| Tool | Current Location | Purpose |
|---|---|---|
| HyperFrames CLI | `projects/<slug>/hyperframes/package.json` | Preview, check, and render video compositions |
| HyperFrames source | `projects/<slug>/hyperframes/index.html` | HTML/CSS/GSAP video source |
| HyperFrames design brief | `projects/<slug>/hyperframes/DESIGN.md` | Visual identity source for the composition |
| Historical ElevenLabs voiceover generator | `remotion-studio/scripts/generate-voiceover.mjs` | Legacy reference only unless the old app is restored |

## Tool Notes

- [voiceover.md](C:\ME\THINGS\Build a Channel\.agents\_shared\tools\voiceover.md)
- [image-generation.md](C:\ME\THINGS\Build a Channel\.agents\_shared\tools\image-generation.md)
- [video-generation.md](C:\ME\THINGS\Build a Channel\.agents\_shared\tools\video-generation.md)

## Future Tool Slots

- image generation workflow
- thumbnail generation workflow
- local asset optimization
- script-to-HyperFrames conversion
- video QA checklist runner
