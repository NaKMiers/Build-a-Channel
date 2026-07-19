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
- Use `projects/2-why-everyone-pretends-to-be-busy/02-script.md` as the structural reference when available.
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
dad jokes, jokes "trending now on the internet," and even dark jokes - explicitly "as long as it
doesn't harm anyone." He also asked to swap the abstract `$/mo tag` motif for concrete devices
(phone, laptop, monitor, car screen), and reminded the skill to browse YouTube/the internet so the
video lands with viewers. Quote: "I love joking in the video."

Lesson:
This creator wants a higher humor density than rev-1 dry-explainer baseline, and he wants the comedy
to feel current. Default future scripts toward more jokes - but keep them learner-safe and
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
  subscription video) is a strong, reusable running gag - adapt the format, don't copy a specific line.
- Prefer concrete real objects/devices as the recurring motif over abstract tags/symbols.
- Still browse YouTube for demand + current comedic packaging every script revision he asks to "make funnier."

Promote to shared memory:
yes - logged as an Experiment in `learning-log.md` (humor density is a tunable channel preference to
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
their own life, a surprising claim, or a contradiction - then reveal.

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
no - the channel-foundation first-10s rule already covers this; this is a sharper script-draft
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
viewer's own brain/wallet/fridge - never a person, group, brand, or protected category, and no
profanity (channel stays learner-clean). Pairs with the 2026-06-23 denser-humor experiment.

Apply next time:
- Default new scripts toward tighter (don't pad) + denser jokes (~every 12-20s), and offer a cheeky
  register option early for this owner.
- Cheeky lines must be self-aimed or system-aimed only; keep a "Humor Safety" sub-section listing the
  vetted edgy lines, and gloss any cheeky phrase ("you're the rabbit", "sucker", "inner accountant")
  in English Learner Notes so the joke isn't native-only.
- Keep the math/claim honesty even while funnier (the loss-leader "when the store loses" turn stays).
- A script tone/length rewrite restales already-generated section voiceover - regenerate the affected
  section(s) and reset the `04-voiceover.md` index.

Promote to shared memory:
no - sharpens the existing humor-density experiment for this owner; do not change
`channel-foundation.md` voice/tone without explicit confirmation. Revisit promoting a "cheeky register"
note if he confirms the style across more videos.

### 2026-06-24 - Speak The Math Aloud (Learner Clarity On Number Beats)

Classification: `Script draft lesson`

Context:
On `why-buy-1-get-1-beats-50-off` Section 2, the owner generated the voiceover, listened, and said
he could not even understand it - the store-side math was confusing. Root cause: the script stated
the profit results ($1 for 50%-off, $2 for BOGO) without ever speaking the subtraction, so a learner
heard "you pay five... the store keeps one dollar" with no audible bridge from $5 paid to $1 kept.
It also flipped pronouns ("Stand behind the counter... you" = store, but "you" = shopper everywhere
else). Fix: say the arithmetic out loud ("Five minus four - the store keeps one dollar" /
"Ten minus eight - the store keeps two dollars") and keep "you" = shopper, "the store" = seller.

Lesson:
For an English-learner channel, any number beat must be VOICED as the operation, not just the result.
If a profit/price/total is the payoff of a calculation, speak the calculation ("X minus Y -") right
before the result so the listener can follow by ear, not only by reading the on-screen tag. Also keep
one stable referent per pronoun across the whole video; a "pretend you're the store" framing that
reuses "you" for the seller confuses learners who have "you" = viewer everywhere else - prefer naming
"the store" in third person.

Apply next time:
- When a section hinges on math, write the subtraction/addition into the narration ("five minus four"),
  put a `[beat]` before the result, and `[slower]` on the operation line.
- Mirror it in the Visual goal so the on-screen tag shows the same operation (`$5 − $4 = $1`), not just
  the answer - audio and screen reinforce the same derivation.
- Avoid pronoun flips: keep "you" = the viewer/shopper; name other actors ("the store", "the seller")
  explicitly rather than reusing "you".
- A clarity rewrite of one section restales only that section's voiceover - regenerate just that
  section and reset its `04-voiceover.md` row, not the whole video.

Promote to shared memory:
no for now - strong learner-clarity execution note; revisit promoting a one-line "speak the math
aloud / one referent per pronoun" rule into `script-learner-voice.md` if it recurs on another video.

### 2026-06-28 - Speak a mechanism step-by-step (extends "speak the math aloud"); edgy topic word can carry the tone

Classification: `Script draft lesson`

Context:
Drafted `5-why-the-internet-is-full-of-ai-slop` (AI slop). The core of the video is a 5-step incentive
chain (cost collapse -> pay-for-attention -> flood the zone -> blind algorithm -> money loop). Wrote it
as numbered spoken steps ("Step one... Step two...") with `[slower]` on the key line, mirroring the
on-screen conveyor-belt steps - the same principle as the 2026-06-24 "speak the math aloud" learner rule,
but applied to a causal mechanism, not arithmetic. Also: the channel's edgy tone is now approved, but this
topic needed no profanity - the topic words "slop / garbage / junk" plus system-aimed cheek ("you cannot
arrest an incentive," "it's dumber than that") carried the edge while keeping the title/thumbnail/first-7s
clean. Built the honest turn into its own section (not all AI is slop; reject the dead-internet conspiracy)
so the video cannot read as AI-panic.

Lesson:
For any "why does this system work this way" video, voice the mechanism as ordered, spoken steps that the
learner can follow by ear, and mirror each step in the visual goal - generalize "speak the math aloud" to
"speak the mechanism aloud." Edge does not require profanity; let the topic's own vocabulary and
system-aimed roasting carry the attitude, and keep the strongest words out of the first 7s/title/thumbnail.
Give a "honest turn" its own section whenever the topic could be mistaken for panic or a conspiracy.

Apply next time:
- Causal/mechanism payload -> numbered spoken steps, `[slower]` on the pivot line, visual mirrors the steps.
- Reach for topic-word edge + system-aimed cheek before profanity; protect monetization-safe placement.
- For panic-prone topics (AI, scams, health), write a dedicated honest-turn section with the reject line.

Promote to shared memory:
no - sharpens existing learner-clarity + tone notes; revisit promoting a one-line "speak the mechanism
aloud" rule into `script-learner-voice.md` if it recurs on another mechanism-heavy video.

### 2026-06-29 - Owner wants a like/share/subscribe OUTRO (reverses the "no spammy CTA" default)

Classification: `Script draft lesson` (candidate `Experiment` for the channel)

Context:
On `5-why-the-internet-is-full-of-ai-slop`, after the script was finished with a deliberate no-CTA close
(S7 ended dry, non-preachy - matching the channel's standing "no spammy CTA" guardrail), the owner asked
to ADD a like/share/subscribe segment at the very end as a new Section 8 ("ở cuối video phải có đoạn yêu
cầu like share subscribe"). Added Section 8 "Outro: Use The Machine": a short CTA that names like/share/
subscribe explicitly but is EARNED by the video's own thesis (the internet is an attention machine, so
the CTA reframes engaging as the viewer USING that machine for "more of this, less slop"), system-aimed
and dry, not begging. Kept S1-S7 unchanged; strongest words / hook / title / thumbnail still carry no CTA.

Lesson:
This owner DOES want an explicit like/share/subscribe outro - the prior "no spammy CTA" rule is not
absolute for him. When adding a CTA, keep it on-brand: a short final section, tied to the video's own
motif/insight so it reads as a payoff not a plug; name like/share/subscribe simply (learner-clear) with
one concrete reason each; stay system/self-aimed and warm, never guilt-trip; protect monetization-safe
placement (no CTA in the first 7s/title/thumbnail).

Apply next time:
- Default to offering a short on-brand CTA outro section for this owner; tie it to the episode's metaphor.
- Adding an outro section does NOT restale S1-S(n-1) narration; only the NEW section needs the full
  per-section pipeline (voiceover -> visual-plan -> visual-implement -> render), and whole-video steps
  (combine/caption/packaging) must include it when run.

Promote to shared memory:
not yet - this conflicts with the existing "no spammy CTA" note in channel-guardrails/packaging. Log here
as a per-owner preference; promote to `learning-log.md` as an Experiment (and reconcile the guardrail) only
after the owner confirms it should be the standing close for ALL videos.

### 2026-07-02 - Pre-delivery 3-lens adversarial review catches what one pass cannot

Classification: `Script draft lesson`

Context:
Drafted `6-why-countries-fight-to-host-the-world-cup` (host-economics, evidence-heavy
topic). Before reporting to the owner, ran a 3-agent adversarial review workflow (lenses:
factual honesty vs research pack, B1-learner clarity/voiceability, engagement/channel
rules), each agent reading the draft + research pack from disk. It caught 24 findings,
including: a genuine factual error ("the LAST host that made a profit was LA 1984" -
contradicted by the pack's own Barcelona 1992 exception); a killer-stat inversion risk
(the "[slower] Two fifty" echo can be heard as 250, not $2.50 - the units must survive
the echo); a silent punchline failure (Zurich never glossed, so the S5 "leaks toward
Zurich" joke dies for B1 learners); "cycle" jargon silently undoing the revenue-honesty
rail; the hook naming the topic word only at ~14s (past the ~10s title-payoff window);
and an over-generalized per-city cost claim ("$100M+ each" spoken over Mexico when the
pack scopes it to US cities). Applied all must/should fixes in rev 2.

Lesson:
For evidence-heavy scripts, a self-pass is not enough: run the 3-lens adversarial review
(honesty / learner / engagement) between draft and delivery. Specific reusable rules it
produced: (1) SPOKEN NUMBER ECHOES MUST KEEP THEIR UNITS ("Two dollars fifty", never
"Two fifty") - the echo is the part learners remember; (2) any place-name punchline
(Zurich) needs its gloss planted in an earlier section; (3) hedges must survive
compression - a superlative ("the last", "every single time") sneaks in where the pack
only supports "one of the only" / "every time anyone has counted"; (4) the topic noun
belongs inside the FIRST spoken line when the video rides a live trend; (5) an announced
numbered scaffold ("step one... step two") must either complete or be dropped; (6) keep a
real-name rule in the Humor System: neutral factual celebrity references OK, real people
as joke targets banned.

Apply next time:
- Evidence-heavy or claim-dense script -> 3-lens adversarial review workflow before the
  chat summary; apply must/should fixes; note rev 2 in the script header.
- Write number echoes with units; gloss punchline place-names early; audit every
  superlative against the pack; topic word in line one on trend-timed videos.

Promote to shared memory:
no - this is script-draft QA process; revisit promoting "number echoes keep units" into
`script-learner-voice.md` if it recurs.

### 2026-07-08 - P6 script craft: motif-as-thesis-object + one-number-on-a-prop + Humor System block (owner's best video)

Classification: `Script draft lesson`

Context:
The owner named `6-why-countries-fight-to-host-the-world-cup` the best video the channel has made and
asked to raise every skill's bar to match it. The 3-lens review and on-brand CTA outro were already
logged; a full re-read of `02-script.md` (rev 2) surfaces the STRUCTURAL script choices that made the
downstream skills succeed. Now codified in SKILL.md ("Motif, Numbers, and Humor System").

Lesson (apply to future scripts, especially evidence-heavy ones):
- RECURRING MOTIF = A THESIS OBJECT. The receipt is not decoration: it is born in the hook ("the trophy
  prints a receipt"), gains one item per section, and the payoff line IS the motif ("check whose name is
  on the receipt"). Choose an object that literally is the argument; name it (plus any secondary motif)
  in Draft Strategy, with a one-line WIT emotional arc (one state per section).
- ONE NUMBER PER BEAT, EVERY NUMBER ON A PROP. P6 is stat-dense but never lectures because no sentence
  stacks two figures and each number lands on a physical object (price tag, receipt line, counter, gauge),
  called out in that section's Visual goal. This single rule is the difference between "explainer" and
  "documentary essay".
- A `Humor System` BLOCK near the top: running gag + register (dry/cheeky/system-aimed) + a bank of vetted
  cheeky lines ("a chess club with four billion in reserves"; "a horoscope with a spreadsheet"; "the
  world's most expensive selfie") + the real-name rule (neutral factual celebrity mentions OK - "And Bruno
  Mars." - real people as joke targets banned). Deliberate comedy, safe and consistent edge.
- PER-SECTION BUTTONS that hand off to the next section ("the money leaves with the guests." -> "Then the
  tournament ends..."). Each section ends on the quotable line.
- PRE-LOAD DOWNSTREAM: each section carries Purpose + Visual goal (motif beat + which number on which prop)
  + Narration + Approval check + Voice revision notes ([beat]/[slower]/[deadpan] placement, which lines to
  isolate). A `Claim Safety Notes` block (Safe / Inferences used carefully / Claims avoided / Humor safety)
  and `English Learner Notes` (in-line glosses, jargon deliberately avoided) make honesty and learner-fit
  auditable. This is why P6's voiceover, visual-plan, and captions all landed on the first serious pass.

Apply next time:
- Draft Strategy block first (core thesis / motif + secondary motif / WIT arc / risk + mitigation), then
  a Humor System block, then sections that each pre-load visual-plan + voiceover.
- Enforce one-number-per-beat-on-a-prop while drafting, not in review.

Promote to shared memory:
partly - "one number per beat, every number on a prop" and "recurring motif = thesis object" are
channel-wide; fold them into `_shared/systems/script-learner-voice.md` on the next shared-memory pass.

### 2026-07-19 - Alan (ElevenLabs) reads ~2x Kokoro pace: word-count-to-runtime math changed; practical "spot it" section fights doom AND adds runtime value

Classification: `Script draft lesson`

Context:
Drafted `7-why-you-cant-get-your-first-job` ("The 4 Reasons You Can't Get Your First Job Anymore" -
number-first title per the locked packaging rule). Ran the required 3-lens adversarial review (honesty /
B1 learner / engagement); 40+ findings, all must/should fixes applied in rev 2.

Lesson:
1. **Runtime math changed with the new voice.** The old 140-150 wpm learner-pace assumption came from
   Kokoro at 0.84. The NEW official voice Alan (ElevenLabs) measures ~229 wpm at speed 1.0, ~207 at 0.9,
   ~193 at 0.85 (from real generated demos). So ~1,200 words = only ~6:30-7:10 of video, NOT 8+. To hit
   the 8:00 mid-roll threshold needs ~1,500-1,650 words of REAL value - or accept a shorter video (the
   channel rule bans padding). Always estimate runtime from the MEASURED voice pace, and surface the
   trade-off to the owner instead of silently inflating word counts (rev 1's counts were ~15-20% inflated
   - the engagement reviewer caught it).
2. Review catches that matter, now standing rules: (a) stat UNITS must match the pack exactly (rev 1 said
   "postings 7x more likely to demand senior skills"; the pack's 52%-vs-7% is about the share of NEW
   SKILLS - a different claim); (b) superlatives must stay scoped ("fastest-growing kind of ENTRY-LEVEL
   job", never "on the whole ladder"); (c) the motif WORD itself must be glossed at first use for B1 ears
   ("each step is called a rung") and B1-hostile verbs swapped ("saw off" -> "cut off"); (d) number beats
   need human units by ear ("about four PEOPLE", not "about four"); (e) don't punch at an age group
   ("everyone over forty" -> "the classic advice").
3. **A practical "how to spot it" section** (3 hedged tells, "commonly reported - no promises") is a
   triple win on bleak topics: gives the viewer agency (anti-doom), is the most shareable beat, and adds
   honest runtime without padding. Pattern: reasons -> honest turn -> practical tells -> hopeful payoff -> CTA.
4. Pattern-break one mid-video section by cold-opening on the absurd artifact BEFORE the "Reason N"
   announce (S5's listing read) - kills the predictable reason-section rhythm.

Apply next time:
- Compute runtime from measured Alan wpm (speed 0.85-0.9 => ~190-210 wpm); state honest per-section word counts.
- Keep the 3-lens review mandatory for claim-dense scripts; fix stat units against the pack verbatim.
- Gloss the motif word at first use; give every number a human unit by ear.
- Offer a practical "spot it / do this" section on any doom-prone topic.

Promote to shared memory:
partly - the Alan wpm numbers belong wherever voiceover timing is planned (voiceover skill memory should
mirror them); the rest is script-draft craft.

### 2026-07-19 - Keep WIT silent in narration; simplify cognitive pace, not only sentence length

Classification: `Script draft lesson`

Context:
The owner reviewed rev 2 of `7-why-you-cant-get-your-first-job` and flagged three connected problems:
the narration said `Meet WIT` even though a new viewer does not know that internal mascot name; the script
felt fast despite short sentences; and several words and jokes needed too much English or cultural context.
(Historical note: this review happened during the short-lived "SIMPLE + CONSISTENT" style experiment,
which the owner REJECTED on 2026-07-19 and fully reverted - see learning-log "FAILED EXPERIMENT". The
LEARNER-PACE lessons below stand on their own and remain valid under the restored P6 standard.)

Lesson:
`WIT` is an internal production name, not required viewer knowledge. Keep WIT as a silent audience
surrogate in visual goals, but never speak the name in narration unless a future video explicitly earns
and explains a character introduction. A script can also feel fast even when its sentences are short if
it stacks a claim, number, definition, qualifier, and joke in one breath. Learner pace is cognitive pace:
one important idea at a time, common words first, visible jokes, and a repeated story object that reduces
the amount the viewer must remember.

Apply next time:
- Audit every narration block for internal labels such as `WIT`; introduce character through visible
  action, not unexplained lore or names.
- Give each section one clear question and one section button.
- Do not stack a new statistic, new term, and punchline in the same breath.
- Prefer jokes that are visible from the scene and understandable without slang, memes, public figures,
  or native-only knowledge.
- Use pauses and repeated plain labels to slow comprehension; do not rely on slower TTS alone.
- Script visual goals follow the P6 standard (per-sentence scenes, thesis-object motif, one number per
  beat on a prop) - the "held boards / SIMPLE + CONSISTENT" phrasing that briefly lived here was part of
  the rejected 2026-07-18 experiment and no longer applies.

Promote to shared memory:
partly. Common-word learner clarity and contextual jokes are already channel-wide Core rules. The unique
`WIT is an internal name, not spoken viewer knowledge` rule stays here unless it recurs in another
production system.

### 2026-07-19 - A numbered-title hook should promise the count without revealing the answers

Classification: `Script draft lesson`

Context:
The owner wanted the hook for `7-why-you-cant-get-your-first-job` to say clearly that the video contains
four reasons. The first revision then over-corrected by naming Reason 1, 2, 3, and 4 inside the hook. The
owner rejected that because revealing the full content map removed the curiosity that should carry the
viewer into the body.

Lesson:
When the title promises a numbered list, the hook should confirm the count but preserve the answers as
open loops. Say one clear line such as `Here are the four reasons you can't get your first job anymore`,
show one matching `4 REASONS` label, and move into Reason 1. Do not preview all four reasons unless the
video is intentionally a roadmap-first tutorial. In a curiosity-driven explainer, each reason is a reveal.

Apply next time:
- Put the promised number inside the first 10 seconds.
- State the title promise in one direct sentence.
- Do not name or summarize all the reasons in the hook.
- Mirror the promise with one count label such as `4 REASONS`, not a four-item preview.
- End the hook with a direct handoff into `Reason one`.
- Let the body reveal each reason one at a time.

Promote to shared memory:
no for now. This is a reusable script-draft execution rule already compatible with the channel's existing
first-10-seconds promise system.

### 2026-07-19 - Build a paid-off cliffhanger chain across sections

Classification: `Script draft lesson`

Context:
The owner asked for every section of `7-why-you-cant-get-your-first-job` to end with a cliffhanger that
pulls the viewer into the next section and continues that chain until the end of the video.

Lesson:
A useful section cliffhanger is not a random tease. The section must first answer its own question and
deliver a mini-payoff. Its final line then opens one specific missing question, and the next section must
begin by answering that exact question. This creates forward pull without breaking trust. The penultimate
section may tease the on-theme CTA, but the final section must close the video rather than opening a fake
loop.

Apply next time:
- Write the transition chain before polishing individual section endings.
- End Sections 1 through the penultimate section with one short, B1-clear open question or incomplete
  consequence.
- Make the next section answer that line immediately; never postpone the promised answer.
- Keep each cliffhanger tied to the thesis object or the mechanism already on screen.
- Avoid repeated empty phrases such as `but it gets worse` or exaggerated danger language.
- Let the final section deliver closure with no new unresolved promise.

Promote to shared memory:
no for now. The script skill already requires section buttons; this sharpens them into a connected
retention chain and should stay in skill memory until confirmed across another video.

### 2026-07-19 - CTA needs a value exchange and a thematic payoff

Classification: `Script draft lesson`

Context:
After the cliffhanger pass on `7-why-you-cant-get-your-first-job`, the owner found the final subscribe
and like request shallow. The outro mentioned actions quickly but did not make the viewer feel why each
action mattered, and it failed to turn the video's job-listing motif into a satisfying final payoff.

Lesson:
An earned CTA is not a checklist of platform verbs. Give each requested action one concrete value
exchange: like signals that the explanation was useful and helps distribution; share helps one specific
person who needs the insight; subscribe promises the exact kind of future content the channel makes.
Then close on the episode's motif so the CTA feels like the final joke, not an ad attached after the
ending.

Apply next time:
- Audit that `like`, `share`, and `subscribe` are all spoken when the owner expects all three.
- Give each action one short, viewer-centered reason.
- State the future-content promise specifically, not `more videos` in general.
- Tie the CTA visual and final line to the video's thesis object or running gag.
- Deliver the actions as separate beats; do not rush them into one sentence.
- End with warmth and closure, never guilt, begging, or a new unresolved promise.

Promote to shared memory:
no for now. This is a script-draft execution lesson that sharpens the existing owner CTA preference.

### 2026-07-20 - End the hook on count plus practical promise; keep CTA in a separate outro

Classification: `Script draft lesson`

Context:
On the recreated `7-why-you-cant-get-your-first-job` rev 2, the owner asked for three connected changes. The hook needed to END on a line promising the four reasons plus how to move forward. Every section needed a paid-off cliffhanger into the next section. The like/share/subscribe ending needed to follow video 6, where the core payoff and the CTA are separate sections. The embedded CTA inside the payoff did not read as a real ending.

Lesson:
A numbered explainer hook should close on `count + problem + practical payoff`, while still hiding the answers. The body should form an explicit question-and-answer chain: each section finishes its own point, then asks one question or names one action that the next section answers immediately. The thematic payoff must finish before platform requests begin. Like, share, and subscribe belong in a separate named `Outro` section tied to the episode motif, with one clear value exchange per action and a final motif line.

Apply next time:

- End the hook with a direct line such as `Here are four reasons X is happening, and how to Y.`
- Do not reveal the four answers in the hook.
- Audit every section ending and the next section opening as a matched pair.
- Keep the payoff section free of platform requests until its core insight has landed.
- Add a separate CTA outro modeled on the structural discipline of video 6, without copying its wording.
- Speak `like`, `share`, and `subscribe` as separate beats when the owner requests all three.
- Close the final outro on the episode's thesis object with no new cliffhanger.

Promote to shared memory:
no. This consolidates existing script-draft hook, cliffhanger, and CTA lessons into a clearer execution rule.

### 2026-07-20 - Vary cliffhanger devices so the chain does not feel templated

Classification: `Script draft lesson`

Context:
The owner said the cliffhangers at the end of each section felt too similar. The chain technically worked, but repeated direct questions made the writing sound like a visible formula.

Lesson:
A retention chain does not require every section to end with a question. Rotate the handoff device while keeping the promise specific and the next-section payoff immediate. Useful devices include a count promise, image transformation, paradox, evidence tease, pattern reveal, action command, withheld verdict, and person-specific handoff.

Apply next time:

- Design the handoff sequence across the whole script before polishing individual section endings.
- Audit repeated grammar such as `But what if`, `But why`, and `one useful question`.
- Keep each button short, quotable, tied to the thesis object, and immediately paid off.
- Let the final section close without a new open loop.

Promote to shared memory:
no. This is a script-specific craft refinement of the existing retention-chain rule.

### 2026-07-20 - Replace a flat listing hook with a self-contained paradox

Classification: `Script draft lesson`

Context:
The owner rejected the `entry-level, three years required` opening in rev 4 as not strong enough and asked for a complete hook rewrite. The example stated the topic, but it did not transform the contradiction into a fresh enough curiosity event.

Lesson:
When a familiar job-listing contradiction feels flat, compress the mechanism into a self-contained paradox, transform the thesis object on screen, add one dry reaction, and then deliver the numbered promise. For this topic, `job -> experience -> job` bends the career ladder into a circle before the script promises the four reasons and the way in.

Apply next time:

- Do not assume a recognizable frustrating example is automatically a strong hook.
- Make the first line contain the mechanism or paradox, not just an artifact from the topic.
- Let the visual object transform before the promise line so the hook creates a memorable image.
- Keep the final hook line as `count + problem + practical payoff` without revealing the answers.

Promote to shared memory:
no. This is a script-draft execution lesson from one rejected hook and should be tested on future videos before wider promotion.

### 2026-07-20 - Ground the paradox in a second-person viewer scenario

Classification: `Script draft lesson`

Context:
After rev 5 compressed the hook directly into the experience-job paradox, the owner provided a preferred demo: begin with a recent graduate finding an entry-level job, reveal the three-year requirement, explain the job-experience loop, turn the ladder into a circle, and only then deliver the four-reason promise.

Lesson:
For this topic, the owner prefers the abstract paradox to grow out of a concrete second-person story. The sequence should let the viewer feel one moment of relief at finding an entry-level listing before the requirement reverses it. `Good` creates the false relief; `Excellent` becomes the dry reaction after the full loop is visible.

Apply next time:

- When the owner supplies a hook demo, preserve its emotional sequence and signature reaction words while polishing the spoken English.
- Use `viewer situation -> false relief -> contradiction -> mechanism -> visual transformation -> promise` for similar modern-life traps.
- Keep the viewer as the subject so the hook feels lived rather than summarized.
- Do not reveal the numbered answers before the final promise.

Promote to shared memory:
no. This is a project-specific hook preference that may become reusable if the owner confirms the pattern on another video.

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
