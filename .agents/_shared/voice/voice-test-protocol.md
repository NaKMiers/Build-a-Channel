# Voice Test Protocol

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
test narration style, pace, deadpan timing, learner clarity, and visual sync before generating full voiceover for future `Why It Works` videos.

This protocol is required for new videos and major voice-direction changes. It does not apply retroactively to existing videos unless the user explicitly asks.

## Required Inputs

Before a voice test, prepare:

- a script section of `45-60` seconds
- the first `10` seconds hook board or rough visual plan
- markup from [script-markup-guide.md](script-markup-guide.md)
- the intended voice choice, normally `David23`
- a rough runtime target

The test section should include:

- the hook
- one clear explanation line
- one dry joke
- one key term or repeated phrase
- one visual punchline or WIT reaction opportunity

Do not choose a clean but easy section. Test the part most likely to reveal problems.

## Variant Set

Generate `2-3` short variants only.

Recommended set:

| Variant | Voice | Speed | Purpose |
| --- | --- | --- | --- |
| A | `David23` / `am_eric` | `0.84` | default long-form pace |
| B | `David23` / `am_eric` | `0.78` | careful deadpan and learner timing |
| C | `David23` / `am_eric` | `0.76` | slower clarity fallback |

If the problem is delivery rather than speed, keep the same speed and compare different markup:

- fewer tags
- stronger `[beat]` placement
- more `[deadpan]` on punchlines
- `[slower]` only on dense lines

Do not test many voices at once unless the user is explicitly choosing a new default narrator.

## Listening Pass

Listen once for each category:

1. Clarity:
   Can an intermediate English learner understand the line without subtitles?
2. Deadpan:
   Does the joke sound underplayed instead of performed?
3. Human rhythm:
   Does the voice breathe like a person or read like a generated tutorial?
4. Pace:
   Are labels and keywords readable before the next idea starts?
5. Fit:
   Does the first `30` seconds sound like `Why It Works`?

Do not decide from the first listen only. Fast narration often feels exciting once and tiring after replay.

## Visual Hook Test

Place the preferred voice test under the first `10` seconds hook board.

Check:

- topic is clear by second `3`
- contradiction is clear by second `5`
- WIT's emotional position is clear by second `8`
- title-thumbnail promise is paid off by second `10`
- the first joke has space to land
- no key label appears too early
- no cue-critical label appears too late to read

If the hook board works silently but fails with voice, fix timing or script before full production.

## Scoring Rubric

Score out of `100`.

| Category | Points | Pass standard |
| --- | ---: | --- |
| Pronunciation clarity | 25 | words are clean and easy to subtitle |
| Deadpan timing | 20 | punchlines breathe without overacting |
| Learner pace | 15 | intermediate learners can follow the main point |
| Human rhythm | 15 | pauses feel intentional, not robotic |
| Visual sync | 15 | labels, WIT reactions, and cuts can follow the voice |
| Brand fit | 10 | sounds smart, simple, funny, dry |

Pass:

- total score is `80+`
- pronunciation clarity is at least `20/25`
- deadpan timing is at least `15/20`
- no category scores below half

If two variants pass, choose the one with better learner clarity unless the stronger variant is clearly more human and still understandable.

## Runtime And Pace Checks

Use these as working ranges, not hard math:

- long-form narration should usually land around `130-155` words per minute after pauses
- dense learner-friendly sections can be closer to `120-140` words per minute
- sustained pace above `165` words per minute is risky for the channel
- punchline beats may add time, but they often improve retention and clarity

Do not cut pauses only to reduce runtime. First cut repeated explanations, weak jokes, or lines the visual already explains.

## Full Voiceover Gate

Generate full voiceover only when:

- one test variant passes the rubric
- the first `10` seconds works with voice and visuals
- the script is locked enough that regeneration will not be wasted
- the chosen speed is documented in the video project
- the visual plan can follow the voice without rushing labels

If the script changes substantially after the voice test, rerun a short test before full generation.

## Notes To Save

For future video projects, record:

- selected voice and speed
- test section used
- variants generated
- winning variant
- score and reason
- any markup changes
- whether the first `10` seconds passed
- known timing risks for production

Reusable lessons belong in `.agents/_shared/channel/learning-log.md` or the channel-wide voice docs.
Per-video decisions belong in `projects/<slug>/`.

## Common Failure Fixes

| Failure | Fix |
| --- | --- |
| voice sounds too sincere | add `[deadpan]` to absurd lines and reduce emotional wording |
| jokes feel rushed | add `[pause]` before the turn and `[beat]` after the punchline |
| learner clarity is weak | split long lines, use `[slower]`, reduce idioms |
| voice sounds robotic | remove excessive tags and rewrite lines to sound spoken |
| visuals arrive early | delay labels, red markup, or WIT reaction to the cue word |
| runtime is too long | cut weak lines before increasing speed |

## Do Not Do

- Do not generate a full video before the voice test passes.
- Do not pick the fastest variant just because it feels energetic.
- Do not imitate another creator's exact voice.
- Do not sacrifice learner clarity for sarcasm.
- Do not use a voice that sounds old, raspy, or too dramatic unless explicitly approved.
