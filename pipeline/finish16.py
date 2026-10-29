#!/usr/bin/env python3
"""CHANNEL 16 finishing: subtitles + lower thirds (ASS), synthesized score, SFX, nat sound, final mix (-14 LUFS).
usage: finish16.py <episode_dir> <clips_dir>   (after build_ep.py)"""
import json, os, re, subprocess, sys, importlib.util
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve
EP = os.path.abspath(sys.argv[1]); CLIPS = os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES, DISPLAY = E.LINES, E.DISPLAY
META = getattr(E, "META", {})
os.chdir(EP)
T = json.load(open("timing.json"))
S, V, TOTAL = T["starts"], T["vdur"], T["total"]
SR = 48000
def run(c): subprocess.run(c, check=True)
def disp(t):
    for a, b in DISPLAY: t = t.replace(a, b)
    return t

# ---------------- ASS: subtitles + lower thirds ----------------
def ts(x):
    x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
def chunks(text, maxc=52):
    out = []
    for s in re.split(r"(?<=[.!?:])\s+", text):
        cur = ""
        for w in s.split():
            if len(cur) + len(w) + 1 > maxc and cur: out.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        if cur: out.append(cur)
    m = []
    for c in out:
        if m and len(c) < 14 and len(m[-1]) + len(c) < maxc + 6: m[-1] += " " + c
        else: m.append(c)
    return m
# ASS colours are &HAABBGGRR
FOAM, SONAR, SIGNAL, ABYSS = "&H00F0F2EA", "&H00C5D14F", "&H00145BFF", "&H001F1406"
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Barlow SemiBold,48,{FOAM},&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0.3,0,1,2.2,1.4,2,220,220,56,1
Style: Kick,JetBrains Mono,26,{SONAR},&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,3,0,1,0,0,7,0,0,0,1
Style: Head,Barlow Condensed Black,68,{FOAM},&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,0,0,7,0,0,0,1
Style: Box,Barlow SemiBold,10,&H281F1406,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Credit,JetBrains Mono,22,&H00C8C8C8,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0.5,0,1,1,0,2,80,80,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
def add(a, b, st, tx, layer=0): ev.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{st},,0,0,0,,{tx}")
srt, n = [], 1
def srt_t(x): return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{min(999,int(round((x%1)*1000))):03d}"

def text_w(s, px):  # rough width of condensed caps for the lower-third box
    return int(len(s) * px * 0.335) + 10
for i, (txt, shots, o) in enumerate(LINES):
    is_gfx = all(s[0].startswith("g:") for s in shots)
    cs = chunks(disp(txt)); tot = sum(len(c) for c in cs); a = S[i]
    for c in cs:
        b = a + V[i] * len(c) / tot
        if not is_gfx: add(a, b - 0.02, "Sub", r"{\fad(80,80)}" + c)   # graphics already carry their own text
        srt.append(f"{n}\n{srt_t(a)} --> {srt_t(b)}\n{c}\n"); n += 1
        a = b
    if "tag" in o:  # lower third: orange bar + translucent plate + mono kicker + headline (slides in, then holds still)
        t1, t2 = o["tag"]; a0, b0 = S[i] + 0.25, S[i] + min(V[i] + 0.4, 6.0)
        w = max(text_w(t1, 64), int(len(t2) * 26 * 0.62)) + 64
        mv = r"\move(76,{y},96,{y},0,350)"
        add(a0, b0, "Box", r"{\an7" + mv.format(y=828) + r"\fad(250,300)\bord0\shad0\1c" + ABYSS + r"\1a&H30&\p1}" + f"m 0 0 l {w} 0 l {w} 132 l 0 132" + r"{\p0}", 2)
        add(a0, b0, "Box", r"{\an7" + mv.format(y=828) + r"\fad(250,300)\bord0\shad0\1c" + SIGNAL + r"\1a&H00&\p1}m 0 0 l 10 0 l 10 132 l 0 132{\p0}", 3)
        add(a0, b0, "Kick", r"{\an7" + mv.format(y=846).replace("76", "106").replace("96", "126") + r"\fad(250,300)}" + t2, 3)
        add(a0, b0, "Head", r"{\an7" + mv.format(y=878).replace("76", "106").replace("96", "126") + r"\fad(250,300)}" + t1, 3)
add(TOTAL - 4.2, TOTAL, "Credit", r"{\fad(400,0)}" + META.get("credit", ""), 5)
add(0.6, 7.0, "Credit", r"{\fad(400,400)\an9\pos(1880,40)\fs20}Footage: U.S. Coast Guard via DVIDS · Independent channel, not affiliated with the USCG", 5)
open("subs.ass", "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")
open("subs_en.srt", "w", encoding="utf-8").write("\n".join(srt))

# ---------------- SCORE ----------------
N = int(TOTAL * SR) + SR; t = np.arange(N) / SR
rng = np.random.default_rng(16)
def lp(x, f, o=4): return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "high", fs=SR, output="sos"), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)
irl = int(3.0 * SR); ir = rng.standard_normal(irl) * np.exp(-np.arange(irl) / (0.7 * SR)); ir = lp(ir, 4500); ir /= np.sqrt(np.sum(ir**2)) * 3
def hz(m): return 440 * 2 ** ((m - 69) / 12)
chap = [S[i] for i, (_, sh, _) in enumerate(LINES) if any(s[0] == "g:chapter" for s in sh)]
last = chap[-1] if chap else TOTAL * .85
# chord plan: tense i-VI-III-VII in D minor, the last chapter brightens to VI-III-VII-I(major)
TENSE = [[50, 57, 62, 65], [46, 53, 58, 62], [53, 57, 60, 65], [48, 55, 60, 64]]
BRIGHT = [[46, 53, 58, 62], [53, 57, 60, 65], [48, 55, 60, 64], [50, 57, 62, 66]]
pad = np.zeros(N); CH = 8.0
k = 0
while k * CH < TOTAL:
    a0 = k * CH; prog = BRIGHT if a0 >= last else TENSE; chord = prog[k % 4]
    i0, i1 = int(a0 * SR), min(N, int((a0 + CH + 2.5) * SR)); tt = np.arange(i1 - i0) / SR
    env = np.minimum(1, tt / 2.2) * np.minimum(1, np.maximum(0, (CH + 2.5 - tt) / 2.5))
    seg = np.zeros(i1 - i0)
    for j, m in enumerate(chord):
        for det in (-0.07, 0.07):
            f = hz(m + det)
            seg += (np.sin(2 * np.pi * f * tt) + .35 * np.sin(4 * np.pi * f * tt) + .15 * np.sin(6 * np.pi * f * tt)) * (0.55 if j == 0 else 0.3)
    pad[i0:i1] += seg * env; k += 1
pad = lp(pad, 1500) * (0.75 + 0.25 * np.sin(2 * np.pi * 0.05 * t))
sub = np.sin(2 * np.pi * hz(38) * t) * 0.25 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.031 * t))
# soft ticking "clock" during search/cold/hoist chapters, plucks in the bright ending
clock = np.zeros(N)
def tick():
    L = int(.05 * SR); x = hp(rng.standard_normal(L), 3500) * np.exp(-np.arange(L) / (0.008 * SR)); return x
tense_from, tense_to = (chap[2], chap[5]) if len(chap) >= 6 else (0, 0)
bt = tense_from
while bt < tense_to:
    i0 = int(bt * SR); x = tick() * (0.5 if int(round((bt - tense_from) / 0.5)) % 2 == 0 else 0.28)
    clock[i0:i0 + len(x)] += x[:max(0, min(len(x), N - i0))]; bt += 0.5
pluck = np.zeros(N)
def ks(f, d=1.6, amp=.35):  # soft pluck: decaying harmonics
    L = int(d * SR); tt = np.arange(L) / SR
    x = sum(np.sin(2 * np.pi * f * h * tt) * np.exp(-tt * (2.2 + 1.8 * h)) / h for h in (1, 2, 3, 4))
    return amp * x * np.minimum(1, tt / 0.004)
NOTES = [74, 77, 81, 79, 74, 72, 77, 76]
bt, q = last, 0
while bt < TOTAL - 3:
    x = ks(hz(NOTES[q % len(NOTES)]))
    i0 = int(bt * SR); pluck[i0:i0 + len(x)] += x[:max(0, min(len(x), N - i0))]; bt += 1.0; q += 1
music = pad * .32 + sub * .5 + clock * .22 + pluck * .5
music = music + fftconvolve(music, ir[:int(1.5 * SR)])[:N] * .3
env = np.ones(N); fi = int(3 * SR); env[:fi] *= np.linspace(0, 1, fi)
eo = int((TOTAL - 6) * SR); env[eo:] *= np.linspace(1, 0, N - eo)
# music drops out briefly before "punch" lines so they land in silence
for i, (_, _, o) in enumerate(LINES):
    if o.get("kind") == "punch":
        a0, a1 = int((S[i] - 0.5) * SR), int((S[i] + V[i] + 0.3) * SR)
        ramp = np.ones(max(0, a1 - a0)); r = int(.35 * SR)
        if len(ramp) > 2 * r: ramp[:r] = np.linspace(1, .25, r); ramp[r:-r] = .25; ramp[-r:] = np.linspace(.25, 1, r)
        env[max(0, a0):max(0, a0) + len(ramp)] *= ramp[:N - max(0, a0)]
music *= env

# ---------------- SFX ----------------
fx = np.zeros(N)
def put(x, at):
    i0 = int(max(0, at) * SR); j = min(N, i0 + len(x)); fx[i0:j] += x[:j - i0]
def whoosh(amp=.35, d=.7):
    L = int(d * SR); tt = np.arange(L) / SR; x = bp(rng.standard_normal(L), 300, 3500) * np.sin(np.pi * tt / tt[-1]) ** 2
    return amp * x / np.abs(x).max()
def boom(amp=.7):
    L = int(3 * SR); tt = np.arange(L) / SR; f = 34 * (1 + 2 * np.exp(-tt * 10))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.8); x = x + fftconvolve(x, ir)[:L] * .5
    return amp * x / np.abs(x).max()
def ping(amp=.35, f=1180):
    L = int(2.5 * SR); tt = np.arange(L) / SR; x = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 3.2) + .3 * np.sin(4 * np.pi * f * tt) * np.exp(-tt * 6)
    x = x + fftconvolve(x, ir)[:L] * .7; return amp * x / np.abs(x).max()
def radio(amp=.3, d=.55):  # squelch burst + two-tone beep (VHF feel)
    L = int(d * SR); tt = np.arange(L) / SR
    x = bp(rng.standard_normal(L), 800, 3200) * np.exp(-tt * 5) * .8
    b = int(.12 * SR); beep = np.sin(2 * np.pi * 1800 * np.arange(b) / SR) * .6
    x[int(.2 * SR):int(.2 * SR) + b] += beep; x[int(.35 * SR):int(.35 * SR) + b] += np.sin(2 * np.pi * 1400 * np.arange(b) / SR) * .6
    return amp * x / np.abs(x).max()
def tickfx(amp=.25):
    L = int(.04 * SR); return amp * hp(rng.standard_normal(L), 2500) * np.exp(-np.arange(L) / (.006 * SR))
put(ping(.4), 0.4)
for i, (_, sh, o) in enumerate(LINES):
    names = [s[0] for s in sh]
    if "g:title" in names: put(whoosh(.35, 1.4), S[i] - 0.9); put(boom(.8), S[i] + 0.3); put(ping(.35), S[i] + 0.35)
    if "g:chapter" in names: put(whoosh(.35), S[i] - 0.4); put(boom(.45), S[i] + 0.05)
    if "g:callcard" in names:
        put(radio(.32), S[i] + 0.05)
        rows = next(s[2] for s in sh if s[0] == "g:callcard").get("rows", [])
        for r_ in range(len(rows)): put(tickfx(.3), S[i] + 0.4 + r_ * 0.32)
    if "g:map" in names: put(ping(.28, 980), S[i] + 0.5)
    if "g:stat" in names or "g:cards3" in names or "g:steps" in names: put(whoosh(.22, .5), S[i] - 0.1)
    if "g:end" in names: put(boom(.7), S[i] + 0.4)

# ---------------- VOICE + NAT ----------------
voice = np.zeros(N)
for i, s in enumerate(S):
    x, sr = sf.read(f"vo/l_{i+1:02d}.wav")
    if x.ndim > 1: x = x.mean(1)
    i0 = int(s * SR); voice[i0:i0 + len(x)] += x[:N - i0]
venv = np.convolve(np.abs(voice), np.ones(int(.3 * SR)) / int(.3 * SR), mode="same")
duck = 1 - 0.55 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1)
music *= duck
sf.write("music.wav", (music / max(1e-9, np.abs(music).max()) * .5).astype(np.float32), SR)
sf.write("fx.wav", (fx / max(1e-9, np.abs(fx).max()) * .6).astype(np.float32), SR)
sf.write("voice.wav", (voice / max(1e-9, np.abs(voice).max()) * .9).astype(np.float32), SR)

os.makedirs("nat", exist_ok=True)
lst = open("nat/list.txt", "w")
for k_, sg in enumerate(T["segs"]):
    out = f"nat/{k_:03d}.wav"; src = sg["src"]
    has_a = (not src.startswith(("g:", "img:"))) and subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", f"{CLIPS}/{src}.mp4"], capture_output=True, text=True).stdout.strip()
    if not has_a:
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{sg['d']:.3f}", out])
    else:
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(sg["ss"]), "-i", f"{CLIPS}/{src}.mp4", "-t", f"{sg['d']:.3f}",
             "-af", f"aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,apad,afade=t=in:d=0.08,afade=t=out:st={max(0, sg['d'] - 0.08):.3f}:d=0.08", "-ac", "1", "-t", f"{sg['d']:.3f}", out])
    lst.write(f"file '{k_:03d}.wav'\n")
lst.close()
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "nat/list.txt",
     "-af", "highpass=f=90,lowpass=f=7000,dynaudnorm=f=250:g=15,volume=0.45", "nat.wav"])
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", "voice.wav", "-i", "music.wav", "-i", "fx.wav", "-i", "nat.wav", "-filter_complex",
     "[0:a]aformat=channel_layouts=stereo,asplit[v1][v2];[1:a]aformat=channel_layouts=stereo,volume=0.42[m];[2:a]aformat=channel_layouts=stereo,volume=0.6[f];"
     "[3:a]aformat=channel_layouts=stereo,volume=0.4[n];[n][v2]sidechaincompress=threshold=0.02:ratio=10:attack=20:release=400[nd];"
     "[v1][m][f][nd]amix=inputs=4:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11",
     "-t", f"{TOTAL:.3f}", "-ar", "48000", "mix.wav"])
print("audio + subs done")
