#!/usr/bin/env python3
"""Directed narration with Kokoro. usage: tts_ep.py <episode_dir> [voice]
Each line's opts['kind'] sets tempo (calm|punch|tense|slow|drive|question); sentences are synthesized
separately and joined with short natural pauses, so the read is not one flat monotone stream.
Writes <ep>/vo/raw_NN.wav (skips existing). Base speed: TTS_SPEED (default 0.97 for am_eric)."""
import sys, os, re, importlib.util, numpy as np, soundfile as sf, librosa
ep = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
voice = sys.argv[2] if len(sys.argv) > 2 else getattr(E, "META", {}).get("voice", "am_eric")
from kokoro_onnx import Kokoro
M = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
BASE = float(os.environ.get("TTS_SPEED", "0.97"))
SPEED = {"calm": 1.0, "punch": 0.93, "tense": 1.04, "slow": 0.9, "drive": 1.08, "question": 0.96}
PAUSE = {"calm": .28, "punch": .42, "tense": .22, "slow": .5, "drive": .18, "question": .4}
os.makedirs(f"{ep}/vo", exist_ok=True)
tot = 0
for i, (t, shots, o) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/raw_{i:02d}.wav"
    if not os.path.exists(f):
        kind = o.get("kind", "calm"); parts = []
        sents = [s for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s]
        for j, s in enumerate(sents):
            sp = BASE * SPEED[kind] * (0.95 if s.endswith("?") else 1.0) * (0.94 if len(s.split()) <= 4 else 1.0)  # short punch lines land slower
            a, sr = k.create(s, voice=voice, speed=sp, lang="en-us")
            a, _ = librosa.effects.trim(a, top_db=38)
            parts.append(a)
            if j < len(sents) - 1: parts.append(np.zeros(int(sr * PAUSE[kind]), dtype=np.float32))
        sf.write(f, np.concatenate(parts), sr)
    a, sr = sf.read(f); tot += len(a) / sr
print("speech seconds:", round(tot, 1))
