// Caption skill — write a translated-language SRT by REUSING the exact English
// per-cue timing. Timing is never re-derived per language: every translated SRT
// shares the same cue boundaries that build-srt.mjs aligned to the real audio,
// so all 22 language tracks match the video frame-for-frame by construction.
//
// Usage:
//   node write-translated-srt.mjs <segments.json> <translated-cues.json> <out.srt>
//
// segments.json        : [{ index, start, end, text }]  (emitted by build-srt.mjs)
// translated-cues.json : ["translated line 1", "translated line 2", ...]
//                        ONE string per cue, SAME length & order as segments.
//                        The model produces this by translating each English cue
//                        in place (whole-cue translation, never word-by-word).
// out.srt              : output path, e.g. output/captions/vietnamese.srt
//
// Hard requirement: translated-cues length === segments length. A mismatch means
// a cue was split/merged/dropped during translation and timing would drift, so
// this script refuses to write rather than emit a misaligned track.
import { readFileSync, writeFileSync } from "node:fs";

const SEGMENTS = process.argv[2];
const CUES = process.argv[3];
const OUT = process.argv[4];

const segs = JSON.parse(readFileSync(SEGMENTS, "utf8"));
const cues = JSON.parse(readFileSync(CUES, "utf8"));

if (!Array.isArray(segs) || !Array.isArray(cues)) {
  console.error("ERROR: both inputs must be JSON arrays.");
  process.exit(1);
}
if (cues.length !== segs.length) {
  console.error(`ERROR: cue count mismatch — segments=${segs.length} translated=${cues.length}. ` +
    `Translate exactly one line per cue (keep count & order); do not split or merge cues.`);
  process.exit(1);
}
const empties = cues.map((c, i) => (c == null || String(c).trim() === "") ? i + 1 : null).filter(Boolean);
if (empties.length) {
  console.error(`ERROR: empty translated cue(s) at index: ${empties.join(", ")}`);
  process.exit(1);
}

function ts(sec) {
  if (sec < 0) sec = 0;
  const ms = Math.round(sec * 1000);
  const p = (n, w) => String(n).padStart(w, "0");
  return `${p(Math.floor(ms / 3600000), 2)}:${p(Math.floor((ms % 3600000) / 60000), 2)}:${p(Math.floor((ms % 60000) / 1000), 2)},${p(ms % 1000, 3)}`;
}

let srt = "";
segs.forEach((s, idx) => {
  srt += `${idx + 1}\n${ts(s.start)} --> ${ts(s.end)}\n${String(cues[idx]).trim()}\n\n`;
});
writeFileSync(OUT, srt, "utf8");

console.error(`wrote ${segs.length} cues -> ${OUT}`);
console.error(`first: ${ts(segs[0].start)} --> ${ts(segs[0].end)}`);
console.error(`last:  ${ts(segs.at(-1).start)} --> ${ts(segs.at(-1).end)}`);
