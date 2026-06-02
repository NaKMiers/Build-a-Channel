# HyperFrames System

This folder stores shared HyperFrames conventions for `Why It Works`.

HyperFrames is now the default production and render path for channel videos.

## Current Model

- Each active video keeps its HyperFrames source in `video-projects/<slug>/hyperframes/`.
- Each HyperFrames project must include a `DESIGN.md` before composition work.
- Future HyperFrames boards should follow [board-grammar.md](board-grammar.md) for naming, timing, cue-critical emphasis, and paused-frame review.
- Future voiceover timing should follow [../voice/narration-system.md](../voice/narration-system.md), [../voice/script-markup-guide.md](../voice/script-markup-guide.md), and [../voice/voice-test-protocol.md](../voice/voice-test-protocol.md).
- Future music, sound effects, and mix checks should follow [../music-and-sound-system.md](../music-and-sound-system.md), [../sound-effects-library/README.md](../sound-effects-library/README.md), and [../audio-mixing-checklist.md](../audio-mixing-checklist.md).
- Voiceover, WIT poses, and one-off media should be copied into the video project's `hyperframes/assets/` folder so renders are self-contained.
- Final and review MP4s still belong in `video-projects/<slug>/renders/`.

## Current Commands

Run from a video HyperFrames folder:

```powershell
npm run dev
npm run check
npm run render
```

For direct CLI use:

```powershell
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
npx hyperframes render --quality draft
```

If rendering cannot find FFmpeg, add the local `ffmpeg-static` folder to `PATH` for that command or install FFmpeg globally.

## Production Rules

- Build the final visible layout first, then animate into it with GSAP.
- Register every timeline in `window.__timelines`.
- Use deterministic animation only; no random or time-based logic.
- Use mostly static board scenes, cue-timed labels, red markup, WIT reactions, real-life evidence objects, and hard cuts.
- Treat voiceover as the timing source: key labels should land on or just before the spoken cue, and punchlines should not appear early.
- Treat narration as the top audio layer: music stays low, ducks under dense explanation, and can disappear for dry punchlines.
- Use sound effects only for essential joke, reveal, or system-action cues; avoid effects on ordinary cuts or every text reveal.
- Use transitions only when they clarify the idea or land a joke.
- Use entrance animations only for scene elements that need a readable cue.
- Check paused frames before review renders: every sampled frame should have a joke, contradiction, or clear evidence.
- Do not use Remotion for new production unless the user explicitly asks.
- Keep `remotion-studio/` unchanged until the user asks to delete it.

## Current Active Example

```text
video-projects/why-free-apps-never-really-free/hyperframes/
```

This is the migration target for the first `Why It Works` rough cut.
