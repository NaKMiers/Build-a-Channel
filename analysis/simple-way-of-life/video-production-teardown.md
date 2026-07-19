# How Simple Ways of Life actually makes a video (evidence-based teardown)

Date: 2026-07-18 · Method: downloaded the 427K breakout video (`pfefmXY7VL0`, 12m19s) at 480p with yt-dlp, probed with ffprobe, extracted frame contact sheets + audio analysis with ffmpeg. Not a guess - measured.

## What the evidence shows

### Visuals: a slideshow of consistent monochrome doodles

- **Style:** black line-drawing on a plain white background. Every scene = one central stick figure + satellite icons in circles + arrows. One single consistent line style across the whole video (and, from thumbnails, the whole channel).
- **Cadence:** ~12 distinct images in the first 60s = **roughly one image change every ~5 seconds.** Images are HELD, not rapid-cut.
- **Motion:** essentially none. Scene-change detection found ~0 hard cuts even at a low threshold; frames within each held image differ only by a slow scale drift = a **slow zoom / Ken Burns pan** with soft crossfades. No character animation, no moving parts.
- **On-screen text: none** in the body. The video carries meaning through narration + illustration only (text lives on the thumbnail, not in the video).

### Audio: bare voiceover, NO music

- Clean, regular phrase gaps (0.4-1.0s of near-silence between sentences) - the signature of a scripted read, consistent with TTS / AI voice (e.g. ElevenLabs).
- Noise floor inside a speech gap: **-66.8 dB mean** = effectively pure silence. **There is NO background music bed at all.** A 427K self-help video is just voice + doodles + silence between phrases.

### Specs

- 480p/30fps available (source likely 1080p), AV1 + Opus, 12m19s.

## The likely production pipeline (confidence noted)

1. **Script:** AI-assisted writing, then a tight scripted read (high confidence it's scripted; AI-written is plausible).
2. **Voiceover:** single AI/TTS voice, clean pauses, no music. (High confidence it's a clean scripted VO; ElevenLabs-class TTS is the likely tool.)
3. **Visuals:** a consistent monochrome doodle set. Most likely a **whiteboard/doodle asset library or tool** (the central-figure + satellite-icons + arrows composition is a classic doodle-tool template), OR a consistent style-locked image generator. NOT bespoke per-scene art, NOT AI photo-real. (Medium confidence on the exact tool; high confidence the style is one reusable consistent set.)
4. **Assembly:** drop each doodle onto the timeline for ~5s, add a slow zoom + soft crossfade, lay the VO on top. A basic editor (CapCut / Wink / similar) is entirely sufficient. No compositing, no per-sentence timing, no text overlays.

## Why this matters for Why It Works

- **Their whole video is far SIMPLER than what Why It Works currently builds.** WIT uses HyperFrames per-sentence compositing, WIT pose swaps, animated interactive UI mockups, real-photo backgrounds, and beat-synced labels. Simple Ways of Life hit 427K with: held doodles, slow zooms, a clean voice, and silence. The lesson is not "add more" - it's that **simple + consistent + well-packaged + well-scripted can win big.**
- **Direct conflict to resolve:** the current `learning-log.md` Core decision (2026-06-28, from the Vietnamese "Threads-City" reference) says illustrate PER SENTENCE with a visual change every few seconds. This breakout channel does the OPPOSITE - one held image per ~5s, slow zoom, no rapid change. Different content types reward different pacing (fast entertainment vs calm explainer). This is a conscious style choice WIT should make deliberately, not inherit by accident from whichever reference was studied last.
- **What is safe to copy:** production simplicity, one consistent reusable visual set, clean scripted VO, held-image pacing as an OPTION, and (already captured) their packaging + cadence + length discipline.
- **What NOT to copy:** their exact plain-doodle look (WIT + humor is a real differentiator - keep it) and their earnest no-jokes tone.
