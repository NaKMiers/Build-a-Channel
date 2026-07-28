# topic - memory

Self-improving notes for topic selection. Single canonical copy, no Claude-side duplicate.

## Already made (never re-propose)

| # | Title | Status |
| --- | --- | --- |
| 0 | Why You Cannot Stop Checking Your Phone | published |
| 1 | Why You Feel Lonelier In A Crowd Than Alone In Your Room | packaged, thumbnail accepted |
| 2 | Why You Still Replay That Argument From Last Week | scaffolded 2026-07-28, no script yet |
| 3 | Why You Are A Different Person With Each Friend Group | scaffolded 2026-07-28, no script yet |

Planned research for the two scaffolded projects, so the `script` skill does not have to
rediscover it:

- **Project 2, anger.** Sell, Tooby and Cosmides on the recalibrational theory of anger:
  anger is a bargaining emotion that exists to raise how much others weight your welfare.
  Pair with the Zeigarnik effect for why the replay loop will not close. Anthropology is
  Boehm on counter-dominance, where letting a slight pass in a small band really did lower
  your share.
- **Project 3, identity.** Code-switching across disjoint audiences. Anthropology is the
  single-audience band: in a group of 150 who knew you from birth there was only one version
  of you available, so there was nothing to segment. Modern life hands you disjoint
  audiences that never meet. Reuses Dunbar's 150 as a supporting fact, not as the subject,
  which is fine because project 1 used it for a different mechanism.

## Proposed but not picked

### 2026-07-28, batch 4, titles 1 to 4 not picked

The user selected title 5. These four remain eligible for a future batch.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| The Asch Effect Is Still Running Your Opinions | conformity and social proof | Asch 1951, 12 trials, 37 percent conforming responses on critical trials |
| Why You Feel Closer To Someone After You Help Them | belonging and reciprocity | Jecker and Landy Ben Franklin effect, reciprocal altruism in small bands |
| Why Your Mind Goes Blank When People Watch You | shame and social fear | Yerkes-Dodson performance curve, social facilitation research |
| Why You Keep Saving Things You Never Use | scarcity and loss aversion | Kahneman and Tversky loss aversion, endowment effect experiments |

### 2026-07-28, batch 3, rejected wholesale without a selection

The user invoked `topic` again and gave no reason, so nothing is recorded about why.
Do not repeat these titles in the immediately following batch.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why You Feel Like A Fraud When Things Are Going Well | status and comparison | Clance and Imes impostor phenomenon, 70 percent often-cited prevalence estimate |
| Why Your Brain Thinks Boredom Is An Emergency | boredom and attention | Eastwood boredom framework, Wilson 2014 15-minute waiting study |
| Why You Feel Guilty When You Rest | sleep and rest | Calvinist work ethic research, hunter-gatherer time-use comparisons |
| Why You Hate Being Bad At Something In Public | shame and social fear | Gilovich spotlight effect, social rank and competence displays |
| Why You Stop Wanting Things Right After You Get Them | habit and reward | Brickman and Campbell hedonic adaptation, reward prediction error |

### 2026-07-28, batch 1, rejected wholesale without a selection

The user replied `again` and gave no reason, so nothing is recorded about why. Do not infer
one. All five stay eligible for a future batch.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why You Blush When You Have Done Nothing Wrong | shame and social fear | Gilovich spotlight effect, guessed ~50 percent noticed vs ~23 percent actual |
| Why A Friend's Win Hurts More Than A Stranger's | status and comparison | Festinger, Tesser self-evaluation maintenance |
| Why Sitting Still With Your Thoughts Feels Unbearable | boredom | Wilson 2014, 15 minutes alone, 67 percent of men self-administered a shock |
| Why You Repeat Rituals You Know Do Nothing | ritual and meaning | Malinowski, elaborate ritual for open-sea fishing, almost none for the safe lagoon |
| Why 3AM Convinces You Your Life Is Falling Apart | sleep and rest | Samson Hadza study, 33 sleepers, only 18 minutes of whole-group sleep synchrony over 20 days |

Batch 3 candidate worth keeping: the Hadza sentinel finding and the Malinowski lagoon
contrast are both two-scene, two-number setups, which is exactly what the split-frame
thumbnail layout wants.

### 2026-07-28, batch 2, titles 2, 3 and 5 not picked

The user picked 1 and 4. These three remain eligible.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why Your 9AM Self Keeps Betraying Your 9PM Self | habit and willpower | Wood and Neal, roughly 43 percent of daily behaviors run habitually in a fixed location |
| Why The Person Who Ignores You Is Hardest To Forget | love and attachment | intermittent reinforcement, Fisher's fMRI showing rejection lighting reward-craving circuits rather than pain circuits |
| Why You Judge A Stranger's Face In Under A Second | social perception | Willis and Todorov, 100 ms is enough to fix a trustworthiness judgment, and longer exposure raises confidence without raising accuracy |

## Lessons

- Project 1 proves the "Why do/can't you ___?" angle works end to end, and its script
  produced unusually good thumbnail material because it contained hard numbers (40, 150, 5,
  200,000). **Prefer topics whose mechanism has a real quantity attached**: the `thumbnail`
  skill's strongest layout needs two numbers that invite subtraction, and a script with no
  numbers cannot feed it.
- Both existing videos are attention or belonging topics. Spread the next batch across the
  other recurring themes (status and comparison, shame and social fear, habit and willpower,
  sleep and rest, ritual and meaning, anger, boredom, identity).
- **Multiple selections are normal, and each one gets its own project folder.** On the first
  real run the user replied `1 and 4`, which correctly produced projects 2 and 3. Number them
  in the order the user listed. Then say that `/script` handles one project at a time and ask
  which to write first, rather than picking for them.
- **`again` means regenerate the whole batch with no reason given.** Record the batch as
  not-picked, do not invent a reason, and keep all five eligible. Do not silently reuse a
  rejected title in the very next batch either: the user rejected the batch, so give them
  genuinely different themes first.
