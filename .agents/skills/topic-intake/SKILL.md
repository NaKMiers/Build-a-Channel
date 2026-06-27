---
name: topic-intake
description: Generate and evaluate next-video topic ideas for the Why It Works YouTube channel, sourced from what the world is ACTUALLY curious about right now. Use when the user asks for topic intake, next video ideas, trending topics, raw topic candidates, scored video angles, or step 0 of the Why It Works workflow. It reads the shared channel brain, BROWSES the web for trending / high-interest topics (Google Trends, high-view recent videos, search and news interest) and gathers real EVIDENCE of demand for every candidate (never fabricated), then shapes ideas into angle packages scored for an A2–C1 English-learner audience whose advantage is "interesting English" (entertainment-first so learners stay and learn). Optionally writes a project topic-intake file when a candidate is chosen.
---

# Topic Intake

## Purpose

Run step `0` of the `Why It Works` video workflow: find topics the world is **actually curious about
right now**, prove the demand with evidence, and shape the best ones into sharp, scored video angles.

This is not a brainstorm of evergreen ideas pulled from memory. The channel's edge is **interesting
English**: an A2–C1 English learner comes for a genuinely funny, current, "why does this work?"
explainer and improves their English as a side effect. So topics must be (a) trending / currently
interesting, (b) backed by real demand evidence, and (c) explainable in entertaining, learner-friendly
English.

## Audience & Advantage (apply to every candidate)

- Audience: **A2–C1 English learners** (anchor at B1; let C1 enjoy the jokes, let A2 lean on captions).
- Advantage: **interesting English** — entertainment first, learning rides along. A topic must be
  something a learner would WANT to watch even if it were in their own language.
- Tone is allowed to be savage/cheeky (see `learning-log.md` confirmed tone rules); edge aimed at the
  system / the viewer's own wallet, never slurs; public figures only as transformative parody.

## Pipeline Position

Step `0`. No required previous output. When Persist Mode creates/updates
`projects/<slug>/00-topic-intake.md`, every later output in the project becomes stale (resolve by
suffix per `.agents/rules/video-workflow.md`). List stale downstream; never silently delete.

## Required Context

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/production-workflow.md`
9. `.agents/_shared/systems/topic-packaging-hooks.md`
10. `.agents/_shared/systems/script-learner-voice.md`
11. `references/memory.md`

## Trend & Evidence Requirement (the core of this skill)

Do not invent topics. Before recommending anything, BROWSE to discover what people are currently
curious about and to PROVE demand for each candidate.

Use the project-local `/browse` skill (`.agents/skills/browse/SKILL.md`); fall back to global gstack
`/browse`. Do not use other browser tools without explicit approval.

Look across multiple demand signals:

- **Google Trends** — rising / breakout queries, and 12-month interest for a candidate term. Capture
  the trend state (rising / breakout / steady-high) and the comparison.
- **YouTube** — recent videos (ideally last weeks/months) on the topic with high view counts; note
  view counts, recency, and how many strong videos exist (saturation vs opportunity).
- **Search / news / social interest** — news volume, Reddit/forum threads, "people also ask", or
  visible engagement showing the topic is alive now.

For EVERY serious candidate, record real evidence:

- the signal type (Trends / YouTube views / news / social)
- the concrete proof (e.g. "Google Trends: breakout"; "3 videos in last 60 days, top has 2.1M views")
- source URL(s)
- recency
- a one-line read of demand and saturation

If browsing fails or a candidate has no real demand signal, mark `Demand evidence: low` and do NOT
invent view counts, trend states, or numbers. A candidate with no evidence cannot be a top pick.

## Request Modes

- **Suggest Mode** — user wants ideas. Return scored candidates with evidence; do not create a project.
- **Persist Mode** — user picks a topic / asks to start the next video. Create or update only
  `projects/<slug>/00-topic-intake.md`. If downstream files exist, mark them stale and tell the user.
- **Improve Memory Mode** — user gives taste feedback; update the active project, then
  `references/memory.md`, then shared memory only for channel-wide lessons.

## Workflow

1. Rebuild channel context; note recent/active topics so candidates don't repeat.
2. BROWSE for what's trending / currently interesting across the channel's world (money, internet,
   society, business, modern life, current culture) — start from real trend/interest signals, not memory.
3. Collect a pool of `8–12` currently-interesting candidates, each with at least one real demand signal.
4. Shape each into a sharper angle: `topic + contradiction + visual metaphor + viewer pain`, with the
   sentence test: `This video is about how ___ looks like ___, but is actually ___.`
5. Gather/confirm demand EVIDENCE per candidate (Trends + recent high-view videos + news/social).
6. Reject or revise on hard fails: no real demand evidence; not explainable as a "why"; no curiosity;
   no visual/scene potential; weak interesting-English fit (too dry/academic to entertain a learner);
   unsafe / copyright / community-standard risk; pure rage-bait; direct product promotion.
7. Score the strongest angles (scorecard below).
8. Keep the best `5–7`; recommend the top `1–3`. For the top pick, sketch what becomes research,
   packaging, and the first 10 seconds.
9. Persist Mode only: write `projects/<slug>/00-topic-intake.md`. Then run the stale downstream check.

## Scorecard (each /5)

- **Trend / timeliness** — is it hot or rising NOW?
- **Demand evidence** — how strong/real is the proof of interest?
- **Curiosity** — strong "wait, why is that?" hook.
- **Relatability (global)** — a universal pain the worldwide learner audience feels (not local-only).
- **Explainability** — there is a real, satisfying hidden "why" to explain.
- **Interesting-English fit** — entertaining + learnable for A2–C1; would they watch for fun?
- **Visual potential** — strong scenes, mascot beats, real-asset/screenshot/caricature material.
- **Packaging strength** — title + thumbnail curiosity without fake claims.
- **Feasibility & safety** — buildable; copyright/law/community-standards safe; protects trust.

Threshold for normal production: strong total with no critical category (trend, demand evidence,
curiosity, explainability, interesting-English fit) below `3/5`.

## Output Format (Suggest Mode)

```markdown
## Best Next Pick
- Working title:
- Sharp angle:
- Why now (trend):
- Demand evidence:
- Why this one:
- Score:
- Main risk:

## Candidate Table
| Rank | Working title | Trend | Demand evidence | Curiosity | Relatable | Explainable | Eng-fit | Visual | Packaging | Feasible/Safe | Total | Decision |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|

## Demand Evidence
| Candidate | Signal type | Concrete proof (no invented numbers) | URL | Recency | Read |
|---|---|---|---|---|---|

## Top Candidate Details
### 1. <working title>
- Topic / why-question:
- Why now (trend state):
- Demand evidence:
- Viewer pain / hidden system:
- Main contradiction:
- Recurring visual metaphor:
- Thumbnail tension:
- First 10 seconds:
- Mascot role:
- Real-life / asset material:
- Interesting-English value (and a phrase or two learners gain):
- Final insight:
- Score breakdown (each /5) + total:
- Demand evidence confidence:
- Required fixes before research:

## Parked / Rejected
- <idea>: <reason>

## Next Step
Pick one, ask for revisions, or ask me to start `projects/<slug>/00-topic-intake.md`.
```

Persist Mode writes the chosen candidate into `projects/<slug>/00-topic-intake.md` using the template
fields from `projects/_template/00-topic-intake.md` plus the full angle package, demand evidence, and
scorecard.

## Hard Fails

- recommending a topic with no real demand evidence, or inventing trend states / view counts
- a top pick that is not currently interesting/trending (unless the user explicitly wants evergreen)
- a topic with no explainable "why", no curiosity, or no visual/scene potential
- weak interesting-English fit (cannot entertain an A2–C1 learner)
- unsafe, copyright-risky, community-standard-violating, rage-bait, or direct-promotion topics
- skipping the browse/evidence pass when browsing was available

## Self-Improvement

Read `references/memory.md` every run. Update it when the user picks/rejects candidates and explains
why, when a demand signal proves reliable or misleading, or when a topic later fails in production.
Promote channel-wide lessons into `.agents/_shared/channel/learning-log.md`, classified `Core` /
`Experiment` / `Operational lesson` / `Reject`. Do not rewrite channel foundation, audience, or tone
from one run without explicit user confirmation.
