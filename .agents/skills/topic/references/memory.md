# topic - memory

Self-improving notes for topic selection. Single canonical copy, no Claude-side duplicate.

## Already made (never re-propose)

| # | Title | Status |
| --- | --- | --- |
| 0 | Why You Cannot Stop Checking Your Phone | published |
| 1 | Why You Feel Lonelier In A Crowd Than Alone In Your Room | packaged, thumbnail accepted |
| 2 | Why You Still Replay That Argument From Last Week | scaffolded 2026-07-28, no script yet |
| 3 | Why You Are A Different Person With Each Friend Group | scaffolded 2026-07-28, no script yet |
| 4 | Why Your Life Feels Faster When Every Day Looks The Same | scaffolded 2026-08-04, no script yet |
| 5 | Why do people follow the crowd? | scripted, cast, metadata, thumbnails done 2026-08-04, user-supplied title |
| 6 | Why You Feel More Tired After Doing Nothing All Day | scaffolded 2026-08-04, no script yet |
| 7 | Why Getting Angry Sometimes Gets You What You Want | scaffolded 2026-08-04, no script yet |
| 8 | Why Your New Phone Makes Everything Else Look Cheap | scaffolded 2026-08-12, the Diderot effect, current holder of number 8 |
| 9 | Why You Give Great Advice You Never Take Yourself | scaffolded 2026-08-19, Solomon's paradox, no script yet |
| old 8 | Why You Stay Quiet When You Know The Room Is Wrong | abandoned 2026-08-12, unpublished, artifacts recoverable at `c9f048f` |
| old 9 | Why You Think Everyone Is Watching When Nobody Is | abandoned 2026-08-12, unpublished, artifacts recoverable at `c9f048f` |

Project 5 numbering note: this was scaffolded as project 7, but the user deleted the old
project 5 (What Every Human Tribe Did That You Still Do Under Stress) and renamed the folder
to `projects/5-why-do-people-follow-the-crowd` mid-pipeline on 2026-08-04. The next new
project number is therefore 7, not 8.

Project 5 note: the user supplied this title verbatim and reaffirmed it after being told it
breaks two title rules (no "you" or "your", third-person "people"). **Their title stands as
the folder name and working title.** `metadata` may still set a compliant published title.
Conformity research to reuse: Asch 1951 line task, 12 critical trials, 37 percent conforming
responses and about 75 percent conforming at least once. Sherif autokinetic effect for how a
group norm forms out of nothing. Berns 2005 and Klucharev for conformity altering perception
and firing an error signal, not just speech. Anthropology is Boehm on counter-dominance and
the survival cost of exile from a band, where being the one dissenter was not a social risk
but a food and protection risk.

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

## ABANDONED PROJECTS 8 AND 9, resolved 2026-08-12

Two completed-but-unpublished projects were dropped from the tree, and the user has
confirmed they stay dropped. Recorded here because the artifacts still exist and the
titles will otherwise look like fresh ideas to a future batch.

- Old **8** (`why-you-stay-quiet-when-you-know-the-room-is-wrong`) and old **9**
  (`why-you-think-everyone-is-watching-when-nobody-is`) were both completed and committed
  in `c9f048f "pr 8 9"`, with 190 media files between them including `audios/full.mp3` and
  the three-part recordings, character sheets, and scene images. Neither was ever
  published: the channel's seven live videos map to projects 1 through 7.
- Commit `44cff0b "skill: metadata"` deleted 209 files under `projects/`, removing both.
  The commit subject says nothing about it, so it looks accidental.
- **The user was shown this on 2026-08-12 and chose to leave them out.** Not a mistake to
  re-raise. Everything remains recoverable with
  `git checkout c9f048f -- 'projects/8-*' 'projects/9-*'` if they ever change their mind.
- The number **8 was then reassigned** to the Diderot project at the user's instruction.
  Old 8 and old 9 no longer own a number.

**Both titles are eligible again, with one condition.** If either is re-proposed, say
plainly that a full voiceover is already recorded and recoverable, because that changes
the cost of the video from a full production to a re-edit. Do not silently offer them as
new ideas.

The old project 9 title is also a near-duplicate of batch 12 title 2 below. Check
deleted-but-recoverable projects in git history, not just the working tree, before
proposing a title.

## Proposed but not picked

### 2026-08-19, batch 13, user picked title 5 (Solomon's paradox -> project 9)

The user restated title 5 verbatim to select it. The other four remain eligible. Batch was
spread across attachment, boredom, ritual, and procrastination; all four carry real numeric
material for the thumbnail stage.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why The Slowest Texter Is The Hardest To Forget | love and attachment | intermittent reinforcement; Fisher fMRI rejection lighting reward circuits; Jankowiak and Fischer, romantic love in 88.5 percent of 166 societies |
| Why Doing Nothing For Ten Minutes Feels Like A Threat | boredom and attention | Wilson 2014, 15 minutes alone, 67 percent of men self-administered a shock; default mode network vigilance |
| Why You Knock On Wood When You Know It Does Nothing | ritual and meaning | Malinowski Trobriand contrast, elaborate magic for open-sea fishing and almost none for the safe lagoon; Damisch 2010 superstition and putting performance |
| Why You Clean The House When A Real Deadline Is Close | habit and willpower | Sirois and Pychyl procrastination as mood repair; Steel meta-analysis; Woodburn immediate-return vs delayed-return economies |

Selected: project 9, **Why You Give Great Advice You Never Take Yourself**, Solomon's paradox.
Research to reuse so `script` does not rediscover it: Grossmann and Kross 2014 on Solomon's
paradox, wiser reasoning about others' problems than one's own, closed by self-distancing
(third-person self-talk). Anthropology is the council or elder-advising structure of the band,
where wisdom was pooled and spoken aloud to others rather than kept inward. Known weakness:
like Diderot this topic is number-light, so pull a hard quantity from the self-distancing or
advice literature during `script` or the thumbnail stage will be starved.

### 2026-08-12, batch 12, none picked, user supplied their own topic

All five were compliant and none were rejected on their merits. The user read the batch,
then asked about a mechanism they already had in mind (the cascade where one luxury
purchase makes every other possession look wrong) and chose that instead. This is the
second time the user has arrived with their own topic after seeing a batch, project 5
being the first. **Treat the batch as a prompt for their own thinking as much as a menu.**
All five remain eligible.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why Your Life Looks Unfixable At 3AM And Fine By 9AM | sleep and rest | Samson Hadza sentinel study, 33 sleepers, 18 minutes of whole-group sleep synchrony across 20 days; Yoo and Walker amygdala reactivity after sleep loss |
| Why You Think Everyone Noticed When Almost Nobody Did | shame and social fear | Gilovich spotlight effect, roughly 50 percent predicted noticing vs 23 percent actual. **Overlaps deleted project 9, check before reusing** |
| Why You Knock On Wood When You Know It Does Nothing | ritual and meaning | Malinowski Trobriand contrast, elaborate magic for open-sea fishing and almost none for the safe lagoon; Damisch 2010 superstition and putting performance |
| Why You Clean The Kitchen Instead Of The Real Task | habit and willpower | Sirois and Pychyl procrastination as mood repair; Steel meta-analysis; Woodburn immediate-return vs delayed-return economies |
| Why You Want The Person Who Answers Slowest | love and attachment | intermittent reinforcement; Fisher fMRI rejection lighting reward circuits; Jankowiak and Fischer, romantic love in 88.5 percent of 166 societies |

### Selected instead: project 8, the Diderot effect

Working title **Why Your New Phone Makes Everything Else Look Cheap**. Research already
established in conversation, so `script` does not have to rediscover it:

- **Psychology.** The consistency or unity motive. A new possession that sits outside the
  existing set creates visible inconsistency, and upgrading the rest is the cheaper
  resolution than returning the one item. Distinct from hedonic adaptation, which is about
  pleasure resetting over time, and the opposite of the endowment effect, which inflates
  what you already own. Diderot makes what you own look worse.
- **Anthropology.** Grant McCracken, *Culture and Consumption* (1988), coined both "the
  Diderot effect" and "Diderot unity". McCracken is himself an anthropologist of
  consumption, so the mechanism and its ancestral layer come from one lineage, the same
  clean shape as the Zeigarnik-to-Masicampo chain in project 2. Extend with potlatch and
  Veblen's conspicuous consumption for status display through matched sets.
- **Origin story.** Diderot's 1769 essay *Regrets on Parting with My Old Dressing Gown*. A
  gifted scarlet gown made his desk, chair, prints and shelves look shabby; he replaced
  them one by one into debt, and wrote that he had been master of the old gown and became
  a slave to the new one.
- **Known weakness: this topic is story-rich and number-poor.** 1769 and 1988 are dates,
  not quantities that invite subtraction, and the `thumbnail` skill's strongest layout
  needs two such numbers. Bring a quantity from the consumption or status-signalling
  literature during `script`, or the thumbnail stage will be starved.

This is also the deliberate bridge into the planned behavioural-economics series: the
title is psychological, so it stays in the existing suggested-video cluster and does not
contaminate the hook-rule retention test, while the subject matter is economics.

### 2026-08-04, batch 10, conformity variants, none picked

The user asked for the topic "Why do people follow the crowd?", was offered five compliant
conformity titles, and rejected all five in favour of their own exact wording. **When a user
names a topic themselves, offer the reframed titles once, then take their wording if they
repeat it.** These four remain eligible as titles for a future conformity video.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why You Doubt Your Own Eyes When Everyone Disagrees | conformity | Asch 1951, 37 percent conforming responses, 75 percent conformed at least once |
| Why You Stay Quiet When You Know The Room Is Wrong | conformity, social fear | Prentice and Miller pluralistic ignorance, Latane and Darley |
| Why A Long Line Makes You Want To Join It | social proof | Sherif autokinetic effect, Cialdini social proof field studies |
| Why Your Taste Is Not As Personal As You Think | identity, social proof | Salganik music lab, 14,341 participants across 8 parallel worlds |

### 2026-08-04, batch 9, rejected wholesale, steer recorded

The user replied "I need a problem that every mistakes, that a good catch". The steer is
toward **a mistake the viewer is making right now without knowing it**, not a feeling they
notice. A feeling title gets sympathy, a mistake title gets caught. Cognitive-bias topics
(attribution, planning fallacy, sunk cost, illusion of explanatory depth) serve this better
than mood topics, and they still carry an ancestral origin.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why You Say Yes When You Really Want To Say No | shame and social fear | Bohns and Flynn compliance underestimation |
| Why You Forget 50 Nice Words But Never 1 Mean One | negativity bias | Baumeister 2001, Gottman 5 to 1 |
| Why You Stop Being Lazy The Second Someone Walks In | habit and willpower | Zajonc social facilitation, Hawthorne |
| Why You Can Fix Everyone's Life But Your Own | identity | Grossmann and Kross 2014 Solomon's paradox |
| Why Your Good News Dies After You Open Your Phone | status and comparison | Festinger, Dunbar 150 as the old comparison ceiling |

### 2026-08-04, batch 8, rejected wholesale, reason given

The user replied "More curious but simple for everone kow", meaning the titles were worded
too cleverly and read as literary rather than plain. **Write titles in words a tired viewer
understands at a glance**, and let the curiosity come from the contradiction inside the
sentence, not from the vocabulary. Plain nouns, small numbers, no inverted phrasing like
"outlives" or "the second someone".

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why You Say Yes When Every Part Of You Means No | shame and social fear | Bohns and Flynn, askers underestimate compliance by roughly half |
| Why One Bad Comment Outlives Fifty Good Ones In Your Head | negativity bias | Baumeister 2001 bad is stronger than good, Gottman 5 to 1 ratio |
| Why You Suddenly Work Harder The Second Someone Walks In | habit and willpower | Zajonc social facilitation, Hawthorne studies |
| Why You Give Advice You Would Never Follow Yourself | identity | Grossmann and Kross 2014 Solomon's paradox, self-distancing |
| Why Your Win Stops Feeling Like A Win After You Scroll | status and comparison | Festinger social comparison, Dunbar 150 as the old comparison ceiling |

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

### 2026-08-08, batch 11

User picked title 1. The other four remain eligible.

| Title | Theme | Numeric material available |
| --- | --- | --- |
| Why One Mean Comment Outweighs Ten Kind Ones | negativity bias | Baumeister 2001, Gottman 5 to 1 ratio |
| Why Your Willpower Runs Out Even When You Do Nothing | habit and willpower | Baumeister ego depletion, glucose depletion studies |
| Why You Give More To Others Than You Give Yourself | identity and belonging | self-neglect paradox, Fisher rejection circuits |
| Why You Still Need Rituals More Than You Think | ritual and meaning | Malinowski, Hadza, cross-cultural ritual prevalence |
