// Renders brand assets: avatar (800x800), banner (2560x1440), watermark (150x150) to ./brand/
import { chromium } from "playwright";
import fs from "fs";
import { PAL, C, fontCSS, rng, star5, bowlMoon, bunny, sky, hills, cloud, wordmark } from "./art.mjs";

fs.mkdirSync("brand", { recursive: true });
const css = fontCSS();
const page = (W, H, body) => `<!doctype html><html><head><style>${css} html,body{margin:0;background:#000}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${body}</svg></body></html>`;

function starfield(W, H, n, seed, maxY = 1) {
  const r = rng(seed); let s = "";
  for (let i = 0; i < n; i++) {
    const x = r() * W, y = r() * H * maxY, k = r();
    s += k > 0.88 ? star5(x, y, 4 + r() * 5, C.star, 0.9) : `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(0.8 + r() * 1.8).toFixed(1)}" fill="#fff" opacity="${(0.35 + r() * 0.5).toFixed(2)}"/>`;
  }
  return s;
}

const avatar = page(800, 800, `${sky(800, 800, PAL.night, "a")}${starfield(800, 800, 40, 7, 0.6)}
${bowlMoon(400, 470, 250, "am")}${bunny(205, 270, 1.85, 0)}`);

const W = 2560, H = 1440;
const banner = page(W, H, `${sky(W, H, PAL.night, "b")}${starfield(W, H, 170, 3, 0.85)}
${cloud(560, 560, 1.4, C.lav, 0.18)}${cloud(2050, 480, 1.7, C.lav, 0.15)}
${hills(W, H, PAL.night)}
${bowlMoon(905, 745, 165, "bm")}${bunny(775, 592, 1.22, 0)}
${wordmark(1100, 700, 112)}
<text x="1105" y="772" font-family="Nunito" font-weight="700" font-size="40" fill="${C.lav}">Gentle lullabies &amp; sleep music for little ones</text>
<rect x="507" y="508" width="1546" height="423" fill="none" stroke="red" stroke-width="3" opacity="${process.env.SAFE?1:0}"/><text x="1105" y="830" font-family="Nunito" font-weight="700" font-size="34" fill="#ffffff" opacity=".75">A new lullaby every evening</text>`);

const wm = page(150, 150, `<circle cx="75" cy="75" r="75" fill="${C.navy}"/>${bowlMoon(75, 88, 46, "wm")}${bunny(40, 52, 0.34, 0)}`);

const b = await chromium.launch();
for (const [name, html, w, h] of [["avatar", avatar, 800, 800], ["banner", banner, W, H], ["watermark", wm, 150, 150]]) {
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.setContent(html); await p.waitForTimeout(200);
  await p.screenshot({ path: `brand/${name}.png`, clip: { x: 0, y: 0, width: w, height: h } });
  await p.close();
}
await b.close();
console.log("brand assets written");
