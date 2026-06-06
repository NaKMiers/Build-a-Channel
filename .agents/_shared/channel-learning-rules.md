# Channel Learning Rules

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
define how `Why It Works` turns upload results, comments, production friction, and creator judgment into reusable channel learning.

This document protects the channel from both mistakes:

- ignoring useful evidence
- overreacting to one upload

## Core Rule

Learn from performance without letting performance rewrite the channel casually.

Use this order:

```text
observation -> diagnosis -> confidence label -> next-video rule -> reusable channel lesson
```

Do not jump from:

```text
one weak upload -> change the whole strategy
```

## What Counts As A Reusable Lesson

A lesson is reusable if it can improve future videos beyond one upload.

Good reusable lessons:

- thumbnails need more concrete objects
- first `30` seconds needs the contradiction earlier
- WIT reactions work best when he is visibly affected by the system
- dense sections need real-life examples before abstract explanation
- useful English phrases should repeat as labels, not classroom notes
- custom animation took too long for the viewer value it created

Weak non-reusable observations:

- this one joke did not land
- this exact thumbnail color looked odd
- this one upload was slow
- one comment disliked the topic
- one viewer asked for a totally different niche

## Learning Categories

Use these categories in `.agents/_shared/channel/learning-log.md`:

```text
Operational lesson
Experiment result
Packaging lesson
Audience insight
```

### Operational Lesson

Use when a production process should change.

Examples:

- reduce custom animation
- create a reusable board template
- run packaging earlier
- move a useful asset into `.agents/_shared/`

### Experiment Result

Use when a planned test produced a result.

Examples:

- a more direct title performed better than a clever title
- a slower voice test improved clarity
- a culture-led topic did or did not fit the channel

### Packaging Lesson

Use when title, thumbnail, or first `10` seconds performance creates a reusable rule.

Examples:

- thumbnail needs one visible contradiction
- title should name the hidden logic
- WIT emotion must be readable at mobile size

### Audience Insight

Use when comments, repeat viewers, questions, or confusion reveal something about the audience.

Examples:

- viewers like hidden internet business models
- learners need clearer labels for abstract money terms
- viewers respond to dry jokes about modern-life subscriptions

## Confidence Labels

Every lesson should carry one confidence label:

```text
High
Medium
Low
```

Use `High` only when:

- the pattern repeats across uploads, or
- analytics and comments clearly point to the same diagnosis

Use `Medium` when:

- one upload gives a clear signal, and
- the diagnosis matches creator judgment or reference-channel comparison

Use `Low` when:

- analytics are tiny
- evidence is mostly taste-based
- one comment or one weak metric is the main signal

Low-confidence lessons should become experiments, not core rewrites.

## Promotion Rules

Use this table before writing lessons into project memory:

| Signal | Store Where | Rule |
| --- | --- | --- |
| One-video note | future `projects/<slug>/` review | Do not promote unless reusable |
| Reusable workflow lesson | `.agents/_shared/channel/learning-log.md` | Label as `Operational lesson` |
| Reusable packaging lesson | `.agents/_shared/channel/learning-log.md` | Label as `Packaging lesson` |
| Reusable audience pattern | `.agents/_shared/channel/learning-log.md` | Label as `Audience insight` |
| Unproven but useful test | `.agents/_shared/channel/learning-log.md` | Label as `Experiment result` or experiment |
| Foundational strategy change | ask user first | Do not edit `channel-foundation.md` without confirmation |

## Do Not Promote

Do not promote these into channel-wide memory:

- one-off personal preference
- comments that conflict with the channel promise
- low-trust advice from random viewers
- demands to abandon English learner clarity
- demands to turn the channel into direct product promotion
- upload performance affected by obvious external timing but no creative diagnosis
- analytics too small to interpret and no useful qualitative signal

## Decision Rules For Future Uploads

### Repeated CTR Problem

If multiple uploads have weak CTR, inspect packaging systems before changing topic lane.

Check:

- title specificity
- thumbnail contradiction
- mobile readability
- WIT emotion
- reference comparison
- title-thumbnail non-duplication

### Repeated First `30s` Problem

If multiple uploads lose viewers early, inspect hooks before changing video length.

Check:

- situation first
- contradiction by second `5`
- WIT reaction by second `8`
- no intro delay
- first line sounds human

### Repeated Mid-Video Retention Problem

If multiple uploads dip in explanation sections, inspect scene grammar and learner clarity.

Check:

- too abstract
- too many labels
- not enough real-life examples
- WIT disappears
- voice pace too fast
- payoff arrives too late

### Repeated Production-Time Problem

If videos take too long, simplify the production system before reducing the publishing standard.

Check:

- reusable boards
- reusable WIT poses
- reusable red markup
- reusable real-life assets
- fewer custom animations
- earlier packaging approval

## Updating `.agents/_shared/channel/learning-log.md`

When adding a reusable lesson, use this shape:

```markdown
### Short Lesson Title

Classification: `Operational lesson` / `Experiment result` / `Packaging lesson` / `Audience insight`

Confidence: `High` / `Medium` / `Low`

Lesson:
one short reusable lesson.

Evidence:
what upload signal, comment pattern, or production result supports it.

Next rule:
what should change in future videos.

Scope note:
this is a reusable channel lesson, not a rewrite of channel identity.
```

## Updating Core Strategy

Do not update `.agents/_shared/channel/channel-foundation.md` from upload feedback unless:

- the lesson is repeated
- the change fits `Why It Works`
- the change passes `.agents/_shared/channel/channel-guardrails.md`
- the user explicitly confirms the core change

Upload feedback can improve systems quickly.
Core identity should change slowly.

## Working Standard

```text
Small signal: note it.
Repeated signal: turn it into a rule.
Core change: ask first.
```
