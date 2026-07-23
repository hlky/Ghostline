# Cyberpunk 2077 Gigs

Source index: [IGN — Gigs](https://www.ign.com/wikis/cyberpunk-2077/Gigs)

This is a structural reference derived from IGN's walkthrough index and
the local [`quest.json`](../../../quest.json) journal export. It summarizes
vanilla quest objectives and links to IGN; it does not reproduce IGN's
walkthrough prose.

Matched quests: **85**

## Quick index

| Quest | Vanilla type | Quest path | Building blocks |
|---|---|---|---|
| [Cyberpsycho Sighting: Bloody Ritual](#cyberpsycho-sighting-bloody-ritual) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Bloody_Ritual)) | CyberPsycho | `quests/minor_quest/ma_wat_nid_15` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Demons of War](#cyberpsycho-sighting-demons-of-war) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Demons_of_War)) | CyberPsycho | `quests/minor_quest/ma_wat_kab_02` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Discount Doc](#cyberpsycho-sighting-discount-doc) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Discount_Doc)) | CyberPsycho | `quests/minor_quest/ma_std_rcr_11` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: House on a Hill](#cyberpsycho-sighting-house-on-a-hill) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_House_on_a_Hill)) | CyberPsycho | `quests/minor_quest/ma_bls_ina_se1_08` | phone/message contact, search/investigate, interact/use device, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Letter of the Law](#cyberpsycho-sighting-letter-of-the-law) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Letter_Of_The_Law)) | CyberPsycho | `quests/minor_quest/ma_hey_spr_06` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Lex Talionis](#cyberpsycho-sighting-lex-talionis) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Lex_Talionis)) | CyberPsycho | `quests/minor_quest/ma_pac_cvi_15` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Lt. Mower](#cyberpsycho-sighting-lt-mower) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Lt._Mower)) | CyberPsycho | `quests/minor_quest/ma_wat_kab_08` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: On Deaf Ears](#cyberpsycho-sighting-on-deaf-ears) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_On_Deaf_Ears)) | CyberPsycho | `quests/minor_quest/ma_cct_dtn_03` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Phantom of Night City](#cyberpsycho-sighting-phantom-of-night-city) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Phantom_of_Night_City)) | CyberPsycho | `quests/minor_quest/ma_cct_dtn_07` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Seaside Cafe](#cyberpsycho-sighting-seaside-cafe) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Seaside_Cafe)) | CyberPsycho | `quests/minor_quest/ma_hey_spr_04` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Second Chances](#cyberpsycho-sighting-second-chances) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Second_Chances)) | CyberPsycho | `quests/minor_quest/ma_bls_ina_se1_22` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Six Feet Under](#cyberpsycho-sighting-six-feet-under) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Six_Feet_Under)) | CyberPsycho | `quests/minor_quest/ma_wat_nid_22` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Smoke on the Water](#cyberpsycho-sighting-smoke-on-the-water) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Smoke_on_the_Water)) | CyberPsycho | `quests/minor_quest/ma_pac_cvi_08` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: The Wasteland](#cyberpsycho-sighting-the-wasteland) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_The_Wasteland)) | CyberPsycho | `quests/minor_quest/ma_bls_ina_se1_07` | phone/message contact, follow/escort, search/investigate, interact/use device, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Ticket to the Major Leagues](#cyberpsycho-sighting-ticket-to-the-major-leagues) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Ticket_to_the_Major_Leagues)) | CyberPsycho | `quests/minor_quest/ma_wat_lch_06` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Under the Bridge](#cyberpsycho-sighting-under-the-bridge) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Under_The_Bridge)) | CyberPsycho | `quests/minor_quest/ma_std_arr_06` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Cyberpsycho Sighting: Where the Bodies Hit the Floor](#cyberpsycho-sighting-where-the-bodies-hit-the-floor) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Where_the_Bodies_Hit_the_Floor)) | CyberPsycho | `quests/minor_quest/ma_wat_nid_03` | phone/message contact, search/investigate, retrieve/collect item, combat/neutralize |
| [Gig: A Lack of Empathy](#gig-a-lack-of-empathy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/A_Lack_of_Empathy)) | StreetStory | `quests/street_stories/city_center/downtown/sts_cct_dtn_03` | travel/reach location, wait/time gate, search/investigate, hack/breach/download, retrieve/collect item, deliver/deposit item, stealth/avoid detection, leave/escape area |
| [Gig: A Shrine Defiled](#gig-a-shrine-defiled) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/A_Shrine_Defiled)) | StreetStory | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | travel/reach location, retrieve/collect item, deliver/deposit item, stealth/avoid detection, leave/escape area |
| [Gig: An Inconvenient Killer](#gig-an-inconvenient-killer) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/An_Inconvenient_Killer)) | StreetStory | `quests/street_stories/city_center/downtown/sts_cct_dtn_02` | meet/contact conversation, travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence, leave/escape area |
| [Gig: Backs Against the Wall](#gig-backs-against-the-wall) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Backs_Against_the_Wall)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item |
| [Gig: Big Pete's Got Big Problems](#gig-big-petes-got-big-problems) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Big_Pete%27s_Got_Big_Problems)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | search/investigate, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Bloodsport](#gig-bloodsport) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Bloodsport)) | StreetStory | `quests/street_stories/watson/little_china/sts_wat_lch_03` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, retrieve/collect item, leave/escape area |
| [Gig: Breaking News](#gig-breaking-news) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Breaking_News)) | StreetStory | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05` | meet/contact conversation, travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, stealth/avoid detection, leave/escape area |
| [Gig: Bring Me the Head of Gustavo Orta](#gig-bring-me-the-head-of-gustavo-orta) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Bring_Me_the_Head_of_Gustavo_Orta)) | StreetStory | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Catch a Tyger's Toe](#gig-catch-a-tygers-toe) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Catch_a_Tyger%27s_Toe)) | StreetStory | `quests/street_stories/watson/little_china/sts_wat_lch_01` | travel/reach location, hack/breach/download, deliver/deposit item, leave/escape area |
| [Gig: Cuckoo's Nest](#gig-cuckoos-nest) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Cuckoo%27s_Nest)) | StreetStory | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device, retrieve/collect item, vehicle sequence |
| [Gig: Dancing on a Minefield](#gig-dancing-on-a-minefield) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Dancing_on_a_Mine_Field)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07` | search/investigate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Dirty Biz](#gig-dirty-biz) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Dirty_Biz)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: Error 404](#gig-error-404) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Error_404)) | StreetStory | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04` | travel/reach location, search/investigate, deliver/deposit item, leave/escape area |
| [Gig: Eye for an Eye](#gig-eye-for-an-eye) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Eye_For_An_Eye)) | StreetStory | `quests/street_stories/heywood/glen/sts_hey_gle_01` | meet/contact conversation, search/investigate, retrieve/collect item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Family Heirloom](#gig-family-heirloom) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Family_Heirloom)) | StreetStory | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Family Matters](#gig-family-matters) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Family_Matters)) | StreetStory | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` | travel/reach location, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item |
| [Gig: Fifth Column](#gig-fifth-column) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Fifth_Column)) | StreetStory | `quests/street_stories/heywood/glen/sts_hey_gle_04` | travel/reach location, search/investigate, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Fixer, Merc, Soldier, Spy](#gig-fixer-merc-soldier-spy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Fixer,_Merc,_Soldier,_Spy)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_04` | phone/message contact, travel/reach location, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Flight of the Cheetah](#gig-flight-of-the-cheetah) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Flight_of_the_Cheetah)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device |
| [Gig: Flying Drugs](#gig-flying-drugs) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Flying_Drugs)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03` | meet/contact conversation, travel/reach location, search/investigate, hack/breach/download, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: For My Son](#gig-for-my-son) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/For_My_Son)) | StreetStory | `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05` | search/investigate, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Freedom of the Press](#gig-freedom-of-the-press) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Freedom_of_the_Press)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: Getting Warmer...](#gig-getting-warmer) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Getting_Warmer)) | StreetStory | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09` | travel/reach location, search/investigate, interact/use device, retrieve/collect item |
| [Gig: Going Up or Down?](#gig-going-up-or-down) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Going_Up_or_Going_Down)) | StreetStory | `quests/street_stories/heywood/glen/sts_hey_gle_05` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize |
| [Gig: Going-away Party](#gig-going-away-party) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Going-Away_Party)) | StreetStory | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, vehicle sequence |
| [Gig: Goodbye, Night City](#gig-goodbye-night-city) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Goodbye,_Night_City)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, retrieve/collect item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Greed Never Pays](#gig-greed-never-pays) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Greed_Never_Pays)) | StreetStory | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: Guinea Pigs](#gig-guinea-pigs) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Guinea_Pigs)) | StreetStory | `quests/street_stories/city_center/downtown/sts_cct_dtn_04` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Hacking the Hacker](#gig-hacking-the-hacker) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Hacking_the_Hacker)) | StreetStory | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | travel/reach location, search/investigate, hack/breach/download, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Hippocratic Oath](#gig-hippocratic-oath) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Hippocratic_Oath)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_02` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, retrieve/collect item |
| [Gig: Hot Merchandise](#gig-hot-merchandise) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Hot_Merchandise)) | StreetStory | `quests/street_stories/heywood/wellsprings/sts_hey_spr_06` | travel/reach location, search/investigate, deliver/deposit item, combat/neutralize, stealth/avoid detection, leave/escape area |
| [Gig: Jeopardy](#gig-jeopardy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Jeopardy)) | StreetStory | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` | wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Last Login](#gig-last-login) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Last_Login)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_05` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: Life's Work](#gig-lifes-work) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Life%27s_Work)) | StreetStory | `quests/street_stories/heywood/glen/sts_hey_gle_06` | meet/contact conversation, travel/reach location, hack/breach/download, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Lousy Kleppers](#gig-lousy-kleppers) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Lousy_Kleppers)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` | wait/time gate, search/investigate, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Many Ways to Skin a Cat](#gig-many-ways-to-skin-a-cat) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Many_Ways_to_Skin_a_Cat)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02` | travel/reach location, search/investigate, retrieve/collect item, combat/neutralize, vehicle sequence |
| [Gig: MIA](#gig-mia) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/MIA)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, retrieve/collect item |
| [Gig: Monster Hunt](#gig-monster-hunt) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Monster_Hunt)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_07` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: No Fixers](#gig-no-fixers) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/No_Fixers)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06` | meet/contact conversation, travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Occupational Hazard](#gig-occupational-hazard) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Occupational_Hazard)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01` | meet/contact conversation, travel/reach location, search/investigate, hack/breach/download, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Old Friends](#gig-old-friends) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Old_Friends)) | StreetStory | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08` | travel/reach location, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Olive Branch](#gig-olive-branch) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Olive_Branch)) | StreetStory | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01` | meet/contact conversation, interact/use device, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: On a Tight Leash](#gig-on-a-tight-leash) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/On_A_Tight_Leash)) | StreetStory | `quests/street_stories/heywood/wellsprings/sts_hey_spr_01` | phone/message contact, meet/contact conversation, travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Playing for Keeps](#gig-playing-for-keeps) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Playing_For_Keeps)) | StreetStory | `quests/street_stories/watson/little_china/sts_wat_lch_05` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item |
| [Gig: Race to the Top](#gig-race-to-the-top) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Race_To_The_Top)) | StreetStory | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03` | travel/reach location, search/investigate, deliver/deposit item, vehicle sequence, leave/escape area |
| [Gig: Radar Love](#gig-radar-love) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Radar_Love)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04` | search/investigate, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Rite of Passage](#gig-rite-of-passage) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Rite_of_Passage)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05` | travel/reach location, leave/escape area |
| [Gig: Scrolls before Swine](#gig-scrolls-before-swine) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Scrolls_Before_Swine)) | StreetStory | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07` | search/investigate, retrieve/collect item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Serial Suicide](#gig-serial-suicide) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Serial_Suicide)) | StreetStory | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | travel/reach location, deliver/deposit item, stealth/avoid detection, leave/escape area |
| [Gig: Serious Side Effects](#gig-serious-side-effects) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Serious_Side_Effects)) | StreetStory | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: Severance Package](#gig-severance-package) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Severance_Package)) | StreetStory | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Shark in the Water](#gig-shark-in-the-water) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Shark_in_the_Water)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_06` | travel/reach location, search/investigate, combat/neutralize, leave/escape area |
| [Gig: Small Man, Big Evil](#gig-small-man-big-evil) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Small_Man,_Big_Evil)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_101` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Sparring Partner](#gig-sparring-partner) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sparring_Partner)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, vehicle sequence |
| [Gig: Sr. Ladrillo's Private Collection](#gig-sr-ladrillos-private-collection) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sr_Ladrillo%27s_Private_Collection)) | StreetStory | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` | travel/reach location, wait/time gate, deliver/deposit item, leave/escape area |
| [Gig: The Frolics of Councilwoman Cole](#gig-the-frolics-of-councilwoman-cole) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Frolics_of_Councilwoman_Cole)) | StreetStory | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | travel/reach location, hack/breach/download, retrieve/collect item, stealth/avoid detection, vehicle sequence, leave/escape area |
| [Gig: The Heisenberg Principle](#gig-the-heisenberg-principle) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Heisenberg_Principle)) | StreetStory | `quests/street_stories/watson/little_china/sts_wat_lch_06` | travel/reach location, search/investigate, deliver/deposit item, leave/escape area |
| [Gig: The Lord Giveth and Taketh Away](#gig-the-lord-giveth-and-taketh-away) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Lord_Giveth_and_Taketh_Away)) | StreetStory | `quests/street_stories/heywood/wellsprings/sts_hey_spr_03` | meet/contact conversation, travel/reach location, search/investigate, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: The Union Strikes Back](#gig-the-union-strikes-back) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Union_Strikes_Back)) | StreetStory | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Gig: Trevor's Last Ride](#gig-trevors-last-ride) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Trevor%27s_Last_Ride)) | StreetStory | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item |
| [Gig: Troublesome Neighbors](#gig-troublesome-neighbors) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Troublesome_Neighbors)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_107` | retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Gig: Two Wrongs Makes Us Right](#gig-two-wrongs-makes-us-right) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Two_Wrongs_Makes_Us_Right)) | StreetStory | `quests/street_stories/pacifica/coastview/sts_pac_cvi_02` | travel/reach location, search/investigate, combat/neutralize, leave/escape area |
| [Gig: Tyger and Vulture](#gig-tyger-and-vulture) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Tyger_and_Vulture)) | StreetStory | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` | travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item |
| [Gig: Until Death Do Us Part](#gig-until-death-do-us-part) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Until_Death_Do_Us_Part)) | StreetStory | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` | travel/reach location, wait/time gate, search/investigate, deliver/deposit item, stealth/avoid detection, leave/escape area |
| [Gig: Wakako's Favorite](#gig-wakakos-favorite) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Wakako%27s_Favorite)) | StreetStory | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05` | meet/contact conversation, follow/escort, search/investigate, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Gig: We Have Your Wife](#gig-we-have-your-wife) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/We_Have_Your_Wife)) | StreetStory | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, vehicle sequence |
| [Gig: Welcome to America, Comrade](#gig-welcome-to-america-comrade) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Welcome_to_America,_Comrade)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_102` | travel/reach location, search/investigate, retrieve/collect item, deliver/deposit item, stealth/avoid detection, vehicle sequence, leave/escape area |
| [Gig: Woman of La Mancha](#gig-woman-of-la-mancha) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Woman_of_La_Mancha)) | StreetStory | `quests/street_stories/watson/kabuki/sts_wat_kab_08` | search/investigate, hack/breach/download, deliver/deposit item, combat/neutralize, leave/escape area |

## Cyberpsycho Sighting: Bloody Ritual

- IGN walkthrough: [Cyberpsycho Sighting: Bloody Ritual](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Bloody_Ritual)
- Vanilla type: `CyberPsycho`
- Quest hash: `2290065945`
- Quest path: `quests/minor_quest/ma_wat_nid_15`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Not everyone's made for Maelstrom. Some – surprise, surprise – don't take to well to having half their face chopped off. They start hearing voices, seeing and imagining things. Then, it's enough to get their hands on a gun, and... that recipe for disaster's ready to serve.

### Objective sequence

1. **Read the shard found on Zaria.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/check_shard_psycho`
2. **Locate where the ritual took place.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/find_ritual`
   - Map pin: ref `#ma_wat_nid_15_tr_area`; position `-1534.6896972656, 2511.7248535156, 7.1199998855591`
3. **Read the shard found on the dead Maelstromer.**  
   `Optional` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/check_shard`
4. **Crack the ritualist's shard.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/hack_shard_mls`
5. **Search the area for survivors.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/look_survivors`
6. **Search the body.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/loot_delivery`
7. **Search the body.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/loot_psycho`
8. **Search the body.**  
   `Optional` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/loot_corpse`
9. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/check_message`
10. **Find cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/find`
   - Map pin: ref `#ma_wat_nid_15_tr_area`; position `-1534.6896972656, 2511.7248535156, 7.1199998855591`
11. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/kill_psycho`
   - Map pin: ref `#ma_wat_nid_15_tr_area`; position `-1534.6896972656, 2511.7248535156, 7.1199998855591`
12. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/search_clues`
   - Map pin: ref `#ma_wat_nid_15_tr_area`; position `-1534.6896972656, 2511.7248535156, 7.1199998855591`
13. **Message Regina about Cyberpsycho Sighting: Bloody Ritual**  
   `Primary` · `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/send_info`

## Cyberpsycho Sighting: Demons of War

- IGN walkthrough: [Cyberpsycho Sighting: Demons of War](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Demons_of_War)
- Vanilla type: `CyberPsycho`
- Quest hash: `1198579324`
- Quest path: `quests/minor_quest/ma_wat_kab_02`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Usually, when a corpo gets his walking papers, he loses all his implants too. They dig those synth organs and cyber eyes right out of his body. But sometimes, the chrome's so far ingrown, it can't be removed safely. Even if someone really, really wants it...

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/check_message`
2. **Read the shard by the cyberpsycho's body.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/check_shard`
3. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/find_psycho`
   - Map pin: ref `#ma_wat_kab_02_tr`; position `-787.1591796875, 1879.7570800781, 47.759994506836`
4. **Investigate the area by the bridge.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/kill_psycho`
   - Map pin: ref `#ma_wat_kab_02_tr`; position `-787.1591796875, 1879.7570800781, 47.759994506836`
6. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues`
   - Map pin: ref `#ma_wat_kab_02_tr_search_area`; position `-790.5, 1890.734375, 50.98291015625`
7. **Send the information to Regina.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info`

## Cyberpsycho Sighting: Discount Doc

- IGN walkthrough: [Cyberpsycho Sighting: Discount Doc](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Discount_Doc)
- Vanilla type: `CyberPsycho`
- Quest hash: `106860731`
- Quest path: `quests/minor_quest/ma_std_rcr_11`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Working on a construction site has its perks: breeze on your face, sun on your shoulders, no creepy corpo smell and tangible results you can show off to the world. It's good, honest work. 'Course Night City's always got a way of fucking things up.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/check_message`
2. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/find_psycho`
3. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/kill_psycho`
4. **Search the attacker.**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/loot_psycho`
5. **Read the shard "Doesn't look good"**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/read_shard_chase`
6. **Read the shard "Send a crew"**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/read_shard_merc`
7. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/search_clues`
8. **Message Regina about Cyberpsycho Sighting: Discount Doc**  
   `Primary` · `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/send_info`

## Cyberpsycho Sighting: House on a Hill

- IGN walkthrough: [Cyberpsycho Sighting: House on a Hill](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_House_on_a_Hill)
- Vanilla type: `CyberPsycho`
- Quest hash: `3723374653`
- Quest path: `quests/minor_quest/ma_bls_ina_se1_08`
- District: Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Shots were heard on the outskirts of NC – rare given the seemingly peaceful area. We oughta go and take a closer look. Why wait for the clean-up crew when there could still be lives that need saving?

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_message`
2. **Read the shard located on the cyberpsycho's body.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_shard`
3. **Read the shard located on the dead woman.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_woman_shard`
4. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues`
   - Map pin: ref `#ma_bls_ina_se1_08_tr_search`; position `2668.5, -560.90625, 102.5846862793`
   - Map pin: ref `#ma_bls_ina_se1_08_tr_area`; position `2668.5, -574.41625976563, 102.5846862793`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/kill`
   - Map pin: ref `#ma_bls_ina_se1_08_tr_area`; position `2668.5, -574.41625976563, 102.5846862793`
6. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search`
   - Map pin: ref `#ma_bls_ina_se1_08_tr_find_psycho`; position `2681.4899902344, -548.15100097656, 104.0350112915`
7. **Message Regina about Cyberspycho Sighting: House on a Hill**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info`

## Cyberpsycho Sighting: Letter of the Law

- IGN walkthrough: [Cyberpsycho Sighting: Letter Of The Law](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Letter_Of_The_Law)
- Vanilla type: `CyberPsycho`
- Quest hash: `1157405054`
- Quest path: `quests/minor_quest/ma_hey_spr_06`
- District: Heywood / Wellsprings
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

I have a bad feeling about this. A real bad feeling.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/check_message`
2. **Read the shard "License? What license?!"**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/check_shard`
3. **Search the computer for more info.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/check_shard1`
4. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/clues`
   - Map pin: ref `#ma_hey_spr_06_tr_start`; position `-2382.2099609375, -1105.2747802734, 14.099999427795`
5. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/find_psycho`
   - Map pin: ref `#ma_hey_spr_06_tr_find_psycho`; position `-2401.740234375, -1084.6550292969, 13.059999465942`
6. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/kill_psycho`
7. **Message Regina about Cyberpsycho Sighting: Letter of the Law**  
   `Primary` · `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/send_info`

## Cyberpsycho Sighting: Lex Talionis

- IGN walkthrough: [Cyberpsycho Sighting: Lex Talionis](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Lex_Talionis)
- Vanilla type: `CyberPsycho`
- Quest hash: `355911891`
- Quest path: `quests/minor_quest/ma_pac_cvi_15`
- District: Pacifica
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

The underpass near GIM is like NC's Bermuda Triangle for the homeless. Sound like a piece of cake? In the heart of Pacifica, nothing ever is.\n\nEnter at your own risk.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_message`
2. **Search the computer for more info.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/clues`
   - Map pin: ref `#ma_pac_cvi_15_tr_psycho_reveal`; position `-2220.1306152344, -1942.6951904297, 5.6500005722046`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho`
   - Map pin: ref `#ma_pac_cvi_15_tr_psycho_reveal`; position `-2220.1306152344, -1942.6951904297, 5.6500005722046`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/kill_psycho`
6. **Message Regina about Cyberpsycho Sighting: Lex Talionis**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info`

## Cyberpsycho Sighting: Lt. Mower

- IGN walkthrough: [Cyberpsycho Sighting: Lt. Mower](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Lt._Mower)
- Vanilla type: `CyberPsycho`
- Quest hash: `45572989`
- Quest path: `quests/minor_quest/ma_wat_kab_08`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

WARNING! CYBERPSYCHO DETECTED. MILITECH HAS LOCKED DOWN THE AREA. KEEP AWAY!

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/check_message`
2. **Read the shard with the conversation between Dr. Martin Sypura and Lt. Mower.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/clues`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/find_psycho`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/kill_psycho`
6. **Send the information to Regina.**  
   `Primary` · `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/send_info`

## Cyberpsycho Sighting: On Deaf Ears

- IGN walkthrough: [Cyberpsycho Sighting: On Deaf Ears](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_On_Deaf_Ears)
- Vanilla type: `CyberPsycho`
- Quest hash: `2528051522`
- Quest path: `quests/minor_quest/ma_cct_dtn_03`
- District: City Center
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Hey V! Watch out. Whoever left those bodies is still hanging around.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/check_message`
2. **Read the shard "Archived Conversation: Maciej Nakonieczny and Cedric Muller"**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/check_shard`
3. **Read the shard "Archived Conversation: Maciej Nakonieczny and Peter Novotny"**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/check_shard_02`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/find`
   - Map pin: ref `#ma_cct_dtn_03_tr`; position `-2165.8298339844, 280.75997924805, 7.710000038147`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/kill`
   - Map pin: ref `#ma_cct_dtn_03_tr`; position `-2165.8298339844, 280.75997924805, 7.710000038147`
6. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/search_for_clues`
   - Map pin: ref `#ma_cct_dtn_03_tr`; position `-2165.8298339844, 280.75997924805, 7.710000038147`
7. **Message Regina about Cyberpsycho Sighting: On Deaf Ears**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/send_info`

## Cyberpsycho Sighting: Phantom of Night City

- IGN walkthrough: [Cyberpsycho Sighting: Phantom of Night City](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Phantom_of_Night_City)
- Vanilla type: `CyberPsycho`
- Quest hash: `3034309748`
- Quest path: `quests/minor_quest/ma_cct_dtn_07`
- District: City Center / Downtown
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Ghosts? Ghosts don't exist, V. The dead can tell you that.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/check_message`
2. **Read the shard "Archived Conversation: Norio Akushitsuna and Dr. Colin Thevenaz"**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/clues`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/find_psycho`
   - Map pin: ref `#ma_cct_dtn_07_tr`; position `-1684.3731689453, 248.0869140625, 7.4500017166138`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/kill_psycho`
6. **Message Regina about Cyberpsycho Sighting: Phantom of Night City**  
   `Primary` · `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/send_info`

## Cyberpsycho Sighting: Seaside Cafe

- IGN walkthrough: [Cyberpsycho Sighting: Seaside Cafe](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Seaside_Cafe)
- Vanilla type: `CyberPsycho`
- Quest hash: `3642072802`
- Quest path: `quests/minor_quest/ma_hey_spr_04`
- District: Heywood / Wellsprings
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Whoever killed them was packing a lot of hate, a lot of rage. And those feelings  don't fade quickly. Be careful.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/check_message`
2. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/find_psycho`
   - Map pin: ref `#ma_hey_spr_04_tr_find`; position `-2244.2314453125, -1315.7640380859, 11.960000038147`
3. **Defeat the attacker.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho`
4. **Search the attacker.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/loot_psycho`
5. **Read the "Saigon Sisters: Season Finale" script.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer`
6. **Read the shard "Message to Linh Hyunh".**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer1`
7. **Read the shard "Message to Dao Hyunh".**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_psycho`
8. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/search_clues`
   - Map pin: ref `#ma_hey_spr_04_tr_investigation`; position `-2259.7412109375, -1326.2182617188, 7.2699990272522`
9. **Message Regina about Cyberpsycho Sighting: Seaside Cafe.**  
   `Primary` · `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info`

## Cyberpsycho Sighting: Second Chances

- IGN walkthrough: [Cyberpsycho Sighting: Second Chances](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Second_Chances)
- Vanilla type: `CyberPsycho`
- Quest hash: `2694020012`
- Quest path: `quests/minor_quest/ma_bls_ina_se1_22`
- District: Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Everyone deserves a second chance, V. I know that better than most. But who's granting that chance and who's getting it are important questions that oughta be asked.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/check_message`
2. **Read the shard "I have seen the light".**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/check_shard`
3. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/find`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_area`; position `4777.8911132813, -1318.0637207031, 139.73417663574`
4. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/kill`
   - Map pin: ref `#ma_bls_ina_se1_22_tower`; position `4830.4599609375, -1386.4197998047, 142.96002197266`
5. **Scan the area for clues.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/scan_trail`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_search_trail_001`; position `4608.7822265625, -1245.9716796875, 143.61819458008`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_search_trail_002`; position `4653.21484375, -1260.0537109375, 144.76118469238`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_area_main`; position `4744.8950195313, -1285.7266845703, 139.73417663574`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_search_trail_003`; position `4762.4609375, -1322.3216552734, 136.85917663574`
6. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/search_for_clues`
   - Map pin: ref `#ma_bls_ina_se1_22_tr_area_main`; position `4744.8950195313, -1285.7266845703, 139.73417663574`
7. **Message Regina about Cyberpsycho Sighting: Second Chances**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/send_info`

## Cyberpsycho Sighting: Six Feet Under

- IGN walkthrough: [Cyberpsycho Sighting: Six Feet Under](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Six_Feet_Under)
- Vanilla type: `CyberPsycho`
- Quest hash: `1527882430`
- Quest path: `quests/minor_quest/ma_wat_nid_22`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Maelstrom certainly has its own unique recruitment and retention methods. Ranks getting too thin? Well, just kidnap a few Valentinos, knock 'em out cold and bolt on some new faceplates. What could possibly go wrong with that? Everything, that's what.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/check_message`
2. **Read the shard "Farewell" found on the attacker.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/clues`
   - Map pin: ref `#ma_wat_nid_22_tr_psycho_kill_2nd_area`; position `-1018.6309814453, 2767.8056640625, 7.1609435081482`
   - Map pin: ref `#ma_wat_nid_22_tr_psycho_kill`; position `-1055.4182128906, 2800.068359375, 7.1609435081482`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/find`
   - Map pin: ref `#ma_wat_nid_22_tr_area`; position `-1064.1245117188, 2795.525390625, 7.1046137809753`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/kill`
6. **Message Regina about Cyberpsycho Sighting: Six Feet Under**  
   `Primary` · `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/send_info`

## Cyberpsycho Sighting: Smoke on the Water

- IGN walkthrough: [Cyberpsycho Sighting: Smoke on the Water](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Smoke_on_the_Water)
- Vanilla type: `CyberPsycho`
- Quest hash: `1159080314`
- Quest path: `quests/minor_quest/ma_pac_cvi_08`
- District: Pacifica / Coastview
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

If it weren't for the all the screaming, dead Scavs and that wreck of a car, be a pretty nice place. But hey, that's life. Wanna go check it out, see what went down? Try the pier first.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/check_message`
2. **Find the cyberpsycho on the pier.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/find_psycho`
   - Map pin: ref `#ma_pac_cvi_08_tr_pier`; position `-2130.4270019531, -1502.8962402344, 12.059999465942`
3. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/kill_psycho`
4. **Search the body.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/loot_psycho`
5. **Search the van.**  
   `Optional` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/check_van`
   - Map pin: ref `#ma_pac_cvi_08_ps_car_mobster`; position `-1951.9826660156, -1600.4393310547, 4.6400003433228`
6. **Search the attacker.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/loot_psycho1`
7. **Read the shard titled "Archived Conversation: Hideyoshi Ueno and Ken Masuda."**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/read_shard_mobster`
8. **Read the shard titled "Archived Conversation: Ken Masuda and Diego Ramirez."**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/read_shard_psycho`
9. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/search_clues`
   - Map pin: ref `#ma_pac_cvi_08_tr_search`; position `-2142.3620605469, -1497.3325195313, 12.059999465942`
10. **Message Regina about Cyberpsycho Sighting: Smoke on the Water**  
   `Primary` · `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/send_info`

## Cyberpsycho Sighting: The Wasteland

- IGN walkthrough: [Cyberpsycho Sighting: The Wasteland](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_The_Wasteland)
- Vanilla type: `CyberPsycho`
- Quest hash: `1197003519`
- Quest path: `quests/minor_quest/ma_bls_ina_se1_07`
- District: Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `follow/escort`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Does a cyclone of dust and sand stirred up by a dash cyberpsychosis sound exciting? Then I do I have some good news for you.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/check_message`
2. **Read the shard "Archived Conversation: Shiv4theWin and Raffen_Fever"**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/clues`
   - Map pin: ref `#ma_bls_ina_se1_07_tr_end`; position `2682.0002441406, -1517.0001220703, 65.53101348877`
   - Map pin: ref `#ma_bls_ina_se1_07_tr_search`; position `2558.76953125, -1702.2598876953, 77.519989013672`
4. **Use your scanner to find traces of the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/find_psycho`
   - Map pin: ref `#ma_bls_ina_se1_07_tr_search`; position `2558.76953125, -1702.2598876953, 77.519989013672`
5. **Follow the blood trail.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail`
   - Map pin: ref `#ma_bls_ina_se1_07_tr_end`; position `2682.0002441406, -1517.0001220703, 65.53101348877`
   - Map pin: ref `#ma_bls_ina_se1_07_mp_track_01`; position `2574.935546875, -1679.294921875, 78.140647888184`
   - Map pin: ref `#ma_bls_ina_se1_07_mp_track_002`; position `2602.6784667969, -1651.6066894531, 72.725692749023`
   - Map pin: ref `#ma_bls_ina_se1_07_mp_track_003`; position `2626.150390625, -1622.8654785156, 69.033378601074`
   - Map pin: ref `#ma_bls_ina_se1_07_mp_track_004`; position `2617.8029785156, -1574.8756103516, 66.065521240234`
   - Map pin: ref `#ma_bls_ina_se1_07_mp_track_005`; position `2640.3852539063, -1537.2620849609, 65.769966125488`
6. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/kill_psycho`
7. **Message Regina about Cyberpsycho Sighting: The Wasteland**  
   `Primary` · `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/send_info`

## Cyberpsycho Sighting: Ticket to the Major Leagues

- IGN walkthrough: [Cyberpsycho Sighting: Ticket to the Major Leagues](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Ticket_to_the_Major_Leagues)
- Vanilla type: `CyberPsycho`
- Quest hash: `1727988675`
- Quest path: `quests/minor_quest/ma_wat_lch_06`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Not all people cope the same way when those first symptoms of cyberpsychosis show up. Some throw themselves off a bridge. Others hand themselves over to the cops. And most of the rest try to self-treat with sedatives – as many as they can get their hands on. No matter the cost.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/check_message`
2. **Read the shard "Glitter"**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/check_shard`
3. **Read the shard "Ticket to the Major Leagues"**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/check_shard_partner`
4. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/clues`
   - Map pin: ref `#ma_wat_lch_06_tr_start`; position `-2058.9404296875, 1238.8999023438, 3.8900001049042`
5. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/find_psycho`
   - Map pin: ref `#ma_wat_lch_06_tr_start`; position `-2058.9404296875, 1238.8999023438, 3.8900001049042`
6. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/kill_psycho`
7. **Message Regina about Cyberpsycho Sighting: Ticket to the Major Leagues**  
   `Primary` · `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/send_info`

## Cyberpsycho Sighting: Under the Bridge

- IGN walkthrough: [Cyberpsycho Sighting: Under The Bridge](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Under_The_Bridge)
- Vanilla type: `CyberPsycho`
- Quest hash: `1568141133`
- Quest path: `quests/minor_quest/ma_std_arr_06`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

V, you don't have anywhere else to be? Only thing you'll stir up here is trouble. I'd beat it, but... you do you.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_message`
2. **Read the shard "Archived Conversation: Tamara Cosby and Tony Ludic".**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_shard`
3. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/kill_psycho`
6. **Message Regina about Cyberpsycho Sighting: Under The Bridge**  
   `Primary` · `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info`

## Cyberpsycho Sighting: Where the Bodies Hit the Floor

- IGN walkthrough: [Cyberpsycho Sighting: Where the Bodies Hit the Floor](https://www.ign.com/wikis/cyberpunk-2077/Cyberpsycho_Sighting:_Where_the_Bodies_Hit_the_Floor)
- Vanilla type: `CyberPsycho`
- Quest hash: `1626134206`
- Quest path: `quests/minor_quest/ma_wat_nid_03`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

There are few certainties in Night City… Super-sketch stomach-melting streetfood, politicians choked by corporate leashes and the echo of screams heard coming from the Totentanz club. Oh wait, and one more: if you step foot down the wrong alley, your head will probably roll out the other end.

### Objective sequence

1. **Read Regina's message in the cyberpsycho message thread.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/check_message`
2. **Read the shard "Archived Conversation: Brick and Ellis".**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/check_shard`
3. **Read the shard "Archived Conversation: Hoof and Sanders".**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/check_shard_02`
4. **Find the cyberpsycho.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/find`
   - Map pin: ref `#ma_wat_nid_03_tr_area`; position `-1710.7592773438, 2222.7678222656, 18.19995880127`
5. **Neutralize the threat.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/kill`
6. **Search the area to collect information.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/search_for_clues`
   - Map pin: ref `#ma_wat_nid_03_tr_area`; position `-1710.7592773438, 2222.7678222656, 18.19995880127`
7. **Send the information to Regina.**  
   `Primary` · `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/send_info`

## Gig: A Lack of Empathy

- IGN walkthrough: [A Lack of Empathy](https://www.ign.com/wikis/cyberpunk-2077/A_Lack_of_Empathy)
- Vanilla type: `StreetStory`
- Quest hash: `3760582495`
- Quest path: `quests/street_stories/city_center/downtown/sts_cct_dtn_03`
- District: City Center / Downtown
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Upload a virus to Empathy's subnet\nLocation: Empathy\nDetails:\n\nMeet Adam Ibrahimovic and Larry Fanghorn. Adam's the bad guy and Larry's our client.\n\nOnce upon a time the two friends opened a club called Empathy and things got off the ground pretty quickly. The eddies poured in, their popularity surged, they were surrounded by hordes of young ladies and one question at the back of their minds – who's got their hand in who's pocket? Adam or Larry?\n\nThe blame fell on our innocent, naive Larry.\n\nWhat does Adam do? He changes the club's access codes, made a few shady deals and hired Animals as bouncers. If you were Larry, wouldn't you be pissed?\n\nHere's what you're gonna do. You'll break into Empathy, upload the attached virus to their net and bring the club's operations to a standstill. Empathy won't budge an inch until Adam welcomes his ol' pal Larry back with open arms.\n\nSounds like a breeze, right? Just keep things quiet, no witnesses and everyone'll be happy.

### Objective sequence

1. **Enter the "Empathy" club.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/get_in_the_club`
   - Map pin: ref `#dtn_03_gps_marker_005`; position `-1630.3990478516, 405.51864624023, 8.0920000076294`
2. **Find the subnet's main computer.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/get_inside_server_room`
   - Map pin: ref `#dtn_03_server_room`; position `-1639.5194091797, 372.42083740234, 14.086702346802`
   - Map pin: ref `#dtn_03_gps_marker_01`; position `-1624.0941162109, 399.7109375, 8.0920000076294`
   - Map pin: ref `#dtn_03_gps_marker_002`; position `-1620.6812744141, 383.78302001953, 8.0930004119873`
   - Map pin: ref `#dtn_03_gps_marker_003`; position `-1614.6339111328, 366.36083984375, 8.0860004425049`
   - Map pin: ref `#dtn_03_gps_marker_004`; position `-1620.2086181641, 396.14538574219, 9.4010000228882`
3. **Collect your reward from the Drop Point.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/get_to_drop_point`
4. **Retrieve your weapons.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/get_your_weapons_back`
5. **Upload the virus to the club's server.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/infect_main_server`
6. **Leave the club.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/leave_club`
7. **Sabotage Empathy.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/sabotage_empathy_club`
8. **Avoid getting into combat.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/avoid_combat`
9. **Deposit your weapons.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_03/sts_cct_dtn_03/leave_weapons`

## Gig: A Shrine Defiled

- IGN walkthrough: [A Shrine Defiled](https://www.ign.com/wikis/cyberpunk-2077/A_Shrine_Defiled)
- Vanilla type: `StreetStory`
- Quest hash: `1105932277`
- Quest path: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03`
- District: Westbrook / Japantown
- Level: 60
- Candidate building blocks: `travel/reach location`, `retrieve/collect item`, `deliver/deposit item`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Place a wiretap in a Tyger Claw-controlled shrine\nLocation: Shinto shrine at Milagro Terrace\nDetails:\n\nThe person should not stray from the road and the tiger should not leave his mountain steppes. Or misfortune will find them both.\n\nTyger Claw boss Taki Kazo thinks he's smart. He thinks I won't find out about his agreement at the shinto shrine on Milagro Terrace. He thinks I don't know he's using the shrine's honden for secret meetings. He thinks he can rule Japantown without my influence. He will be wrong.\n\nI'll give you a wiretap to place right at the shintai in the most sacred of shinto spaces. Don't make a noise. And don't disappoint me.

### Objective sequence

1. **Get out of the shrine complex.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone`
2. **Get to the honden.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in`
3. **Remain undetected.**  
   `Optional` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth`
4. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward`
5. **Place the wiretap inside the shrine's main hall.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden`

## Gig: An Inconvenient Killer

- IGN walkthrough: [An Inconvenient Killer](https://www.ign.com/wikis/cyberpunk-2077/An_Inconvenient_Killer)
- Vanilla type: `StreetStory`
- Quest hash: `593305771`
- Quest path: `quests/street_stories/city_center/downtown/sts_cct_dtn_02`
- District: City Center / Downtown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Neutralize Jack Mausser\nLocation: 7th Hell Club, corner of Corporation St. and Ringroad West\nDetails:\n\nI'll cut to the chase. Jack Mausser – NC's gonkest merc. Did a recent job for me and went too far. Way too fucking far. He was supposed to klep some shards from a Zetatech transport – quiet-like. Except it wasn't fucking quiet. That psycho offed every single guard, beheaded the driver and blew up the truck. Corp's foaming at the mouth, searching high and low for the prick, and I'll be damned if I go down 'cause of him. I need you to toss his head at their feet. Maybe then they'll let this go.\n\nMausser owns a seedy club downtown called 7th Hell. Gut tells me he's holed up there till the smoke's cleared. I need you to get inside the club and take his psycho ass down – preferably on the down-low. Understood? Good. Let me know when it's done.

### Objective sequence

1. **Tell the fixer to send a ride.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/call`
2. **Talk to Jack Mausser.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/talk_jack`
3. **Find Jack Mausser.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/find_targets`
   - Map pin: ref `#dtn_02_tr_7thhell`; position `-1950.5963134766, -44.317760467529, -3.7943105697632`
4. **Get to Jack Mausser in VIP area.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/find_way_inside`
   - Map pin: ref `#dtn_02_tr_vip_room`; position `-1925.52734375, -32.223251342773, 3.4656896591187`
5. **Carry the body to the designated location.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/get_body`
   - Map pin: ref `#dtn_02_tr_enter`; position `-1943.5059814453, -56.129566192627, 7.4656896591187`
6. **Get inside 7th Hell.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/get_inside`
   - Map pin: ref `#dtn_02_tr_enter`; position `-1943.5059814453, -56.129566192627, 7.4656896591187`
7. **Leave the club.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/get_out`
   - Map pin: ref `#dtn_02_tr_enter`; position `-1943.5059814453, -56.129566192627, 7.4656896591187`
8. **Collect your reward from the Drop Point.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/get_reward`
9. **Neutralize Jack Mausser.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/kill`
10. **Carry Mausser to the fixer's car.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/put_in_trunk`
   - Map pin: ref `#dtn_02_fixer_car`; position `-1902.1685791016, -83.98014831543, 7.9199991226196`
11. **Avoid entering combat inside the club.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_02/sts_cct_dtn_02/do_not_start_combat`

## Gig: Backs Against the Wall

- IGN walkthrough: [Backs Against the Wall](https://www.ign.com/wikis/cyberpunk-2077/Backs_Against_the_Wall)
- Vanilla type: `StreetStory`
- Quest hash: `1197270346`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_03`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`

### Journal premise

Gig type: Search and Recover\nObjective: Recovered stolen medicine\nLocation: Housing block on Columbus St.\nDetails:\n\nA few years back I scrolled a little feature called "How Affordable is Health?" It turns out not very. My numbers showed only 3 percent of Night Citizens could afford healthcare. A lot has changed since. For the worse. Some people are declaring open war on rippers, breaking into clinics, klepping meds and chems. No surprise there. And no surprise these rippers want to protect what's theirs.\n\nThey want you to recover a pack of stolen meds. Thanks to the GPS tracer hidden inside, we know exactly where to look.

### Objective sequence

1. **Go to the indicated residence.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house`
2. **Find the stolen medicine.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds`
3. **Deposit the medicine in the Drop Point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve`
4. **Retrieve the stolen medicine.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve_stolen_meds`
5. **Retrieve the stolen medicine.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds`

## Gig: Big Pete's Got Big Problems

- IGN walkthrough: [Big Pete's Got Big Problems](https://www.ign.com/wikis/cyberpunk-2077/Big_Pete%27s_Got_Big_Problems)
- Vanilla type: `StreetStory`
- Quest hash: `4224564162`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02`
- District: Badlands
- Level: 60
- Candidate building blocks: `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Get rid of Big Pete – a mechanic with the Wraiths.\nDetails:\n\nBig Pete runs a garage out here in the Badlands, fixes up clunkers for the Raffen Shiv. Before that he was hustling as a techie in Night City. Now, Pete's not your definition of a nice guy. Soon enough he made some powerful enemies and had to skip town.\nJust so happens Pete's enemies are my friends and I owe said friends a favor. You make Big Pete eat dust – I get one less favor to owe.\n\nIt's not hard to find him. Just try any of the Wraith's garages.

### Objective sequence

1. **Carry out the hit on Big Pete.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/complete_the_hit_on_big_pete`
2. **Neutralize Big Pete.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete`
3. **Find Big Pete.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete`
4. **Get inside Big Pete's garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in`
5. **Leave the area.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave`

## Gig: Bloodsport

- IGN walkthrough: [Bloodsport](https://www.ign.com/wikis/cyberpunk-2077/Bloodsport)
- Vanilla type: `StreetStory`
- Quest hash: `2454252026`
- Quest path: `quests/street_stories/watson/little_china/sts_wat_lch_03`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `retrieve/collect item`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Roh Chi-Won\nLocation: Tyger Claws dojo on Brookland St.\nDetails:\n\nMatter's urgent. My client, Macidew Coolidge (you might recognize him from his show,"Boxathon," on N54 from a few years back) is looking for someone to get his coach back from the Tyger Claws.\n\nHere's the deal. Macidew got himself into a debt hole. Looking to climb out the easy way, he cut a deal with the Tygers. They gave him a wad of cash to go down in the next fight. And what did he do with it? He goes to the bookie incognito and bets on his own win. Next thing you know, he KO's his opponent in the second round and blasts off into the sunset in an AV.\n\nIt was happily ever after for Macidew, until they kidnapped his coach, Roh Chi-Won. They're threatening to kill him if Macidew doesn't come back to Night City. Macidew doesn't want his coach's death to weigh on his conscience, so he got in touch with me and I got in touch with you. Sending you the coords for where they're keeping Roh Chi-Won. Try getting to him without tripping the alarm. Hostages and shootouts don't mix well. Good luck.

### Objective sequence

1. **Escort Roh to the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/escort_roh_to_car`
2. **Collect your reward.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/get_special_reward`
3. **Go to the Tyger Claws' dojo.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/go_inside_building`
4. **Do not raise the alarm.**  
   `Optional` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/optional_alarm`
5. **Go down to the basement.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/go_to_basement`
6. **Find out where Roh is being held.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/go_to_ricky_wu`
7. **Help Roh get outside.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/lead_ricky_outside`
8. **Set Roh free.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/rescue_ricky`
9. **Talk to Roh.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_03/sts_wat_lch_03/talk_with_roh`

## Gig: Breaking News

- IGN walkthrough: [Breaking News](https://www.ign.com/wikis/cyberpunk-2077/Breaking_News)
- Vanilla type: `StreetStory`
- Quest hash: `1540656053`
- Quest path: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Deliver van\nLocation: Kendachi Factory, Arroyo\nDetails:\n\nYou ever watch the news? Personally, I think it's all propaganda. But that's just me. Still, people watch, and some people make the news.\n\nMy client's Ted Fox, an N54 reporter. He's doing a story on the link between gangs and corps. On paper, they're enemies, but in reality, seems like the corporats and gangoons are scratching each other's backs. Key word – seems. Ted needs hard evidence.\n\nThat's where you come in to save the day. Ted'll tell you exactly what you have to do, but be ready to get onto Kendachi factory grounds, poke around. All clear? Head on over to Ted. As they say in the media biz – it's showtime!

### Objective sequence

1. **Collect your reward.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/collect_reward`
2. **Go back to Ted.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/go_back_to_parking`
   - Map pin: ref `#arr_05_tr_sts_parking_001`; position `-230.35942077637, -1699.4689941406, 6.818359375`
3. **Install the tracker.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/install_a_tracking_chip`
4. **Contract type: Sabotage\nGoal: Put tracking device under a Kendachi’s truck. \nClients dossier: Ted Fox, age 37 a well-known 54 news reporter \nLocation: Parking lot near Kendachi's factory in Arroyo  \n\nDetails: My client's been looking into the illegal implant trade run by the 6th Street gang via a Kendachi factory. Fox got some info that the gangers are reportedly using some next-gen military-grade combat implants (Alfa-Bravo-Control Cybereye).  He’s sure it’s the factory manager selling the implants to the gangers on the side. Find Ted Fox near Kendachi factory, take tracking device and put it under truck.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/meet_with_ted`
5. **Enter Ted Fox's car.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/sit_with_ted`
6. **Remain undetected.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/be_unseen`
7. **Leave the parking lot.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/escape`
   - Map pin: ref `#arr_05_marker_003`; position `-280.77005004883, -1721.0299072266, 8.5800008773804`
8. **Get to the parking lot.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/get_to_the_factory_parking`
   - Map pin: ref `#arr_05_tr_factory_parking`; position `-273.24127197266, -1725.6343994141, 9.8023586273193`
9. **Plant the tracker in truck.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/instal_chip_on_truck`
10. **Talk to Ted Fox.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/speak_with_ted`
11. **Take the tracker.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/take_tracking_device`

## Gig: Bring Me the Head of Gustavo Orta

- IGN walkthrough: [Bring Me the Head of Gustavo Orta](https://www.ign.com/wikis/cyberpunk-2077/Bring_Me_the_Head_of_Gustavo_Orta)
- Vanilla type: `StreetStory`
- Quest hash: `4069781424`
- Quest path: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01`
- District: Heywood / Vista Del Rey
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Gustavo Orta\nLocation: Building on Petrel St.\nDetails:\n\nThe world is built on certain rules. Rules that don't appear out of nothing – which grew from the blood and mistakes of our predecessors. These rules are meant to protect us, but the young disregard them. They believe they are special, that they are not held to the same rules, that fate is theirs to tempt.\n\nMartha Frakes believed the same and now sleeps in a coma after taking a bullet to the head. The streets tell me this is her punishment for abandoning family. The girl turned from her own father, Nolan Frakes, to side with the enemy – Gustavo Orta.\n\nBut what the street says doesn't matter – not to Nolan. He believes Gustavo is solely responsible for what happened to his daughter. Let's fulfill the wish of a father desperate for revenge. He's paying, after all.\n\nGo to Gustavo's apartment. Deal with him. Don't worry about authorization. My netrunner made sure you don't run into any problems.\n\nAnd FYI – if you hadn't caught on yet – Gustavo is Valentinos, Nolan is 6th Street. Stay sharp.

### Objective sequence

1. **Put Gustavo in the trunk.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/drop_body`
2. **Find Gustavo.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/find_gustavo`
3. **Collect your reward from the Drop Point.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/get_reward`
4. **Convince Gustavo to leave town.**  
   `Optional` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/persuade`
5. **Contract type Bounty Hunt \n Goal Get rid off Gustavo Orta \nLocation Apartment block in Vista del Ray \n Details  Get rid off Gustavo Orta. Gustavo is high rank Valentino living in apartment in Vista del Rey. He got under Nolan Frakes's skin - 6th Street who's daughter was dating Gustavo. Recently, Martha get shot and now she is lying in coma in hospital. Nolan blames Gustavo for this tragedy. You need to get inside Gustavo's apartment in Vista del Rey and get rid off him. If it's possible, try to convince him to get out of the city**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/get_inside_flat`
   - Map pin: ref `#rey_01_mp_building`; position `-969.560546875, 82.722145080566, 8.4112777709961`
6. **Go to the 32nd floor.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/get_to_floor`
   - Map pin: ref `#rey_01_mp_elevator`; position `-979.07458496094, 99.71875, 9.7468490600586`
7. **Go to Gustavo's apartment.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/gustavo_apartment`
8. **Neutralize Gustavo.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/kill_gustavo`
9. **Leave the apartment complex.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/leave_building`
10. **Leave the apartment complex with Gustavo's body.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01/sts_hey_rey_01/take_body_outside`
   - Map pin: ref `#rey_01_mp_building_001`; position `-968.44073486328, 81.921836853027, 8.4112777709961`

## Gig: Catch a Tyger's Toe

- IGN walkthrough: [Catch a Tyger's Toe](https://www.ign.com/wikis/cyberpunk-2077/Catch_a_Tyger%27s_Toe)
- Vanilla type: `StreetStory`
- Quest hash: `2718872079`
- Quest path: `quests/street_stories/watson/little_china/sts_wat_lch_01`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `travel/reach location`, `hack/breach/download`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Upload b@d's malware\nLocation: Megabuilding H11\nDetails:\n\nb@d got in touch with me. They like short nicknames and simple gigs, so I'll spare you the fixer spiel and get right to the point.\n\nYou'll find b@d's malware attached to this message. You have to download it (just be careful – it's hella dangerous) and then upload it to the subnet in the H11 megabuilding. Piece o' cake, right? Sorry to burst your bubble, but you'll have Tygers on the prowl.\n\nb@d's plan is to attack some Arasaka subnet and use H11 as a smokescreen. Clever, right? Instead of leading to them, all traces of b@d's breach'll lead right back to the megabuilding.\n\nFYI, our netrunner already hacked the megabuilding elevator, so getting into the server room won't be a problem.

### Objective sequence

1. **Leave the server room.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/get_out`
2. **Get to the main server.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/get_to_server_room`
3. **Upload b@d's malware to the system.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/upload_software`

## Gig: Cuckoo's Nest

- IGN walkthrough: [Cuckoo's Nest](https://www.ign.com/wikis/cyberpunk-2077/Cuckoo%27s_Nest)
- Vanilla type: `StreetStory`
- Quest hash: `1318564080`
- Quest path: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Jasmine Dixon\nLocation: Psychiatric ward on Sequoia St.\nDetails:\n\nI'm not a fan of badges. They stick their nose in other people's biz, give ordinary people a hard time, do the corps' bidding. But sometimes it's worth getting into bed with your enemies – at least they'll owe you something for later.\n\nThere's this badge, Jasmine Dixon. She's been patrolling NC streets since '61, reached the rank of sergeant. One day at the precinct she heard something she shouldn't've. Instead of keeping her mouth shut, she took it to her supervisor. The next day they wheeled her off to a psych ward. The kind where they prescribe lobotomies and electrotherapy.\n\nHer husband will do anything to help her and as far as payment goes, "anything" is as good as it gets. You'll get your standard rate, of course. So, whaddya say? Gotta help a couple in need, don't you think?

### Objective sequence

1. **Escort Jasmine Dixon to the transport.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/get_to_the_car`
2. **Get inside the hospital.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/inside`
   - Map pin: ref `#rcr_02_mp_inside`; position `668.38262939453, -1401.0177001953, 29.366863250732`
3. **Take the guard's keys.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/key`
4. **Escort Jasmine Dixon out of the hospital.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/leave`
5. **Open Jasmine Dixon's cell.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/open`
   - Map pin: ref `#rcr_02_jasmine_door_marker`; position `666.19964599609, -1441.0495605469, 34.23999786377`
6. **Find Jasmine Dixon's cell.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/reach`
7. **Reach Jasmine Dixon's cell (no. 7, 2nd floor)**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/reach1`
8. **Save Jasmine Dixon.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/rescue_jasmine`
9. **Get inside the restricted area.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/secured`
   - Map pin: ref `#rcr_02_door_second`; position `674.14782714844, -1432.7315673828, 28.574001312256`
10. **Talk to Jasmine Dixon.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/talk`
11. **Talk to Jasmine Dixon.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02/sts_std_rcr_02/talk_to_jasmine`

## Gig: Dancing on a Minefield

- IGN walkthrough: [Dancing on a Mine Field](https://www.ign.com/wikis/cyberpunk-2077/Dancing_on_a_Mine_Field)
- Vanilla type: `StreetStory`
- Quest hash: `1997294558`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07`
- District: Badlands
- Level: 60
- Candidate building blocks: `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Special Delivery\nObjective: Retrieve the abandoned car from the minefield and deliver it to Dakota\nLocation: Nearest road off Interstate 9\nDetails:\n\nThe Badlands are peppered with disarmed minefields from 2071. Though, after several folk were "dislegged" by these "disarmed" mines, most decided to steer clear of these areas. That is, except the smuggling types. A number of their routes run through those fields.\n\nRisky, yes, but brilliant all the same. Why would anyone guard the border when the mines practically do your job for you?\n\nBut listen up: a smuggler and his rig got stranded out in the middle of one of those minefields. Maybe his tank went dry, maybe he had a heart attack, or maybe he set out on some vision quest – who knows, doesn't matter. What's important is I don't know the routes these fellas run and now they're getting dropped in my lap.\n\nGet me this stranded vehicle. I know some nomads who'd pay handsomely for that GPS data.

### Objective sequence

1. **Approach the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/approach_the_car`
2. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/collect_reward`
3. **Deliver the vehicle to the garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/deliver_car`
   - Map pin: ref `#ina_07_mp_workshop`; position `2421.7717285156, -772.36663818359, 66.69953918457`
4. **Find the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/find_car`
5. **Get in the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/get_inside`
6. **Get rid of the pursuers.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/get_rid_of_chase`
7. **Exit the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/leave_car`
8. **Leave the shop.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/leave_workshop`
   - Map pin: ref `#ina_07_mp_leave_workshop`; position `2422.5903320313, -764.79504394531, 66.699546813965`
9. **Park in the garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/park_in_garage`
   - Map pin: ref `#ina_07_mp_workshop`; position `2421.7717285156, -772.36663818359, 66.69953918457`
10. **Examine the body.**  
   `Optional` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/optional_investigation`
11. **Escape with the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/run_away`
12. **Do not damage the car.**  
   `Optional` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/dont_damage_the_car`

## Gig: Dirty Biz

- IGN walkthrough: [Dirty Biz](https://www.ign.com/wikis/cyberpunk-2077/Dirty_Biz)
- Vanilla type: `StreetStory`
- Quest hash: `12580887`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Get the raw BD of the murder of Bryce Stone's son\nLocation: Buildings off Shipyard Way\nDetails:\n\nMy good friend, the televangelist Bryce Stone (don't ask, it's complicated) needs our help. His little boy was kidnapped and brutally murdered a few days later. The NCPD dropped the case due to lack of evidence. Bryce decided to take matters into his own hands and found the BD scroll of his murder, but the virtu's heavily edited, meaning there aren't a lot of clues to go on. If you could get your hands on the raw cut there's a chance we could identify the murderer.\n\nThe virtu was put out by two XBD tuners (Gottfrid and Fredrik) in Northside. I'm betting they still have the original somewhere. Just watch out for the Maelstromers that are guarding them.

### Objective sequence

1. **Find the XBD recording.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/find_recording`
2. **Take recording BD_9430.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_recording`
3. **Deposit the recording in the Drop Point.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_droppoint`
4. **Contract type Retrieving\nGoal Get an original recording of a black BD of a murder\nClients dossier Bryce Stone, televangelist from NEWS54\nLocation Docks in Northside Industrial District\nDetails Client's son was murdered. Guy who murdered his son recorded everything on a braindance. My intel tells me that recording is currently in the hands of Gottfrid&Frederik - creators of The Shuttle Dock - one of the most famous BD sharing site - and BD dealers as well. You have to go to these two guys and take the original version of Braindance from them - using the original recording televangelist will be able to analyze the crime and find the murderer.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_hideout`
5. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/leave_area`

## Gig: Error 404

- IGN walkthrough: [Error 404](https://www.ign.com/wikis/cyberpunk-2077/Error_404)
- Vanilla type: `StreetStory`
- Quest hash: `1623874770`
- Quest path: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Bring down propaganda machine slandering Weldon Holt\nLocation: Garage on Oak St.\nDetails:\n\nPolitics. Only thing slimier than the thongs at Licks. At least corpos usually tell you to your face how they're gonna screw you in the end. Fake smiles, impossible promises, shameless pandering – all foreplay till they fuck you in the ass and pay themselves for it with eddies outta your wallet. It's in their nature. And what's in ours? Blowing shit up. Got just such a gig for you this time.\n\n6th Street's got a stiffy for Jefferson Peralez so they have these servers pumping out anti-Holt propaganda. They see Peralez becoming mayor as like the second coming of Abraham Lincoln or some shit, here to unite the city with the NUSA. Naive gonks.\n\nTL;DR – My client wants 6th Street's propaganda machine gone. Simple.

### Objective sequence

1. **Find the garage with the servers.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/access_miss_rose_garage`
2. **Install Malware**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/destroy_server`
3. **Enter the garage area.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/enter_garage_area`
4. **Leave the area.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/leave_area`
5. **Search for garage 66.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/look_for_garage_66`

## Gig: Eye for an Eye

- IGN walkthrough: [Eye For An Eye](https://www.ign.com/wikis/cyberpunk-2077/Eye_For_An_Eye)
- Vanilla type: `StreetStory`
- Quest hash: `1472895526`
- Quest path: `quests/street_stories/heywood/glen/sts_hey_gle_01`
- District: Heywood / The Glen
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Tucker Albach\nLocation: Condo on the corner of Scoffield and Sinkyone St.\nDetails:\n\nA girl died a while back in the Glen. Her name was Rosita. I knew her. Seventeen years old, picture-perfect smile. Got hit by a car while she was crossing the road. I saw the CCTV – almost tore her legs off clean. If she'd've gotten to the emergency room sooner, she might've lived. Who knows. But it was the middle of the night, empty street. Driver fled the scene.\n\nSoon enough, the NCPD found our culprit. Lady's named Tucker Albach, vice managing director or something at Kiroshi. Her insurance covered vehicular manslaughter so as far as the NCPD's concerned – she's off the hook. Only punishment she got is her insurance raising her premium. Hardly a slap on the wrist.\n\nOver my dead body. This isn't what justice is supposed to look like. Eye for an eye, tooth for a tooth, hand for a hand, wound for a wound. Rosita wants Tucker gone, and you're gonna pull the trigger.

### Objective sequence

1. **Carry Tucker to the fixer's car.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/deliver_body_to_car`
2. **Talk to Tucker Albach.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/talk_with_tucker`
3. **Neutralize Tucker Albach.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/eliminate_tucker`
4. **Leave Tucker's building.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/exit_location`
5. **Carry Tucker out of the building.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/exit_location_with_body`
6. **Get inside Tucker's building.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/get_access_to_appartement`
7. **Find Tucker Albach.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/get_trough_to_tucker`
   - Map pin: ref `#gle_01_mp_tucker_office_001`; position `-1685.8023681641, -972.90930175781, 20.646364212036`
8. **Take the money from the safe.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_01/sts_hey_gle_01/get_money_from_safe`

## Gig: Family Heirloom

- IGN walkthrough: [Family Heirloom](https://www.ign.com/wikis/cyberpunk-2077/Family_Heirloom)
- Vanilla type: `StreetStory`
- Quest hash: `1617241117`
- Quest path: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06`
- District: Westbrook / Charter Hill
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Search and Recover\nObjective: Rare, bootleg Samurai recording\nLocation: Parking lot on Crockett St.\nDetails:\n\nThere's this old saying – if it wasn't for fools, there would be no sages. The same is true for fixers.\n\nThe fool who needs your help is a man named Dan. Dan has a gambling problem – lately he managed to lose his car in a game of cards. To tell the truth, the ride's no great loss or anything – this guy isn't short on cars. What was valuable, however, was the one-of-a-kind bootleg Samurai recording stowed in the trunk. How did our fool come into possession of it, you ask? Well, he's Nancy's son. The same Nancy who played keyboard for the band, in the days when that snot-nosed boy used to call me "aunty."\n\nYou'll get that album for me. Gut tells me they haven't pawned it off just yet, it's probably still stashed somewhere around the place. And if you can swing it, grab Dan's car too for a little bonus. I'll snap you the coordinates of the guy holding the goods. And be aware, he licks the boots of the 6th Street Gang, so expect to deal with another fool. A stubborn one.

### Objective sequence

1. **Deliver the recording to Dan.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/deliver_bootleg`
2. **Leave the parking lot.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/escape`
   - Map pin: ref `#hil_06_marker_escape`; position `432.41195678711, -398.46463012695, 7.5022048950195`
3. **Find the bootleg recording of Samurai.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/find_bootleg`
   - Map pin: ref `#hil_06_tr_bootleg`; position `416.38000488281, -427.80026245117, 3.0499999523163`
4. **Go to the parking lot.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/get_inside`
   - Map pin: ref `#hil_06_tr_enter`; position `436.60818481445, -435.26803588867, 2.6390211582184`
5. **Deliver the car to Dan.**  
   `Optional` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/deliver_car`
   - Map pin: ref `#hil_06_parking_spot`; position `-148.78698730469, -109.64752197266, 9.4899959564209`
   - Map pin: ref `#hil_06_tr_car_deliver`; position `-154.61010742188, -113.83001708984, 6.9599981307983`
6. **Exit the car.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/get_out_car`
7. **Leave the area.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/get_out_from_dan`
   - Map pin: ref `#hil_06_tr_safe_zone`; position `-169.15362548828, -106.943359375, 14.479994773865`
8. **Return to the car.**  
   `Optional` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/get_back_car`
   - Map pin: ref `#hil_06_the_car`; position `414.24203491211, -440.86694335938, 2.9749104976654`
9. **Retrieve Dan's car.**  
   `Optional` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/take_car`
   - Map pin: ref `#hil_06_the_car`; position `414.24203491211, -440.86694335938, 2.9749104976654`
   - Map pin: ref `#hil_06_tr_enter`; position `436.60818481445, -435.26803588867, 2.6390211582184`
10. **Collect your reward from Drop Point.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/get_reward`
11. **Retrieve the bootleg recording of Samurai.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06/sts_wbr_hil_06/retrieve_bootleg`

## Gig: Family Matters

- IGN walkthrough: [Family Matters](https://www.ign.com/wikis/cyberpunk-2077/Family_Matters)
- Vanilla type: `StreetStory`
- Quest hash: `3432934147`
- Quest path: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`

### Journal premise

Gig type: Search and Recover\nObjective: Retrieve the Zetatech data Juliet Horrigan owes El Capitán\nLocation: House on Gibson St.\nDetails:\n\nI like everyone to know I'm patient, understanding. I realize there's a time for work and a time for family. Without a good work-life balance we'd all blast our brains out. I get it, I do. But... disappearing for 2 weeks cuz of "family issues?" That how Juliet thinks of me? How much she respects me? I love her cuz she's ripped so much nova data outta Zetatech for me, but man she's starting to hurt my feelings, you know?\n\nGo to her place, see what her deal is. But remember – #1 priority is that data she still owes me. Juliet's nova and all, but if she's got a problem with that, well... like I said, data is prio #1.

### Objective sequence

1. **Deposit the datashard in the Drop Point.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver`
2. **Find a way to open the safe.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe`
3. **Get the chip from Juliet's home.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/get_datachip`
4. **Go to Juliet's home.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house`
5. **Look for the chip.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house`
6. **Exit the building.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/leave_house`
7. **Take the chip from the safe.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/loot_datachip`
8. **Open the safe.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe`
9. **Find out what happened to Juliet.**  
   `Optional` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate`

## Gig: Fifth Column

- IGN walkthrough: [Fifth Column](https://www.ign.com/wikis/cyberpunk-2077/Fifth_Column)
- Vanilla type: `StreetStory`
- Quest hash: `1009463697`
- Quest path: `quests/street_stories/heywood/glen/sts_hey_gle_04`
- District: Heywood / The Glen
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal data on Javier Alvarado's embezzlement activity\nLocation: El Pinche Pollo Restaurant\nDetails:\n\nIt's election season so everyone's got a political stick up their ass. Can't say I like it but it is good for biz.\n\nYoung woman came up to me, claims to be a media. She must be a wizard with words because I've never seen a mediajock like her burn so much cash.\n\nShe's fishing for dirt on the mayor's adviser, Javier Alvarado. Says Alvarado is bezzling public money, padding the Valentinos' pockets.\n\nProof? Apparently found in the office of El Pinche Pollo, some Valentino-run restaurant. Have a look there. This media seemed confident of her sources.\n\nAnd you know how this rolls. She fronts the eddies, we don't ask who she "writes" for.

### Objective sequence

1. **Enter the restaurant.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in`
2. **Get inside the office.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner`
3. **Leave the restaurant.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area`
4. **Steal the incriminating data.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/main_objective`
5. **Find incriminating evidence on the mayor's advisor.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence`
6. **Drink to Jackie with the bouncer.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink`

## Gig: Fixer, Merc, Soldier, Spy

- IGN walkthrough: [Fixer, Merc, Soldier, Spy](https://www.ign.com/wikis/cyberpunk-2077/Fixer,_Merc,_Soldier,_Spy)
- Vanilla type: `StreetStory`
- Quest hash: `2754148664`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_04`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `phone/message contact`, `travel/reach location`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal Mikhail Akulov's datashard\nLocation: Hotel Raito on Adam St.\nDetails:\n\nRemember the job with Mikhail Akulov's car that you royally botched? I hope so, cuz this time you're going to make up for it. In case your memory needs refreshing, Akulov is a top-tier soviet fixer who's in NC to cut some deal with Arasaka. Go to our dear comrade's hotel and klep his datashard. comrade.\n\nThe shard supposedly contains extremely valuable intel on talks with the Japanese. My client wants that shard.\n\nAs if it needs to be said, but he'll have heavy protection. And remember I'll pay extra if you do this on the hush.\n\nCall me when it's done.

### Objective sequence

1. **Gain access to the elevator.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/access_elevator`
   - Map pin: ref `#kab_04_mp_0lvl_elevators`; position `-1207.6518554688, 1391.2447509766, 24.130310058594`
2. **Neutralize Nadezhda.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/defeat`
3. **Go to Mikhail Akulov's penthouse.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/acess_penthouse`
   - Map pin: ref `#kab_04_mp_penthouse`; position `-1200.9658203125, 1406.8822021484, 109.80194854736`
4. **Do not raise the alarm.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/do_not_trigger_combat`
5. **Deliver the shard to Regina's client.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/deliver`
6. **Obtain Mikhail Akulov's datashard.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/extract_data1`
7. **Enter the elevator.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/get_inside_elevator`
   - Map pin: ref `#kab_04_mp_generic_elevator`; position `-1205.8400878906, 1389.6198730469, 21.300003051758`
   - Map pin: ref `#kab_04_mp_penthouse_elevator`; position `-1209.6204833984, 1389.6198730469, 21.300003051758`
8. **Enter Hotel Raito.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/get_inside_hotel`
9. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/get_reward`
10. **Go to the meeting point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/hand_the_briefcase`
11. **Leave the hotel.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/leave_the_penthouse`
   - Map pin: ref `#kab_04_mp_exit`; position `-1183.830078125, 1400.8400878906, 21.260000228882`
12. **Call Regina.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_04/sts_wat_kab_04/phone`

## Gig: Flight of the Cheetah

- IGN walkthrough: [Flight of the Cheetah](https://www.ign.com/wikis/cyberpunk-2077/Flight_of_the_Cheetah)
- Vanilla type: `StreetStory`
- Quest hash: `1847882645`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`

### Journal premise

Gig type: SOS: Merc Needed\nTarget: Hwangbo\nLocation: Motel on Martin St.\nDetails:\n\nYou know that classic comedy setup where a gonk gets into serious trouble and only some, like, misanthropic hardass can save him? Well, let that be your guiding plot for today.\n\nThe gonk in question is called Hwangbo. He did some small-time work for the Tyger Claws, but instead of keeping his head down and being patient, he took a shortcut and stole from his own gang. Genius, right? Not only that, but the whole thing had his name written all over it.\n\nHwangbo's marked for death, meaning he has to disappear – the faster, the better. I already found a nomad smuggler, but someone still needs to get him from one end of the city to the other. But if he's spotted out on the street, the Tyger Claws'll know about it. You know what you gotta do, right? So let's get to it. He's holed up somewhere in the motel on Martin.

### Objective sequence

1. **Escort Hwangbo to the meeting with the nomads.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/escort_haruo_to_nomad`
   - Map pin: ref `#nid_03_tr_nomad_place_001`; position `-1015.5104980469, 2636.9541015625, 22.123355865479`
2. **Go to the meeting point.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/stop_car`
   - Map pin: ref `#sts_wat_nid_03_tr_stop_car`; position `-1014.5002441406, 2636, 22.123046875`
3. **Talk to Hwangbo before leaving.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/talk_with_hwangbo_nomad`
4. **Use Hwangbo's car.**  
   `Optional` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/go_to_car`
   - Map pin: ref `#nid_03_ws_hwango_car_spawn_001`; position `-1478.2900390625, 2155.771484375, 18.479999542236`
5. **Meet Hwangbo in room 1237.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/find_haruo`
6. **Find Hwangbo.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/find_room_1237`
   - Map pin: ref `#nid_03_tr_find_room_001`; position `-1495.2698974609, 2207.8100585938, 18.180000305176`
7. **Talk to Hwangbo.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03/sts_wat_nid_03/talk_with_haruo`

## Gig: Flying Drugs

- IGN walkthrough: [Flying Drugs](https://www.ign.com/wikis/cyberpunk-2077/Flying_Drugs)
- Vanilla type: `StreetStory`
- Quest hash: `2881403711`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03`
- District: Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Eliminate cause for drone disappearance\nLocation: Union RR\nDetails:\n\nA good friend of mine, Mosquito, is running an op in the Badlands. He packs a chem shipment in a drone and sends it off to the city, then when he gets his eddies wired, he slices off a piece for me. The problem now is those drones aren't making roost at their destinations. Someone's plucking them out of the sky along the way.\n\nWe sent the last drone with a GPS tag. The thieves took the bait and we're getting pinged from the transmitter. You follow that ping then make sure Mosquito's birds can fly free once again.

### Objective sequence

1. **Talk to Dakota.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/call_fixer`
2. **Collect your reward from Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/collect_reward`
3. **Destroy the antenna.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/destroy_antenna`
4. **Examine the destroyed drone.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/examine_drone`
5. **Locate the transmission source.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/find_antenna`
6. **Enter the room with the drone.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/find_missing_drone`
7. **Find out how the drones were intercepted.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/find_source_of_transmission`
8. **Go to the signal source.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/go_to_the_signal_destination`
9. **Determine how the Wraiths hijacked the drones.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/investigate_the_area`
10. **Leave the outpost.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/leave_the_outpost`
11. **Stop the drones from being stolen.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/missing_drones`
12. **Hack the system to destroy the antenna.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/netrunner_destroy`

## Gig: For My Son

- IGN walkthrough: [For My Son](https://www.ign.com/wikis/cyberpunk-2077/For_My_Son)
- Vanilla type: `StreetStory`
- Quest hash: `754516214`
- Quest path: `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05`
- District: Pacifica / West Wind Estate
- Level: 60
- Candidate building blocks: `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Logan Garcia\nLocation: Old Paint Factory on Baptiste St.\nDetails:\n\nTarget's name is one Logan Garcia. He runs an Animals fight club. Used to fight himself, actually. Still gets in the ring from time to time. Problem is he doesn't know when to put on the brakes. Recently he knocked his sparring buddy, Lenny Steiner, to the mat with a giant dent in his skull. Except instead of calling for help, he had the kid thrown in the bay with a cinderblock tied round his neck.\n\nThe kid's mom, Monica Steiner, wants justice for her sweet baby boy, Lenny. More importantly, she's willing to pay to get it. Do the job, it's yours. Minus my modest cut, of course.

### Objective sequence

1. **Carry the body to the fixer's transport.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/bring_body_to_car`
   - Map pin: ref `#wwd_05_fixer_car`; position `-510.59802246094, -1874.2733154297, 7.7688975334167`
2. **Put Logan in the trunk.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/get_body_to_trunk`
   - Map pin: ref `#wwd_05_fixer_car`; position `-510.59802246094, -1874.2733154297, 7.7688975334167`
3. **Get inside the boxing club at the old paint factory.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/get_inside_factory`
   - Map pin: ref `#wwd_05_tr_factory`; position `-479.03198242188, -1941.4150390625, 7.137656211853`
4. **Neutralize Logan Garcia.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/kill_logan`
5. **Leave the boxing club.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/leave_building`
   - Map pin: ref `#wwd_05_tr_factory`; position `-479.03198242188, -1941.4150390625, 7.137656211853`
6. **Find Logan Garcia.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/locate_logan`
   - Map pin: ref `#wwd_05_tr_inside`; position `-499.65631103516, -1932.34375, 7.987060546875`
7. **Carry the body outside.**  
   `Primary` · `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05/sts_pac_wwd_05/take_body_outside`
   - Map pin: ref `#wwd_05_fixer_car`; position `-510.59802246094, -1874.2733154297, 7.7688975334167`

## Gig: Freedom of the Press

- IGN walkthrough: [Freedom of the Press](https://www.ign.com/wikis/cyberpunk-2077/Freedom_of_the_Press)
- Vanilla type: `StreetStory`
- Quest hash: `2686455703`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Max and bring him to me\nLocation: the old broadcast TV in Northside\nDetails:\n\nNight City doesn't like people that like to kick the hornet's nest, and Max Jones... well, he kicked a bunch of 'em at the same time. Kicked them so hard, in fact, that someone put a hit out on him. Thing is, personally, I'd rather he stayed alive.\n\nMax Jones is an old friend from my muckraking days. We co-wrote a vidcast about independent farmers who were put out of biz by Biotechnica drones. Those were the days.\n\nNowadays, Max doesn't even take my calls. He's as stubborn as they come, but now I'm worried he's really lost touch with reality. He probably thinks he can manage perfectly fine on his own, but that's what all young, gonk men think – that they're invincible. Bring him to reason, will ya?\n\nSending you the coords to his hideout. If I managed to track him down, it's only a matter of time until the others do too.

### Objective sequence

1. **Carry Max outside.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/carry_max`
2. **Collect your reward.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/collect_reward`
3. **Convince Max to meet with Regina.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/confront_max`
4. **Escort Max outside.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/escort_max`
5. **Find Max.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/find_max`
6. **Enter the TV studio building.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/get_inside_building`
7. **Find Max.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/get_to_max`
8. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/leave`
9. **Persuade or force Max Jones to meet with Regina.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/main`
10. **Place Max in the trunk.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_12/sts_wat_nid_12/max_trunk`

## Gig: Getting Warmer...

- IGN walkthrough: [Getting Warmer](https://www.ign.com/wikis/cyberpunk-2077/Getting_Warmer)
- Vanilla type: `StreetStory`
- Quest hash: `223590576`
- Quest path: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09`
- District: Westbrook
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `interact/use device`, `retrieve/collect item`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue netrunner from Tyger Claws\nTarget info: 8ug8ear, real name unknown, 24 years old\nLocation: Salinas St.\nDetails:\n\nUsed to be 8ug8ear and the Tygers got along. They were supposed to work a Kiroshi warehouse job together, but she left them out to dry – remotely drove out a van packed with high-end gear and abandoned them inside. Certain death. But those Tygers are a tough crew, you know how stubborn they can be. The next day they pull up to her apartment wanting to know where she stashed the tech. 8ug8ear was desperate, escaped to the Net, shrouded herself in soft that'd flatline her if they tried to disconnect her. Of course now they just have to watch the clock tick. Eventually, 8ug8ear will have to come out or risk frying her own synapses. And the Tygers are patient, especially in matters of revenge. Personally, I think they like it more this way.\n\nGet 8ug8ear out of there and give word – I'll send transport. But remember to disconnect her safely. She's useless to me dead.

### Objective sequence

1. **Carry 8ug8ear to the fixer's car.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/bring_tobias`
   - Map pin: ref `#rey_09_sm_arrive`; position `-528.46246337891, 1302.5087890625, 37.25345993042`
2. **Lower 8ug8ear's body temperature before disconnecting her.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/cool_down`
3. **Find 8ug8ear.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/find_tobias`
4. **Find a way to safely disconnect 8ug8ear.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/find_way_to_cool`
5. **Take coolant.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/get_coolants`
6. **Enter the building.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/get_in`
   - Map pin: ref `#rey_09_tr_leave`; position `-558.56622314453, 1303.1251220703, 37.253028869629`
7. **Carry 8ug8ear out of the building.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/leave_building`
   - Map pin: ref `#rey_09_tr_leave`; position `-558.56622314453, 1303.1251220703, 37.253028869629`
8. **Save 8ug8ear.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/main`
9. **Disconnect 8ug8ear.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_09/sts_hey_rey_09/unplug_tobias`

## Gig: Going Up or Down?

- IGN walkthrough: [Going Up or Going Down](https://www.ign.com/wikis/cyberpunk-2077/Going_Up_or_Going_Down)
- Vanilla type: `StreetStory`
- Quest hash: `940686843`
- Quest path: `quests/street_stories/heywood/glen/sts_hey_gle_05`
- District: Heywood / The Glen
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`

### Journal premise

Gig type: Thievery\nObjective: Scandium rods\nLocation: Megabuilding H1, Congress St.\nDetails:\n\nThis isn't your run-of-the-mill gig. Client this time is me. You know the H1 megabuilding in the Glen? City within a city – crumbling tower of concrete and faulty wiring. That it hasn't already collapsed is thanks to a guy named El Gallo. Brilliant techie, he was. Past tense.\n\nIt's the same old story. El Gallo's got a drug problem. A big one. He's completely lost touch with reality, goes from one score of syn-coke to another. Needless to say, he's in no state to repair any creaky doors. But for some reason he got it into his head that everything'll be better if he could just get his hands on some scandium rods, so he stole them from a corpo warehouse.\n\nThese rods are rare parts. Rare and very expensive. I wouldn't want to see them go to waste. Go to H1 (access code's already taken care of) and get them from El Gallo before that junkie pawns them. I don't care how you do it, so long as it gets done.

### Objective sequence

1. **Neutralize El Gallo.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill`
2. **Talk to El Gallo.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo`
3. **Deposit scandium rods in the Drop Point.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver`
4. **Go to El Gallo's workshop.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find`
   - Map pin: ref `#gle_05_hideout_mappin`; position `-1616.6008300781, -563.69317626953, 12.189999580383`
5. **Go outside.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave`
   - Map pin: ref `#gle_05_hideout_leave`; position `-1612.9200439453, -567.32318115234, 17.929998397827`
6. **Look for the scandium rods.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores`
7. **Take the scandium rods from the cache.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts`
8. **Steal the scandium rods.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk`

## Gig: Going-away Party

- IGN walkthrough: [Going-Away Party](https://www.ign.com/wikis/cyberpunk-2077/Going-Away_Party)
- Vanilla type: `StreetStory`
- Quest hash: `302638271`
- Quest path: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `vehicle sequence`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Flavio dos Santos\nLocation: Mallagra St.\nDetails:\n\n6th Street got shaken up with an internal coup, the boss took a bullet in the back of the head. The guy who filled his shoes was the same who pulled the trigger – they call him Gunner.  The new bossman has unleashed a purge to rid the gang of all the people loyal to the last chief. My client, Flavio, is next in line to get shot and he'd very much like to skip town.\n\nAlready struck a deal with the nomads who agreed to ship him to the other coast. All you have to do is escort Flavio to the place their guide will pick him up. Little problem to note: there's already a price on our friend's head, so he's gotta watch it.\n\nSending you coords of where Flavio's holed up. You need to get there, load him into your ride, and deliver to the nomads ASAP. Keep your iron at the ready and don't forget to always check your mirrors. 6th St gave him a death sentence so any tails on his ass are likely to be hot.

### Objective sequence

1. **Find out what happened to Flavio.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/check_on_hayashi`
2. **Enter Flavio's hideout and find out what happened.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/check_what_happened_to_flavio`
   - Map pin: ref `#rcr_03_tr_safehouse_mp_new`; position `471.42108154297, -1240.8819580078, 30.50634765625`
3. **Enter the hideout.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/enter_building`
   - Map pin: ref `#rcr_03_tr_safehouse_mp_new`; position `471.42108154297, -1240.8819580078, 30.50634765625`
4. **Exit car.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/exit_car`
5. **Find Flavio dos Santos in his hideout.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/find_flavio`
   - Map pin: ref `#rcr_03_tr_safehouse_mappin`; position `479.58892822266, -1234.9260253906, 26.457275390625`
   - Map pin: ref `#rcr_03_tr_safehouse_mappin`; position `479.58892822266, -1234.9260253906, 26.457275390625`
   - Map pin: ref `#rcr_03_tr_safehouse_mappin`; position `479.58892822266, -1234.9260253906, 26.457275390625`
6. **Escort Flavio to the transport.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/get_hayashi_to_ca`
7. **Go and get Flavio from the hideout.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/go_to_safehouse`
   - Map pin: ref `#rcr_03_tr_safehouse_mp_new`; position `471.42108154297, -1240.8819580078, 30.50634765625`
8. **Get in the car with Flavio.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/join_flavio_in_car`
9. **Bring Flavio to the nomad contact.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/meet_nomad_contact`
   - Map pin: ref `#rcr_03_tr_near_nomad`; position `260.06704711914, -1576.6617431641, 7.5100002288818`
10. **Return to Car**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/return_to_car`
11. **Scan the bodies to find Flavio.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/scan_bodies_to_find_flavio`
12. **Talk to Flavio.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/talk_hayashi`
13. **Talk to the nomad.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03/sts_std_rcr_03/talk_to_nomad`

## Gig: Goodbye, Night City

- IGN walkthrough: [Goodbye, Night City](https://www.ign.com/wikis/cyberpunk-2077/Goodbye,_Night_City)
- Vanilla type: `StreetStory`
- Quest hash: `4290605476`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05`
- District: Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Bruce Welby\nLocation: Coachwhip Ln.\nDetails:\n\nSometimes you need a friend to lean on. Sometimes you need a friend to break you out of an immigrant detention center at the Night City-SoCal border.\n\nSmuggler Bruce Welby required the latter.\n\nBruce tried to cross the state line with hot cargo in tow, but it didn't work out as planned and now he's been chained up by Militech border security already several days. His buddy (and Militech employee), Archibald Crane, found out about the situation through the grapevine. I'll be damned if that cuckoo corpo actually decided to help his friend instead of towing the corpo line. He contacted me to get Bruce out of his cage.\n\nYou're the missing element in this friendship triangle. Find Bruce, break him out, and escort him to his chombatta, Archie. And let's make sure Militech doesn't notice a thing, OK? Get to it.\n\nOne more thing – Archie says not to kill any corpos. So, what can I say? The client's always right.

### Objective sequence

1. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/collect_reward`
2. **Do not kill any Militech personnel.**  
   `Optional` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/dont_kill_militech`
3. **Escort Bruce outside the compound.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/escort_bruce_new`
4. **Find Bruce inside the compound.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/find_bruce`
5. **Reach Militech's compound.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_in_farm`
6. **Exit the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_out_car`
7. **Take Bruce to Archibald.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_to_archibald`
8. **Escape the compound using the truck in parking lot.**  
   `Optional` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_to_truck`
9. **Reach Militech's compound.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_to_area`
10. **Reach Bruce.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/get_to_bruce`
11. **Escort Bruce outside the compound.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/help_escape`
12. **Take Bruce to the extraction point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/take_bruce_to_meeting_point`
13. **Talk to Archibald.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/talk_archibald`
14. **Talk to Bruce.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/talk_bruce`
15. **Wait for Archie.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05/sts_bls_ina_05/wait_for_archie`

## Gig: Greed Never Pays

- IGN walkthrough: [Greed Never Pays](https://www.ign.com/wikis/cyberpunk-2077/Greed_Never_Pays)
- Vanilla type: `StreetStory`
- Quest hash: `2542047576`
- Quest path: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12`
- District: Westbrook / Japantown
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Search and Recovery\nObjective: Retrieve Leah Gladen's lockbreaker device\nLocation: Building on the corner of Holly and Floyd St, door code 2137\nDetails:\n\nA great treasure can turn out to be a great curse. Remember that, V.\n\nOne of the fences in my territory, Leah Gladen, came into possession of some highly valuable equipment – a lockbreak device capable of jailbreaking corp cyberware (some call it a CorpCracker). This tech opens doors for suits who want out but don't want to lose function of corp-issued chrome or are looking to make an extra eddie by selling secondhand.\n\nLeah wasn't born yesterday. She knows what the tech is worth. She and I went back and forth, long price negotiations. We were close to reaching a deal when all contact was lost.\n\nYour job is to find out what happened to Leah – but more importantly to get that skeleton key for me. Don't bother reporting back until you have it. Don't waste time.

### Objective sequence

1. **Get out of Wired Head.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape`
2. **Reach the hidden room.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way`
3. **Go to Leah Gladen's apartment block.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block`
4. **Deposit the equipment at the Drop Point.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint`
5. **Enter code 2137.**  
   `Optional` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code`
6. **Go to Leah Gladen's apartment.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment`
7. **Go to the braindance club Wired Head.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples`
8. **Go to the braindance club Wired Head.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/go_to_bd_bar`
9. **Take Leah Gladen's equipment.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker`
10. **Search Leah Gladen's apartment.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence`
11. **Search the hidden room.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room`
12. **Search Wired Head.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar`

## Gig: Guinea Pigs

- IGN walkthrough: [Guinea Pigs](https://www.ign.com/wikis/cyberpunk-2077/Guinea_Pigs)
- Vanilla type: `StreetStory`
- Quest hash: `1595061866`
- Quest path: `quests/street_stories/city_center/downtown/sts_cct_dtn_04`
- District: City Center / Downtown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Eliminate Joanne Koch\nLocation: Biotechnica corporate hotel, on Republic Way\nDetails:\n\nChick's name is Joanne Koch, regional director for tech and development or some shit at Biotechnica. Means she tests all the shiny new gizmos. Last little gizmo she tested? Yeah, that one flatlined over 70 souls – folks from a clan called Red Orchid or Red Ocher or something like that. Koch tried to dry the tears of victims' families with a few ennies (ever try that? doesn't work) and decided to close the book on it. Sure enough, book didn't close all the way – all them families pooled together to hire someone who'd give this Director Koch the cordial greeting she deserves. You know the kind – SUPER CORDIAL, to show her they REALLY CARE.\n\nI'll flick you the coords and the access code to the corpo hotel Koch is holed up in. Shoot me a word after the smoke's cleared.

### Objective sequence

1. **Neutralize the attackers on the roof before the AV arrives.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/clear_out_roof`
   - Map pin: ref `#dtn_04_tr_roof_mp`; position `-2158.91015625, 470.79995727539, 95.679992675781`
2. **Talk to Joanne Koch.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/talk_to_joanne_koch`
3. **Carry Koch to the AV.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/deliver_body`
   - Map pin: ref `#dtn_04_tr_av`; position `-2150.2097167969, 477.25994873047, 96.249954223633`
4. **Get inside the hotel.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/enter_the_hotel`
   - Map pin: ref `#dtn_04_tr_1st_floor`; position `-2148.7006835938, 469.09072875977, 9.4750099182129`
5. **Escape the hotel.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/escape_the_hotel`
   - Map pin: ref `#dtn_04_tr_1st_floor`; position `-2148.7006835938, 469.09072875977, 9.4750099182129`
6. **Find Joanne Koch.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/find_joanne_koch`
   - Map pin: ref `#dtn_04_tr_target_floor_journal`; position `-2150.2482910156, 480.19277954102, 89.398361206055`
7. **Get inside Koch's apartment.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/get_inside_apartment`
   - Map pin: ref `#dtn_04_tr_target`; position `-2167.1994628906, 457.8147277832, 89.555404663086`
8. **Neutralize Joanne Koch.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/kill_billy`
   - Map pin: ref `#dtn_04_tr_hotel`; position `-2124.0017089844, 481.05355834961, 9.4809455871582`
9. **Stay clear of the landing zone.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/move_away_from_take_off_zone`
10. **Reach the 19th floor.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/reach_2nd_floor`
   - Map pin: ref `#dtn_04_elevator`; position `-2126.9484863281, 482.81735229492, 9.4747352600098`
   - Map pin: ref `#dtn_04_mp_sm_room`; position `-2130.0310058594, 482.70431518555, 89.494812011719`
11. **Wait for the AV outside the landing zone.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_04/sts_cct_dtn_04/wait_for_av_outside_landing_zone`

## Gig: Hacking the Hacker

- IGN walkthrough: [Hacking the Hacker](https://www.ign.com/wikis/cyberpunk-2077/Hacking_the_Hacker)
- Vanilla type: `StreetStory`
- Quest hash: `70279251`
- Quest path: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `hack/breach/download`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Infect 6th Street computer with a virus\nLocation: 6th Street hideout on MLK Blvd\nDetails:\n\nThose boys and girls from 6th Street think they got wicked smarts, that they can jump a Militech transport in my hood without me knowing about it. They think they can crack corpo weapons and tip the balance of power in this city to their favor. It's time they got a rude awakening.\n\nI'll snap you the location of the 6th St hideout and the door code. Job's simple – find a way in, look for the comp they use to jailbreak corpo tech, upload the virus I'll supply to you and voila, their fancy new weapon melts into a sparkly new slagheap.\n\nOne more thing. If you happen to find a Lucius Thoran, do me a favor and make his ass disappear, will ya? Thoran's a techie – came up with this gonk plan, which makes him a real thorn in my ass. Pun intended.\n\nStay safe and have fun.

### Objective sequence

1. **Upload the virus onto 6th Street netrunner's computer.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete`
2. **Find 6th Street netrunner's computer.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/find`
3. **Get inside 6th Street's hideout.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside`
4. **Enter the megabuilding.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding`
   - Map pin: ref `#sts_std_arr_11_elevator_marker`; position `-168.82002258301, -871.19006347656, 11.470001220703`
5. **Leave the 6th Street hideout.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out`
   - Map pin: ref `#sts_std_arr_11_exit_lab`; position `-209.24015808105, -849.23059082031, 7.6600189208984`
   - Map pin: ref `#sts_std_arr_11_elevator_marker_001`; position `-168.05990600586, -871.04010009766, 263.18002319336`
6. **Go to the Drop Point.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point`
7. **Kill Lucius.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius`

## Gig: Hippocratic Oath

- IGN walkthrough: [Hippocratic Oath](https://www.ign.com/wikis/cyberpunk-2077/Hippocratic_Oath)
- Vanilla type: `StreetStory`
- Quest hash: `3798498617`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_02`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `retrieve/collect item`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Lucy Thackery from Maelstrom captivity\nLocation: Clean Cut clinic on Longshore North St.\nDetails:\n\nBlood looks out for blood. Bertie's a leadhead who was gonk enough to join up with Maelstrom. Realized pretty quick the psychogang operates by simple rules – you stay, you die, or you pay.\n\nIn comes his sister, Lucy, who chose option number three. Instead of hard scratch, she bought out her bro's freedom with her expertise and services. She put 3 months of cyberware repair on the table. Problem is, five months have already come and gone.\n\nNow in comes you. This gig's on Bertie's dime – guess he had a few extra eddies stuffed in his mattress.

### Objective sequence

1. **Escort Lucy Thackery outside.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/escor`
   - Map pin: ref `#kab_02_tr_main`; position `-1156.1545410156, 2411.0822753906, 7.1124377250671`
2. **Escort Lucy to the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/escort_to_car`
3. **Find Lucy.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/find`
   - Map pin: ref `#kab_02_tr_lucy_loc`; position `-1177.4216308594, 2424.5944824219, 7.1065673828125`
4. **Persuade Lucy to leave.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/persuade`
5. **Pick up the synthetic blood.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/blood`
6. **Go to the Clean Cut building.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/get_inside`
   - Map pin: ref `#kab_02_tr_main`; position `-1156.1545410156, 2411.0822753906, 7.1124377250671`
7. **Talk to Lucy Thackery.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/tlk`
8. **Inject the patient with synthetic blood.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/blood_inject`
9. **Pick up the clotter.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/filler`
10. **Inject patient with the clotter.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/filler_inject`
11. **Scan the patient.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/scan`
12. **Rescue Lucy Thackery.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/main`

## Gig: Hot Merchandise

- IGN walkthrough: [Hot Merchandise](https://www.ign.com/wikis/cyberpunk-2077/Hot_Merchandise)
- Vanilla type: `StreetStory`
- Quest hash: `2763167402`
- Quest path: `quests/street_stories/heywood/wellsprings/sts_hey_spr_06`
- District: Heywood / Wellsprings
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Neutralize Rebeca Price\nLocation: Data Inc. Store in Heywood\nDetails:\n\nI'm guessing you don't follow the stock market, but recently Militech has been lagging behind everyone else. Just stroll around Corpo Plaza and you'll see their HQ abuzz like a hornet's nest. You can tell they're just itching for an excuse to send the armed cavalry into the city.\n\nYou've got reasonable people telling you not to get under corps' skins, and then you have Rebeca Price, who decides to open a fucking store selling hacked (and previously stolen) Militech equipment. It's not that I don't value small businesses – on the contrary! It's just that not having the fucking army on our streets is something I value more.\n\nRebeca Price needs to disappear. The "how" is your call. I won't go into the fine details. And I'm sure you know what to do if any Animals get in your way. They of all creatures should understand the importance of balance in our delicate little ecosystem.

### Objective sequence

1. **Find Rebeca Price.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/find_nolan`
2. **Find a way into the basement.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/find_path`
3. **Reach the back of the store.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/get_in_back`
4. **Contract type Bounty Hunt\nGoal Get rid off Rebeca Pryce\nTarget dossier Rebeca Pryce, age 35, owner of the pawnshop in Wellspring \nLocation Electronic shop in Wellspring.\nDetails Get rid off Rebeca Pryce. Rebeca is an owner of the electronic shop in Wellspring. It is, however, only a disguise. Infrared signature detected under her shop other construction. It's find out that Rebeca is hacking there Militech high tech weapon and send it on the street. If Rebeca will not disapear, Militech will start doing big mess in Heywood. I want to avoid this. Rebeca has to disapear. If it will be possible bring her to me alive.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/get_in_shop`
5. **Leave the store.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/get_out`
6. **Carry the body to the car.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/get_to_car`
7. **Neutralize Rebeca Price.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/kill_nolan1`
8. **Carry Rebeca out of the store.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_06/sts_hey_spr_06/pick_up`

## Gig: Jeopardy

- IGN walkthrough: [Jeopardy](https://www.ign.com/wikis/cyberpunk-2077/Jeopardy)
- Vanilla type: `StreetStory`
- Quest hash: `1377965103`
- Quest path: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06`
- District: Heywood / Vista Del Rey
- Level: 60
- Candidate building blocks: `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Search and Recover\nObjective: Shard with daemon program\nLocation: La Catrina Crematorium, intersection of Phalarope and Plover St.\nDetails:\n\nI'd like you to commit a minor transgression against God and His people – disturbing the dead from their eternal rest.\n\nDeceased's name is Jim Greyer. He smuggled unstable shards by slotting them inside his head. Sadly, during his last transit things went sideways. The Daemon got out of its cage and barbecued his brain. Jim Greyer ended up in the La Catrina funeral home along with my client's shard.\n\nGo to La Catrina, find Greyer's body and get that shard before it's burnt to cinders. FYI – the crematorium's cozy with the Valentinos. That's where they get rid of their bodies. One wrong move and you'll end up there too.

### Objective sequence

1. **Deposit the shard in the Drop Point.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop`
2. **Leave the crematorium.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape`
   - Map pin: ref `#rey_06_tr_funeral_house`; position `-1137.0987548828, -666.32019042969, 8.2500038146973`
3. **Get inside the morgue.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body`
   - Map pin: ref `#rey_06_tr_morgue`; position `-1127.8034667969, -675.46575927734, 4.2500038146973`
4. **Find Jim Greyer's body.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1`
   - Map pin: ref `#rey_06_tr_funeral_001`; position `-1115.8640136719, -652.45190429688, 8.2500038146973`
5. **Look for Jim Greyer's body in the morgue.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue`
   - Map pin: ref `#rey_06_tr_morgue`; position `-1127.8034667969, -675.46575927734, 4.2500038146973`
6. **Contract type Thievery\nGoal Retrieve the shard from Grayer’s head. \nLocation La Cartina Funeral House in Vista Del Rey . \n\nDetails My client worked with a Nomad mule, Jim Greyer. Contractor gave him a shard, which Greyer used to smuggle danger cybervirus. Unfortunately, during his last smuggling op, the security system malfunctioned, freezing Jim’s head before he even got to the Spaceport. Greyer’s body now lies in the morgue at the La Cartina Funeral Home (controlled by Valentinos) awaiting cremation. You have to retrieve shard form smuggler’s head.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home`
7. **Retrieve the infected shard.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/main`
8. **Find Jim Greyer using your scanner.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies`
9. **Pull the shard from Jim Greyer's body.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs`

## Gig: Last Login

- IGN walkthrough: [Last Login](https://www.ign.com/wikis/cyberpunk-2077/Last_Login)
- Vanilla type: `StreetStory`
- Quest hash: `3900720086`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_05`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal Alois Daquin's laptop\nLocation: Housing block on Eisenhower St.\nDetails:\n\nAlois Daquin – the corpo megaprick who cheated me. And not only me. There's a whole city out there that wants to get its hands on this guy. As they say, the fate of a traitor is sealed at the time of his betrayal.\n\nBut what interests me beyond my vengeance is Alois' datapad and, well, the data on it. Our traitor picked up and fucked off right outta NC so fast he left his gear in town.\n\nJust 20 min. ago I got a login ping from his comp on an Eisenhower St. localnet.\n\nHead over there and grab his device. Once we get it, we take advantage of this confused mess.

### Objective sequence

1. **Enter the building where Alois' laptop was connected to the Net.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/check_signal`
2. **Deposit the laptop in the Drop Point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/deliver_shard`
3. **Find Alois' laptop.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/get_shard`
   - Map pin: ref `#kab_05_tr_basement`; position `-1110.4373779297, 2145.98046875, 9.3701620101929`
4. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/go_to_ride`
   - Map pin: ref `#kab_05_tr_inside`; position `-1111.5426025391, 2144.0969238281, 9.392970085144`
5. **Retrieve Alois' laptop.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/loot_shard`
   - Map pin: ref `#kab_05_tr_basement`; position `-1110.4373779297, 2145.98046875, 9.3701620101929`

## Gig: Life's Work

- IGN walkthrough: [Life's Work](https://www.ign.com/wikis/cyberpunk-2077/Life%27s_Work)
- Vanilla type: `StreetStory`
- Quest hash: `2796335445`
- Quest path: `quests/street_stories/heywood/glen/sts_hey_gle_06`
- District: Heywood / The Glen
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Search and Recover\nObjective: Upload a virus and retrieve Jake Estevez's custom car\nLocation: McBride St.\nDetails:\n\nWhy is it some unwritten law of the world that every talented techie has shit-poor character? Only God knows.\n\nJake Estevez is one such genius among techies and an asshole among shitheads. Fifteen minutes with the man and my barrel against his forehead, but good news is we found a way to get along.\n\nJake's been a grease monkey for 6th Street about TWO WEEKS now. (Of course, I'm not on good terms with 6SG, but I do grudgingly admire their patience. It is, after all, a virtue.) Over that time Jake's been doing a custom job on a car for them – his "life's work," he says. Designed the soft for it too. Remember I said he has shit-poor character? Yeah, well he pissed off the wrong pendejos in 6SG and had to delta and never look back.\n\nBottom line: Jake wants his precious car back. Go the 6SG autoshop, upload the virus I sent you and get it back for him – don't scratch the ride and you'll get extra. We'll both be flush after this.

### Objective sequence

1. **Collect the reward.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/collect_reward`
2. **Deliver the vehicle to Jake Estevez.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/delicer_car`
   - Map pin: ref `#gle_06_car_target`; position `-1431.8237304688, -1288.6013183594, 47.180000305176`
3. **Go to the auto shop.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/entergarage`
   - Map pin: ref `#gle_06_tr_inside_garage_001`; position `-1443.6602783203, -1297.1378173828, 47.078277587891`
4. **Leave the garage.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/exit_garage`
   - Map pin: ref `#gle_06_tr_end_garage`; position `-1196.3084716797, -1100.33984375, 12.934143066406`
5. **Do not damage Jake's car.**  
   `Optional` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/do_not_damage`
6. **Exit the vehicle.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/leave`
7. **Get to Jake's car.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/reach_car`
   - Map pin: ref `#gle_06_car_target`; position `-1431.8237304688, -1288.6013183594, 47.180000305176`
8. **Retrieve Jake's car.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/retrieve_car`
   - Map pin: ref `#gle_06_tr_inside_garage_001`; position `-1443.6602783203, -1297.1378173828, 47.078277587891`
9. **Talk to Jake Estevez.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/talk`
10. **Upload the software to start the car.**  
   `Primary` · `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/uploaddata`

## Gig: Lousy Kleppers

- IGN walkthrough: [Lousy Kleppers](https://www.ign.com/wikis/cyberpunk-2077/Lousy_Kleppers)
- Vanilla type: `StreetStory`
- Quest hash: `4132951293`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `wait/time gate`, `search/investigate`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal the databank with the transport route data from Malorian Ltd.\nLocation: Warehouse, Offshore St.\nDetails:\n\nV, big news going around town. A Malorian van was stolen on Sir Francis Drake avenue. Maelstrom claimed responsibility.\n\nIt just so happens that one of my informants saw the whole thing, and he was smart enough to tail them using a drone.\n\nHard part's over – we already know where they've stashed the van. I'd say we got lucky, but the truth is my people know how to get shit done. OK, OK, I'll quit flattering myself.\n\nGo to the chop shop and find a databank in the van that has Malorian's transport route data. The gangers have no idea it's worth more than the all the cargo they're sitting on.

### Objective sequence

1. **Deposit the databank in the Drop Point.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files`
2. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse`
3. **Get inside the Maelstrom warehouse.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside`
   - Map pin: ref `#nid_06_warehouse`; position `-1343.6878662109, 2757.0773925781, 7.206298828125`
4. **Find the databank from the Malorian van.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive`
5. **Steal the databank.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take`

## Gig: Many Ways to Skin a Cat

- IGN walkthrough: [Many Ways to Skin a Cat](https://www.ign.com/wikis/cyberpunk-2077/Many_Ways_to_Skin_a_Cat)
- Vanilla type: `StreetStory`
- Quest hash: `1586516041`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`

### Journal premise

Gig type: Thievery\nObjective: Steal a Revere Courier Services van\nLocation: Revere Courier Services warehouse on Martin St\nDetails:\n\nThis isn't gonna be your usual gig. You're gonna go to the Revere Courier Services facility in Northside and steal a minibus full of leather jackets.\n\nDon't worry, I was also scratching my head at first. But the job itself couldn't be simpler.\n\nSomeone's smuggling syn-leather combat jackets to NC to get around the corporate embargo. The leather's imported in the form of jackets, which is then distributed to underground ripperdoc that use them for their implants, which are then sold at competitive prices. Quite a supply chain, right? My client tracked down the shipment but can't take care of it on her own. You're her replacement. Just remember that the RCS can't roll until it validates the driver's identity.\nOh and did I mention that the RCS warehouse is controlled by the Tyger Claws? No? Well I'm telling you now. They use it for laundering cash, so don't be surprised to see them prowling around.\nBe careful and good luck.

### Objective sequence

1. **Drive the van to the indicated location.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/convey`
   - Map pin: ref `#sts_wat_nid_02_marker_ending`; position `-1321.7359619141, 2320.951171875, 6.7658081054688`
   - Map pin: ref `#sts_wat_nid_02_marker_road`; position `-1382.4365234375, 2370.4487304688, 6.7819271087646`
2. **Find the van transporting syn-leather.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/find_the_van`
3. **Gain access to the van using the main computer.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_authorization`
4. **Enter the van.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_into`
5. **Do not kill civilians.**  
   `Optional` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/optional`
6. **Exit the van.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_out`
7. **Defeat or lose all enemies.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_out1`
8. **Collect your reward from the Drop Point.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_reward`
9. **(unnamed objective)**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/info`
10. **Go to the Revere Courier Services facility.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/inside`
11. **Steal the van transporting syn-leather.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/steal`

## Gig: MIA

- IGN walkthrough: [MIA](https://www.ign.com/wikis/cyberpunk-2077/MIA)
- Vanilla type: `StreetStory`
- Quest hash: `4040131205`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09`
- District: Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Find Benedict McAdams\nLocation: Clements St.\nDetails:\n\nA fixer's worth no more and no less than their last promise. And I promised Benedict McAdams I'd get him out of town once he checked off a job for me.\n\nBenedect's one devil of a pro. Just six hours in of taking the job and Councilman McClean's heart beat for the last time – that fat fish I'd had dangling on my line too long. The risk of a slip-up was high, so before he set to it, Benedict installed a GPS in his biomon so I could have an eye in the sky on him, as it were.\n\nThis slickster didn't work alone, mind you – had a driver, Jason Wildriver. The problem is, instead of hauling quick across the border, Jason went off route. Something here stinks worse than McClean's fishy corpse.\n\nFind them and bring me Benedict. I'll find him a new driver.

### Objective sequence

1. **Take Ben to a safe location.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/01_rescue_ben`
2. **Go to the abandoned farmhouse.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/02_go_to_protein_farms`
   - Map pin: ref `#ina_09_tr_mp_house`; position `-2926.5236816406, -4728.8901367188, 67.875534057617`
3. **Find Ben.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/find_ben`
   - Map pin: ref `#ina_09_tr_mp_house`; position `-2926.5236816406, -4728.8901367188, 67.875534057617`
4. **Find a key to the basement door.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/find_key`
   - Map pin: ref `#ina_09_tr_key_search`; position `-2929.15625, -4726.9682617188, 67.875244140625`
5. **Exit the car.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/leave_the_car`
6. **Take Ben to the meeting point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/take_ben_to_meeting_point`
   - Map pin: ref `#ina_09_tr_meeting_point_mp`; position `-2149.3515625, -5338.3969726563, 88.216323852539`
7. **Talk to Dakota's guy.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/talk_to_nomad`
8. **Talk to Ben.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/talk_with_ben`
9. **Wait for Dakota's guy.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09/sts_bls_ina_09/wait_for_dakota_man`
   - Map pin: ref `#ina_09_tr_meeting_point_mp`; position `-2149.3515625, -5338.3969726563, 88.216323852539`

## Gig: Monster Hunt

- IGN walkthrough: [Monster Hunt](https://www.ign.com/wikis/cyberpunk-2077/Monster_Hunt)
- Vanilla type: `StreetStory`
- Quest hash: `2576862732`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_07`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Jotaro Shobo (age 44, Japanese-American)\nLocation: Ho-Oh club on Allen St.\nDetails:\n\nFeel like doing everyone a favor and making eddies doing it? Deal with Jotaro Shobo. Twisted motherfucker like no other.\n\nHe's a Tyger Claw and a sadistic scumbag who's got a thing for scrolling XBDs. Who's to say whether he just gets carried away or (and my money's on this) he gets off on the tortured screams of his victims. Best guess is seventeen murders to his name, but the (in)justice for the street's dead and missing joytoys is notorious.\n\nBut the Moxes are different.\n\nMox netrunners connected a few dots and tracked down Jotaro's studio – Ho-Oh – quaint little club in Kabuki. This area's a no-go for Moxes which is why they need a helping hand.\n\nFind this fucker Jotaro and tell him his days in the entertainment biz are done.

### Objective sequence

1. **Carry Jotaro to the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/deliver_jotaro`
2. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/get_special_reward`
3. **Go to the Ho-Oh club.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/get_to_casino`
4. **Neutralize Jotaro.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/kill_jotaro`
5. **Leave the club.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/leave`
6. **Take Jotaro's body and leave the area.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/leave_with_body`
7. **Find Jotaro.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_07/sts_wat_kab_07/locate_jotaro`

## Gig: No Fixers

- IGN walkthrough: [No Fixers](https://www.ign.com/wikis/cyberpunk-2077/No_Fixers)
- Vanilla type: `StreetStory`
- Quest hash: `3324791973`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06`
- District: Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Iris Tanner\nLocation: Edgewood Ln.\nDetails:\n\nIris Tanner is the best tech specialist I've met in decades of living outside the city. Car broke down? Trouble with water filters? Ailing generator? Call Iris and give her five minutes with it.\n\nOne thing she's not great with though: People. Reading them, at least.\n\nFoolish girl started doing biz with the Wraiths. Making them angry is bad, sure, but making them happy is almost worse. Rather than just pay for a job well done, they kidnapped her instead. You ask why they'd kidnap someone who's capable of putting out an SOS from a rickety old radio? I – Dakota "Mad Coyote" Smith, eldest daughter of the Pomo tribe, eldest fixer in the Badlands – will offer my expert opinion: They're stupid.

### Objective sequence

1. **Go to the Wraiths' territory.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/01_get_to_outpost`
   - Map pin: ref `#ina_06_tr_camp_area_mp`; position `2129.3693847656, -1814.1729736328, 64.077209472656`
2. **Retrieve Iris's car.**  
   `Optional` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/opt_get_iris_car`
3. **Infiltrate the Wraiths' territory.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/02_get_inside_outpost`
   - Map pin: ref `#ina_06_tr_camp_area`; position `2129.3693847656, -1814.1729736328, 59.308242797852`
4. **Find out where Iris Tanner is being held.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/03_find_tanner`
   - Map pin: ref `#ina_06_tr_camp_area`; position `2129.3693847656, -1814.1729736328, 59.308242797852`
5. **Take Iris Tanner to Dakota.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/deliver_tanner_to_dakota`
6. **Find Iris Tanner.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/find_tanner`
   - Map pin: ref `#ina_06_tr_camp_area`; position `2129.3693847656, -1814.1729736328, 59.308242797852`
7. **Get rid of Iris' guard.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/kill_guard`
8. **Leave the shop.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/leave_area`
   - Map pin: ref `#ina_06_tr_leave_workshop_mappin`; position `2413.8212890625, -779.61901855469, 72.901901245117`
9. **Park Iris' car in the garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/park_car_in_garage`
   - Map pin: ref `#ina_06_tr_deliver_car_mp`; position `2421.0322265625, -772.3798828125, 66.210571289063`
10. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/pick_up_optional_reward`
11. **Save Iris Tanner.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/rescue_iris_tanner`
12. **Talk to Dakota.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/talk_dakota`
13. **Talk to Iris Tanner.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/talk_tanner`

## Gig: Occupational Hazard

- IGN walkthrough: [Occupational Hazard](https://www.ign.com/wikis/cyberpunk-2077/Occupational_Hazard)
- Vanilla type: `StreetStory`
- Quest hash: `2594602659`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `hack/breach/download`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nTarget: Hal Cantos\nLocation: Mox warehouse on Longshore North\nDetails:\n\nGot a call from a Hal Cantos – guy's a known quantity in the area, crack BD tuner, used to work for WNS news 'til he got axed for fraud. His biz is strictly street now. Like it even matters...\n\nHal's got himself in an interesting sich. He was tuning a BD for The Mox and must've fucked up, 'cause one of the girls went off the handle after she put on the wreath – started screaming and shooting at everything that moved. Hal managed to find a place to hide, but it's only a matter of time before she gets him. You're gonna make sure that doesn't happen.\n\nSending you the warehouse coordinates where Hal's holed up. Again, in case you missed it, there's an ACTIVE SHOOTER in the building. Go in with your iron at the ready. Eddies'll reach you only if Hal makes it out alive.

### Objective sequence

1. **Enter the Mox warehouse.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/enter`
2. **Find Hal Cantos.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/find`
3. **Neutralize the cyberpsycho.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/kill`
4. **Leave the Mox warehouse.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/leave`
5. **Save Hal Cantos.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/main`
6. **Talk to Hal Cantos.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/talk`
7. **Hack into the Moxes' subnet to weaken the cyberpsycho.**  
   `Optional` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/hack`

## Gig: Old Friends

- IGN walkthrough: [Old Friends](https://www.ign.com/wikis/cyberpunk-2077/Old_Friends)
- Vanilla type: `StreetStory`
- Quest hash: `2763272613`
- Quest path: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08`
- District: Heywood / Vista Del Rey
- Level: 60
- Candidate building blocks: `travel/reach location`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Karubo Bairei\nLocation: Dive bar on the corner of Congress and Pigeon st.\nDetails:\n\nThere's a time for forgiveness and a time for revenge. There's a time for turning the other cheek and a time for crushing your enemies like the roaches they are. In the words of the prophet Jeremiah: "Cursed is he who keeps their sword from bloodshed!"\n\nThe man you're to eliminate is Karubo Bairei. He's an old-timer, but don't let appearances fool you – he used to be a solo. He killed my friends – people who were like brothers and sisters to me. When all hell broke loose in Night City, he fled to the east coast. Now he's back, probably thinking everyone forgot about him. But not me.\n\nKarubo runs a filthy dive that serves as a Valentinos hangout. Go there and show him that nobody can avoid the hand of justice.\n\nAnd try not to make a scene, OK? Be professional – no unnecessary attention.

### Objective sequence

1. **Neutralize Karubo Bairei.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/eliminate_karubo_barei`
2. **Enter Karubo's bar.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/get_inside`
3. **Collect your reward from the Drop Point.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/go_to_drop_point`
4. **Leave the bar.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/leave_area`
5. **Carry Karubo's body outside.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/take_karubos_body_outside`
6. **Carry Karubo's body to the fixer's transport.**  
   `Optional` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/optional_disposal`
7. **Neutralize Karubo without raising the alarm.**  
   `Optional` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_08/sts_hey_rey_08/take_down_karubo_silently`

## Gig: Olive Branch

- IGN walkthrough: [Olive Branch](https://www.ign.com/wikis/cyberpunk-2077/Olive_Branch)
- Vanilla type: `StreetStory`
- Quest hash: `2269454619`
- Quest path: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01`
- District: Westbrook / Japantown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `interact/use device`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Special Delivery\nObjective: Meet with Sergei Karasinsky and deliver his gift to the designated address\nLocation: Garage on Redwood St.\nDetails:\n\nSergei Karasinsky called. He's a solo who, like my husband, acts before he thinks. It's a personal characteristic that always leads to the same thing sooner or later – trouble. Fortunately for us, Sergei is not only a man who acts without thinking but a panicked one at that. This means the pay is good and almost literally flying out of his account into ours.\n\nSergei is waiting for you at Silk Road. You will meet him there and pick up the peace offering he would like delivered to the Tyger Claws. He can't do this himself because he's recently been added to their blacklist.\n\nThe boy believes this small token will help the Tygers find forgiveness in their hearts for his terrible mistake.

### Objective sequence

1. **Defeat the Tyger Claws in the diner.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/defeat_tc`
2. **Free Alex.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/free_alex`
3. **Exit the vehicle.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/leave_car_gift`
4. **Leave the area.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/leave_diner`
5. **Look inside trunk.**  
   `Optional` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/check`
6. **Meet Sergei at the designated location.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/meet`
   - Map pin: ref `#jpn_01_tr_meet_sergei`; position `-565.68096923828, 689.38140869141, 34.54504776001`
7. **Open the trunk of Sergei's car.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/open_trunk`
8. **Park in the back of Tyger Claws' diner.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/park`
9. **Talk to the man in the trunk.**  
   `Optional` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/talk_bound`
10. **Drive Sergei's car to the Tyger Claws' restaurant.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/drive`
11. **Get in the car.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/get_inside`
   - Map pin: ref `#jpn_01_car_mappin`; position `-564.04699707031, 698.28717041016, 35.22452545166`
12. **Get into the garage.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/get_inside_garage`
   - Map pin: ref `#jpn_01_doors_garage`; position `-561.92803955078, 691.19641113281, 35.46354675293`
13. **Talk to the Tyger Claws leader.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/talk`
14. **Talk to Sergei Karasinsky.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/talk_sergei`
15. **Talk to the man in the trunk.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01/sts_wbr_jpn_01/talk_with_alex`

## Gig: On a Tight Leash

- IGN walkthrough: [On A Tight Leash](https://www.ign.com/wikis/cyberpunk-2077/On_A_Tight_Leash)
- Vanilla type: `StreetStory`
- Quest hash: `1087553175`
- Quest path: `quests/street_stories/heywood/wellsprings/sts_hey_spr_01`
- District: Heywood / Wellsprings
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Neutralize José Luis\nLocation: Bus Depot on Benko St.\nDetails:\n\nA few weeks ago a police officer was shot dead. Same old story – some Valentino kids got into a scrap with the badges. The fatal piece of lead was shot by a ganger named José Luis.\n\nThe investigation was dropped and officers from the local precinct were told to back off. Pretty interesting turn of events, wouldn't you say? José must have some friends in high places.\n\nHere's the deal – one of the officers wants José to be brought to justice, which is where you come in. If you happen to find out who's protecting the Valentino, I'll throw in extra. Good luck.

### Objective sequence

1. **Go to the bus depot.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/get_inside`
   - Map pin: ref `#spr_01_tr_enter`; position `-2075.7678222656, -974.58618164063, 7.3697929382324`
2. **Leave the depot.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/get_out`
   - Map pin: ref `#spr_01_tr_enter`; position `-2075.7678222656, -974.58618164063, 7.3697929382324`
3. **Collect your reward.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/get_reward`
4. **Carry José's body outside the depot.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/take_body`
   - Map pin: ref `#spr_01_tr_enter`; position `-2075.7678222656, -974.58618164063, 7.3697929382324`
5. **Carry José to the fixer's transport.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/take_to_fixer`
   - Map pin: ref `#spr_01_fixer_car`; position `-2120.17578125, -1036.2231445313, 8.1790065765381`
6. **Find out why the NCPD dropped the investigation.**  
   `Optional` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/find_out`
   - Map pin: ref `#spr_01_tr_enter`; position `-2075.7678222656, -974.58618164063, 7.3697929382324`
7. **Find José Luis.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/find_jose_luise`
   - Map pin: ref `#spr_01_tr_enter`; position `-2075.7678222656, -974.58618164063, 7.3697929382324`
8. **Call Padre.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/phone`
9. **Neutralize José Luis.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/take_down`
10. **Talk to Padre.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_01/sts_hey_spr_01/talk_padre`

## Gig: Playing for Keeps

- IGN walkthrough: [Playing For Keeps](https://www.ign.com/wikis/cyberpunk-2077/Playing_For_Keeps)
- Vanilla type: `StreetStory`
- Quest hash: `3322922762`
- Quest path: `quests/street_stories/watson/little_china/sts_wat_lch_05`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`

### Journal premise

Gig type: Search and Recover\nObjective: Jacob Lamb's implant\nLocation: Kashuu Hanten Bar, Clarendon St.\nDetails:\n\nGot a call from Jacob Lamb – friend of mine, director, from the good ol' days. Ex-director, I should say. Ever since Bushido X made a loss of a billion, the guy never set foot on a set again.\n\nJacob makes a living playing cards. One time he tried his luck at an illegal Tyger Claws casino at the back of the Kashuu Hanten eatery. Things weren't looking good, but instead of getting up from the table, he waited until he'd recoup. First went all his money, then his watch, wedding ring... And finally, one of his optics.\n\nJacob wants his implant back. Sending you the coordinates of the casino where he lost it. AFAIK, the eye's still there. How you get it is your biz, not mine.

### Objective sequence

1. **Deposit the implant in the Drop Point.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit`
2. **Wait for the bartender to bring the implant.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/find`
3. **Blackmail the bartender to give you the implant.**  
   `Optional` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/blackmaill`
4. **Go to the Kashuu Hanten bar in Little China.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/inside`
5. **Find the bar staff key.**  
   `Optional` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/card`
6. **Find Jacob Lamb's implant.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/main`
7. **Steal Jacob Lamb's eye.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/retrive`
8. **Take the optic implant from the storage room.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/take`

## Gig: Race to the Top

- IGN walkthrough: [Race To The Top](https://www.ign.com/wikis/cyberpunk-2077/Race_To_The_Top)
- Vanilla type: `StreetStory`
- Quest hash: `2537879880`
- Quest path: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal documents incriminating Matheus Stove\nLocation: Kendachi Factory, El Camino Rd\nDetails:\n\nYour mom ever tell you saying "two wrongs don't make a right"? Yeah, well we're the third one.\nKendachi's about to select a new director of some shit department or other – that part doesn't matter. What's important is it's two candidates for one gig. Know where this is going, right? Bingo – one of 'em is my client and he wants dirt on his new arch-nemesis Matheus Stove.\n\nMain problem is that Stove's the human equivalent of unseasoned, boiled scop. He's bland, he's boring. No bodies in his backyard, no dates with minors, nothing. But there's no way a guy in his position in a place like Night City is 100% dirt-free. I mean there's no fuckin' way.\n\nCouple contacts of mine say Stove has a few strings tied to the Valentinos. You need to slip into his office and slip a few files off his computer. If we're lucky, we get something to back up the rumors, costing Mr. Squeaky-clean Stove his shot at the promotion.

### Objective sequence

1. **Get inside Matheus' office.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/find_disk`
2. **Find incriminating data on Matheus.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_data`
3. **Enter the Kendachi factory area.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_ground`
4. **Get inside the Kendachi factory.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_inside`
5. **Leave the Kendachi factory area.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/leave_area`

## Gig: Radar Love

- IGN walkthrough: [Radar Love](https://www.ign.com/wikis/cyberpunk-2077/Radar_Love)
- Vanilla type: `StreetStory`
- Quest hash: `4101201868`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04`
- District: Badlands
- Level: 60
- Candidate building blocks: `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal mobile radar station, model P9D/2.161\nLocation: Militech base at Lone Star Motel\nDetails:\n\nThe Badlands are a fragile ecosystem where each piece has an important role to play. Change one thing and the whole circle of life starts to unwind. Militech doesn't seem to understand and set up a whole operation to cement the borders. They have a prototype mobile radar unit they use to track Aldecaldo transports currently moored at their latest outpost. We get our mitts on that, the Aldecaldos can reverse engineer themselves a jamming signal designed to beat the new Militech toy. Once those transports are invisible again, the ecosystem will be restored to balance.

### Objective sequence

1. **Deliver the P9D/2.161 radar to Dakota's garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/deliver_car`
   - Map pin: ref `#ina_04_tr_inside_workshop`; position `2420.9682617188, -771.017578125, 67.382690429688`
2. **Find the radar van P9D/2.161.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/find_the_mobile_radar`
   - Map pin: ref `#ina_04_tr_van_loc_smaller`; position `3627.625, -930.85931396484, 120.53125`
3. **Return to the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/get_back_to_van`
4. **Bring the mobile radar to Dakota.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/get_dakota_mobile_radar`
5. **Get out of the vehicle.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/get_out_of_the_van`
6. **Get inside the Militech base.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/go_to_motel`
   - Map pin: ref `#ina_04_tr_outpost_objective`; position `3639.2250976563, -924.74261474609, 120.50505828857`
7. **Leave the garage.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/leave_workshop`
   - Map pin: ref `#ina_04_tr_exit_garage_objective`; position `2423.5, -762.49993896484, 66.375`
8. **Defeat or lose all enemies.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/lose_chase`
   - Map pin: ref `#ina_04_tr_lose_chase`; position `2423.5, -766.5, 66.421875`
9. **Steal the mobile radar P9D/2.161.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/steal_the_van`

## Gig: Rite of Passage

- IGN walkthrough: [Rite of Passage](https://www.ign.com/wikis/cyberpunk-2077/Rite_of_Passage)
- Vanilla type: `StreetStory`
- Quest hash: `976194533`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `travel/reach location`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal a recording of Maelstrom's initiation rite\nLocation: Daniels St.\nDetails:\n\nGot some paparazzo work for ya. Need to get my hands on a recording of the Maelstrom initiation "ceremony." TLDR to get into the gang you need undergo an optic nerve split operation – a rite of passage, of sorts. Footage of the whole thing, that's what I'm paying for.\n\nGot a tip you can find just such a reel at the HeavenMed clinic – it's the place they put all the new recruits under the knife for the first time. Op rooms are all fitted with cams too. Could be a file, an entire disk, access to the servers – I don't care. What matters is that footage. Get it done.

### Objective sequence

1. **Escape from the clinic.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/escape_clinic`
2. **Go to the server room.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/find_recording`
3. **Go to the Maelstrom ripperdoc clinic.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/get_to_clinic`
4. **Steal the surgery recording.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/steal_recording`

## Gig: Scrolls before Swine

- IGN walkthrough: [Scrolls Before Swine](https://www.ign.com/wikis/cyberpunk-2077/Scrolls_Before_Swine)
- Vanilla type: `StreetStory`
- Quest hash: `666595724`
- Quest path: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07`
- District: Watson / Northside
- Level: 60
- Candidate building blocks: `search/investigate`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nTarget: CCTV footage\nLocation: Maelstrom warehouse on the corner of Industrial and Eisenhower St.\nDetails:\n\nClient is Aaron McCarlson, NCPD sergeant. Used to work for me as a consultant on the show "Cops 'n' Chops" (8 seasons!!) and is asking for a favor.\n\nAaron's been digging into Maelstrom for a while now – says he found the warehouse where they torture people. But you know how it is for badges – law slows them down with mountains of paperwork, so if they want to get something done, they have to get creative. Aaron knows that, which is why instead of waiting for fat-assed judges to grant him permission, he wants to get help from a "contractor."\n\nJob's simple. Get into warehouse (coordinates attached), steal the security cam footage and bring it back to Aaron. Should be enough to push his case through. And if you happen to shoot a few Maelstromers along the way, well... shit happens, right? World won't be worse off without them, that's for sure.

### Objective sequence

1. **Retrieve the footage from warehouse.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/decide_what_with_recording`
2. **Bring the footage to Aaron.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/deliver_recording`
3. **Find the computer with the footage.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/find_terminal`
4. **Get inside the warehouse.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/get_to_warehouse`
5. **Defeat Aaron.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/kill_aaron`
6. **Leave Aaron's building.**  
   `Primary` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/leave_building`
7. **Tell Aaron you know what he did.**  
   `Optional` · `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07/sts_wat_nid_07/confront_aaron`

## Gig: Serial Suicide

- IGN walkthrough: [Serial Suicide](https://www.ign.com/wikis/cyberpunk-2077/Serial_Suicide)
- Vanilla type: `StreetStory`
- Quest hash: `2457764693`
- Quest path: `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01`
- District: City Center / Corpo Plaza
- Level: 60
- Candidate building blocks: `travel/reach location`, `deliver/deposit item`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal CCTV footage\nLocation: Memorial Park Station\nDetails:\n\nSomething's rotten in the City of Dreams. A series of suicides, a rash of self-destruction. The contagion mostly targets politicians, corpos, journalists and police officers.\n\nThe latest victim was Zoli Barnes, a journalist who "fell" onto the tracks at Memorial Park station. Her death was officially ruled a suicide, but Barnes' parents say that she went to meet one her informants at the station and that she never would've taken her own life (I know, I know, that's what all parents say). Seems like the jury's still out – nobody really knows what happened because every last shred of CCTV footage was wiped clean. Her parents tracked down the witnesses, but they didn't want to talk and what's more – Militech took a keen interest in the whole thing.\n\nIt's our turn to make heads or tails of this. Head to the station, breach the servers and download any CCTV-related files. I'll have my code monkeys try to recover the deleted footage.\nP.S. Oh and by the way, at the time Zoli was working on a piece about Brad Noorwood – a Militech fanboy in the Night City Council.\n\nAnyway, looks that piece is never getting published.\nP.P.S. Transferring you Militech authorization that'll get you into the station.

### Objective sequence

1. **Steal the CCTV footage.**  
   `Primary` · `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data`
2. **Leave the station.**  
   `Primary` · `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape`
3. **Sneak into the station.**  
   `Primary` · `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building`
4. **Reach the main server room in the station.**  
   `Primary` · `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room`
5. **Acquire the data.**  
   `Primary` · `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/steal_recording`

## Gig: Serious Side Effects

- IGN walkthrough: [Serious Side Effects](https://www.ign.com/wikis/cyberpunk-2077/Serious_Side_Effects)
- Vanilla type: `StreetStory`
- Quest hash: `933834037`
- Quest path: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Search and Recover\nObjective: Retrieve a container containing beta acid\nLocation: Dewdrop Inn\nDetails:\n\nThis ain't too complicated, you know the drill. Something slipped through somebody's fingers and it's your job to get it back. Got this choom, Doug – Denver Doug – a ripper. Recently did this patch job on a 6th street dickhole and when he took off Denver noticed a gallon of beta acid gone missing. Dunno wtf he uses it for but that 6er knows all kinds of shit can get cooked from it on the street. 1+1 = a dealer klepped it.\n\nSo Denver hired a guy, Booker Updike, to find the missing acid, then POOF – he's a ghost. Last seen at the Dewdrop Inn in Arroyo. Head over there, get your hands on that beta, and if you got a minute, find out what happened to this Booker guy.

### Objective sequence

1. **Go to the room upstairs.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/after_investigation`
2. **Go to room 203.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/after_mail`
3. **Deposit the beta acid in the Drop Point.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/drop`
4. **Get out of the motel.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/escape`
5. **Look for the stolen beta acid in the lab.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/find_in_lab`
6. **Find the beta acid container.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/lab`
7. **Go to the Dewdrop Inn.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/motel`
8. **Go to room 103 and find out what happened to Booker.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/check_out_room`
9. **Retrieve the beta acid container.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/retrieve`
10. **Search room 103.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/investigation`
11. **Find Booker Updike.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/room`

## Gig: Severance Package

- IGN walkthrough: [Severance Package](https://www.ign.com/wikis/cyberpunk-2077/Severance_Package)
- Vanilla type: `StreetStory`
- Quest hash: `2663436901`
- Quest path: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Retrieve Rihanna Kumar's Cytech research\nLocation: Cytech Factory on Olivia St.\nDetails:\n\nRihanna Kumar used to be a top engineer at Cytech. Lived in a preem house, ate ganic meat, looked down on the poor – all the corpo basics. Then her little fairy tale took a twist. Cytech turned her world upside down. No more house, no more meat – but got new perspective on poverty from the other side of the fence. She's enlisted us to help her get a severance package.\n\nBreak into the Cytech factory and retrieve the data of the projects our poor, mistreated client was working on. With that, she can turn this personal shitstorm into a new dawn for her career (fuck... missed my calling as a poet). Anyway, most important thing is that she's paying us for the gig. Have fun.

### Objective sequence

1. **Deposit the data in the Drop Point.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/drop`
2. **Go to the factory.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/get_in`
   - Map pin: ref `#arr_10_tr_factory_inside`; position `-733.86053466797, -1408.314453125, 8.3100004196167`
3. **Do not kill civilians.**  
   `Optional` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/dont_kill`
4. **Contract type Retriving \n Goal Retrive data with years of work \n Location Cytech factory in Arroyo. \n  Details Rihanna Kumar was an engineer at the Cytech factory but they fired her.  After hours on one of the Cytech comps she conducted her own research on increasing the efficiency of Cytech implants.  She asked me to retrive this data from her computer in factory. It should be in the server room on the second floor. Try to not harm any of the workers - she pay's extra for taking things smooth and without unnecessary bloodshed. Good luck.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/get_inside_factory_ground`
   - Map pin: ref `#arr_10_tr_enter`; position `-706.48449707031, -1386.7216796875, 7.8200001716614`
5. **Leave the factory.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/leave`
   - Map pin: ref `#arr_10_component_marker`; position `-704.44866943359, -1379.7397460938, 9.3463401794434`
6. **Retrieve Rihanna's data files.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/recover_data`
7. **Get to the second floor.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/second_floor`
   - Map pin: ref `#arr_10_second_floor`; position `-751.6025390625, -1431.2816162109, 15.340000152588`
8. **Transfer Data**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/send_data_to_fixer`
9. **Get to the server room.**  
   `Primary` · `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/server_room`
   - Map pin: ref `#arr_10_tr_server`; position `-745.73004150391, -1441.5001220703, 13.85000038147`

## Gig: Shark in the Water

- IGN walkthrough: [Shark in the Water](https://www.ign.com/wikis/cyberpunk-2077/Shark_in_the_Water)
- Vanilla type: `StreetStory`
- Quest hash: `1419368268`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_06`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Blake Croyle\nLocation: Aoba on O'Malley Place St.\nDetails:\n\nRacketeering's the name of the game in Kabuki. The badges pretend like they don't see when hustlers like Blake reel in the next victim.\n\nThe script's always the same. Act I – a promising money deal. Act II – an unpayable debt. The sucker this time was Roger Wang, store chain owner. Blake's already seized ownership of one of the stores but has bigger plans. Like I said, this kind of debt's unpayable, so Wang got wise and paid us instead. This human shitstain Croyle is about to disappear, so the time to act is now.\n\nAnd one more thing – Blake's got huscle from the Animals watching his back.

### Objective sequence

1. **Put Blake in the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/drop_trenton_body`
2. **Find Blake.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/find_target`
3. **Go to the store seized by Blake.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/go_to_shop`
4. **Neutralize Blake.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/kill_or_subdue`
5. **Leave**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/leave_area`
6. **Carry Blake to the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/leave_area_with_body`

## Gig: Small Man, Big Evil

- IGN walkthrough: [Small Man, Big Evil](https://www.ign.com/wikis/cyberpunk-2077/Small_Man,_Big_Evil)
- Vanilla type: `StreetStory`
- Quest hash: `3711325308`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_101`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Jae-Hyun\nLocation: Rooftop slums near Allen St.\nDetails:\n\nCountless dreamers head to big cities in search of a fresh start. And so many of them have nowhere to return to. Outcasts, loners, rejects. Jae-Hyun's put a targets on the backs of those society's failed. And there's no shortage of them in Night City.\n\nHere's the rundown on Jae-Hyun's meat grinder: he identifies some poor bastard, kidnaps them, and delivers them to scavs for biomon or other cyberware removal. They're stripped of their identities and end up the "property" of some shitbag like Jotaro to do with as they please.\n\nCourse no one really looks for these people. And even if they did where would they start? What are the odds? To find someone in Night City who doesn't exist?\n\nLet's face it – Jae-Hyun is just one head of the hydra, but fuck it – let's chop it off anyway. Could be a good while before more grow back in his place.

### Objective sequence

1. **Carry the body to the fixer's vehicle.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/drop_body`
2. **Find Jae-Hyun in the restricted part of the slums.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/find_target`
3. **Go to the slums.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/get_to_area`
4. **Neutralize Jae-Hyun.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/kill_target`
5. **Leave**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/leave_area`
6. **Pick up Jae-Hyun and leave the area.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/transport_jae_hyun_body`

## Gig: Sparring Partner

- IGN walkthrough: [Sparring Partner](https://www.ign.com/wikis/cyberpunk-2077/Sparring_Partner)
- Vanilla type: `StreetStory`
- Quest hash: `3878698230`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11`
- District: Badlands
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`

### Journal premise

Gig type: Thievery\nObject: Retrieve data from broken training bot\nLocation: Warbler Lake Hazardous Waste Facility, Anderson St.\nDetails:\n\nThere's this kid – folks call him Joe. Red Joe. Now, this Joe kid has talent, knows his hooks and jabs. I swear he could knock a horse's teeth out. Point is, kid's got what it takes to go pro. Problem is, coaches aren't easy to come by in the Badlands. But lo and behold! Word is a next-gen sparring bot's landed in a scrapyard there – still in working order. That's city folk for ya – second a piece of tech glitches, it gets tossed out in the trash. Soft included.\n\nAnyway, back to the bot. Find it and download its software before they recycle it into metal straws or whatever it is NC people like.\n\nP.S. Oh and one more thing – the guy that runs the landfill? Watch out for him. Real piece of work.

### Objective sequence

1. **Get your hands on training software.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/00_boxing_robot_shard`
2. **Collect the additional reward from the Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/collect_reward`
3. **Deposit the shard in the Drop Point.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/deliver_chip`
4. **Pull the shard from the bot.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/extract_data`
5. **Establish the broken bot's location.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/find_data_on_robot_location`
6. **Find the broken bot.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/find_robot`
   - Map pin: ref `#ina_11_tr_landfill_mp`; position `1393.8427734375, -1684.4211425781, 49.22021484375`
7. **Contract type- Retrieval \n Goal- retrieve disk from training robot's head \n Location- Municipal Landfill in Badlands \n Details- There is a damaged robot which has been used by NC Bonecrushers (best boxing team in NC) dumped somewhere on a Landfil. I have a client who is very interested in robots hard drive which still contains data about their training routines. You can just buy the robot of the Vendor, or try to find it on your own... Data on it's location should be on the main compuer in the office. Check Landfill registry to locate Jackson Inc containers - from my intel this company took robot for recycling from Bonecrushers. Than deliver the disk to the drop box.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/get_to_landfill`
8. **Go to the broken bot's location.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/go_to_robot`
9. **Wait for the bot.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/wait_for_robot`
   - Map pin: ref `#ina_11_tr_wait_for_robot_mp`; position `1378.6577148438, -1676.775390625, 49.202262878418`

## Gig: Sr. Ladrillo's Private Collection

- IGN walkthrough: [Sr Ladrillo's Private Collection](https://www.ign.com/wikis/cyberpunk-2077/Sr_Ladrillo%27s_Private_Collection)
- Vanilla type: `StreetStory`
- Quest hash: `3578660365`
- Quest path: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02`
- District: Heywood / Vista Del Rey
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal data from a computer\nLocation: Dicky Twister, corner of Congress and Pajaro St.\nDetails:\n\nSaint Augustine once wrote: When one has a healthy sense of smell, he will immediately recognize the stench of sin. Well, even anyone with a sinus infection in this city can smell the fuckfests over at Dicky Twister. This gay strip club is full of chicos with glazed, dead eyes who will do anything you desire for an extra eddie tucked into their thongs.\n\nThe stench coming from that place finally wafted into NCPD command. My little rats tell me they plan to kick down the door any day now. That's bad news. The owner of Dicky Twister, a pimp called Sr. Ladrillo, is no gonk – and a fanatic for recordkeeping. He has a computer full of data thanks to spying tech in his VIP rooms. We're talking politicians, suits, crime bosses, celebrities (maybe even the cops themselves)... If the boys in blue get their hands on these recordings, Ladrillo's geniusly built house of cards collapses, leaving the whole district in chaos. And chaos isn't in our best interest at the moment.\n\nKlep those recordings at the Dicky Twister before the cops do. Thankfully, the Lord has blessed us – Ladrillo is currently out of town. But better to make haste, for ignoring divine assistance is a sin in its own right.

### Objective sequence

1. **Deposit the compromising material in the Drop Point.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/drop`
2. **Get out of Dicky Twister.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape`
3. **Get to Sr. Ladrillo's office.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room`
4. **Go to Dicky Twister.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club`
5. **Steal the compromising material from within Dicky Twister.**  
   `Primary` · `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad`

## Gig: The Frolics of Councilwoman Cole

- IGN walkthrough: [The Frolics of Councilwoman Cole](https://www.ign.com/wikis/cyberpunk-2077/The_Frolics_of_Councilwoman_Cole)
- Vanilla type: `StreetStory`
- Quest hash: `4125561827`
- Quest path: `quests/street_stories/city_center/downtown/sts_cct_dtn_05`
- District: City Center / Downtown
- Level: 60
- Candidate building blocks: `travel/reach location`, `hack/breach/download`, `retrieve/collect item`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal recordings of Eva Cole\nLocation: Marina, Cannery Row\nDetails:\n\nSo there's this Councilwoman, Eva Cole. By day, she's a living nightmare for greedy corpos, pointin' the finger on abuse, digging up problematic witnesses, dishin' out fees and penalties and whatever. And by night – she fucks. Like a fuckin' cat in heat, with whoever lands on the deck of her yacht docked down at the marina. I'd act more surprised, but I ain't – I mean you gotta let out all that stress somehow, right? So anyway, one of these corpos that got its toes stomped on wants footage of these wet-n-wild orgy fuckfests. They got in mind a joint screening with the councilwoman will help her see the light of a more... pro-business attitude.\n\nI send you the yacht name and coords, you fetch the footage. Oh... and I wouldn't sit on any of the furniture if I was you.\n\nOne last thing – there's more €$ to be made if you do this on the quiet.

### Objective sequence

1. **Escape the docks.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks`
2. **Remain undetected.**  
   `Optional` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth`
3. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward`
4. **Get inside the docks' security room.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room`
5. **Go to the docks.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks`
6. **Recording**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/main`
7. **Download the incriminating recordings and send them to the fixer.**  
   `Primary` · `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc`

## Gig: The Heisenberg Principle

- IGN walkthrough: [The Heisenberg Principle](https://www.ign.com/wikis/cyberpunk-2077/The_Heisenberg_Principle)
- Vanilla type: `StreetStory`
- Quest hash: `4009599336`
- Quest path: `quests/street_stories/watson/little_china/sts_wat_lch_06`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Destroy the glitter lab\nLocation: Building on Rovinj St.\nDetails\n\nUnless you've been living under a rock, you've heard of Glitter. Word is that if you take it, you're hooked for life, but apparently it's easier to OD on than neo-fentanyl.\n\nIt was only a matter of time before some zit-faced, rich kid fried his skull sponge. Kid's mother was Arati Kapoor, co-owner of the Masala Studios restaurant franchise. Needless to say, she's pretty torn up about it, but she's not the kind to wallow in her grief – she's got a plan.\n\nThe lab where glitter is cooked has to be wiped off the face of the earth. And if some of those dipshits making it expire on the spot? I think you know the answer.\n\nFlicking you the coords now. FYI – the place might be guarded by Tyger Claws.

### Objective sequence

1. **Destroy the equipment used to make glitter.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line`
2. **Enter the basement.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement`
3. **Enter the building.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building`
4. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out`
5. **Find the lab.**  
   `Primary` · `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room`

## Gig: The Lord Giveth and Taketh Away

- IGN walkthrough: [The Lord Giveth and Taketh Away](https://www.ign.com/wikis/cyberpunk-2077/The_Lord_Giveth_and_Taketh_Away)
- Vanilla type: `StreetStory`
- Quest hash: `1585827533`
- Quest path: `quests/street_stories/heywood/wellsprings/sts_hey_spr_03`
- District: Heywood / Wellsprings
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Search and Recover\nObjective: Retrieve the Militech car purchased by the nomads\nLocation: Garage on Russell St.\nDetails:\n\nA group of nomads decided to run some sidebiz in Night City and bought a stolen Militech SUV from the Valentinos. This happened on my turf, but unfortunately they "forgot" to ask me for help because they didn't want to cut in a fixer. The Valentinos took the eddies, slammed their heads against the pavement and told them to fuck off.\n\nThe nomads just want to get what they paid for – the right way this time, through a fixer. Their rep Dakota called me and I promised her I would help. The SUV ended up in a Valentinos garage in Wellsprings. You need to get it back.\n\nGetting back at the Valentinos isn't part of the gig – you let me handle it.

### Objective sequence

1. **Deliver the SUV to the nomads.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/convey`
   - Map pin: ref `#sts_hey_spr_03_marker_ending`; position `-1991.1284179688, -1272.7352294922, 14.445406913757`
   - Map pin: ref `#sts_hey_spr_03_marker_road`; position `-1961.1247558594, -1233.6252441406, 10.466796875`
2. **Defeat or lose all enemies.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/convey1`
3. **Escape with the SUV.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/escape`
4. **Exit the garage.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/exit_the_garage`
5. **Enter the SUV.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/get_into`
6. **Go back to the SUV.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/go_back_to_car`
7. **Park the SUV in the garage.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/leave`
8. **Leave the area.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/leave_area`
9. **Find the SUV.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/nomad`
10. **Meet with the nomads.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/talk`
11. **Go to the Valentinos' auto shop.**  
   `Primary` · `quests/street_stories/heywood/wellsprings/sts_hey_spr_03/sts_hey_spr_03/workshop`

## Gig: The Union Strikes Back

- IGN walkthrough: [The Union Strikes Back](https://www.ign.com/wikis/cyberpunk-2077/The_Union_Strikes_Back)
- Vanilla type: `StreetStory`
- Quest hash: `577624120`
- Quest path: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01`
- District: Santo Domingo / Rancho Coronado
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Vic Vega\nLocation: Carsten St, Rancho Coronado\nDetails:\n\nAt first I thought it was just rumors and the kind of drunken bullshit you hear at a bar at 3 AM, y'know? But when you hear the same story from three separate witnesses, you start taking an interest. Now that my informant confirmed the accounts, it's time to dive into the action.\n\nLook, I don't wanna sound like some naggy old crone, but back in my day workers knew how to stand up for themselves. Instead of fixers they had unions to fight for their rights. I know, I know. Anyway, now with the unions gone, these workers can't afford to hire fixers on starvation-level salaries. Lucky for them, I like to do some pro bono work from time to time. You know, a little something for the public good.\n\nOnto the fine detes. Vic Vega – the kind of scum who writes "cracking skulls" in the hobby section of his CV. Well, that's exactly what he's doing in Rancho Coronado. Cracking skulls. Not only that, but he's got the full backing of the corp execs, who'd rather give their workers brain damage instead of a 2% raise.\n\nVega and his people've been terrorizing the whole neighborhood. Workers've had enough – who the fuck wouldn't agree? You're gonna find Vic Vega and end that psycho for good. Maybe then the corpos'll realize they crossed the line.

### Objective sequence

1. **Put Vic Vega in the fixer's transport.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/car`
2. **Do not let any civilians get hurt.**  
   `Optional` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/dont_kill_any_civilians`
3. **Collect your bonus.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/collect_reward`
4. **Get inside C-Team's building.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/enter_the_facility`
5. **Leave the building.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/escape`
6. **Find Vic Vega.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/find_vega`
7. **Enter Vic Vega's office.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/get_to_the_office`
8. **Neutralize Vic Vega.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/kill_mad_dog1`
9. **Take Vic Vega's body to the designated location.**  
   `Primary` · `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_01/sts_std_rcr_01/leave_area_with_body`

## Gig: Trevor's Last Ride

- IGN walkthrough: [Trevor's Last Ride](https://www.ign.com/wikis/cyberpunk-2077/Trevor%27s_Last_Ride)
- Vanilla type: `StreetStory`
- Quest hash: `3071127012`
- Quest path: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08`
- District: Badlands
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Find Trevor's remains and deliver them to his family\nLocation: Highway 101\nDetails:\n\nThere's a popular saying among the Aldecaldos: "she who lives in the hearts of her loved ones can never truly die." Trevor Brass might indeed live on in memory, but if he had just keep his butt planted instead of dealing with Wraiths he'd still be just plain alive.\nI digress. Yesterday, man of mine spotted Trevor's car at a Wraiths' nest. The car had more holes than it started with and the Wraiths aren't known for taking prisoners.\nTrevor's relatives, as I mentioned, belong to the Aldecaldos. They aren't out for revenge. They just want to bury their son.\n\nFind Trevor's remains and help his family find peace.

### Objective sequence

1. **Retrieve Trevor's body.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back`
2. **Go to the Wraiths' territory.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp`
   - Map pin: ref `#ina_08_mp`; position `-1378.9855957031, -3643.5920410156, 55.30078125`
3. **Find Trevor's body.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body`
   - Map pin: ref `#ina_08_tr_find_body`; position `-1412.9704589844, -3644.5986328125, 55.216835021973`
4. **Scan the bodies to find Trevor.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor`
   - Map pin: ref `#ina_08_tr_in_freezer`; position `-1420.5793457031, -3640.3293457031, 54.676490783691`
5. **Wait for the pickup.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/05a_wait_for_pickup`
   - Map pin: ref `#ina_08_tr_pickup_area`; position `-1350.9066162109, -3697.8056640625, 55.000003814697`
6. **Place Trevor's body in the trunk.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk`
7. **Retrieve the body from the Wraith outpost.**  
   `Primary` · `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location`
   - Map pin: ref `#ina_08_get_out_mp`; position `-1376.9083251953, -3645.4641113281, 55.990272521973`

## Gig: Troublesome Neighbors

- IGN walkthrough: [Troublesome Neighbors](https://www.ign.com/wikis/cyberpunk-2077/Troublesome_Neighbors)
- Vanilla type: `StreetStory`
- Quest hash: `3058147867`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_107`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nTarget: Taki Kenmochi\nLocation: Residence building at Cortes and Kennedy St.\nDetails:\n\nI got a place at this block in Kabuki. Not many know about it (welcome to the club) and I prefer to keep it that way. Problem is a certain Tyger Cunt (and friends) set up a pachinko operation right on my fucking doorstep. Could mean trouble for me down the road.\n\nLemme guess – you're thinking it's better to hide in plain sight? Yeah, fuck that. When (not if) the NCPD cracks down on those pachinko machines, I know they're gonna poke their ugly pig noses around in my backyard. Can't risk them seeing something they shouldn't.\n\nWe can't sit on this. Head to the residential block where a Tyger by name of Taki Kenmochi is running this pachinko show. Deal with her. Any other Tygers in the area will get the message and peace out quick.

### Objective sequence

1. **Carry Taki Kenmochi to the fixer's transport.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/deliver`
2. **Locate Taki Kenmochi.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/find_target`
3. **Approach the pachinko machines.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/get_in`
4. **Move away from the pachinko machines.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/get_out`
5. **Pick up Taki Kenmochi and leave the area.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/pick_up_unconscious_target`
6. **Neutralize Taki Kenmochi.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/take_down`

## Gig: Two Wrongs Makes Us Right

- IGN walkthrough: [Two Wrongs Makes Us Right](https://www.ign.com/wikis/cyberpunk-2077/Two_Wrongs_Makes_Us_Right)
- Vanilla type: `StreetStory`
- Quest hash: `435741885`
- Quest path: `quests/street_stories/pacifica/coastview/sts_pac_cvi_02`
- District: Pacifica / Coastview
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal a van hauling the Animals' medical supplies\nLocation: Baptiste St.\nDetails:\n\nHere's the situation, you need to enter an Animal den steal a certain van carrying medical stimulants. A modified lidocaine, to be precise.\n\nKeep in mind the cargo is rather hot – stolen already once before from Maelstrom.\n\nThose metalmongers use the lidocaine for initation rites, whereas the intend to use it as an ingredient in their favorite "juice" cocktail. In my line of work, we call this a market shortage. What do you say we up the demand even more?\n\nStep 1 - you steal the van. Step 2 – I resell the lidocaine to ripperdoc., Step 3 – they sell it at market price. Step 4 – profit.

### Objective sequence

1. **Park the van in the small lot near the mall in Pacifica.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/convey_truck`
2. **Defeat or lose all enemies.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/deliver_chased`
3. **Escape by van from the NCART station.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/escape_by_van`
4. **Find the van in the NCART tunnels.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/find_truck`
5. **Exit the van.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_out`
6. **Get to the unfinished NCART station.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_metro_station`
7. **Get to the van.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_the_van`
8. **Steal the van.**  
   `Primary` · `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/steal`

## Gig: Tyger and Vulture

- IGN walkthrough: [Tyger and Vulture](https://www.ign.com/wikis/cyberpunk-2077/Tyger_and_Vulture)
- Vanilla type: `StreetStory`
- Quest hash: `277336735`
- Quest path: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07`
- District: Westbrook / Charter Hill
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`

### Journal premise

Gig type: Thievery\nObjective: Steal Vortex's credchip\nLocation: Tyger Claws' casino on Longshore South\nDetails:\n\nThe vulture is the wisest bird. While others lose strength in the pursuit of prey, the vulture waits patiently – it only spreads its wings when it smells blood on the air.\n\nYou will be my vulture, V. I heard a Tyger Claws casino has been robbed by one of their own – a dealer. The girl had an alias, Vortex, and she managed the casino's machines. She programmed them to skim a small percentage so a drop from each win landed in her bucket. It took years for the Tygers to realize how they were being cheated. You can imagine they were not pleased. But their ferocity extended too far. Vortex died during the interrogation before revealing where she stored the stolen money. A vulture is wiser than a Tyger, V. You will find it.\n\nI will send you the Vortex's last known location. Don't let me down.

### Objective sequence

1. **Take Vortex's credchip.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer`
2. **Deposit Vortex's credchip in the Drop Point.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet`
3. **Enter the casino.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in`
4. **Search the casino office.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers`
5. **Find Vortex's credchip.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den`
6. **Find the office on the second floor.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan`

## Gig: Until Death Do Us Part

- IGN walkthrough: [Until Death Do Us Part](https://www.ign.com/wikis/cyberpunk-2077/Until_Death_Do_Us_Part)
- Vanilla type: `StreetStory`
- Quest hash: `885903102`
- Quest path: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01`
- District: Westbrook / Charter Hill
- Level: 60
- Candidate building blocks: `travel/reach location`, `wait/time gate`, `search/investigate`, `deliver/deposit item`, `stealth/avoid detection`, `leave/escape area`

### Journal premise

Gig type: Thievery\nObjective: Steal the shard with Emilio Gutierrez's depository receipts\nLocation: Apartment on Palm St.\nDetails:\n\nWould you like to hear about my fourth husband? He was very lazy, gullible, and filthy rich. I divorced him as quickly as I could and never made so much money in such a short time. With that said, can I really blame Mrs. Gutierrez for stripping Mr. Gutierrez down to the last enny? Of course not. In fact, I'd like to meet her lawyers.\n\nBut enough about Mrs. Gutierrez. Our client happens to be the injured party, Mr. Gutierrez. He lost his car and luxury penthouse, now the poor fool has barely anything to live in because he left his depository receipts in their old apartment (the locks are already changed). You'll have to retrieve them, because our new divorcee isn't going to give them back out of the kindness of her heart.\n\nThe penthouse is on the last floor of the building. Don't worry, I'm providing you with elevator access.\n\nFor obvious reasons, Mr. Gutierrez is counting on your utmost discretion. If things go quietly, he'll toss in extra.

### Objective sequence

1. **Deposit the shard in the Drop Point.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point`
2. **Escape the building.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape`
   - Map pin: ref `#hil_01_marker_001`; position `-10.579804420471, 26.870666503906, 14.842537879944`
3. **Find Gutierrez's office.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find`
4. **Go to the apartment on Palm Street.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment`
5. **Go to the top floor.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor`
   - Map pin: ref `$/03_night_city/c_westbrook/charter_hill/loc_sts_wbr_hil_01_prefabMXY3ZIA/loc_sts_wbr_hil_01_gameplay_prefabE5PRUQQ/loc_sts_wbr_hil_01_devices_prefabTAW7YJY/lift_2_floors_prefabSI7AFCY/marker_1`; position `14.212005615234, 19.140552520752, 15.361577033997`
   - Map pin: ref `#hil_01_marker_002`; position `11.464663505554, 20.978260040283, 136.81781005859`
6. **Steal the shard with the depository receipts.**  
   `Primary` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps`
7. **Remain undetected.**  
   `Optional` · `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen`

## Gig: Wakako's Favorite

- IGN walkthrough: [Wakako's Favorite](https://www.ign.com/wikis/cyberpunk-2077/Wakako%27s_Favorite)
- Vanilla type: `StreetStory`
- Quest hash: `299087042`
- Quest path: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05`
- District: Westbrook / Japantown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Locate netrunner Chang-Hoon Nam, 67 years old, regular associate\nLocation: Restaurant on Crescent St.\nDetails:\n\nFor years, I worked to get jobs done comfortably, with a crew I hand-picked myself. I chose Chang-Hoon Nam years ago, and he hasn't let me down once. I don't know what happened to him, but you got to get him back. Check the basement in that Chinese place. He keeps his gear there, sometimes takes a side gig or two. Think he's still alive – if he weren't, he's the type who'd come back as a ghost and apologize, just like in those tales from the old country that make me want to puke. He's sentimental like that.

### Objective sequence

1. **Find a way to Chang-Hoon Nam's hideout.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/door`
2. **Escape with Chang-Hoon Nam.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/escape`
3. **Find out what happened to Chang-Hoon Nam.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/find_what_happend`
4. **Find out what happened to Chang-Hoon Nam.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/investigate`
5. **Leave the area.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/leave_the_area`
6. **Follow the lights**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/lights`
7. **Slot the shard in Chang-Hoon Nam's neural port.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/put_in`
8. **Find the shard for stabilizing Chang-Hoon Nam's condition.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/shard`
9. **Take the shard.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/take_shard`
10. **Talk to Chang-Hoon Nam.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/talk1`
11. **Find Chang-Hoon Nam**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05/sts_wbr_jpn_05/way`

## Gig: We Have Your Wife

- IGN walkthrough: [We Have Your Wife](https://www.ign.com/wikis/cyberpunk-2077/We_Have_Your_Wife)
- Vanilla type: `StreetStory`
- Quest hash: `1989354122`
- Quest path: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02`
- District: Westbrook / Japantown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `vehicle sequence`

### Journal premise

Gig type: SOS: Merc Needed\nObjective: Rescue Lauren Costigan from the Tyger Claws\nLocation: Building by Raymond St.\nDetails:\n\nOld sins cast long shadows. And Bradley Costigan is guilty of many. As a result, he not only found himself in prison, but also invited trouble into the life of his wife, Lauren Costigan. It's your task to help her.\n\nWhen Bradley landed a spot behind bars, he was contacted by old acquaintances in the Tyger Claws. Shiv some snitches, they said. He said no.\n\nTygers don't like that word. They kidnapped his wife and sent stills as proof. No great surprise, Bradley began to cooperate. But he also remembered me. He's promised payment and I believe he's desperate enough to be good for it.\n\nMy people have already tracked where the stills were taken. Once you have the coordinates, set to work immediately.

### Objective sequence

1. **Escort Lauren out of the building.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/escape_workshop_with_bill`
   - Map pin: ref `#jpn_02_tr_escort_finish_001`; position `-272.01391601563, 1618.7041015625, 41.407611846924`
2. **Reach Lauren Costigan's cell.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/find_way_inside`
   - Map pin: ref `#jpn_02_tr_meeting_lauren`; position `-268.2317199707, 1629.9688720703, 33.200397491455`
3. **Get inside the workshop.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/get_inside`
   - Map pin: ref `#jpn_02_tr_escort_finish_001`; position `-272.01391601563, 1618.7041015625, 41.407611846924`
4. **Find Lauren Costigan.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/get_to_the_basement`
   - Map pin: ref `#jpn_02_tr_basement_001`; position `-253.51965332031, 1642.6341552734, 33.117454528809`
5. **Rescue Lauren Costigan.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/rescue_bill1`
6. **Talk to Lauren.**  
   `Primary` · `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/tell_lauren_to_get_to_car`

## Gig: Welcome to America, Comrade

- IGN walkthrough: [Welcome to America, Comrade](https://www.ign.com/wikis/cyberpunk-2077/Welcome_to_America,_Comrade)
- Vanilla type: `StreetStory`
- Quest hash: `369018367`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_102`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `travel/reach location`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

Gig type: Agent Saboteur\nObjective: Place GPS tracker on Mikhail Akulov's car\nLocation: Kabuki port\nDetails:\nWhen a top Soviet fixer, Mikhail Akulov, landed in NC, it generated a lot of buzz in the biz. So far, says he's just in town to cut a small-time deal. The USSR's premier fixer in town to personally handle minor league gigs at enny stakes? Yeah, can't say I'm convinced either\nSo what's his game? Why Night City? My client needs answers to these questions and more. They want to follow his every step on NC soil and that's why you need to plant a GPS transmitter on our dear comrade's car. And keep it clean and quiet.

### Objective sequence

1. **Find the container with the vehicle.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/find_cargo_with_car`
2. **Collect your bonus from the Drop Point.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/get_special_reward`
3. **Remain undetected.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/stealth`
4. **Go to the docks in Kabuki.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/get_to_docks`
5. **Leave the docks.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/leave_docks`
6. **Plant the GPS tracker on the vehicle.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/plant_tracker`

## Gig: Woman of La Mancha

- IGN walkthrough: [Woman of La Mancha](https://www.ign.com/wikis/cyberpunk-2077/Woman_of_La_Mancha)
- Vanilla type: `StreetStory`
- Quest hash: `36580749`
- Quest path: `quests/street_stories/watson/kabuki/sts_wat_kab_08`
- District: Watson / Kabuki
- Level: 60
- Candidate building blocks: `search/investigate`, `hack/breach/download`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Gig type: Gun for Hire\nObjective: Force Anna Hamill to drop her police investigation\nLocation: Kabuki market\nDetails:\n\nAnna Hamill is a blue-blooded cop, through and through. The kind you'd expect to see in some NCPD promo. Beautiful, smart, honest to a fault. In other words, a really bad fit for Night City.\n\nHer NCPD colleagues are another story. They all have back problems from sitting on fat wallets.\n\nThis current case Hamill's working has them all breaking out in hives. She's digging into the smuggling racket in Kabuki market, which – if she makes any real headway – means bad biz for her cop buddies' finances. They want someone from outside the precinct to nip this thing in the bud.\n\nNormally that's where I'd leave it, but I wanna add one more thing. I kinda feel bad for the girl. Rather she not flatline if you can avoid it. Convince her to skip town, or drop the case and make a career change at least.

### Objective sequence

1. **Confront Anna Hamill.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/confront_dave`
2. **Carry Anna Hamill to the fixer's car.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/deliver_body_to_fixer_car`
3. **Upload the program to the marketplace network.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/check_cameras`
4. **Find Anna Hamill.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/find_anna`
5. **Neutralize Anna Hamill.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/kill_dave`
6. **Leave the area.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/leave_area`
7. **Typ kontraktu: Neutralizacja\nCel: Zmuś Annę Hammil do przerwania śledztwa\nLokalizacja: okolice bazarau Kabuki\nSzczegóły:\n\n\nAnna Hammil, to policjantka jakby wyjęta z filmu promującego Akademię Policyjną. Piękna, mądra i niezwykle uczciwa. Mówiąc inaczej, nie nadaje się do pracy w Night City.\n\n\nCo innego jej koledzy z NPCD. Oni od siedzenia na grubych portfelach dostali skrzywienia kręgosłupa. Tego moralnego.\n\n\nTeraz boli ich, że Anna prowadzi śledztwo w sprawie nielegalnego obrotu wszczepami na bazarze w Kabuki. Wynik  śledztwa mógłby źle wpłynąć na ich finanse, dlatego chcą by Anna je przerwała.\n\n\nPowiem tak. Normalnie nie zleciłabym ci tej roboty, ale po prostu szkoda mi tej dziewczyny. Spróbuj ją przekonać, żeby rzuciła ten syf i zmieniła towarzystwo.**  
   `Optional` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/talk_with_shopkeepers`
8. **Carry Anna Hamill out of the bazaar.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/take_body_outside`
9. **Confront Anna Hamill.**  
   `Primary` · `quests/street_stories/watson/kabuki/sts_wat_kab_08/sts_wat_kab_08/talk_with_dave1`
