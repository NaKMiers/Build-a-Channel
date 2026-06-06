# Plan 13: Topic Angle Selection

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide topic angle selection system so future topics become sharp, clickable, visual, creator-led videos before scripting starts.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable topic angle selection system for the entire channel. It must not create an angle package for any specific video.

Allowed outputs:

- `.agents/_shared/topic-angle-selection-system.md`
- `.agents/_shared/topic-angle-scorecard.md`
- `.agents/_shared/channel/topic-angle-scorecards/README.md`

Forbidden outputs:

- no edits to `projects/<slug>/`
- no per-video angle package unless explicitly requested

Source insight:
Broad topic ideas are not enough. Future videos need sharper creator premises before production starts.

## Problem

Broad topics can sound useful but still fail on YouTube.

Weak broad angles:

- `How free apps make money`
- `Why budgeting fails`
- `Why productivity content is bad`
- `Why cheap products are worse`

These are understandable, but they do not automatically create:

- curiosity
- a thumbnail
- a visual motif
- a deadpan point of view
- a reason this channel should make the video

## Target

Every chosen topic should become a sharp angle:

`topic + contradiction + visual metaphor + viewer pain`

Examples:

- `A helpful system is secretly a checkout.`
- `A personal habit is actually a business model.`
- `A cheap product is sometimes an expensive product with the future removed.`
- `A convenience tool is often a fee machine wearing a friendly jacket.`
- `A productivity promise may sell the feeling of control, not control.`

## Angle Selection Scorecard

Score every candidate from `1-5`.

| Criterion | Question |
|---|---|
| Curiosity | Does this make people ask `wait, why?` |
| Relatability | Has the viewer felt this problem? |
| Visual motif | Can we draw or show it in one repeated image? |
| Humor potential | Can WIT suffer from it? |
| English learner fit | Is the topic useful real-world English? |
| Explanation depth | Is there a real system behind the joke? |
| Packaging strength | Can thumbnail and title become specific? |
| Production feasibility | Can we make it with current tools and assets? |

Recommended threshold:
Do not produce a long video under `30/40` unless the user explicitly wants an experiment.

## Required Angle Package

Before scripting, define:

- topic
- sharper angle
- main contradiction
- recurring metaphor
- thumbnail tension
- first `10` second hook
- WIT's emotional role
- real-life objects
- final insight

Template:

```markdown
# Angle Package

Topic:
Sharp angle:
Main contradiction:
Recurring metaphor:
Thumbnail tension:
First 10 seconds:
WIT role:
Real-life objects:
Final insight:
Why now:
Why this channel:
```

## Red Flags

Reject or revise the angle if:

- it sounds like generic education
- the thumbnail would be only text
- WIT has no reason to be there
- there is no real-life object
- the joke is only in the script, not visual
- the final insight is obvious
- it does not help English learners understand modern life

## Workflow

1. Start with `5-10` raw topic ideas.
2. Turn each into a sharp angle.
3. Score each angle.
4. Pick the best `1-2`.
5. Build rough title and thumbnail before writing script.
6. Write first `10` seconds.
7. Only then expand into full script.

## Acceptance Criteria

An angle is ready if:

- it can be explained in one sentence
- it creates a thumbnail image immediately
- it gives WIT a clear emotional role
- it has a repeated visual motif
- it supports at least `5` visual jokes
- it ends with a useful insight

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read .agents/_shared/channel/channel-improvement-plans/13-topic-angle-selection-plan.md.
Create or update the channel-wide topic angle selection system.
Allowed outputs are .agents/_shared/topic-angle-selection-system.md, .agents/_shared/topic-angle-scorecard.md, and .agents/_shared/channel/topic-angle-scorecards/.
Do not edit projects.
Do not create an angle package for a specific video unless I explicitly ask.
```
