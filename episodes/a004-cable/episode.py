# CHANNEL 16 · ANATOMY OF A RESCUE 004 — On the Cable (how a Coast Guard helicopter hoist works, 6 real rescues)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (location/date lower third), kind (narration direction: calm|punch|tense|slow|drive|question)
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

ICE = 1002629     # Air Station Kodiak MH-60, Apr 12, 2026: 3 adults + 1 child off an 18-ft vessel on an ice floe ~10 mi W of Chefornak (PO1 Shannon Shepard)
TUG = 972655      # Air Station Kodiak MH-60, Aug 1, 2025: 4 hoisted from the tug Sea Ranger ~130 mi S of Cordova (PO1 Shannon Shepard)
WALRUS = 950715   # Air Station Elizabeth City MH-60, Jan 28, 2025: 2 men hoisted from the sinking sailboat Walrus off North Carolina
SHIP = 977299     # Air Station Astoria, Sept 11, 2025: 80-year-old hoisted from the cruise ship Ruby Princess, 184 mi W of Cape Flattery (PO3 Daylan Garlic-Jackson)
KAYAK = 1019642   # Air Station Ventura Jayhawk, Aug 15, 2026: 2 kayakers hoisted from the water off Anacapa Island
PEAK = 1012192    # Air Station Port Angeles, June 20, 2026: hiker hoisted from a gully on Mount Larrabee, crew operating at 6,710 ft (PO3 William Kirk) — vertical

AKW = [[-166.8, 62.0], [-150.8, 56.6]]            # western Alaska: Kodiak -> Bethel -> Chefornak
CHEF = [-164.27, 60.16]; FLOE = [-164.60, 60.16]; KODIAK = [-152.49, 57.75]; KSAL = [-156.65, 58.68]; BETHEL = [-161.76, 60.79]
GOA = [[-155.5, 61.6], [-141.5, 56.6]]            # Gulf of Alaska
CORDOVA = [-145.76, 60.54]; RANGER = [-145.80, 58.66]
NC = [[-79.6, 37.1], [-74.3, 33.2]]
WILM = [-77.94, 34.22]; WALRUS_P = [-76.14, 34.25]; ECITY = [-76.17, 36.26]; BEAUFORT = [-76.66, 34.72]
WAC = [[-130.4, 49.7], [-121.6, 45.5]]            # Washington / Oregon coast, offshore
FLATTERY = [-124.72, 48.38]; RUBY = [-128.73, 48.38]; ASTORIA = [-123.88, 46.16]
CI = [[-119.95, 34.45], [-118.95, 33.80]]          # Anacapa / Oxnard
ARCH = [-119.36, 34.017]; OXNARD = [-119.21, 34.20]; MUGU = [-119.12, 34.12]; CHANNELIS = [-119.23, 34.165]
NWWA = [[-124.3, 49.35], [-120.9, 47.65]]          # Port Angeles -> Mount Larrabee -> Bellingham
PA = [-123.43, 48.12]; LARRABEE = [-121.65, 48.98]; BELL = [-122.54, 48.79]

LINES = [
 # ---------------- COLD OPEN (Chefornak) ----------------
 ("April twelfth, twenty twenty-six. About five in the morning. The sea ice about ten miles west of Chefornak, Alaska.",
  [C(ICE, 2), C(ICE, 9)], dict(tag=("NEAR CHEFORNAK, ALASKA", "APR 12, 2026"), kind="calm")),
 ("Down there is an eighteen-foot boat, stuck on an ice floe. Three adults and a child have been trapped out here for more than a day.",
  [C(ICE, 14), C(ICE, 19)], dict(kind="tense")),
 ("The helicopter above them has flown hundreds of miles to get here, stopping twice for fuel, through blowing snow, icing, and near-zero visibility.",
  [C(ICE, 28), C(ICE, 34)], dict(kind="drive")),
 ("Now everything depends on one cable. And on the people at each end of it.",
  [C(ICE, 45), C(ICE, 52)], dict(kind="slow", gap=0.7)),
 ("So how do you lift a family off the ice, from a helicopter, in twenty-eight degrees and a twenty-nine mile an hour wind?",
  [C(ICE, 57), C(ICE, 61.5)], dict(kind="question", gap=0.6)),
 ("This is how a Coast Guard helicopter hoist works. Six real rescues: a tug, a sailboat, a cruise ship, two kayakers, a mountain, and the ice.",
  [G("title", title="On the<br><span style=\"color:#FF5B14\">cable</span>", sub="ANATOMY OF A RESCUE · 004", size=230)], dict(kind="slow", gap=2.6)),

 # ---------------- I. THE CREW ----------------
 ("It starts with who's on board.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="I", t="THE CREW")], dict(kind="calm")),
 ("A Coast Guard Jayhawk is typically operated by a crew of four. And two of those jobs are what this video is about.",
  [G("cards3", kicker="MH-60T JAYHAWK", title="A CREW OF FOUR",
     cards=[dict(h="PILOTS", t="At the controls", s="CAN'T SEE DIRECTLY BELOW", size=96), dict(h="FLIGHT MECH", t="At the door", s="RUNS THE HOIST", size=96), dict(h="SWIMMER", t="On the cable", s="RESCUE SWIMMER", size=96)],
     footer="SOURCES: USCG AIR STATION CAPE COD · MILITARY.COM")], dict(kind="calm")),
 ("The flight mechanic runs the hoist. And because the pilot can't see what's directly below the helicopter, the flight mechanic also relays commands to the pilot, while working the cable.",
  [C(TUG, 45), C(TUG, 51)], dict(tag=("GULF OF ALASKA", "AUG 1, 2025"), kind="drive")),
 ("The rescue swimmer is an aviation survival technician. Twenty-two weeks of training: seven to become an emergency medical technician, ten on rescue swimming and helicopter rescue, five on survival equipment.",
  [G("cards3", kicker="AVIATION SURVIVAL TECHNICIAN", title="22 WEEKS OF TRAINING",
     cards=[dict(h="7", t="weeks · EMT certification"), dict(h="10", t="weeks · rescue swimmer"), dict(h="5", t="weeks · aviation life support")],
     footer="SOURCE: GOCOASTGUARD.COM")], dict(kind="calm")),
 ("And on the end of the cable goes one of a few devices. A rescue basket. A litter. Or a sling. Most of the lifts you'll see in this video use the basket.",
  [G("cards3", kicker="ON THE END OF THE CABLE", title="THE RESCUE DEVICES",
     cards=[dict(h="BASKET", t="Rescue basket", s="MOST LIFTS IN THIS VIDEO", size=96), dict(h="LITTER", t="Rescue litter", size=96), dict(h="SLING", t="Rescue sling", size=96)],
     footer="SOURCE: USCG AUXILIARY · SURFACE GUIDE TO HELICOPTER OPERATIONS")], dict(kind="calm")),
 ("The Jayhawk's equipment includes hoist cameras. And a lot of what you'll see here looks straight down the cable.",
  [C(TUG, 99.5), C(TUG, 105)], dict(kind="calm", gap=0.6)),

 # ---------------- II. THE DECK (Sea Ranger) ----------------
 ("First, the deck of a boat in trouble.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="II", t="THE DECK")], dict(kind="calm")),
 ("August first, twenty twenty-five. A hundred-and-ten-foot tug, the Sea Ranger, is taking on water in the Gulf of Alaska, about a hundred thirty miles south of Cordova.",
  [G("map", map=dict(bounds=GOA, rings=[dict(ll=RANGER, r=45, n=3, d=0.4)],
     cities=[dict(ll=RANGER, name="SEA RANGER", sub="~130 MI S OF CORDOVA", d=0.3, color="#FF5B14"), dict(ll=CORDOVA, name="CORDOVA", d=0.6), dict(ll=KODIAK, name="AIR STATION KODIAK", d=0.8, size=28)]),
     kicker="AUGUST 1, 2025", title="GULF OF ALASKA")], dict(kind="calm")),
 ("Ten seventeen in the morning: the first report. A Hercules airplane from Kodiak finds the tug at one-oh-eight. The crew says they're not in distress. The plane drops a pump, and heads back.",
  [G("callcard", kicker="COAST GUARD ARCTIC DISTRICT · AUG 1, 2025", title="SEA RANGER",
     rows=[["10:17", "REPORT · TAKING ON WATER"], ["13:08", "HC-130 LOCATES THE TUG"], ["—", "CREW: NOT IN DISTRESS"], ["—", "DEWATERING PUMP DROPPED"]])], dict(kind="calm")),
 ("At three fifty-seven, a second report. The tug is adrift. There's smoke in the engine room. It's still taking on water, and its pumps won't start.",
  [G("callcard", kicker="COAST GUARD ARCTIC DISTRICT · AUG 1, 2025", title="SECOND CALL",
     rows=[["15:57", "VESSEL ADRIFT"], ["ENGINE ROOM", "SMOKE"], ["HULL", "STILL TAKING ON WATER"], ["PUMPS", "WON'T START"]])], dict(kind="tense")),
 ("This time Kodiak launches a Jayhawk. It's over the tug at seven forty-two that evening.",
  [C(TUG, 40.2), C(TUG, 43.5)], dict(tag=("GULF OF ALASKA", "AUG 1, 2025"), kind="drive")),
 ("A hoist from a deck has rules for the people on that deck too. Coast Guard Auxiliary training spells them out.",
  [G("steps", kicker="U.S. COAST GUARD AUXILIARY · SURFACE GUIDE", title="THE BOAT'S HALF OF THE HOIST",
     items=[["Hold", "A steady course and speed, as the pilot directs"], ["Clear", "Stow loose gear, lower antennas, furl sails"], ["Wait", "Let the basket touch the deck first"], ["Never", "Connect the cable to the boat"]], active=3,
     footer="SOURCE: USCG AUXILIARY · SURFACE GUIDE TO HELICOPTER OPERATIONS")], dict(kind="calm")),
 ("The helicopter usually comes in from behind the boat and hovers off its left side. Everything loose gets stowed, because the rotor downwash is very powerful. It can blow loose gear, or even a person, over the side.",
  [C(TUG, 55), C(TUG, 62)], dict(kind="calm")),
 ("Then there's static. Spinning rotor blades act like an electric generator, and the charge can build up on whatever hangs from the cable. So you let the basket touch the deck first. Then you grab it.",
  [C(TUG, 136), C(TUG, 141)], dict(kind="drive")),
 ("See the thin line running down to the deck? That's a trail line. It lets the people below guide the basket, and keep it from swinging.",
  [C(TUG, 312), C(TUG, 318)], dict(kind="calm")),
 ("And one rule is absolute: never connect the hoist cable to the boat.",
  [C(TUG, 150)], dict(kind="punch", gap=0.6)),
 ("One by one, all four people on the Sea Ranger went up in the basket.",
  [C(TUG, 183), C(TUG, 189)], dict(kind="drive")),
 ("Last up, the swimmer.",
  [C(TUG, 419.5)], dict(kind="punch", gap=0.5)),
 ("No injuries. The search and rescue coordinator called it the best possible outcome, for a rescue that far out in the Gulf of Alaska.",
  [C(TUG, 202), C(TUG, 207.5)], dict(kind="calm", gap=0.8)),

 # ---------------- III. THE BASKET (Walrus) ----------------
 ("So what happens to the person in the basket?",
  [G("chapter", case="ANATOMY OF A RESCUE", n="III", t="THE BASKET")], dict(kind="question")),
 ("January twenty-eighth, twenty twenty-five. Two men are sailing a thirty-two-foot sailboat, the Walrus, from Beaufort, North Carolina, toward Puerto Rico. They hit bad weather. Water comes in faster than their pump can keep up.",
  [G("map", map=dict(bounds=NC, rings=[dict(ll=WALRUS_P, r=40, n=3, d=0.5)],
     cities=[dict(ll=BEAUFORT, name="BEAUFORT", d=0.2, anchor="end", size=28), dict(ll=WALRUS_P, name="WALRUS", sub="~103 MI E OF WILMINGTON", d=0.4, color="#FF5B14"),
             dict(ll=WILM, name="WILMINGTON", d=0.6, anchor="end", size=28), dict(ll=ECITY, name="AIR STATION ELIZABETH CITY", d=0.8, size=28, anchor="end")]),
     kicker="JANUARY 28, 2025", title="OFF NORTH CAROLINA")], dict(kind="tense")),
 ("They send a distress alert from their marine radio, and from a satellite emergency device. Their gear is registered, so the Coast Guard gets precise distress information, fast.",
  [C(WALRUS, 40.3), G("callcard", kicker="DISTRICT FIVE COMMAND CENTER · JAN 28, 2025", title="WALRUS · DISTRESS", rows=[["VHF-DSC", "DISTRESS ALERT FROM THE MARINE RADIO"], ["SENDs", "SATELLITE EMERGENCY NOTIFICATION DEVICE"], ["GEAR", "REGISTERED"]]), G("stat", a="2 ALERTS", b="RADIO + SATELLITE · BOTH REGISTERED", c="SOURCE: U.S. COAST GUARD · WECT")], dict(tag=("OFF NORTH CAROLINA", "JAN 28, 2025"), kind="drive")),
 ("A Hercules gets there first and drops a pump. Then a Jayhawk arrives from Elizabeth City. With the boat still sinking, the Jayhawk crew hoists both men off.",
  [C(WALRUS, 9), C(WALRUS, 13)], dict(kind="drive")),
 ("The rescue swimmer signals the helicopter crew when to raise each person.",
  [C(WALRUS, 11)], dict(kind="calm")),
 ("Each man rides up in the basket. At the door, the crew pulls the basket inside, helps him out, and straps him into a seat.",
  [C(WALRUS, 27.2), C(WALRUS, 31.5)], dict(kind="calm")),
 ("Both were reported stable, with no injuries. The sailboat was left at sea. And the mission coordinator stressed how essential it is for all mariners to register their communications gear.",
  [C(WALRUS, 32.8), C(WALRUS, 23.5)], dict(kind="slow", gap=0.8)),

 # ---------------- IV. THE SHIP (Ruby Princess) ----------------
 ("Sometimes, the deck belongs to a cruise ship.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="IV", t="THE SHIP")], dict(kind="calm")),
 ("September eleventh, twenty twenty-five. A hundred eighty-four miles west of Cape Flattery, Washington. An eighty-year-old man aboard the cruise ship Ruby Princess has an object lodged in his throat.",
  [G("map", map=dict(bounds=WAC, arcs=[dict(**{"from": ASTORIA, "to": RUBY}, d=0.6, dur=1.4, bend=0.12)],
     rings=[dict(ll=RUBY, r=40, n=3, d=0.3)],
     cities=[dict(ll=RUBY, name="RUBY PRINCESS", sub="184 MI W OF CAPE FLATTERY", d=0.3, color="#FF5B14", dy=-60), dict(ll=FLATTERY, name="CAPE FLATTERY", d=0.5, size=28),
             dict(ll=ASTORIA, name="AIR STATION ASTORIA", d=0.7, size=28)]),
     kicker="SEPTEMBER 11, 2025", title="OFF THE WASHINGTON COAST")], dict(kind="calm")),
 ("A helicopter crew from Air Station Astoria comes in over the ship.",
  [C(SHIP, 3.3), C(SHIP, 8.4)], dict(tag=("184 MI W OF CAPE FLATTERY", "SEPT 11, 2025"), kind="drive")),
 ("On a hoist like this, the crew talks it through, call by call. The Coast Guard's own video captions some of those calls.",
  [G("callcard", kicker="CAPTIONS FROM THE COAST GUARD'S VIDEO", title="THE HOIST CALLS",
     rows=[["01", "BASKET IS CLEAR OF THE DECK"], ["02", "BASKET IS AT THE CABIN DOOR"], ["03", "THE HOOK IS ON ITS WAY DOWN"], ["04", "SWIMMER IS OFF THE DECK AND ON HIS WAY UP"], ["05", "SWIMMER IS INSIDE THE CABIN AND HOIST COMPLETE"]],
     footer="RUBY PRINCESS MEDEVAC · AIR STATION ASTORIA · VIA DVIDS")], dict(kind="calm")),
 ("Basket is clear of the deck. Basket is at the cabin door.",
  [C(SHIP, 15.4), C(SHIP, 25.3)], dict(kind="slow")),
 ("Then the hook goes back down, for the swimmer.",
  [C(SHIP, 41), C(SHIP, 44)], dict(kind="calm")),
 ("Swimmer is off the deck, and on his way up. Hoist complete.",
  [C(SHIP, 47), C(SHIP, 55.6)], dict(kind="slow", gap=0.8)),

 # ---------------- V. THE WATER (Anacapa) ----------------
 ("And sometimes, there's no deck at all.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="V", t="THE WATER")], dict(kind="slow")),
 ("August, twenty twenty-six. Eleven seventeen on a Friday night, the Coast Guard gets a call from two people in the water off Anacapa Island, California.",
  [G("map", map=dict(bounds=CI, rings=[dict(ll=ARCH, r=40, n=3, d=0.4)],
     cities=[dict(ll=ARCH, name="ARCH ROCK", sub="ANACAPA ISLAND", d=0.3, color="#FF5B14", anchor="end", dy=40), dict(ll=OXNARD, name="OXNARD", d=0.6, size=28),
             dict(ll=MUGU, name="AIR STATION VENTURA", d=0.8, size=28, dy=50)]),
     kicker="AUGUST 2026 · 11:17 P.M.", title="OFF ANACAPA ISLAND")], dict(kind="calm")),
 ("Their fourteen-foot kayak has overturned about half a mile off Arch Rock. They've been adrift for about four hours.",
  [G("callcard", kicker="SECTOR LOS ANGELES-LONG BEACH · AUGUST 2026", title="TWO IN THE WATER",
     rows=[["23:17", "CALL FROM THE WATER"], ["KAYAK", "14-FT · OVERTURNED"], ["POSITION", "~1/2 MI OFF ARCH ROCK"], ["ADRIFT", "ABOUT 4 HOURS"]])], dict(kind="tense")),
 ("They have no radio. But they're wearing wetsuits and life jackets, and they're within cellphone range.",
  [C(KAYAK, 2), C(KAYAK, 8)], dict(tag=("ANACAPA ISLAND, CALIFORNIA", "AUG 15, 2026"), kind="calm")),
 ("The Coast Guard sends out an urgent marine broadcast, and launches crews from Station Channel Islands and Air Station Ventura. The Jayhawk is over them at midnight.",
  [C(KAYAK, 12), C(KAYAK, 16.5)], dict(kind="drive")),
 ("The basket comes straight down to them, in the water.",
  [C(KAYAK, 21.5), C(KAYAK, 25)], dict(kind="tense")),
 ("Both kayakers are hoisted out, and flown to Oxnard Airport. Both were reported stable.",
  [C(KAYAK, 30), C(KAYAK, 37)], dict(kind="calm")),
 ("The lesson from the search and rescue coordinator: carry more than one reliable way to call. A signaling device. And a VHF marine radio.",
  [C(KAYAK, 66), C(KAYAK, 72)], dict(kind="calm", gap=0.8)),

 # ---------------- VI. THE MOUNTAIN (Mount Larrabee) ----------------
 ("The cable doesn't only work over water.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VI", t="THE MOUNTAIN")], dict(kind="calm")),
 ("June twentieth, twenty twenty-six. Mount Larrabee, in Washington's Mount Baker Wilderness. A thirty-three-year-old hiker has fallen about a hundred twenty feet down a steep gully, and can't get down on her own.",
  [C(PEAK, 0.2), C(PEAK, 14.4), C(PEAK, 20.0)], dict(tag=("MOUNT LARRABEE, WASHINGTON", "JUNE 20, 2026"), kind="tense")),
 ("The state's emergency management division asks the Coast Guard for help. The evacuation has to happen before sunset.",
  [G("map", map=dict(bounds=NWWA, arcs=[dict(**{"from": PA, "to": LARRABEE}, d=0.4, dur=1.3, bend=-0.15)],
     rings=[dict(ll=LARRABEE, r=40, n=3, d=0.3, color="#FFC93C")],
     cities=[dict(ll=PA, name="AIR STATION PORT ANGELES", d=0.2, size=28, dy=40), dict(ll=LARRABEE, name="MOUNT LARRABEE", sub="HOIST AT 6,710 FT", d=1.5, color="#FFC93C", anchor="end", dy=-60),
             dict(ll=BELL, name="BELLINGHAM", d=0.8, size=28, anchor="end", dy=40)]),
     kicker="JUNE 20, 2026 · BEFORE SUNSET", title="MOUNT BAKER WILDERNESS")], dict(kind="calm")),
 ("A Dolphin crew from Air Station Port Angeles searches the narrow gully for forty minutes. Then a reflection catches their attention. Hikers in the party lead them to her.",
  [C(PEAK, 24.1), C(PEAK, 27.5), C(PEAK, 32.3)], dict(kind="drive")),
 ("The helicopter is at six thousand seven hundred ten feet, with less than ten minutes of fuel left to stay on scene.",
  [G("stat", a="6,710 FT", b="ALTITUDE ON SCENE", c="LESS THAN 10 MINUTES OF FUEL LEFT ON SCENE · SOURCE: USCG")], dict(kind="tense")),
 ("At about eight forty that evening, the crew makes a precision hoist, and flies her to Bellingham, where emergency crews are waiting.",
  [C(PEAK, 37.3), G("map", map=dict(bounds=NWWA, arcs=[dict(**{"from": LARRABEE, "to": BELL}, d=0.4, dur=1.0, bend=0.15)], cities=[dict(ll=LARRABEE, name="MOUNT LARRABEE", d=0.2, color="#FFC93C", anchor="end", dy=-60), dict(ll=BELL, name="BELLINGHAM", sub="EMS WAITING", d=1.3, size=30, anchor="end", dy=40)]), kicker="JUNE 20, 2026 · ABOUT 8:40 P.M.", title="TO BELLINGHAM")], dict(kind="drive")),
 ("The aircraft commander thanked the hikers too. With survival training and safety gear, he said, they were partners in the rescue.",
  [G("quote", q="This successful outcome is a direct result of the outstanding teamwork and rapid coordination between our agencies.", w="LT. CMDR. MARSHALL BURTT · AIRCRAFT COMMANDER")], dict(kind="calm", gap=0.8)),

 # ---------------- VII. THE ICE (Chefornak) ----------------
 ("Which brings us back to the ice.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VII", t="THE ICE")], dict(kind="slow")),
 ("Saturday, April eleventh. Four twenty-four in the afternoon. Alaska State Troopers report a seal hunting party trapped on the ice west of Chefornak. Four people, including a child. Stuck for more than twenty-four hours.",
  [G("callcard", kicker="COAST GUARD ARCTIC DISTRICT · APRIL 11, 2026", title="TRAPPED ON THE ICE",
     rows=[["SAT 16:24", "REPORT FROM ALASKA STATE TROOPERS"], ["ABOARD", "3 ADULTS · 1 CHILD"], ["VESSEL", "18-FT · ON AN ICE FLOE"], ["STUCK", "MORE THAN 24 HOURS"]])], dict(kind="tense")),
 ("Overnight, they manage to free the boat and try to reach a shore party that came out from the village by snowmachine. But moving ice blocks the way.",
  [G("map", map=dict(bounds=[[-165.6, 60.55], [-163.4, 59.8]], rings=[dict(ll=FLOE, r=40, n=3, d=0.3, color="#FF5B14")],
     cities=[dict(ll=FLOE, name="ICE FLOE", sub="~10 MI W OF CHEFORNAK", d=0.3, color="#FF5B14", anchor="end"), dict(ll=CHEF, name="CHEFORNAK", d=0.6)]),
     kicker="BERING SEA · APRIL 2026", title="BLOCKED BY MOVING ICE")], dict(kind="calm")),
 ("Kodiak sends a Jayhawk and a Hercules. The helicopter has to stop for fuel twice, in King Salmon and in Bethel.",
  [G("map", map=dict(bounds=AKW, arcs=[dict(**{"from": KODIAK, "to": KSAL}, d=0.3, dur=0.8, bend=0.1), dict(**{"from": KSAL, "to": BETHEL}, d=1.1, dur=0.8, bend=0.1), dict(**{"from": BETHEL, "to": FLOE}, d=1.9, dur=0.7, bend=0.1, color="#FF5B14")],
     cities=[dict(ll=KODIAK, name="KODIAK", d=0.1, size=30), dict(ll=KSAL, name="KING SALMON · FUEL", d=0.9, size=30, dy=40), dict(ll=BETHEL, name="BETHEL · FUEL", d=1.6, size=30, dy=-40),
             dict(ll=FLOE, name="ICE FLOE", d=1.9, color="#FF5B14", anchor="end", dy=40)]),
     kicker="APRIL 11–12, 2026", title="KODIAK → THE ICE")], dict(kind="drive")),
 ("The pilot-in-command said they battled nearly every Alaska-centric aviation weather hazard imaginable. The Coast Guard says they flew through mountainous terrain, blowing snow, icing, and near-zero visibility.",
  [G("stat", a="800+ MI", b="FLOWN BY THE JAYHAWK CREW", c="MOUNTAINOUS TERRAIN · BLOWING SNOW · ICING · NEAR-ZERO VISIBILITY · SOURCE: USCG")], dict(kind="tense")),
 ("About five in the morning, they're over the boat. Twenty-eight degrees. Wind at twenty-nine miles an hour. Cloud ceiling, eight hundred feet.",
  [C(ICE, 96.5), C(ICE, 103)], dict(tag=("NEAR CHEFORNAK, ALASKA", "APR 12, 2026"), kind="slow")),
 ("The basket goes down to the ice. And one by one, all four go up.",
  [C(ICE, 136), C(ICE, 143)], dict(kind="tense")),
 ("No injuries. They're flown back to Chefornak.",
  [C(ICE, 183), C(ICE, 188)], dict(kind="calm")),
 ("Afterward, the crew agreed it was one of the most challenging missions any of them had ever flown.",
  [C(ICE, 212), C(ICE, 218)], dict(kind="slow")),
 ("And part of why it worked: the hunting party had three ways to communicate, including satellite. The Coast Guard said that greatly helped crews find them.",
  [C(ICE, 226), C(ICE, 231)], dict(kind="calm", gap=0.8)),

 # ---------------- VIII. WHAT MAKES IT WORK ----------------
 ("So what do these six hoists have in common?",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VIII", t="WHAT MAKES IT WORK")], dict(kind="question")),
 ("Look closely, and a few things keep coming up.",
  [G("steps", kicker="WHAT THESE RESCUES HAVE IN COMMON", title="FOUR THINGS THAT GET YOU HOISTED",
     items=[["Call", "More than one way, and registered"], ["Gear", "Life jackets, wetsuits, survival gear"], ["Be seen", "A reflection led the crew to her"], ["Follow", "Let it touch down · never tie it off"]])], dict(kind="calm")),
 ("One: a way to call. Usually more than one. A radio alert and a satellite device off North Carolina. Three ways to communicate on the ice. A cellphone in the water off Anacapa.",
  [C(WALRUS, 33.5), C(KAYAK, 76)], dict(kind="drive")),
 ("Two: gear that buys time. Wetsuits and life jackets for the kayakers. And on the Sea Ranger, a crew the Coast Guard called well equipped.",
  [C(KAYAK, 62), C(TUG, 372)], dict(kind="calm")),
 ("Three: be seen. On Mount Larrabee, a reflection is what caught the crew's attention.",
  [C(PEAK, 15), C(PEAK, 37.5)], dict(kind="calm")),
 ("And four: follow the rules. Hold course and speed as the pilot directs. Let the basket touch down first. And never connect the cable to the boat.",
  [C(TUG, 228), C(TUG, 330)], dict(kind="drive")),
 ("Every person you saw on the end of that cable in this video made it into the helicopter.",
  [C(ICE, 146.5), C(TUG, 192)], dict(kind="punch", gap=0.8)),
 ("Next time on Channel Sixteen, another call, minute by minute. Stay safe out there.",
  [G("end", stamp="ON THE CABLE")], dict(kind="calm", gap=2.4)),
]

DISPLAY = [
 ("April twelfth, twenty twenty-six", "April 12, 2026"), ("April eleventh", "April 11"), ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"),
 ("August first", "August 1"), ("January twenty-eighth", "January 28"), ("September eleventh", "September 11"), ("June twentieth", "June 20"),
 ("eighteen-foot", "18-foot"), ("eight hundred miles", "800 miles"), ("twenty-eight degrees", "28 degrees"), ("twenty-nine mile an hour", "29 mph"),
 ("twenty-nine miles an hour", "29 miles an hour"), ("eight hundred feet", "800 feet"),
 ("Twenty-two weeks", "22 weeks"), ("seven to become", "7 to become"), ("ten on rescue", "10 on rescue"), ("five on survival", "5 on survival"),
 ("hundred-and-ten-foot", "110-foot"), ("a hundred thirty miles", "130 miles"), ("Ten seventeen", "10:17"), ("one-oh-eight", "1:08"),
 ("three fifty-seven", "3:57"), ("seven forty-two", "7:42"), ("thirty-two-foot", "32-foot"), ("A hundred eighty-four miles", "184 miles"),
 ("eighty-year-old", "80-year-old"), ("Eleven seventeen", "11:17"), ("fourteen-foot", "14-foot"), ("thirty-three-year-old", "33-year-old"),
 ("a hundred twenty feet", "120 feet"), ("forty minutes", "40 minutes"), ("six thousand seven hundred ten feet", "6,710 feet"), ("ten minutes", "10 minutes"),
 ("eight forty", "8:40"), ("ten miles", "10 miles"), ("hundreds of miles", "hundreds of miles"), ("Four twenty-four", "4:24"), ("twenty-four hours", "24 hours"), ("Channel Sixteen", "Channel 16"),
 ("twenty-eight", "28"), ("Twenty-eight degrees", "28 degrees"), ("Twenty-nine", "29"),
]

META = dict(
    case="ANATOMY OF A RESCUE · 004", label="CH 16 · 156.800 MHz",
    title="On the Cable: How a Coast Guard Helicopter Hoist Works, in 6 Real Rescues",
    voice="am_eric",
    credit=("Footage: U.S. Coast Guard via DVIDS (public domain). Appearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NCHANNEL 16 is an independent channel, not affiliated with the U.S. Coast Guard."),
)
