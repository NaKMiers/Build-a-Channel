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

Use `David23` as the default narrator for future `Why It Works` videos.

Approved voice location:

```text
common/voice/david23/
```

Sample:

```text
common/voice/david23/david23-sample.mp3
```

Generation settings:

- TTS voice: `am_eric`
- balanced long-form speed: `0.84`
- slower learner-paced fallback speed: `0.76`
- audition/sample speed: `1.10`
- language: `en-us`

For full videos, default to `0.84` when targeting a normal YouTube explainer pace around `3:10-3:30` for this script length.
Use `0.76` only when the user asks for a noticeably slower learner-paced cut.

Keep George and all previous candidate/reference voices available as fallback/reference voices.
Do not delete or overwrite existing George/reference voices.
