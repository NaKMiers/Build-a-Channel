// Caption skill — align exact script cues to real word timestamps and write SRT.
// Usage:
//   node build-srt.mjs <timings.json> <cues.json> <out.srt> [audioDurationSeconds] [segments.json]
//
// timings.json  : { words: [{ word, start, end }] }  (from transcribe-combined.mjs)
// cues.json     : ["First caption line.", "Second line.", ...] exact display text
//                 derived from the project's 02-script.md narration, in order.
// out.srt       : output path (export under projects/<slug>/output/captions/english.srt)
// segments.json : OPTIONAL output path. When given, also writes the per-cue
//                 timing table [{ index, start, end, text }] so the multi-language
//                 step can reuse the EXACT same timing for every translated SRT
//                 (timing comes once from the real audio; translations only swap text).
//
// Words shown come from cues.json (ground truth). Timing comes from the audio
// (Needleman-Wunsch alignment of normalized tokens), so wording is exact and
// timing matches the voice. Unmatched cue words are time-interpolated.
import { readFileSync, writeFileSync } from "node:fs";

const TIMINGS = process.argv[2];
const CUES = process.argv[3];
const OUT = process.argv[4];
const AUDIO_DUR = process.argv[5] ? parseFloat(process.argv[5]) : null;
const SEGMENTS_OUT = process.argv[6] || null;

const cues = JSON.parse(readFileSync(CUES, "utf8"));
const data = JSON.parse(readFileSync(TIMINGS, "utf8"));

const NUMMAP = { zero:"0", one:"1", two:"2", three:"3", four:"4", five:"5", six:"6", seven:"7", eight:"8", nine:"9", ten:"10" };
function norm(w) {
  let s = w.toLowerCase().replace(/&/g, "and").replace(/\$/g, "");
  s = s.replace(/[^a-z0-9]/g, "");
  if (NUMMAP[s]) s = NUMMAP[s];
  return s;
}

const gt = [];
cues.forEach((c, ci) => {
  for (const raw of c.split(/\s+/)) {
    const n = norm(raw);
    if (n) gt.push({ ci, n });
  }
});
const hyp = data.words.map(w => ({ n: norm(w.word), start: w.start, end: w.end })).filter(w => w.n);

const N = gt.length, M = hyp.length;
const MATCH = 2, MIS = -1, GAP = -1;
const dp = Array.from({ length: N + 1 }, () => new Float64Array(M + 1));
const bt = Array.from({ length: N + 1 }, () => new Int8Array(M + 1));
for (let i = 1; i <= N; i++) { dp[i][0] = i * GAP; bt[i][0] = 1; }
for (let j = 1; j <= M; j++) { dp[0][j] = j * GAP; bt[0][j] = 2; }
for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= M; j++) {
    const s = gt[i - 1].n === hyp[j - 1].n ? MATCH : MIS;
    const diag = dp[i - 1][j - 1] + s;
    const up = dp[i - 1][j] + GAP;
    const left = dp[i][j - 1] + GAP;
    let best = diag, dir = 0;
    if (up > best) { best = up; dir = 1; }
    if (left > best) { best = left; dir = 2; }
    dp[i][j] = best; bt[i][j] = dir;
  }
}
const gtTime = new Array(N).fill(null);
let i = N, j = M;
while (i > 0 || j > 0) {
  const dir = (i > 0 && j > 0) ? bt[i][j] : (i > 0 ? 1 : 2);
  if (dir === 0) {
    if (gt[i - 1].n === hyp[j - 1].n) gtTime[i - 1] = { start: hyp[j - 1].start, end: hyp[j - 1].end };
    i--; j--;
  } else if (dir === 1) { i--; } else { j--; }
}
for (let k = 0; k < N; k++) {
  if (gtTime[k]) continue;
  let p = k - 1; while (p >= 0 && !gtTime[p]) p--;
  let nq = k + 1; while (nq < N && !gtTime[nq]) nq++;
  const prev = p >= 0 ? gtTime[p].end : null;
  const next = nq < N ? gtTime[nq].start : null;
  if (prev != null && next != null) {
    const t = prev + (next - prev) * ((k - p) / (nq - p));
    gtTime[k] = { start: t, end: t };
  } else if (prev != null) gtTime[k] = { start: prev, end: prev };
  else if (next != null) gtTime[k] = { start: next, end: next };
  else gtTime[k] = { start: 0, end: 0 };
}

const segs = cues.map(() => ({ start: null, end: null }));
gt.forEach((g, k) => {
  const t = gtTime[k], s = segs[g.ci];
  if (s.start == null || t.start < s.start) s.start = t.start;
  if (s.end == null || t.end > s.end) s.end = t.end;
});
const MIN = 0.7;
for (let k = 0; k < segs.length; k++) {
  if (segs[k].start == null) segs[k].start = k > 0 ? segs[k - 1].end : 0;
  if (segs[k].end == null || segs[k].end <= segs[k].start) segs[k].end = segs[k].start + MIN;
  if (k > 0 && segs[k].start < segs[k - 1].end) segs[k].start = segs[k - 1].end;
  if (segs[k].end <= segs[k].start) segs[k].end = segs[k].start + MIN;
}
for (let k = 0; k < segs.length - 1; k++) {
  if (segs[k + 1].start > segs[k].end) segs[k].end = segs[k + 1].start;
}
const last = segs[segs.length - 1];
const cap = AUDIO_DUR || (hyp.length ? hyp[hyp.length - 1].end : last.end);
last.end = Math.min(Math.max(last.end, last.start + MIN), cap);

function ts(sec) {
  if (sec < 0) sec = 0;
  const ms = Math.round(sec * 1000);
  const p = (n, w) => String(n).padStart(w, "0");
  return `${p(Math.floor(ms / 3600000), 2)}:${p(Math.floor((ms % 3600000) / 60000), 2)}:${p(Math.floor((ms % 60000) / 1000), 2)},${p(ms % 1000, 3)}`;
}

let srt = "";
cues.forEach((c, idx) => { srt += `${idx + 1}\n${ts(segs[idx].start)} --> ${ts(segs[idx].end)}\n${c}\n\n`; });
writeFileSync(OUT, srt, "utf8");

if (SEGMENTS_OUT) {
  const table = cues.map((c, idx) => ({ index: idx + 1, start: segs[idx].start, end: segs[idx].end, text: c }));
  writeFileSync(SEGMENTS_OUT, JSON.stringify(table, null, 2), "utf8");
  console.error(`wrote ${table.length} timing segments -> ${SEGMENTS_OUT}`);
}

console.error(`cues: ${cues.length}, gt tokens: ${N}, hyp tokens: ${M}`);
console.error(`first: ${ts(segs[0].start)} --> ${ts(segs[0].end)}`);
console.error(`last:  ${ts(last.start)} --> ${ts(last.end)}`);
