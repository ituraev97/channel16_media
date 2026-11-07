# CHANNEL 16 — production runbook

One run = one long video (8–12 min, English) + 5 vertical Shorts (each 62–75 s, posted to YouTube Shorts AND TikTok). Read the Projects doc `claude/channel16-bible.md` first (rules, brand, voice, formats). Episode `episodes/a001-found/` is the reference for structure, pacing and style.

## 1. Setup (fresh container)
```bash
git clone --depth 1 https://github.com/ituraev97/channel16_media /home/claude/channel16_media   # add_repo owner=ituraev97 repo=channel16_media access=push first
cd /home/claude/channel16_media/pipeline && npm i
pip install --break-system-packages kokoro-onnx soundfile scipy fonttools brotli librosa
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
cd /home/claude/channel16_media/pipeline/node_modules/@fontsource && mkdir -p ~/.fonts && python3 -c "
from fontTools.ttLib import TTFont; import os
for s,d in [('barlow-condensed/files/barlow-condensed-latin-900-normal.woff2','BarlowCondensed-Black.ttf'),('barlow-condensed/files/barlow-condensed-latin-800-normal.woff2','BarlowCondensed-ExtraBold.ttf'),('barlow/files/barlow-latin-600-normal.woff2','Barlow-SemiBold.ttf'),('jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2','JetBrainsMono-Bold.ttf')]:
  f=TTFont(s); f.flavor=None; f.save(os.path.expanduser('~/.fonts/'+d))" && fc-cache -f
mkdir -p /home/claude/clips && cp /home/claude/channel16_media/clips.json /home/claude/clips/
```

## 2. Pick the rescues
- DVIDS API (key in the scheduled-task prompt): `https://api.dvidshub.net/search?api_key=KEY&q=coast%20guard%20rescue&type[]=video&sort=date` → `asset?id=video:ID` → download the 1920x1080 file to `/home/claude/clips/ID.mp4`.
- Never reuse a clip already in `used_clips.json` for a Shorts story. Skip anything with injuries in close-up, bodies, or a possible self-harm situation.
- Add the clip's active picture area to `clips.json` (`box`, e.g. "1440:1080:240:0" for 4:3), then `python3 pipeline/src_cuts.py /home/claude/clips ID` (internal cuts; the builder avoids flash fragments automatically).
- Contact sheet every 3 s with timestamps to choose shots.

## 3. Research + script
- Facts only from pages actually opened (DVIDS description/news, USCG press release, local news). Save `sources.md` (claim → URL).
- `episode.py`: `LINES = [(spoken, shots, opts)]`, opts: `kind` (calm|punch|tense|slow|drive|question), `tag` (place, date lower third), `gap`. Numbers as words; hard names respelled + `DISPLAY` map.
- Graphics (`pipeline/graphics.mjs`): title, chapter, stat, callcard (radio log rows), steps, cards3, map (bounds, rings, arcs, cities), timeline, list, end.
- Footage must never pretend to be a different event; general claims (death, hypothermia) go on graphics, not over real rescued people.
- Independent fact-check by a separate agent before building. Fix everything it finds.

## 4. Build
```bash
EP=/home/claude/channel16_media/episodes/NNN-slug; P=/home/claude/channel16_media/pipeline; CL=/home/claude/clips
python3 $P/tts_ep.py $EP                 # voice am_eric, directed per line
cd $P && python3 make_gspec.py $EP && node graphics.mjs $EP/gspec.json $EP/gfx
python3 $P/build_ep.py $EP $CL           # 24p clips are motion-interpolated (slow) — run in background; segments are cached
python3 $P/motion_check.py $EP/video_raw.mp4 $EP/timing.json $CL/clips.json   # must report 0 issues
python3 $P/finish16.py $EP $CL           # subtitles, lower thirds, score, SFX, nat sound, -14 LUFS
bash $P/encode.sh $EP $EP/long.mp4 95    # < 100 MB for GitHub
python3 $P/plan_shorts.py $EP $CL         # plan shot windows first (FIX=1 re-packs starts: no OVERLAP/END/FRAG); PLATFORM=youtube for YSHORTS
python3 $P/short16.py $EP $CL            # 5 TikTok Shorts from shorts_spec.py — each must run >= 61.5 s (script refuses shorter)
python3 $P/short16.py $EP $CL --platform youtube   # YouTube Shorts y1–y3 from YSHORTS: 15–30 s, CTA = YCTA; a line may add dict(label=...) to caption what the footage is
cd $P && node thumb16.mjs $EP/thumb.json $EP   # thumb_A + thumb_C
```

## Shorts for TikTok monetization (owner rule, Nov 2026)
- TikTok Creator Rewards pays only for videos over 1 minute, so every Short is 62–75 s: about 200–230 spoken words, 13–16 lines, 20–28 shots, ONE rescue told as a mini case (hook question → what happened → the call → conditions → the search/approach → the hoist → outcome → one survival lesson → "Follow for more real rescues"). Never pad with silence, freeze frames or repeated shots — the length must come from real story beats.
- Hook in the first 1.5 s (on-screen hook text + the most dramatic shot). Something new on screen every 2–3 s.
- TikTok safe zones: nothing important below y 1440 or right of x 940 between y 700–1700; captions centre at y≈1240, CTA at y≈1060.

## 5. QA (do not skip)
- motion_check: 0 issues (repeats, jumps, graphic drift). Phone/FLIR sources with duplicated frames: make a de-duplicated copy (mpdecimate + minterpolate) under a new id (939855d, 1014541g). Re-run on each Short too, and ffprobe each Short: duration must be ≥ 61.5 s.
- Contact sheet every 8 s: no gore, no unreadable overlaps, subtitles inside frame, lower thirds sized to text.
- `ffmpeg -i long.mp4 -af ebur128 -f null -` → about −14 LUFS.
- Thumbnail at 168×94: big words still read; nothing in the bottom-right corner.

## 6. Upload + schedule
- Branch = weekday of the ET publish date (`drop-mon` … `drop-sun`), orphan commit with only that day's files, force-push. URL: `https://raw.githubusercontent.com/ituraev97/channel16_media/drop-XXX/<file>`.
- Metricool brand CHANNEL 16 = blogId 7743228 (YouTube + TikTok @channel16rescues): long 12:00 ET (YouTube only), Shorts 09:00, 11:00, 15:00, 17:00, 21:00 ET; madeForKids false, category EDUCATION.
- Each Short = ONE post with providers [youtube, tiktok]; tiktokData {title (≤90 chars), privacyOption PUBLIC_TO_EVERYONE, disableComment false, disableDuet false, disableStitch false, autoAddMusic false, isAigc false}; videoCoverMilliseconds 1500. If the combined post is rejected, make two posts (one per network) for the same time.
- Commit `episode.py`, `shorts_spec.py`, `sources.md`, `thumb.json`, `youtube_description.txt`, updated `used_clips.json` and `clips.json` to `main` (never video files).
