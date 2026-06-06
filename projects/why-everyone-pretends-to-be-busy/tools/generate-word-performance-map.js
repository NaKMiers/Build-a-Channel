const fs = require("fs");
const path = require("path");

const outputPath = path.resolve(__dirname, "../voiceover/word-performance-map.json");

const sections = [
  {
    id: "hook",
    title: "Hook",
    tone: "dry, observant, lightly suspicious",
    mood: "calm amusement",
    pace: "slow-normal",
    energy: "medium-low",
    lines: [
      "Here is something weird about modern life.",
      "The less time you have to do real work,",
      "the more professional you look.",
      "If your calendar is full,",
      "your inbox is exploding,",
      "and your phone keeps making tiny panic noises,",
      "people assume you are important.",
      "But if you sit quietly and think about one hard problem,",
      "people may assume you are lazy.",
      "Or unemployed.",
      "Or having a small spiritual crisis.",
      "So everyone becomes busy.",
      "Or at least,",
      "everyone becomes very good at looking busy."
    ]
  },
  {
    id: "reframe",
    title: "Reframe",
    tone: "clear, skeptical, explanatory",
    mood: "controlled suspicion",
    pace: "normal",
    energy: "medium",
    lines: [
      "This video is not about lazy people pretending to work.",
      "That is a different problem.",
      "This is about something stranger.",
      "Modern life often rewards the appearance of work more than the work itself.",
      "Because real progress is hard to see.",
      "But busyness is very visible.",
      "You can see meetings.",
      "You can see messages.",
      "You can see someone typing very fast with a serious face.",
      "You cannot always see thinking.",
      "Which is unfortunate,",
      "because thinking is where a lot of the actual work happens."
    ]
  },
  {
    id: "busy_became_status",
    title: "Part 1: Busy Became Status",
    tone: "deadpan social commentary",
    mood: "quietly amused",
    pace: "normal",
    energy: "medium",
    lines: [
      "The first reason people pretend to be busy is simple.",
      "Busy became status.",
      "When someone says,",
      "I'm so busy,",
      "it does not only mean they have many things to do.",
      "It can also mean,",
      "Please understand that I am important.",
      "This is why people say they are busy even when nobody asked.",
      "You ask,",
      "How are you?",
      "They say,",
      "Busy.",
      "Which is technically not an emotion,",
      "but we accept it because everyone is tired.",
      "Busy sounds responsible.",
      "Busy sounds needed.",
      "Busy sounds like your life has demand.",
      "And demand feels like value.",
      "If nobody needs you,",
      "that feels scary.",
      "If everyone needs you,",
      "that also feels scary,",
      "but at least you can put it on LinkedIn.",
      "So people fill their time.",
      "Sometimes with real work.",
      "Sometimes with meetings,",
      "calls,",
      "updates,",
      "planning documents,",
      "planning meetings,",
      "and meetings about why the planning document is not finished.",
      "At some point,",
      "the work is not the work anymore.",
      "The work is proving that you are near the work."
    ]
  },
  {
    id: "tools_create_fake_urgency",
    title: "Part 2: Tools Create Fake Urgency",
    tone: "calm description of ridiculous systems",
    mood: "mildly overwhelmed but dry",
    pace: "normal with list build",
    energy: "medium",
    lines: [
      "The second reason is that modern tools create fake urgency.",
      "Email was supposed to make communication easier.",
      "Then chat apps made email faster.",
      "Then project management apps organized the chat about the email.",
      "Then calendar apps scheduled meetings about why the project management app is confusing.",
      "And now your workday is basically five apps interrupting each other.",
      "Everything has a red dot.",
      "Everything has a number.",
      "Everything says urgent.",
      "Because please ignore this until later is apparently bad marketing.",
      "So your brain starts treating every notification like a tiny emergency.",
      "A message appears.",
      "You reply.",
      "Another message appears.",
      "You reply again.",
      "Then someone reacts to your reply with a thumbs up,",
      "and somehow your brain counts this as progress.",
      "Meanwhile,",
      "the important task is still sitting there.",
      "Quietly.",
      "Untouched.",
      "Like a sad vegetable in the back of the fridge."
    ]
  },
  {
    id: "visibility_beats_progress",
    title: "Part 3: Visibility Beats Progress",
    tone: "dry analytical",
    mood: "skeptical but fair",
    pace: "normal",
    energy: "medium",
    lines: [
      "The third reason is that visible work is easier to reward.",
      "If you answer messages quickly,",
      "people can see that.",
      "If you attend every meeting,",
      "people can see that.",
      "If you update a dashboard,",
      "write a report,",
      "and say just circling back,",
      "people can definitely see that.",
      "But if you spend two hours thinking deeply,",
      "the result may look like nothing happened.",
      "You might be solving the real problem.",
      "But from the outside,",
      "you are just sitting there.",
      "Possibly blinking.",
      "So people start doing work that looks like work.",
      "They reply fast.",
      "They join calls.",
      "They move tasks from one column to another column.",
      "They write updates about future updates.",
      "This is called productivity theater.",
      "It is like normal theater,",
      "except the tickets are paid in stress,",
      "and the main character is a spreadsheet."
    ]
  },
  {
    id: "busy_is_a_shield",
    title: "Part 4: I'm Busy Is A Shield",
    tone: "dry, human, slightly sympathetic",
    mood: "honest and amused",
    pace: "normal-slow",
    energy: "medium-low",
    lines: [
      "The fourth reason is that I'm busy is useful.",
      "It is a shield.",
      "Sometimes it means,",
      "I cannot take more work.",
      "Sometimes it means,",
      "I do not want to make this decision.",
      "Sometimes it means,",
      "Please stop asking me questions.",
      "And sometimes it means,",
      "I have no idea what I am doing,",
      "but I need to look serious until the answer appears.",
      "This is not always dishonest.",
      "A lot of people really are overloaded.",
      "But the problem is that busy becomes the only acceptable way to say no.",
      "You cannot always say,",
      "I need quiet time to think.",
      "That sounds suspiciously healthy.",
      "You cannot always say,",
      "This meeting is unnecessary.",
      "That is considered dangerous.",
      "So people say,",
      "I'm busy.",
      "And everyone understands.",
      "Because everyone else is also busy.",
      "Or pretending.",
      "Or both."
    ]
  },
  {
    id: "payoff",
    title: "Payoff",
    tone: "clear, reflective, deadpan at the end",
    mood: "satisfying realization",
    pace: "slower",
    energy: "medium-low",
    lines: [
      "So why does everyone pretend to be busy?",
      "Because modern life confuses activity with value.",
      "It rewards the person who looks available,",
      "responsive,",
      "and overloaded.",
      "Even when the real work needs focus,",
      "silence,",
      "and time.",
      "The problem is not that people are lazy.",
      "The problem is that looking busy became safer than looking thoughtful.",
      "And once a culture rewards busyness,",
      "everyone starts performing it.",
      "Students highlight notes instead of studying.",
      "Workers answer messages instead of solving problems.",
      "Creators organize ideas instead of making things.",
      "And everyone says they are busy,",
      "because saying,",
      "I am protecting my attention from meaningless noise,",
      "sounds too honest for a Tuesday.",
      "So maybe the goal is not to become less busy.",
      "The goal is to become more honest about what actually matters.",
      "Because if everything is urgent,",
      "nothing is important.",
      "And if your whole day is full of fake emergencies,",
      "congratulations.",
      "You are not lazy.",
      "You are just trapped inside a calendar with Wi-Fi."
    ]
  }
];

const emphasized = new Set([
  "weird", "modern", "less", "real", "work", "professional", "busy",
  "visible", "thinking", "status", "demand", "value", "urgent",
  "urgency", "notification", "emergency", "important", "progress",
  "productivity", "theater", "shield", "lazy", "thoughtful",
  "everything", "nothing", "wifi", "wi-fi", "attention"
]);

const deadpanLines = [
  "Or unemployed.",
  "That is a different problem.",
  "Which is technically not an emotion,",
  "Busy.",
  "Quietly.",
  "Untouched.",
  "Possibly blinking.",
  "That sounds suspiciously healthy.",
  "That is considered dangerous.",
  "Or both.",
  "congratulations.",
  "You are not lazy.",
  "You are just trapped inside a calendar with Wi-Fi."
];

const fillerPlan = new Map([
  ["This video is not about lazy people pretending to work.", "I mean,"],
  ["This is not always dishonest.", "To be fair,"],
  ["So maybe the goal is not to become less busy.", "Basically,"]
]);

function normalize(word) {
  return word.toLowerCase().replace(/[^a-z0-9-']/g, "");
}

function tokenize(line) {
  return line.match(/[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*/g) || [];
}

function lineMood(section, line) {
  if (deadpanLines.includes(line)) return "deadpan punchline";
  if (line.includes("?")) return "curious, lightly skeptical";
  if (line.includes("urgent") || line.includes("emergency")) return "mild fake panic";
  if (line.includes("thinking") || line.includes("progress")) return "clear and thoughtful";
  if (line.includes("lazy")) return "unfair but funny";
  return section.mood;
}

function lineTone(section, line) {
  if (deadpanLines.includes(line)) return "flat, dry, almost serious";
  if (line.includes("Everything") || line.includes("Sometimes")) return "list rhythm, controlled";
  if (line.includes("productivity theater")) return "definition, dry emphasis";
  if (line.includes("Wi-Fi")) return "final deadpan";
  return section.tone;
}

function durationForWord(word, pace, emphasis) {
  const len = word.length;
  let dur = 0.17 + Math.min(len, 11) * 0.018;
  if (pace.includes("slow")) dur += 0.035;
  if (pace.includes("list build")) dur -= 0.01;
  if (emphasis !== "none") dur += 0.045;
  if (len <= 2) dur -= 0.035;
  return Math.max(0.12, Number(dur.toFixed(3)));
}

function pauseAfterLine(line) {
  if (deadpanLines.includes(line)) return 0.55;
  if (line.endsWith("?")) return 0.45;
  if (line.endsWith(",")) return 0.22;
  if (line.length < 16) return 0.36;
  return 0.32;
}

function wordDelivery(word, line, section) {
  const n = normalize(word);
  const isEmphasis = emphasized.has(n);
  if (isEmphasis && ["busy", "urgent", "progress", "important", "work"].includes(n)) {
    return "slightly slower and clearer; match on-screen label if used";
  }
  if (deadpanLines.includes(line)) return "keep flat; do not overact";
  if (line.includes("Everything") || line.includes("Sometimes")) return "keep list rhythm clean";
  if (section.id === "payoff") return "clear, slightly slower, let the idea land";
  return "natural conversational delivery";
}

function addGap(timeline, seconds, reason, sectionId, afterLine) {
  timeline.push({
    type: "gap",
    estimatedStart: Number(currentTime.toFixed(3)),
    estimatedEnd: Number((currentTime + seconds).toFixed(3)),
    duration: Number(seconds.toFixed(3)),
    section: sectionId,
    afterLine,
    reason
  });
  currentTime += seconds;
}

function addFiller(timeline, filler, section, lineIndex) {
  const words = tokenize(filler);
  timeline.push({
    type: "gap",
    estimatedStart: Number(currentTime.toFixed(3)),
    estimatedEnd: Number((currentTime + 0.18).toFixed(3)),
    duration: 0.18,
    section: section.id,
    reason: "small breath before optional filler"
  });
  currentTime += 0.18;

  words.forEach((word, i) => {
    const duration = durationForWord(word, "normal", "light");
    const start = currentTime;
    const end = currentTime + duration;
    timeline.push({
      type: "filler",
      fillerKind: "optional_spoken_naturalizer",
      includeByDefault: false,
      section: section.id,
      lineIndex,
      fillerWordIndex: i,
      word,
      normalized: normalize(word),
      estimatedStart: Number(start.toFixed(3)),
      estimatedEnd: Number(end.toFixed(3)),
      duration: Number(duration.toFixed(3)),
      tone: "casual bridge, not sloppy",
      mood: "human clarification",
      pace: "quick but clear",
      energy: "low",
      emphasis: "light",
      delivery: "only include if TTS sounds too stiff without it"
    });
    currentTime = end;
  });

  addGap(timeline, 0.14, "gap after optional filler", section.id, filler);
}

let currentTime = 0;
let wordIndexGlobal = 0;
const timeline = [];
const wordsOnly = [];

sections.forEach((section, sectionIndex) => {
  if (sectionIndex > 0) addGap(timeline, 0.65, "section transition breath", section.id, null);

  section.lines.forEach((line, lineIndex) => {
    const filler = fillerPlan.get(line);
    if (filler) addFiller(timeline, filler, section, lineIndex);

    const words = tokenize(line);
    const mood = lineMood(section, line);
    const tone = lineTone(section, line);
    const pace = deadpanLines.includes(line) ? "slow-deadpan" : section.pace;

    if (lineIndex === 0 && sectionIndex === 0) addGap(timeline, 0.25, "opening breath", section.id, null);
    if (lineIndex > 0 && words.length > 0 && ["Or", "But", "Because", "So", "And"].includes(words[0])) {
      addGap(timeline, 0.16, "natural phrase pickup", section.id, section.lines[lineIndex - 1]);
    }

    words.forEach((word, wordIndexInLine) => {
      const normalized = normalize(word);
      const emphasis = emphasized.has(normalized)
        ? (["productivity", "theater", "urgent", "nothing", "important"].includes(normalized) ? "medium-high" : "medium")
        : "none";
      const duration = durationForWord(word, pace, emphasis);
      const start = currentTime;
      const end = currentTime + duration;
      const entry = {
        type: "word",
        globalWordIndex: wordIndexGlobal,
        section: section.id,
        sectionTitle: section.title,
        lineIndex,
        wordIndexInLine,
        word,
        normalized,
        estimatedStart: Number(start.toFixed(3)),
        estimatedEnd: Number(end.toFixed(3)),
        duration: Number(duration.toFixed(3)),
        tone,
        mood,
        pace,
        energy: section.energy,
        emphasis,
        stress: emphasis === "none" ? "normal" : "slightly stressed",
        pauseBefore: wordIndexInLine === 0 ? "line pickup only" : "none",
        pauseAfter: wordIndexInLine === words.length - 1 ? pauseAfterLine(line) : 0,
        delivery: wordDelivery(word, line, section),
        visualSyncHint: emphasis === "none" ? null : `optional on-screen emphasis for "${word}"`
      };
      timeline.push(entry);
      wordsOnly.push(entry);
      currentTime = end;
      wordIndexGlobal += 1;
    });

    addGap(timeline, pauseAfterLine(line), line.endsWith(",") ? "comma line pause" : "sentence or punchline pause", section.id, line);
  });
});

const output = {
  video: {
    title: "Why Everyone Pretends To Be Busy",
    slug: "why-everyone-pretends-to-be-busy",
    channel: "Why It Works",
    narrator: "David23",
    status: "pre-generation performance map",
    timingWarning: "estimatedStart and estimatedEnd are draft timing controls. Replace with forced-alignment timestamps after audio generation."
  },
  defaults: {
    tone: "clear, dry, simple, conversational",
    mood: "calm person explaining a ridiculous system without acting surprised",
    pace: "learner-friendly; do not rush punchlines",
    fillerPolicy: "Use gaps and breath first. Optional spoken fillers are disabled by default."
  },
  stats: {
    scriptWordCount: wordsOnly.length,
    timelineEventCount: timeline.length,
    estimatedRuntimeSeconds: Number(currentTime.toFixed(3)),
    optionalSpokenFillers: timeline.filter((event) => event.type === "filler").length
  },
  timeline,
  wordsOnly
};

fs.writeFileSync(outputPath, JSON.stringify(output, null, 2), "utf8");
console.log(outputPath);
console.log(`words=${wordsOnly.length}`);
console.log(`events=${timeline.length}`);
console.log(`estimatedRuntimeSeconds=${output.stats.estimatedRuntimeSeconds}`);
