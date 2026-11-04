#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for STORM FILES 006."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "A man and his dog on a roof")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
    if shots[0][0] == "g:stat" and shots[0][2].get("a") == "900+":
        ch.append((fmt(T["starts"][i]), "The Count, and What It Teaches"))
summary = ("September 2018. Hurricane Florence comes ashore in North Carolina as only a Category 1, then crawls over the Carolinas for four days and becomes the wettest tropical cyclone on record there: 35.93 inches of rain near Elizabethtown. "
           "Using real U.S. Coast Guard footage, we follow the flood that came after the storm: a man and his dog Lucky on a roof north of the Cape Fear River, a Jayhawk crew that flew 37 people, seven dogs and four cats out of one Rocky Point neighborhood, "
           "a woman who had run out of medication in Pender County, shallow-water boat teams in Lumberton, and a rescue swimmer working chest-deep water, barbed wire and floating fire ants to get two people and six dogs out of a flooded home.")
src = [
 ("Hurricane Florence (NWS Wilmington)", "https://www.weather.gov/ilm/HurricaneFlorence"),
 ("NHC Advisory 60A, Sept. 14, 2018", "https://nhc.noaa.gov/archive/2018/al06/al062018.public_a.060.shtml"),
 ("Florence rainfall (NOAA Weather Prediction Center)", "https://www.wpc.ncep.noaa.gov/tropical/rain/florence2018.html"),
 ("Florence landfall and record flooding (NASA GPM)", "https://gpm.nasa.gov/applications/weather/hurricane-florence-makes-landfall-brings-torrential-rains-and-record-flooding-carolinas"),
 ("Florence recap (weather.com)", "https://weather.com/storms/hurricane/news/2018-09-19-hurricane-florence-carolinas-flooding-wind-storm-surge-recap"),
 ("Remembering Florence (WECT)", "https://www.wect.com/2019/09/16/remembering-florence-vast-storm-that-dwarfed-its-low-category"),
 ("The Long Blue Line: storm warriors fight Hurricane Florence (U.S. Coast Guard History)", "https://www.history.uscg.mil/Research/THE-LONG-BLUE-LINE/Article/2929404/the-long-blue-line-coast-guards-storm-warriors-fight-hurricane-florence/"),
 ("57 people and 8 pets, Sept. 15 (U.S. Coast Guard)", "https://content.govdelivery.com/accounts/USDHSCG/bulletins/20d9577"),
 ("North Carolina response update, Sept. 18 (U.S. Coast Guard)", "https://content.govdelivery.com/accounts/USDHSCG/bulletins/20e2a2f"),
 ("Florence hits home for Coast Guard members (Fox News)", "https://www.foxnews.com/us/florence-hits-home-for-coast-guard-members-from-north-carolina"),
 ("Man and dog rescued from a rooftop (News4Jax / AP)", "https://www.news4jax.com/news/2018/09/18/coast-guard-rescues-man-and-dog-from-north-carolina-rooftop/"),
 ("Two people and six dogs (CBS Philadelphia)", "https://www.cbsnews.com/philadelphia/news/atlantic-city-based-coast-guard-member-saves-2-people-several-dogs-from-flooded-nc-home-following-florence/"),
 ("Turn Around Don't Drown (National Weather Service)", "https://weather.gov/tsa/hydro_tadd"),
 ("DVIDS videos", "https://www.dvidshub.net/video/626424 · /625984 · /626073 · /626286 · /626817 · /626278 · /627901 · /627892 · /625750 · /625741"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — Air Station Elizabeth City, Air Station Atlantic City (PO1 Steve Maccaferri, CPO Brad Fitzpatrick), Air Station Clearwater, Coast Guard East, Sector North Carolina; PO2 Dustin Williams, PO3 Ronald Hodges, PO3 Shannon Kearney, PO3 Nathan Cox, PO3 Jim Connor.",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescue #searchandrescue"]
TAGS = ["coast guard rescue", "hurricane florence", "coast guard helicopter rescue", "flood rescue", "north carolina flooding", "rooftop rescue",
        "mh-60 jayhawk", "mh-65 dolphin", "air station elizabeth city", "air station atlantic city", "rescue swimmer", "shallow water rescue",
        "pet rescue", "real rescue footage", "storm files", "channel 16", "hurricane rescue", "search and rescue"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
