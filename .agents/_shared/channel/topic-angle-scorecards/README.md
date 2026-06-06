# Topic Angle Scorecards

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
store the reusable rules and blank templates for future `Why It Works` topic angle scorecards.

This folder must not contain an angle package for an existing video unless the user explicitly asks to apply the channel-wide system to that video project.

## Source Systems

Use these files first:

- [Topic Angle Selection System](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-selection-system.md)
- [Topic Angle Scorecard](C:\ME\THINGS\Build a Channel\.agents\_shared\topic-angle-scorecard.md)

## Folder Rule

This directory is for channel-wide scorecard templates and reusable scoring notes.

When a future video project is explicitly started or restarted, copy the blank template into:

```text
projects/<slug>/00-idea.md
```

Do not create per-video angle packages here by default.

## Blank Angle Package Template

```markdown
# Angle Package

Classification: `Core candidate` / `Experiment candidate` / `Reject`

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

## Score

Curiosity: __ / 5
Relatability: __ / 5
Visual motif: __ / 5
Humor potential: __ / 5
English learner fit: __ / 5
Explanation depth: __ / 5
Packaging strength: __ / 5
Production feasibility: __ / 5

Total: __ / 40

Critical category check:
Curiosity >= 3: yes/no
Visual motif >= 3: yes/no
Explanation depth >= 3: yes/no
Packaging strength >= 3: yes/no

Hard fails triggered:

Decision:
PASS / REVISE / REJECT / EXPERIMENT

Required fixes before scripting:
1.
2.
3.
```

## Minimum Production Standard

For normal long-form production:

```text
Minimum total: 30 / 40
Critical categories: at least 3 / 5 each
Hard fails: none
```

Below `30/40`, use one of these decisions:

- `REVISE`: sharpen the contradiction, motif, WIT role, or package
- `EXPERIMENT`: use only with explicit approval
- `REJECT`: keep it out of production for now

## Rejection Rules Summary

Reject or revise if:

- the angle sounds like generic education
- the thumbnail would be only text
- WIT has no emotional job
- there is no real-life object or UI evidence
- the repeated visual motif is missing
- the final insight is obvious
- the explanation is mostly opinion
- the topic does not help English learners understand modern life
- the angle needs unsafe assets, copied frames, or misleading packaging
