# script - memory

Self-improving notes for the narration script. Single canonical copy.

## Verified researcher usage

Project 1 cited, correctly: Robin Dunbar (the 150 number and its 5 / 15 / 50 / 150 layers),
John Cacioppo (loneliness as hypervigilance for social threat), Polly Wiessner (firelit talk
in forager bands), Christopher Boehm (the ladder of gossip, ridicule, exile), and the
Cyberball exclusion paradigm. That mix satisfies the rule: two behavioral scientists plus
two anthropologists.

## Project 3 cited (2026-07-28)

Mark Leary (sociometer theory, self-esteem as a gauge of relational value), Tory Higgins
(audience tuning and the saying-is-believing effect, where the tuned description writes
itself back into the speaker's own memory), Patricia Linville (self-complexity as a
bulkhead against a single domain failure), Polly Wiessner (Ju/'hoansi firelit talk, about
four in five firelight conversations were stories about people), Christopher Boehm (gossip,
ridicule, shunning, exile). Three behavioral scientists plus two anthropologists.

Wiessner and Boehm are reused from project 1 but for a different mechanism: project 1 used
them for exclusion and the cost of exile, project 3 uses them for the indivisibility of
reputation under a single permanent audience. Reuse of a researcher is fine when the finding
does different work.

## Project 2 cited (2026-07-28)

Bluma Zeigarnik (interrupted tasks recalled roughly twice as well as completed ones, 1927,
with the Kurt Lewin restaurant-waiter observation that prompted it), Susan Nolen-Hoeksema
(rumination as passive circular attention that feels like problem-solving while producing
worse solutions), Brad Bushman (the catharsis test: venting on a punching bag while thinking
of the provocateur increased later aggression), E. J. Masicampo and Roy Baumeister
("Consider it done", making a specific plan releases an unfinished goal without completing
it), Max Gluckman (the peace in the feud, cross-cutting ties forcing disputes closed),
E. Adamson Hoebel (Greenlandic Inuit song duels, public performance, audience laughter as
verdict, formal end to the grievance). Four behavioral scientists plus two anthropologists.

Two craft notes worth keeping:

- The Zeigarnik-to-Masicampo chain is the cleanest science-to-shift line the channel has
  produced so far. The mechanism that opens the loop and the finding that closes it come from
  the same research lineage, so the shift genuinely falls out of the science instead of being
  bolted on. Look for that shape when planning: find the open-loop mechanism first, then the
  study that closes that specific loop.
- The Lewin waiter story is an anecdote, not a published experiment. It is written as
  "the story goes that", which keeps it honest. Do the same with any origin anecdote.
- First person is allowed in exactly one place: the sentence the viewer says to themselves
  as the shift. Narration stays 2nd person. Grep `\b(we|I)\b` and confirm every hit is
  modeled viewer speech, not narrator voice.

Fresh anthropologists to reach for so Wiessner and Boehm are not used a fourth time:
Hoebel, Gluckman, Jean Briggs, Richard B. Lee, Sarah Blaffer Hrdy, Joseph Henrich.

## OPEN DISCREPANCY: question density

`.agents/rules/channel-dna.md` says "Question every 4 to 6 sentences". **The accepted
project 1 script does not do this**, and never did: it has 3 question marks across roughly
165 sentences, which is one per 55. Following the written rule literally would mean about 30
questions in a 2,000 word script, which would read nothing like the video the user approved.

Projects 2 and 3 were written to match the fixture, 3 questions, not the rule. The rule text
is either wrong or means something looser than it says. **The user has not ruled on this
yet.** Project 2 came in at 1 question on first draft and was edited up to 3 to land on the
fixture, so check this before shipping rather than after.
Until they do, match the fixture and say so, because the fixture is the quality bar named in
`AGENTS.md`.

Measure both before shipping a script:

```bash
F=projects/<n>-*/script_*.md
echo "questions $(grep -o '?' $F | wc -l)  sentences $(grep -oE '[.!?]' $F | wc -l)"
```

## Lessons

- The opening line and the closing echo should be drafted **before** the body. Project 1's
  echo works because it was planned: "You can be surrounded by forty people and still feel
  like the last person on earth" returns at the end reframed as "because your brain was never
  counting people at all. It was counting who knows you."
- Concrete quantities in the narration pay off twice: they make the anthropology feel
  measured, and they give the `thumbnail` skill its strongest material. Project 1's 40 / 150 /
  5 / 200,000 fed the accepted thumbnail directly.
- Keep the script free of every markdown character. This is not cosmetic. The forced aligner
  flattens the file into one word stream, so a stray `##` or `**` becomes a spoken token and
  shifts every timestamp after it.
