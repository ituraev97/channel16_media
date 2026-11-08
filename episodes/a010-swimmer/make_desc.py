#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for ANATOMY 010."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "A wave flips the boat")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
    if txt.startswith("So, five rescues"):
        ch.append((fmt(T["starts"][i]), "What it takes"))
summary = ("What does a Coast Guard rescue swimmer actually do? Five real U.S. Coast Guard rescues, in real Coast Guard footage, show the job of an aviation survival technician (AST) from the jump to the hoist. "
           "A breaking wave flips a boat off the Columbia River bar while the swimmer is already in the water; three people in life jackets on Lake Michigan; a medical emergency near Nahma; "
           "a swimmer who stays behind off Sargent, Texas; a pump lowered on the hoist cable near Galveston; and the Advanced Helicopter Rescue School in Astoria, where rescue swimmers train in 10- to 15-foot surf.")
src = [
 ("U.S. Coast Guard release, Feb. 3, 2023 (Sandpiper, Columbia River)", "https://www.news.uscg.mil/Press-Releases/Article/3288449/"),
 ("Coast Guard Foundation (Sandpiper rescue, AHRS students)", "https://coastguardfoundation.org/news/multiple-coast-guard-units-to-be-honored-for-pacific-northwest-rescue-at-awards-dinner"),
 ("GoCoastGuard.com — Aviation Survival Technician", "https://gocoastguard.com/careers/enlisted/ast"),
 ("U.S. Coast Guard release, Aug. 31, 2022 (Training Center Petaluma rescue swimmer class)", "https://www.news.uscg.mil/Press-Releases/Article/3145622/"),
 ("U.S. Coast Guard via DVIDS, July 2025 (Sturgeon Bay, Mich.)", "https://www.dvidshub.net/news/544074/coast-guard-rescues-3-lake-michigan"),
 ("U.S. Coast Guard release, Sept. 2025 (Sargent, Texas)", "https://www.news.uscg.mil/Press-Releases/Article/4303147/coast-guard-rescues-3-from-capsized-vessel-near-sargent-texas/"),
 ("MyCG, May 14, 2026 (Advanced Helicopter Rescue School)", "https://www.mycg.uscg.mil/News/Article/4485729/forging-responders-in-the-graveyard-of-the-pacific/"),
 ("MyNorthwest, Sept. 2026 (Parker Reef kayaker)", "https://mynorthwest.com/local/san-juan-islands-rescue-coast-guard-crews-save-man-after-his-kayak-overturns/4280473"),
 ("DVIDS videos", "https://www.dvidshub.net/video/909520 · /872430 · /1028863 · /971965 · /970021 · /976930 · /993525 · /1006811 · /987403"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — PO1 Kyle Turcotte, PO2 Michael Clark, PO3 Jessica Walker, Thomas Molloy, "
 "Coast Guard Video Production Team (PO2 Ryan Schultz, PO2 Jose Hernandez, Erik Villa Rodriguez); courtesy videos by Air Station Traverse City and Air Station Houston.",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescueswimmer #searchandrescue"]
TAGS = ["coast guard rescue swimmer", "rescue swimmer", "aviation survival technician", "coast guard rescue", "helicopter rescue at sea",
        "wave flips boat", "columbia river bar", "rescue swimmer training", "advanced helicopter rescue school", "capsized boat rescue",
        "life jacket", "search and rescue", "real rescue footage", "anatomy of a rescue"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
