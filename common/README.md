# Common

This folder stores reusable systems for the `Why It Works` channel.

Use this folder for things that should improve multiple videos, not just one video.

## Folders

```text
common/
  assets/       shared brand assets, sound beds, reusable graphics
  remotion/     Remotion conventions and shared production notes
  skills/       local project skills and repeatable Codex workflows
  templates/    reusable templates for video projects and production docs
  tools/        reusable tool notes and scripts
```

## Rule

If something belongs to one video, put it in:

```text
video-projects/<slug>/
```

If something should help many videos, put it in:

```text
common/
```

## Current Production App

The current Remotion app still lives at:

```text
remotion-studio/
```

Keep it there for now to avoid breaking commands.
Use `common/remotion/` to document shared Remotion conventions and future extraction plans.

Move code only when the production system is stable enough to reorganize without losing momentum.
