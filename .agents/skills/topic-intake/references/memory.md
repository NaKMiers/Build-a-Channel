# Topic Intake Skill Memory

This file stores memory specific to the `topic-intake` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about how this skill should suggest, score, reject, and persist topic candidates.

## Current Skill Standard

- Generate angles, not generic topics.
- Start from the shared channel brain every run because the channel can improve over time.
- Browse YouTube or the web before recommending or choosing ideas.
- Prefer the project-local vendored browse skill at `.agents/skills/browse/SKILL.md`; fall back to global gstack browse only if needed.
- Use high-view reference videos as demand and packaging evidence, not as source material to copy.
- Score candidates before recommending them.
- Show the full score breakdown for every candidate in the main table.
- Treat the first output as candidate selection, not research, script, or production.
- Do not create a project folder unless the user chooses a candidate or explicitly asks to start the project.
- When Persist Mode creates or updates `00-topic-intake.md`, treat all downstream outputs in that project as stale.
- Do not delete stale downstream outputs unless the user explicitly asks; otherwise tell the user to rerun downstream skills in order.
- Keep the channel influence-first; do not suggest topics that exist mainly to promote a product.

## Calibration From Current Best Project

Reference project:
`projects/2-why-everyone-pretends-to-be-busy`

Useful pattern:

- broad topic: people look busy
- sharp angle: modern life rewards visible activity over real progress
- viewer pain: people feel pressured to perform busyness
- hidden system: status, tools, visibility, and social safety reward visible activity
- recurring motif: calendar cage and fake emergency machine
- WIT role: trapped, attacked, overloaded, deadpan
- final insight: modern life confuses activity with value

Apply this pattern to future topic suggestions:

- Find the hidden system behind a familiar pain.
- Make the system happen to WIT.
- Pick one recurring object or motif before script writing.
- Protect the viewer from blame by showing the system first.
- Keep the final insight simple enough for an English learner to repeat.

## Candidate Mix

Default to a balanced batch:

- `2-3` money or spending angles
- `2-3` internet behavior angles
- `2` modern life or work-status angles
- `1-2` business or hidden pricing angles
- `1` wildcard if it still fits the channel promise

Avoid repeating active or recent production topics unless the user asks for variations.

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `topic-intake` as the first sequential video-production skill for `Why It Works`.

Initial memory rules:

- always read `.agents/_shared/` before suggesting topics
- keep skill-specific learning here
- promote reusable channel-wide lessons into `.agents/_shared/channel/learning-log.md`
- use the topic angle scorecard as the gate before research, packaging, hooks, scripts, or production

### 2026-06-06 - Add Reference And Score Transparency

Classification: `Topic intake lesson`

Context:
The first test run gave a ranked topic list, but the user wanted to know the exact criteria behind the score and wanted internet or YouTube references before choosing an idea.

Lesson:
Topic intake should not choose from internal judgment only. It should compare candidates against high-view reference videos and show the full score breakdown for each candidate.

Apply next time:

- browse YouTube or the web before recommending topic ideas
- list reference videos with channel, URL, visible views when available, and what to learn
- show all `8` score criteria per candidate, then sum to `/40`
- use references as demand and packaging signals, not as material to copy

Promote to shared memory:
no, this is currently a topic-intake skill behavior rather than a channel-wide strategy change.

### 2026-06-06 - Prefer Project-Local Browse

Classification: `Operational lesson`

Context:
The user noted that references to global skills may break when the project runs on another PC.

Lesson:
Topic intake should prefer project-local vendored skill dependencies when possible, then fall back to global skills only when necessary.

Apply next time:

- use `.agents/skills/browse/SKILL.md` for browsing instructions
- use `.agents/skills/browse/dist/browse.exe` on Windows when available
- if local browse is unavailable, say so clearly and then use global gstack browse if installed

Promote to shared memory:
yes, this is a portability rule for project-local skills.

### 2026-06-06 - Pipeline Stale Cascade

Classification: `Operational lesson`

Context:
The user clarified that every skill should behave as part of a sequential production pipeline.

Lesson:
`topic-intake` is the first step. It does not require previous outputs, but changing its output makes research, script, packaging, and later production files stale.

Apply next time:

- when creating or updating `00-topic-intake.md`, check for `01-research-pack.md`, `02-script.md`, `03-packaging.md`, and later downstream files
- list downstream files that are now stale
- tell the user to remove stale files or rerun downstream skills in order, starting with `research-pack`
- do not remove downstream files unless the user explicitly asks

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-21 - Pre-Chosen Topic + External Script Is Persist Mode

Classification: `Topic intake lesson`

Context:
The user brought the `Why Everyone Pretends To Be Busy` topic with a complete external
script (`why-people-pretend-to-be-busy.md`) and asked to "run the full workflow, starting
with topic-intake." This topic was the channel's quality benchmark in skill memory but had
never been made into a real project folder.

Lesson:
When the user arrives with an already-chosen topic (and possibly a finished script) and asks
to start the pipeline at step 0, this is Persist Mode, not Suggest Mode. Still browse for
reference demand evidence and run the full scorecard, then persist `00-topic-intake.md`.

Apply next time:

- Treat a named topic + "run the workflow" as Persist Mode; create only `00-topic-intake.md`.
- Reconcile the slug to the established canonical name from the channel brain when one exists
  (used `why-everyone-pretends-to-be-busy`, not the download filename `why-people-pretend-to-be-busy`).
- Do NOT copy an externally-provided script into `02-script.md` at step 0. The script enters via
  `script-draft` after `research-pack`, so research can ground it; note its existence in the intake file.
- Still satisfy the browsing + full scorecard requirements even when the topic is pre-chosen.

Promote to shared memory:
no, this is topic-intake intake-mode behavior, not a channel-wide strategy change.

### 2026-06-24 - User-Brought Pricing Claim: Verify Math Before Persisting

Classification: `Topic intake lesson`

Context:
The user floated their own angle ("Buy 1 Get 1 Free makes more profit than 50% off, isn't
it? but it looks the same"). It scored highest in the batch (`39/40`) and had the strongest
proven demand found all session (Vox "Why 'Buy one, get one free' isn't a great deal" ~3.7M).
Persisted as `projects/4-why-buy-1-get-1-beats-50-off/00-topic-intake.md`.

Lesson:
When the user brings a topic built on a math/economics/pricing claim, verify the actual
mechanism with a worked numeric example BEFORE scoring or persisting, and bake an honesty
guardrail into the intake file. For BOGO vs 50% off: BOGO ~2x the store's gross profit ONLY
when margin > 50% (item costs under half its price) AND the shopper takes both units; and the
two deals are not equal for the buyer either (50% off keeps cash if you only need one). The
channel angle is the contradiction ("same deal, double profit / free cuts your judgment"), not
a blanket "BOGO is always more profit."

Apply next time:
- For any "X is more profitable / cheaper / a trick" idea, build the small worked example first.
- Write a "must stay honest" section into `00-topic-intake.md` stating the conditions under which
  the claim holds, so research and script inherit the guardrail.
- A user's own idea is still Suggest Mode until they say "start"/"I choose that"; only then Persist.
- Confirming the user's instinct (with the precise condition) builds trust; don't just validate blindly.

Promote to shared memory:
no, this is topic-intake verification behavior, not a channel-wide strategy change.

### 2026-06-25 - "More like BOGO" = a topic FAMILY, not one topic

Classification: `Topic intake lesson`

Context:
After captioning the BOGO video, the user asked for "some topic like buy1get1 beats 50%off, trick
in business that make people a rabbit." I generated a focused batch in that one family (pricing/
perception tricks that hijack a mental shortcut: charm pricing $9.99, decoy effect, anchoring/fake
original price, Veblen, unit-price trap, fake scarcity), browsed demand for each, and scored. The
user chose `$9.99` (charm pricing). Persisted `projects/5-why-everything-costs-9-99/00-topic-intake.md`.

Lesson:
When the user references a past video as the template ("topic like X"), treat it as a request for
the same ANGLE FAMILY, not a single idea. Mine the chosen reference's DNA (here: a tiny detail that
fools one mental shortcut + clean worked example + two-price-tag visual + WIT-as-rabbit) and generate
a tight batch that all share that DNA, instead of spreading across all lanes. Lead with the closest
twin that also has the strongest proven demand. For $9.99 specifically, Half as Interesting (~1.2M)
is hard proof, and HAI is the channel's #1 topic-selection model - so flag "learn, don't copy its
structure." Kept the 2026-06-24 pricing-claim rule: verified the left-digit mechanism with a worked
penny example and wrote a "Must Stay Honest" guardrail (perception nudge, not a lie; tendency not law;
reverses at the luxury/round-number end) into the intake file so research + script inherit it.

Apply next time:
- "like <past video>" -> same-family batch, mine the reference's contradiction+motif+WIT pattern.
- Recommend the closest twin with the best demand; offer the higher-ceiling sibling as the alt.
- For any pricing/psychology claim, worked example + honesty guardrail in `00-topic-intake.md` first.

Promote to shared memory:
no, this is topic-intake batching/intake behavior, not a channel-wide strategy change.

### 2026-06-26 - Re-running intake on a previously-chosen topic whose folder was deleted

Classification: `Topic intake lesson`

Context:
The user said "why everything costs 9.99 / this is the topic, run /topic-intake." Skill memory
(2026-06-25) showed this exact topic was already chosen and persisted as
`projects/5-why-everything-costs-9-99/00-topic-intake.md`, but the whole project 5 folder had since
been deleted from the working tree (and removed at HEAD). Recovered the prior 38/40 intake from git
(`git show HEAD~1:...`), re-verified demand via browse (Half as Interesting ~1.2M confirmed; found a
NEW data point, BrainStuff/HowStuffWorks ~421K; plus brand-new uploads proving the topic is still
evergreen-active), and re-created the intake file with a refreshed reference table dated today.

Lesson:
A pre-chosen topic + "run topic-intake" is Persist Mode (per 2026-06-21). When skill memory says that
topic was already worked through but the project folder is gone, do not blindly regenerate from
scratch and do not silently restore the old file either: recover the prior intake from git to keep its
validated scorecard/guardrail, but still satisfy the browsing requirement with a fresh re-verify so the
reference table reflects today (it may strengthen - found the 421K HowStuffWorks reference this time).
Because the folder was fully deleted, there were no downstream files to mark stale (clean slate).

Apply next time:
- Check git history for a deleted intake before regenerating; reuse the validated scorecard + honesty
  guardrail, refresh only what browsing updates.
- Always re-browse for demand even when reusing - date the reference table to the current run.
- If the whole folder is gone, the stale-downstream check is trivially empty; say so.

Promote to shared memory:
no, this is topic-intake re-creation behavior, not a channel-wide strategy change.

### 2026-06-28 - Fresh-trend batch; user picked the freshest/highest-demand angle (AI slop)

Classification: `Topic intake lesson`

Context:
Plain `/topic-intake` (Suggest Mode). Browsed YouTube view counts + Google News recency for a
balanced 7-candidate batch deliberately OUTSIDE the recent pricing-trick family (projects 4-5).
Top picks all required two signal types. The user chose candidate 1, AI slop ("Why The Internet
Is Full Of Garbage Now"), which had ranked 1 (43/45) on the strongest trend + freshest news
(hours-old articles, "60% of TikTok is AI slop") and clean global relatability. Persisted as
`projects/5-why-the-internet-is-full-of-ai-slop/00-topic-intake.md`.

Lesson:
When the user gives no steer, lead with the candidate that has the freshest, most current trend
AND truly global relatability, not just the highest raw view count. Tipflation had bigger raw
views but US-skewed pain; AI slop won on currency + global feed-pollution everyone shares. The
user picked the recommended #1, which validates: rank by (trend currency x global pain), then
demand size, then visual/packaging. Also: after several same-family pricing topics (4-5), a fresh
internet/AI lane was welcome - vary the lane when the user does not ask for "more like X."

Note carried into the intake file: for an AI-topic, write a "Why slop wins" incentive chain +
an honesty guardrail (define slop cleanly; the incentive is the villain, not "AI"; no invented
stats; public-figure AI images referenced as phenomenon via WIT caricature only). This mirrors
the pricing-claim guardrail habit (2026-06-24 / 06-25) - any "X is ruining Y" topic needs the
real mechanism + honesty rails baked in at step 0 so research and script inherit them.

Apply next time:
- No steer -> rank by trend-currency x global-relatability first, then demand size, then visuals.
- Vary the lane after a run of same-family picks unless the user asks for the same family.
- For AI / "X is ruining Y" topics, bake the incentive mechanism + honesty guardrail into intake.

Promote to shared memory:
no, this is topic-intake ranking/intake behavior, not a channel-wide strategy change.

### 2026-07-02 - User-steered family batch; user's own angle beat the higher-scored sibling

Classification: `Topic intake lesson`

Context:
The user steered the run to the World Cup family (2026 tournament live, mid-knockout) with
their own raw angle ("why world is loss but every hold it?") and asked for it "or a much
better choice." Browsed a 5-candidate family batch. The ticket-price/dynamic-pricing angle
scored highest (43/45, freshest demand: BBC ~1M, Business Insider ~893K, Bloomberg ~410K,
all within a month) and was recommended; the user still chose their own host-economics
angle (39/45; CNBC ~1M evergreen proof). Persisted as
`projects/6-why-countries-fight-to-host-the-world-cup/00-topic-intake.md`.

Lesson:
When the user brings their own angle and asks "or choose better," present the
better-scoring sibling honestly, but expect the user's own angle to win even against a
higher score - ownership and taste beat a 4-point scorecard gap, and both were above
threshold so both were legitimate. The recommendation's job is to inform, not override.
Also: before persisting, a parallel fact-check workflow on the topic's anchor claims (7
claims, one web-verification agent each) caught a would-be scripting error - USA 1994 is
NOT a host-economics success story (host metros came in $5.5-9.3B BELOW forecast; only the
organizing committee profited; the real exceptions are LA 1984 and Barcelona 1992). The
verified facts + honesty rails went into the intake file as a "Verified Anchor Facts"
table so research and script inherit them.

Apply next time:
- User-brought angle above threshold + explicit pick = persist it; log the higher-scored
  sibling as parked, not as a pushback.
- For any topic whose whole premise is an economics/history claim, run the anchor-claim
  verification pass BEFORE writing the intake, and bake a dated verified-facts table +
  "Must Stay Honest" rails into `00-topic-intake.md`.
- Parked candidate worth resurrecting: "Why World Cup Tickets Cost $6,000 One Day and $600
  the Next" (dynamic pricing, 43/45 on 2026-07-02, evidence: BBC ~1M, Business Insider
  ~893K, Bloomberg ~410K, StubHub class action + 4 US state probes). Strongest while the
  tournament runs (final: 2026-07-19); the mechanism (surge pricing everywhere: Uber,
  flights, concerts) keeps a longer shelf life if reframed away from the tournament.

Promote to shared memory:
no, this is topic-intake intake-mode and verification behavior, not a channel-wide change.

### 2026-07-08 - P6 shipped as the best video ever: its intake STRUCTURE is now the standard

Classification: `Topic intake lesson`

Context:
`6-why-countries-fight-to-host-the-world-cup` shipped and the owner called it the best video the channel
has made, asking to raise every skill to match it. The 2026-07-02 entry above logged HOW the topic was
picked; this confirms the intake FILE STRUCTURE as the template, because the downstream quality traces
directly back to what the intake pre-decided.

Lesson (make every future `00-topic-intake.md` carry these, because P6's did and it paid off end-to-end):
- A `## Angle Package` written as `topic + contradiction + visual metaphor + viewer pain` - and a named
  RECURRING MOTIF SEED + WIT-ARC SEED right there at intake (P6 seeded "trophy prints an endless receipt"
  and the euphoric-fan -> lone-guy-with-receipt arc). The motif that carries the whole finished video was
  chosen at step 0, not discovered later.
- A `## The Real Mechanism` numbered chain (promise -> reality -> contract -> leftovers -> why-still -> the
  live twist) that grounds BOTH research and script so the spine is stable from the start.
- A `## Must Stay Honest` rails block + a dated `## Verified Anchor Facts` table (one web-verification
  agent per anchor claim) for any topic whose premise is an economics/history claim - research and script
  INHERIT these rails, which is what kept a stat-dense video accurate and un-rewritten.
- Dual scorecards (channel template /40 + batch /45) and 3-signal demand evidence (YouTube views + Google
  Trends + news volume) with real links, so "why now" and "why this angle" are evidenced, not asserted.
- An `## Interesting-English Value` block naming the reusable phrases + on-screen gloss targets, so learner
  value is designed in from step 0.

Apply next time: treat the P6 intake as the section-by-section template for any evidence-heavy trending
topic; the motif seed + honesty rails at intake are the highest-leverage, cheapest quality investment in
the whole pipeline.

Promote to shared memory:
partly - "seed the recurring motif + WIT arc at intake" and "honesty rails + verified-facts table for
claim-based premises" are channel-wide; fold into `_shared/systems/topic-packaging-hooks.md` next pass.

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Topic intake lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
