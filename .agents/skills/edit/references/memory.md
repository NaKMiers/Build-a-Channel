# edit - memory

The transcript is the only place the real cut time still exists. `prompts/image-prompts.md`
and the scene file names both carry the truncated `[M:SS]`, so never derive a cut from a
file name when `transcribes/transcript.md` is present.

MLT counts a clip as `out - in + 1` frames. A clip meant to last N frames has `in="0"` and
`out=` frame `N-1`. Getting this wrong shifts every cut after it by one frame per clip.

Kdenlive's timecode is `HH:MM:SS.mmm` and the milliseconds must be derived from the frame
(`round(frame * 1000 / fps)`), never the other way round, or a frame lands one off.

An image producer's `length` must cover its longest timeline use. Kdenlive's own default
is five seconds; a cue that holds longer needs a longer producer or the clip truncates.

The generated project is `<project>/edit/`, not `outputs/`. `outputs/` is published
packaging, and a `.kdenlive` file full of absolute machine paths is not that.

Verified against the hand-built `~/Videos/11.kdenlive`: same MLT structure, same profile,
same track layout. Cuts confirmed frame-exact by rendering through `melt` and hashing the
frames around each boundary.
