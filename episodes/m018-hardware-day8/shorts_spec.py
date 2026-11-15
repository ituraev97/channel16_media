# CHANNEL 16 · MILITARY HARDWARE · m018 (TikTok only, Tue Nov 17, 2026). Five vertical videos t1–t5, 62–75 s each.
# Exercises, tests, training and demonstrations only. Facts: sources.md. shot: (clip_id, start, cx)
JE = 470653   # 2nd Cavalry Regt fires FGM-148 Javelins, Saber Strike 16, Tapa, Estonia, June 19, 2016 (30p, 720p)
JT = 886420   # Weapons Co. 1/23 Marines fire a Javelin, ITX 4-23, Twentynine Palms, Calif., June 9, 2023 (30p)
JF = 985440   # BLT 1/7, 31st MEU, Javelin/TOW range, Camp Fuji, Japan, Oct 2025 (30p) — Javelin shots only
MP = 894189   # M1150 ABV fires an M58 MICLIC, near Boleslawiec, Poland, Aug 17, 2023 (30p, 4:3 box)
MW = 973020   # MICLIC at Fort McCoy, Wis., 469th/402nd Combat Engineer Cos, Aug 2025 (30p)
MA = 927608   # 4th Combat Engineer Bn fires a line charge from an AAV, ITX 4-24, Twentynine Palms, June 11, 2024 (30p)
GW = 934266   # Mk 38 25 mm live fire aboard USS Wasp, Mediterranean, Aug 2, 2024 (30p)
GL = 973398   # Mk 38 live fire aboard USS Abraham Lincoln, Pacific, Aug 2, 2025 (30p)
GB = 550102   # Mk 38 live-fire training aboard USS Abraham Lincoln, Atlantic, Aug 31, 2017 (30p)
GA = 524054   # USS America live-fire exercise vs simulated small fast-boat attack, COMPTUEX, May 8, 2017 (30p)
GM = 1005696  # USS Mustin fires a Mk 38 Mod 4, South China Sea, April 17, 2026 (30p)
FT = 845173   # F/A-18E/F Super Hornets on USS Harry S. Truman, NATO Neptune Shield 22, May 2022 (25p)
FK = 1015995  # F/A-18F Super Hornets launch from MCAS Kaneohe Bay for the RIMPAC 2026 SINKEX, July 17, 2026 (60p)
SJ = 772985   # FTM-44 mission video: ICBM target launch (Kwajalein) + SM-3 Block IIA launch from USS John Finn, Nov 16, 2020 (30p, 720p)
SK = "508345d"  # de-duplicated copy (mpdecimate+minterpolate) of 508345, 20-76 s (new t = old - 20), local only;
SK0 = 508345  # SFTM-01: SM-3 Block IIA launch from USS John Paul Jones, MRBM target from Kauai, Feb 3, 2017 (30p)

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

LB_JE = dict(label="ESTONIA · EXERCISE SABER STRIKE · JUNE 2016")
LB_JT = dict(label="TWENTYNINE PALMS, CALIF. · TRAINING · JUNE 2023")
LB_JF = dict(label="CAMP FUJI, JAPAN · LIVE-FIRE TRAINING · OCT 2025")
LB_JAV = dict(label="U.S. ARMY & MARINES · JAVELIN TRAINING FOOTAGE")
LB_MP = dict(label="POLAND · ARMY TRAINING · AUG 2023")
LB_MW = dict(label="FORT McCOY, WIS. · ARMY TRAINING · 2025")
LB_MA = dict(label="TWENTYNINE PALMS, CALIF. · MARINE TRAINING · JUNE 2024")
LB_MIC = dict(label="U.S. ARMY & MARINES · LINE-CHARGE TRAINING")
LB_GW = dict(label="USS WASP · MEDITERRANEAN · AUG 2024")
LB_GL = dict(label="USS ABRAHAM LINCOLN · PACIFIC · AUG 2025")
LB_GB = dict(label="USS ABRAHAM LINCOLN · LIVE-FIRE TRAINING · 2017")
LB_GA = dict(label="USS AMERICA · LIVE-FIRE EXERCISE · MAY 2017")
LB_GM = dict(label="USS MUSTIN · MK 38 MOD 4 · APRIL 2026")
LB_MK38 = dict(label="U.S. NAVY · MK 38 LIVE-FIRE TRAINING")
LB_FT = dict(label="USS HARRY S. TRUMAN · NATO NEPTUNE SHIELD · MAY 2022")
LB_FK = dict(label="KANEOHE BAY, HAWAII · RIMPAC EXERCISE · JULY 2026")
LB_SJ = dict(label="FLIGHT TEST FTM-44 · PACIFIC · NOV 2020")
LB_SK = dict(label="FLIGHT TEST SFTM-01 · OFF HAWAII · FEB 2017")

SHORTS = [
 dict(id="t1", hook="[2,500 M]<br>FIRE AND FORGET", title="The Javelin guides itself after launch, so the gunner can take cover (training footage)",
      lines=[
  ("This missile steers itself to the target. The gunner can take cover right away.", [(JT, 36.75, .42)], "tense", LB_JAV),
  ("It's the Javelin: a man-portable, fire-and-forget, anti-tank guided missile.", [(JE, 7.00, .45), (JE, 14.00, .50)], "punch", LB_JE),
  ("The Pentagon's test office puts its reach at twenty-five hundred meters.", [(JE, 19.68, .55), (JE, 99.00, .50)], "drive", LB_JE),
  ("Two parts: the missile, in a disposable launch tube, and a reusable command launch unit with day and night sights.", [(JF, 120.80, .50), (JF, 105.50, .50)], "calm", LB_JF),
  ("Ready to fire, the whole system weighs about fifty pounds.", [(JE, 0.40, .50)], "punch", LB_JE),
  ("The gunner places a cursor on the target, and the missile locks on before launch.", [(JT, 22.00, .50), (JT, 27.50, .45)], "calm", LB_JT),
  ("Then, a soft launch: the missile is kicked out of the tube, and its motor lights a moment later.", [(JE, 40.00, .45), (JE, 47.00, .45)], "drive", LB_JE),
  ("Lockheed Martin says that's why it can be fired from inside buildings, or bunkers.", [(JE, 24.00, .50), (JE, 52.00, .50)], "calm", LB_JE),
  ("It can fly straight in, or climb high and come down on top, where armor is weakest.", [(JE, 103.50, .55), (JE, 108.00, .55)], "calm", LB_JE),
  ("Estonia, June twenty sixteen: Second Cavalry Regiment soldiers fire Javelins during exercise Saber Strike.", [(JE, 74.00, .45), (JE, 82.50, .45)], "calm", LB_JE),
  ("Twentynine Palms, California, June twenty twenty-three: a Marine Reserve gunner takes aim.", [(JT, 0.40, .50), (JT, 30.00, .45)], "calm", LB_JT),
  ("Camp Fuji, Japan, October twenty twenty-five: Marines of the Thirty-First Marine Expeditionary Unit train with it.", [(JF, 127.00, .50), (JF, 137.00, .50)], "calm", LB_JF),
  ("It entered U.S. service in nineteen ninety-six. Lockheed Martin marked its fifty thousandth delivery in twenty twenty-one.", [(JE, 58.00, .50), (JE, 63.50, .50)], "calm", LB_JE),
  ("Javelin or Stinger: which shoulder-fired missile impresses you more? Follow for more.", [(JE, 130.15, .50), (JE, 140.00, .50)], "punch", LB_JE),
 ]),
 dict(id="t2", hook="[1,750 LB]<br>OF EXPLOSIVE ON A ROPE", title="A rocket drags 1,750 lb of explosive across a minefield: the MICLIC line charge (training)",
      lines=[
  ("A rocket drags a one hundred meter line of explosives across a minefield. Then, this.", [(MP, 6.25, .30), (MW, 78.40, .50)], "tense", LB_MIC),
  ("This is the M fifty-eight MICLIC: a mine-clearing line charge.", [(MW, 38.00, .50), (MW, 43.00, .50)], "punch", LB_MW),
  ("Its line carries seventeen hundred fifty pounds of C four explosive.", [(MW, 46.50, .55)], "drive", LB_MW),
  ("The rope is one hundred meters long, and a rocket pulls it out.", [(MW, 51.20, .50), (MW, 53.40, .50)], "calm", LB_MW),
  ("The blast clears a lane about one hundred meters long, and fourteen to sixteen meters wide, depending on the ground.", [(MW, 71.00, .50), (MW, 74.50, .50)], "calm", LB_MW),
  ("Mines in its path either go off, or get pushed out of the way.", [(MW, 81.50, .50), (MW, 86.50, .50)], "punch", LB_MW),
  ("It can fire from an Assault Breacher Vehicle, an Amphibious Assault Vehicle, or a towed trailer.", [(MP, 0.40, .50), (MA, 0.40, .50), (MW, 13.20, .50)], "calm", LB_MIC),
  ("Poland, August twenty twenty-three: a First Cavalry Division breacher vehicle fires one in training.", [(MP, 9.30, .50), (MP, 13.00, .50)], "calm", LB_MP),
  ("Downrange, the charge goes off.", [(MP, 24.00, .50), (MP, 32.00, .50)], "punch", LB_MP),
  ("A Marine instructor put the whole load in the tub, the part the rocket pulls out, at over thirty-six hundred pounds.", [(MW, 9.40, .50), (MW, 19.30, .50)], "calm", LB_MW),
  ("Fort McCoy, Wisconsin, twenty twenty-five: Army combat engineers fire one, on a wide-open range.", [(MW, 31.00, .50), (MW, 62.00, .50), (MW, 66.50, .50)], "calm", LB_MW),
  ("Twentynine Palms, California, June twenty twenty-four: Marine combat engineers launch one in training.", [(MA, 38.00, .50), (MA, 44.70, .45)], "calm", LB_MA),
  ("The line lands across the range, and detonates.", [(MA, 48.50, .50), (MA, 52.00, .50)], "drive", LB_MA),
  ("The smoke from one shot hangs over the training area.", [(MW, 90.50, .50), (MW, 98.50, .50)], "slow", LB_MW),
  ("Would you want to be anywhere near it? Follow for more.", [(MP, 36.00, .50)], "punch", LB_MP),
 ]),
 dict(id="t3", hook="[180 ROUNDS/MIN]<br>SHIP SELF-DEFENSE", title="The Navy's 25 mm Mk 38: up to 180 rounds a minute to defend ships up close (live fire)",
      lines=[
  ("Up to one hundred eighty rounds a minute. This is how a Navy ship defends itself up close.", [(GW, 60.60, .40), (GW, 27.00, .50)], "tense", LB_GW),
  ("The Mark thirty-eight: a twenty-five millimeter machine gun system, for ship self-defense.", [(GB, 4.20, .50), (GB, 8.50, .50)], "punch", LB_GB),
  ("Its targets, per the Navy: fast attack craft, and fast inshore attack craft.", [(GW, 9.00, .50), (GW, 13.00, .50)], "calm", LB_GW),
  ("Effective range: twenty-five hundred yards.", [(GA, 133.00, .50)], "drive", LB_GA),
  ("It fires single shots, or bursts.", [(GA, 137.20, .50)], "punch", LB_GA),
  ("The Mod two version, fielded from two thousand five, is stabilized and remote-controlled.", [(GL, 58.40, .50), (GL, 67.00, .50)], "calm", LB_GL),
  ("Pacific Ocean, August twenty twenty-five: sailors on the carrier Abraham Lincoln run a live-fire exercise.", [(GL, 13.00, .50), (GL, 36.00, .50)], "calm", LB_GL),
  ("The rounds splash down, far out from the ship.", [(GL, 74.20, .50), (GL, 77.00, .50)], "drive", LB_GL),
  ("Mediterranean, August twenty twenty-four: the amphibious assault ship USS Wasp, in a sustainment shoot.", [(GW, 32.40, .45), (GW, 0.40, .50)], "calm", LB_GW),
  ("Twenty seventeen, off Southern California: USS America tests its defenses against a simulated attack by small, fast, unmanned boats.", [(GA, 6.00, .50), (GA, 145.00, .50), (GA, 150.50, .50)], "calm", LB_GA),
  ("The Navy lists it on carriers, cruisers, destroyers, amphibious ships, and Coast Guard cutters.", [(GA, 16.00, .50), (GW, 17.00, .50)], "calm", LB_MK38),
  ("The newest, Mod four, steps up to a thirty millimeter gun, to better defend against drones and fast unmanned boats.", [(GM, 0.30, .55), (GM, 10.60, .50)], "drive", LB_GM),
  ("USS Mustin was the first Navy warship to receive it. Here it fires in a live-fire exercise, in April twenty twenty-six.", [(GM, 16.60, .50), (GM, 6.00, .50)], "calm", LB_GM),
  ("Twenty-five or thirty millimeters: which would you want on deck? Follow for more.", [(GL, 79.00, .50), (GL, 85.00, .50)], "punch", LB_GL),
 ]),
 dict(id="t4", hook="[MACH 1.8+]<br>OFF A CARRIER DECK", title="F/A-18 Super Hornet: Mach 1.8+, two engines with 22,000 lb of thrust each, off a carrier",
      lines=[
  ("Off the deck of an aircraft carrier. Top speed: Mach one point eight plus.", [(FT, 45.10, .50), (FT, 50.20, .50)], "tense", LB_FT),
  ("The F A eighteen Super Hornet: the Navy's twin-engine, multi-mission strike fighter.", [(FT, 0.30, .50), (FT, 7.00, .50)], "punch", LB_FT),
  ("Its jobs: air superiority, escort, reconnaissance, close air support, and precision strike.", [(FT, 21.00, .50), (FT, 30.00, .50)], "calm", LB_FT),
  ("Two General Electric F four-fourteen engines, each with twenty-two thousand pounds of thrust.", [(FT, 35.00, .50), (FT, 39.50, .50)], "drive", LB_FT),
  ("Maximum takeoff weight: sixty-six thousand pounds.", [(FT, 12.00, .50)], "punch", LB_FT),
  ("Unit cost, per Naval Air Systems Command: sixty-seven point four million dollars, in twenty twenty-one money.", [(FK, 71.00, .50)], "calm", LB_FK),
  ("The E model has one seat. The F model, two.", [(FK, 84.40, .50), (FK, 88.80, .50)], "calm", LB_FK),
  ("Combat range, with two Sidewinders: twelve hundred seventy-five nautical miles.", [(FT, 86.00, .50)], "calm", LB_FT),
  ("It first flew in November nineteen ninety-five, and replaced the F-14 Tomcat.", [(FT, 91.00, .50), (FT, 96.50, .50)], "calm", LB_FT),
  ("May twenty twenty-two: Super Hornets on the deck of USS Harry S. Truman, during NATO's Neptune Shield training activity.", [(FT, 24.50, .50), (FT, 16.50, .50)], "calm", LB_FT),
  ("Coming back, they land on the same deck.", [(FT, 61.20, .50), (FT, 65.00, .50)], "punch", LB_FT),
  ("Slowed down: a Super Hornet touches down on Truman.", [(FT, 70.00, .50), (FT, 76.50, .50)], "slow", LB_FT),
  ("July twenty twenty-six: Navy F A eighteen Fs launch in Hawaii, for a sinking exercise at RIMPAC.", [(FK, 99.50, .50), (FK, 104.00, .50)], "calm", LB_FK),
  ("The target: the hulk of the retired amphibious assault ship Peleliu.", [(FK, 110.40, .50), (FK, 113.80, .50)], "calm", LB_FK),
  ("Super Hornet or F-35C: which would you launch first? Follow for more.", [(FK, 118.00, .50), (FK, 124.00, .50)], "punch", LB_FK),
 ]),
 dict(id="t5", hook="[HIT-TO-KILL]<br>IN SPACE", title="An SM-3 Block IIA hit an ICBM-class target in a 2020 test. No explosive warhead",
      lines=[
  ("A Navy destroyer fires a missile built to hit another missile, in space.", [(SJ, 55.45, .50), (SJ, 63.30, .50)], "tense", LB_SJ),
  ("This is the Standard Missile three, Block two A, tested by the Missile Defense Agency and the Navy.", [(SJ, 69.00, .50)], "punch", LB_SJ),
  ("It has no explosive warhead. Its kinetic warhead destroys the target by hitting it.", [(SJ, 137.00, .50)], "calm", LB_SJ),
  ("Raytheon compares the impact to a ten-ton truck, at six hundred miles an hour.", [(SJ, 142.60, .50), (SJ, 147.00, .50)], "drive", LB_SJ),
  ("November twenty twenty. The target, representing an intercontinental ballistic missile, lifts off from Kwajalein Atoll.", [(SJ, 22.90, .50), (SJ, 27.00, .50)], "calm", LB_SJ),
  ("Northeast of Hawaii, the destroyer USS John Finn fires an SM-3 Block two A.", [(SJ, 96.00, .50), (SJ, 100.00, .50)], "calm", LB_SJ),
  ("The ship got its tracking data over a command network, and fired on that remote data.", [(SJ, 160.00, .50)], "calm", LB_SJ),
  ("The missile was first designed for intermediate-range targets. This test showed it could hit an ICBM-class target.", [(SJ, 165.20, .50), (SJ, 106.00, .50)], "calm", LB_SJ),
  ("Block two A is the twenty-one-inch version, developed jointly by the United States and Japan.", [(SK, 38.60, .50)], "calm", LB_SK),
  ("February twenty seventeen, off Hawaii: USS John Paul Jones scored the first intercept of a ballistic missile target with a Block two A.", [(SK, 44.00, .50), (SK, 48.00, .50)], "calm", LB_SK),
  ("That target was a medium-range ballistic missile, launched from Kauai.", [(SK, 2.00, .50), (SK, 18.00, .40)], "calm", LB_SK),
  ("Raytheon says more than four hundred SM-3s, of all versions, have gone to the U.S. and Japanese navies.", [(SJ, 169.00, .50)], "calm", LB_SJ),
  ("A bullet hitting a bullet: impressive, or terrifying? Follow for more.", [(SJ, 31.00, .50), (SJ, 88.00, .50)], "punch", LB_SJ),
 ]),
]
YSHORTS = []

DISPLAY = [("F A eighteen Fs", "F/A-18Fs"), ("fifty thousandth", "50,000th"), ("F A eighteen", "F/A-18"), ("seventeen hundred fifty pounds", "1,750 pounds"), ("Twenty-five or thirty millimeters", "25 or 30 mm"), ("twenty-five hundred meters", "2,500 meters"), ("fifty pounds", "50 pounds"), ("June twenty sixteen", "June 2016"), ("Second Cavalry Regiment", "2nd Cavalry Regiment"),
           ("twenty twenty-three", "2023"), ("October twenty twenty-five", "October 2025"), ("Thirty-First Marine Expeditionary Unit", "31st Marine Expeditionary Unit"),
           ("nineteen ninety-six", "1996"), ("twenty twenty-one", "2021"), ("fifty thousand", "50,000"),
           ("M fifty-eight", "M58"), ("C four", "C-4"),
           ("one hundred meters", "100 meters"), ("one hundred meter", "100-meter"), ("fourteen to sixteen meters", "14 to 16 meters"), ("First Cavalry Division", "1st Cavalry Division"),
           ("thirty-six hundred pounds", "3,600 pounds"), ("twenty twenty-five", "2025"), ("twenty twenty-four", "2024"),
           ("one hundred eighty rounds", "180 rounds"), ("Mark thirty-eight", "Mk 38"), ("twenty-five millimeter", "25 mm"), ("twenty-five hundred yards", "2,500 yards"),
           ("Mod two", "Mod 2"), ("Mod three", "Mod 3"), ("Mod four", "Mod 4"), ("two thousand five", "2005"), ("Twenty seventeen", "2017"), ("twenty eighteen", "2018"),
           ("three hundred forty-one", "341"), ("thirty millimeter", "30 mm"), ("April twenty twenty-six", "April 2026"),
           ("Mach one point eight plus", "Mach 1.8+"), ("F four-fourteen", "F414"), ("twenty-two thousand pounds", "22,000 pounds"), ("sixty-six thousand pounds", "66,000 pounds"),
           ("sixty-seven point four million dollars", "$67.4 million"), ("twelve hundred seventy-five", "1,275"), ("nineteen ninety-five", "1995"),
           ("May twenty twenty-two", "May 2022"), ("July twenty twenty-six", "July 2026"),
           ("Standard Missile three, Block two A", "Standard Missile-3 Block IIA"), ("Block two A", "Block IIA"), ("ten-ton", "10-ton"), ("six hundred miles", "600 miles"),
           ("November twenty twenty", "November 2020"), ("twenty-one-inch", "21-inch"), ("February twenty seventeen", "February 2017"),
           ("more than thirty", "more than 30"), ("four hundred", "400"), ("Twentynine Palms", "Twentynine Palms")]
