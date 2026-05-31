import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectDir = path.resolve(__dirname, "..");
const compositionsDir = path.join(projectDir, "compositions");
const gap = 0.002;

const num = (value) => {
  const fixed = Number(value.toFixed(3));
  return Object.is(fixed, -0) ? 0 : fixed;
};

for (const name of fs.readdirSync(compositionsDir)) {
  if (!name.endsWith(".html")) continue;

  const file = path.join(compositionsDir, name);
  let html = fs.readFileSync(file, "utf8");
  const sectionRegex = /<section\b[^>]*\bdata-start="([0-9.]+)"[^>]*\bdata-duration="([0-9.]+)"[^>]*>/g;
  const sections = [...html.matchAll(sectionRegex)].map((match) => ({
    tag: match[0],
    start: Number(match[1]),
    duration: Number(match[2]),
  }));

  let changed = false;

  for (let index = 0; index < sections.length - 1; index += 1) {
    const section = sections[index];
    const next = sections[index + 1];
    const maxDuration = Math.max(0, next.start - section.start - gap);

    if (section.duration > maxDuration) {
      const newDuration = num(maxDuration);
      const newTag = section.tag.replace(/\bdata-duration="[0-9.]+"/, `data-duration="${newDuration}"`);
      html = html.replace(section.tag, newTag);
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(file, html);
  }
}
