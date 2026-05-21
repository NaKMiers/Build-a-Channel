# Remotion System

This folder stores shared Remotion conventions for `Why It Works`.

The active app currently remains in:

```text
remotion-studio/
```

## Current Commands

Run from `remotion-studio/`:

```powershell
cmd /c npm run voices
cmd /c npm run voiceover
cmd /c npm run dev
cmd /c npm run render:sample
```

PowerShell may block direct `npm` calls on this machine, so prefer `cmd /c npm ...`.

## Production Rule

Do not create a new Remotion app per video unless there is a strong reason.

Preferred model:

- one reusable Remotion system
- per-video scene data
- per-video assets and renders stored under `video-projects/<slug>/` when practical

## Future Extraction Plan

When stable, extract reusable pieces from `remotion-studio/src/` into shared modules:

- theme system
- Wit character component
- scene components
- typography rules
- audio timing helpers
- render QA utilities

Until then, avoid disruptive moves.
