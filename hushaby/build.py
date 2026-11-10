#!/usr/bin/env python3
"""Build one Little Hushaby episode from episodes/<id>/episode.json.
episode.json:
 {"id":"e001-brahms-twinkle", "long": {"seconds":720, "tunes":["brahms","twinkle"], "insts":["musicbox","celesta","harp","piano"],
   "shifts":[0,5,-2,3], "tempo":[76,64], "noise":{"kind":"none"}, "scene":{"char":"bunny","pal":"night","seed":5},
   "thumb":{"l1":"...","l2":"...","badge":"..."}},
  "short": {"tune":"twinkle","inst":"musicbox","tempo":74,"caption":"Twinkle Twinkle\\nLittle Star","scene":{...}}}
Outputs in episodes/<id>/out/: long.mp4, short.mp4, thumb.jpg, + QA sheet.
"""
import json, os, subprocess, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
ep_dir = sys.argv[1]; ep = json.load(open(os.path.join(ep_dir, "episode.json")))
out = os.path.join(ep_dir, "out"); os.makedirs(out, exist_ok=True)
only = sys.argv[2] if len(sys.argv) > 2 else "all"
sh = lambda c: subprocess.run(c, shell=True, check=True, cwd=HERE)

def plan_long(L):
    secs = L["seconds"]; tunes = L["tunes"]; insts = L["insts"]; shifts = L.get("shifts", [0]); t0, t1 = L.get("tempo", [76, 64])
    est_pass = 44.0; n = int(secs / est_pass) + 2
    passes = []
    for i in range(n):
        frac = i / max(1, n - 1)
        inst = insts[i % len(insts)]
        passes.append({"tune": tunes[i % len(tunes)], "inst": inst, "shift": shifts[(i // len(tunes)) % len(shifts)],
                       "tempo": round(t0 + (t1 - t0) * frac, 1), "acc": "celesta" if inst == "harp" else "harp",
                       "octave": 12, "vel": 0.8 - 0.15 * frac, "gap": 3.0})
    return {"seconds": secs, "seed": L.get("seed", 1), "lufs": L.get("lufs", -18), "pad": True, "noise": L.get("noise", {"kind": "none"}),
            "passes": passes, "fade_out": 20}

def loop_video(scene, w, h, name, loop=24, fps=24, crf=24):
    params = dict(scene, w=w, h=h, loop=loop, fps=fps, out=f"frames/{name}", layout="wide" if w > h else "tall")
    sh(f"timeout 1200 node scene.mjs '{json.dumps(params)}'")
    dst = os.path.join(out, f"{name}_loop.mp4")
    sh(f"ffmpeg -v error -y -framerate {fps} -i frames/{name}/f%05d.png -c:v libx264 -preset slow -tune animation -crf {crf} -g {loop*fps} -keyint_min {loop*fps} -sc_threshold 0 -pix_fmt yuv420p {dst}")
    return dst

def mux(loop_mp4, wav, dst, seconds, loop_s, abr):
    """repeat the keyframe-aligned loop with the concat demuxer (stream copy), then add the audio"""
    import math
    reps = math.ceil(seconds / loop_s) + 1
    lst = dst + ".txt"
    with open(lst, "w") as f:
        f.write("".join(f"file '{os.path.abspath(loop_mp4)}'\n" for _ in range(reps)))
    sh(f"ffmpeg -v error -y -f concat -safe 0 -i {lst} -i {wav} -map 0:v -map 1:a -c:v copy -c:a aac -b:a {abr} -t {seconds} -movflags +faststart {dst}")
    os.remove(lst)

if only in ("all", "long"):
    L = ep["long"]
    pl = plan_long(L); json.dump(pl, open(os.path.join(out, "long_plan.json"), "w"), indent=1)
    synth_py = "longsynth.py" if L["seconds"] > 1200 else "synth.py"  # 60-min sleep videos: memory-safe segment renderer
    sh(f"python3 {synth_py} {out}/long_plan.json {out}/long.wav")
    lp = loop_video(L["scene"], 1280, 720, "long", fps=L.get("fps", 24), crf=L.get("crf", 24))
    mux(lp, f"{out}/long.wav", f"{out}/long.mp4", L["seconds"], 24, L.get("abr", "128k"))
    th = dict(L["thumb"], char=L["scene"].get("char", "bunny"), pal=L["scene"].get("pal", "night"), out=f"{out}/thumb.png")
    sh(f"timeout 120 node thumb.mjs '{json.dumps(th)}'")
    sh(f"ffmpeg -v error -y -i {out}/thumb.png -q:v 2 {out}/thumb.jpg")
if only in ("all", "short"):
    S = ep["short"]
    sp = {"seconds": S.get("seconds", 45), "seed": S.get("seed", 2), "lufs": -16, "pad": True, "intro": 1.5, "fade_out": 4,
          "passes": [{"tune": S["tune"], "inst": S["inst"], "tempo": S.get("tempo", 74), "octave": 12, "acc": "harp", "shift": S.get("shift", 0)}]}
    json.dump(sp, open(os.path.join(out, "short_plan.json"), "w"), indent=1)
    sh(f"python3 synth.py {out}/short_plan.json {out}/short.wav")
    lp = loop_video(dict(S["scene"], caption=S["caption"]), 1080, 1920, "short", loop=24, crf=22)
    mux(lp, f"{out}/short.wav", f"{out}/short.mp4", S.get("seconds", 45), 24, "160k")
for f in ("long.mp4", "short.mp4"):
    p = os.path.join(out, f)
    if os.path.exists(p):
        d = subprocess.run(f"ffprobe -v error -show_entries format=duration,size -of csv=p=0 {p}", shell=True, capture_output=True, text=True).stdout.strip()
        print(f, d)
