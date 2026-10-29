# CHANNEL 16 — production runbook

One run = one long video (8–12 min, English) + 5 vertical Shorts. Read the Projects doc `claude/channel16-bible.md` first (rules, brand, voice, formats). Episode `episodes/a001-found/` is the reference for structure, pacing and style.

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
python3 $P/short16.py $EP $CL            # 5 Shorts from shorts_spec.py
cd $P && node thumb16.mjs $EP/thumb.json $EP   # thumb_A + thumb_C
```

## 5. QA (do not skip)
- motion_check: 0 issues (repeats, jumps, graphic drift). Re-run on each Short too.
- Contact sheet every 8 s: no gore, no unreadable overlaps, subtitles inside frame, lower thirds sized to text.
- `ffmpeg -i long.mp4 -af ebur128 -f null -` → about −14 LUFS.
- Thumbnail at 168×94: big words still read; nothing in the bottom-right corner.

## 6. Upload + schedule
- Branch = weekday of the ET publish date (`drop-mon` … `drop-sun`), orphan commit with only that day's files, force-push. URL: `https://raw.githubusercontent.com/ituraev97/channel16_media/drop-XXX/<file>`.
- Metricool (brand of CHANNEL 16 — to be created once the channel exists): long 12:00 ET, Shorts 09:00, 11:00, 15:00, 17:00, 21:00 ET; madeForKids false, category EDUCATION.
- Commit `episode.py`, `shorts_spec.py`, `sources.md`, `thumb.json`, `youtube_description.txt`, updated `used_clips.json` and `clips.json` to `main` (never video files).
