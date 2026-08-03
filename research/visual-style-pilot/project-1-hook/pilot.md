# TossExplains V2 Visual Pilot: Project 1 Hook

Status: Direction B selected for pipeline implementation under the approved
`prompts/plan.md`.

## Scope

- Source sequence: Project 1, 0:00 to 0:58.
- Source narration: `projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/transcribes/transcript.txt`.
- Source cast: `@YOU` and `@CROWD` from the accepted Project 1 sheets.
- Source comparison frame: `projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/scenes/[0-00].jpg`.
- Existing Project 1 files were read only and remain unchanged.
- Preview renderer: OpenAI image generation, used because Google Flow is not connected to
  this workspace. The prompt pack must still be smoke-tested in Google Flow before the first
  production V2 video is published.

## Decision

Direction B, Warm Editorial Storybook Doodle, is the production target.

Direction A is a safe fallback for concept cards and diagrams. Direction C is useful as a
ceiling reference for rare emotional peaks, but it is too dense and dark to become the default
channel surface.

The comparison board is `comparison-board.jpg`.

| Direction      | Near-white area | Mean saturation | Decision                                                      |
| -------------- | --------------: | --------------: | ------------------------------------------------------------- |
| V1 original    |           66.1% |           0.035 | Too much empty white and too little color separation          |
| A conservative |            3.1% |           0.133 | Useful CLEAN tier, but still visually cautious                |
| B recommended  |            0.1% |           0.309 | Selected default balance of clarity, place, color, and depth  |
| C aggressive   |            0.2% |           0.510 | Strong single image, but too busy and dark for continuous use |

These numbers describe this controlled frame only. They are diagnostic signals, not global
targets for every scene.

## What the board proves

- A warm ground immediately removes the repeated-slide feeling without changing the core idea.
- Story-specific background objects make the frame feel authored rather than generated from a
  generic doodle template.
- A pale negative-space corridor around Toss protects the emotional focal point even when the
  environment becomes richer.
- Three depth planes add more perceived production value than extra character detail.
- Color variation in the crowd improves the image, but Toss must remain the only repeated cobalt
  anchor. Direction B currently lets a few crowd shirts become too blue, so production prompts
  must reserve saturated channel blue for Toss.
- Direction C shows the failure boundary: strong lamp glow, dark corners, large foreground crops,
  and many small props begin to compete with the narration.

## 30-state production plan

The 58 second pilot uses all 27 source cues as generated prompt units, including six controlled
variants. Three additional CapCut-only beats create 30 visible states, or 31 meaningful states
per minute, without requiring 30 unrelated generations. The machine-checkable version is
`visual-plan.md`.

| ID    | Time | Register | Shot         | Tier        | Visual decision                                                                              |
| ----- | ---- | -------- | ------------ | ----------- | -------------------------------------------------------------------------------------------- |
| B001  | 0:00 | STORY    | Wide         | LAYERED     | Toss isolated inside two laughing crowd masses; warm social interior; `FORTY PEOPLE` verdict |
| B002  | 0:04 | STORY    | Close        | CLEAN       | Push into Toss while the crowd softens behind him; hollow expression becomes the only task   |
| B003  | 0:06 | STORY    | Wide         | LAYERED     | Packed train carriage with rail, windows, and bodies creating compressed depth               |
| B004  | 0:08 | STORY    | Medium       | LAYERED     | Office kitchen counter, mug, kettle, and two coworkers turned toward each other              |
| B005  | 0:09 | STORY    | Wide         | LAYERED     | Wedding edge composition with cake, warm lamps, and an inward-facing group                   |
| B005a | 0:12 | STORY    | Wide delta   | ATMOSPHERIC | Preserve B005 exactly; add a restrained amber light plate                                    |
| B005b | 0:13 | STORY    | Wide delta   | LAYERED     | Preserve B005 exactly; add raised brows, open laughs, and three short laugh accents          |
| B006  | 0:15 | METAPHOR | High wide    | CLEAN       | Closed human ring around Toss; warm pastel ground; one empty pale corridor to center         |
| B007  | 0:17 | METAPHOR | Close        | ATMOSPHERIC | Cold cobalt hollow under Toss's ribs against a warm crowd at the edges                       |
| B008  | 0:21 | STORY    | Wide         | LAYERED     | Toss entering a quiet apartment through a doorway; warm room, no other people                |
| B009  | 0:22 | STORY    | Close        | CLEAN       | Hand on closing door; background reduced to one cream wall and one cobalt edge               |
| B010  | 0:23 | STORY    | Macro        | CLEAN       | Phone placed face down on a wood-toned table; Toss hand and sleeve only                      |
| B011  | 0:25 | STORY    | Wide         | LAYERED     | Toss seated on a rug in a quiet room with a lamp, low shelf, and generous calm space         |
| B011a | 0:27 | STORY    | Wide delta   | LAYERED     | Preserve B011 exactly; soften brows and add a small calm smile                               |
| B012  | 0:29 | CARD     | Medium       | CLEAN       | Toss plus one large question mark on a pale blue-grey editorial card                         |
| B013  | 0:31 | DIAGRAM  | Wide         | CLEAN       | Crowd count flows toward a descending loneliness gauge; question verdict at top              |
| B013a | 0:33 | DIAGRAM  | Wide build   | CLEAN       | Preserve B013; reveal count marks, plus sign, and the flawed arithmetic path                 |
| B014  | 0:36 | CARD     | Medium       | CLEAN       | Door icon and Toss stepping through; `GET OUT MORE` verdict                                  |
| B015  | 0:38 | CARD     | Close        | CLEAN       | Invitation in Toss's hands; `SAY YES` verdict                                                |
| B016  | 0:39 | CARD     | Wide         | CLEAN       | Calendar fills with orange marks; `FILL THE CALENDAR` verdict                                |
| B017  | 0:41 | DIAGRAM  | Medium       | LAYERED     | Brain on cobalt card counts bodies while a red connection signal stays low                   |
| B017a | 0:43 | DIAGRAM  | Medium delta | LAYERED     | Preserve B017; counting path fades and connection-quality path illuminates                   |
| B018  | 0:45 | PAYOFF   | Split wide   | LAYERED     | Same crowd shown as CURE on left and TRIGGER on right; Toss bridges the split                |
| B019  | 0:50 | CARD     | Medium       | CLEAN       | `INTROVERT` crossed out; Toss looks toward a new path rather than the label                  |
| B020  | 0:53 | METAPHOR | Wide         | LAYERED     | Huge crossed-out 40 behind a small Toss; crowd recedes into light silhouettes                |
| B021  | 0:56 | CARD     | Close        | CLEAN       | `LONELINESS` isolated on an ivory card with a small connection-gap icon                      |
| B021a | 0:58 | PAYOFF   | Close delta  | CLEAN       | Preserve B021; cross out the old definition and reveal the gap icon in cobalt and orange     |

## Cadence and edit rules

- No unchanged hold should exceed 3.5 seconds in the hook.
- A visual change can be a new composition, a composition-preserving delta, a diagram build, or
  a meaningful camera move. Decorative motion does not count.
- Use one new visual task per narration claim.
- Delta variants must preserve camera, character placement, environment geometry, and major props.
- CapCut may add only restrained 2 to 4 percent pushes, lateral moves, parallax from prepared
  plates, and simple cut or dissolve transitions.

## Production acceptance checks

- Toss remains recognizable at 25 percent scale.
- Saturated cobalt belongs to Toss or to one semantic diagram signal, not generic crowd clothing.
- CLEAN frames use light cream or pastel cards, not repeated pure white.
- LAYERED frames show foreground, subject plane, and background without filling every gap.
- ATMOSPHERIC frames are limited to B005a and B007 in this hook.
- All text is short editorial verdict text, never narration subtitles.
- No photorealism, 3D, anime, manga, realistic anatomy, glossy vector finish, or fake text.
- Google Flow must preserve at least 80 percent of delta compositions in a five-pair smoke test.

## Preview limitations to carry into implementation

- Direction B generated more than forty visible figures. Future prompts should say `a crowd that
reads as about forty people` unless exact counting is necessary.
- Direction B allowed blue crowd shirts. Future locks reserve saturated channel blue for Toss.
- Direction C changed the crowd from loose side masses into a corridor. This improves cinematic
  depth but changes the original geometry too much for a delta edit.
- All three previews preserved the headline, but production text should still be added in CapCut
  when exact spelling is mission-critical.
