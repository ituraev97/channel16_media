# Shorts for THE CALL 005 — each is one rescue with its own narration; facts as listed in sources.md.
# shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop inside the active picture (0..1)
SHORTS = [
 dict(id="s1", hook="~300 MILES<br>[OFFSHORE]", title="Sinking 300 miles off Cape Hatteras: the rescue that refueled on an aircraft carrier",
      lines=[
  ("Two hundred sixty nautical miles off Cape Hatteras. A sailing catamaran is filling with water, and the five people aboard are in a life raft.", [("986112s", 0.625, .08), ("986112s", 9.625, .35)], "tense"),
  ("That far out pushes the limits of a Coast Guard Jayhawk's range.", [("986112s", 20.625, .45)], "tense"),
  ("A Hercules finds the raft first, and confirms all five are stable.", [("986112s", 12.625, .45)], "calm"),
  ("On the way out, the Jayhawk refuels on an aircraft carrier, the USS George H.W. Bush. Then it reaches the raft.", [("986112t", 3.215, .1), ("986112t", 10.215, 0.0)], "drive"),
  ("The swimmer goes into the water. Then the hoist.", [("986112s", 19.125, .45), ("986112s", 51.625, .55)], "tense"),
  ("All five come up in good health. The helicopter refuels on the carrier again, then flies them home.", [(986004, 1.0, .45), (986004, 12.0, .45)], "drive"),
  ("The boat was lost. Everyone aboard made it home.", [("986112t", 14.2, 0.0), (986112, 183.0, .5)], "slow"),
 ]),
 dict(id="s2", hook="A DOG, A CAT<br>[UP TO 18-FT SEAS]", title="Coast Guard hoists two people, a dog and a cat off Cape Hatteras",
      lines=[
  ("Sixty-five miles off Cape Hatteras. A catamaran with a torn sail, and a small hole in the boat. Seas up to eighteen feet.", [(992015, 7.0, .5), (992015, 14.0, .5)], "tense"),
  ("Aboard: two people, a dog, and a cat. They set off their EPIRB.", [(992015, 22.0, .5)], "drive"),
  ("Within minutes, the Coast Guard has their position. A Jayhawk from Elizabeth City gets there in about an hour.", [(992015, 49.0, .5), (992015, 56.0, .5)], "drive"),
  ("The first survivor goes up with the cat, in a dry bag.", [(992015, 30.0, .5), (992015, 36.5, .5)], "calm"),
  ("The second goes up with the dog, in its own flotation vest.", [(992015, 62.0, .5), (992015, 76.0, .5)], "calm"),
  ("The rescue swimmer said it was his first dog, and his first cat.", [("992015v", 151.0, .5), ("992015v", 157.0, .5)], "slow"),
  ("And the cat? One commenter online wrote: that kitty is so unbothered.", [(992017, 16.0, .5), ("992015v", 196.0, .5)], "calm"),
 ]),
 dict(id="s3", hook="BEACON<br>[ON]", title="Boat capsizes off Oahu: two men on the hull, a beacon, and a Coast Guard hoist",
      lines=[
  ("One fifty-eight in the afternoon. A personal locator beacon goes off, along the west side of Oahu.", [(1013516, 1.0, .5), (1013516, 4.0, .5)], "tense"),
  ("A twelve-foot fishing boat has capsized off Keaau Beach Park. Two men are sitting on the overturned boat.", [(1013516, 24.0, .5), (1013516, 28.0, .5)], "drive"),
  ("Both are wearing life jackets.", [(1013516, 6.0, .5)], "punch"),
  ("At three twenty-seven, a Coast Guard Dolphin from Barbers Point finds them.", [(1013516, 8.5, .5)], "drive"),
  ("The basket comes down. One at a time, both men are hoisted up, and flown ashore.", [(1013516, 12.0, .5), (1013516, 17.0, .5), (1013516, 31.0, .5)], "calm"),
  ("A life jacket, and a beacon on your person. The Coast Guard says the beacon instantly alerts them to your position.", [(1013516, 34.3, .5), (1013516, 38.8, .5)], "slow"),
 ]),
 dict(id="s4", hook="STUCK ON<br>[THE CLIFF]", title="Hiker injured on a cliff at God's Thumb, Oregon: Coast Guard hoist",
      lines=[
  ("God's Thumb, on the Oregon coast. A hiker falls, and is left on a cliff with multiple injuries.", [(1008137, 1.0, .5), (1008137, 5.0, .5)], "tense"),
  ("Lincoln County dispatch calls the Coast Guard for help.", [(1008137, 13.0, .5)], "drive"),
  ("A Dolphin crew from Air Facility Newport comes in over the cliff, and the hoist cable goes down.", [(1008137, 14.5, .5), (1008137, 20.0, .5)], "drive"),
  ("The crew hoists her safely off the cliff.", [(1008137, 25.2, .5), (1008137, 27.0, .5)], "tense"),
  ("Then they fly her to Samaritan North Lincoln Hospital.", [(1008137, 36.0, .5)], "calm"),
  ("A powerful reminder, a Coast Guard aviation survival technician said, of how quickly a day outdoors can turn dangerous.", [(1008137, 30.6, .5), (1008137, 39.3, .5)], "slow"),
 ]),
 dict(id="s5", hook="THE RESCUERS<br>[CAPSIZED TOO]", title="Federal agents capsize trying to save two boaters off Puerto Rico: all five rescued",
      lines=[
  ("Night, off Isla de Cabras, Puerto Rico. A boat has capsized. By the time this Coast Guard helicopter arrives, a rescue boat has capsized too.", [(1001660, 1.0, .5), (1001660, 5.0, .5)], "tense"),
  ("Customs and Border Protection agents had gone to help two boaters, in ten-foot swells, and their boat capsized as well.", [(1001660, 10.5, .5), (1001660, 15.0, .5)], "drive"),
  ("Now five people are in the water. A Coast Guard boat can't get to them, beyond the reef line.", [(1001660, 33.0, .5), (1001660, 38.0, .5)], "tense"),
  ("A Puerto Rico Police helicopter pulls out two of them.", [(1001660, 43.0, .5)], "drive"),
  ("Then a Coast Guard Jayhawk puts its swimmer in the water, and hoists the last three.", [(1001660, 48.0, .5), (1001660, 63.5, .5)], "drive"),
  ("All five made it out, treated for minor injuries.", [(1001660, 66.5, .5)], "slow"),
 ]),
]
DISPLAY = [("Two hundred sixty nautical miles", "260 nautical miles"), ("Sixty-five miles", "65 miles"), ("eighteen feet", "18 feet"),
           ("One fifty-eight", "1:58"), ("twelve-foot", "12-foot"), ("three twenty-seven", "3:27"), ("ten-foot", "10-foot")]
CTA = "FOLLOW FOR MORE REAL RESCUES"
