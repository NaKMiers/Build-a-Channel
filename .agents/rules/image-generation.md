# Image generation - how prompt files become images

Canonical description of the tool the owner actually runs, and the one piece of syntax
`image-prompts.md` carries for it: the `---` chain break.

Read this before writing or editing `prompts/image-prompts.md`. Everything here is about
the machine that consumes that file. The art rules live in `.agents/rules/visual-style.md`.

## The tool

Scene images are generated in a Google Flow chain workflow, driven through the
"Nguyen Hieu AI - Auto Download" panel. It is a batch tool, not a chat. The owner runs it
once per episode with the whole prompt file pasted in.

The four steps of one run:

1. **Ref binding.** Upload the character reference sheets from `characters/`, one per
   character, and type a TOKEN for each: `@YOU`, `@CREW`, `@FISHER`. The token is typed by
   hand and must match the cast table in `prompts/character-prompts.md` exactly.
2. **Image settings.** Model and resolution, for example Nano Banana 2 at 2K, aspect 16:9.
3. **Image prompts.** Paste the entire contents of `prompts/image-prompts.md` into the
   IMAGE PROMPTS box, or upload it as `.txt`. The tool splits the pasted text into records
   on blank lines. Every `@TOKEN` inside a prompt resolves to the reference bound in step 1.
4. **CREATE N IMAGES.** The button shows the record count it parsed. That number must equal
   the prompt count `/scenes` reported. If it is higher, the file has a stray line in it.

Steps 1 and 3 are why the prompt rules exist. **Step 1 is why a prompt names a cast member
by `@TOKEN` and never re-describes them:** the design arrives from the bound sheet, not from
the prose. **Step 3 is why `image-prompts.md` is prompts only, one prompt per unbroken line,
separated by exactly one blank line:** a header line or a wrapped prompt becomes its own
junk record and shifts every image after it.

## The chain, and why it needs a break

The run produces a node graph: one card per prompt, each card wired to the bound character
refs, **and wired to the card before it.** By default prompt N inherits the image generated
for prompt N-1.

That default is the reason the pipeline holds together visually. It is what actually
delivers the scene-holding rule in `.agents/skills/scenes/SKILL.md`, and what keeps a
`VARIANT` beat sitting on the same composition as its source plate instead of redrawing it.

It is also the one failure mode. When the next beat is supposed to be a genuinely new
scene, a new chapter, a new era, a new location, the inherited frame leaks through and the
"new" scene comes back looking like the old one. The prompt says one thing and the wire
says another, and the wire usually wins.

## The `---` chain break

A line containing exactly three hyphens, alone, cuts the wire between the prompt above it
and the prompt below it. The prompt below starts a fresh chain with only the bound
character refs behind it.

```
[0:00] <STYLE ANCHOR> <scene> <STYLE LOCK>

---

[0:02] <STYLE ANCHOR> <scene> <STYLE LOCK>
```

Shape rules, enforced by `check`:

- Exactly `---`, three hyphens, nothing else on the line.
- Exactly one blank line above it and one blank line below it.
- Never the first or the last line of the file. A break needs a prompt on both sides.
- Never two breaks with only a blank line between them.
- It is the **only** non-prompt line the file may contain. Everything else still fails the
  prompts-only rule.

## When to break, and when not to

Break the chain before a prompt whose frame must not inherit the one before it:

- A chapter or act boundary in the script.
- A hard cut in place, era, or cast: modern bedroom to ancestral savanna, `@YOU` alone to a
  tribe scene.
- A register switch that changes the whole surface, for example an illustrated story
  environment to a clean diagram or text card, and back.
- Any V2 beat planned as a new `PLATE` whose composition the previous frame would
  contaminate.

Keep the chain, no break, when the next frame is meant to look like the last one:

- A hold, where several consecutive cues share one scene and only an expression changes.
- Any `VARIANT`, which exists to preserve the source composition and change one named delta.
- Any `CALLBACK`, which reuses an earlier plate on purpose.
- A new plate in the same setting, where inherited palette and line weight are a gift.

**A break between a variant or callback and the plate it points back to destroys its
lineage.** The chain is linear, so the source plate reaches a later beat only by passing
through every card in between. Place breaks between chains, never inside one.

Judgment call in one line: if you would be annoyed to see the previous image bleed into
this one, break. If you would be relieved, do not.

## The `@[timestamp]` scene reference

The chain is linear and only reaches one card back, so a `---` permanently severs a later
frame from everything before it. That is correct for composition and wrong for identity: an
object introduced at `[0:38]` and shown again at `[10:12]` has no path back to its own first
drawing, so the second one is redrawn from words alone and comes back a different colour. The
cast sheets solve this for characters, because they are bound once and reach every card. They
do not solve it for props, diagrams, and recurring objects that do not deserve a sheet.

`@[timestamp]` is the manual wire that closes that gap. Written inside a prompt, it tells the
tool to find the card whose prompt begins with that exact timestamp, take the image that card
generated, and attach it to this card as an **additional** reference alongside the bound
character sheets.

The contract, which the tool implements and `scenes` and `check` both enforce:

- **Syntax is `@[M:SS]`, colon and all**, copied character for character from the target
  prompt's own leading timestamp. `@[0:38]`, never `@[0-38]`. The hyphen form is only ever a
  file name.
- **It resolves to exactly one card.** Timestamps in `image-prompts.md` are unique and strictly
  ascending, because `transcript` remaps any duplicate before `scenes` runs, cascading when the
  next second is also taken. That uniqueness is what makes the syntax addressable at all.
- **Backward only.** The target must appear earlier in the file. A reference pointing forward
  or at itself names an image that does not exist yet at generation time.
- **It survives `---`.** This is the whole point. The break cuts the automatic wire to the
  previous card; it must never cut a reference placed by hand. A break and a reference are
  different mechanisms and the break does not outrank it.
- **It adds to the chain, it does not replace it.** A `VARIANT` that also carries a reference
  inherits its source plate *and* receives the referenced image, plus the character sheets.
- **Any number are legal, two is the practical ceiling.** Past two, the model starts blending
  the composition of the referenced frames into the new one and the frame falls apart.
- **It is a design source, not a composition source.** The tool hands over a whole image
  because that is all it can hand over, so the prompt must say which part of it counts. Every
  prompt containing an `@[timestamp]` also carries the V2 SCENE REFERENCE LIMIT string from
  `visual-style.md` verbatim, which restricts the reference to the named object's shape,
  proportion, colour, and line treatment and forbids taking composition, camera, background, or
  any other object from it. This is exactly the opposite of a `VARIANT`, where
  `Preserve the attached source plate` deliberately does take the whole composition.
- **Never rendered.** The existing style lock already covers it: `@[name] is mention syntax for
  reference only and must never be rendered as visible text`.

**Always point at the object's first appearance, never at its most recent one.** If `[10:12]`
references `[5:04]` and `[5:04]` references `[0:38]`, each hop re-generates from a copy and the
drift compounds down the chain. Every appearance pointing straight back at `[0:38]` makes the
twentieth one as accurate as the second. `scenes` records that canonical timestamp per object
in the continuity ledger at the top of `visual-plan.md`.

## After the run

The tool auto-downloads the generated images. The owner saves each one into `scenes/` under
its timestamp with the colon replaced by a hyphen, `[3:20]` to `[3-20].jpg`, then runs
`/scene-polish` and `/check`. Breaks do not create files and do not shift the mapping
between a prompt and its scene image.
