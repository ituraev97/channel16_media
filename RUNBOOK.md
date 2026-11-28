# CHANNEL 16 — production runbook

> - **VOICE RULES (owner 2026-11-28): work HARD on intonation, pace and pronunciation; this channel has its OWN voice — Kokoro am_eric (directed per line). Never use another channel's voice.**
>   Intonation: give every line a tone/energy (≈25% energetic on reveals, numbers, verdicts; ≈15% calm for context; rest normal); short sentences of varied length, the key word at the end, commas where a speaker breathes; never one flat tone for a whole video. After voicing measure the take: pitch variation ≥ 4 semitones, loudness range ≥ 6 LU — re-voice a flat take.
>   Pace: long narration 150–165 wpm (sleep content excepted: keep its slow pace), Shorts 160–180 wpm; never speed long narration up to fit a duration — cut words; no silence > 0.6 s except one deliberate beat (sleep pipeline: its verse pauses stay).
>   Pronunciation: numbers, dates, money, units written out in words in the TTS text; every unclear name/place/foreign word gets a phonetic respelling for the voice only (real spelling in captions/titles); keep them in `voice_lexicon.md` and reuse them; acronyms as letters with hyphens (F-B-I) unless said as a word. Speech-recognition check: any misread name → re-voice before rendering.


> **LATEST OWNER DECISIONS — read first, they override older sections below (2026-11-24)**
> - Thumbnails v6 (section "Thumbnails v6" near the end): thumb_A and thumb_B are made with `tools/thumbkit/thumbkit.py` + AI pictures from `tools/img_client.py` (request them at the START of the run); only thumb_C uses this channel's old generator. Every run must at least request the AI pictures; if they do not arrive in time, say so in the report.
> - EMOTION FIRST: every thumbnail shows a strong emotion (rage, shock, fear, disbelief) — never a calm face; the AI may only re-light a real face, never change it.
> - Promise rule + subtitles + minimal bleeps (section "Promise, clips & subtitles" at the end).
> - VOICE PACE (owner 2026-11-24: "the voice speeds up and talks too fast"): long-form narration is NEVER sped up — `speed`/`tempo`/`tempos` ≤ 1.0 for the long video (the relay now clamps long-form to 1.0 and Shorts to 1.10). Target 150–165 words per minute: budget ≈ 155 words per minute of narration when you size the script, short sentences, commas where a speaker breathes; do not cram to hit a duration — cut words instead.


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
- Military-hardware TikToks (from Nov 10, 2026): TikTok-only episode folder `episodes/mNNN-<slug>/` with only `shorts_spec.py` (SHORTS, YSHORTS = [], DISPLAY, CTA, HUD, CREDIT) + `sources.md` + `dvids/` descriptions; build with `plan_shorts.py` + `short16.py` directly (no long video). Rules: Projects doc `claude/channel16-tiktok-military-bible.md`. Hosting branch `tiktok-<weekday>`, providers tiktok ONLY (YouTube = Little Hushaby).
- TikTok Creator Rewards pays only for videos over 1 minute, so every Short is 62–75 s: about 200–230 spoken words, 13–16 lines, 20–28 shots, ONE rescue told as a mini case (hook question → what happened → the call → conditions → the search/approach → the hoist → outcome → one survival lesson → "Follow for more real rescues"). Never pad with silence, freeze frames or repeated shots — the length must come from real story beats.
- Hook in the first 1.5 s (on-screen hook text + the most dramatic shot). Something new on screen every 2–3 s.
- TikTok safe zones: nothing important below y 1440 or right of x 940 between y 700–1700; captions centre at y≈1240, CTA at y≈1060. short16.py condenses caption chunks longer than 24 characters (\fscx) so they stay inside x ≤ 940 (Nov 10, 2026).
- src_cuts.py can miss soft cuts and dissolves (seen in 995774, 1009153) and can flag muzzle flashes as cuts: check motion_check JUMPs frame by frame, add missed cuts to clips.json and remove flash 'cuts' inside a continuous firing shot.

## Performance rules
Weekly review (Mondays). Source: Metricool TikTok post metrics (TKPO02/05/06/07; TKPO15 avg watch time still not returned), last 28 days. Each rule is backed by >= 3 videos; rules are recommendations, not schedule or content-rule changes. Data 2026-11-16: 23 mature military videos (Nov 10–14, median 241 views, mean 295) vs 18 rescue videos (Nov 4–8, median 310).
1. Guns and cannons firing win: M777 583, Mk 45 410, A-10 GAU-8 388, Abrams 387, HIMARS 348 (median of all gun/cannon/rocket-artillery videos 387, n=7 incl. Paladin 200, Bradley 217). Make at least two of the five daily videos a gun/cannon/artillery firing.
2. Missile launches and missile-defense tests are the weakest: THAAD 174, Trident 154, SM-2 130, Patriot 209, Minuteman 231 (median 174, n=5; all at or below the overall median). Max one missile/missile-defense video per day, and not in the 15:00 slot.
3. Bombers beat fighter demos: B-2 refueling 895, B-52H 397, B-1B 288 (median 397, n=3) vs F-35B 148, F-22 186, CV-22 209 (median 186, n=3). Prefer heavy aircraft with an unusual view (tanker boom, cockpit, deck) over fighter flybys.
4. Length is not the driver for military: 62–67 s median 348 (n=5), 68–71 s 241 (n=7), 72–75 s 209 (n=11). Last week's "longer wins" did not hold; stop stretching to 75 s — 64–72 s is fine, as long as every beat is real.
5. Slots matter little: medians 09:00 209 (n=3), 11:00 217 (n=5), 15:00 288 (n=5), 17:00 260 (n=5), 21:00 241 (n=5). Keep the strongest system at 15:00 (still the best median) and the second strongest at 21:00 (two of the top four).
Dropped: "themed run" and "unusual camera + number" rules (rescue-era, not testable on military data yet).
Caveats: each day's views are 1–6 days old at review time; small samples; categories overlap (A-10 counted as gun). Recheck next Monday.

Changelog
- 2026-11-09: first version from 16 rescue TikToks (median 265 views); no military data yet.
- 2026-11-16: rewritten from 23 military TikToks (Nov 10–14): guns/cannons > bombers > others > missiles; length rule dropped.

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

## Thumbnails v6 — YouTube-AI style: AI picture + real text/documents (owner decision 2026-11-23)
Owner: "make them like the thumbnails YouTube Studio's AI draws — bright, illustrated, with brands". This section overrides the **thumb_A and thumb_B** parts of the earlier thumbnail rules; thumb_C keeps the current generator, so YouTube Studio → Test & Compare measures the new style. Earlier content rules stay: lawful image sources, every word true and sourced, fact-check of thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

0. **EMOTION FIRST (owner 2026-11-24):** every thumbnail must show a strong emotion at first glance (rage, shock, fear, disbelief) — never a calm or smiling face. Pick the PEAK real frame/photo, let the AI dramatize light/smoke/contrast while keeping the exact face and expression; if no emotional real frame exists, put the emotion into the scene (fire, sirens, red stamp). Details: STYLE.md "EMOTION FIRST".
1. Read `tools/thumbkit/STYLE.md` — templates learned from YouTube's own AI thumbnails: doc (documentary split), evidence/fraud (object + real document + stamp), ntsb (full-bleed reconstruction + telemetry HUD + red circle), mugshot (real face + seized items, soft seam), versus, solo. Pick the template that fits this channel's examples.
2. AI pictures (free, FLUX.2 klein on the owner's office PC) via Drive "IMG RELAY" — request EARLY in the run (≈ 12 min per picture, longer while the PC voices — at most 3 pictures per run):
   `python3 tools/img_client.py request <ID> plates.json --creds /tmp/drive_creds.json` then later `python3 tools/img_client.py wait <ID> <ep>/plates --creds /tmp/drive_creds.json --timeout 2400`.
   plates.json = `[{"name":"plate_A.png","prompt":"cinematic photo of ..., dramatic side light, dark background, high detail","w":1280,"h":720,"seed":1}, ...]` (max 6). The AI paints ONLY pictures — NEVER ask it for text, documents, logos-as-evidence. Real people: send their REAL lawful photo as `"ref"` (edit mode: "same person, same expression, re-lit with red and blue police lights, sharp, cinematic") — never generate a real person from text.
   No answer in time → build A/B with real frames (thumbkit solo/versus) and say so in the report.
3. Compose with `tools/thumbkit/thumbkit.py <ep>/thumbkit.json` (setup: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"`; header lists every layout and overlay: tag, ribbon, hud, circle, path, stamp, bignum, pill, label, band). Text, numbers, stamps and the REAL document crop are drawn by thumbkit — documents come only from the real source (PDF page → `doc`, `highlights` boxes in its pixels).
4. LOOK at every thumb at full size and at 320 px: AI picture has no garbage text/extra fingers/melted objects, faces unchanged, words readable. Bad picture → new seed/prompt (one retry), otherwise fall back to the real-frame layout.

CHANNEL 16 notes: Drive creds for the relay = the same OAuth JSON the other cloud channels use (Projects doc `claude/google-drive-oauth.md` → /tmp/drive_creds.json, never into git). Best templates here: "ntsb"-style full-bleed rescue reconstruction (helicopter hoist over storm sea, cutter in heavy waves) + `hud` with real case numbers (WIND 45 KT / SEAS 18 FT / SURVIVORS 4) + red `tag` ("USCG RESCUE", "MAYDAY"). Real crew/survivor faces only from official USCG photos/video (edit mode), never generated.

## Promise, clips & subtitles (owner decision 2026-11-24 — lesson from HOTFIX comments: "baited by title, talks about it for 2 seconds", "censors so much you can't tell what he's saying", "ai slop")
- **Promise rule:** the moment the title + thumbnail promise (the arrest, the verdict, the crash, the confession, the number) must appear IN FULL within the first 60 s — the real clip/document/audio, not a 2-second tease — and that story takes ≥ 25 % of the runtime. The title describes what the video is mostly about; never sell one moment that only pays off near the end. Shorts: the hook's promise is paid by the last 3 s.
- **Original audio is always subtitled:** every bodycam/court/interview/stream clip gets burned-in subtitles (word-timed from faster-whisper or the official transcript), big and high-contrast, so viewers understand it on a phone with bad speakers.
- **Bleep only the f-word, c-word and slurs**, exactly the word length (±0.03 s); milder swearing stays audible; the subtitle shows the bleeped word as f***. No swearing at all in the first 15 s (advertiser rules). Gore/violence rules of this runbook stay as they are.
- **Against the "AI slop" impression:** open on real footage/real voices, not narration over stock; real material (clips, documents, photos) ≥ 30 % of the runtime; the narrator states clear judgements ("this is where it went wrong"), no filler or repeated recaps; length follows the story — a tight 12-minute video beats a padded 25.
- Check before publishing: watch the first 60 s — is the promise delivered? Read 3 random subtitled clips with the sound off — are they understandable?
