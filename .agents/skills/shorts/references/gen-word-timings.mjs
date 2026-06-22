// gen-word-timings.mjs — word-level timings for one short's voiceover.
//
// Usage:
//   1) decode the short mp3 to 16 kHz mono f32:  <ffmpeg> -y -i short.mp3 -ar 16000 -ac 1 -f f32le out.raw
//   2) node gen-word-timings.mjs out.raw short-0N-word-timings.json
//
// IMPORTANT: Node ESM resolves @xenova/transformers from THIS script's folder, not cwd.
// Run from a folder that has the package installed (e.g. %TEMP%/wiw-whisper/ already has it
// plus the cached whisper-tiny.en model). Copy this file there, or `npm i @xenova/transformers@2.17.2`.
//
// Tail glitch: whisper-tiny.en can stamp the last few words non-monotonically at end-of-audio.
// After writing, sanity-check the final 1-2 words and re-time the last caption line monotonically
// up to the audio duration when building the short's captions.

import { pipeline } from '@xenova/transformers';
import fs from 'node:fs';

const raw = process.argv[2];
const out = process.argv[3];
if (!raw || !out) {
  console.error('usage: node gen-word-timings.mjs <input.raw f32le 16kHz mono> <output.json>');
  process.exit(1);
}

const buf = fs.readFileSync(raw);
const audio = new Float32Array(buf.buffer, buf.byteOffset, Math.floor(buf.byteLength / 4));

const t = await pipeline('automatic-speech-recognition', 'Xenova/whisper-tiny.en');
const o = await t(audio, { return_timestamps: 'word', chunk_length_s: 30, stride_length_s: 5 });

const words = (o.chunks || []).map(c => ({
  word: (c.text || '').trim(),
  start: c.timestamp && c.timestamp[0] != null ? c.timestamp[0] : null,
  end: c.timestamp && c.timestamp[1] != null ? c.timestamp[1] : null,
}));

fs.writeFileSync(out, JSON.stringify({ transcript: (o.text || '').trim(), words }, null, 2));
console.log('WROTE ' + words.length + ' words -> ' + out);
console.log(words.map(w => w.start + '-' + w.end + ' ' + w.word).join('\n'));
