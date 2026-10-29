#!/usr/bin/env python3
"""CHANNEL 16 vertical Shorts (1080x1920), one rescue each, own narration.
usage: short16.py <episode_dir> <clips_dir> [id ...]   reads <ep>/shorts_spec.py (SHORTS, DISPLAY, CTA)
Footage: static 9:16 crop of the active picture (no zoom/drift), 24p sources motion-interpolated to 30p.
Audio: directed Kokoro narration + light score + SFX, -14 LUFS. Captions: 2-3 words, centre-low, inside safe zones."""
import os, re, sys, json, subprocess, importlib.util, numpy as np, soundfile as sf, librosa
from scipy.signal import butter, sosfilt, fftconvolve
EP, CLIPS = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); ONLY = set(sys.argv[3:])
sp = importlib.util.spec_from_file_location("ss", f"{EP}/shorts_spec.py"); SS = importlib.util.module_from_spec(sp); sp.loader.exec_module(SS)
META = json.load(open(f"{CLIPS}/clips.json"))
W, H, FPS, SR = 1080, 1920, 30, 48000
from kokoro_onnx import Kokoro
K = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
VOICE = os.environ.get("VOICE", "am_eric"); BASE = float(os.environ.get("TTS_SPEED", "1.0"))  # Shorts run a touch faster than long-form
SPEED = {"calm": 1.0, "punch": 0.93, "tense": 1.04, "slow": 0.92, "drive": 1.08, "question": 0.96}
PAUSE = {"calm": .22, "punch": .38, "tense": .18, "slow": .4, "drive": .15, "question": .35}
GRADE = "eq=contrast=1.06:saturation=0.98:gamma=0.98,colorbalance=bs=0.03:rh=0.02,vignette=angle=PI/5,format=yuv420p"
def run(c): subprocess.run(c, check=True)
def disp(t):
    for a, b in SS.DISPLAY: t = t.replace(a, b)
    return t
def ts(x): x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
def lp(x, f): return sosfilt(butter(4, f, "low", fs=SR, output="sos"), x)
def hp(x, f): return sosfilt(butter(2, f, "high", fs=SR, output="sos"), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)
def fps_of(clip): return eval(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", clip]).decode().strip())

HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,Barlow Condensed Black,112,&H00F0F2EA,&H00FFFFFF,&H001F1406,&H00000000,0,0,0,0,100,100,1,0,1,7,0,8,70,70,250,1
Style: Cap,Barlow Condensed Black,96,&H00F0F2EA,&H00FFFFFF,&H001F1406,&H00000000,0,0,0,0,100,100,1,0,1,7,0,5,70,70,0,1
Style: Hud,JetBrains Mono,34,&H00F0F2EA,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,2,0,1,2,0,7,0,0,0,1
Style: Small,JetBrains Mono,24,&H00C8C8C8,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0.5,0,1,1.5,0,2,60,60,150,1
Style: CTA,Barlow Condensed Black,64,&H003CC9FF,&H00FFFFFF,&H001F1406,&H00000000,0,0,0,0,100,100,2,0,1,5,0,5,60,60,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
def chunks(text):  # 2-3 word caption chunks, breaking at punctuation
    out, cur = [], []
    for w in text.split():
        cur.append(w)
        if len(cur) == 3 or re.search(r"[.,!?]$", w) and len(cur) >= 2: out.append(" ".join(cur)); cur = []
    if cur: out.append(" ".join(cur))
    return out

os.makedirs(f"{EP}/shorts", exist_ok=True)
for sh in SS.SHORTS:
    if ONLY and sh["id"] not in ONLY: continue
    wd = f"{EP}/shorts/{sh['id']}"; os.makedirs(wd, exist_ok=True)
    # ---- narration
    vo, starts, durs, t = [], [], [], 0.35
    for li, (txt, shots, kind) in enumerate(sh["lines"]):
        parts = []
        sents = [s for s in re.split(r"(?<=[.!?])\s+", txt) if s]
        for j, s in enumerate(sents):
            a, _ = K.create(s, voice=VOICE, speed=BASE * SPEED[kind] * (0.94 if len(s.split()) <= 4 else 1), lang="en-us")
            a, _ = librosa.effects.trim(a, top_db=38); parts.append(a)
            if j < len(sents) - 1: parts.append(np.zeros(int(24000 * PAUSE[kind]), np.float32))
        a = librosa.resample(np.concatenate(parts), orig_sr=24000, target_sr=SR)
        starts.append(t); durs.append(len(a) / SR); vo.append(a); t += len(a) / SR + (0.45 if kind in ("punch", "slow") else 0.28)
    TOTAL = t + 1.6
    # ---- picture: static 9:16 crops, cut points spread evenly over each line
    segs, acc = [], 0.0
    for li, (txt, shots, kind) in enumerate(sh["lines"]):
        a0 = 0.0 if li == 0 else starts[li]; b0 = starts[li + 1] if li + 1 < len(starts) else TOTAL
        for j, (cid, ss, cx) in enumerate(shots):
            d = round((a0 + (b0 - a0) * (j + 1) / len(shots) - acc) * FPS) / FPS
            clip = f"{CLIPS}/{cid}.mp4"; box = META.get(str(cid), {}).get("box", "iw:ih:0:0")
            cuts = META.get(str(cid), {}).get("cuts", []); cdur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", clip]))
            def ok(a):  # never include a <1.2 s fragment of a source shot (reads as a glitch)
                pts = [a] + [c for c in cuts if a + 0.05 < c < a + d - 0.05] + [a + d]
                return all(pts[k + 1] - pts[k] >= 1.2 for k in range(len(pts) - 1))
            if not ok(ss):
                cands = [c for c in (ss + k * 0.25 * sg for k in range(1, 17) for sg in (1, -1)) if 0 <= c <= cdur - d - 0.4 and ok(c)]
                if cands: print(f"MOVE {cid} {ss} -> {cands[0]:.2f}", flush=True); ss = cands[0]
            rate = f"minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if fps_of(clip) < 28 else f"fps={FPS}"
            vf = (f"crop={box},crop=min(iw\\,ih*9/16):ih:(iw-min(iw\\,ih*9/16))*{cx}:0,{rate},scale={W}:{H}:flags=lanczos,setsar=1,{GRADE}")
            out = f"{wd}/v{len(segs):02d}.mp4"; n = int(round(d * FPS))
            run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(ss), "-i", clip, "-t", f"{d + 0.3:.3f}", "-vf", vf, "-frames:v", str(n), "-an",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), out])
            segs.append(dict(f=out, t=acc, d=n / FPS, src=str(cid), ss=ss)); acc += n / FPS
    open(f"{wd}/list.txt", "w").write("".join(f"file '{os.path.basename(s['f'])}'\n" for s in segs))
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{wd}/list.txt", "-c", "copy", f"{wd}/raw.mp4"])
    # ---- captions + hook + HUD
    ev = []
    hook = re.sub(r"\[(.+?)\]", r"{\\c&H145BFF&}\1{\\c&HF0F2EA&}", sh["hook"].replace("<br>", r"\N"))
    ev.append(f"Dialogue: 4,{ts(0)},{ts(TOTAL)},Hook,,0,0,0,,{{\\fad(120,0)\\t(0,180,\\fscx100\\fscy100)\\fscx112\\fscy112}}{hook}")
    ev.append(f"Dialogue: 4,{ts(0)},{ts(TOTAL)},Hud,,0,0,0,,{{\\an7\\pos(70,120)}}{{\\c&H145BFF&}}●{{\\c&HF0F2EA&}} CH 16 · REAL RESCUE")
    for li, (txt, _, _) in enumerate(sh["lines"]):
        cs = chunks(disp(txt)); tot = sum(len(c) for c in cs); s = starts[li]
        for c in cs:
            e = s + durs[li] * len(c) / tot
            ev.append(f"Dialogue: 3,{ts(s)},{ts(e - 0.01)},Cap,,0,0,0,,{{\\an5\\pos(540,1240)\\fscx90\\fscy90\\t(0,80,\\fscx100\\fscy100)}}{c.upper()}")
            s = e
    ev.append(f"Dialogue: 5,{ts(TOTAL - 2.2)},{ts(TOTAL)},CTA,,0,0,0,,{{\\an5\\pos(540,1480)\\fad(200,0)}}{SS.CTA}")
    ev.append(f"Dialogue: 5,{ts(0.4)},{ts(5.5)},Small,,0,0,0,,{{\\fad(300,300)}}Footage: U.S. Coast Guard via DVIDS · not affiliated with the USCG")
    open(f"{wd}/subs.ass", "w", encoding="utf-8").write(HEAD + "\n".join(ev) + "\n")
    # ---- audio: voice + light score + sfx + nat
    N = int(TOTAL * SR) + SR; tt = np.arange(N) / SR; rng = np.random.default_rng(int(sh["id"][1:]))
    voice = np.zeros(N)
    for s0, a in zip(starts, vo): i0 = int(s0 * SR); voice[i0:i0 + len(a)] += a[:N - i0]
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    chords = [[50, 57, 62, 65], [46, 53, 58, 62], [53, 57, 60, 65], [48, 55, 60, 64]]
    pad = np.zeros(N)
    for k, c0 in enumerate(np.arange(0, TOTAL, 4.0)):
        i0, i1 = int(c0 * SR), min(N, int((c0 + 5.5) * SR)); x = np.arange(i1 - i0) / SR
        env = np.minimum(1, x / 1.2) * np.minimum(1, np.maximum(0, (5.5 - x) / 1.5))
        pad[i0:i1] += sum(np.sin(2 * np.pi * hz(m + d) * x) * (.5 if q == 0 else .28) for q, m in enumerate(chords[k % 4]) for d in (-.07, .07)) * env
    pad = lp(pad, 1400)
    clock = np.zeros(N); L = int(.04 * SR)
    for b in np.arange(0.35, TOTAL - 1.5, 0.5):
        i0 = int(b * SR); clock[i0:i0 + L] += hp(rng.standard_normal(L), 3500) * np.exp(-np.arange(L) / (.006 * SR)) * (.5 if int(b * 2) % 2 == 0 else .3)
    music = pad * .3 + clock * .2
    ir = rng.standard_normal(int(2 * SR)) * np.exp(-np.arange(int(2 * SR)) / (.5 * SR)); ir = lp(ir, 4000); ir /= np.sqrt((ir ** 2).sum()) * 3
    music = music + fftconvolve(music, ir)[:N] * .3
    env = np.ones(N); env[:int(.4 * SR)] = np.linspace(0, 1, int(.4 * SR)); env[int((TOTAL - 1.5) * SR):] *= np.linspace(1, 0, N - int((TOTAL - 1.5) * SR))
    venv = np.convolve(np.abs(voice), np.ones(int(.3 * SR)) / int(.3 * SR), mode="same")
    music *= env * (1 - .55 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1))
    fx = np.zeros(N)
    Lw = int(.6 * SR); x = np.arange(Lw) / SR; wh = bp(rng.standard_normal(Lw), 300, 3500) * np.sin(np.pi * x / x[-1]) ** 2
    for s in segs[1:]: i0 = int(max(0, s["t"] - .3) * SR); fx[i0:i0 + Lw] += wh[:N - i0] * .12
    Lb = int(2 * SR); x = np.arange(Lb) / SR; boom = np.sin(2 * np.pi * np.cumsum(34 * (1 + 2 * np.exp(-x * 10))) / SR) * np.exp(-x * 2)
    fx[:Lb] += boom * .6
    sf.write(f"{wd}/voice.wav", voice.astype(np.float32), SR); sf.write(f"{wd}/music.wav", (music / (np.abs(music).max() + 1e-9) * .5).astype(np.float32), SR)
    sf.write(f"{wd}/fx.wav", (fx / (np.abs(fx).max() + 1e-9) * .6).astype(np.float32), SR)
    nat = []
    for k, s in enumerate(segs):
        o = f"{wd}/n{k:02d}.wav"
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(s["ss"]), "-i", f"{CLIPS}/{s['src']}.mp4", "-t", f"{s['d']:.3f}",
             "-af", f"aresample={SR},pan=mono|c0=0.5*c0+0.5*c1,apad,afade=t=in:d=0.06,afade=t=out:st={max(0, s['d'] - .06):.3f}:d=0.06", "-ac", "1", "-t", f"{s['d']:.3f}", o])
        nat.append(o)
    open(f"{wd}/nat.txt", "w").write("".join(f"file '{os.path.basename(o)}'\n" for o in nat))
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{wd}/nat.txt", "-af", "highpass=f=90,dynaudnorm=f=250:g=15,volume=0.45", f"{wd}/nat.wav"])
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f"{wd}/voice.wav", "-i", f"{wd}/music.wav", "-i", f"{wd}/fx.wav", "-i", f"{wd}/nat.wav", "-filter_complex",
         "[0:a]highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=4:release=90,aformat=channel_layouts=stereo,asplit[v1][v2];"
         "[1:a]aformat=channel_layouts=stereo,volume=0.42[m];[2:a]aformat=channel_layouts=stereo,volume=0.6[f];[3:a]aformat=channel_layouts=stereo,volume=0.4[n];"
         "[n][v2]sidechaincompress=threshold=0.02:ratio=10:attack=20:release=400[nd];[v1][m][f][nd]amix=inputs=4:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11",
         "-t", f"{TOTAL:.3f}", "-ar", str(SR), f"{wd}/mix.wav"])
    out = f"{EP}/shorts/{sh['id']}.mp4"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f"{wd}/raw.mp4", "-i", f"{wd}/mix.wav",
         "-vf", f"tpad=stop_mode=clone:stop_duration=2,ass={wd}/subs.ass,fade=t=out:st={TOTAL - 0.4:.2f}:d=0.4", "-t", f"{TOTAL:.3f}",
         "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    json.dump(dict(total=TOTAL, segs=[dict(t=s["t"], d=s["d"], src=s["src"], ss=s["ss"]) for s in segs]), open(f"{wd}/timing.json", "w"))
    print(sh["id"], round(TOTAL, 1), "s ->", out, flush=True)
