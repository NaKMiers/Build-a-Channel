# Video Generation Tool

Purpose:
track reusable video-generation or video-assembly tools beyond Remotion.

## Current Status

The default video assembly system is Remotion:

```text
remotion-studio/
```

No separate AI video-generation tool is locked yet.

## Rules

- Do not introduce a new video-generation tool unless it clearly improves the production pipeline.
- Keep generated video clips inside `video-projects/<slug>/assets/` or `video-projects/<slug>/renders/`.
- Record reusable workflows in `common/`.
- Keep the final edit path simple enough to repeat weekly.
