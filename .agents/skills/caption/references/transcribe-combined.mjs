// Caption skill — full-audio word-level transcription helper.
// Usage:
//   node transcribe-combined.mjs <full-audio.mp3> <out-timings.json> <ffmpeg.exe>
// Output JSON: { text, words: [{ word, start, end }] }
//
// Reuses Xenova/whisper-tiny.en via @xenova/transformers. Run from a folder
// that has @xenova/transformers installed (e.g. %TEMP%/wiw-whisper). First run
// downloads the tiny model (~tens of MB); afterwards it is cached.
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { pipeline, env } from "@xenova/transformers";

env.allowLocalModels = false;

const AUDIO = process.argv[2];
const OUT = process.argv[3];
const FFMPEG = process.argv[4];
const RAW = (process.env.TEMP || ".") + "/wiw-caption.raw";

execFileSync(FFMPEG, ["-y", "-i", AUDIO, "-ar", "16000", "-ac", "1", "-f", "f32le", RAW], { stdio: "ignore" });
const buf = readFileSync(RAW);
const audio = new Float32Array(buf.buffer, buf.byteOffset, Math.floor(buf.length / 4));
console.error("samples:", audio.length, "dur:", (audio.length / 16000).toFixed(3), "s");

const t = await pipeline("automatic-speech-recognition", "Xenova/whisper-tiny.en");
const o = await t(audio, { return_timestamps: "word", chunk_length_s: 30, stride_length_s: 5 });

const words = [];
for (const c of o.chunks) {
  const w = (c.text || "").trim();
  if (!w) continue;
  const [s, e] = c.timestamp;
  words.push({ word: w, start: s ?? 0, end: e ?? s ?? 0 });
}
writeFileSync(OUT, JSON.stringify({ text: o.text, words }, null, 2));
console.error("wrote", words.length, "words; last end:", words.at(-1)?.end);
