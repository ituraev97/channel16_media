#!/usr/bin/env python3
"""QA for a built episode: durations, loudness/true peak, loop seam, contact sheets, spectrogram, silence gaps.
usage: qa.py episodes/<id>   -> prints a report and writes out/qa_*.png"""
import os, sys, subprocess, re, json
import numpy as np
from PIL import Image
d = os.path.join(sys.argv[1], "out")
run = lambda c: subprocess.run(c, shell=True, capture_output=True, text=True)
ok = True
for name, lo, hi, l_lo, l_hi in (("long", None, None, -20, -16), ("short", 30, 58, -17.5, -14.5)):
    p = f"{d}/{name}.mp4"
    if not os.path.exists(p): continue
    dur = float(run(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {p}").stdout)
    size = os.path.getsize(p) / 1e6
    r = run(f"ffmpeg -nostats -i {p} -af ebur128=peak=true -f null -").stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])
    flags = []
    if lo and not (lo <= dur <= hi): flags.append("DURATION")
    if not (l_lo <= I <= l_hi): flags.append("LOUDNESS")
    if TP > -1.0: flags.append("TRUE-PEAK")
    if size > 95: flags.append("SIZE>95MB")
    # silence gaps > 4 s (excluding last 25 s fade)
    sil = run(f"ffmpeg -nostats -i {p} -af silencedetect=n=-55dB:d=4 -f null -").stderr
    gaps = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", sil) if float(x) < dur - 25 and float(x) > 1]
    if gaps: flags.append(f"SILENCE@{gaps[:3]}")
    print(f"{name}: {dur:.1f}s {size:.1f}MB I={I} LUFS TP={TP} dBFS {'OK' if not flags else ' '.join(flags)}")
    ok &= not flags
    # contact sheet
    n = 8; ts = [dur * k / (n - 1) * 0.98 + 0.5 for k in range(n)]
    tiles = []
    for k, t in enumerate(ts):
        run(f"ffmpeg -v error -y -ss {t:.2f} -i {p} -frames:v 1 -vf scale=480:-2 {d}/_t{k}.png")
        tiles.append(Image.open(f"{d}/_t{k}.png"))
    tw, th = tiles[0].size; cols = 4
    sheet = Image.new("RGB", (tw * cols, th * ((n + cols - 1) // cols)))
    for k, im in enumerate(tiles): sheet.paste(im, ((k % cols) * tw, (k // cols) * th)); os.remove(f"{d}/_t{k}.png")
    sheet.save(f"{d}/qa_{name}_sheet.png")
    # loop seam
    lp = f"{d}/{name}_loop.mp4"
    raw = subprocess.run(f"ffmpeg -v error -i {lp} -vf scale=192:108,format=gray -f rawvideo -", shell=True, capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, 108, 192).astype(float)
    seam = np.abs(fr[-1] - fr[0]).mean(); step = np.median(np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2)))
    print(f"  loop seam diff {seam:.2f} (typical frame step {step:.2f}) {'OK' if seam < max(2, 3 * step) else 'SEAM!'}")
    ok &= seam < max(2, 3 * step)
# spectrogram of first 40 s of the long audio
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
for name in ("long", "short"):
    w = f"{d}/{name}.wav"
    if not os.path.exists(w): continue
    from scipy.io import wavfile
    sr, x = wavfile.read(w); x = x[: sr * 40, 0].astype(float) / 32767
    plt.figure(figsize=(12, 3.5)); plt.specgram(x + 1e-9, NFFT=4096, Fs=sr, noverlap=3072, cmap="magma"); plt.ylim(0, 4000); plt.tight_layout()
    plt.savefig(f"{d}/qa_{name}_spec.png", dpi=60); plt.close()
print("QA", "PASS" if ok else "FAIL")
