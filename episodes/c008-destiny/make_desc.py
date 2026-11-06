#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for THE CALL 008."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "31 aboard")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
summary = ("On the night of March 2, 2021, the Canadian scallop trawler Atlantic Destiny had a catastrophic engine failure about 120 nautical miles south of Yarmouth, Nova Scotia: "
           "an engine that would not stop, a fire, and seawater pouring into the hull, with 31 people aboard, winds gusting to 55 knots and water near 5 °C. "
           "Using real U.S. Coast Guard footage and the Transportation Safety Board of Canada's investigation, we follow the night step by step: "
           "the relayed distress call, the Royal Canadian Air Force Hercules and Cormorant, two Air Station Cape Cod Jayhawks that hoisted 21 fishermen, "
           "the last six taken off by the Canadian Coast Guard ship Cape Roger, and what the TSB found about why the ship was lost.")
src = [
 ("TSB Marine Investigation Report M21A0041 (Atlantic Destiny)", "https://bst-tsb.gc.ca/eng/rapports-reports/marine/2021/m21a0041/m21a0041.html"),
 ("TSB news release, Jan. 24, 2024", "https://tsb-bst.gc.ca/eng/medias-media/communiques/marine/2024/m21a0041-20240124.html"),
 ("U.S. Coast Guard release, March 3, 2021", "https://content.govdelivery.com/accounts/USDHSCG/bulletins/2c4da1d"),
 ("Vertical Magazine, \"Atlantic Destiny\"", "https://verticalmag.com/features/atlantic-destiny/"),
 ("CBS Boston, March 3, 2021", "https://www.cbsnews.com/boston/news/cape-cod-coast-guard-canadian-fisherman-rescue/"),
 ("National Fisherman", "https://nationalfisherman.com/national-international/u-s-canadian-forces-rescue-31-from-canadian-scallop-vessel"),
 ("Newport Buzz, Oct. 6, 2021 (award ceremony)", "https://thenewportbuzz.com/?p=32475"),
 ("DVIDS videos", "https://www.dvidshub.net/video/785731 · /816332 · /833450"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — Air Station Cape Cod / First District (PO3 Briana Carter; PO1 Travis Magee).",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescue #searchandrescue"]
TAGS = ["coast guard rescue", "atlantic destiny", "nova scotia rescue", "fishing vessel fire", "ship sinking", "mh-60 jayhawk", "air station cape cod",
        "cormorant helicopter", "royal canadian air force", "helicopter hoist", "rescue swimmer", "georges bank", "scallop trawler",
        "real rescue footage", "the call", "channel 16", "search and rescue", "transportation safety board"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
