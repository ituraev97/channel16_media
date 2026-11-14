# CHANNEL 16 · MILITARY HARDWARE · m017 (TikTok only, Mon Nov 16, 2026). Five vertical videos t1–t5, 62–75 s each.
# Exercises, tests, training and demonstrations only. Facts: sources.md. shot: (clip_id, start, cx)
SN = 451610   # 2nd LAAD Bn Marines fire FIM-92C Stingers, Vaagan Range, Orland, Norway, Cold Response 16, Feb 24, 2016 (30p)
SW = 936202   # 2nd LAAD Marines fire a FIM-92A Stinger at a training UAV, Sweden, Sept 6, 2024 (60p)
AV = 944147   # 5-4 ADA Stinger live fire with Avenger and MANPADS, Putlos Training Area, Germany, Nov 13, 2024 (30p)
IN = 975005   # 11th Airborne Division fires the FIM-92 Stinger, Super Garuda Shield 25, Baturaja, Indonesia, Aug 26, 2025 (30p)
FB = 771440   # 389th FS F-15E Strike Eagles over Mountain Home AFB, Idaho, 2020 (24p, 4K source downscaled)
FL = 786139   # 48th FW F-15C/F-15E fire four AIM-120B at a drone target, Atlantic Ocean, March 3, 2021 (60p)
FK = 884724   # 391st FS F-15Es take off from Kadena AB, Japan, Exercise Southern Beach, May 16, 2023 (30p)
RA = 386816   # "Navy Railgun Goes East" (ONR, Jan 2015): railgun lab and firing test footage (30p)
RH = 403786   # Railgun fires the Hyper Velocity Projectile, NSWC Dahlgren, Sept 2014 (30p)
RT = 516509   # Railgun first shot at Dahlgren's new Terminal Range, Nov 17, 2016 (60p)
RS = "539084d"   # de-duplicated copy (mpdecimate+minterpolate) of 539084, first 60 s;
RS0 = 539084  # Railgun multi-shot salvos (rep-rate fires), NSWC Dahlgren, 2017 (30p)
MA = 914247   # 4th Sqn, 2nd Cavalry Regt M2 .50-cal live fire, Grafenwoehr, Germany, Feb 29, 2024 (60p)
MJ = 971988   # 2nd Distribution Support Bn Marines, M2 on JLTV, Camp Lejeune, N.C., July 27, 2025 (24p)
MK = 997976   # 12th Littoral Combat Team Marines, Mk-19 and M2 CALFEX, Rodriguez Live-Fire Complex, Korea, Feb 28, 2026 (60p)
NA = 890582   # Fox Btry, 2/11 Marines, first Marine unit to fire NMESIS, NAS Point Mugu, Calif., June 27-29, 2023 (24p)
NB = 890579   # B-roll of the same NMESIS firing, Point Mugu, June 2023 (30p)
NC = 885463   # NMESIS launcher mobility characterization testing, Feb 2021 - Feb 2022 (30p)

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

LB_SN = dict(label="NORWAY · EXERCISE COLD RESPONSE · FEB 2016")
LB_SW = dict(label="SWEDEN · STINGER LIVE FIRE · SEPT 2024")
LB_AV = dict(label="PUTLOS, GERMANY · AVENGER LIVE FIRE · NOV 2024")
LB_IN = dict(label="INDONESIA · SUPER GARUDA SHIELD · AUG 2025")
LB_FB = dict(label="MOUNTAIN HOME AFB, IDAHO · F-15E FLIGHT · 2020")
LB_FL = dict(label="OVER THE ATLANTIC · LIVE-FIRE TRAINING · MARCH 2021")
LB_FK = dict(label="KADENA AB, JAPAN · EXERCISE SOUTHERN BEACH · 2023")
LB_RA = dict(label="U.S. NAVY RAILGUN · TEST FOOTAGE (ONR)")
LB_RH = dict(label="DAHLGREN, VA. · PROJECTILE TEST · 2014")
LB_RT = dict(label="DAHLGREN, VA. · TERMINAL RANGE · NOV 2016")
LB_RS = dict(label="DAHLGREN, VA. · MULTI-SHOT SALVOS · 2017")
LB_MA = dict(label="GRAFENWOEHR, GERMANY · LIVE-FIRE RANGE · FEB 2024")
LB_MJ = dict(label="CAMP LEJEUNE, N.C. · VEHICLE GUN RANGE · JULY 2025")
LB_MK = dict(label="SOUTH KOREA · LIVE-FIRE EXERCISE · FEB 2026")
LB_NA = dict(label="POINT MUGU, CALIF. · NMESIS LIVE FIRE · JUNE 2023")
LB_NC = dict(label="NMESIS MOBILITY TESTING · 2021-2022")
LB_F15 = dict(label="U.S. AIR FORCE F-15 TRAINING FOOTAGE")
LB_M2 = dict(label="U.S. ARMY & MARINES · LIVE-FIRE TRAINING")

SHORTS = [
 dict(id="t1", hook="[5-MILE REACH]<br>FROM THE SHOULDER", title="The Stinger: a heat-seeking missile fired from the shoulder, with a 5-mile reach",
      lines=[
  ("This missile is fired from the shoulder. And it can reach an aircraft five miles away.", [(SN, 114.60, .62)], "tense", LB_SN),
  ("It's the F I M ninety-two Stinger.", [(SW, 129.80, .25)], "punch", LB_SW),
  ("A portable surface-to-air missile, with an infrared seeker that homes in on its target.", [(SW, 36.50, .50), (SW, 47.90, .50)], "calm", LB_SW),
  ("Maximum effective range: twenty-six thousand four hundred feet.", [(SN, 97.20, .50), (SN, 66.00, .50)], "drive", LB_SN),
  ("It engages targets from six hundred to twelve thousand five hundred feet up.", [(SN, 121.90, .50)], "calm", LB_SN),
  ("With its grip stock, the system weighs about thirty-five pounds. The missile is about five feet long.", [(SW, 67.00, .45), (SW, 26.50, .50)], "calm", LB_SW),
  ("It reached initial operational capability in February nineteen eighty-one.", [(SW, 21.60, .50)], "calm", LB_SW),
  ("Norway, twenty sixteen. Marines of the Second Low Altitude Air Defense Battalion fire Stingers during exercise Cold Response.", [(SN, 80.20, .50), (SN, 108.20, .45)], "calm", LB_SN),
  ("Their targets: remote-controlled aircraft, launched from a rail.", [(SN, 15.70, .50), (SN, 43.00, .50)], "calm", LB_SN),
  ("Germany, November twenty twenty-four: in a live-fire exercise, the Army fires them from the Avenger.", [(AV, 176.00, .42), (AV, 181.50, .30)], "drive", LB_AV),
  ("A Humvee with eight Stingers, in two missile pods.", [(AV, 83.30, .50), (AV, 95.10, .50)], "punch", LB_AV),
  ("Indonesia, August twenty twenty-five: soldiers of the Eleventh Airborne Division fire the Stinger there for the first time ever.", [(IN, 92.90, .40), (IN, 30.10, .50), (IN, 87.80, .40)], "calm", LB_IN),
  ("Since twenty nineteen, the Army has been adding proximity fuzes, so a Stinger can take out a drone without a direct hit.", [(IN, 60.10, .40), (IN, 10.10, .45)], "calm", LB_IN),
  ("Its maker, Raytheon, says twenty-five nations have adopted it.", [(SW, 95.20, .45), (SW, 110.40, .50)], "calm", LB_SW),
  ("Shoulder or Humvee: which launcher would you pick? Follow for more.", [(SW, 133.50, .35)], "punch", LB_SW),
 ]),
 dict(id="t2", hook="[MACH 2.5+]<br>TWO-SEAT STRIKE JET", title="The F-15E Strike Eagle: Mach 2.5+, a crew of two, and up to eight AMRAAM missiles",
      lines=[
  ("A live AMRAAM leaves an F-15. Mach two point five plus. A crew of two. This is the F-15E Strike Eagle.", [(FL, 28.50, .50), (FB, 92.50, .50), (FB, 27.20, .50)], "tense", LB_F15),
  ("The Air Force calls it a dual-role fighter, built for air-to-air and air-to-ground missions.", [(FB, 33.50, .50), (FB, 39.50, .50)], "calm", LB_FB),
  ("Two crew: a pilot, and a weapon systems officer.", [(FB, 6.00, .50), (FB, 69.00, .45)], "calm", LB_FB),
  ("Two Pratt and Whitney engines, each producing up to twenty-nine thousand pounds of thrust.", [(FB, 72.80, .45), (FB, 75.50, .45)], "drive", LB_FB),
  ("Top speed: eighteen hundred seventy-five miles an hour.", [(FB, 98.00, .50)], "punch", LB_FB),
  ("It's built to fight at low altitude, day or night, in any weather.", [(FB, 79.00, .50), (FB, 84.50, .50)], "calm", LB_FB),
  ("For air-to-air, it can carry up to eight A-I-M one-twenty AMRAAM missiles.", [(FB, 120.00, .50), (FB, 123.50, .50)], "calm", LB_FB),
  ("March twenty twenty-one, over the Atlantic: F-15s from the Forty-Eighth Fighter Wing, based at RAF Lakenheath in England, fire four live AMRAAMs in a training mission.", [(FL, 3.00, .50), (FL, 6.50, .50), (FL, 36.00, .45)], "calm", LB_FL),
  ("The target was a drone. The mission tested combat readiness, in a peacetime environment.", [(FL, 44.00, .50), (FL, 55.00, .50)], "calm", LB_FL),
  ("The first production F-15E was delivered in April nineteen eighty-eight.", [(FB, 140.20, .30)], "calm", LB_FB),
  ("It's about sixty-four feet long, with a wingspan of almost forty-three feet.", [(FB, 146.00, .50), (FB, 153.00, .50)], "calm", LB_FB),
  ("Maximum takeoff weight: eighty-one thousand pounds.", [(FK, 0.30, .50), (FK, 3.50, .45)], "punch", LB_FK),
  ("Kadena Air Base, Japan, May twenty twenty-three: Strike Eagles take off for exercise Southern Beach.", [(FK, 38.50, .45), (FK, 42.50, .55)], "calm", LB_FK),
  ("Ferry range, with extra fuel tanks: twenty-four hundred miles.", [(FB, 110.00, .50), (FB, 114.00, .50)], "calm", LB_FB),
  ("Strike Eagle or F-16: which would you rather fly? Follow for more.", [(FB, 14.00, .50), (FB, 160.00, .50)], "punch", LB_FB),
 ]),
 dict(id="t3", hook="[MACH 6+]<br>NO GUNPOWDER", title="The Navy's railgun: no gunpowder, Mach 6+ per ONR. Here's why it was paused",
      lines=[
  ("No gunpowder. No chemical propellant. This Navy gun fired with electricity.", [(RA, 12.85, .50), (RA, 9.30, .50)], "tense", LB_RA),
  ("The electromagnetic railgun. The Office of Naval Research said its projectiles could top Mach six.", [(RT, 74.75, .40), (RT, 77.50, .35), (RT, 82.90, .35)], "drive", LB_RT),
  ("A massive electrical pulse does the launching.", [(RA, 0.20, .50), (RA, 6.30, .55)], "calm", LB_RA),
  ("Planned range: more than one hundred nautical miles.", [(RS, 17.80, .50)], "punch", LB_RS),
  ("Twenty fourteen, Dahlgren, Virginia: a test of the hypervelocity projectile.", [(RH, 22.30, .50), (RH, 26.95, .50)], "calm", LB_RH),
  ("A guided, low-drag round, designed to work in different gun systems.", [(RH, 33.40, .50)], "calm", LB_RH),
  ("November twenty sixteen: the first shot at Dahlgren's new terminal range.", [(RT, 85.75, .55), (RT, 90.40, .50)], "calm", LB_RT),
  ("Engineers watch from the control room. High-speed cameras follow the shot.", [(RT, 59.86, .50), (RT, 92.60, .50)], "calm", LB_RT),
  ("Twenty seventeen: the first multi-shot salvos.", [(RS0, 72.50, .22), (RS, 22.80, .50)], "drive", LB_RS),
  ("The goal: thirty-two megajoules. One megajoule, the Navy says, is about a one-ton vehicle moving at one hundred sixty miles an hour.", [(RS, 27.80, .50), (RS, 49.20, .50)], "calm", LB_RS),
  ("In twenty eighteen, the Navy's top admiral told Congress it hadn't reached its promised range. The barrel was the likely limit.", [(RT, 44.80, .50), (RA, 17.80, .50)], "calm", LB_RA),
  ("In twenty twenty-one, the Navy said it would pause the program, citing tight budgets and integration challenges.", [(RS, 32.75, .50), (RT, 65.50, .50), (RS, 37.70, .50)], "calm", LB_RA),
  ("Military.com called it a five-hundred-million-dollar experiment.", [(RH, 29.80, .50), (RS, 25.00, .50)], "calm", LB_RA),
  ("Railgun or missiles: which would you bet on? Follow for more.", [(RT, 95.00, .55), (RT, 48.50, .50)], "punch", LB_RT),
 ]),
 dict(id="t4", hook="[SINCE 1933]<br>STILL FIRING", title="The M2 .50-cal machine gun was adopted in 1933. It's still firing in live-fire training",
      lines=[
  ("This machine gun was adopted in nineteen thirty-three. Soldiers still fire it today.", [(MA, 30.00, .55), (MA, 17.20, .60)], "tense", LB_MA),
  ("The M2, a fifty-caliber machine gun. Nickname: Ma Deuce.", [(MA, 40.00, .45)], "punch", LB_MA),
  ("John Browning developed it at the end of World War One.", [(MA, 1.00, .45), (MA, 49.00, .50)], "calm", LB_MA),
  ("Cyclic rate of fire: four hundred fifty to five hundred fifty rounds a minute.", [(MA, 53.50, .45), (MA, 70.50, .45)], "drive", LB_MA),
  ("Maximum effective range: eighteen hundred thirty meters. That's about two thousand yards.", [(MA, 61.60, .50), (MA, 78.60, .50)], "calm", LB_MA),
  ("Gun and tripod together: one hundred twenty-eight pounds.", [(MA, 94.30, .45)], "punch", LB_MA),
  ("Nearly two million were produced during World War Two.", [(MA, 150.80, .50)], "calm", LB_MA),
  ("Grafenvur, Germany, February twenty twenty-four: Second Cavalry Regiment soldiers on a live-fire range.", [(MA, 105.50, .55), (MA, 99.50, .45)], "calm", LB_MA),
  ("It mounts on most military vehicles and aircraft, or fires from a tripod.", [(MJ, 104.00, .50), (MA, 133.40, .50)], "calm", LB_M2),
  ("Camp Lejeune, North Carolina, July twenty twenty-five: Marines fire it from a Joint Light Tactical Vehicle.", [(MJ, 159.60, .50), (MJ, 210.70, .45), (MJ, 236.10, .50)], "calm", LB_MJ),
  ("The newer M2A1 adds a quick-change barrel, and a new flash hider.", [(MJ, 146.60, .50), (MA, 139.20, .45)], "calm", LB_M2),
  ("In twenty twelve, the Army put its M2 inventory at more than fifty-four thousand guns.", [(MA, 155.00, .50), (MA, 22.00, .60)], "calm", LB_MA),
  ("South Korea, February twenty twenty-six: Marines fire M2s in a combined-arms live-fire exercise.", [(MK, 175.30, .50), (MK, 184.80, .50)], "calm", LB_MK),
  ("A Marine Corps handout calls it the mainstay of its heavy machine gun platoons.", [(MK, 193.60, .50), (MK, 200.50, .50)], "calm", LB_MK),
  ("More than ninety years on the job. What other old-timer is still serving? Follow for more.", [(MA, 124.50, .45)], "punch", LB_MA),
 ]),
 dict(id="t5", hook="[0 CREW ON BOARD]<br>MISSILE LAUNCHER", title="This Marine missile launcher has no one inside: NMESIS fires the Naval Strike Missile",
      lines=[
  ("A missile launcher with no one inside. This is Nemesis.", [(NA, 23.40, .30), (NA, 29.05, .50)], "tense", LB_NA),
  ("The Navy-Marine Expeditionary Ship Interdiction System: an unmanned launcher, built on a Joint Light Tactical Vehicle.", [(NA, 6.55, .50), (NB, 154.10, .50)], "calm", LB_NA),
  ("It fires the Naval Strike Missile. Range: about one hundred nautical miles.", [(NB, 194.00, .70)], "drive", LB_NA),
  ("It's an anti-ship missile, with a passive, dual-band infrared seeker.", [(NA, 42.50, .50), (NB, 24.20, .50)], "calm", LB_NA),
  ("The vehicle is Oshkosh's ROGUE Fires: Remotely Operated Ground Unit for Expeditionary Fires.", [(NB, 186.60, .50)], "calm", LB_NA),
  ("The Marines say it lets a small crew operate in forward areas, with minimal detectability.", [(NC, 80.00, .60), (NC, 190.00, .50)], "calm", LB_NC),
  ("Point Mugu, June twenty twenty-three: a live-fire test by Fox Battery, Second Battalion, Eleventh Marines.", [(NA, 62.50, .50), (NA, 45.56, .50)], "calm", LB_NA),
  ("They became the first Marine unit to operate and fire it.", [(NA, 69.90, .50), (NB, 102.50, .50)], "punch", LB_NA),
  ("Before the shot, Marines load the launch pods.", [(NB, 0.30, .50), (NB, 20.00, .50)], "calm", LB_NA),
  ("It had been test-fired twice before: in November twenty twenty, and in August twenty twenty-one.", [(NC, 100.00, .50), (NC, 228.00, .35)], "calm", LB_NC),
  ("As of twenty twenty-three, each Nemesis battery was planned to have eighteen launchers.", [(NB, 134.40, .50)], "calm", LB_NA),
  ("The Marine Corps planned fourteen batteries, with all of them fielded by twenty thirty.", [(NB, 144.10, .50), (NB, 10.90, .50)], "calm", LB_NA),
  ("Raytheon builds the Naval Strike Missile in the U.S. Its original maker is Norway's Kongsberg.", [(NC, 205.00, .50), (NC, 264.00, .30)], "calm", LB_NC),
  ("Back at Point Mugu, the launch smoke drifts over the range.", [(NB, 198.70, .70), (NA, 27.05, .50)], "slow", LB_NA),
  ("Unmanned launchers: the future, or a risky idea? Follow for more.", [(NC, 245.00, .35), (NC, 268.50, .45)], "punch", LB_NC),
 ]),
]
YSHORTS = []

DISPLAY = [("F I M ninety-two", "FIM-92"), ("twenty-six thousand four hundred feet", "26,400 feet"), ("six hundred to twelve thousand five hundred", "600 to 12,500"),
           ("thirty-five pounds", "35 pounds"), ("twenty-five nations", "25 nations"), ("five feet", "5 feet"), ("nineteen eighty-one", "1981"), ("twenty sixteen", "2016"),
           ("Second Low Altitude Air Defense Battalion", "2nd Low Altitude Air Defense Battalion"), ("twenty twenty-four", "2024"), ("eight Stingers", "8 Stingers"),
           ("twenty twenty-five", "2025"), ("Eleventh Airborne Division", "11th Airborne Division"), ("twenty nineteen", "2019"), ("five miles", "5 miles"),
           ("Mach two point five plus", "Mach 2.5+"), ("twenty-nine thousand pounds", "29,000 pounds"), ("eighteen hundred seventy-five", "1,875"),
           ("eight A-I-M one-twenty", "8 AIM-120"), ("twenty twenty-one", "2021"), ("Forty-Eighth Fighter Wing", "48th Fighter Wing"), ("four live", "4 live"),
           ("nineteen eighty-eight", "1988"), ("sixty-four feet", "64 feet"), ("forty-three feet", "43 feet"), ("eighty-one thousand pounds", "81,000 pounds"),
           ("twenty twenty-three", "2023"), ("twenty-four hundred miles", "2,400 miles"),
           ("Mach six", "Mach 6"), ("one hundred nautical", "100 nautical"), ("two thousand five", "2005"), ("Twenty fourteen", "2014"), ("twenty sixteen", "2016"),
           ("Twenty seventeen", "2017"), ("thirty-two megajoules", "32 megajoules"), ("one-ton", "1-ton"), ("one hundred sixty miles", "160 miles"),
           ("twenty eighteen", "2018"), ("five-hundred-million-dollar", "$500 million"),
           ("nineteen thirty-three", "1933"), ("M2, a fifty-caliber", "M2, a .50-caliber"), ("two thousand yards", "2,000 yards"), ("Grafenvur", "Grafenwoehr"), ("twenty twelve", "2012"), ("One megajoule", "1 megajoule"), ("Nemesis", "NMESIS"), ("four hundred fifty to five hundred fifty", "450 to 550"),
           ("eighteen hundred thirty meters", "1,830 meters"), ("one hundred twenty-eight pounds", "128 pounds"), ("two million", "2 million"),
           ("Second Cavalry Regiment", "2nd Cavalry Regiment"), ("ninety-five percent", "95 percent"), ("fifty-four thousand", "54,000"),
           ("twenty twenty-six", "2026"), ("ninety years", "90 years"),
           ("Second Battalion, Eleventh Marines", "2nd Battalion, 11th Marines"), ("twenty twenty", "2020"), ("eighteen launchers", "18 launchers"),
           ("fourteen batteries", "14 batteries"), ("twenty thirty", "2030")]
