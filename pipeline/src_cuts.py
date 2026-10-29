#!/usr/bin/env python3
"""Find hard cuts inside source clips (incl. FLIR jump-cuts that scdet misses) and store them in <clips>/clips.json as "cuts".
usage: src_cuts.py <clips_dir> [id ...]"""
import sys, os, json, subprocess, numpy as np
CL = os.path.abspath(sys.argv[1]); meta_f = f"{CL}/clips.json"
META = json.load(open(meta_f)) if os.path.exists(meta_f) else {}
ids = sys.argv[2:] or [f[:-4] for f in os.listdir(CL) if f.endswith(".mp4")]
W, H = 160, 90
for cid in ids:
    if "cuts" in META.get(cid, {}) and not sys.argv[2:]: continue
    fps = eval(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", f"{CL}/{cid}.mp4"]).decode())
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", f"{CL}/{cid}.mp4", "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    prev, d = None, []
    while True:
        b = p.stdout.read(W * H)
        if len(b) < W * H: break
        f = np.frombuffer(b, np.uint8).astype(np.float32)
        if prev is not None: d.append(np.abs(f - prev).mean())
        prev = f
    d = np.array(d); cuts = []
    for i in range(len(d)):
        loc = np.median(np.r_[d[max(0, i - 4):i], d[i + 1:i + 5]]) if len(d) > 2 else 0
        if d[i] > 6 and d[i] > 4 * max(loc, 0.8): cuts.append(round((i + 1) / fps, 3))
    META.setdefault(cid, {})["cuts"] = cuts
    print(cid, cuts, flush=True)
json.dump(META, open(meta_f, "w"), indent=1)
