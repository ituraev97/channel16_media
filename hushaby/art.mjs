// Little Hushaby — shared SVG art (brand palette, mascot, moon, sky). Pure functions returning SVG strings.
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
const here = path.dirname(fileURLToPath(import.meta.url));

export const PAL = {
  night: { sky0: "#141a3d", sky1: "#252b63", sky2: "#4a3f86", glow: "#ffe9b0", hill0: "#1b2149", hill1: "#232a5a" },
  dusk: { sky0: "#1d1b45", sky1: "#3b2f6e", sky2: "#8a5f9e", glow: "#ffd9a8", hill0: "#241f4f", hill1: "#2f2862" },
  winter: { sky0: "#0f1c38", sky1: "#1e3463", sky2: "#3f5d8f", glow: "#f3f6ff", hill0: "#dfe6f5", hill1: "#c9d3ea" },
  ocean: { sky0: "#0d1a33", sky1: "#17305a", sky2: "#2c5b7e", glow: "#fff1c4", hill0: "#10294a", hill1: "#163a62" },
};
export const C = {
  moon: "#ffe9b0", moonShade: "#f4d58c", cream: "#fbf6ee", creamShade: "#ece2d6", pink: "#f6b8c8", pinkDeep: "#ec97ad",
  lav: "#b9a8e8", lavDeep: "#9583d6", star: "#ffd976", ink: "#5a4a6b", navy: "#141a3d", brown: "#b88a63", brownShade: "#a17552", ginger: "#f2c08f", gingerShade: "#e0a46f", gingerStripe: "#d48f5c",
};

export function fontCSS() {
  const f = (p) => fs.readFileSync(path.join(here, "node_modules/@fontsource", p)).toString("base64");
  return `@font-face{font-family:Fredoka;font-weight:600;src:url(data:font/woff2;base64,${f("fredoka/files/fredoka-latin-600-normal.woff2")}) format('woff2')}
@font-face{font-family:Fredoka;font-weight:500;src:url(data:font/woff2;base64,${f("fredoka/files/fredoka-latin-500-normal.woff2")}) format('woff2')}
@font-face{font-family:Fredoka;font-weight:700;src:url(data:font/woff2;base64,${f("fredoka/files/fredoka-latin-700-normal.woff2")}) format('woff2')}
@font-face{font-family:Nunito;font-weight:700;src:url(data:font/woff2;base64,${f("nunito/files/nunito-latin-700-normal.woff2")}) format('woff2')}`;
}

// deterministic random
export function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

export function star5(cx, cy, r, fill, op = 1) {
  const pts = [];
  for (let i = 0; i < 10; i++) {
    const a = -Math.PI / 2 + (i * Math.PI) / 5, rr = i % 2 ? r * 0.45 : r;
    pts.push(`${(cx + rr * Math.cos(a)).toFixed(1)},${(cy + rr * Math.sin(a)).toFixed(1)}`);
  }
  return `<polygon points="${pts.join(" ")}" fill="${fill}" opacity="${op}" stroke="${fill}" stroke-width="${(r * 0.18).toFixed(1)}" stroke-linejoin="round"/>`;
}

// crescent "bowl" moon centred at (cx,cy) with outer radius R
export function bowlMoon(cx, cy, R, id = "m") {
  return `<defs><mask id="${id}mask"><rect x="${cx - R - 5}" y="${cy - R - 5}" width="${2 * R + 10}" height="${2 * R + 10}" fill="#fff"/>
<circle cx="${cx}" cy="${cy - R * 0.42}" r="${R * 0.93}" fill="#000"/></mask>
<radialGradient id="${id}glow"><stop offset="0" stop-color="${C.moon}" stop-opacity=".55"/><stop offset="1" stop-color="${C.moon}" stop-opacity="0"/></radialGradient></defs>
<circle cx="${cx}" cy="${cy}" r="${R * 1.55}" fill="url(#${id}glow)"/>
<g mask="url(#${id}mask)"><circle cx="${cx}" cy="${cy}" r="${R}" fill="${C.moon}"/>
<circle cx="${cx + R * 0.35}" cy="${cy + R * 0.55}" r="${R * 0.09}" fill="${C.moonShade}"/><circle cx="${cx - R * 0.45}" cy="${cy + R * 0.42}" r="${R * 0.06}" fill="${C.moonShade}"/>
<circle cx="${cx - R * 0.05}" cy="${cy + R * 0.78}" r="${R * 0.05}" fill="${C.moonShade}"/></g>`;
}

// sleeping bunny in a local 220x150 box (head left). breath 0..1 scales the body a little.
export function bunny(x, y, s = 1, breath = 0, capColor = C.lav) {
  const b = 1 + 0.025 * breath;
  return `<g transform="translate(${x},${y}) scale(${s})">
 <ellipse cx="118" cy="128" rx="74" ry="9" fill="#000" opacity=".12"/>
 <g transform="translate(118,124) scale(1,${b}) translate(-118,-124)">
  <ellipse cx="122" cy="96" rx="62" ry="36" fill="${C.cream}"/>
  <ellipse cx="128" cy="108" rx="52" ry="22" fill="${C.creamShade}" opacity=".55"/>
  <circle cx="180" cy="86" r="13" fill="#fff"/>
  <ellipse cx="150" cy="118" rx="20" ry="9" fill="${C.cream}"/>
 </g>
 <g transform="rotate(-8 92 52)">
  <ellipse cx="118" cy="48" rx="42" ry="12" fill="${C.cream}"/><ellipse cx="121" cy="48" rx="31" ry="6" fill="${C.pink}"/>
 </g>
 <g transform="rotate(4 92 60)">
  <ellipse cx="122" cy="64" rx="40" ry="12" fill="${C.creamShade}"/><ellipse cx="125" cy="64" rx="29" ry="5.5" fill="${C.pinkDeep}" opacity=".8"/>
 </g>
 <circle cx="66" cy="86" r="38" fill="${C.cream}"/>
 <path d="M40 88 q9 8 18 0" fill="none" stroke="${C.ink}" stroke-width="3.4" stroke-linecap="round"/>
 <path d="M44 92 l-3 4 M50 94 l0 5 M56 92 l3 4" stroke="${C.ink}" stroke-width="2" stroke-linecap="round"/>
 <ellipse cx="44" cy="104" rx="9" ry="5" fill="${C.pink}" opacity=".85"/>
 <ellipse cx="88" cy="102" rx="7" ry="4" fill="${C.pink}" opacity=".6"/>
 <circle cx="30" cy="96" r="4" fill="${C.pinkDeep}"/>
 <path d="M30 100 q4 5 9 2" fill="none" stroke="${C.ink}" stroke-width="1.8" stroke-linecap="round"/>
 <ellipse cx="54" cy="122" rx="17" ry="9" fill="${C.cream}"/><path d="M46 124 l0 4 M53 125 l0 4" stroke="${C.creamShade}" stroke-width="2" stroke-linecap="round"/>
 <path d="M38 62 Q58 36 92 50 Q112 36 132 32 Q118 50 100 72 Q70 54 38 62 Z" fill="${capColor}"/>
 <path d="M36 64 Q66 50 100 72" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".9"/>
 ${star5(134, 31, 10, C.star)}
</g>`;
}

// sleeping teddy bear in the same 220x150 box
export function bear(x, y, s = 1, breath = 0, capColor = C.lav) {
  const b = 1 + 0.025 * breath;
  return `<g transform="translate(${x},${y}) scale(${s})">
 <ellipse cx="118" cy="128" rx="74" ry="9" fill="#000" opacity=".12"/>
 <g transform="translate(118,124) scale(1,${b}) translate(-118,-124)">
  <ellipse cx="124" cy="94" rx="64" ry="38" fill="${C.brown}"/>
  <ellipse cx="128" cy="106" rx="50" ry="22" fill="${C.brownShade}" opacity=".5"/>
  <ellipse cx="152" cy="118" rx="21" ry="10" fill="${C.brown}"/>
 </g>
 <circle cx="66" cy="84" r="40" fill="${C.brown}"/>
 <circle cx="88" cy="50" r="13" fill="${C.brown}"/><circle cx="88" cy="50" r="7" fill="${C.pink}" opacity=".8"/>
 <ellipse cx="42" cy="98" rx="20" ry="15" fill="#e7c9a6"/>
 <ellipse cx="32" cy="92" rx="6" ry="4.5" fill="${C.ink}"/>
 <path d="M30 100 q5 5 10 1" fill="none" stroke="${C.ink}" stroke-width="1.8" stroke-linecap="round"/>
 <path d="M50 78 q9 8 18 0" fill="none" stroke="${C.ink}" stroke-width="3.4" stroke-linecap="round"/>
 <ellipse cx="74" cy="98" rx="8" ry="4.5" fill="${C.pink}" opacity=".7"/>
 <ellipse cx="56" cy="122" rx="18" ry="9" fill="${C.brown}"/>
 <path d="M34 58 Q56 30 92 44 Q114 30 134 28 Q120 46 102 68 Q70 48 34 58 Z" fill="${capColor}"/>
 <path d="M32 60 Q64 46 102 68" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".9"/>
 ${star5(136, 27, 10, C.star)}
</g>`;
}


// sleeping ginger kitten in the same 220x150 box (head left, eyes closed, curled tail, nightcap)
export function kitten(x, y, s = 1, breath = 0, capColor = C.lav) {
  const b = 1 + 0.025 * breath;
  return `<g transform="translate(${x},${y}) scale(${s})">
 <ellipse cx="118" cy="128" rx="74" ry="9" fill="#000" opacity=".12"/>
 <path d="M176 112 Q214 112 206 84 Q200 66 184 74" fill="none" stroke="${C.ginger}" stroke-width="15" stroke-linecap="round"/>
 <path d="M200 80 Q196 72 186 76" fill="none" stroke="${C.gingerStripe}" stroke-width="15" stroke-linecap="round" opacity=".6"/>
 <g transform="translate(118,124) scale(1,${b}) translate(-118,-124)">
  <ellipse cx="124" cy="96" rx="62" ry="34" fill="${C.ginger}"/>
  <ellipse cx="128" cy="108" rx="50" ry="20" fill="${C.gingerShade}" opacity=".5"/>
  <path d="M112 66 q6 14 0 26 M132 64 q6 14 0 28 M152 68 q6 12 0 24" fill="none" stroke="${C.gingerStripe}" stroke-width="5" stroke-linecap="round" opacity=".55"/>
  <ellipse cx="150" cy="120" rx="20" ry="8" fill="${C.ginger}"/>
 </g>
 <path d="M38 64 L42 34 L64 54 Z" fill="${C.ginger}"/><path d="M44 58 L45 42 L57 53 Z" fill="${C.pink}" opacity=".8"/>
 <path d="M80 52 L98 30 L102 62 Z" fill="${C.ginger}"/>
 <circle cx="66" cy="86" r="37" fill="${C.ginger}"/>
 <ellipse cx="50" cy="102" rx="20" ry="13" fill="${C.cream}"/>
 <path d="M60 64 q4 6 0 12 M70 62 q4 6 0 12" fill="none" stroke="${C.gingerStripe}" stroke-width="3.5" stroke-linecap="round" opacity=".6"/>
 <path d="M38 86 q8 7 16 0" fill="none" stroke="${C.ink}" stroke-width="3.2" stroke-linecap="round"/>
 <path d="M68 86 q8 7 16 0" fill="none" stroke="${C.ink}" stroke-width="3.2" stroke-linecap="round"/>
 <path d="M47 96 l5 4 l5 -4 Z" fill="${C.pinkDeep}"/>
 <path d="M52 100 q-4 5 -8 3 M52 100 q4 5 8 3" fill="none" stroke="${C.ink}" stroke-width="1.8" stroke-linecap="round"/>
 <path d="M30 100 l-14 -2 M30 104 l-13 3 M74 100 l14 -2 M74 104 l13 3" stroke="${C.cream}" stroke-width="1.6" stroke-linecap="round" opacity=".9"/>
 <ellipse cx="34" cy="96" rx="6" ry="3.5" fill="${C.pink}" opacity=".6"/><ellipse cx="80" cy="96" rx="6" ry="3.5" fill="${C.pink}" opacity=".6"/>
 <ellipse cx="56" cy="122" rx="17" ry="8" fill="${C.ginger}"/><path d="M48 124 l0 4 M55 125 l0 4" stroke="${C.gingerShade}" stroke-width="2" stroke-linecap="round"/>
 <path d="M50 58 Q66 34 96 46 Q114 34 134 30 Q120 48 104 68 Q76 50 50 58 Z" fill="${capColor}"/>
 <path d="M46 60 Q74 48 104 68" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".9"/>
 ${star5(136, 29, 10, C.star)}
</g>`;
}

export const CHARACTERS = { bunny, bear, kitten };

export function sky(W, H, pal, id = "s") {
  return `<defs><linearGradient id="${id}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${pal.sky0}"/><stop offset=".62" stop-color="${pal.sky1}"/><stop offset="1" stop-color="${pal.sky2}"/></linearGradient></defs>
<rect width="${W}" height="${H}" fill="url(#${id}g)"/>`;
}

export function hills(W, H, pal) {
  return `<path d="M0 ${H * 0.86} Q${W * 0.18} ${H * 0.78} ${W * 0.38} ${H * 0.86} T${W * 0.78} ${H * 0.84} T${W} ${H * 0.82} L${W} ${H} L0 ${H} Z" fill="${pal.hill1}"/>
<path d="M0 ${H * 0.92} Q${W * 0.25} ${H * 0.85} ${W * 0.5} ${H * 0.92} T${W} ${H * 0.9} L${W} ${H} L0 ${H} Z" fill="${pal.hill0}"/>`;
}

export function cloud(x, y, s, fill, op) {
  return `<g transform="translate(${x},${y}) scale(${s})" opacity="${op}" fill="${fill}">
<ellipse cx="0" cy="0" rx="70" ry="26"/><circle cx="-30" cy="-14" r="28"/><circle cx="14" cy="-24" r="34"/><circle cx="50" cy="-8" r="24"/></g>`;
}

export function wordmark(x, y, size, fill = C.moon, anchor = "start") {
  return `<text x="${x}" y="${y}" font-family="Fredoka" font-weight="600" font-size="${size}" fill="${fill}" text-anchor="${anchor}" letter-spacing="${size * 0.01}">Little Hushaby</text>`;
}
