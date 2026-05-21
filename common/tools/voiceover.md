# Voiceover Tool

Purpose:
generate narration audio for approved video scripts.

## Current Implementation

Current script:

```text
remotion-studio/scripts/generate-voiceover.mjs
```

Current voice-list script:

```text
remotion-studio/scripts/list-elevenlabs-voices.mjs
```

## Current Commands

Run from `remotion-studio/`:

```powershell
cmd /c npm run voices
cmd /c npm run voiceover
```

## Rules

- Do not generate full voiceover until the script and visual plan are approved.
- Keep API keys only in local env files.
- Store final per-video voiceover notes in `video-projects/<slug>/voiceover/`.
- Record reusable voice lessons in this file or `common/skills/continuous-improvement-loop.md`.
