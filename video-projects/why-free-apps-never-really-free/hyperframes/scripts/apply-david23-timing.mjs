import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectDir = path.resolve(__dirname, "..");
const voiceName = process.env.HF_VOICE_NAME ?? "David23";
const voiceResultsDir = process.env.HF_VOICE_RESULTS_DIR ?? "david23";
const voiceAssetDir = process.env.HF_VOICE_ASSET_DIR ?? voiceResultsDir;
const voiceResultsPath = path.resolve(projectDir, "..", "voiceover", voiceResultsDir, "generation-results.json");

const oldAudio = [
  { id: "free-gifts", duration: 23.17 },
  { id: "pricing-reframe", duration: 43.65 },
  { id: "attention-ads", duration: 38.77 },
  { id: "behavior-habit", duration: 28.24 },
  { id: "freemium-pain", duration: 21.21 },
  { id: "lock-in", duration: 21.26 },
  { id: "label-stack", duration: 22.39 },
  { id: "hidden-checkout", duration: 41.22 },
];

const oldParts = [
  { id: "Part01Hook", slug: "part-01-hook", start: 0, end: 23.17 },
  { id: "Part02TheSuspicion", slug: "part-02-the-suspicion", start: 23.17, end: 36.19 },
  { id: "Part03Reframe", slug: "part-03-reframe", start: 36.19, end: 54 },
  { id: "Part04WhatFreeReallyMeans", slug: "part-04-what-free-really-means", start: 54, end: 66.82 },
  { id: "Part05Method1Ads", slug: "part-05-method-1-ads", start: 66.82, end: 85.97 },
  { id: "Part06Retention", slug: "part-06-retention", start: 85.97, end: 105.59 },
  { id: "Part07Method2Behavior", slug: "part-07-method-2-behavior", start: 105.59, end: 133.83 },
  { id: "Part08Freemium", slug: "part-08-freemium", start: 133.83, end: 155.04 },
  { id: "Part09Method3LockIn", slug: "part-09-method-3-lock-in", start: 155.04, end: 176.3 },
  { id: "Part10YouAreTheProduct", slug: "part-10-you-are-the-product", start: 176.3, end: 198.69 },
  { id: "Part11MainLesson", slug: "part-11-main-lesson", start: 198.69, end: 224 },
  { id: "Part12PayoffEnding", slug: "part-12-payoff-ending", start: 224, end: 239.91 },
];

const num = (value) => {
  const fixed = Number(value.toFixed(3));
  return Object.is(fixed, -0) ? 0 : fixed;
};

const clipDuration = (start, end) => num(Math.max(0, end - start - 0.001));

const results = JSON.parse(fs.readFileSync(voiceResultsPath, "utf8").replace(/^\uFEFF/, ""));
const newDurationById = new Map(results.map((item) => [item.id, Number(item.duration)]));
const indexPath = path.join(projectDir, "index.html");

if (!process.env.FORCE_DAVID23_TIMING && fs.existsSync(indexPath)) {
  const currentIndex = fs.readFileSync(indexPath, "utf8");
  if (currentIndex.includes(`assets/voiceover/${voiceAssetDir}/`) && !currentIndex.includes("assets/voiceover/george-restored/")) {
    console.log(JSON.stringify({ ok: true, skipped: true, reason: `${voiceName} timing is already applied.` }, null, 2));
    process.exit(0);
  }
}

function withTimeline(audioList, durationFor) {
  let cursor = 0;
  return audioList.map((audio) => {
    const duration = durationFor(audio);
    const item = { ...audio, start: cursor, end: cursor + duration, duration };
    cursor += duration;
    return item;
  });
}

const oldTimeline = withTimeline(oldAudio, (audio) => audio.duration);
const newTimeline = withTimeline(oldAudio, (audio) => {
  const duration = newDurationById.get(audio.id);
  if (!duration) throw new Error(`Missing David23 duration for ${audio.id}`);
  return duration;
});

function mapGlobalTime(oldTime) {
  const finalOld = oldTimeline.at(-1).end;
  if (Math.abs(oldTime - finalOld) < 0.02) return newTimeline.at(-1).end;

  const index = oldTimeline.findIndex((audio) => oldTime >= audio.start - 0.001 && oldTime <= audio.end + 0.001);
  if (index === -1) throw new Error(`Could not map old time ${oldTime}`);

  const oldAudioItem = oldTimeline[index];
  const newAudioItem = newTimeline[index];
  const ratio = newAudioItem.duration / oldAudioItem.duration;
  return newAudioItem.start + (oldTime - oldAudioItem.start) * ratio;
}

const newParts = oldParts.map((part) => ({
  ...part,
  oldDuration: part.end - part.start,
  start: mapGlobalTime(part.start),
  end: mapGlobalTime(part.end),
}));

function scaleTimedAttributes(html, scale) {
  return html.replace(/\b(data-(?:start|duration|appear|wiggle-start|media-start)=")([0-9.]+)(")/g, (_, prefix, value, suffix) => {
    return `${prefix}${num(Number(value) * scale)}${suffix}`;
  });
}

function setTimelineCycleDuration(html, duration) {
  return html.replace(/Math\.ceil\(\(([0-9.]+) - start\) \/ 0\.8\)/g, `Math.ceil((${num(duration)} - start) / 0.8)`);
}

function updateComposition(part) {
  const file = path.join(projectDir, "compositions", `${part.slug}.html`);
  const oldPart = oldParts.find((item) => item.slug === part.slug);
  const oldDuration = oldPart.end - oldPart.start;
  const newDuration = part.end - part.start;
  const scale = newDuration / oldDuration;
  let html = fs.readFileSync(file, "utf8");

  html = scaleTimedAttributes(html, scale);
  html = html.replace(
    new RegExp(`data-composition-id="${part.id}" data-start="0" data-duration="[^"]+"`),
    `data-composition-id="${part.id}" data-start="0" data-duration="${clipDuration(part.start, part.end)}"`,
  );
  html = setTimelineCycleDuration(html, clipDuration(part.start, part.end));

  fs.writeFileSync(file, html);
}

function renderAudio(part) {
  return newTimeline
    .filter((audio) => audio.end > part.start + 0.001 && audio.start < part.end - 0.001)
    .map((audio) => {
      const overlapStart = Math.max(audio.start, part.start);
      const overlapEnd = Math.min(audio.end, part.end);
      const mediaStart = num(overlapStart - audio.start);
      const playbackRate = audio.id === "behavior-habit" ? ' data-playback-rate="1"' : "";
      return `<audio${playbackRate} id="audio-${audio.id}" src="../assets/voiceover/${voiceAssetDir}/${audio.id}.mp3" data-start="${num(overlapStart - part.start)}" data-duration="${clipDuration(overlapStart, overlapEnd)}" data-media-start="${mediaStart}" data-track-index="0" data-volume="1"></audio>`;
    })
    .join("\n      ");
}

function updatePartPreview(part) {
  const file = path.join(projectDir, "part-previews", `${part.slug}.html`);
  let html = fs.readFileSync(file, "utf8");
  const duration = clipDuration(part.start, part.end);
  const audioHtml = renderAudio(part);

  html = html.replace(
    /data-composition-id="[^"]+AudioPreview" data-start="0" data-duration="[^"]+"/,
    `data-composition-id="${part.id}AudioPreview" data-start="0" data-duration="${duration}"`,
  );
  html = html.replace(
    /(\s*)<audio[\s\S]*?(?=\n\s*<div id="part-)/,
    `\n      ${audioHtml}`,
  );
  html = html.replace(
    new RegExp(`(<div id="${part.slug}"[^>]*data-start=")0(" data-duration=")[^"]+(")`),
    `$10$2${duration}$3`,
  );

  fs.writeFileSync(file, html);
}

function updateIndex() {
  const file = indexPath;
  let html = fs.readFileSync(file, "utf8");
  const fullDuration = clipDuration(0, newTimeline.at(-1).end);
  const audioHtml = newTimeline
    .map((audio) => {
      const playbackRate = audio.id === "behavior-habit" ? ' data-playback-rate="1"' : "";
      return `<audio${playbackRate} id="audio-${audio.id}" src="assets/voiceover/${voiceAssetDir}/${audio.id}.mp3" data-start="${num(audio.start)}" data-duration="${clipDuration(audio.start, audio.end)}" data-media-start="0" data-track-index="0" data-volume="1"></audio>`;
    })
    .join("\n      ");

  html = html.replace(
    /data-composition-id="FullVideo" data-start="0" data-duration="[^"]+"/,
    `data-composition-id="FullVideo" data-start="0" data-duration="${fullDuration}"`,
  );
  html = html.replace(
    /(\s*)<audio[\s\S]*?(?=\n\s*<div id="part-01-hook")/,
    `\n      ${audioHtml}`,
  );

  for (const part of newParts) {
    const duration = clipDuration(part.start, part.end);
    html = html.replace(
      new RegExp(`(<div id="${part.slug}"[^>]*data-start=")[^"]+(" data-duration=")[^"]+(")`),
      `$1${num(part.start)}$2${duration}$3`,
    );
  }

  html = setTimelineCycleDuration(html, fullDuration);
  fs.writeFileSync(file, html);
}

for (const part of newParts) {
  updateComposition(part);
  updatePartPreview(part);
}
updateIndex();

const fullDuration = clipDuration(0, newTimeline.at(-1).end);

console.log(JSON.stringify({
  voice: voiceName,
  audio: newTimeline.map((audio) => ({
    id: audio.id,
    start: num(audio.start),
    duration: num(audio.duration),
    end: num(audio.end),
  })),
  parts: newParts.map((part) => ({
    id: part.id,
    slug: part.slug,
    start: num(part.start),
    duration: clipDuration(part.start, part.end),
    scale: num((part.end - part.start) / part.oldDuration),
  })),
  fullDuration: fullDuration,
}, null, 2));
