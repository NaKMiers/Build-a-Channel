# Voiceover Tool

Purpose:
generate narration audio for approved video scripts.

## Current Implementation

Current active use:

```text
projects/<slug>/hyperframes/assets/voiceover/
```

Existing George MP3 files can be copied into the HyperFrames project and referenced directly by `<audio>` clips.

Historical legacy generation script:

```text
remotion-studio/scripts/generate-voiceover.mjs
```

Historical legacy voice-list script:

```text
remotion-studio/scripts/list-elevenlabs-voices.mjs
```

Historical legacy reference voice test script:

```text
remotion-studio/scripts/generate-reference-voice-test.mjs
```

## Current Commands

If the legacy app is restored and new ElevenLabs audio is needed, the old commands were:

```powershell
cmd /c npm run voices
cmd /c npm run voiceover
cmd /c npm run voiceover:reference-test
```

If `remotion-studio/` is absent, do not assume these scripts are available.

## Rules

- Do not generate full voiceover until the script and visual plan are approved.
- Before full voiceover, mark the script with `.agents/_shared/voice/script-markup-guide.md`.
- Run the first `45-60` seconds through `.agents/_shared/voice/voice-test-protocol.md`.
- Follow `.agents/_shared/voice/narration-system.md` for David23 delivery, pacing, and timing rules.
- Keep API keys only in local env files.
- Store final per-video voiceover notes in `projects/<slug>/voiceover/`.
- Copy render-ready audio files into `projects/<slug>/hyperframes/assets/voiceover/`.
- Record reusable voice lessons in this file or `.agents/_shared/workflows/continuous-improvement-loop.md`.
- Only use a reference voice when the recording is owned by the creator or explicit permission exists.
- For early tests, create temporary reference voices and delete them after generation unless the voice is intentionally approved.
- ElevenLabs instant voice cloning may require a paid plan. If the API returns `paid_plan_required`, keep the reference recording as a style guide or upgrade before retrying.

## Current Channel Voice Decision

Use `David23` as the default narrator for future `Why It Works` videos.

Approved voice location:

```text
.agents/_shared/voice/david23/
```

Sample:

```text
.agents/_shared/voice/david23/david23-sample.mp3
```

Generation settings:

- TTS voice: `am_eric`
- balanced long-form speed: `0.84`
- careful learner test speed: `0.78`
- slower learner-paced fallback speed: `0.76`
- audition/sample speed: `1.10`
- language: `en-us`

For full videos, default to `0.84` unless the short voice test shows that jokes, labels, or dense explanations need more room.
Use `0.78` as the careful learner-friendly test variant.
Use `0.76` only when the user asks for a noticeably slower learner-paced cut or the voice test fails at faster settings.

Keep George and all previous candidate/reference voices available as fallback/reference voices.
Do not delete or overwrite existing George/reference voices.
