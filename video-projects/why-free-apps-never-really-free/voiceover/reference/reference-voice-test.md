# Reference Voice Test

Status: `Blocked by ElevenLabs plan`

Reference file:

```text
video-projects/why-free-apps-never-really-free/voiceover/reference/reference-voiceover.m4a
```

Test script:

```text
remotion-studio/scripts/generate-reference-voice-test.mjs
```

Command:

```powershell
cmd /c npm run voiceover:reference-test
```

## Result

The script reached ElevenLabs successfully, but ElevenLabs returned:

```text
paid_plan_required
Your subscription does not include instant voice cloning.
```

## Interpretation

The reference audio file is present and the local workflow is ready, but the current ElevenLabs account cannot create an instant cloned voice from the sample.

## Options

1. Upgrade/enable an ElevenLabs plan that includes instant voice cloning, then rerun:

```powershell
cmd /c npm run voiceover:reference-test
```

2. Keep using the current `George` narrator while using Anh Khoa's recording as a style reference for pacing and delivery.

3. Try another service or local tool later if the project decides cloned narration is important.

## Current Decision

Use `George` for now.

Keep Anh Khoa's reference recording for future voice cloning after the video production flow is shaped and stable.
