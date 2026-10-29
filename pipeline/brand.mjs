// CHANNEL 16 brand asset renderer. usage: node brand.mjs <out_dir> [frame.jpg]
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve(path.dirname(new URL(import.meta.url).pathname), "node_modules");
const out = process.argv[2]; const FRAME = process.argv[3] ? `data:image/jpeg;base64,${fs.readFileSync(process.argv[3]).toString("base64")}` : "";
fs.mkdirSync(out, { recursive: true });

export const C = { abyss: "#06141F", deep: "#0E2A3A", foam: "#EAF2F0", signal: "#FF5B14", flare: "#FFC93C", sonar: "#4FD1C5", fog: "#8DA2AE" };
const F = (fam, file) => `@font-face{font-family:'${fam}';src:url(data:font/woff2;base64,${fs.readFileSync(`${NM}/@fontsource/${file}`).toString("base64")}) format("woff2")}`;
const CSS = [
  F("BC9", "barlow-condensed/files/barlow-condensed-latin-900-normal.woff2"),
  F("BC8", "barlow-condensed/files/barlow-condensed-latin-800-normal.woff2"),
  F("BC7", "barlow-condensed/files/barlow-condensed-latin-700-normal.woff2"),
  F("B6", "barlow/files/barlow-latin-600-normal.woff2"),
  F("JBM", "jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2"),
  F("JBM5", "jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2"),
  `*{margin:0;padding:0;box-sizing:border-box}body{background:transparent}
   .bc9{font-family:BC9;line-height:.86}.bc8{font-family:BC8}.mono{font-family:JBM;letter-spacing:.06em}
   .dot{display:inline-block;width:14px;height:14px;vertical-align:1px;border-radius:50%;background:${C.signal};box-shadow:0 0 .5em ${C.signal}}`,
].join("\n");

// Mark: "16" with three radio arcs. size in px.
export const mark = (s, bg = true) => {
  const R = 74, r = 50, cx = 100, cy = 100; // ring outer/inner radius
  const seg = (a0, a1, col) => { const p = (a, rad) => [cx + rad * Math.cos(a * Math.PI / 180), cy + rad * Math.sin(a * Math.PI / 180)];
    const [x1, y1] = p(a0, R), [x2, y2] = p(a1, R), [x3, y3] = p(a1, r), [x4, y4] = p(a0, r);
    return `<path d="M${x1} ${y1} A${R} ${R} 0 0 1 ${x2} ${y2} L${x3} ${y3} A${r} ${r} 0 0 0 ${x4} ${y4} Z" fill="${col}"/>`; };
  let ring = ""; for (let i = 0; i < 4; i++) ring += seg(-90 + 45 + i * 90 - 45 + 2, -90 + 45 + i * 90 + 45 - 2, i % 2 ? C.foam : C.signal);
  return `<svg width="${s}" height="${s}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
 ${bg ? `<rect width="200" height="200" rx="46" fill="${C.abyss}"/>` : ""}
 ${ring}
 <text x="100" y="125" text-anchor="middle" font-family="BC9" font-size="72" fill="${C.foam}" letter-spacing="-1">16</text>
</svg>`; };

const wordmark = (h) => `<div style="display:flex;align-items:center;gap:${h * 0.28}px">
  ${mark(h)}<div><div class="bc9" style="font-size:${h * 0.62}px;color:${C.foam};letter-spacing:.04em">CHANNEL <span style="color:${C.signal}">16</span></div>
  <div class="mono" style="font-size:${h * 0.15}px;color:${C.sonar};margin-top:${h * 0.08}px">156.800 MHz · REAL RESCUES</div></div></div>`;

const pages = {
  avatar_800: [800, 800, () => `<div style="width:800px;height:800px">${mark(800)}</div>`],
  watermark_150: [150, 150, () => `<div style="width:150px;height:150px;opacity:.92">${mark(150)}</div>`],
  banner_2560: [2560, 1440, () => `<div style="width:2560px;height:1440px;background:${C.abyss};position:relative;overflow:hidden">
     ${FRAME ? `<div style="position:absolute;inset:0;background:url(${FRAME}) center/cover;opacity:.38;filter:saturate(.7)"></div>` : ""}
     <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(6,20,31,.35),${C.abyss} 72%)"></div>
     ${sonar(1280, 720, 900, .10)}
     <div style="position:absolute;left:507px;top:509px;width:1546px;height:423px;display:flex;align-items:center;justify-content:space-between">
       ${wordmark(250)}
       <div class="mono" style="font-size:30px;color:${C.foam};text-align:right;line-height:1.7">
         <div><span class="dot"></span>&nbsp; NEW RESCUES DAILY</div><div style="color:${C.fog}">LONG CASES · SHORTS</div></div>
     </div></div>`],
  palette: [1600, 900, () => `<div style="width:1600px;height:900px;background:${C.abyss};padding:70px;color:${C.foam}">
     ${wordmark(170)}
     <div style="display:flex;gap:22px;margin-top:70px">${Object.entries(C).map(([k, v]) => `<div style="flex:1">
       <div style="height:170px;border-radius:18px;background:${v};border:2px solid ${C.deep}"></div>
       <div class="bc8" style="font-size:38px;margin-top:14px;text-transform:uppercase">${k}</div><div class="mono" style="font-size:22px;color:${C.fog}">${v}</div></div>`).join("")}</div>
     <div style="display:flex;gap:60px;margin-top:60px;align-items:baseline">
       <div class="bc9" style="font-size:96px">BARLOW CONDENSED 900</div><div style="font-family:B6;font-size:40px;color:${C.fog}">Barlow 600 body</div>
       <div class="mono" style="font-size:34px;color:${C.sonar}">JETBRAINS MONO</div></div></div>`],
  lower_third: [1920, 1080, () => `<div style="width:1920px;height:1080px;position:relative;background:${FRAME ? `url(${FRAME}) center/cover` : C.deep}">
     ${hud()}
     <div style="position:absolute;left:96px;bottom:150px;display:flex;align-items:stretch">
       <div style="width:10px;background:${C.signal}"></div>
       <div style="background:rgba(6,20,31,.86);padding:18px 30px 16px">
         <div class="mono" style="font-size:24px;color:${C.sonar}">AIR STATION SITKA · MH-60 JAYHAWK</div>
         <div class="bc9" style="font-size:66px;color:${C.foam};margin-top:6px">LIFE RAFT TAKING ON WATER</div></div></div></div>`],
};
// thin sonar rings (decor)
function sonar(cx, cy, r, op) {
  return `<svg style="position:absolute;left:0;top:0" width="2560" height="1440">${[1, .75, .5, .25].map((k) =>
    `<circle cx="${cx}" cy="${cy}" r="${r * k}" fill="none" stroke="${C.sonar}" stroke-opacity="${op}" stroke-width="3"/>`).join("")}</svg>`;
}
// radio HUD used in every video: top-left channel readout, top-right UTC clock + position
export function hud(t = "03:12:40", pos = "57°29'N 134°36'W") {
  return `<div style="position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:16px">
     ${mark(78)}<div class="mono" style="font-size:24px;color:${C.foam};line-height:1.35">
     <div><span class="dot"></span>&nbsp; CH 16 · DISTRESS</div><div style="color:${C.sonar}">156.800 MHz</div></div></div>
   <div class="mono" style="position:absolute;right:64px;top:58px;font-size:24px;color:${C.foam};text-align:right;line-height:1.35;text-shadow:0 2px 8px #000">
     <div>${t} AKDT</div><div style="color:${C.sonar}">${pos}</div></div>`;
}

const b = await chromium.launch(); const pg = await b.newPage();
for (const [name, [w, h, fn]] of Object.entries(pages)) {
  await pg.setViewportSize({ width: w, height: h });
  await pg.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${fn()}</body></html>`);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(150);
  await pg.screenshot({ path: path.join(out, `${name}.png`), omitBackground: true });
  console.log(name);
}
await b.close();
