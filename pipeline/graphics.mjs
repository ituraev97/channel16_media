// CHANNEL 16 graphics renderer: builds HTML per graphic, renders intro frames + hold frame with Playwright.
// usage: node graphics.mjs <spec.json> <outdir>
import fs from "fs";
import path from "path";
import { createRequire } from "module";
import * as d3 from "d3-geo";
import * as topo from "topojson-client";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const NM = path.resolve("node_modules");
const world = JSON.parse(fs.readFileSync(`${NM}/world-atlas/countries-50m.json`));
const states = JSON.parse(fs.readFileSync(`${NM}/us-atlas/states-10m.json`));
const countries = topo.feature(world, world.objects.countries).features;
const land10 = JSON.parse(fs.readFileSync(`${NM}/world-atlas/land-10m.json`));
const landFeats = (() => { // split the land multipolygon into polygons and keep only those d3 sees as small (fixes inverted giant fills)
  const f = topo.feature(land10, land10.objects.land); const g = f.geometry || f.features[0].geometry;
  const polys = g.type === "MultiPolygon" ? g.coordinates : [g.coordinates];
  return polys.map((c) => { let p = { type: "Feature", geometry: { type: "Polygon", coordinates: c } };
    if (d3.geoArea(p) > 2 * Math.PI) p = { type: "Feature", geometry: { type: "Polygon", coordinates: c.map((r) => r.slice().reverse()) } };
    return p; }); })();
const usStates = topo.feature(states, states.objects.states).features;
const W = 1920, H = 1080;

const FONTS = `
@font-face{font-family:Anton;src:url(file://${NM}/@fontsource/barlow-condensed/files/barlow-condensed-latin-900-normal.woff2)}
@font-face{font-family:Oswald;font-weight:500;src:url(file://${NM}/@fontsource/barlow-condensed/files/barlow-condensed-latin-700-normal.woff2)}
@font-face{font-family:Oswald;font-weight:700;src:url(file://${NM}/@fontsource/barlow-condensed/files/barlow-condensed-latin-800-normal.woff2)}
@font-face{font-family:Plex;font-weight:500;src:url(file://${NM}/@fontsource/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2)}
@font-face{font-family:Plex;font-weight:600;src:url(file://${NM}/@fontsource/jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2)}`;

const CSS = `${FONTS}
.sonar{color:#4FD1C5}
:root{--sonar:#4FD1C5;--ink:#06141F;--bone:#EAF2F0;--red:#FF5B14;--amber:#FFC93C;--steel:#8DA2AE}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:${W}px;height:${H}px;overflow:hidden;background:var(--ink);color:var(--bone)}
.stage{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#0E2A3A 0%,#06141F 70%)}
.grain::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.18;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.6 -.3'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.mono{font-family:Plex;font-weight:600;letter-spacing:.32em;color:var(--steel)}
.anton{font-family:Anton;letter-spacing:.01em}
.osw{font-family:Oswald;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.red{color:var(--red)}.amber{color:var(--amber)}
.stamp{border:8px solid var(--red);color:var(--red);font-family:Plex;font-weight:600;letter-spacing:.3em;padding:10px 26px;display:inline-block}
.a{will-change:transform,opacity}
svg text{font-family:Oswald;font-weight:700;letter-spacing:.08em}
`;

const ANIM = `
<script>
function clamp(x){return Math.max(0,Math.min(1,x))}
function ease(x){return 1-Math.pow(1-x,3)}
window.setT=function(t){
 document.querySelectorAll('[data-d]').forEach(el=>{
  const d=parseFloat(el.dataset.d), dur=parseFloat(el.dataset.dur||'0.45'), k=el.dataset.k||'fade';
  const p=ease(clamp((t-d)/dur));
  if(k==='fade'){el.style.opacity=p;el.style.transform='translateY('+(24*(1-p))+'px)'}
  else if(k==='pop'){el.style.opacity=p;el.style.transform=(el.dataset.base||'')+' scale('+(1.35-0.35*p)+')'}
  else if(k==='slam'){el.style.opacity=p>0?1:0;el.style.transform=(el.dataset.base||'')+' scale('+(1.6-0.6*p)+')'}
  else if(k==='draw'){const L=el.getTotalLength();el.style.strokeDasharray=L;el.style.strokeDashoffset=L*(1-p);el.style.opacity=p>0?1:0}
  else if(k==='wipe'){el.style.clipPath='inset(0 '+(100-100*p)+'% 0 0)'}
  else if(k==='count'){const to=parseFloat(el.dataset.to);const v=to*p;el.textContent=(el.dataset.pre||'')+Math.round(v).toLocaleString('en-US')+(el.dataset.suf||'')}
 });
};
</script>`;

function page(body) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body><div class="stage grain">${body}</div>${ANIM}</body></html>`;
}

// ---------- map helpers ----------
const byId = (id) => countries.find((f) => +f.id === id);
function mapSvg({ bounds, highlight = {}, dim = [], cities = [], arcs = [], labels = [], rings = [], usHighlight = [], useUS = false, pad = 80, topPad = 0 }) {
  let proj, feats;
  if (useUS) {
    proj = d3.geoAlbersUsa().fitExtent([[pad, pad + 40], [W - pad, H - pad]], topo.feature(states, states.objects.states));
    feats = usStates;
  } else {
    const box = { type: "MultiPoint", coordinates: bounds };
    proj = d3.geoMercator().clipExtent([[0, 0], [W, H]]).fitExtent([[pad + (topPad ? 40 : 0), pad + topPad], [W - pad, H - pad - 40]], box);
    feats = Object.keys(highlight).length ? countries : landFeats;
  }
  const g = d3.geoPath(proj);
  let s = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="position:absolute;inset:0"><rect width="${W}" height="${H}" fill="#06141F"/>`;
  s += `<defs><filter id="glow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>`;
  for (const f of feats) {
    const id = useUS ? f.id : +f.id;
    const hl = useUS ? usHighlight.includes(id) : highlight[id];
    const fill = hl ? (useUS ? "#5A2410" : hl) : "#1F3F52";
    s += `<path d="${g(f)}" fill="${fill}" stroke="${hl ? "#FF5B14" : "#3A6378"}" stroke-width="${hl ? 2 : 1}" ${hl ? `data-d="${0.15}" data-dur="0.6"` : ""}/>`;
  }
  for (const a of arcs) {
    const p1 = proj(a.from), p2 = proj(a.to);
    const mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2;
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1];
    const bend = a.bend ?? 0.25;
    const cx = mx - dy * bend, cy = my + dx * bend;
    s += `<path d="M${p1[0]},${p1[1]} Q${cx},${cy} ${p2[0]},${p2[1]}" fill="none" stroke="${a.color || "#FFC93C"}" stroke-width="5" stroke-linecap="round" filter="url(#glow)" data-k="draw" data-d="${a.d ?? 0.4}" data-dur="${a.dur ?? 1.1}"/>`;
  }
  for (const r of rings) {
    const p = proj(r.ll); if (!p) continue;
    for (let k = 1; k <= (r.n || 3); k++) s += `<circle cx="${p[0]}" cy="${p[1]}" r="${(r.r || 60) * k}" fill="none" stroke="${r.color || "#4FD1C5"}" stroke-opacity="${0.9 - k * 0.2}" stroke-width="3" ${k === 1 ? "" : 'stroke-dasharray="10 10"'} data-d="${(r.d ?? 0.5) + k * 0.18}" data-dur="0.6"/>`;
  }
  for (const c of cities) {
    const p = proj(c.ll);
    if (!p) continue;
    const ax = c.anchor || "start";
    const dx = ax === "end" ? -22 : 22;
    s += `<g data-d="${c.d ?? 0.3}"><circle cx="${p[0]}" cy="${p[1]}" r="10" fill="${c.color || "#EAF2F0"}" filter="url(#glow)"/>`;
    const dy = c.dy || 0;
    s += `<text x="${p[0] + dx}" y="${p[1] + 12 + dy}" text-anchor="${ax}" font-size="${c.size || 38}" fill="#EAF2F0">${c.name}</text>`;
    if (c.sub) s += `<text x="${p[0] + dx}" y="${p[1] + 50 + dy}" text-anchor="${ax}" font-size="24" fill="#8DA2AE" style="font-family:Plex;letter-spacing:.2em">${c.sub}</text>`;
    s += `</g>`;
  }
  for (const l of labels) {
    const p = proj(l.ll);
    s += `<text x="${p[0]}" y="${p[1]}" text-anchor="middle" font-size="${l.size || 30}" fill="${l.color || "#8DA2AE"}" data-d="${l.d ?? 0.2}" style="letter-spacing:.3em">${l.t}</text>`;
  }
  return s + `</svg>`;
}

function header(kicker, title, d = 0.1) {
  return `<div style="position:absolute;left:110px;top:90px">
   <div class="mono a" data-d="${d}" style="font-size:24px">${kicker}</div>
   <div class="osw a" data-d="${d + 0.12}" style="font-size:64px;margin-top:10px">${title}</div></div>`;
}
const footer = (src) => `<div class="mono a" data-d="0.9" style="position:absolute;left:110px;bottom:150px;font-size:21px;letter-spacing:.16em">${src}</div>`;

// ---------- graphic builders ----------
const B = {
  title: (o) => page(`
   <svg style="position:absolute;inset:0" width="1920" height="1080">${[1, 2, 3, 4].map((k) => `<circle class="a" data-d="${0.05 + k * 0.12}" data-dur="0.8" cx="960" cy="540" r="${k * 150}" fill="none" stroke="#4FD1C5" stroke-opacity="${0.32 - k * 0.06}" stroke-width="3"/>`).join("")}</svg>
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="mono a sonar" data-d="0.05" style="font-size:30px;letter-spacing:.3em"><span style="display:inline-block;width:18px;height:18px;border-radius:50%;background:#FF5B14;box-shadow:0 0 16px #FF5B14;margin-right:16px;vertical-align:2px"></span>${o.kicker || "CH 16 · 156.800 MHz"}</div>
    <div class="anton a" data-d="0.3" data-k="pop" style="font-size:${o.size || 250}px;line-height:.88;margin-top:30px;text-align:center;text-transform:uppercase">${o.title}</div>
    <div class="osw a" data-d="0.75" style="font-size:52px;letter-spacing:.3em;margin-top:24px;padding-left:.3em;color:#8DA2AE">${o.sub || ""}</div>
   </div>
   <div class="a" data-d="1.0" style="position:absolute;bottom:64px;left:0;right:0;text-align:center"><span class="anton" style="font-size:40px;letter-spacing:.06em">CHANNEL <span style="color:#FF5B14">16</span></span></div>`),

  chapter: (o) => page(`
   <div style="position:absolute;left:180px;top:50%;transform:translateY(-50%)">
     <div class="mono a" data-d="0.05" style="font-size:30px">${o.case || "THE CALL"} · PART ${o.n}</div>
     <div class="a" data-d="0.2" data-k="wipe" style="height:10px;width:220px;background:var(--red);margin:28px 0"></div>
     <div class="anton a" data-d="0.3" style="font-size:200px;line-height:.95">${o.t}</div>
   </div>`),

  stat: (o) => {
    const m = o.a.match(/^([\d,]+)(.*)$/);
    const num = m ? `<span class="a" data-d="0.15" data-k="count" data-dur="1.1" data-to="${m[1].replace(/,/g, "")}" data-suf="${m[2]}">${o.a}</span>` : `<span class="a" data-d="0.15" data-k="pop">${o.a}</span>`;
    return page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding-left:180px">
     <div class="anton" style="font-size:300px;line-height:.9">${num}</div>
     <div class="a" data-d="0.5" data-k="wipe" style="height:10px;width:260px;background:var(--red);margin:34px 0 30px"></div>
     <div class="osw a" data-d="0.6" style="font-size:60px">${o.b}</div>
     <div class="mono a" data-d="0.8" style="font-size:26px;margin-top:20px">${o.c || ""}</div></div>`);
  },

  name: () => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
     <div class="mono a" data-d="0.05" style="font-size:28px">LOS ANGELES · EARLY 1980s</div>
     <div class="anton a" data-d="0.2" data-k="pop" style="font-size:210px;margin-top:20px">MARA <span class="red">SALVATRUCHA</span></div>
     <div class="osw a" data-d="0.7" style="font-size:44px;color:var(--amber);margin-top:10px">A GANG OF THEIR OWN</div></div>`),

  name2: () => page(`${header("WHAT THE NAME MEANS", "MARA · SALVA · TRUCHA")}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
    ${[["MARA", "Central American slang for <b>gang</b>", "possibly from <i>marabunta</i> — a swarm of army ants"], ["SALVA", "<b>Salvadoran</b>", "the refugees who founded it"], ["TRUCHA", "street slang for <b>sharp, alert</b>", "watch your back"]].map((c, i) => `
     <div class="a" data-d="${0.3 + i * 0.25}" style="border-top:8px solid ${i === 0 ? "#FF5B14" : i === 1 ? "#EAF2F0" : "#FFC93C"};padding-top:30px">
       <div class="anton" style="font-size:130px">${c[0]}</div>
       <div class="osw" style="font-size:40px;margin-top:10px;text-transform:none;letter-spacing:.02em">${c[1]}</div>
       <div style="font-family:Plex;font-size:24px;color:#8DA2AE;margin-top:16px;line-height:1.4">${c[2]}</div></div>`).join("")}
   </div>${footer("ETYMOLOGY DISPUTED · SOURCES: WIKIPEDIA, INSIGHT CRIME")}`),

  thirteen: () => {
    const letters = "ABCDEFGHIJKLM".split("");
    return page(`${header("WHY 13", "M IS THE 13TH LETTER")}
     <div style="position:absolute;left:110px;right:110px;top:380px;display:flex;justify-content:space-between">
      ${letters.map((l, i) => `<div class="a" data-d="${0.2 + i * 0.07}" style="text-align:center">
        <div class="anton" style="font-size:${l === "M" ? 190 : 110}px;color:${l === "M" ? "#FF5B14" : "#21465A"};line-height:1">${l}</div>
        <div class="mono" style="font-size:22px;letter-spacing:.1em;color:${l === "M" ? "#EAF2F0" : "#4A6A7A"}">${i + 1}</div></div>`).join("")}
     </div>
     <div class="osw a" data-d="1.3" style="position:absolute;left:110px;bottom:150px;font-size:44px;color:var(--amber)">MARA SALVATRUCHA + SUREÑOS → MS-13</div>
     ${footer("BELIEVED TO SIGNAL ALLEGIANCE TO THE SUREÑOS / MEXICAN MAFIA")}`);
  },

  cliques: () => {
    let boxes = "";
    const names = ["CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE"];
    names.forEach((n, i) => {
      const col = i % 6, row = Math.floor(i / 6);
      boxes += `<div class="a" data-d="${0.2 + i * 0.06}" data-k="pop" style="position:absolute;left:${170 + col * 270}px;top:${380 + row * 230}px;width:230px;height:170px;border:4px solid #EAF2F0;display:flex;flex-direction:column;align-items:center;justify-content:center">
       <div class="osw" style="font-size:34px">${n}</div><div class="mono" style="font-size:18px;margin-top:8px;letter-spacing:.15em">TERRITORY ${String(i + 1).padStart(2, "0")}</div></div>`;
    });
    return page(`${header("STRUCTURE", "BUILT FROM CLIQUES")}${boxes}${footer("EACH CLIQUE: ITS OWN LEADERS · ITS OWN TERRITORY · ITS OWN CRIMES")}`);
  },

  ranfla: () => {
    let s = `${header("STRUCTURE", "THE BOARD OF DIRECTORS")}
     <div class="a" data-d="0.25" data-k="pop" style="position:absolute;left:560px;top:300px;width:800px;height:170px;background:#FF5B14;display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div class="anton" style="font-size:72px">RANFLA NACIONAL</div><div class="mono" style="font-size:20px;color:#EAF2F0;letter-spacing:.2em">SENIOR LEADERS · MOSTLY INSIDE SALVADORAN PRISONS</div></div>
     <svg width="${W}" height="${H}" style="position:absolute;inset:0">`;
    for (let i = 0; i < 8; i++) {
      const x = 180 + i * 222 + 90;
      s += `<path d="M960,470 L960,560 L${x},560 L${x},640" fill="none" stroke="#8DA2AE" stroke-width="3" data-k="draw" data-d="${0.6 + i * 0.05}" data-dur="0.5"/>`;
    }
    s += `</svg>`;
    for (let i = 0; i < 8; i++) {
      s += `<div class="a" data-d="${0.9 + i * 0.05}" style="position:absolute;left:${180 + i * 222}px;top:640px;width:180px;height:120px;border:3px solid #EAF2F0;display:flex;align-items:center;justify-content:center" class="osw"><span class="osw" style="font-size:28px">CLIQUE</span></div>`;
    }
    return page(s + footer("SOURCE: U.S. DEPARTMENT OF JUSTICE, JAN. 2021"));
  },

  doc_treasury: () => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:120px;width:1260px;height:840px;background:#EAF2F0;color:#06141F;padding:80px 90px;transform:rotate(-1.2deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">U.S. DEPARTMENT OF THE TREASURY · OCTOBER 2012</div>
    <div style="height:3px;background:#06141F;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:96px;line-height:1">MS-13 DESIGNATED A<br>TRANSNATIONAL CRIMINAL<br>ORGANIZATION</div>
    <div style="font-family:Plex;font-weight:500;font-size:30px;line-height:1.5;margin-top:40px;color:#333">The first street gang to receive the designation.<br>Assets under U.S. jurisdiction can be frozen.</div>
    <div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">SOURCE: ICE / TREASURY PRESS RELEASE · EXECUTIVE ORDER 13581</div>
   </div>
   <div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-12deg)" style="position:absolute;right:300px;bottom:170px;font-size:44px;background:rgba(236,231,220,.0)">DESIGNATED · TCO</div>
   `),

  raging: (o) => page(`${header("OPERATION RAGING BULL", o.phase === 1 ? "PHASE I · EL SALVADOR" : "PHASE II · UNITED STATES")}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:60px">
    <div class="a" data-d="0.25" style="border-top:10px solid ${o.phase === 1 ? "#FF5B14" : "#21465A"};padding-top:30px;opacity:${o.phase === 1 ? 1 : .45}">
      <div class="mono" style="font-size:24px">PHASE I · EL SALVADOR</div>
      <div class="anton" style="font-size:220px;line-height:1">${o.phase === 1 ? `<span class="a" data-d="0.4" data-k="count" data-to="53" data-dur="1">53</span>` : "53"}</div>
      <div class="osw" style="font-size:36px">ARRESTS · 18-MONTH INVESTIGATION</div></div>
    <div class="a" data-d="0.4" style="border-top:10px solid ${o.phase === 2 ? "#FF5B14" : "#21465A"};padding-top:30px;opacity:${o.phase === 2 ? 1 : .45}">
      <div class="mono" style="font-size:24px">PHASE II · U.S. · OCT 8 – NOV 11, 2017</div>
      <div class="anton" style="font-size:220px;line-height:1">${o.phase === 2 ? `<span class="a" data-d="0.55" data-k="count" data-to="214" data-dur="1.1">214</span>` : "—"}</div>
      <div class="osw" style="font-size:36px">${o.phase === 2 ? "ARRESTS · 93 CRIMINAL CHARGES" : "&nbsp;"}</div></div>
   </div>
   ${o.phase === 2 ? `<div class="osw a" data-d="1.2" style="position:absolute;left:110px;bottom:140px;font-size:56px;color:var(--amber)">TOTAL: 267 ARRESTS</div>` : ""}
   ${footer("SOURCES: ICE, NBC NEWS · NOVEMBER 2017")}`),

  quote: (o) => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 200px">
    <div class="anton a" data-d="0.05" style="font-size:240px;color:#FF5B14;line-height:.6">“</div>
    <div class="osw a" data-d="0.2" style="font-size:92px;line-height:1.1;text-transform:none;letter-spacing:.01em">${o.q.replace(/[“”]/g, "")}</div>
    <div class="mono a" data-d="0.7" style="font-size:26px;margin-top:40px">${o.w}</div></div>`),

  doc_doj: () => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:110px;width:1260px;height:860px;background:#EAF2F0;color:#06141F;padding:80px 90px;transform:rotate(1deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">EASTERN DISTRICT OF NEW YORK · JANUARY 14, 2021</div>
    <div style="height:3px;background:#06141F;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:110px;line-height:1">INDICTMENT<br>UNSEALED</div>
    <div style="font-family:Plex;font-weight:500;font-size:32px;line-height:1.5;margin-top:40px;color:#333">Defendants: 14 leaders of the<br><b>Ranfla Nacional</b> — MS-13's top council.<br>Investigated by Joint Task Force Vulcan.</div>
    <div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">SOURCE: U.S. DEPARTMENT OF JUSTICE · CHARGES ARE ALLEGATIONS</div>
   </div>
   <div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-10deg)" style="position:absolute;right:300px;bottom:150px;font-size:44px">TERRORISM CHARGES</div>
   `),

  charges: () => page(`${header("THE CHARGES", "UNITED STATES v. RANFLA NACIONAL")}
   <div style="position:absolute;left:110px;top:330px">
   ${["Conspiracy to provide material support to terrorists", "Conspiracy to commit acts of terrorism transcending national boundaries", "Conspiracy to finance terrorism", "Narco-terrorism conspiracy"].map((c, i) => `
    <div class="a" data-d="${0.25 + i * 0.25}" style="display:flex;align-items:center;gap:34px;margin-bottom:44px">
     <div class="anton" style="font-size:72px;color:#FF5B14;width:80px">0${i + 1}</div>
     <div class="osw" style="font-size:52px;text-transform:none;letter-spacing:.01em">${c}</div></div>`).join("")}
   </div>${footer("ALLEGATIONS · DEFENDANTS PRESUMED INNOCENT UNLESS PROVEN GUILTY")}`),

  fto: () => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="mono a" data-d="0.05" style="font-size:28px">U.S. DEPARTMENT OF STATE · FEBRUARY 20, 2025</div>
    <div class="anton a" data-d="0.25" style="font-size:150px;margin-top:30px;text-align:center;line-height:1">FOREIGN TERRORIST<br>ORGANIZATION</div>
    <div class="stamp a" data-d="0.9" data-k="slam" data-base="rotate(-5deg)" style="font-size:54px;margin-top:50px">MS-13 · DESIGNATED</div></div>
    ${footer("SOURCE: FEDERAL REGISTER, FEBRUARY 2025")}`),

  end: (o) => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="mono a" data-d="0.05" style="font-size:30px">${o.label || "CH 16 · 156.800 MHz"}</div>
    <div class="stamp a" data-d="0.4" data-k="slam" data-base="rotate(-6deg)" style="font-size:120px;margin-top:40px;padding:20px 60px;border-width:14px">${o.stamp || "ALL SAFE"}</div>
    <div class="a" data-d="1.2" style="margin-top:80px"><span class="anton" style="font-size:72px;letter-spacing:.06em">CHANNEL <span style="color:#FF5B14">16</span></span></div>
    <div class="osw a" data-d="1.5" style="font-size:34px;color:var(--amber);margin-top:20px">SUBSCRIBE FOR THE NEXT CALL</div></div>`),

  // ---------- generic builders for future episodes ----------
  doc: (o) => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:120px;width:1260px;height:840px;background:#EAF2F0;color:#06141F;padding:80px 90px;transform:rotate(${o.rot ?? -1}deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">${o.header}</div>
    <div style="height:3px;background:#06141F;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:${o.tsize || 96}px;line-height:1">${o.title}</div>
    <div style="font-family:Plex;font-weight:500;font-size:30px;line-height:1.5;margin-top:40px;color:#333">${o.body || ""}</div>
    ${o.source ? `<div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">${o.source}</div>` : ""}
   </div>
   ${o.stamp ? `<div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-10deg)" style="position:absolute;right:300px;bottom:160px;font-size:44px">${o.stamp}</div>` : ""}
   `),
  list: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;top:330px;right:110px">
   ${o.items.map((c, i) => `<div class="a" data-d="${0.25 + i * 0.22}" style="display:flex;align-items:center;gap:34px;margin-bottom:40px">
     <div class="anton" style="font-size:72px;color:#FF5B14;width:90px">${String(i + 1).padStart(2, "0")}</div>
     <div class="osw" style="font-size:50px;text-transform:none;letter-spacing:.01em">${c}</div></div>`).join("")}
   </div>${o.footer ? footer(o.footer) : ""}`),
  phases: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:60px">
    ${[o.left, o.right].map((c, i) => `<div class="a" data-d="${0.25 + i * 0.15}" style="border-top:10px solid ${o.active === i ? "#FF5B14" : "#21465A"};padding-top:30px;opacity:${o.active === i || o.active === undefined ? 1 : .45}">
      <div class="mono" style="font-size:24px">${c.label}</div>
      <div class="anton" style="font-size:220px;line-height:1">${c.num}</div>
      <div class="osw" style="font-size:36px">${c.desc}</div></div>`).join("")}
   </div>
   ${o.total ? `<div class="osw a" data-d="1.2" style="position:absolute;left:110px;bottom:140px;font-size:56px;color:var(--amber)">${o.total}</div>` : ""}
   ${o.footer ? footer(o.footer) : ""}`),
  cards3: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
    ${o.cards.map((c, i) => `<div class="a" data-d="${0.3 + i * 0.25}" style="border-top:8px solid ${["#FF5B14", "#EAF2F0", "#FFC93C"][i % 3]};padding-top:30px">
       <div class="anton" style="font-size:${c.size || 110}px;line-height:1">${c.h}</div>
       <div class="osw" style="font-size:38px;margin-top:14px;text-transform:none;letter-spacing:.02em">${c.t}</div>
       <div style="font-family:Plex;font-size:24px;color:#8DA2AE;margin-top:16px;line-height:1.4">${c.s || ""}</div></div>`).join("")}
   </div>${o.footer ? footer(o.footer) : ""}`),
  timeline: (o) => page(`${header(o.kicker, o.title)}
   <div class="a" data-d="0.2" data-k="wipe" style="position:absolute;left:110px;right:110px;top:560px;height:6px;background:#21465A"></div>
   ${o.events.map((e, i) => { const x = 110 + i * (1700 / Math.max(1, o.events.length - 1)); return `<div class="a" data-d="${0.35 + i * 0.2}" style="position:absolute;left:${x - 12}px;top:548px;width:30px;height:30px;border-radius:50%;background:${i === o.events.length - 1 ? "#FF5B14" : "#EAF2F0"}"></div>
     <div class="a" data-d="${0.4 + i * 0.2}" style="position:absolute;left:${Math.min(x - 20, 1550)}px;top:${i % 2 ? 610 : 380}px;width:340px"><div class="anton" style="font-size:64px">${e.y}</div><div class="osw" style="font-size:28px;text-transform:none;letter-spacing:.02em">${e.t}</div></div>`; }).join("")}
   ${o.footer ? footer(o.footer) : ""}`),
  map: (o) => page(mapSvg(o.map) + (o.kicker ? header(o.kicker, o.title) : "") + (o.footer ? footer(o.footer) : "")),

};

B.callcard = (o) => page(`${header(o.kicker || "CH 16 · LOG", o.title || "")}
  <div style="position:absolute;left:110px;top:300px;width:1700px">${o.rows.map((r, i) => `<div class="a" data-d="${0.4 + i * 0.32}" style="display:flex;gap:44px;align-items:baseline;padding:22px 0;border-top:2px solid #21465A">
    <div class="mono sonar" style="font-size:40px;letter-spacing:.08em;width:260px">${r[0]}</div>
    <div class="osw" style="font-size:54px;letter-spacing:.03em;color:${i === o.rows.length - 1 ? "#FF5B14" : "#EAF2F0"}">${r[1]}</div></div>`).join("")}</div>
  ${o.footer ? footer(o.footer) : ""}`);
B.steps = (o) => page(`${header(o.kicker, o.title)}
  <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:repeat(${o.items.length},1fr);gap:40px">${o.items.map((it, i) => `<div class="a" data-d="${0.35 + i * 0.25}" style="border-top:8px solid ${i === (o.active ?? -1) ? "#FF5B14" : "#4FD1C5"};padding-top:28px">
    <div class="mono" style="font-size:28px;color:#8DA2AE;letter-spacing:.2em">${String(i + 1).padStart(2, "0")}</div>
    <div class="anton" style="font-size:84px;line-height:.95;margin-top:14px;text-transform:uppercase">${it[0]}</div>
    <div style="font-family:Oswald;font-weight:500;font-size:40px;color:#8DA2AE;margin-top:16px;line-height:1.2">${it[1]}</div></div>`).join("")}</div>
  ${o.footer ? footer(o.footer) : ""}`);

const spec = JSON.parse(fs.readFileSync(process.argv[2]));
const outdir = process.argv[3];
fs.mkdirSync(outdir, { recursive: true });
const browser = await chromium.launch();
const pg = await browser.newPage({ viewport: { width: W, height: H } });
for (const g of spec) {
  const dir = path.join(outdir, g.key);
  fs.mkdirSync(dir, { recursive: true });
  const html = B[g.name](g.opts || {});
  const f = path.join(dir, "index.html");
  fs.writeFileSync(f, html);
  await pg.goto("file://" + f);
  await pg.evaluate(() => document.fonts.ready);
  const n = Math.round((g.intro || 1.8) * 30);
  for (let i = 0; i <= n; i++) {
    await pg.evaluate((t) => window.setT(t), i / 30);
    await pg.screenshot({ path: path.join(dir, `f${String(i).padStart(4, "0")}.jpg`), type: "jpeg", quality: 92 });
  }
  console.log("rendered", g.key, n + 1, "frames");
}
await browser.close();
