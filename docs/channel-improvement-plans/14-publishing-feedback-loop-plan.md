# Plan 14: Publishing Feedback Loop

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide publishing feedback loop so each future published video produces reusable learning for the entire channel instead of treating upload performance as random luck.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable publishing feedback loop for the entire channel. It must not create or update a review for any specific video.

Allowed outputs:

- `common/publishing-feedback-loop.md`
- `common/post-upload-review-template.md`
- `common/channel-learning-rules.md`

Forbidden outputs:

- no edits to `video-projects/<slug>/`
- no post-upload review for any existing video project unless explicitly requested

Source insight:
Weak expected performance is not only a production concern. The channel needs a loop that measures packaging, retention, comments, and production effort, then improves the next upload system.

## Problem

Without a feedback loop, the channel may keep improving things that do not affect performance.

Possible mistakes:

- polishing visuals while thumbnail is weak
- improving explanation while hook is weak
- making WIT cuter when he needs to be funnier
- adding detail while retention needs simpler jokes
- producing full videos before testing packaging

## Target

After every upload, write a short postmortem that answers:

`What should change in the next video?`

The loop should improve:

- topics
- titles
- thumbnails
- first `30` seconds
- WIT use
- voice delivery
- visual texture
- production effort

## Metrics To Track

Track these when available:

- impressions
- click-through rate
- views after `24h`
- views after `7d`
- average view duration
- average percentage viewed
- first `30s` retention
- retention dips
- traffic source
- comments and repeated viewer reactions
- subs gained

If analytics are too small to be statistically meaningful, still track:

- whether thumbnail looked clickable beside references
- whether first `10` seconds felt strong
- whether people who watched gave qualitative feedback
- how hard the video was to produce

## Post-Upload Template

Create this channel-wide template:

```text
common/post-upload-review-template.md
```

Template:

```markdown
# Post-Upload Review

Video:
Publish date:
Runtime:

## Packaging

Title:
Thumbnail:
CTR:
Impressions:
What probably helped:
What probably hurt:

## Retention

Average view duration:
Average percentage viewed:
First 30s retention:
Biggest dip:
Likely reason:

## Creative Notes

Best joke:
Weakest section:
Best WIT moment:
Weakest WIT moment:
Best real-life visual:
Most generic board:

## Audience Signals

Comments:
Questions:
Confusion:
Requests:

## Production Notes

What took too long:
What should become reusable:
What should be removed from workflow:

## Next Video Rules

1.
2.
3.
```

## Decision Rules

If CTR is weak:

- fix thumbnail and title before changing the whole format
- compare beside references
- check whether thumbnail creates a question

If first `30s` retention is weak:

- improve hook
- reduce intro
- make contradiction visible earlier
- add WIT reaction sooner

If retention drops mid-video:

- identify if the section became too abstract
- add real-life example
- add visual joke
- cut explanation length

If comments show confusion:

- improve learner clarity
- add repeated phrase
- simplify visual labels

If production took too long:

- move assets into reusable library
- reduce custom animation
- use stronger static boards

## Learning Log Rules

Only write channel-level lessons into `docs/learning-log.md` if they are reusable.

Classify them as:

- `Operational lesson`
- `Experiment result`
- `Packaging lesson`
- `Audience insight`

Do not rewrite `docs/channel-foundation.md` unless the user explicitly confirms a core change.

## Acceptance Criteria

The feedback loop is working if:

- every upload produces one short post-upload review
- the next video uses at least one lesson from the previous upload
- repeated problems become workflow rules
- strong assets become reusable assets
- weak assumptions are labeled and tested instead of becoming strategy

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/14-publishing-feedback-loop-plan.md.
Create or update the channel-wide publishing feedback loop.
Allowed outputs are common/publishing-feedback-loop.md, common/post-upload-review-template.md, and common/channel-learning-rules.md.
Do not edit video-projects.
Do not create or update a specific video's post-upload review unless I explicitly ask.
Do not change core channel strategy without explicit approval.
```
