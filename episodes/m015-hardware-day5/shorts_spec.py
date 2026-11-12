# CHANNEL 16 · MILITARY HARDWARE · m015 (TikTok only, Sat Nov 14, 2026). Five vertical videos t1–t5, 62–75 s each.
# Exercises, tests, training and demonstrations only. Facts: sources.md. shot: (clip_id, start, cx)
TA = 705868   # Flight Test THAAD-23 (FTT-23), Reagan Test Site, Kwajalein Atoll, Aug 30, 2019 (MDA)
TK = 540934   # Flight Experiment THAAD-01 (FET-01), Pacific Spaceport Complex Alaska, Kodiak, July 30, 2017 (MDA)
TI = 537462   # FTT-18 THAAD intercept test, Kodiak, Alaska, July 11, 2017 (MDA)
PC = 944609   # M109A7 Paladin live fire, Alpha Battery 2-82 FA, Fort Cavazos, Texas, Nov 20, 2024 (60p)
PS = 954992   # Marne Focus: HIMARS and Paladin live fire, Fort Stewart, Ga., Mar 11, 2025 (60p)
PL = 955158   # M109A7 Paladin Table VI / German live fire, Pabrade Training Area, Lithuania, Mar 6, 2025
PP = 864039   # Bull Battery M109A7 Paladin live fire, Torun, Poland, Nov 3, 2022 (4:3)
BC = 873471   # B-1B Lancers land and take off, Andersen AFB, Guam, Cope North, Feb 10, 2023 (50p)
BD = 453808   # B-1 takeoffs with afterburners, Dyess AFB, Texas (Feb 2016)
BG = 573931   # Global Thunder 18: nighttime afterburners, Dyess AFB (Nov 2017)
BS = 914029   # Bomber Task Force 24-2 first B-1B takeoff, Lulea-Kallax Air Base, Sweden, Feb 26, 2024 (60p)
BY = 849317   # Three B-1Bs take off, Dyess AFB, June 29, 2022 (37th anniversary of the B-1 at Dyess) (60p)
BE = 1004381  # B-1B Lancer capabilities, 53rd Wing, Eglin AFB (Apr 2026) — only shots without burned-in graphics
HP = 1017152  # Decommissioned USS Peleliu (LHA 5) struck by Harpoons, RIMPAC 2026 SINKEX, July 17, 2026
HPA, HPB, HPC = "1017152a", "1017152b", "1017152c"  # de-duplicated (mpdecimate+minterpolate) cuts of 1017152 at 20.9–25.3, 37.4–42.2, 49.7–59.2 s (source repeats every 4th frame there)
HQ = 1015815  # same event, second camera
HO = 615631   # USS Olympia (SSN 717) fires a Harpoon during RIMPAC 2018 SINKEX, July 12, 2018 (4:3)
HW = 683291   # Harpoon launched from USS Curtis Wilbur (DDG 54), Pacific Vanguard, Philippine Sea, May 26, 2019 (60p)
HC = 475606   # USS Coronado (LCS 4) launches a Harpoon Block 1C, RIMPAC, July 19, 2016
OR = 482116   # CV-22B tilt-rotor air-to-air refueling with an MC-130H Combat Talon II, Hurlburt Field, Fla., Sept 7, 2016 (60p)
OM = 675255   # CV-22 Osprey, 352d Special Operations Wing, RAF Mildenhall, takeoff and landing (Mar 2019)
OT = 635383   # CV-22 Osprey take off from runway (U.S. Air Force courtesy video, Oct 2018)
OL = 635387   # CV-22 Osprey landing on runway (U.S. Air Force courtesy video, Oct 2018)

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

LB_TA = dict(label="KWAJALEIN ATOLL · THAAD FLIGHT TEST · AUG 2019")
LB_TK = dict(label="KODIAK, ALASKA · THAAD FLIGHT TEST · JULY 30, 2017")
LB_TI = dict(label="KODIAK, ALASKA · THAAD FLIGHT TEST · JULY 11, 2017")
LB_TKA = dict(label="OVER THE PACIFIC · TARGET AIR-LAUNCH · JULY 30, 2017")
LB_P1 = dict(label="M109A7 PALADIN · U.S. ARMY LIVE-FIRE TRAINING")
LB_PC = dict(label="FORT CAVAZOS, TEXAS · LIVE-FIRE EXERCISE · NOV 2024")
LB_PS = dict(label="FORT STEWART, GA. · LIVE-FIRE EXERCISE · MAR 2025")
LB_PL = dict(label="PABRADE, LITHUANIA · LIVE-FIRE TRAINING · MAR 2025")
LB_PP = dict(label="TORUN, POLAND · LIVE-FIRE TRAINING · NOV 2022")
LB_B2 = dict(label="B-1B · DYESS AFB 2022 / 53RD WING VIDEO 2026")
LB_B9 = dict(label="DYESS AFB, TEXAS · B-1B TAKEOFFS · 2016 AND 2022")
LB_BC = dict(label="ANDERSEN AFB, GUAM · EXERCISE COPE NORTH · FEB 2023")
LB_BD = dict(label="DYESS AFB, TEXAS · B-1 TAKEOFFS · 2016")
LB_BG = dict(label="DYESS AFB · EXERCISE GLOBAL THUNDER 18 · 2017")
LB_BS = dict(label="LULEA-KALLAX, SWEDEN · BOMBER TASK FORCE · FEB 2024")
LB_BY = dict(label="DYESS AFB, TEXAS · B-1B TAKEOFF · JUNE 2022")
LB_BE = dict(label="U.S. AIR FORCE 53RD WING VIDEO · 2026")
LB_HP = dict(label="EX-USS PELELIU · RIMPAC 2026 SINKEX · JULY 2026")
LB_HO = dict(label="USS OLYMPIA · RIMPAC 2018 SINKEX · JULY 2018")
LB_HW = dict(label="USS CURTIS WILBUR · EXERCISE PACIFIC VANGUARD · MAY 2019")
LB_HC = dict(label="USS CORONADO · RIMPAC EXERCISE · JULY 2016")
LB_OR = dict(label="HURLBURT FIELD, FLA. · AIR REFUELING TRAINING · 2016")
LB_OM = dict(label="RAF MILDENHALL, ENGLAND · CV-22 TAKEOFF · 2019")
LB_O1 = dict(label="CV-22 OSPREY · U.S. AIR FORCE TRAINING FOOTAGE")
LB_OT = dict(label="U.S. AIR FORCE VIDEO · CV-22 · 2018")

SHORTS = [
 dict(id="t1", hook="[HIT-TO-KILL]<br>MISSILE VS MISSILE", title="THAAD stops a ballistic missile by hitting it. 8 interceptors per launcher (MDA tests)",
      lines=[
  ("That's a missile built to hit another missile. This is THAAD, in a Missile Defense Agency test.", [(TA, 51.50, .48), (TA, 66.00, .45)], "tense", LB_TA),
  ("THAAD stands for Terminal High Altitude Area Defense.", [(TA, 77.00, .50)], "punch", LB_TA),
  ("It's built to stop ballistic missiles in the last phase of their flight, inside or just outside the atmosphere.", [(TI, 99.50, .50), (TI, 111.00, .50)], "calm", LB_TI),
  ("It stops its target by hitting it. The Agency calls that hit-to-kill: kinetic energy destroys the warhead.", [(TA, 93.00, .50), (TA, 99.60, .50)], "drive", LB_TA),
  ("Each launcher sits on a truck, carries eight interceptors, and reloads quickly.", [(TI, 60.00, .50), (TI, 66.50, .50)], "calm", LB_TI),
  ("A radar, the A N T P Y two, searches, tracks, and feeds the interceptor its data.", [(TK, 65.00, .50), (TK, 75.30, .50)], "calm", LB_TK),
  ("July thirtieth, twenty seventeen. An Air Force C-17 air-launches a medium-range target missile over the Pacific.", [(TK, 18.00, .50), (TK, 20.90, .50), (TK, 24.00, .50)], "tense", LB_TKA),
  ("THAAD answers from the Pacific Spaceport Complex, in Kodiak, Alaska.", [(TK, 51.10, .50), (TK, 57.00, .50)], "calm", LB_TK),
  ("Intercept.", [(TK, 90.70, .50)], "punch", LB_TK),
  ("Nineteen days earlier, from the same site, it intercepted an intermediate-range target.", [(TI, 32.00, .50), (TI, 131.00, .50)], "calm", LB_TI),
  ("In August twenty nineteen, THAAD fired from Kwajalein Atoll, in the Marshall Islands.", [(TA, 60.40, .50), (TA, 72.00, .50)], "calm", LB_TA),
  ("That test used a remote launcher kit for the first time, to extend the area it can defend.", [(TA, 81.00, .50), (TA, 84.60, .50)], "calm", LB_TA),
  ("By then: sixteen for sixteen. Today the Agency lists seventeen for seventeen.", [(TA, 103.00, .50)], "punch", LB_TA),
  ("Eight batteries procured. Seven are fielded with the U.S. Army.", [(TI, 117.70, .50), (TI, 120.60, .50)], "calm", LB_TI),
  ("THAAD or Patriot: which missile shield impresses you more? Follow for more.", [(TA, 109.45, .50), (TA, 54.85, .50)], "punch", LB_TA),
 ]),
 dict(id="t2", hook="[155MM]<br>IT'S NOT A TANK", title="It looks like a tank, but it's a 155mm howitzer: the Army's M109A7 Paladin in live fire",
      lines=[
  ("It looks like a tank. It's not. It's the Army's M109A7 Paladin, and it fires one-hundred-fifty-five-millimeter rounds.", [(PP, 103.85, .50), (PC, 13.40, .12), (PS, 112.50, .50), (PS, 120.20, .50)], "tense", LB_P1),
  ("It's a self-propelled howitzer: a tracked vehicle carrying a big artillery cannon.", [(PP, 18.00, .50), (PP, 22.00, .50)], "calm", LB_PP),
  ("Its job: massed, precision indirect fire, in support of maneuver units.", [(PS, 122.95, .50), (PS, 126.00, .50)], "calm", LB_PS),
  ("Crew: four soldiers.", [(PC, 1.00, .50)], "punch", LB_PC),
  ("The cannon is the M two eighty-four. Range: about twenty-two kilometers with standard rounds, thirty with rocket-assisted ones.", [(PL, 112.00, .50), (PL, 104.50, .50)], "calm", LB_PL),
  ("Rate of fire: up to four rounds a minute, or one a minute, sustained.", [(PS, 136.00, .50), (PP, 97.00, .50)], "drive"),
  ("Here, the crew loads a round into the breech.", [(PC, 39.00, .50), (PC, 5.00, .50)], "calm", LB_PC),
  ("Rounds come from a tracked ammunition carrier, the M992A3, which holds up to ninety-eight.", [(PC, 28.80, .50), (PS, 143.00, .50)], "calm"),
  ("The cannon sits on a chassis common to the Bradley Fighting Vehicle. Engine: six hundred seventy-five horsepower.", [(PP, 70.00, .50), (PP, 75.50, .50)], "drive", LB_PP),
  ("Top road speed: about sixty-one kilometers an hour.", [(PL, 28.50, .50)], "punch", LB_PL),
  ("Fort Stewart, Georgia, March twenty twenty-five: Paladins and HIMARS in the same live fire.", [(PS, 100.00, .50), (PS, 106.00, .50)], "calm", LB_PS),
  ("And Lithuania, the same month, with German soldiers sending targeting information to the U.S. crews.", [(PL, 65.00, .50), (PL, 98.00, .50)], "calm", LB_PL),
  ("In twenty eighteen, the Army planned to field up to six hundred eighty-nine Paladin sets.", [(PP, 87.00, .50)], "calm", LB_PP),
  ("Downrange, the rounds land in the impact area.", [(PL, 124.00, .50)], "tense", LB_PL),
  ("Paladin or HIMARS: which would you rather have behind you? Follow for more.", [(PS, 129.05, .50)], "punch", LB_PS),
 ]),
 dict(id="t3", hook="[137 FT → 79 FT]<br>WINGS THAT SWING", title="The B-1B Lancer swings its wings back for speed: Mach 1.2 and a 75,000-pound payload",
      lines=[
  ("Look at those wings. On the B-1B Lancer, they swing.", [(BC, 24.00, .50)], "tense", LB_BC),
  ("Forward for takeoff, landing and air refueling. Swept back for high-subsonic and supersonic flight.", [(BY, 138.00, .50), (BE, 32.30, .50)], "calm", LB_B2),
  ("Wingspan: one hundred thirty-seven feet spread forward. Seventy-nine, swept.", [(BS, 80.00, .50), (BS, 86.00, .50)], "punch", LB_BS),
  ("Four General Electric F101 engines with afterburner, each over thirty thousand pounds of thrust.", [(BG, 33.70, .50)], "drive", LB_BG),
  ("Top speed: Mach one point two at sea level. That's more than nine hundred miles an hour.", [(BD, 78.00, .50), (BD, 84.00, .50)], "punch", LB_BD),
  ("Payload: seventy-five thousand pounds, the largest conventional payload in the Air Force.", [(BC, 1.00, .50), (BC, 6.00, .50)], "calm", LB_BC),
  ("Crew: four. Two pilots, and two combat systems officers.", [(BY, 14.50, .50), (BY, 33.00, .50)], "calm", LB_BY),
  ("Length: one hundred forty-six feet. Maximum takeoff weight: four hundred seventy-seven thousand pounds.", [(BD, 1.00, .50), (BD, 20.00, .50)], "calm", LB_BD),
  ("This is Dyess Air Force Base, Texas. The first B-1B was delivered here in June nineteen eighty-five.", [(BY, 103.00, .50), (BD, 227.00, .50)], "calm", LB_B9),
  ("It holds almost fifty world records in its class, for speed, payload, range, and time to climb.", [(BS, 94.00, .50), (BS, 100.00, .50)], "drive", LB_BS),
  ("Its nuclear role ended in nineteen ninety-four. Today it's a conventional bomber.", [(BC, 12.50, .50), (BC, 16.50, .50)], "calm", LB_BC),
  ("Here, B-1s are in Sweden, in February twenty twenty-four, on a Bomber Task Force deployment.", [(BS, 112.00, .50), (BS, 120.00, .50)], "calm", LB_BS),
  ("Unit cost, per the Air Force: three hundred seventeen million dollars.", [(BE, 15.75, .50), (BG, 19.00, .50)], "punch"),
  ("B-1B or B-52: which bomber would you pick? Follow for more.", [(BY, 151.00, .50), (BY, 159.00, .50)], "punch", LB_BY),
 ]),
 dict(id="t4", hook="[NEARLY 40,000 TONS]<br>VS 2 HARPOONS", title="A submarine fired two Harpoons at a retired, nearly 40,000-ton warship: RIMPAC 2026 SINKEX",
      lines=[
  ("A missile fired from a submarine, hitting a warship of nearly forty thousand tons. This was a planned sinking exercise.", [(HP, 8.75, .55), (HP, 4.20, .50)], "tense", LB_HP),
  ("The target: the former USS Peleliu, nearly forty thousand tons.", [(HP, 0.05, .50)], "calm", LB_HP),
  ("Two UGM-84 Harpoon missiles hit it, fired from the submarine USS Columbia, in July twenty twenty-six.", [(HPA, 0.40, .50), (HP, 42.20, .50)], "drive", LB_HP),
  ("The Harpoon is the Navy's all-weather, over-the-horizon anti-ship missile.", [(HW, 24.00, .50), (HW, 45.00, .50)], "punch", LB_HW),
  ("It entered service in nineteen seventy-seven. It can launch from ships, submarines, aircraft and shore batteries.", [(HC, 3.20, .50)], "calm", LB_HC),
  ("Here, the submarine USS Olympia fires one, during RIMPAC twenty eighteen.", [(HO, 13.00, .50)], "calm", LB_HO),
  ("Guidance: active radar. At the end, it can skim the sea, or pop up before it hits.", [(HW, 59.00, .50), (HW, 31.00, .50)], "drive", LB_HW),
  ("Ship and submarine versions are fifteen feet long, and weigh about fifteen hundred pounds with the booster.", [(HPB, 0.25, .50), (HO, 23.00, .50)], "calm"),
  ("A turbojet keeps it flying. A solid-fuel booster gets it started.", [(HW, 64.00, .50)], "calm", LB_HW),
  ("Twenty-nine partner nations use the Harpoon Block Two.", [(HP, 12.50, .50)], "punch", LB_HP),
  ("Uncrewed surface vessels also took part. The Navy says the ship was sunk.", [(HPC, 4.40, .50), (HPC, 0.10, .50)], "tense", LB_HP),
  ("She now rests about fifteen thousand feet down, more than fifty nautical miles north of Kauai.", [(HQ, 7.20, .10)], "calm", LB_HP),
  ("Peleliu served the Navy for more than thirty-five years.", [(HQ, 12.75, .10)], "slow", LB_HP),
  ("Harpoon or torpedo: which impresses you more? Follow for more.", [(HQ, 16.50, .10)], "punch", LB_HP),
 ]),
 dict(id="t5", hook="[280 KNOTS]<br>TAKES OFF LIKE A HELO", title="The CV-22 Osprey takes off like a helicopter and refuels midair like a plane",
      lines=[
  ("It hovers like a helicopter, and refuels in midair like a plane. This is the CV-22 Osprey.", [(OR, 94.00, .50), (OL, 1.00, .50)], "tense", LB_O1),
  ("It's the Air Force's special operations tiltrotor.", [(OM, 40.00, .50), (OM, 46.00, .50)], "punch", LB_OM),
  ("It takes off and lands vertically.", [(OT, 1.00, .50)], "calm", LB_OT),
  ("Once airborne, the engine nacelles on each wing tilt forward, and it flies with the range and speed of a turboprop.", [(OT, 13.00, .50), (OT, 18.00, .50)], "calm", LB_OT),
  ("Its job: carry special operations forces in and out over long distances, and resupply them.", [(OR, 60.00, .50), (OR, 66.50, .50)], "calm", LB_OR),
  ("Here, it plugs into a fuel hose from an MC-130H Combat Talon Two, over Hurlburt Field, Florida.", [(OR, 41.00, .50), (OR, 46.00, .50)], "drive", LB_OR),
  ("Two Rolls-Royce engines, each over six thousand two hundred shaft horsepower.", [(OR, 75.00, .50), (OR, 80.00, .50)], "punch", LB_OR),
  ("Each rotor is thirty-eight feet across. Wingspan: almost eighty-four feet.", [(OR, 99.00, .50), (OR, 106.50, .50)], "calm", LB_OR),
  ("Top speed: two hundred eighty knots. Ceiling: twenty-five thousand feet.", [(OR, 110.50, .50), (OR, 127.50, .50)], "punch", LB_OR),
  ("Combat radius: five hundred nautical miles, with one internal auxiliary tank.", [(OR, 117.00, .50), (OR, 18.00, .50)], "calm", LB_OR),
  ("It carries twenty-four seated troops, or ten thousand pounds of cargo.", [(OR, 25.50, .50), (OR, 53.00, .50)], "calm", LB_OR),
  ("A crew of four: a pilot, a copilot, and two flight engineers.", [(OR, 136.00, .50), (OR, 143.00, .50)], "calm", LB_OR),
  ("Here, an Osprey from RAF Mildenhall, England, lifts off on a routine flight.", [(OM, 59.00, .50), (OM, 66.00, .50)], "calm", LB_OM),
  ("First operational aircraft delivered: January two thousand seven. Unit cost: ninety million dollars.", [(OL, 14.00, .50), (OL, 19.50, .50)], "punch", LB_OT),
  ("Osprey or Black Hawk: which would you rather ride in? Follow for more.", [(OL, 26.00, .50)], "punch", LB_OT),
 ]),
]
YSHORTS = []

DISPLAY = [("A N T P Y two", "AN/TPY-2"), ("twenty seventeen", "2017"), ("twenty nineteen", "2019"), ("July thirtieth", "July 30"),
           ("sixteen for sixteen", "16 for 16"), ("seventeen for seventeen", "17 for 17"), ("Eight batteries", "8 batteries"),
           ("Seven are", "7 are"), ("eight interceptors", "8 interceptors"), ("Nineteen days", "19 days"),
           ("one-hundred-fifty-five-millimeter", "155mm"), ("M two eighty-four", "M284"), ("twenty-two kilometers", "22 km"), ("thirty with", "30 km with"),
           ("four rounds", "4 rounds"), ("one a minute", "1 a minute"), ("ninety-eight", "98"), ("six hundred seventy-five", "675"), ("sixty-one kilometers", "61 km"),
           ("twenty twenty-four", "2024"), ("twenty twenty-five", "2025"), ("twenty fourteen", "2014"), ("six hundred eighty-nine", "689"),
           ("Crew: four", "Crew: 4"),
           ("one hundred thirty-seven feet", "137 feet"), ("Seventy-nine", "79"), ("thirty thousand pounds", "30,000 pounds"), ("Mach one point two", "Mach 1.2"),
           ("nine hundred miles", "900 miles"), ("seventy-five thousand", "75,000"), ("one hundred forty-six", "146"), ("four hundred seventy-seven thousand", "477,000"),
           ("nineteen eighty-five", "1985"), ("nineteen eighty-eight", "1988"), ("almost fifty", "almost 50"), ("nineteen ninety-four", "1994"),
           ("three hundred seventeen million dollars", "$317 million"), ("Forty-four", "44"),
           ("forty-thousand-ton", "40,000-ton"), ("forty thousand tons", "40,000 tons"), ("twenty twenty-six", "2026"), ("nineteen seventy-seven", "1977"),
           ("twenty eighteen", "2018"), ("fifteen feet", "15 feet"), ("fifteen hundred pounds", "1,500 pounds"), ("Twenty-nine", "29"), ("Block Two", "Block II"),
           ("fifteen thousand feet", "15,000 feet"), ("fifty nautical", "50 nautical"), ("six thousand feet", "6,000 feet"), ("thirty-five years", "35 years"),
           ("Combat Talon Two", "Combat Talon II"), ("six thousand two hundred", "6,200"), ("thirty-eight feet", "38 feet"), ("eighty-four feet", "84 feet"),
           ("two hundred eighty knots", "280 knots"), ("twenty-five thousand feet", "25,000 feet"), ("five hundred nautical", "500 nautical"),
           ("twenty-four seated", "24 seated"), ("ten thousand pounds", "10,000 pounds"), ("A crew of four", "A crew of 4"),
           ("two thousand seven", "2007"), ("ninety million dollars", "$90 million")]
