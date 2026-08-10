# Retired prompts - provenance record

These two files were the whole pipeline before it was split into the nine skills under
`.agents/skills/` and the six rule files under `.agents/rules/`. They are kept, not deleted,
for one reason: they are the provenance record for 256 rules, several of which were recovered
from specific generation failures.

- `master-prompt.md` - the 533 line, 5 stage video engine. 204 rule lines.
- `character-prompt.md` - the reference sheet template and the Toss identity lock. 52 rule
  lines.

**Do not edit these and do not paste them into a chat.** They are superseded. If a rule in
`.agents/rules/` looks wrong, thin, or missing, check it against these files first, then fix
the rule file. Never re-introduce a second live copy of a rule.

Two known internal contradictions in the retired files, resolved during the port:

1. **Hand shape.** `master-prompt.md` line 62 and `character-prompt.md` say small splayed
   line fingers. `master-prompt.md` line 239 says round mitten shapes. Resolved in favour of
   splayed line fingers: `MASCOT.jpeg` shows them, two of three sources agree, and
   `character-prompt.md` lists "no mitten hands" in its NEGATIVE block. See
   `.agents/rules/mascot-toss.md`.
2. **Sheet file extension.** The retired prompt says `NAME.png` in six places, but every real
   project uses `NAME.jpeg`. Resolved in favour of `.jpeg`, matching practice.

`README.md` at the repo root also contains a stale claim that `character-prompt.md` specifies
a "TRUE STICKMAN look (circle head, single-line spine, no filled torso)". That is the opposite
of what the file says: it specifies a filled garment torso and explicitly negatives
"no pure line-only stickman with a single-line spine".
