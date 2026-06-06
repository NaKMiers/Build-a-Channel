# Video Generation Tool

Purpose:
track reusable video-generation or video-assembly tools for the channel.

## Current Status

The default video assembly and render system is HyperFrames:

```text
projects/<slug>/hyperframes/
```

The old Remotion app is kept temporarily for reference and should not be edited or deleted unless the user asks.

## Rules

- Do not introduce another video-generation tool unless it clearly improves the HyperFrames pipeline.
- Keep generated video clips inside `projects/<slug>/assets/` or `projects/<slug>/renders/`.
- Record reusable workflows in `.agents/_shared/`.
- Keep the final edit path simple enough to repeat weekly.
- Run `npm run check` before treating a HyperFrames composition as ready.
