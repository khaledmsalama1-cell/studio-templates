#!/usr/bin/env node
// Validate templates/**/*.json, then write index.json (what the Studio fetches) and the README catalogue.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const FORMATS = { reel: "video", promo: "video", landscape: "video", carousel: "image", post: "image", square: "image", story: "image" };
const SCENES = new Set(["hook", "point", "list", "stat", "quote", "media", "cta"]);
const PLACEHOLDERS = new Set(["brand", "product", "cta", "topic", "audience", "handle"]);

const errors = [];
const templates = [];
const ids = new Set();
for (const dir of fs.readdirSync(path.join(root, "templates")).sort()) {
  for (const file of fs.readdirSync(path.join(root, "templates", dir)).filter((f) => f.endsWith(".json")).sort()) {
    const where = `templates/${dir}/${file}`;
    const bad = (m) => errors.push(`${where}: ${m}`);
    let t;
    try {
      t = JSON.parse(fs.readFileSync(path.join(root, "templates", dir, file), "utf8"));
    } catch (e) {
      bad(`invalid JSON (${e.message})`);
      continue;
    }
    if (!/^[a-z0-9][a-z0-9-]*$/.test(t.id || "") || `${t.id}.json` !== file) bad("id must be kebab-case and match the file name");
    if (ids.has(t.id)) bad("duplicate id");
    ids.add(t.id);
    for (const k of ["name", "description", "category"]) if (!t[k]) bad(`missing ${k}`);
    if (t.kind === "external") {
      if (!/^https:\/\//.test(t.url || "")) bad("external templates need an https url");
      if (dir !== "external") bad("external templates live in templates/external");
    } else if (t.kind === "studio") {
      if (!FORMATS[t.format] || dir !== t.format) bad(`format must be one of ${Object.keys(FORMATS).join(", ")} and match the folder`);
      if (!Array.isArray(t.scenes) || !t.scenes.length) bad("needs scenes");
      (t.scenes || []).forEach((s, i) => {
        const at = `scene ${i + 1}`;
        if (!SCENES.has(s.type)) bad(`${at}: unknown type ${s.type}`);
        if (s.type === "stat" && !s.value) bad(`${at}: stat needs value`);
        if (s.type === "list" && !s.items?.length) bad(`${at}: list needs items`);
        if (s.type !== "media" && !s.text) bad(`${at}: needs text`);
        if (FORMATS[t.format] === "video" && !s.say) bad(`${at}: video scenes need a say line`);
        for (const m of JSON.stringify(s).matchAll(/\{\{(\w+)\}\}/g)) if (!PLACEHOLDERS.has(m[1])) bad(`${at}: unknown placeholder {{${m[1]}}}`);
      });
    } else bad("kind must be studio or external");
    templates.push(t);
  }
}
if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

const studio = templates.filter((t) => t.kind === "studio");
const external = templates.filter((t) => t.kind === "external");
fs.writeFileSync(path.join(root, "index.json"), JSON.stringify({ version: 1, generatedAt: new Date().toISOString(), formats: FORMATS, templates }, null, 1) + "\n");

let md = fs.readFileSync(path.join(root, "README.header.md"), "utf8").replace("{{COUNT}}", templates.length).replace("{{STUDIO}}", studio.length).replace("{{EXTERNAL}}", external.length);
const label = { reel: "Reels (9:16 video)", promo: "Product promos (9:16 video)", landscape: "Landscape video (16:9)", carousel: "Carousels (4:5 slides)", post: "Feed posts (4:5)", square: "Square posts (1:1)", story: "Stories (9:16 frames)" };
for (const f of Object.keys(FORMATS)) {
  const list = studio.filter((t) => t.format === f);
  if (!list.length) continue;
  md += `\n### ${label[f]} — ${list.length}\n\n| Template | What it's for | Category | Scenes |\n|---|---|---|---|\n`;
  for (const t of list) md += `| [${t.name}](templates/${f}/${t.id}.json) | ${t.description} | ${t.category} | ${t.scenes.length} |\n`;
}
md += `\n### External starters — ${external.length}\n\n| Starter | Engine | What it is |\n|---|---|---|\n`;
for (const t of external) md += `| [${t.name}](${t.url}) | ${t.engine} | ${t.description} |\n`;
fs.writeFileSync(path.join(root, "README.md"), md);
console.log(`✔ ${studio.length} studio templates + ${external.length} external starters valid → index.json, README.md`);
