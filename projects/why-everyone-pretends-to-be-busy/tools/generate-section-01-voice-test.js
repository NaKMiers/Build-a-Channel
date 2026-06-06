const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const voiceoverRoot = path.join(projectRoot, "voiceover");
const fullMapPath = path.join(voiceoverRoot, "word-performance-map.json");
const outputDir = path.join(voiceoverRoot, "section-01-hook");
const ttsDir = path.join(outputDir, "tts-inputs");
const scratchAudioDir = path.join(outputDir, "scratch-audio");

const sectionId = "hook";
const sectionTitle = "Section 1: Hook";
const targetDurationSeconds = 24.085;

const scriptLines = [
  "Here is something weird about modern life.",
  "The less time you have to do real work, the more professional you look.",
  "If your calendar is full, your inbox is exploding, and your phone keeps making tiny panic noises, people assume you are important.",
  "But if you sit quietly and think about one hard problem, people may assume you are lazy. Or unemployed. Or having a small spiritual crisis.",
  "So everyone becomes busy. Or at least, everyone becomes very good at looking busy."
];

const markedLines = [
  "Here is something [emphasis: weird] about modern life.",
  "The [emphasis: less time] you have to do [emphasis: real work], the more [emphasis: professional] you look.",
  "If your [emphasis: calendar] is full, your [emphasis: inbox] is exploding, and your [emphasis: phone] keeps making tiny [emphasis: panic noises], people assume you are [emphasis: important].",
  "But if you sit quietly and think about one hard problem, people may assume you are [emphasis: lazy]. [deadpan] Or unemployed. [deadpan] Or having a small spiritual crisis.",
  "So everyone becomes [emphasis: busy]. Or at least, everyone becomes very good at [emphasis: looking busy]."
];

const variant = {
  id: "young-fast",
  name: "single young fast hook test",
  intendedVoice: "young male around age 22",
  scratchVoice: "am_adam",
  speed: 1.05,
  language: "en-us",
  durationSeconds: targetDurationSeconds,
  outputFile: "scratch-audio/section-01-hook-young-fast-am_adam-1.05.mp3"
};

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function stripMarkup(text) {
  return text
    .replace(/\[(?:deadpan|slower)\]\s*/g, "")
    .replace(/\[emphasis:\s*([^\]]+)\]/g, "$1")
    .trim();
}

function getSectionMap() {
  const fullMap = JSON.parse(fs.readFileSync(fullMapPath, "utf8"));
  const sectionEvents = fullMap.timeline.filter((event) => event.section === sectionId);
  const sectionWords = sectionEvents.filter((event) => event.type === "word");

  const start = sectionEvents[0]?.estimatedStart ?? 0;
  const end = sectionEvents[sectionEvents.length - 1]?.estimatedEnd ?? 1;
  const originalDuration = end - start;
  const scale = targetDurationSeconds / originalDuration;

  function adjust(event) {
    const adjusted = { ...event };
    adjusted.estimatedStart = Number(((event.estimatedStart - start) * scale).toFixed(3));
    adjusted.estimatedEnd = Number(((event.estimatedEnd - start) * scale).toFixed(3));
    if (typeof event.duration === "number") adjusted.duration = Number((event.duration * scale).toFixed(3));
    if (typeof event.pauseAfter === "number") adjusted.pauseAfter = Number((event.pauseAfter * scale).toFixed(3));
    return adjusted;
  }

  return {
    video: {
      title: "Why Everyone Pretends To Be Busy",
      slug: "why-everyone-pretends-to-be-busy",
      section: sectionTitle,
      status: "Step 10.1 young-fast voice test map",
      timingWarning: "Estimated timings are scaled to the 24.085s young-fast scratch MP3. Replace with forced-alignment timestamps after final approved audio exists."
    },
    narrator: {
      name: "young-fast scratch voice",
      scratchVoice: variant.scratchVoice,
      intendedFinalVoice: "David23 / am_eric when available",
      speed: variant.speed,
      language: variant.language,
      note: "Local HyperFrames TTS does not expose am_eric, so am_adam is used for timing and young-tone direction only."
    },
    policy: {
      spokenFillers: "disabled",
      fillerReason: "Hook target is about 25s; avoid spoken fillers and exaggerated blank-line pauses.",
      deliveryTarget: "young, clear, fast, dry, lightly suspicious"
    },
    stats: {
      words: sectionWords.length,
      timelineEvents: sectionEvents.length,
      estimatedRuntimeSeconds: targetDurationSeconds,
      targetBoardRuntimeSeconds: 25
    },
    variants: [variant],
    timeline: sectionEvents.map(adjust),
    wordsOnly: sectionWords.map(adjust)
  };
}

function writeReadme() {
  const markdown = `# Step 10.1 - Section 1 Voice Test

Video: \`Why Everyone Pretends To Be Busy\`

Section: \`Section 1: Hook\`

Status: \`remade as one young-fast voice test\`

## Result

The old slow scratch files were removed.

Current voice test:

- File: \`${variant.outputFile}\`
- Local scratch voice: \`${variant.scratchVoice}\`
- Speed: \`${variant.speed}\`
- Duration: \`${targetDurationSeconds}s\`
- Target: about \`25s\`
- Audio output rule: keep only the most useful final preview format, not both MP3 and WAV.

## Direction

Voice should sound:

- young male, around age \`22\`
- clear and bright
- casual, dry, lightly suspicious
- not elder, not deep, not theatrical
- fast enough for a hook, but still understandable

## Script Input

Use:

\`tts-inputs/section-01-hook-young-fast.txt\`

This version removes the exaggerated blank-line pauses from the earlier test.

## Production Decision

Use this \`${targetDurationSeconds}s\` test as the Section 1 timing reference.

Retiming note:
the old board target \`0:00-0:29\` was acceptable as a rough estimate, but the current approved direction is tighter: Section 1 should land around \`24-25s\`.

## Caveat

This is still scratch audio because local HyperFrames TTS does not expose the approved channel voice \`David23 / am_eric\`. It is useful for timing and tone direction. Final voice can be regenerated later with the approved voice once the generator supports it.
`;

  fs.writeFileSync(path.join(outputDir, "README.md"), markdown, "utf8");
}

function writeScratchResults() {
  const output = {
    video: "Why Everyone Pretends To Be Busy",
    section: sectionTitle,
    status: "remade as one young-fast scratch voice test",
    warning: "This file uses am_adam because the local HyperFrames TTS command does not currently expose the approved David23 base voice am_eric. Use it for timing and tone direction, not final brand approval.",
    generatedWith: {
      tool: "npx hyperframes tts",
      voice: variant.scratchVoice,
      speed: variant.speed,
      language: variant.language
    },
    result: {
      variant: variant.id,
      file: variant.outputFile,
      durationSeconds: targetDurationSeconds,
      targetDurationSeconds: 25,
      use: "Section 1 timing reference"
    },
    audioOutputRule: "Keep only one final audio preview file, choosing the most useful format. For this section, keep MP3 and remove the temporary WAV.",
    removedOldScratchAudio: true,
    productionDecision: "Retiming Section 1 around 24-25 seconds is now preferred over the earlier 29 second estimate."
  };

  fs.writeFileSync(path.join(outputDir, "scratch-results.json"), JSON.stringify(output, null, 2), "utf8");
}

function writeFiles() {
  ensureDir(outputDir);
  ensureDir(ttsDir);
  ensureDir(scratchAudioDir);

  for (const file of fs.readdirSync(ttsDir)) {
    if (file.startsWith("variant-")) fs.unlinkSync(path.join(ttsDir, file));
  }

  const sectionMap = getSectionMap();
  fs.writeFileSync(path.join(outputDir, "section-01-script.txt"), `${scriptLines.join("\n")}\n`, "utf8");
  fs.writeFileSync(path.join(outputDir, "section-01-marked-script.md"), `# Section 1 Marked Script\n\n${markedLines.join("\n")}\n`, "utf8");
  fs.writeFileSync(path.join(outputDir, "section-01-voice-performance-map.json"), JSON.stringify(sectionMap, null, 2), "utf8");
  fs.writeFileSync(path.join(ttsDir, "section-01-hook-young-fast.txt"), `${scriptLines.join("\n")}\n`, "utf8");
  fs.writeFileSync(path.join(ttsDir, "section-01-hook-young-fast-direction.md"), `# Section 1 Young Fast Voice Direction\n\nVoice test target:\nyoung male narrator, around age 22, bright and clear, not elder, not deep, not dramatic.\n\nLocal scratch voice:\n\`${variant.scratchVoice}\`\n\nSpeed target:\nfast enough to land near \`25s\`, but still understandable for English learners.\n\nDelivery:\ndry, casual, lightly suspicious. Do not over-pause after every sentence. Keep the final line dry, not theatrical.\n`, "utf8");
  writeReadme();
  writeScratchResults();
}

writeFiles();
console.log(path.relative(process.cwd(), outputDir));
