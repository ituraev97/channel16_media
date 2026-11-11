# CHANNEL 16 · MILITARY HARDWARE · m014 (TikTok only, Fri Nov 13, 2026). Five vertical videos t1–t5, 62–75 s each.
# Exercises, tests, training and demonstrations only. Facts: sources.md. shot: (clip_id, start, cx)
P_WS = 902897    # Patriot live-fire B-roll (U.S. Army, released Nov 2023): six launches, desert range
P_PAL = 891073   # Patriot live fire, Northern Edge 23-2, Palau, July 17, 2023 (24p)
P_TS = 807095    # MIM-104 Patriot live fire, Talisman Sabre 21, Camp Growl, Queensland, Australia, July 17, 2021
P_RO = 800437    # Patriot live fire with Romanian allies, Capu Midia, Romania, June 9, 2021
B_STW = 953176   # 3-67 AR M2A3 Bradley Table VI live fire, Fort Stewart, Ga., Feb 20, 2025
B_HOOD = 1021131 # M2A3 Bradley gunnery table certification, Fort Hood, Texas, Aug 27, 2026 (vertical original)
B_GRAF = 1013085 # 370th CEC-A Bradley crew gunnery, Grafenwoehr Training Area, Germany, May 13, 2026
F_JB20 = 772463  # F-22 Raptor Demonstration Team, JBER, Alaska (2020) (24p)
F_JB22 = 852895  # F-22 aerial demonstration, Arctic Thunder Open House, JBER, Alaska, July 31, 2022
F_CBM = 781084   # F-22 Airpower Demo, Columbus AFB, Miss. (Jan 2021)
F_MIA = 964538   # F-22 demo team commander, cockpit view, Hyundai Air and Sea Show, Miami, May 24, 2025 (vertical original)
S_CT = 591550    # USS Connecticut (SSN 22) surfaced in the Arctic Ocean, ICEX 2018, Beaufort Sea, March 21, 2018
S_HF = 591554    # USS Hartford (SSN 768) surfacing in the Arctic Ocean, ICEX 2018, Beaufort Sea, March 21, 2018
S_TO = 742094    # USS Toledo (SSN 769) surfaces through the ice at Ice Camp Seadragon, ICEX 2020
K_NE = 683099    # KC-10 refuels a B-2 Spirit (and Navy jets), exercise Northern Edge, JBER, Alaska, May 23, 2019
K_TR = 827578    # 70th ARS (Travis AFB) air refuels a B-2, Jan 1, 2022 (Rose Parade flyover support)
K_AM = 935141    # B-2 Bomber Task Force takeoffs and landings, RAAF Base Amberley, Australia, Aug 23, 2024
K_AMT = 936030   # B-2s taxi and take off, Bomber Task Force, RAAF Base Amberley, Sept 3, 2024
K_RF = 781914    # B-2 leads Red Flag 21-1 takeoffs, Nellis AFB, Nev., Jan 26, 2021

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

LB_WS = dict(label="PATRIOT · U.S. ARMY LIVE FIRE · RELEASED NOV 2023")
LB_PAL = dict(label="PALAU · EXERCISE NORTHERN EDGE · JULY 2023")
LB_TS = dict(label="QUEENSLAND, AUSTRALIA · TALISMAN SABRE · JULY 2021")
LB_RO = dict(label="ROMANIA · LIVE-FIRE EXERCISE · JUNE 2021")
LB_STW = dict(label="FORT STEWART, GA. · LIVE-FIRE GUNNERY · FEB 2025")
LB_HOOD = dict(label="FORT HOOD, TEXAS · GUNNERY CERTIFICATION · AUG 2026")
LB_GRAF = dict(label="GRAFENWOEHR, GERMANY · CREW GUNNERY · MAY 2026")
LB_JB20 = dict(label="JBER, ALASKA · F-22 DEMO TEAM · RELEASED 2020")
LB_JB22 = dict(label="JBER, ALASKA · AIR SHOW DEMONSTRATION · JULY 2022")
LB_CBM = dict(label="COLUMBUS AFB, MISS. · F-22 DEMO · RELEASED JAN 2021")
LB_MIA = dict(label="MIAMI · AIR AND SEA SHOW · MAY 2025")
LB_CT = dict(label="USS CONNECTICUT · ICE EXERCISE 2018 · ARCTIC OCEAN")
LB_HF = dict(label="USS HARTFORD · ICE EXERCISE 2018 · ARCTIC OCEAN")
LB_TO = dict(label="USS TOLEDO · ICE EXERCISE 2020 · ICE CAMP SEADRAGON")
LB_NE = dict(label="EXERCISE NORTHERN EDGE · ALASKA · MAY 2019")
LB_TR = dict(label="TRAVIS AFB TANKER · B-2 REFUELING · JAN 2022")
LB_AM = dict(label="RAAF BASE AMBERLEY · BOMBER TASK FORCE · 2024")
LB_RF = dict(label="NELLIS AFB, NEV. · RED FLAG 21-1 · JAN 2021")

SHORTS = [
 dict(id="t1", hook="[5,000 KM/H]<br>PATRIOT INTERCEPTOR", title="A Patriot interceptor leaves its launcher. Up to 16 PAC-3 missiles per launcher, per NATO",
      lines=[
  ("That's a Patriot interceptor, leaving its launcher during a U.S. Army live fire.", [(P_WS, 42.12, .16), (P_WS, 45.30, .30)], "tense", LB_WS),
  ("Patriot stands for Phased Array Tracking Radar to Intercept on Target.", [(P_PAL, 12.45, .50), (P_PAL, 52.70, .50)], "punch", LB_PAL),
  ("It's a surface-to-air system, built to defend against aircraft and missiles.", [(P_WS, 16.60, .15), (P_WS, 36.60, .20)], "calm", LB_WS),
  ("A battery includes a radar, an engagement control station, and launchers.", [(P_TS, 42.60, .50), (P_TS, 29.00, .50)], "calm", LB_TS),
  ("The control station is the only crewed station. It calculates the interceptor's path.", [(P_TS, 34.10, .45), (P_TS, 56.40, .50)], "calm"),
  ("Per NATO, one launcher carries four PAC-2 missiles, or up to sixteen PAC-3s.", [(P_RO, 0.90, .40), (P_RO, 4.10, .40)], "punch", LB_RO),
  ("PAC-2 explodes close to its target. PAC-3 hits it directly. That's called hit-to-kill.", [(P_WS, 22.85, .15), (P_WS, 55.95, .12)], "drive", LB_WS),
  ("Speed, per NATO: five thousand kilometers an hour. That's more than three thousand miles an hour.", [(P_WS, 2.72, .10), (P_TS, 105.30, .50)], "punch"),
  ("Radar range: more than one hundred fifty kilometers.", [(P_PAL, 49.50, .35)], "calm", LB_PAL),
  ("In Palau, in July twenty twenty-three, a Patriot battery engaged a cruise missile surrogate target.", [(P_PAL, 15.00, .50), (P_PAL, 18.76, .50), (P_PAL, 27.80, .50)], "calm", LB_PAL),
  ("In Queensland, during Talisman Sabre twenty twenty-one, U.S. soldiers fired Patriot in Australia for the first time.", [(P_TS, 108.50, .50), (P_TS, 112.10, .50)], "calm", LB_TS),
  ("And in Romania, in June twenty twenty-one: a live fire alongside Romanian allies.", [(P_RO, 62.70, .60), (P_RO, 67.80, .50)], "tense", LB_RO),
  ("Missile length, per NATO: five point two meters. Weight: three hundred twenty kilograms.", [(P_WS, 75.80, .25), (P_WS, 79.00, .25)], "calm", LB_WS),
  ("Which air defense system should we break down next? Follow for more.", [(P_WS, 103.40, .40)], "punch", LB_WS),
 ]),
 dict(id="t2", hook="[25MM]<br>CHAIN GUN ON TRACKS", title="The M2A3 Bradley: a 25mm chain gun, a TOW launcher and six infantrymen aboard",
      lines=[
  ("Watch the smoke. That's a Bradley Fighting Vehicle, firing during live-fire gunnery.", [(B_STW, 147.00, .30)], "tense", LB_STW),
  ("The Bradley Fighting Vehicle carries infantry onto the battlefield, and gives them fire support.", [(B_HOOD, 21.50, .50), (B_HOOD, 25.00, .50)], "calm", LB_HOOD),
  ("A three-man crew, plus six infantrymen.", [(B_HOOD, 3.80, .50)], "punch"),
  ("Its main gun: the M242 Bushmaster, a twenty-five-millimeter chain gun.", [(B_GRAF, 45.80, .50)], "punch", LB_GRAF),
  ("It also carries a TOW missile launcher, and a seven-point-six-two-millimeter machine gun.", [(B_HOOD, 9.50, .50), (B_GRAF, 39.20, .50)], "drive"),
  ("Optics and electronics help the crew find targets.", [(B_HOOD, 30.50, .50)], "calm", LB_HOOD),
  ("The Army built it to keep pace with the Abrams tank.", [(B_GRAF, 19.40, .45), (B_GRAF, 24.50, .50)], "calm", LB_GRAF),
  ("This is Fort Stewart, Georgia, in February twenty twenty-five. A Table Six live fire.", [(B_STW, 18.50, .95), (B_STW, 24.00, .95)], "calm", LB_STW),
  ("Table Six evaluates whether crews can engage both moving and stationary targets.", [(B_STW, 33.90, .40), (B_STW, 37.50, .40)], "drive"),
  ("Crews qualify by day, and by night.", [(B_STW, 113.20, .50)], "punch"),
  ("Pass, and they move up to squad, section and platoon live fires.", [(B_STW, 108.50, .50), (B_STW, 155.00, .50)], "calm"),
  ("Fort Hood, Texas, August twenty twenty-six: gunnery table certification.", [(B_HOOD, 48.00, .50), (B_HOOD, 54.90, .50)], "calm", LB_HOOD),
  ("And Graf-en-vur, Germany, in May twenty twenty-six.", [(B_GRAF, 66.50, .50), (B_GRAF, 52.40, .15)], "calm", LB_GRAF),
  ("In September twenty twenty-five, the Army issued more than one hundred M2A3s to soldiers of the Seventh Cavalry Regiment, for a rotation in Poland.", [(B_STW, 84.50, .50), (B_STW, 91.00, .50)], "calm"),
  ("One more burst.", [(B_STW, 168.10, .50)], "punch"),
  ("Bradley or Abrams: which would you rather crew? Follow for more.", [(B_STW, 160.00, .50)], "punch", LB_STW),
 ]),
 dict(id="t3", hook="[MACH 1.5+]<br>NO AFTERBURNER", title="The F-22 Raptor cruises above Mach 1.5 without afterburner. Air Force demo footage",
      lines=[
  ("Watch this fighter climb straight up. This is the F-22 Raptor.", [(F_JB20, 56.30, .50), (F_JB20, 59.60, .50)], "tense", LB_JB20),
  ("An Air Force stealth fighter, flown by one pilot.", [(F_JB20, 63.00, .70)], "punch", LB_JB20),
  ("It can cruise faster than Mach one point five without afterburner. The Air Force calls that supercruise.", [(F_JB22, 0.60, .55), (F_JB22, 31.50, .60)], "drive", LB_JB22),
  ("Top speed: Mach two class.", [(F_JB22, 89.50, .50)], "punch"),
  ("Two Pratt and Whitney F119 engines, each in the thirty-five-thousand-pound thrust class.", [(F_JB22, 69.00, .50), (F_JB22, 73.50, .50)], "drive"),
  ("Their nozzles can be steered. That's thrust vectoring, and the Air Force says it helps the Raptor outmaneuver other aircraft.", [(F_JB20, 45.90, .50), (F_JB20, 50.30, .55), (F_JB20, 52.80, .50)], "calm", LB_JB20),
  ("Its missiles ride inside the jet: six AMRAAMs and two Sidewinders, in the air-to-air setup.", [(F_JB20, 73.50, .55), (F_JB20, 76.25, .75)], "calm", LB_JB20),
  ("Plus a twenty-millimeter cannon, with four hundred eighty rounds.", [(F_JB22, 147.00, .50)], "punch", LB_JB22),
  ("Wingspan: forty-four and a half feet. Maximum takeoff weight: eighty-three thousand five hundred pounds.", [(F_JB22, 171.00, .55), (F_JB22, 178.00, .50)], "calm"),
  ("Ceiling: above fifty thousand feet.", [(F_CBM, 45.00, .50)], "punch", LB_CBM),
  ("This is the F-22 Demonstration Team, over Joint Base Elmendorf-Richardson, Alaska.", [(F_JB20, 84.40, .50), (F_JB20, 88.90, .50)], "calm", LB_JB20),
  ("And this is the view from the cockpit, during a demonstration over Miami.", [(F_MIA, 1.00, .50), (F_MIA, 7.00, .50)], "tense", LB_MIA),
  ("The demo team flies these maneuvers at air shows around the world.", [(F_MIA, 15.00, .50), (F_MIA, 21.00, .50)], "calm", LB_MIA),
  ("The F-22 reached initial operational capability in December two thousand five. Unit cost, per an Air Force fact sheet: about one hundred forty-three million dollars.", [(F_JB22, 241.00, .50), (F_JB22, 276.00, .50)], "calm", LB_JB22),
  ("Raptor or F-35: which would you rather fly? Follow for more.", [(F_JB22, 156.00, .50)], "punch"),
 ]),
 dict(id="t4", hook="[9,138 TONS]<br>THROUGH THE ICE", title="A 353-foot Navy submarine surfaced through Arctic ice. This is USS Connecticut",
      lines=[
  ("That's the sail of a nuclear submarine, sticking up through the Arctic ice.", [(S_CT, 33.50, .50), (S_CT, 49.00, .40)], "tense", LB_CT),
  ("USS Connecticut, a Seawolf-class fast-attack submarine, in the Beaufort Sea, north of Alaska.", [(S_CT, 38.00, .50), (S_CT, 42.00, .50)], "calm", LB_CT),
  ("It surfaced during Ice Exercise twenty eighteen, a five-week Navy exercise in the Arctic.", [(S_CT, 52.00, .40), (S_CT, 56.50, .40)], "calm"),
  ("The Navy calls the Seawolf class exceptionally quiet, fast, and well armed.", [(S_CT, 64.00, .50), (S_CT, 68.00, .50)], "punch"),
  ("Connecticut is three hundred fifty-three feet long, and displaces nine thousand one hundred thirty-eight tons submerged.", [(S_CT, 103.00, .50), (S_CT, 109.00, .50)], "calm"),
  ("One nuclear reactor. Speed: more than twenty-five knots.", [(S_CT, 82.00, .50)], "drive"),
  ("Eight torpedo tubes, and room for up to fifty weapons in the torpedo room.", [(S_CT, 86.00, .50), (S_CT, 99.50, .50)], "calm"),
  ("A crew of one hundred forty.", [(S_CT, 113.00, .50)], "punch"),
  ("A second U.S. submarine surfaced in the exercise too: USS Hartford, a Los Angeles-class boat.", [(S_HF, 85.00, .50), (S_HF, 90.00, .50)], "calm", LB_HF),
  ("That's ice, still sitting on top of its sail.", [(S_HF, 93.50, .50)], "tense", LB_HF),
  ("Crews walk out across the ice to the boat.", [(S_HF, 100.50, .50), (S_HF, 106.00, .50)], "calm"),
  ("The exercise ran from a temporary ice camp, built on a moving ice floe, about one hundred fifty miles off Alaska's north slope.", [(S_HF, 160.00, .50), (S_HF, 246.00, .50)], "calm", LB_HF),
  ("In twenty twenty, USS Toledo surfaced through the ice at Ice Camp Seadragon.", [(S_TO, 28.00, .50), (S_TO, 33.00, .50)], "calm", LB_TO),
  ("According to the Navy, the first Arctic surfacing was made by USS Skate, in March nineteen fifty-nine.", [(S_TO, 40.00, .60), (S_TO, 46.00, .60)], "calm", LB_TO),
  ("One more look at Connecticut.", [(S_CT, 172.00, .50)], "slow", LB_CT),
  ("Submarine or icebreaker: which would you rather take through the Arctic? Follow for more.", [(S_CT, 195.00, .50)], "punch", LB_CT),
 ]),
 dict(id="t5", hook="[$1.157 BILLION]<br>REFUELING MIDAIR", title="The B-2 Spirit stealth bomber refueling midair: about $1.157 billion each (1998 dollars)",
      lines=[
  ("This stealth bomber cost more than a billion dollars apiece, in nineteen ninety-eight dollars. And it's taking on fuel in midair.", [(K_NE, 178.00, .50), (K_NE, 184.10, .50)], "tense", LB_NE),
  ("The B-2 Spirit. A flying wing, flown by just two pilots. A B-52 has a crew of five.", [(K_NE, 136.90, .50), (K_NE, 140.60, .50)], "punch", LB_NE),
  ("The fuel boom of an Air Force KC-10 tanker connects to the top of the bomber.", [(K_NE, 156.00, .50), (K_NE, 160.00, .50)], "calm", LB_NE),
  ("This was exercise Northern Edge, in Alaska, in May twenty nineteen.", [(K_NE, 196.50, .50), (K_NE, 200.50, .50)], "calm", LB_NE),
  ("Without refueling, its range is about six thousand nautical miles.", [(K_AM, 5.60, .55)], "punch", LB_AM),
  ("Wingspan: one hundred seventy-two feet. Length: only sixty-nine.", [(K_NE, 205.00, .50), (K_NE, 208.50, .50)], "calm", LB_NE),
  ("Four General Electric F118 engines, seventeen thousand three hundred pounds of thrust each.", [(K_AMT, 64.00, .55), (K_AMT, 68.00, .55)], "drive", LB_AM),
  ("Payload: sixty thousand pounds. Ceiling: fifty thousand feet.", [(K_AMT, 39.50, .45), (K_AMT, 42.90, .50)], "calm", LB_AM),
  ("Its stealth comes from reducing its radar, infrared, acoustic, electromagnetic and visual signatures.", [(K_TR, 41.00, .45), (K_TR, 44.10, .45)], "calm", LB_TR),
  ("Here, a tanker crew from Travis Air Force Base passed a B-2 fifty-five thousand pounds of fuel, on New Year's Day twenty twenty-two.", [(K_TR, 57.60, .50), (K_TR, 61.70, .50)], "calm", LB_TR),
  ("And these B-2s are on a Bomber Task Force deployment to Amberley, Australia, in twenty twenty-four.", [(K_AM, 66.50, .60), (K_AMT, 24.00, .50)], "calm", LB_AM),
  ("Unit cost, per the Air Force: about one point one five seven billion dollars, in nineteen ninety-eight dollars.", [(K_NE, 219.90, .50), (K_NE, 193.10, .50)], "punch", LB_NE),
  ("B-2 or B-52: which bomber impresses you more? Follow for more.", [(K_NE, 171.00, .50)], "punch", LB_NE),
 ]),
]
YSHORTS = []

DISPLAY = [("five thousand kilometers an hour", "5,000 km/h"), ("three thousand miles", "3,000 miles"), ("one hundred fifty kilometers", "150 km"),
           ("four PAC-2", "4 PAC-2"), ("sixteen PAC-3s", "16 PAC-3s"), ("twenty twenty-three", "2023"), ("twenty twenty-one", "2021"),
           ("mid-nineteen-eighties", "mid-1980s"), ("five point two meters", "5.2 meters"), ("three hundred twenty kilograms", "320 kg"),
           ("twenty-five-millimeter", "25mm"), ("seven-point-six-two-millimeter", "7.62mm"), ("twenty twenty-five", "2025"), ("twenty twenty-six", "2026"),
           ("Table Six", "Table VI"), ("one hundred M2A3s", "100 M2A3s"), ("Seventh Cavalry", "7th Cavalry"), ("Graf-en-vur", "Grafenwöhr"),
           ("Mach one point five", "Mach 1.5"), ("Mach two", "Mach 2"), ("Pratt and Whitney", "Pratt & Whitney"), ("thirty-five-thousand-pound", "35,000-pound"),
           ("twenty-millimeter", "20mm"), ("four hundred eighty", "480"), ("forty-four and a half", "44.5"), ("eighty-three thousand five hundred", "83,500"),
           ("fifty thousand", "50,000"), ("two thousand five", "2005"), ("one hundred forty-three million dollars", "$143 million"),
           ("twenty eighteen", "2018"), ("three hundred fifty-three", "353"), ("nine thousand one hundred thirty-eight", "9,138"), ("twenty-five knots", "25 knots"),
           ("up to fifty", "up to 50"), ("one hundred forty", "140"), ("one hundred fifty miles", "150 miles"), ("twenty twenty,", "2020,"), ("nineteen fifty-nine", "1959"),
           ("six thousand nautical", "6,000 nautical"), ("one hundred seventy-two", "172"), ("sixty-nine", "69"), ("seventeen thousand three hundred", "17,300"),
           ("sixty thousand", "60,000"), ("three hundred thirty-six thousand five hundred", "336,500"), ("fifty-five thousand", "55,000"),
           ("twenty twenty-two", "2022"), ("twenty twenty-four", "2024"), ("nineteen ninety-three", "1993"), ("twenty nineteen", "2019"),
           ("one point one five seven billion dollars", "$1.157 billion"), ("nineteen ninety-eight dollars", "1998 dollars")]
