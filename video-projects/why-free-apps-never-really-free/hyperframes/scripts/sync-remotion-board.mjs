import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectDir = path.resolve(__dirname, "..");
const workspaceDir = path.resolve(projectDir, "..", "..", "..");
const remotionFile = path.join(
  workspaceDir,
  "remotion-studio",
  "src",
  "FreeAppsFullBoardVideo.tsx",
);
const compositionsDir = path.join(projectDir, "compositions");
const partPreviewDir = path.join(projectDir, "part-previews");

const theme = {
  paper: "#FFFDF7",
  ink: "#101827",
  red: "#E5162E",
  blue: "#2057D6",
  yellow: "#F2C14E",
  teal: "#8DD6DF",
  green: "#95D5B2",
  soft: "#F7F1E8",
};

const sceneAudio = [
  { id: "free-gifts", src: "free-gifts.mp3", duration: 23.17 },
  { id: "pricing-reframe", src: "pricing-reframe.mp3", duration: 43.65 },
  { id: "attention-ads", src: "attention-ads.mp3", duration: 38.77 },
  { id: "behavior-habit", src: "behavior-habit.mp3", duration: 28.24 },
  { id: "freemium-pain", src: "freemium-pain.mp3", duration: 21.21 },
  { id: "lock-in", src: "lock-in.mp3", duration: 21.26 },
  { id: "label-stack", src: "label-stack.mp3", duration: 22.39 },
  { id: "hidden-checkout", src: "hidden-checkout.mp3", duration: 41.22 },
];

const audioTimeline = sceneAudio.reduce(
  (acc, audio) => {
    const from = audio.startAt ?? acc.cursor;
    acc.items.push({ ...audio, from, to: from + audio.duration });
    acc.cursor += audio.duration;
    return acc;
  },
  { cursor: 0, items: [] },
).items;

const fullDuration = audioTimeline[audioTimeline.length - 1].to;

const partCompositions = [
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
  { id: "Part12PayoffEnding", slug: "part-12-payoff-ending", start: 224, end: fullDuration },
];

const esc = (value) =>
  String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");

const num = (value) => Number(value.toFixed(4));
const local = (global, start) => num(global - start);
const durationBetween = (start, end) => Math.max(0, num(end - start - 0.001));
const attr = (name, value) => (value === undefined || value === null ? "" : ` ${name}="${esc(value)}"`);
const underlineAfterVoiceDelay = 0.18;
const style = (entries) =>
  entries
    .filter(([, value]) => value !== undefined && value !== null)
    .map(([key, value]) => `${key}:${value}`)
    .join(";");

function extractBoards() {
  const source = fs.readFileSync(remotionFile, "utf8");
  const marker = "const boards: BoardSpec[] = ";
  const start = source.indexOf(marker);
  const end = source.indexOf("\n];\n\nconst Board", start);

  if (start === -1 || end === -1) {
    throw new Error("Could not find Remotion board array.");
  }

  const body = source.slice(start + marker.length, end + 2);
  return Function("theme", `return (${body});`)(theme);
}

function visibleCard(card) {
  const { appearAt, popIn, instantAppear, ...rest } = card;
  return rest;
}

function expandRoutineLoopBoards(board) {
  if (board.id !== "routine-loop") return [board];

  const cards = board.cards ?? [];
  const cueTimes = [board.at, ...cards.map((card) => card.appearAt).filter(Boolean)];

  return cueTimes.map((cue, index) => ({
    ...board,
    id: index === 0 ? board.id : `${board.id}-step-${index}`,
    at: cue,
    cards: cards
      .filter((card) => (card.appearAt ?? board.at) <= cue)
      .map(visibleCard),
  }));
}

function tuneVoiceTimedReveals(board) {
  if (board.id === "pay-options") {
    return {
      ...board,
      subtitleAppearAt: 144.7,
    };
  }

  return board;
}

const boards = extractBoards().map(tuneVoiceTimedReveals).flatMap(expandRoutineLoopBoards);

function poseFile(pose) {
  const map = {
    "holding-phone": "wit-pose-phone-bill-panic.png",
    "pointing-right": "wit-pose-pointing-right.png",
    "pointing-left": "wit-pose-pointing-left.png",
    suspicious: "wit-pose-suspicious-detective.png",
    shocked: "wit-pose-shocked.png",
    confused: "wit-pose-confused.png",
    deadpan: "wit-pose-smug-side-eye.png",
    talking: "wit-pose-talking.png",
    receipt: "wit-pose-receipt-evidence.png",
    panic: "wit-pose-money-panic.png",
    thinking: "wit-pose-thinking.png",
    defeated: "wit-pose-tiny-defeated.png",
    neutral: "wit-pose-neutral-default.png",
  };

  return map[pose] ?? "wit-pose-neutral-default.png";
}

function renderWit(wit, assetPrefix) {
  if (!wit) return "";
  const height =
    wit.pose === "receipt"
      ? wit.width * 1.44
      : wit.pose === "suspicious"
        ? wit.width * 1.38
        : wit.width * 1.3;
  const top = wit.pose === "receipt" ? 26 : wit.pose === "suspicious" ? 18 : 0;
  const transform = wit.flipX ? "scaleX(-1)" : undefined;

  return `<div class="wit-wrap" data-layout-allow-overflow style="${style([
    ["left", `${wit.left}px`],
    ["top", `${wit.top}px`],
    ["width", `${wit.width}px`],
    ["height", `${height}px`],
  ])}"><img class="wit-img" src="${assetPrefix}assets/wit/poses/core-24/${poseFile(wit.pose)}" alt="WIT" style="${style([
    ["top", `${top}px`],
    ["width", `${wit.width}px`],
    ["transform", transform],
  ])}" /></div>`;
}

function renderTextBlock(kind, spec) {
  if (!spec.text) return "";
  const isSubtitle = kind === "subtitle";
  const left = spec.left ?? (isSubtitle ? 940 : 260);
  const top = spec.top ?? (isSubtitle ? 300 : 180);
  const size = spec.size ?? (isSubtitle ? 54 : 64);
  const width = spec.width ?? (isSubtitle ? 660 : 720);
  const lineHeight = spec.lineHeight ?? 1.05;
  const align = spec.align ?? "left";
  const color = spec.color ?? theme.ink;
  const appearAt = spec.appearAt ?? 0;
  const delayed = appearAt > spec.partStart;
  const cue = delayed ? local(appearAt, spec.partStart) : undefined;
  const classes = ["text-block", kind];
  if (delayed) classes.push("delayed-text");
  if (spec.wiggle) classes.push("wiggle");

  return `<div class="${classes.join(" ")}"${attr("data-appear", cue)}${attr("data-wiggle-start", spec.wiggleStartAt)} style="${style([
    ["left", `${left}px`],
    ["top", `${top}px`],
    ["width", `${width}px`],
    ["color", color],
    ["font-size", `${size}px`],
    ["line-height", lineHeight],
    ["text-align", align],
    ["opacity", delayed ? 0 : undefined],
  ])}">${esc(spec.text)}</div>`;
}

function renderCard(card, index, partStart) {
  const color = card.color ?? "#FFFFFF";
  const rotate = card.rotate ?? 0;
  const fontSize = card.fontSize ?? 48;
  const appearAt = card.appearAt ?? 0;
  const delayed = appearAt > partStart;
  const cue = delayed ? local(appearAt, partStart) : undefined;
  const classes = ["label-card"];
  if (delayed) classes.push("delayed-card");
  if (card.wiggle) classes.push("wiggle");

  return `<div id="card-${index}" class="${classes.join(" ")}"${attr("data-appear", cue)}${attr("data-rotate", rotate)}${attr("data-instant", card.instantAppear ? "true" : undefined)}${attr("data-pop", card.popIn ? "true" : undefined)} style="${style([
    ["left", `${card.left}px`],
    ["top", `${card.top}px`],
    ["width", `${card.width}px`],
    ["height", `${card.height}px`],
    ["background-color", color],
    ["font-size", `${fontSize}px`],
    ["transform", delayed ? undefined : `rotate(${rotate}deg) scale(1)`],
    ["opacity", delayed ? 0 : 1],
  ])}">${esc(card.text)}</div>`;
}

function renderCross(cross) {
  if (!cross) return "";
  return `<div class="red-cross" style="${style([
    ["left", `${cross.left}px`],
    ["top", `${cross.top}px`],
    ["width", `${cross.width}px`],
    ["height", `${cross.height}px`],
  ])}"><div class="cross-a"></div><div class="cross-b"></div></div>`;
}

function renderUnderline(underline, index, partStart) {
  if (!underline) return "";
  const hasStartAt = underline.startAt !== undefined && underline.startAt !== null;
  const startAt = underline.startAt ?? 0;
  const delayed = hasStartAt && startAt >= partStart;
  const cue = delayed ? local(startAt + underlineAfterVoiceDelay, partStart) : undefined;
  const drawDuration = underline.drawDuration ?? (delayed ? 0.18 : undefined);
  return `<div id="underline-${index}" class="underline${delayed ? " delayed-underline" : ""}"${attr("data-appear", cue)}${attr("data-draw-duration", drawDuration)}${attr("data-snap", underline.snapVisible ? "true" : undefined)} style="${style([
    ["left", `${underline.left}px`],
    ["top", `${underline.top}px`],
    ["width", `${underline.width}px`],
    ["background-color", underline.color ?? theme.red],
    ["transform", delayed ? "rotate(-1.5deg) scaleX(0)" : "rotate(-1.5deg) scaleX(1)"],
  ])}"></div>`;
}

function renderArrow(arrow) {
  if (!arrow) return "";
  return `<div class="arrow" style="${style([
    ["left", `${arrow.left}px`],
    ["top", `${arrow.top}px`],
    ["width", `${arrow.width}px`],
    ["transform", `rotate(${arrow.rotate ?? 0}deg)`],
  ])}"><div class="arrow-head"></div></div>`;
}

function renderSmashText(smash, partStart) {
  if (!smash) return "";
  const cue = local(smash.startAt, partStart);
  return `<div class="smash-text" data-appear="${cue}" data-rotate="${smash.rotate ?? 0}" style="${style([
    ["left", `${smash.left}px`],
    ["top", `${smash.top}px`],
    ["color", smash.color ?? theme.red],
    ["font-size", `${smash.size}px`],
    ["opacity", 0],
  ])}">${esc(smash.text)}</div>`;
}

function renderPhone(phone) {
  if (!phone) return "";
  const width = phone.width;
  const height = width * 1.5;
  const badge = phone.badge ?? "FREE";
  const items = phone.items ?? ["video", "maps", "messaging"];

  const itemHtml = items
    .map((label, index) => {
      const fontSize = label.length > 10 ? width * 0.075 : width * 0.095;
      return `<div class="phone-item" style="${style([
        ["left", `${width * 0.19}px`],
        ["top", `${width * 0.66 + index * width * 0.18}px`],
        ["width", `${width * 0.64}px`],
        ["font-size", `${fontSize}px`],
      ])}">${esc(label)}</div>`;
    })
    .join("");

  const invoice = phone.invoice
    ? `<div class="phone-invoice" style="${style([
        ["right", `${width * 0.07}px`],
        ["bottom", `${width * 0.16}px`],
        ["width", `${width * 0.58}px`],
        ["height", `${width * 0.42}px`],
        ["font-size", `${width * 0.068}px`],
      ])}">invoice<div>later</div></div>`
    : "";

  return `<div class="phone" style="${style([
    ["left", `${phone.left}px`],
    ["top", `${phone.top}px`],
    ["width", `${width}px`],
    ["height", `${height}px`],
    ["border-radius", `${width * 0.13}px`],
  ])}"><div class="phone-speaker" style="${style([
    ["width", `${width * 0.24}px`],
  ])}"></div><div class="phone-badge" style="${style([
    ["left", `${width * 0.16}px`],
    ["top", `${width * 0.24}px`],
    ["width", `${width * 0.68}px`],
    ["height", `${width * 0.3}px`],
    ["font-size", `${width * 0.18}px`],
  ])}">${esc(badge)}</div>${itemHtml}${phone.crossed ? renderCross({ left: width * 0.14, top: width * 0.23, width: width * 0.72, height: width * 0.33 }) : ""}${invoice}</div>`;
}

function renderBoard(board, index, partStart, partEnd, assetPrefix) {
  const next = boards[index + 1]?.at ?? fullDuration;
  const start = Math.max(board.at, partStart);
  const end = Math.min(next, partEnd);
  const duration = durationBetween(start, end);

  if (duration <= 0) return "";

  const content = [
    board.endCard
      ? `<div class="end-card-frame"></div>`
      : "",
    renderPhone(board.phone),
    renderWit(board.wit, assetPrefix),
    board.title
      ? renderTextBlock("title", {
          text: board.title,
          left: board.titleLeft ?? 260,
          top: board.titleTop ?? 180,
          size: board.titleSize ?? 64,
          width: board.titleWidth ?? 720,
          color: board.titleColor,
          align: board.titleAlign,
          appearAt: board.titleAppearAt,
          partStart,
        })
      : "",
    board.subtitle
      ? renderTextBlock("subtitle", {
          text: board.subtitle,
          left: board.subtitleLeft ?? 940,
          top: board.subtitleTop ?? 300,
          size: board.subtitleSize ?? 54,
          width: board.subtitleWidth ?? 660,
          color: board.subtitleColor,
          align: board.subtitleAlign,
          lineHeight: board.subtitleLineHeight,
          appearAt: board.subtitleAppearAt,
          wiggle: board.subtitleWiggle,
          wiggleStartAt: local(board.at, partStart),
          partStart,
        })
      : "",
    ...(board.cards ?? []).map((card, cardIndex) => renderCard(card, cardIndex, partStart)),
    renderCross(board.cross),
    renderUnderline(board.underline, 0, partStart),
    ...(board.underlines ?? []).map((underline, underlineIndex) =>
      renderUnderline(underline, underlineIndex + 1, partStart),
    ),
    renderArrow(board.arrow),
    board.accentText
      ? renderTextBlock("accent-text", {
          text: board.accentText.text,
          left: board.accentText.left,
          top: board.accentText.top,
          size: board.accentText.size,
          color: board.accentText.color,
          width: board.accentText.width,
          appearAt: board.accentText.appearAt,
          partStart,
        })
      : "",
    renderSmashText(board.smashText, partStart),
  ].join("");

  return `<section id="${esc(board.id)}" class="board-clip clip" data-start="${local(start, partStart)}" data-duration="${duration}" data-track-index="1">${content}</section>`;
}

function renderAudio(partStart, partEnd, assetPrefix) {
  return audioTimeline
    .filter((audio) => audio.to > partStart && audio.from < partEnd)
    .map((audio) => {
      const overlapStart = Math.max(audio.from, partStart);
      const overlapEnd = Math.min(audio.to, partEnd);
      const mediaStart = num(overlapStart - audio.from);
      const playbackRate = audio.id === "behavior-habit" ? "1" : undefined;
      return `<audio${attr("data-playback-rate", playbackRate)} id="audio-${audio.id}" src="${assetPrefix}assets/voiceover/${audio.src}" data-start="${local(overlapStart, partStart)}" data-duration="${durationBetween(overlapStart, overlapEnd)}" data-media-start="${mediaStart}" data-track-index="0" data-volume="1"></audio>`;
    })
    .join("\n      ");
}

function baseCss() {
  return `
      :root {
        --paper: ${theme.paper};
        --ink: ${theme.ink};
        --red: ${theme.red};
        --blue: ${theme.blue};
        --yellow: ${theme.yellow};
        --teal: ${theme.teal};
        --green: ${theme.green};
        --soft: ${theme.soft};
      }
      * { box-sizing: border-box; }
      html, body {
        margin: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: var(--paper);
        color: var(--ink);
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
      }
      [data-composition-id] {
        position: relative;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background-color: var(--paper);
        background-image:
          linear-gradient(90deg, rgba(16, 24, 39, 0.03) 1px, rgba(255, 253, 247, 0) 1px),
          linear-gradient(0deg, rgba(16, 24, 39, 0.03) 1px, rgba(255, 253, 247, 0) 1px);
        background-size: 72px 72px;
      }
      .board-clip {
        position: absolute;
        inset: 0;
        overflow: hidden;
      }
      .text-block {
        position: absolute;
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        font-weight: 800;
        white-space: pre-line;
        transform-origin: center;
      }
      .delayed-text {
        opacity: 0;
      }
      .label-card {
        position: absolute;
        border: 6px solid var(--ink);
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        line-height: 1;
        font-weight: 800;
        white-space: pre-line;
        box-shadow: 0 13px 0 rgba(16, 24, 39, 0.13);
        transform-origin: center;
      }
      .wit-wrap {
        position: absolute;
      }
      .wit-img {
        position: absolute;
        left: 0;
        height: auto;
        filter: drop-shadow(0 18px 22px rgba(16, 24, 39, 0.14));
      }
      .phone {
        position: absolute;
        border: 8px solid var(--ink);
        background: #ffffff;
        box-shadow: 0 22px 0 rgba(16, 24, 39, 0.14);
      }
      .phone-speaker {
        height: 18px;
        border-radius: 999px;
        background: var(--ink);
        margin: 24px auto 0;
      }
      .phone-badge {
        position: absolute;
        border: 5px solid var(--ink);
        border-radius: 24px;
        background: var(--yellow);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        font-weight: 800;
      }
      .phone-item {
        position: absolute;
        height: 48px;
        border-bottom: 4px solid var(--ink);
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        font-weight: 800;
      }
      .phone-invoice {
        position: absolute;
        border: 5px solid var(--ink);
        border-radius: 12px;
        background: #ffffff;
        transform: rotate(4deg);
        padding: 18px;
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        font-weight: 800;
        box-shadow: 0 14px 0 rgba(16, 24, 39, 0.12);
      }
      .phone-invoice div {
        margin-top: 18px;
        padding-top: 12px;
        border-top: 4px dashed var(--ink);
        color: var(--red);
      }
      .red-cross {
        position: absolute;
      }
      .cross-a, .cross-b {
        position: absolute;
        left: 0;
        top: calc(50% - 8px);
        width: 100%;
        height: 14px;
        border-radius: 999px;
        background: var(--red);
        transform-origin: center;
      }
      .cross-a { transform: rotate(-9deg); }
      .cross-b { transform: rotate(8deg); }
      .underline {
        position: absolute;
        height: 9px;
        border-radius: 999px;
        transform-origin: left center;
      }
      .arrow {
        position: absolute;
        height: 12px;
        border-radius: 999px;
        background: var(--ink);
        transform-origin: left center;
      }
      .arrow-head {
        position: absolute;
        right: -3px;
        top: -14px;
        width: 0;
        height: 0;
        border-top: 20px solid rgba(255, 253, 247, 0);
        border-bottom: 20px solid rgba(255, 253, 247, 0);
        border-left: 34px solid var(--ink);
      }
      .smash-text {
        position: absolute;
        font-family: "Ink Free", "Lucida Handwriting", "Segoe Print", "Comic Sans MS", cursive;
        line-height: 1;
        font-weight: 800;
        transform-origin: center;
        filter: drop-shadow(0 10px 0 rgba(16, 24, 39, 0.12));
      }
      .end-card-frame {
        position: absolute;
        inset: 74px;
        border: 8px solid var(--ink);
        border-radius: 24px;
        opacity: 0.08;
      }
    `;
}

function timelineScript(compositionId, duration) {
  return `
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });

      document.querySelectorAll(".delayed-card").forEach((el) => {
        const appear = Number(el.dataset.appear || 0);
        const rotate = Number(el.dataset.rotate || 0);
        const instant = el.dataset.instant === "true";
        const pop = el.dataset.pop === "true";
        const startScale = instant ? 0.86 : 0.2;
        tl.set(el, { opacity: instant ? 1 : 0, scale: startScale, rotation: rotate }, appear);
        if (pop) {
          tl.to(el, { opacity: 1, scale: 1.08, duration: 0.13, ease: "power4.out", overwrite: "auto" }, appear);
          tl.to(el, { scale: 1, duration: 0.2, ease: "power2.out", overwrite: "auto" }, appear + 0.13);
        } else {
          tl.to(el, { opacity: 1, scale: 1, duration: 0.1, ease: "power2.out", overwrite: "auto" }, appear);
        }
      });

      document.querySelectorAll(".delayed-text").forEach((el) => {
        const appear = Number(el.dataset.appear || 0);
        tl.set(el, { opacity: 0, y: 8 }, 0);
        tl.to(el, { opacity: 1, y: 0, duration: 0.18, ease: "power2.out", overwrite: "auto" }, appear);
      });

      document.querySelectorAll(".delayed-underline").forEach((el) => {
        const appear = Number(el.dataset.appear || 0);
        const draw = Number(el.dataset.drawDuration || 0.16);
        const snap = el.dataset.snap === "true" ? 0.18 : 0;
        tl.set(el, { scaleX: snap }, appear);
        tl.to(el, { scaleX: 1, duration: draw, ease: "power2.out" }, appear);
      });

      document.querySelectorAll(".smash-text").forEach((el) => {
        const appear = Number(el.dataset.appear || 0);
        const rotate = Number(el.dataset.rotate || 0);
        tl.set(el, { opacity: 0, scale: 0.2, rotation: rotate }, 0);
        tl.to(el, { opacity: 1, scale: 2.35, duration: 0.07, ease: "power4.out", overwrite: "auto" }, appear);
        tl.to(el, { scale: 0.9, duration: 0.17, ease: "power2.inOut", overwrite: "auto" }, appear + 0.07);
        tl.to(el, { scale: 1, duration: 0.13, ease: "power2.out", overwrite: "auto" }, appear + 0.24);
      });

      document.querySelectorAll(".wiggle").forEach((el) => {
        const start = Number(el.dataset.wiggleStart || el.dataset.appear || 0);
        const cycles = Math.max(0, Math.ceil((${duration} - start) / 0.8) - 1);
        if (cycles > 0) {
          const baseRotation = Number(el.dataset.rotate || 0);
          tl.to(el, {
            rotation: baseRotation + 0.8,
            scale: 1.006,
            duration: 0.4,
            repeat: cycles,
            yoyo: true,
            ease: "sine.inOut",
            overwrite: "auto",
          }, start);
        }
      });

      window.__timelines["${compositionId}"] = tl;
    `;
}

function renderPart(part) {
  const duration = durationBetween(part.start, part.end);
  const boardHtml = boards
    .map((board, index) => renderBoard(board, index, part.start, part.end, "../"))
    .join("\n        ");

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>${esc(part.id)}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>${baseCss()}</style>
  </head>
  <body>
    <div id="root" data-composition-id="${part.id}" data-start="0" data-duration="${duration}" data-width="1920" data-height="1080">
      ${boardHtml}
    </div>
    <script>
${timelineScript(part.id, duration)}
    </script>
  </body>
</html>
`;
}

function renderPartPreview(part) {
  const duration = durationBetween(part.start, part.end);
  const audioHtml = renderAudio(part.start, part.end, "../");

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>${esc(part.id)} Audio Preview</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>${baseCss()}</style>
  </head>
  <body>
    <div id="root" data-composition-id="${part.id}AudioPreview" data-start="0" data-duration="${duration}" data-width="1920" data-height="1080">
      ${audioHtml}
      <div id="${part.slug}" class="clip" data-composition-id="${part.id}" data-composition-src="../compositions/${part.slug}.html" data-start="0" data-duration="${duration}" data-track-index="1"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["${part.id}AudioPreview"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
`;
}

function renderIndex() {
  const partsHtml = partCompositions
    .map(
      (part) =>
        `<div id="${part.slug}" class="clip" data-composition-id="${part.id}" data-composition-src="compositions/${part.slug}.html" data-start="${part.start}" data-duration="${durationBetween(part.start, part.end)}" data-track-index="1"></div>`,
    )
    .join("\n      ");
  const audioHtml = renderAudio(0, fullDuration, "");

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>Why Free Apps Are Never Really Free - Full Rough Cut</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>${baseCss()}</style>
  </head>
  <body>
    <div id="root" data-composition-id="FullVideo" data-start="0" data-duration="${durationBetween(0, fullDuration)}" data-width="1920" data-height="1080">
      ${audioHtml}
      ${partsHtml}
    </div>
    <script>
${timelineScript("FullVideo", fullDuration)}
    </script>
  </body>
</html>
`;
}

fs.mkdirSync(compositionsDir, { recursive: true });
fs.mkdirSync(partPreviewDir, { recursive: true });

for (const part of partCompositions) {
  fs.writeFileSync(path.join(compositionsDir, `${part.slug}.html`), renderPart(part));
  fs.writeFileSync(path.join(partPreviewDir, `${part.slug}.html`), renderPartPreview(part));
}

fs.writeFileSync(path.join(projectDir, "index.html"), renderIndex());

console.log(
  JSON.stringify(
    {
      generated: {
        full: path.join(projectDir, "index.html"),
        parts: partCompositions.length,
        boards: boards.length,
        duration: num(fullDuration),
      },
    },
    null,
    2,
  ),
);
