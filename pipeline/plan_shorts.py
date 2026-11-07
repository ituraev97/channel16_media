#!/usr/bin/env python3
"""Plan Shorts shot windows before building (bible: saves rebuilds).
usage: plan_shorts.py <episode_dir> <clips_dir> [id ...]   (PLATFORM=youtube plans YSHORTS)
Synthesizes each line with the same Kokoro settings as short16.py (cached in <ep>/shorts/_plan), then prints every shot's
source window ss..ss+d and flags OVERLAP (same clip, windows intersect), END (window runs past the clip), FRAG (a <1.2 s piece between cuts)."""
import os, re, sys, json, hashlib, subprocess, importlib.util, numpy as np, soundfile as sf, librosa
EP, CL = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); ONLY = set(sys.argv[3:])
sp = importlib.util.spec_from_file_location("ss", f"{EP}/shorts_spec.py"); SS = importlib.util.module_from_spec(sp); sp.loader.exec_module(SS)
YT = os.environ.get("PLATFORM", "tiktok") == "youtube"; FIX = os.environ.get("FIX") == "1"; NEW = []
META = json.load(open(f"{CL}/clips.json")); FPS = 30
from kokoro_onnx import Kokoro
K = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
SPEED = {"calm": 1.0, "punch": 0.93, "tense": 1.04, "slow": 0.92, "drive": 1.08, "question": 0.96}
PAUSE = {"calm": .22, "punch": .38, "tense": .18, "slow": .4, "drive": .15, "question": .35}
cache = f"{EP}/shorts/_plan"; os.makedirs(cache, exist_ok=True)
def dur(txt, kind):
    h = hashlib.md5(f"{txt}|{kind}".encode()).hexdigest()[:12]; f = f"{cache}/{h}.wav"
    if not os.path.exists(f):
        parts = []
        sents = [s for s in re.split(r"(?<=[.!?])\s+", txt) if s]
        for j, s in enumerate(sents):
            a, _ = K.create(s, voice="am_eric", speed=SPEED[kind] * (0.94 if len(s.split()) <= 4 else 1), lang="en-us")
            a, _ = librosa.effects.trim(a, top_db=38); parts.append(a)
            if j < len(sents) - 1: parts.append(np.zeros(int(24000 * PAUSE[kind]), np.float32))
        sf.write(f, np.concatenate(parts), 24000)
    return sf.info(f).duration
cdur = {}
def clipdur(c):
    if c not in cdur: cdur[c] = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{CL}/{c}.mp4"]))
    return cdur[c]
for sh in (SS.YSHORTS if YT else SS.SHORTS):
    if ONLY and sh["id"] not in ONLY: continue
    starts, t = [], 0.35
    ds = []
    for txt, shots, kind, *_ in sh["lines"]:
        d = dur(txt, kind); starts.append(t); ds.append(d); t += d + (0.45 if kind in ("punch", "slow") else 0.28)
    TOTAL = t + 1.6; acc = 0.0; wins = []
    print(f"== {sh['id']} total {TOTAL:.1f} s  words {sum(len(l[0].split()) for l in sh['lines'])}")
    for li, (txt, shots, kind, *_) in enumerate(sh["lines"]):
        a0 = 0.0 if li == 0 else starts[li]; b0 = starts[li + 1] if li + 1 < len(starts) else TOTAL
        for j, (cid, ss, cx) in enumerate(shots):
            d = round((a0 + (b0 - a0) * (j + 1) / len(shots) - acc) * FPS) / FPS; acc += d
            cuts = META.get(str(cid), {}).get("cuts", []); flags = []
            if FIX:  # nearest start to the requested one that is clean
                def clean(x):
                    if x < 0.2 or x + d > clipdur(str(cid)) - 0.15: return False
                    pts = [x] + [c for c in cuts if x + 0.05 < c < x + d - 0.05] + [x + d]
                    if any(pts[k + 1] - pts[k] < 1.2 for k in range(len(pts) - 1)): return False
                    return not any(c2 == str(cid) and s2 - 0.1 < x + d and x < e2 + 0.1 for (c2, s2, e2, l2) in wins)
                cand = [round(ss + sg * k * 0.1, 2) for k in range(0, 3000) for sg in ((1,) if k == 0 else (1, -1))]
                ss = next((x for x in cand if clean(x)), ss)
            NEW.append(ss)
            if ss + d > clipdur(str(cid)) - 0.1: flags.append("END")
            pts = [ss] + [c for c in cuts if ss + 0.05 < c < ss + d - 0.05] + [ss + d]
            if any(pts[k + 1] - pts[k] < 1.2 for k in range(len(pts) - 1)): flags.append(f"FRAG{[round(c,2) for c in cuts if ss < c < ss + d]}")
            for (c2, s2, e2, l2) in wins:
                if c2 == str(cid) and s2 < ss + d and ss < e2: flags.append(f"OVERLAP(line {l2})")
            wins.append((str(cid), ss, ss + d, li + 1))
            print(f"  L{li+1:02d} {cid:>9} {ss:7.2f}-{ss+d:7.2f} ({d:4.2f})", " ".join(flags))

if FIX:
    sp_f = f"{EP}/shorts_spec.py"; txt = open(sp_f).read()
    a = txt.index("YSHORTS = [") if YT else txt.index("SHORTS = ["); b = txt.index("]\n\nDISPLAY") if YT else txt.index("YSHORTS = [")
    blk = txt[a:b]; it = iter(NEW)
    if ONLY: raise SystemExit("FIX needs all shorts of the list")
    blk = re.sub(r"\((\w+), ([0-9.]+), (\.\d+)\)", lambda m: f"({m.group(1)}, {next(it):.2f}, {m.group(3)})", blk)
    open(sp_f, "w").write(txt[:a] + blk + txt[b:]); print("spec rewritten")
