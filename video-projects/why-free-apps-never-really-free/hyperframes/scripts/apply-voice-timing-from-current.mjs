import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectDir = path.resolve(__dirname, "..");
const videoDir = path.resolve(projectDir, "..");

const sourceResultsDir = process.env.HF_SOURCE_VOICE_RESULTS_DIR ?? "david23-balanced-paced";
const targetResultsDir = process.env.HF_TARGET_VOICE_RESULTS_DIR ?? "david23-slow-careful";
const targetAssetDir = process.env.HF_TARGET_VOICE_ASSET_DIR ?? targetResultsDir;

const audioIds = [
  "free-gifts",
  "pricing-reframe",
  "attention-ads",
  "behavior-habit",
  "freemium-pain",
  "lock-in",
  "label-stack",
  "hidden-checkout",
];

const num = (value) => {
  const fixed = Number(value.toFixed(3));
  return Object.is(fixed, -0) ? 0 : fixed;
};

const clipDuration = (start, end) => num(Math.max(0, end - start - 0.001));

function readResults(dir) {
  const file = path.join(videoDir, "voiceover", dir, "generation-results.json");
  const rows = JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
  const byId = new Map(rows.map((row) => [row.id, Number(row.duration)]));

  return audioIds.map((id) => {
    const duration = byId.get(id);
    if (!duration) {
      throw new Error(`Missing duration for ${id} in ${dir}`);
    }
    return { id, duration };
  });
}

function withTimeline(items) {
  let cursor = 0;
  return items.map((item) => {
    const start = cursor;
    const end = cursor + item.duration;
    cursor = end;
    return { ...item, start, end };
  });
}

const sourceTimeline = withTimeline(readResults(sourceResultsDir));
const targetTimeline = withTimeline(readResults(targetResultsDir));
const sourceFullDuration = sourceTimeline.at(-1).end;
const targetFullDuration = targetTimeline.at(-1).end;
const indexPath = path.join(projectDir, "index.html");
const currentIndex = fs.readFileSync(indexPath, "utf8");

const partRegex =
  /<div id="([^"]+)" class="clip" data-composition-id="([^"]+)" data-composition-src="compositions\/([^"]+\.html)" data-start="([0-9.]+)" data-duration="([0-9.]+)" data-track-index="1"><\/div>/g;

const parts = [...currentIndex.matchAll(partRegex)].map((match) => ({
  slug: match[1],
  id: match[2],
  file: match[3],
  oldStart: Number(match[4]),
  oldEnd: Number(match[4]) + Number(match[5]) + 0.001,
}));

if (parts.length !== 12) {
  throw new Error(`Expected 12 part clips in index.html, found ${parts.length}`);
}

parts.at(-1).oldEnd = sourceFullDuration;

function mapGlobalTime(sourceTime) {
  if (Math.abs(sourceTime - sourceFullDuration) < 0.03) {
    return targetFullDuration;
  }

  const index = sourceTimeline.findIndex(
    (audio) => sourceTime >= audio.start - 0.002 && sourceTime <= audio.end + 0.002,
  );

  if (index === -1) {
    throw new Error(`Could not map source time ${sourceTime}`);
  }

  const sourceAudio = sourceTimeline[index];
  const targetAudio = targetTimeline[index];
  const ratio = targetAudio.duration / sourceAudio.duration;
  return targetAudio.start + (sourceTime - sourceAudio.start) * ratio;
}

const targetParts = parts.map((part) => ({
  ...part,
  newStart: mapGlobalTime(part.oldStart),
  newEnd: mapGlobalTime(part.oldEnd),
}));

function scaleTimedAttributes(html, scale) {
  return html.replace(
    /\b(data-(?:start|duration|appear|wiggle-start|media-start)=")([0-9.]+)(")/g,
    (_, prefix, value, suffix) => `${prefix}${num(Number(value) * scale)}${suffix}`,
  );
}

function setTimelineCycleDuration(html, duration) {
  return html.replace(
    /Math\.ceil\(\(([0-9.]+) - start\) \/ 0\.8\)/g,
    `Math.ceil((${num(duration)} - start) / 0.8)`,
  );
}

function updateComposition(part) {
  const file = path.join(projectDir, "compositions", part.file);
  const sourceDuration = part.oldEnd - part.oldStart;
  const targetDuration = part.newEnd - part.newStart;
  const scale = targetDuration / sourceDuration;
  let html = fs.readFileSync(file, "utf8");

  html = scaleTimedAttributes(html, scale);
  html = html.replace(
    new RegExp(`data-composition-id="${part.id}" data-start="0" data-duration="[^"]+"`),
    `data-composition-id="${part.id}" data-start="0" data-duration="${clipDuration(part.newStart, part.newEnd)}"`,
  );
  html = setTimelineCycleDuration(html, clipDuration(part.newStart, part.newEnd));

  fs.writeFileSync(file, html);
}

function renderAudio(start, end, assetPrefix) {
  return targetTimeline
    .filter((audio) => audio.end > start + 0.001 && audio.start < end - 0.001)
    .map((audio) => {
      const overlapStart = Math.max(audio.start, start);
      const overlapEnd = Math.min(audio.end, end);
      const mediaStart = num(overlapStart - audio.start);
      return `<audio id="audio-${audio.id}" src="${assetPrefix}assets/voiceover/${targetAssetDir}/${audio.id}.mp3" data-start="${num(overlapStart - start)}" data-duration="${clipDuration(overlapStart, overlapEnd)}" data-media-start="${mediaStart}" data-track-index="0" data-volume="1"></audio>`;
    })
    .join("\n      ");
}

function updatePartPreview(part) {
  const file = path.join(projectDir, "part-previews", part.file);
  const duration = clipDuration(part.newStart, part.newEnd);
  let html = fs.readFileSync(file, "utf8");

  html = html.replace(
    /data-composition-id="[^"]+AudioPreview" data-start="0" data-duration="[^"]+"/,
    `data-composition-id="${part.id}AudioPreview" data-start="0" data-duration="${duration}"`,
  );
  html = html.replace(
    /(\s*)<audio[\s\S]*?(?=\n\s*<div id="part-)/,
    `\n      ${renderAudio(part.newStart, part.newEnd, "../")}`,
  );
  html = html.replace(
    new RegExp(`(<div id="${part.slug}"[^>]*data-start=")0(" data-duration=")[^"]+(")`),
    `$10$2${duration}$3`,
  );

  fs.writeFileSync(file, html);
}

function updateIndex() {
  const fullDuration = clipDuration(0, targetFullDuration);
  let html = fs.readFileSync(indexPath, "utf8");

  html = html.replace(
    /data-composition-id="FullVideo" data-start="0" data-duration="[^"]+"/,
    `data-composition-id="FullVideo" data-start="0" data-duration="${fullDuration}"`,
  );
  html = html.replace(
    /(\s*)<audio[\s\S]*?(?=\n\s*<div id="part-01-hook")/,
    `\n      ${renderAudio(0, targetFullDuration, "")}`,
  );

  for (const part of targetParts) {
    html = html.replace(
      new RegExp(`(<div id="${part.slug}"[^>]*data-start=")[^"]+(" data-duration=")[^"]+(")`),
      `$1${num(part.newStart)}$2${clipDuration(part.newStart, part.newEnd)}$3`,
    );
  }

  html = setTimelineCycleDuration(html, fullDuration);
  fs.writeFileSync(indexPath, html);
}

for (const part of targetParts) {
  updateComposition(part);
  updatePartPreview(part);
}
updateIndex();

console.log(
  JSON.stringify(
    {
      sourceResultsDir,
      targetResultsDir,
      sourceDuration: num(sourceFullDuration),
      targetDuration: num(targetFullDuration),
      audio: targetTimeline.map((audio) => ({
        id: audio.id,
        start: num(audio.start),
        duration: num(audio.duration),
        end: num(audio.end),
      })),
      parts: targetParts.map((part) => ({
        id: part.id,
        slug: part.slug,
        start: num(part.newStart),
        duration: clipDuration(part.newStart, part.newEnd),
      })),
    },
    null,
    2,
  ),
);
