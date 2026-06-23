# Script Draft Skill Memory

This file stores memory specific to the `script-draft` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about selecting projects, shaping sectioned scripts, preserving source claims, improving WIT arcs, and making scripts easier to voice and board.

## Current Skill Standard

- Select the project before drafting.
- Smart-select a project only when context is clear or exactly one unfinished script candidate exists.
- Require real, non-empty `00-topic-intake.md` and `01-research-pack.md`.
- If both are missing, stop and ask for `topic-intake`, then `research-pack`, then rerun `script-draft`.
- If `00-topic-intake.md` is missing, stop and ask the user to run `topic-intake`.
- If `01-research-pack.md` is missing, stop and ask the user to run `research-pack` after topic intake exists.
- If the research pack is older than the topic intake, treat it as stale and require `research-pack` before drafting.
- Write only `projects/<slug>/02-script.md`.
- When `02-script.md` is created, updated, or rerun, treat `04-09` main-pipeline outputs as stale, starting with `04-voiceover.md`. Do not mark packaging stale.
- Do not delete stale downstream outputs unless the user explicitly asks; otherwise tell the user to rerun downstream skills in order.
- Use `projects/why-everyone-pretends-to-be-busy/02-script.md` as the structural reference when available.
- Copy the reference script's discipline, not its topic, jokes, or wording.
- Draft in sections with estimates, word counts, purpose, visual goal, narration, approval checks, and voice revision notes.
- Treat `01-research-pack.md` as the claim source of truth.
- Label risky ideas as inferences or avoid them.
- Keep the script learner-friendly, dry, concrete, and boardable.
- Stop before voiceover, visual plan, render, review, upload, or learning.
- After creating or updating a script, respond in chat with status, estimated duration, a `3-5` line brief, and the section summary table.
- Do not paste the full script into chat unless the user asks.

## Script Draft Output Standard

A good script draft should make the next voice revision easy.

It should include:

- one core thesis
- one recurring motif
- one WIT emotional arc
- a section summary table
- sectioned narration blocks
- visual goals, not full visual plans
- approval checks for future section review
- claim safety notes
- English learner notes
- a clear next-step boundary
- a concise chat response that helps the user review the output quickly

## Chat Response Lesson

After writing `02-script.md`, the user wants the chat response to include:

- script status
- estimated duration
- a `3-5` line brief for the entire script
- section summary

Apply every run. This is part of the skill output contract, not a reason to rerun the skill.

## Reference Script Lesson

The current best reference is `Why Everyone Pretends To Be Busy`.

Useful structure to preserve:

- section summary table before the full script
- each section has a job, visual goal, narration, and approval checks
- section names describe the hidden mechanism, not generic chapter numbers
- script can be implemented one section at a time
- humor comes from the system happening to WIT
- final payoff restates the useful insight in simple English

Do not preserve:

- exact number of sections
- workplace topic structure
- exact jokes
- exact pacing
- exact labels

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `script-draft` as step 3 of the sequential Why It Works video-production skill system.

Initial rules:

- require topic intake and research pack
- write only `02-script.md`
- structure scripts into sections
- keep claims tied to research
- include WIT, learner clarity, visual goals, and approval checks
- keep skill-specific learning here and promote only reusable channel-wide lessons upward

### 2026-06-06 - Chat Summary Required

Classification: `Script draft lesson`

Context:
After running the first script draft, the user clarified that the skill should respond in chat with a quick summary of the script output.

Lesson:
The written file is the main artifact, but the chat response must make the script easy to judge quickly.

Apply next time:
Include status, estimated duration, `3-5` line brief, and section summary in chat after creating or updating `02-script.md`. Do not rerun the skill only to produce this summary.

Promote to shared memory:
No. This is specific to the `script-draft` skill response contract.

### 2026-06-06 - Require Previous Outputs And Stale Downstream

Classification: `Operational lesson`

Context:
The user clarified that `script-draft` should run only after Topic Intake and Research Pack outputs exist, and that rerunning previous steps should stale later outputs.

Lesson:
`script-draft` is a main-pipeline step, not a standalone writer. It must build from `00-topic-intake.md` and `01-research-pack.md`, and its own rerun makes voiceover, visual plan, render, review, upload, and learning files stale. Packaging is a side branch and should not be marked stale by script changes.

Apply next time:

- require non-empty `00-topic-intake.md` and `01-research-pack.md`
- if one or both are missing, stop and name the missing skill(s)
- if the research pack is older than the topic intake, require `research-pack` rerun before drafting
- after writing `02-script.md`, list stale downstream outputs from `04-voiceover.md` through `09-self-learning.md`
- do not remove stale files unless the user explicitly asks

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-07 - Packaging Hard Prerequisite Exception

Classification: `Core operational update`

Context:
The user clarified that packaging requires only topic intake and research pack, but script remains before packaging in the production order.

Lesson:
`script-draft` remains in the main pipeline and does not require packaging. Packaging is outside the main pipeline.

Apply next time:

- require non-empty `00-topic-intake.md` and `01-research-pack.md`
- after writing `02-script.md`, list stale downstream main-pipeline outputs from `04-voiceover.md` onward
- do not require `03-packaging.md` before drafting

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-23 - Owner Wants Denser, Trend-Aware Humor (And Devices As Motif)

Classification: `Script draft lesson`

Context:
On `why-everything-is-a-subscription-now`, the owner reviewed rev 1 and asked for a funnier script:
dad jokes, jokes "trending now on the internet," and even dark jokes — explicitly "as long as it
doesn't harm anyone." He also asked to swap the abstract `$/mo tag` motif for concrete devices
(phone, laptop, monitor, car screen), and reminded the skill to browse YouTube/the internet so the
video lands with viewers. Quote: "I love joking in the video."

Lesson:
This creator wants a higher humor density than rev-1 dry-explainer baseline, and he wants the comedy
to feel current. Default future scripts toward more jokes — but keep them learner-safe and
guardrail-safe. Concrete object/device motifs beat abstract symbols for him.

Apply next time:

- Aim for a joke roughly every 15-25s (denser than the 20-40s baseline), still "joke supports clarity."
- Build a short "Humor System" block in the script: list the running gag, pun types, and trending
  formats used, plus a 1-line reference table for the jokes/demand browsed.
- Trending/meme/slang lines MUST be paired with an on-screen visual and a one-line gloss in English
  Learner Notes, because the channel bans jokes that need native-only cultural knowledge.
- Dark jokes allowed ONLY if self-aimed/absurd and targeting the *system*, never a person, group, or
  protected category, and never encouraging real harm. Add a "Humor Safety" sub-section to Claim Safety.
- A recognized meme FORMAT adapted to the topic (e.g. "your free trial of ___ has expired" for a
  subscription video) is a strong, reusable running gag — adapt the format, don't copy a specific line.
- Prefer concrete real objects/devices as the recurring motif over abstract tags/symbols.
- Still browse YouTube for demand + current comedic packaging every script revision he asks to "make funnier."

Promote to shared memory:
yes — logged as an Experiment in `learning-log.md` (humor density is a tunable channel preference to
validate against retention, not yet a foundation rewrite). Do not change `channel-foundation.md`
voice/tone without explicit owner confirmation.

### 2026-06-23 - Hooks Must Open A Curiosity Gap, Not Set A Scene

Classification: `Script draft lesson`

Context:
On `why-everything-is-a-subscription-now`, the owner rejected a hook that opened with a calm
scene-setter ("It's a normal morning. You pick up your phone..."). His note: a slow situational
open does not attract viewers; "you should raise curiosity on viewer first."

Lesson:
The channel's first-10-seconds rule (situation → suspicious detail → WIT reaction → bigger question)
is right, but the FIRST SPOKEN LINE must itself be a curiosity gap, not throat-clearing. A calm
"normal morning / you do X" open buries the hook. Lead with a question the viewer can't answer about
their own life, a surprising claim, or a contradiction — then reveal.

Apply next time:

- Open S1 with one of: a direct question about the viewer ("How many subscriptions are you paying
  for right now? It's higher than you think"), a surprising/counterintuitive claim, or a sharp
  contradiction. Make the viewer feel a gap they want closed within the first 1-2 lines.
- No "It's a normal [time]. You [do ordinary thing]." openers. No branding, no definitions, no
  "In this video." (already a hard fail).
- Still hit the rest of the 10s beats (topic by ~3s, contradiction by ~5s, WIT emotion by ~8s,
  title promise by ~10s) AFTER the curiosity line.
- The motif/running gag can stay, but as a beat inside the hook, not as the opening line.

Promote to shared memory:
no — the channel-foundation first-10s rule already covers this; this is a sharper script-draft
execution note (lead-line must be the curiosity gap).

### 2026-06-24 - Owner Wants Shorter + Cheeky/"Slightly Rude" Register

Classification: `Script draft lesson`

Context:
On `why-buy-1-get-1-beats-50-off`, after a clean dry-explainer rev 1 (~5:30, 1026 words), the owner
said: "the script is pretty long, make it shorter a bit, more joke, you can [be] something rude (but
slightly), make it less serious and more funny." Rev 2 trimmed to ~4:32 / ~855 words and added a
cheeky edge ("you are the rabbit", "not the first sucker, just the latest", "your brain goes a little
stupid", "go be slightly harder to trick").

Lesson:
This creator's comedy taste extends past dry-deadpan into a light cheeky/roast register, AND he
prefers tighter runtime. "Slightly rude" = affectionate roasting of the *trick*, the concept, and the
viewer's own brain/wallet/fridge — never a person, group, brand, or protected category, and no
profanity (channel stays learner-clean). Pairs with the 2026-06-23 denser-humor experiment.

Apply next time:
- Default new scripts toward tighter (don't pad) + denser jokes (~every 12-20s), and offer a cheeky
  register option early for this owner.
- Cheeky lines must be self-aimed or system-aimed only; keep a "Humor Safety" sub-section listing the
  vetted edgy lines, and gloss any cheeky phrase ("you're the rabbit", "sucker", "inner accountant")
  in English Learner Notes so the joke isn't native-only.
- Keep the math/claim honesty even while funnier (the loss-leader "when the store loses" turn stays).
- A script tone/length rewrite restales already-generated section voiceover — regenerate the affected
  section(s) and reset the `04-voiceover.md` index.

Promote to shared memory:
no — sharpens the existing humor-density experiment for this owner; do not change
`channel-foundation.md` voice/tone without explicit confirmation. Revisit promoting a "cheeky register"
note if he confirms the style across more videos.

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Script draft lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
