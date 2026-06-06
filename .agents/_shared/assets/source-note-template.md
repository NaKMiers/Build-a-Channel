# Source Note Template

Classification: `Core`

Scope: `CHANNEL_WIDE`

Use this template for reusable real-life assets, UI mockups, generated images, licensed images, and future per-video asset copies.

For reusable shared assets, keep source notes near the asset or inside the relevant `source-notes/` folder.

For future video-specific assets, copy this template into the video project only after an explicit apply command.

## Blank Template

```markdown
# Asset Source Note

Asset ID:

Asset filename:

Asset path:

Asset category:

Reusable status:
`channel-wide reusable` / `video-specific only` / `reference only`

Source type:
`self-shot` / `generated` / `public-domain` / `licensed` / `self-made mockup` / `recreated screenshot mockup` / `scanned texture`

Created or collected by:

Date created or collected:

Original source URL:

License or permission:

Tool or model used:

Generation prompt:

Editing notes:

Private information check:
`pass` / `needs cleanup` / `not applicable`

Logo and trademark check:
`pass` / `needs review` / `not applicable`

Copyright check:
`pass` / `needs review`

Commercial/video use allowed:
`yes` / `no` / `unclear`

Allowed uses:

Restrictions:

Safe-use decision:
`approved` / `approved with limits` / `reference only` / `reject`

Reason for decision:

Reviewer:

Review date:
```

## Short Sidecar Version

Use this when the full source is obvious, such as a self-made generic mockup:

```markdown
# Asset Source Note

Asset:

Source type:

Created by:

Date:

Safe-use decision:

Notes:
```

## Required Checks

Before marking `approved`, confirm:

- no private data is visible
- no watermark is visible
- source and license are clear
- real logos are absent or intentionally justified
- UI is fictional unless there is a specific approved reason
- generated assets include prompt/tool/date notes
- the asset can be used in a public `Why It Works` video

If any check is unclear, mark:

```text
approved with limits
```

or:

```text
reference only
```

Do not use `unclear` assets in final public videos.
