#!/usr/bin/env python3
"""Render timeline segments for an episode. usage: build_ep.py <episode_dir> <clips_dir>
episode.py must define LINES (see episodes/001-ms13/episode.py) and META (imgs: {key: path}).
Graphics frames must already exist in <ep>/gfx (node graphics.mjs <ep>/gspec.json <ep>/gfx)."""
import json, os, subprocess, sys, glob, hashlib, importlib.util
EP = os.path.abspath(sys.argv[1]); CLIPS = os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES = E.LINES; IMGS = getattr(E, "META", {}).get("imgs", {})
W, H, FPS = 1920, 1080, 30
CLIPMETA = json.load(open(os.path.join(CLIPS, "clips.json"))) if os.path.exists(os.path.join(CLIPS, "clips.json")) else {}
os.chdir(EP); os.makedirs("seg", exist_ok=True)
def run(c): subprocess.run(c, check=True)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())

vd = []
for i in range(1, len(LINES) + 1):
    raw, out = f"vo/raw_{i:02d}.wav", f"vo/l_{i:02d}.wav"
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw):
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af",
             "highpass=f=70,equalizer=f=140:t=q:w=1:g=3,equalizer=f=3200:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=3:attack=4:release=90,loudnorm=I=-16:TP=-1.5",
             "-ar", "48000", "-ac", "2", out])
    vd.append(dur(out))
starts, t = [], 1.0
for i, (txt, shots, o) in enumerate(LINES):
    starts.append(t); t += vd[i] + o.get("gap", 0.45)
TOTAL = t
print("TOTAL", round(TOTAL, 1), flush=True)

GRADE = ("eq=contrast=1.06:saturation=0.96:gamma=0.98,colorbalance=bs=0.03:bm=0.01:rh=0.02,vignette=angle=PI/5,format=yuv420p")
def gkey(name, opts): return name + "_" + hashlib.md5(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:6]
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS)]

def render(idx, shot, d):
    src, ss, o = shot; n = max(1, int(round(d * FPS)))
    out = f"seg/{idx:03d}.mp4"
    key = hashlib.md5(json.dumps([shot, n, CLIPMETA.get(str(src), {}), GRADE]).encode()).hexdigest()
    if os.path.exists(out) and os.path.exists(out + ".key") and open(out + ".key").read().split()[0] == key:  # cache
        k, ssu = open(out + ".key").read().split(); return out, n / FPS, float(ssu)
    res = _render(idx, shot, d, out, n)
    open(out + ".key", "w").write(f"{key} {res[2]}")
    return res

def _render(idx, shot, d, out, n):
    src, ss, o = shot
    if src.startswith("g:"):
        key = gkey(src[2:], o); frames = sorted(glob.glob(f"gfx/{key}/f*.jpg")); nint = len(frames)
        vf = (f"[0:v]fps={FPS},trim=end_frame={min(n, nint)},setpts=PTS-STARTPTS[a];"
              f"[1:v]loop=loop=-1:size=1,fps={FPS},trim=end_frame={max(0, n - nint) + 1},setsar=1,setpts=PTS-STARTPTS[b];"  # RULE: graphics hold perfectly still after their intro (no zoom/drift -> no jitter)
              f"[a][b]concat=n=2:v=1,trim=end_frame={n},format=yuv420p,fade=t=in:st=0:d=0.2[v]")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"gfx/{key}/f%04d.jpg",
             "-loop", "1", "-i", frames[-1], "-filter_complex", vf, "-map", "[v]", "-frames:v", str(n), "-an"] + ENC + [out])
    elif src.startswith("img:"):
        img = IMGS[src[4:]]; kb = o.get("kb", "in")
        z = "min(zoom+0.0008,1.22)" if kb == "in" else "1.15"
        x = "iw/2-(iw/zoom/2)" if kb == "in" else f"(iw-iw/zoom)*on/{n}"
        # RULE: Ken Burns only on stills, computed on a 4x-supersampled canvas so motion is sub-pixel smooth
        vf = (f"scale=7680:-2,crop=7680:4320,zoompan=z='{z}':x='{x}':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
              f"eq=saturation=0.6,curves=preset=increase_contrast,{GRADE}")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", img, "-vf", vf, "-frames:v", str(n), "-an"] + ENC + [out])
    else:
        clip = f"{CLIPS}/{src}.mp4"
        cd = dur(clip)
        if ss + d > cd - 0.4:  # never run past the end of a clip (end slates / black)
            print(f"WARN clip {src} start {ss} + {d:.1f}s > {cd:.1f}s, clamping", flush=True)
            ss = max(0.0, cd - d - 0.4)
        cuts = CLIPMETA.get(str(src), {}).get("cuts", [])
        def ok(a):  # a window may contain a source cut only if both sides last >= 1.2 s (a real edit, not a flash)
            pts = [a] + [c for c in cuts if a + 0.05 < c < a + d - 0.05] + [a + d]
            return all(pts[k + 1] - pts[k] >= 1.2 for k in range(len(pts) - 1)) if len(pts) > 2 else True
        if not ok(ss):
            cands = [ss + k * 0.25 * sg for k in range(1, 17) for sg in (1, -1)]
            cands = [c for c in cands if 0 <= c <= cd - d - 0.4 and ok(c)]
            if cands: print(f"MOVE clip {src} {ss} -> {cands[0]:.2f} (source cut)", flush=True); ss = cands[0]
            else: print(f"WARN clip {src} @{ss}: crosses a source cut", flush=True)
        box = CLIPMETA.get(str(src), {}).get("box", "iw:ih:0:0")
        src_fps = eval(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", clip]).decode().strip())
        # RULE: 24p sources are motion-interpolated to 30p (plain fps conversion repeats every 4th frame = visible judder)
        rate = f"minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if src_fps < 28 else f"fps={FPS}"
        mode = o.get("mode", "fit")
        if mode == "fill":  # crop the active picture to 16:9 (static crop, vertical position fy 0..1)
            fy = o.get("fy", 0.5)
            vf = (f"crop={box},{rate},crop=iw:min(ih\\,iw*9/16):0:(ih-min(ih\\,iw*9/16))*{fy},"
                  f"scale={W}:{H}:flags=lanczos,setsar=1,{GRADE}")
        else:  # fit: full active picture centred over a blurred, darkened copy of itself (no stretching, no black bars)
            vf = (f"crop={box},{rate},split[a][b];[a]scale=480:270:force_original_aspect_ratio=increase,crop=480:270,gblur=sigma=12,"
                  f"eq=brightness=-0.12:saturation=0.8,scale={W}:{H}:flags=bicubic[bg];[b]scale=-2:{H}:flags=lanczos[fg];"
                  f"[bg][fg]overlay=(W-w)/2:0,setsar=1,{GRADE}")
        # RULE: no artificial zoom/drift on footage (integer-pixel crops/scales make it shake); keep the camera's own motion
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{ss}", "-i", clip, "-t", f"{d + 0.3:.3f}", "-filter_complex", f"[0:v]{vf}[v]",
             "-map", "[v]", "-frames:v", str(n), "-an"] + ENC + [out])
    return out, n / FPS, (ss if not src.startswith(("g:", "img:")) else shot[1])

segs, files, acc, idx = [], [], 0.0, 0
for i, (txt, shots, o) in enumerate(LINES):
    a = 0.0 if i == 0 else starts[i]; b = starts[i + 1] if i + 1 < len(LINES) else TOTAL
    for j, shot in enumerate(shots):
        d = round((a + (b - a) * (j + 1) / len(shots) - acc) * FPS) / FPS
        f, real, ss_used = render(idx, shot, d); files.append(f)
        segs.append(dict(t=acc, d=real, src=shot[0], ss=ss_used, line=i)); acc += real; idx += 1
    print(f"line {i+1}/{len(LINES)}", flush=True)
with open("seg/list.txt", "w") as fh:
    for f in files: fh.write(f"file '{os.path.basename(f)}'\n")
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "seg/list.txt", "-c", "copy", "video_raw.mp4"])
json.dump(dict(starts=starts, vdur=vd, total=TOTAL, segs=segs), open("timing.json", "w"), indent=1)
print("done", round(acc, 2))
