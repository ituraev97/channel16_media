#!/usr/bin/env python3
"""Smoothness QA. usage: motion_check.py <video.mp4> [timing.json]
Reads every frame (gray, 192x108) and reports, away from cuts:
  - REPEAT: inside moving footage a frame identical to the previous one while neighbours move (dropped/duplicated frame -> judder)
  - JUMP: a frame-to-frame change > 4x the local median (a hitch, wobble or bad seam)
  - GFX: graphic segments that are not perfectly still after their intro (any drift after 2.6 s)
Exit code 1 if anything is found."""
import sys, json, subprocess, numpy as np
vid = sys.argv[1]; tj = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else None
CM = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
W, H = 192, 108
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", vid, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
prev, d = None, []
while True:
    b = p.stdout.read(W * H)
    if len(b) < W * H: break
    f = np.frombuffer(b, np.uint8).astype(np.float32)
    if prev is not None: d.append(np.abs(f - prev).mean())
    prev = f
d = np.array(d); fps = 30.0
cuts, gfx = set(), []
if tj:
    for s in tj["segs"]:
        c = int(round(s["t"] * fps)); cuts.update(range(c - 2, c + 3))
        if s["src"].startswith("g:"): gfx.append((s["t"], s["t"] + s["d"]))
        elif CM:
            for sc in CM.get(str(s["src"]), {}).get("cuts", []):
                if s["ss"] < sc < s["ss"] + s["d"]: c2 = int(round((s["t"] + sc - s["ss"]) * fps)); cuts.update(range(c2 - 2, c2 + 3))
def in_gfx(i):
    t = i / fps; return any(a <= t < b for a, b in gfx)
issues = []
for i in range(3, len(d) - 3):
    if i in cuts: continue
    loc = np.median(np.r_[d[i - 3:i], d[i + 1:i + 4]])
    t = (i + 1) / fps
    if not in_gfx(i):
        if d[i] < 0.02 and loc > 0.6: issues.append((t, "REPEAT", round(float(loc), 2)))
        if loc > 0.3 and d[i] > 4 * loc and d[i] > 3: issues.append((t, "JUMP", round(float(d[i] / loc), 1)))
for a, b in gfx:
    i0, i1 = int((a + 2.6) * fps), int(b * fps) - 2
    if i1 > i0 and d[i0:i1].max() > 0.3: issues.append((a, "GFX-DRIFT", round(float(d[i0:i1].max()), 2)))
for t, k, v in issues: print(f"{int(t//60)}:{t%60:05.2f}  {k}  {v}")
print(f"frames {len(d)+1}, issues {len(issues)}")
sys.exit(1 if issues else 0)
