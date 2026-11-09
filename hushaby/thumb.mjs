// Thumbnail 1280x720. usage: node thumb.mjs '{"l1":"Brahms Lullaby","l2":"& Twinkle Twinkle","badge":"Music Box · 12 min","char":"bunny","pal":"night","out":"thumb.png"}'
import { chromium } from "playwright";
import { PAL, C, fontCSS, rng, star5, bowlMoon, CHARACTERS, sky, cloud } from "./art.mjs";
const o = Object.assign({ l1: "Brahms Lullaby", l2: "", badge: "", char: "bunny", pal: "night", cap: C.lav, out: "thumb.png", seed: 9 }, JSON.parse(process.argv[2] || "{}"));
const W = 1280, H = 720, pal = PAL[o.pal], r = rng(o.seed);
let s = sky(W, H, pal, "t");
for (let i = 0; i < 70; i++) { const x = r() * W, y = r() * H; s += r() > 0.85 ? star5(x, y, 5 + r() * 6, C.star, 0.9) : `<circle cx="${x}" cy="${y}" r="${1 + r() * 2}" fill="#fff" opacity="${0.4 + r() * 0.5}"/>`; }
s += cloud(980, 130, 1.3, C.lav, 0.16);
const R = 230, mx = 930, my = 430;
s += bowlMoon(mx, my, R, "tm") + CHARACTERS[o.char](mx - 120 * 2.0, my - R * 0.82 - 8, 2.0, 0, o.cap);
const fit = (txt, max, base) => Math.min(base, Math.floor(max / (txt.length * 0.52)));
const f1 = fit(o.l1, 600, 104), f2 = fit(o.l2, 600, 66);
s += `<text x="60" y="${o.l2 ? 300 : 340}" font-family="Fredoka" font-weight="700" font-size="${f1}" fill="${C.moon}" stroke="${pal.sky0}" stroke-width="10" paint-order="stroke">${o.l1}</text>`;
if (o.l2) s += `<text x="64" y="${300 + f2 * 1.25}" font-family="Fredoka" font-weight="600" font-size="${f2}" fill="${C.lav}" stroke="${pal.sky0}" stroke-width="8" paint-order="stroke">${o.l2}</text>`;
if (o.badge) { const bw = o.badge.length * 21 + 64; s += `<rect x="60" y="470" rx="34" width="${bw}" height="68" fill="${C.star}"/><text x="${60 + bw / 2}" y="516" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="38" fill="${C.navy}">${o.badge}</text>`; }
s += `<text x="62" y="660" font-family="Fredoka" font-weight="600" font-size="34" fill="${C.cream}" opacity=".7">Little Hushaby</text>`;
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H } });
await p.setContent(`<!doctype html><html><head><style>${fontCSS()} html,body{margin:0}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">${s}</svg></body></html>`);
await p.waitForTimeout(200); await p.screenshot({ path: o.out, clip: { x: 0, y: 0, width: W, height: H } }); await b.close();
console.log("thumb", o.out);
