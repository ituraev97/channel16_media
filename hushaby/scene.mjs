// Little Hushaby — seamless animated scene loop -> PNG frames.
// usage: node scene.mjs '{"w":1280,"h":720,"loop":24,"fps":24,"char":"bunny","pal":"night","cap":"#b9a8e8","seed":5,"out":"frames/long","layout":"wide"}'
// Every motion uses whole cycles per loop, so frame N == frame 0 and the loop can repeat for hours without a jump.
import { chromium } from "playwright";
import fs from "fs";
import { PAL, C, fontCSS, rng, star5, bowlMoon, CHARACTERS, sky, hills, cloud } from "./art.mjs";

const o = Object.assign({ w: 1280, h: 720, loop: 24, fps: 24, char: "bunny", pal: "night", cap: C.lav, seed: 5, out: "frames/long", layout: "wide", snow: false }, JSON.parse(process.argv[2] || "{}"));
const { w: W, h: H, loop: L, fps } = o;
const pal = PAL[o.pal]; const draw = CHARACTERS[o.char];
fs.rmSync(o.out, { recursive: true, force: true }); fs.mkdirSync(o.out, { recursive: true });

const r = rng(o.seed);
const stars = Array.from({ length: Math.round(W * H / 9000) }, () => ({ x: r() * W, y: r() * H * 0.78, s: 0.8 + r() * 1.9, gold: r() > 0.9, k: 1 + Math.floor(r() * 3), ph: r() * 6.28, b: 0.35 + r() * 0.55 }));
const clouds = [0, 1, 2].map((i) => ({ x: W * (0.12 + 0.36 * i + r() * 0.1), y: H * (0.18 + r() * 0.22), s: (W / 1280) * (0.9 + r() * 0.7), ph: r() * 6.28, op: 0.1 + r() * 0.08 }));
const flakes = Array.from({ length: 70 }, () => ({ x: r() * W, y0: r() * H, sp: 1 + Math.floor(r() * 2), sw: 6 + r() * 10, ph: r() * 6.28, s: 1.5 + r() * 2.5 }));
const wide = o.layout === "wide";
const R = wide ? H * 0.27 : W * 0.36;              // moon radius
const mx = wide ? W * 0.5 : W * 0.5, my = wide ? H * 0.56 : H * 0.5;
const cs = (R * 1.55) / 220;                        // character scale (box 220 wide)
const TAU = Math.PI * 2;

function frame(t) {
  const ph = t / L;
  let s = sky(W, H, pal, "k");
  for (const st of stars) {
    const op = st.b * (0.62 + 0.38 * Math.sin(TAU * st.k * ph + st.ph));
    s += st.gold ? star5(st.x, st.y, st.s * 2.6, C.star, op.toFixed(2)) : `<circle cx="${st.x.toFixed(1)}" cy="${st.y.toFixed(1)}" r="${st.s.toFixed(1)}" fill="#fff" opacity="${op.toFixed(2)}"/>`;
  }
  for (const c of clouds) s += cloud(c.x + 22 * (W / 1280) * Math.sin(TAU * ph + c.ph), c.y, c.s, C.lav, c.op);
  s += hills(W, H, pal);
  const bob = 6 * (W / 1280) * Math.sin(TAU * ph);
  const breath = Math.sin(TAU * 6 * ph);
  s += `<g transform="translate(0,${bob.toFixed(2)})">${bowlMoon(mx, my, R, "mm")}${draw(mx - 120 * cs, my - R * 0.82 - 4 * cs, cs, breath, o.cap)}`;
  // three soft "z" drifting up from the sleeper (6 s cycle)
  for (let i = 0; i < 3; i++) {
    const p = (ph * (L / 6) + i / 3) % 1;
    const zx = mx - 40 * cs + 30 * cs * p + 8 * cs * Math.sin(TAU * p), zy = my - R * 0.82 - 10 * cs - 70 * cs * p;
    s += `<text x="${zx.toFixed(1)}" y="${zy.toFixed(1)}" font-family="Fredoka" font-weight="600" font-size="${(14 + 12 * p) * cs}" fill="${C.cream}" opacity="${(0.75 * Math.sin(Math.PI * p)).toFixed(2)}">z</text>`;
  }
  s += `</g>`;
  if (o.snow) for (const f of flakes) {
    const y = (f.y0 + (H + 20) * f.sp * ph) % (H + 20) - 10, x = f.x + f.sw * Math.sin(TAU * 2 * ph + f.ph);
    s += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${f.s}" fill="#fff" opacity=".8"/>`;
  }
  if (o.caption) {
    const lines = o.caption.split("\n"); const fs1 = W * 0.075;
    lines.forEach((ln, i) => { s += `<text x="${W / 2}" y="${H * 0.15 + i * fs1 * 1.2}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="${fs1}" fill="${i ? C.lav : C.moon}" stroke="${pal.sky0}" stroke-width="${fs1 * 0.06}" paint-order="stroke">${ln}</text>`; });
  }
  s += `<text x="${W - 26 * (W / 1280)}" y="${H - 22 * (W / 1280)}" text-anchor="end" font-family="Fredoka" font-weight="600" font-size="${24 * (W / 1280)}" fill="${C.cream}" opacity=".42">Little Hushaby</text>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${s}</svg>`;
}

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: W, height: H } });
await p.setContent(`<!doctype html><html><head><style>${fontCSS()} html,body{margin:0;background:#000;overflow:hidden}</style></head><body><div id="v"></div></body></html>`);
const N = L * fps;
for (let i = 0; i < N; i++) {
  await p.evaluate((svg) => { document.getElementById("v").innerHTML = svg; }, frame(i / fps));
  if (i === 0) await p.waitForTimeout(150);
  await p.screenshot({ path: `${o.out}/f${String(i).padStart(5, "0")}.png`, clip: { x: 0, y: 0, width: W, height: H } });
}
await b.close();
console.log(`${N} frames -> ${o.out}`);
