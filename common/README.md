# Common

This folder stores reusable systems for the `Why It Works` channel.

Use this folder for things that should improve multiple videos, not just one video.

## Folders

```text
common/
  assets/       shared brand assets, sound beds, reusable graphics
  hyperframes/  HyperFrames conventions and shared production notes
  remotion/     legacy Remotion notes kept temporarily for reference
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

The current production renderer is HyperFrames.

Per-video HyperFrames projects live at:

```text
video-projects/<slug>/hyperframes/
```

The old Remotion app still lives at:

```text
remotion-studio/
```

Keep it there for now because the user asked to delete it later, not during the migration.
Use `common/hyperframes/` for the active production conventions.

Do not move or delete legacy Remotion code unless the user explicitly requests it.
