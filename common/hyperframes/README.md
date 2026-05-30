# HyperFrames System

This folder stores shared HyperFrames conventions for `Why It Works`.

HyperFrames is now the default production and render path for channel videos.

## Current Model

- Each active video keeps its HyperFrames source in `video-projects/<slug>/hyperframes/`.
- Each HyperFrames project must include a `DESIGN.md` before composition work.
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
- Use transitions between scenes.
- Use entrance animations for scene elements.
- Do not use Remotion for new production unless the user explicitly asks.
- Keep `remotion-studio/` unchanged until the user asks to delete it.

## Current Active Example

```text
video-projects/why-free-apps-never-really-free/hyperframes/
```

This is the migration target for the first `Why It Works` rough cut.
