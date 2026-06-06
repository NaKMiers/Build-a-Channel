# Legacy Remotion System

This folder stores old Remotion conventions for `Why It Works`.

Remotion is no longer the default production path. HyperFrames is now the active renderer.

Historical app path:

```text
remotion-studio/
```

This path is kept in notes only. HyperFrames is the current production path.

## Historical Commands

If the legacy app is restored, the old commands were:

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
- per-video assets and renders stored under `projects/<slug>/` when practical

## Migration Note

Do not recreate, move, or delete legacy Remotion production unless the user asks.
Use `.agents/_shared/hyperframes/` and `projects/<slug>/hyperframes/` for current production.

If useful later, manually port reusable ideas from the historical Remotion app into HyperFrames patterns:

- theme system
- Wit character component
- scene components
- typography rules
- audio timing helpers
- render QA utilities

Until then, avoid disruptive moves.
