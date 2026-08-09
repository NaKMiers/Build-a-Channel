# Video Swipe Memory

## Environment

- Prefer system ffmpeg. If unavailable, `tools/video-frames.py ensure-ffmpeg` installs a
  static build under `~/.cache/humanprice-ffmpeg`.
- YouTube oEmbed provides public title and author without an API key. The watch page may
  still trigger a bot check, so duration can come from `/browse` as `--expect-duration`.
- An unreachable verification request is a hard error. Offline verification requires an
  explicit user choice.

## Durable analysis lessons

- Contact sheets are navigation aids. Review every selected frame at readable size.
- Candidate extraction proposes cuts; the agent decides which frames are distinct.
- Keep pacing, transition, hierarchy, and narrative mechanisms separate from rendering
  style. HumanPrice can borrow the former, never copy the latter.
- Subtitle animation can inflate scene-change counts. Thresholds must be tuned to the
  competitor's editing grammar.
- Record what transfers to a HumanPrice scene prompt and what violates the style lock.
