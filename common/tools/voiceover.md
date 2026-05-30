# Voiceover Tool

Purpose:
generate narration audio for approved video scripts.

## Current Implementation

Current active use:

```text
video-projects/<slug>/hyperframes/assets/voiceover/
```

Existing George MP3 files can be copied into the HyperFrames project and referenced directly by `<audio>` clips.

Legacy generation script:

```text
remotion-studio/scripts/generate-voiceover.mjs
```

Legacy voice-list script:

```text
remotion-studio/scripts/list-elevenlabs-voices.mjs
```

Legacy reference voice test script:

```text
remotion-studio/scripts/generate-reference-voice-test.mjs
```

## Current Commands

Run from `remotion-studio/` only if new ElevenLabs audio is needed:

```powershell
cmd /c npm run voices
cmd /c npm run voiceover
cmd /c npm run voiceover:reference-test
```

## Rules

- Do not generate full voiceover until the script and visual plan are approved.
- Keep API keys only in local env files.
- Store final per-video voiceover notes in `video-projects/<slug>/voiceover/`.
- Copy render-ready audio files into `video-projects/<slug>/hyperframes/assets/voiceover/`.
- Record reusable voice lessons in this file or `common/skills/continuous-improvement-loop.md`.
- Only use a reference voice when the recording is owned by the creator or explicit permission exists.
- For early tests, create temporary reference voices and delete them after generation unless the voice is intentionally approved.
- ElevenLabs instant voice cloning may require a paid plan. If the API returns `paid_plan_required`, keep the reference recording as a style guide or upgrade before retrying.

## Current Channel Voice Decision

Use `George` as the working narrator while the production flow is still being shaped.

Keep creator reference recordings for future voice cloning after the workflow is stable enough to justify upgrading ElevenLabs.
