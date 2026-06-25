# Section 08 Payoff Design

Status: `preview build`

Composition:

- ID: `Section08Payoff`
- Duration: `29.141s`
- Format: `1920x1080`
- Preview port: `1008`

Design rules:

- Use three held payoff scenes: hidden-future price tag, real-price receipt, final cardboard question.
- Use static hard cuts between big scenes and timed hard-show cue layers inside each scene.
- Keep WIT to three large emotional beats: suspicious evaluator, receipt evidence holder, deadpan final checker.
- Keep all cue text as short handwritten labels; no paragraph cards and no new product categories.
- Add all receipt and tag text in HyperFrames/CSS, not inside source photos.
- No MP4/WebM export unless explicitly requested.

Asset decisions:

- `hidden-tags.png` uses the generated price-tag-with-hidden-future-tags support base.
- `receipt-table.png` uses the generated price-tag/receipt tabletop support base.
- `cardboard.jpg` uses the real cardboard-box reference as a calm ending texture.
- WIT pose files are hardlinked from the project-level `assets/wit/` directory.

Motion decisions:

- Ordinary labels are static timed cue states.
- Cross-out, cut mark, and final underline are drawn as static impact marks that appear on their spoken cues.
- No decorative fly-ins, camera moves, or transitional animation.
