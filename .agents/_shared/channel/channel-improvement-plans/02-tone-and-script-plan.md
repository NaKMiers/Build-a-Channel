# Plan 02: Tone And Script

Classification:
`Core channel upgrade plan`

Goal:
change the channel-wide script and tone system from `clear explainer` to `deadpan creator exposing a weird system`, while keeping simple English for learners.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable script and tone system for the entire channel. It must not inspect, rewrite, or modify any video project.

Allowed outputs:

- `.agents/_shared/script-tone-system.md`
- `.agents/_shared/script-templates/deadpan-explainer-template.md`
- `.agents/_shared/script-templates/section-joke-builder.md`
- `.agents/_shared/script-templates/learner-friendly-script-checklist.md`

Forbidden outputs:

- no edits to `projects/<slug>/02-script.md`
- no rewriting an existing video script
- no per-video deadpan rewrite

## Problem

The current script style is clear and useful, but sometimes too polite.

Weaknesses:

- Some lines sound like a formal explainer.
- Some jokes are clever but not visual.
- The explanation sometimes arrives before enough tension is created.
- The script can feel like it is teaching a topic instead of noticing something ridiculous.

## Target Voice

The channel voice should be:

- clear
- simple
- dry
- skeptical
- observant
- slightly tired of modern life
- funny without announcing that it is funny

The channel voice should not be:

- academic
- corporate
- motivational
- slang-heavy
- fake-deep
- too polished
- native-speaker-only comedy

## Core Script Rule

Every major section must answer two questions:

1. What is the explanation?
2. What is the funny image?

If a section only explains, it is not finished.

## Script Transformation Pattern

Turn formal ideas into concrete deadpan observations.

Weak:

`Free is not always the absence of payment. Sometimes it is just the removal of friction.`

Better:

`Free does not mean no one is paying. It usually means the cashier is hiding behind a plant.`

Weak:

`Apps use retention to increase ad inventory.`

Better:

`Every extra minute you spend scrolling becomes a tiny product sitting on a shelf called attention inventory.`

## Required Script Ingredients

Each long video should include:

- one main metaphor
- one repeated phrase
- one running visual joke
- one fake-serious line
- one absurd comparison
- one painfully relatable example
- one final insight that feels bigger than the topic

## Learner-Friendly Rules

Keep:

- short sentences
- common words
- repeated keywords
- visible labels
- clear examples
- simple structure

Avoid:

- dense idioms
- fast cultural references
- long abstract paragraphs
- sarcasm that requires native context
- jokes that hide the main meaning

The viewer should understand the point even if they miss one joke.

## Script Workflow

For the channel system, create reusable templates that force every future script to:

1. Start from a plain explanation.
2. Identify the main contradiction.
3. Choose the recurring metaphor.
4. Add one visual joke per section.
5. Replace formal lines with deadpan concrete lines.
6. Remove lines that explain what the visual already shows.
7. Add repeated phrases for memory.
8. Check learner clarity.
9. Read aloud with pauses.
10. Cut anything that sounds like a school essay.

## Section Checklist

For each section, verify:

- Is there one clear point?
- Is there one funny visual?
- Is the wording simple?
- Does WIT have a reason to exist?
- Is there a phrase worth putting on screen?
- Does the section move the story forward?

## Acceptance Criteria

A script pass is successful if:

- The hook creates tension within `10` seconds.
- Each section has a visual joke.
- The repeated metaphor appears at least `3` times.
- The ending lands a real insight.
- The script is readable for intermediate English learners.
- No section feels like generic educational content.

## Do Not Do

- Do not copy Casually Explained's exact persona.
- Do not make the language too native or obscure.
- Do not turn the channel into pure comedy without explanation.
- Do not keep a clever line if it cannot become a clear visual.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read .agents/_shared/channel/channel-improvement-plans/02-tone-and-script-plan.md.
Create or update the channel-wide script tone system.
Allowed outputs are .agents/_shared/script-tone-system.md and .agents/_shared/script-templates/.
Do not edit projects.
Do not rewrite any specific video script.
The output should become the required standard for all future Why It Works scripts.
```
