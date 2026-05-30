# Legacy Remotion System

This folder stores old Remotion conventions for `Why It Works`.

Remotion is no longer the default production path. HyperFrames is now the active renderer.

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

Do not create new Remotion work unless the user explicitly asks.

Legacy model:

- one reusable Remotion system
- per-video scene data
- per-video assets and renders stored under `video-projects/<slug>/` when practical

## Migration Note

Keep `remotion-studio/` unchanged until the user asks to delete it.
Use `common/hyperframes/` and `video-projects/<slug>/hyperframes/` for current production.

If useful later, manually port reusable ideas from `remotion-studio/src/` into HyperFrames patterns:

- theme system
- Wit character component
- scene components
- typography rules
- audio timing helpers
- render QA utilities

Until then, avoid disruptive moves.
