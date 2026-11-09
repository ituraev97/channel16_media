# CHANNEL 16 · MILITARY HARDWARE · m011 (TikTok only, Nov 10, 2026). Five vertical videos t1–t5, 62–75 s each (Creator Rewards needs > 1 min).
# Exercises, tests and training only. Facts: sources.md. shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop inside the active picture (0..1)
CIWS_N24 = 934763    # USS Nimitz (CVN 68), Phalanx CIWS live fire, Aug 1, 2024, Pacific (MC3 Tomas Valdes)
CIWS_N26 = 999801    # USS Nimitz, Mk 15 Phalanx live-fire exercise, Mar 16, 2026, Pacific (MC2 Edward Jacome)
CIWS_GB = 994248     # USS George H.W. Bush (CVN 77), Phalanx live-fire exercise, Nov 7, 2025, Atlantic (slate 0–5 s: never used)
SINK_A = 851655      # RIMPAC 2022 SINKEX #2: ex-USS Denver (LPD 9) sunk July 22, 2022 (targeting video 48–87 s)
SINK_L = 851314      # RIMPAC 2022 SINKEX: JGSDF Type 12 + NMESIS fire from Kauai, July 22, 2022
A10_NV = 858493      # A-10s, 422nd Test and Evaluation Squadron, strafing run, Nevada Test and Training Range, Sept 13, 2022
A10_CK = 593024      # A-10C Demo Team commander, strafe runs, southern Arizona, Mar 21, 2018 (cockpit camera)
A10_AZ = "492253a"   # A-10s from Luke AFB strafing at Barry M. Goldwater Range, Nov 9, 2016 (cut 825–888 s of DVIDS 492253)
HIM_KS = 940463      # HIMARS, A Btry 2-300th FA, Fort Riley, Kansas, Aug 15, 2024
HIM_MI = 698988      # HIMARS night live fire, 2-182 FA Michigan NG, Northern Strike 19, Camp Grayling, July 24–25, 2019
MM_S20 = 765660      # unarmed Minuteman III operational test launch GT 233GM, Vandenberg, Sep 2, 2020, 12:03 a.m. PDT
MM_S20D = "765660d"  # 765660 20.6–25.1 s, duplicate frames removed (mpdecimate + minterpolate)
MM_F20 = 737827      # unarmed Minuteman III developmental test launch, Vandenberg, Feb 5, 2020, 12:33 a.m. PT
A10_AZ_ = A10_AZ

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

L_N24 = dict(label="USS NIMITZ · LIVE-FIRE EXERCISE · AUG 2024")
L_N26 = dict(label="USS NIMITZ · LIVE-FIRE EXERCISE · MAR 2026")
L_GB = dict(label="USS GEORGE H.W. BUSH · LIVE-FIRE EXERCISE · NOV 2025")
L_SINK = dict(label="SINKING EXERCISE (SINKEX) · RIMPAC 2022")
L_KAUAI = dict(label="KAUAI, HAWAII · RIMPAC 2022 SINKEX")
L_NV = dict(label="NEVADA TEST AND TRAINING RANGE · 2022")
L_CK = dict(label="A-10 DEMO TEAM · TRAINING · ARIZONA, 2018")
L_AZ = dict(label="BARRY M. GOLDWATER RANGE · ARIZONA · 2016")
L_KS = dict(label="FORT RILEY, KANSAS · TRAINING · AUG 2024")
L_MI = dict(label="NORTHERN STRIKE EXERCISE · MICHIGAN · 2019")
L_MM1 = dict(label="VANDENBERG · UNARMED TEST LAUNCHES · 2020")
L_MM2 = dict(label="VANDENBERG · UNARMED TEST LAUNCH · FEB 2020")

SHORTS = [
 dict(id="t1", hook="[4,500]<br>ROUNDS A MINUTE", title="This Navy gun fires 4,500 rounds a minute and can do the whole job by itself",
      lines=[
  ("This is the last line of defense on a U.S. Navy aircraft carrier. Listen.", [(CIWS_N24, 55.50, .52), (CIWS_N24, 101.50, .40)], "tense", L_N24),
  ("It's called Phalanx. The Mark fifteen Close-In Weapon System.", [(CIWS_N26, 13.00, .50)], "punch"),
  ("A radar-guided, twenty-millimeter Gatling gun, built to stop anti-ship missiles that get past other fleet defenses.", [(CIWS_N26, 29.00, .55), (CIWS_N26, 33.50, .55)], "drive", L_N26),
  ("Against missiles and aircraft, the Navy lists its rate of fire at four thousand five hundred rounds a minute.", [(CIWS_N24, 121.50, .40), (CIWS_N24, 139.80, .40)], "punch"),
  ("The magazine holds fifteen hundred and fifty rounds. At that rate, about twenty seconds of fire.", [(CIWS_N26, 38.00, .55)], "tense"),
  ("What makes it different: it can do the whole job by itself.", [(CIWS_N24, 154.00, .40)], "slow"),
  ("Search. Detect. Track. Engage. Then it checks whether the target was destroyed.", [(CIWS_N24, 9.00, .55), (CIWS_N24, 17.00, .55)], "drive"),
  ("The current version, Block One B, added an electro-optical sensor.", [(CIWS_N26, 45.00, .50)], "calm"),
  ("So it can also take on small, fast boats, helicopters and drones.", [(CIWS_N24, 200.00, .45)], "tense"),
  ("The whole mount weighs about thirteen thousand six hundred pounds.", [(CIWS_N24, 236.00, .40)], "calm"),
  ("Phalanx first went to sea in nineteen eighty, aboard the carrier USS Coral Sea.", [(CIWS_N24, 270.00, .40)], "calm"),
  ("This is the carrier George H.W. Bush, firing hers in the Atlantic, November twenty twenty-five.", [(CIWS_GB, 6.00, .58), (CIWS_GB, 14.60, .58)], "calm", L_GB),
  ("And back aboard Nimitz, another burst over the Pacific.", [(CIWS_N24, 250.50, .40)], "tense", L_N24),
  ("Four thousand five hundred rounds a minute. Would you fly a missile into that? Follow for more.", [(CIWS_N24, 305.00, .40)], "punch"),
 ]),
dict(id="t2", hook="WHAT IT TAKES<br>TO [SINK] A WARSHIP", title="What it took to sink a retired U.S. Navy warship (RIMPAC 2022 SINKEX)",
      lines=[
  ("This is a real ex-U.S. Navy warship, rolling over in the Pacific. And it was planned.", [(SINK_A, 80.20, .50), (SINK_L, 5.80, .72)], "tense", L_SINK),
  ("She's the ex-USS Denver, commissioned in nineteen sixty-eight. In April nineteen seventy-five, she played a significant role in the evacuation of Saigon.", [(SINK_A, 73.20, .50), (SINK_A, 60.85, .50)], "calm", L_SINK),
  ("She was decommissioned in twenty fourteen, after forty-six years, as the oldest deployable warship in the Navy.", [(SINK_A, 65.35, .50), (SINK_A, 69.70, .50)], "slow"),
  ("In July twenty twenty-two, she became the target of a sinking exercise, a SINKEX, during RIMPAC.", [(SINK_A, 23.00, .50), (SINK_L, 12.00, .65)], "drive"),
  ("First, the hull was cleaned. Fuel, mercury, PCBs and trash came out.", [(SINK_L, 17.50, .65)], "calm"),
  ("The site: more than fifty nautical miles north of Kauai, over water more than fifteen thousand feet deep.", [(SINK_A, 26.75, .50), (SINK_A, 29.90, .50)], "calm"),
  ("From the shore of Kauai, a Japanese Type twelve launcher and a U.S. NMESIS launcher fired anti-ship missiles.", [(SINK_L, 0.50, .72), (SINK_L, 27.50, .62)], "drive", L_KAUAI),
  ("Twenty-six nations and thirty-eight ships took part in RIMPAC that summer.", [(SINK_L, 45.00, .55)], "calm"),
  ("From the air and sea: Super Hornets, Army Apaches, Marine Hornets, and the five-inch gun of the destroyer USS Chaffee.", [(SINK_A, 41.50, .50), (SINK_A, 38.15, .50)], "drive"),
  ("This is what the targeting cameras saw.", [(SINK_A, 48.50, .50)], "punch", L_SINK),
  ("Hit after hit, on an empty, decommissioned hull.", [(SINK_A, 51.20, .50)], "tense"),
  ("And more missiles kept coming from shore.", [(SINK_A, 55.00, .70)], "drive", L_KAUAI),
  ("Forty-six years of service, and one last job. What would you have sent first? Follow for more.", [(SINK_L, 60.00, .55)], "punch"),
 ]),
 dict(id="t3", hook="SEVEN BARRELS<br>[30 MM]", title="The A-10's gun fires 3,900 rounds a minute. This is a strafing run on a test range",
      lines=[
  ("Watch the ground. That dust is an A-10 strafing run, on a training range in Nevada.", [(A10_NV, 41.00, .55), (A10_NV, 36.00, .30)], "tense", L_NV),
  ("The A-10C Thunderbolt Two. The first Air Force aircraft designed specifically for close air support of ground forces.", [(A10_NV, 0.30, .45), (A10_NV, 8.00, .45)], "calm"),
  ("Its main weapon: a thirty-millimeter GAU-8 Gatling gun, with seven barrels.", [(A10_NV, 12.00, .40)], "punch"),
  ("The Air Force says it can fire three thousand nine hundred rounds a minute.", [(A10_NV, 29.00, .40), (A10_NV, 47.00, .55)], "drive"),
  ("The pilot sits behind titanium armor, which also protects parts of the flight controls.", [(A10_CK, 5.00, .50)], "calm", L_CK),
  ("The jet can survive direct hits from armor-piercing and high-explosive rounds up to twenty-three millimeters.", [(A10_CK, 20.00, .50), (A10_NV, 17.00, .45)], "tense"),
  ("It can carry up to sixteen thousand pounds of mixed ordnance.", [(A10_NV, 20.40, .45)], "calm"),
  ("Fully loaded, it can weigh up to fifty-one thousand pounds at takeoff.", [(A10_NV, 23.90, .45)], "calm"),
  ("Listed speed on the fact sheet: four hundred twenty miles an hour.", [(A10_AZ, 44.40, .45)], "drive", L_AZ),
  ("And it can take off and land on short strips, close to the front lines.", [(A10_AZ, 14.00, .40)], "calm", L_AZ),
  ("The first A-10s entered service in March nineteen seventy-six.", [(A10_NV, 30.90, .45)], "calm"),
  ("The fact sheet lists about two hundred eighty-one in the total force.", [(A10_CK, 40.00, .50)], "calm"),
  ("Back over Nevada. Another pass, another wall of dust.", [(A10_NV, 54.00, .55), (A10_NV, 57.50, .55)], "tense", L_NV),
  ("Seven barrels, thirty millimeters, fifty years in service.", [(A10_NV, 63.00, .55)], "punch"),
  ("Would you rather fly it, or hear it? Follow for more.", [(A10_CK, 46.00, .50), (A10_NV, 66.70, .55)], "punch"),
 ]),
 dict(id="t4", hook="SIX ROCKETS<br>[ONE TRUCK]", title="Six rockets on one truck: the Army's HIMARS in a live-fire exercise",
      lines=[
  ("Six rockets. One truck. This is HIMARS, firing on a training range in Kansas.", [(HIM_KS, 242.60, .80), (HIM_KS, 225.60, .45)], "tense", L_KS),
  ("The M142 High Mobility Artillery Rocket System.", [(HIM_KS, 254.00, .80)], "punch"),
  ("Its launcher carries one pod of six rockets. The older, tracked MLRS carries two.", [(HIM_KS, 258.40, .55), (HIM_KS, 209.50, .55)], "drive"),
  ("Or, instead of the rockets: one ATACMS missile, or two Precision Strike Missiles.", [(HIM_KS, 216.60, .40)], "calm"),
  ("It fires the same family of munitions as the MLRS, and it can move by rail or by air.", [(HIM_KS, 192.50, .50)], "calm"),
  ("That rocket pod alone weighs about five thousand pounds.", [(HIM_KS, 183.80, .50)], "calm"),
  ("It all rides on a five-ton truck chassis, lighter than the tracked MLRS.", [(HIM_KS, 157.00, .50)], "calm"),
  ("And it was built to fit inside a C-130 cargo plane.", [(HIM_KS, 266.00, .50)], "punch"),
  ("The Army says it can roll off an aircraft, fire, and be loaded back on in a matter of minutes.", [(HIM_KS, 221.20, .55), (HIM_KS, 229.70, .45)], "drive"),
  ("In Kansas, soldiers of the second battalion, three hundredth field artillery fired it in August twenty twenty-four.", [(HIM_KS, 203.00, .50), (HIM_KS, 236.90, .50)], "calm"),
  ("This is the same system at night. Michigan, Exercise Northern Strike, July twenty nineteen.", [(HIM_MI, 46.80, .80), (HIM_MI, 52.00, .80)], "tense", L_MI),
  ("Each launch lights up the whole range.", [(HIM_MI, 94.80, .80)], "slow", L_MI),
  ("Back in Kansas, the launcher rolls out.", [(HIM_KS, 247.20, .45)], "drive", L_KS),
  ("Six rockets, one truck, one cargo plane.", [(HIM_KS, 261.20, .40)], "punch"),
  ("Which system should we show next? Tell me in the comments, and follow for more.", [(HIM_KS, 304.00, .50)], "punch"),
 ]),
 dict(id="t5", hook="[15,000] MPH<br>AT BURNOUT", title="Minuteman III: 15,000 mph at burnout, deployed since 1970 (unarmed test launch)",
      lines=[
  ("Midnight at Vandenberg, California. This is an unarmed Minuteman Three, on a test launch.", [(MM_S20, 14.70, .52), (MM_F20, 17.90, .55)], "tense", L_MM1),
  ("An intercontinental ballistic missile, fired from an underground silo.", [(MM_S20, 23.60, .50), (MM_F20, 20.80, .55)], "calm", L_MM1),
  ("At burnout, it's moving at about fifteen thousand miles an hour. Roughly Mach twenty-three.", [(MM_S20, 25.65, .50), (MM_S20, 28.70, .58)], "punch"),
  ("Its range: more than six thousand miles. Its ceiling: about seven hundred miles up.", [(MM_S20, 32.00, .50), (MM_S20, 35.00, .50)], "drive"),
  ("It weighs about seventy-nine thousand pounds, and has three solid-fuel rocket stages.", [(MM_S20, 38.00, .50), (MM_S20, 41.00, .50)], "calm"),
  ("Tracking cameras follow it up through the night sky.", [(MM_S20, 44.50, .50)], "slow"),
  ("Minuteman Three was first deployed in June nineteen seventy. Production ended in December nineteen seventy-eight.", [(MM_F20, 23.20, .55), (MM_F20, 26.50, .55)], "calm", L_MM2),
  ("The Air Force keeps four hundred of them, across three missile wings.", [(MM_F20, 30.30, .55)], "calm"),
  ("Each silo is hardened, and linked by hardened cables to an underground launch control center.", [(MM_F20, 34.90, .55), (MM_F20, 41.00, .55)], "calm"),
  ("Crews of two officers are on duty there around the clock.", [(MM_F20, 43.70, .55)], "slow"),
  ("This second launch, in February twenty twenty, was a developmental test. Also at night, also unarmed.", [(MM_F20, 47.40, .50), (MM_F20, 50.60, .50)], "calm", L_MM2),
  ("The Air Force says tests like these show the system is safe, secure, effective and ready.", [(MM_F20, 54.75, .50)], "calm"),
  ("Fifteen thousand miles an hour.", [(MM_S20D, 0.10, .52)], "punch", L_MM1),
  ("What should we break down next? Follow for more.", [(MM_S20, 48.50, .50)], "punch"),
 ]),
]
YSHORTS = []

DISPLAY = [("Mark fifteen", "Mk 15"), ("twenty-millimeter", "20mm"), ("four thousand five hundred", "4,500"), ("Four thousand five hundred", "4,500"),
           ("fifteen hundred and fifty", "1,550"), ("twenty seconds", "20 seconds"), ("Block One B", "Block 1B"), ("thirteen thousand six hundred", "13,600"),
           ("nineteen eighty", "1980"), ("twenty twenty-five", "2025"), ("nineteen sixty-eight", "1968"), ("nineteen seventy-five", "1975"),
           ("twenty fourteen", "2014"), ("forty-six", "46"), ("Forty-six", "46"), ("twenty twenty-two", "2022"), ("fifty nautical", "50 nautical"),
           ("fifteen thousand feet", "15,000 feet"), ("Type twelve", "Type 12"), ("five-inch", "5-inch"), ("A-10C Thunderbolt Two", "A-10C Thunderbolt II"),
           ("thirty-millimeter", "30mm"), ("GAU-8", "GAU-8/A"), ("three thousand nine hundred", "3,900"), ("twenty-three millimeters", "23mm"), ("sixteen thousand", "16,000"),
           ("four hundred twenty", "420"), ("nineteen seventy-six", "1976"), ("two hundred eighty-one", "281"), ("thirty millimeters", "30mm"),
           ("fifty years", "50 years"), ("fifty-one thousand", "51,000"), ("M142", "M142"), ("five thousand", "5,000"), ("five-ton", "5-ton"), ("C-130", "C-130"),
           ("second battalion, three hundredth field artillery", "2nd Battalion, 300th Field Artillery"), ("twenty twenty-four", "2024"),
           ("July twenty nineteen", "July 2019"), ("Minuteman Three", "Minuteman III"), ("fifteen thousand", "15,000"), ("Fifteen thousand", "15,000"),
           ("Mach twenty-three", "Mach 23"), ("six thousand", "6,000"), ("seven hundred", "700"), ("seventy-nine thousand", "79,000"),
           ("nineteen seventy-eight", "1978"), ("nineteen seventy", "1970"), ("four hundred", "400"), ("twenty twenty", "2020"), ("Twenty-six", "26"), ("thirty-eight", "38")]
