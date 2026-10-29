#!/usr/bin/env python3
"""Compare narrator voices for liveliness. usage: voice_test.py <out_dir>
Metrics per sample: pitch spread (semitones, std of voiced F0), pitch range (p95-p5, st),
energy variation (dB std over 50 ms frames), words per minute, pause share."""
import sys, os, re, json, numpy as np, soundfile as sf, librosa
from kokoro_onnx import Kokoro
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
k = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
TEXT = [
    ("It's just after three in the morning, two miles off an island in Alaska.", "calm"),
    ("His fishing boat is gone.", "punch"),
    ("The life raft he's sitting in is filling with water... and nobody knows he's there.", "tense"),
    ("Except for one thing.", "punch"),
    ("A single call, on channel sixteen.", "slow"),
    ("Forty minutes later, a helicopter from Air Station Sitka is hovering over the rocks, and a rescue swimmer is on the way down.", "drive"),
    ("So how do you find one man, in the dark, in a sea this big?", "question"),
]
SPEED = {"calm": 1.0, "punch": 0.92, "tense": 1.04, "slow": 0.88, "drive": 1.1, "question": 0.96}
PAUSE = {"calm": .35, "punch": .55, "tense": .3, "slow": .7, "drive": .25, "question": .6}

def synth(voice, mode):
    sr = 24000; parts = []
    for t, kind in TEXT:
        sp = 1.06 if mode == "flat" else 1.06 * SPEED[kind]
        a, sr = k.create(t, voice=voice, speed=sp, lang="en-us")
        a, _ = librosa.effects.trim(a, top_db=35)
        parts += [a, np.zeros(int(sr * (0.3 if mode == "flat" else PAUSE[kind])), dtype=np.float32)]
    return np.concatenate(parts), sr

def metrics(a, sr):
    f0, vflag, _ = librosa.pyin(a, fmin=60, fmax=400, sr=sr, frame_length=1024)
    f = f0[vflag & ~np.isnan(f0)]; st = 12 * np.log2(f / np.median(f))
    rms = librosa.feature.rms(y=a, frame_length=1200, hop_length=1200)[0]; db = 20 * np.log10(rms + 1e-6)
    speech = db > db.max() - 35
    words = sum(len(t.split()) for t, _ in TEXT)
    return {"pitch_std_st": round(float(st.std()), 2), "pitch_range_st": round(float(np.percentile(st, 95) - np.percentile(st, 5)), 1),
            "energy_std_db": round(float(db[speech].std()), 2), "wpm": round(words / (len(a) / sr) * 60), "pause_share": round(float(1 - speech.mean()), 2)}

res = {}
for v in ["am_michael", "am_fenrir", "am_onyx", "am_puck", "bm_george", "bm_lewis", "am_eric", "af_heart"]:
    for mode in ["flat", "directed"]:
        if mode == "flat" and v not in ("am_michael",): continue
        a, sr = synth(v, mode); sf.write(f"{out}/{v}_{mode}.wav", a, sr)
        res[f"{v}_{mode}"] = metrics(a, sr); print(v, mode, res[f"{v}_{mode}"], flush=True)
json.dump(res, open(f"{out}/metrics.json", "w"), indent=1)
