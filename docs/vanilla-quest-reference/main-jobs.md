# Cyberpunk 2077 Main Jobs

Source index: [IGN — Main Jobs](https://www.ign.com/wikis/cyberpunk-2077/Walkthrough_-_Main_Jobs)

This is a structural reference derived from IGN's walkthrough index and
the local [`quest.json`](../../../quest.json) journal export. It summarizes
vanilla quest objectives and links to IGN; it does not reproduce IGN's
walkthrough prose.

Matched quests: **57**

## Quick index

| Quest | Vanilla type | Quest path | Building blocks |
|---|---|---|---|
| [(Don't Fear) The Reaper](#dont-fear-the-reaper) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/How_to_Get_the_Secret_Ending)) | MainQuest | `quests/meta/09_solo` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, choice/decision |
| [Automatic Love](#automatic-love) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Automatic_Love_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q105_dollhouse` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [Belly of the Beast](#belly-of-the-beast) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Belly_Of_The_Beast_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower` | meet/contact conversation, travel/reach location, wait/time gate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [Birds with Broken Wings](#birds-with-broken-wings) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Birds_With_Broken_Wings)) | MainQuest | `ep1/quests/main_quest/q304_stadium` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Black Steel In The Hour of Chaos](#black-steel-in-the-hour-of-chaos) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Black_Steel_in_the_Hour_of_Chaos_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q305_prison_convoy` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, combat/neutralize |
| [Disasterpiece](#disasterpiece) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Disasterpiece_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q105_03_braindance_studio` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, vehicle sequence |
| [Dog Eat Dog](#dog-eat-dog) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Dog_Eat_Dog)) | MainQuest | `ep1/quests/main_quest/q301_crash` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, combat/neutralize, stealth/avoid detection, vehicle sequence |
| [Down on the Street](#down-on-the-street) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Down_on_the_Street_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q112_01_old_friend` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, vehicle sequence |
| [Firestarter](#firestarter) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Firestarter_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q304_deal` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [For Whom the Bell Tolls](#for-whom-the-bell-tolls) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/For_Whom_The_Bell_Tolls_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q115_afterlife` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, interact/use device, retrieve/collect item, vehicle sequence |
| [Forward to Death](#forward-to-death) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Forward_To_Death_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q114_02_maglev_line_assault` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, interact/use device, retrieve/collect item, combat/neutralize, vehicle sequence |
| [Four Score and Seven](#four-score-and-seven) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Four_Score_and_Seven_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q305_reed_epilogue` | meet/contact conversation, wait/time gate |
| [From Her to Eternity](#from-her-to-eternity) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/From_Her_to_Eternity_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q306_postcontent` | phone/message contact, search/investigate, retrieve/collect item |
| [Get It Together](#get-it-together) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Get_It_Together)) | MainQuest | `ep1/quests/main_quest/q303_hands` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Ghost Town](#ghost-town) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Ghost_Town_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q103_warhead` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [Gimme Danger](#gimme-danger) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Gimme_Danger_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q112_02_industrial_park` | meet/contact conversation, follow/escort, wait/time gate, search/investigate, hack/breach/download, retrieve/collect item, vehicle sequence, leave/escape area |
| [Hole in the Sky](#hole-in-the-sky) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Hole_in_the_Sky)) | MainQuest | `ep1/quests/main_quest/q301_finding_myers` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device, hack/breach/download, combat/neutralize |
| [I Walk the Line](#i-walk-the-line) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I_Walk_the_Line_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q110_voodoo` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [I've Seen That Face Before](#ive-seen-that-face-before) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I%27ve_Seen_That_Face_Before_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q304_netrunners` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, vehicle sequence, leave/escape area |
| [Knockin' on Heaven's Door](#knockin-on-heavens-door) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Knockin%27_On_Heaven%27s_Door_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q115_rogues_last_flight` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, vehicle sequence, choice/decision |
| [Last Caress](#last-caress) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Last_Caress_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q113_rescuing_hanako` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, retrieve/collect item, combat/neutralize |
| [Leave in Silence](#leave-in-silence) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Leave_in_Silence_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q305_border_crossing` | meet/contact conversation, follow/escort, wait/time gate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Life During Wartime](#life-during-wartime) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Life_During_Wartime_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q104_02_av_chase` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Lightning Breaks](#lightning-breaks) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Lightning_Breaks_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q104_01_sabotage` | meet/contact conversation, travel/reach location, wait/time gate, interact/use device, retrieve/collect item, vehicle sequence |
| [Love Like Fire](#love-like-fire) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Love_Like_Fire_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q101_01_firestorm` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, combat/neutralize, vehicle sequence |
| [Lucretia My Reflection](#lucretia-my-reflection) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Lucretia_My_Reflection)) | MainQuest | `ep1/quests/main_quest/q302_reed` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [M'ap Tann Pèlen](#map-tann-plen) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/M%27ap_Tann_Pelen_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q110_01_voodooboys` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device |
| [Never Fade Away](#never-fade-away) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Never_Fade_Away_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q108_johnny` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Nocturne Op55N1](#nocturne-op55n1) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Nocturne_Op55N1_Walkthrough)) | MainQuest | `quests/meta/02_sickness` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, interact/use device, retrieve/collect item, deliver/deposit item, choice/decision, leave/escape area |
| [Play It Safe](#play-it-safe) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Play_It_Safe_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q112_03_dashi_parade` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, hack/breach/download, combat/neutralize, choice/decision, leave/escape area |
| [Playing for Time](#playing-for-time) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Playing_for_Time_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q101_resurrection` | phone/message contact, meet/contact conversation, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Practice Makes Perfect](#practice-makes-perfect) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Practice_Makes_Perfect_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q000_tutorial` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, combat/neutralize, stealth/avoid detection |
| [Run This Town](#run-this-town) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Run_This_Town_Walkthrough)) | MainQuest | `ep1/quests/minor_quest/mq304_succession` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [Search and Destroy](#search-and-destroy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Search_and_Destroy_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q112_04_hideout` | meet/contact conversation, travel/reach location, deliver/deposit item, leave/escape area |
| [Somewhat Damaged](#somewhat-damaged) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Somewhat_Damaged_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q305_bunker` | meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Spider and the Fly](#spider-and-the-fly) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Spider_and_the_Fly)) | MainQuest | `ep1/quests/main_quest/q301_q302_rescue_myers` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence, leave/escape area |
| [Tapeworm](#tapeworm) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Tapeworm_Walkthrough)) | MainQuest | `quests/side_quest/sq032_tapeworm` | travel/reach location, follow/escort, wait/time gate, interact/use device, retrieve/collect item, deliver/deposit item, leave/escape area |
| [The Corpo-Rat](#the-corpo-rat) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Corpo)) | MainQuest | `quests/main_quest/prologue/q000_corpo` | meet/contact conversation, travel/reach location, wait/time gate, interact/use device, retrieve/collect item, vehicle sequence, leave/escape area |
| [The Damned](#the-damned) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Damned)) | MainQuest | `ep1/quests/main_quest/q303_baron` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, leave/escape area |
| [The Heist](#the-heist) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Heist_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q005_heist` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [The Information](#the-information) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Information_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q004_braindance` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, leave/escape area |
| [The Killing Moon](#the-killing-moon) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Killing_Moon_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q306_devils_bargain` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, retrieve/collect item, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence, leave/escape area |
| [The Nomad](#the-nomad) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Nomad)) | MainQuest | `quests/main_quest/prologue/q000_nomad` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [The Pickup](#the-pickup) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Pickup_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q003_maelstrom` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence, leave/escape area |
| [The Rescue](#the-rescue) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Rescue_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q001_intro` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, hack/breach/download, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence |
| [The Ride](#the-ride) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Ride_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q001_02_dex` | phone/message contact, meet/contact conversation, vehicle sequence |
| [The Ripperdoc](#the-ripperdoc) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Ripperdoc_Walkthrough)) | MainQuest | `quests/main_quest/prologue/q001_01_victor` | phone/message contact, meet/contact conversation, search/investigate, retrieve/collect item, vehicle sequence |
| [The Space in Between](#the-space-in-between) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Space_In_Between_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q105_02_jigjig` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, combat/neutralize |
| [The Streetkid](#the-streetkid) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Street_Kid)) | MainQuest | `quests/main_quest/prologue/q000_street_kid` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Things Done Changed](#things-done-changed) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Things_Done_Changed_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q307_tomorrow` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, deliver/deposit item, choice/decision, leave/escape area |
| [Through Pain to Heaven](#through-pain-to-heaven) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Through_Pain_to_Heaven_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q306_reed_epilogue` | meet/contact conversation, wait/time gate, search/investigate |
| [Totalimmortal](#totalimmortal) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Totalimmortal_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q113_corpo` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, choice/decision |
| [Transmission](#transmission) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Transmission_Walkthrough)) | MainQuest | `quests/main_quest/act_01/q110_03_cyberspace` | phone/message contact, meet/contact conversation, follow/escort, wait/time gate, search/investigate, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [Unfinished Sympathy](#unfinished-sympathy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Unfinished_Sympathy_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q306_somi_epilogue` | meet/contact conversation, wait/time gate |
| [We Gotta Live Together](#we-gotta-live-together) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/We_Gotta_Live_Together)) | MainQuest | `quests/main_quest/act_01/q114_01_nomad_initiation` | meet/contact conversation, travel/reach location, follow/escort, interact/use device, combat/neutralize, vehicle sequence, choice/decision |
| [Who Wants to Live Forever](#who-wants-to-live-forever) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Who_Wants_to_Live_Forever_Walkthrough)) | MainQuest | `ep1/quests/main_quest/q307_before_tomorrow` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, vehicle sequence |
| [You Know My Name](#you-know-my-name) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/You_Know_My_Name)) | MainQuest | `ep1/quests/main_quest/q303_songbird` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |

## (Don't Fear) The Reaper

- IGN walkthrough: [(Don't Fear) The Reaper](https://www.ign.com/wikis/cyberpunk-2077/How_to_Get_the_Secret_Ending)
- Vanilla type: `MainQuest`
- Quest hash: `3926943725`
- Quest path: `quests/meta/09_solo`
- District: City Center / Corpo Plaza
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `choice/decision`

### Objective sequence

1. **Talk to Johnny.**  
   `Primary` · `quests/meta/09_solo/404/000_talk_johnny`
2. **Find a way to the level with Mikoshi.**  
   `Primary` · `quests/meta/09_solo/404/00b_find_way`
3. **Gain access to the elevators.**  
   `Primary` · `quests/meta/09_solo/404/00c_gain_access_elev`
4. **Defeat all enemies in the lobby.**  
   `Primary` · `quests/meta/09_solo/404/00d2_defeat_enemies`
5. **Loot the access token.**  
   `Primary` · `quests/meta/09_solo/404/00d_find_loot`
6. **Take the elevator to Mikoshi.**  
   `Primary` · `quests/meta/09_solo/404/00e_take_elev`
   - Map pin: ref `#q115_mp_solo_tower_elevator`; position `-1442.2836914063, 185.11427307129, 16.804281234741`
   - Map pin: ref `#q115_mp_solo_tower_elevator_terminal`; position `-1443.4080810547, 184.58753967285, 16.802095413208`
7. **Find the Mikoshi Access Point.**  
   `Primary` · `quests/meta/09_solo/404/01b_find_mikoshi`
8. **Defeat all enemies in the control room.**  
   `Primary` · `quests/meta/09_solo/404/01c2_clear_control`
9. **Talk to Johnny.**  
   `Primary` · `quests/meta/09_solo/404/01c_talk_johnny`
10. **Connect Alt to the mainframe.**  
   `Primary` · `quests/meta/09_solo/404/01d_connect_alt`
   - Map pin: ref `#q115_mp_jack_in_alt_mainframe`; position `-1451.4094238281, 148.27377319336, -26.287958145142`
11. **Go to the Mikoshi Access Point.**  
   `Primary` · `quests/meta/09_solo/404/01e_to_mikoshi`
   - Map pin: ref `#q116_mp_mikoshi_access_corridor`; position `-1408.0173339844, 145.28379821777, -24.723808288574`
12. **Defeat all enemies in the mainframe room.**  
   `Primary` · `quests/meta/09_solo/404/01f2_clear_nest`
13. **Find a way to connect Alt to the mainframe.**  
   `Primary` · `quests/meta/09_solo/404/01f_figure_out`
   - Map pin: ref `#q115_mp_netrunners_nest`; position `-1449.4479980469, 148.16578674316, -24.46693611145`
14. **Expose the mainframe.**  
   `Primary` · `quests/meta/09_solo/404/01g_raise_mainframe`
15. **Wait for the mainframe to surface.**  
   `Primary` · `quests/meta/09_solo/404/01h_wait_mainframe`
   - Map pin: ref `#q115_mp_jack_in_alt_mainframe`; position `-1451.4094238281, 148.27377319336, -26.287958145142`
16. **Defeat Adam Smasher.**  
   `Primary` · `quests/meta/09_solo/404/02_defeat_smasher`
17. **Decide Adam Smasher's fate.**  
   `Primary` · `quests/meta/09_solo/404/02b_decide_smasher`
18. **Get to the Mikoshi Access Point.**  
   `Primary` · `quests/meta/09_solo/404/03_get_to_access`
   - Map pin: ref `#q116_mp_mikoshi_access`; position `-1301.1682128906, 140.60104370117, -25.506830215454`
19. **Connect to the Access Point.**  
   `Primary` · `quests/meta/09_solo/404/04_jack_in`

## Automatic Love

- IGN walkthrough: [Automatic Love](https://www.ign.com/wikis/cyberpunk-2077/Automatic_Love_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2972821318`
- Quest path: `quests/main_quest/act_01/q105_dollhouse`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Get inside Evelyn's booth.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/03_investigation/chamber_go`
   - Map pin: ref `#q105_mp_dollhouse_cabin_11`; position `-629.2783203125, 785.353515625, 128.68029785156`
2. **Examine Evelyn's booth.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/03_investigation/chamber_investigate`
   - Map pin: ref `#q105_mp_dollhouse_cabin_11`; position `-629.2783203125, 785.353515625, 128.68029785156`
3. **Check the security feeds.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/03_investigation/client_computer`
4. **Find the security room.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/03_investigation/client_info`
5. **Ask Woodman about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/02b_ask_woodman`
6. **Confront Woodman.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/02c_confront_woodman`
7. **Leave the office.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/06_leave_office`
8. **Get more info about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/data`
9. **Go meet Woodman.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/find_woodman`
10. **Interrogate Woodman.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/interrogate_woodman`
11. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/johnny`
12. **Defeat Woodman.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/kill`
13. **Jack in to Woodman's computer.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/link`
14. **Head to Woodman's office.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/04_woodman/office`
15. **Take the elevator to the ground floor.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/03_take_elevator`
16. **Leave Clouds.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/leave`
17. **Call Judy.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/03_call_judy`
18. **Collect your weapons from the locker.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/take_weapons`
19. **Talk to Johnny.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/03a_talk_johnny`
20. **Sit and wait until the evening.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/02a_wait`
21. **Go into booth 6.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_1`
22. **Go into booth 9.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_2`
23. **Get more info about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/doll_info`
24. **Take the elevator to Clouds.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/elevator`
25. **Get €$500.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/get_money`
26. **Check in at the Clouds reception.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/go_reception`
   - Map pin: ref `#q105_mp_dollhouse_reception`; position `-641.36828613281, 810.85015869141, 130.35552978516`
27. **Find more info about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/info_evelyn`
28. **Head to Clouds in the evening.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/into_dollhouse`
   - Map pin: ref `#q105_mp_dollhouse_entrance`; position `-662.71759033203, 806.86450195313, 129.89273071289`
29. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/johnny`
30. **Go to Megabuilding H8.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/location`
31. **Ask Tom about Evelyn.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/talk_tom`
32. **Jack in at reception.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/reception`
33. **Return to Clouds' reception.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/return_dollhouse`
   - Map pin: ref `#q105_mp_dollhouse_reception`; position `-641.36828613281, 810.85015869141, 130.35552978516`
34. **Go into booth 6.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_6`
35. **Go into booth 9.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_9`
36. **Acquire a VIP access card.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/find_a_vip_card`
37. **Ask the doll about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_doll_question`
38. **Join the doll in the booth.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/room_doll_wait`
39. **Look for Evelyn at Clouds.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/search_evelyn`
40. **Find a way past security.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/security`
41. **Sit on the bed.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/sit`
42. **Ask Tom about Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/talk_tom1`
43. **Find Tom.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/tom_roxanne`
44. **Get inside the VIP area.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/vip`
45. **Deposit your weapons.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/dollhouse/weapons`
46. **Call Judy.**  
   `Optional` · `quests/main_quest/act_01/q105_dollhouse/lizzies/holocall_judy`
47. **Take the cigarette case.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/03a_loot_case`
48. **So you've decided to find the chick who put on this first-class shitshow. She had a job and you took it 'cause there was no one else to knock some sense into your gonk head. I'm here now, but so what? This search and rescue bullshit's a dead end, but that's not about to stop you. Maybe Evelyn will, who knows? Sure seems like she doesn't wanna be found.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/go_lizzies`
49. **Leave Lizzie's Bar.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/leave_lizzies`
50. **Meet with Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/meet_judy`
51. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/talk_johnny`
52. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_dollhouse/lizzies/talk_judy`

## Belly of the Beast

- IGN walkthrough: [Belly Of The Beast](https://www.ign.com/wikis/cyberpunk-2077/Belly_Of_The_Beast_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `792298338`
- Quest path: `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Climb onto the SERC.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/deeperunderground`
   - Map pin: ref `#q114_mp_driller`; position `-1395.9013671875, 15.51513671875, -36.747978210449`
2. **Wait for Mitch to finish calibrating.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/drill_wait`
   - Map pin: ref `#q114_mp_driller_goal`; position `-1444.2844238281, 25.8203125, -36.388404846191`
3. **You're almost there, V. In the heart of fucking darkness. Can you feel it? You're so close to the moment of goddamn truth. And I'm right there with you. Still. Always. Even if I'm just a blacked-out passenger in the backseat. Whatever you do, do it for us. At the very least, that's what I'm fucking counting on.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/drive`
   - Map pin: ref `#q114_mp_tunnel_drive`; position `159.48890686035, 2339.6437988281, 66.763130187988`
4. **Connect to the control panel.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/enter_driller`
   - Map pin: ref `#q114_mp_driller_controls`; position `-1394.8657226563, 17.172119140625, -35.302406311035`
5. **Get inside the Arasaka building.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/hole`
   - Map pin: ref `#q114_mp_driller_goal`; position `-1444.2844238281, 25.8203125, -36.388404846191`
6. **Talk to Mitch.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/inspect_driller`
7. **Exit the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/leave_panzer`
8. **Enter the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/panzer`
9. **Start the SERC.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/start_drill`
   - Map pin: ref `#q114_mp_driller_controls`; position `-1394.8657226563, 17.172119140625, -35.302406311035`
10. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/talk_panam`
11. **Talk to the Aldecaldos.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/talk_to_mitch`
12. **Talk to Saul and Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/talk_to_saul_panam`
13. **Wait for the Aldecaldos to open the tunnel.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/wait`
14. **Wait for the SERC to finish drilling.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/wait_for_driller`
15. **Join Mitch and Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/06_tunnel/walk_to_mitch_saul`
16. **Climb up.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/climb_to_manufacturing`
   - Map pin: ref `#q114_mp_shaft_goal_001`; position `-1498.3104248047, 78.043785095215, -32.654014587402`
   - Map pin: ref `#q114_mp_shaft_goal_002`; position `-1501.5096435547, 54.358757019043, -30.56226348877`
   - Map pin: ref `#q114_mp_shaft_goal_003`; position `-1499.9686279297, 54.377502441406, -21.50110244751`
   - Map pin: ref `#q114_mp_shaft_goal_004`; position `-1496.0697021484, 53.859527587891, -21.90234375`
17. **Reach the netrunner's nest.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/deeper`
   - Map pin: ref `#q114_mp_nest_passage`; position `-1471.5833740234, 108.83010864258, -25.273712158203`
18. **Use the terminal to lift the lockdown.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/get_rid_of_transport`
   - Map pin: ref `#q114_mp_gate_control_room`; position `-1455.8088378906, 96.054641723633, -25.242359161377`
19. **Reach the security room.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/get_to_security`
   - Map pin: ref `#q114_mp_gate_control_room`; position `-1455.8088378906, 96.054641723633, -25.242359161377`
20. **Move through the shaft.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/pass_hatch`
   - Map pin: ref `#q114_mp_shaft_goal_004`; position `-1496.0697021484, 53.859527587891, -21.90234375`
21. **Look around for a maintenance shaft.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/search_dampening`
   - Map pin: ref `#q114_mp_shaft_start`; position `-1496.2066650391, 78.334190368652, -32.654010772705`
22. **Neutralize the guards to access the terminal.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/secure_top_area`
23. **Leave the manufacturing level.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/sneak_manufacturing`
   - Map pin: ref `#q114_mp_cargo_exit_main`; position `-1480.2489013672, 100.01335144043, -25.090717315674`
   - Map pin: ref `#q114_mp_cargo_exit_side`; position `-1472.0487060547, 99.665054321289, -25.090717315674`
24. **Talk to Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/surveymanufacturing`
25. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/talk_nomads_wrap`
26. **Wait for the Aldecaldos to regroup.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/07_manufacturing/wait_for_saul`
27. **Wait for Alt.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/alt`
28. **Break into the netrunner's nest.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/breach_nest`
   - Map pin: ref `#q114_mp_netrunners_nest`; position `-1448.1171875, 147.10955810547, -27.652015686035`
29. **Take manual control of the SERC.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/enable_mainframe`
30. **Reach Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/mikoshi_floor`
31. **Talk to Saul and Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/plan_approach`
32. **Wait for the terminal.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/plug_alt`
33. **Slot the shard into the terminal.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/setup_splinter`
34. **Talk to the Aldecaldos.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/08_netrunner/talk_nomads`
35. **Reach Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/00_access_mikoshi`
36. **Open the gate.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/00b_wait_for_alt`
   - Map pin: ref `#q116_mp_open_gate`; position `-1407.2750244141, 145.1993560791, -24.96167755127`
37. **Defeat Adam Smasher.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/01_defeat_adam`
38. **Get to the Mikoshi Access Point.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/03_go_to_access`
   - Map pin: ref `#q116_mp_mikoshi_access`; position `-1301.1682128906, 140.60104370117, -25.506830215454`
39. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/04_talk_to_alt`
40. **Decide Smasher's fate.**  
   `Optional` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/02_decide_adam`
41. **Connect to Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/05_jack_in`
   - Map pin: ref `#q116_mp_mikoshi_access`; position `-1301.1682128906, 140.60104370117, -25.506830215454`
42. **Talk to Panam.**  
   `Optional` · `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/04b_talk_to_panam`

## Birds with Broken Wings

- IGN walkthrough: [Birds With Broken Wings](https://www.ign.com/wikis/cyberpunk-2077/Birds_With_Broken_Wings)
- Vanilla type: `MainQuest`
- Quest hash: `1011843887`
- Quest path: `ep1/quests/main_quest/q304_stadium`
- District: Pacifica
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Always thought it was in showbiz you couldn't trust a soul. Turns out, in hindsight, met a few good eggs in my time. But, man... all these cloaks from Langley? Guaranteed dagger in the back... And probably stuck there by a friend. You're gettin' played here, no doubt about it, but not much choice with our survival on the table. Just do me a favor – ears perked, eyes peeled and mind always, always razor-fuckin'-sharp.

### Objective sequence

1. **Wait a day for a call from Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/01_call_in/00_wait_for_reed`
2. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/01_call_in/01_talk_to_reed`
3. **Go to Alex's safehouse.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/01_go_to_safehouse`
   - Map pin: ref `#q304_mp_alex_safehouse`; position `-2435.7619628906, -2658.2365722656, 13.153308868408`
   - Map pin: ref `#q304_mp_alex_bar_entrance`; position `-2436.013671875, -2648.0998535156, 29.406314849854`
4. **Check gathered intel.**  
   `Optional` · `ep1/quests/main_quest/q304_stadium/02_briefing/01c_check_optional`
5. **Talk to Reed and Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/01b_talk_to_reed_alex`
6. **Take part in the briefing.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/02_join_the_meeting`
   - Map pin: ref `#q304_mp_briefing_table`; position `-2427.2426757813, -2671.4030761719, 14.574462890625`
7. **Play Songbird's recording.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/02b_turn_on_the_recording`
   - Map pin: ref `#q304_mp_briefing_table`; position `-2427.2426757813, -2671.4030761719, 14.574462890625`
8. **Watch Songbird's recording.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/02bb_listen_to_the_recording`
   - Map pin: ref `#q304_mp_songbird_recording`; position `-2425.9606933594, -2673.2761230469, 16.114992141724`
9. **Take the briefing shard.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/02c_lean_over_table`
   - Map pin: ref `#q304_mp_briefing_table`; position `-2427.2426757813, -2671.4030761719, 14.574462890625`
10. **Follow Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/03_follow_alex`
11. **Leave the safehouse.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02_briefing/03_leave_the_safehouse`
   - Map pin: ref `#q304_mp_safehouse_elevator`; position `-2436.4077148438, -2646.9367675781, 12.667804718018`
   - Map pin: ref `#q304_mp_alex_bar_exit_back_a`; position `-2418.9338378906, -2634.6682128906, 22.939914703369`
   - Map pin: ref `#q304_mp_alex_bar_exit_back_b`; position `-2417.2470703125, -2633.5927734375, 22.939914703369`
   - Map pin: ref `#q304_mp_alex_bar_exit`; position `-2422.3864746094, -2669.8942871094, 27.997924804688`
12. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/00_talk_to_alex`
13. **Call Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/00b_call_alex`
14. **Access the tracking station transceiver.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/01_access_trasmitter_01`
   - Map pin: ref `#q304_mp_transmiter_01_ap`; position `-1773.5137939453, -1916.3779296875, 68.847274780273`
15. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/01b_talk_to_alex`
16. **Access the second tracking station transceiver.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/02_access_tramistter_02`
   - Map pin: ref `#q304_mp_transmiter_04_ap`; position `-907.57055664063, -1774.7507324219, 20.12042427063`
17. **Find a way to restart the transceiver.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03_fix_trasmitter`
18. **Follow the hints to find the control panel.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03c_follow_hints`
19. **Talk to the kid.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03d_talk_to_kid`
20. **Wait for the power to restart.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03e_wait_power`
   - Map pin: ref `#q304_2c_mp_electric_box`; position `-895.80017089844, -1791.3502197266, 20.999998092651`
21. **Neutralize all enemies near the transceiver.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03f_clear_the_area`
22. **Pay for a tip on how to fix the transceiver.**  
   `Optional` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03b_pay_for_clue`
23. **Use the control panel to restart power.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/03d_use_the_switch`
   - Map pin: ref `#q304_2c_mp_electric_box`; position `-895.80017089844, -1791.3502197266, 20.999998092651`
24. **Download data from the transceiver.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/04_download_data`
   - Map pin: ref `#q304_mp_transmiter_04_ap`; position `-907.57055664063, -1774.7507324219, 20.12042427063`
25. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/02b_car_rental/04a_talk_to_johnny`
26. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/00_talk_to_songbird`
27. **Sit.**  
   `Optional` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/02a_sit_down`
   - Map pin: ref `#q304_mp_songbird_lean_down`; position `-1733.6168212891, -2677.9814453125, 78.437477111816`
28. **Call Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/01_call_reed`
29. **Meet Songbird between 11:00 PM and 1:00 AM.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/01_go_to_meeting_spot`
   - Map pin: ref `#q304_mp_songbird_meeting_spot`; position `-1697.2679443359, -2648.970703125, 79.61417388916`
30. **Meet Songbird between 11:00 PM and 1:00 AM.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/01_go_to_meeting_spot_2nd`
   - Map pin: ref `#q304_03_sm_songbird_interrupt`; position `-1703.7221679688, -2668.1213378906, 80.32447052002`
31. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/01b_talk_to_reed`
32. **Lean down.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/02_lean_down`
   - Map pin: ref `#q304_mp_songbird_lean_down`; position `-1733.6168212891, -2677.9814453125, 78.437477111816`
33. **Stand.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/02b_stand_up`
34. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/03_talk_to_songbird`
35. **Walk into the bushes.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/03b_enter_the_bushes`
   - Map pin: ref `#q304_mp_bushes`; position `-1697.3801269531, -2660.3413085938, 79.40998840332`
36. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/03c_follow_songbird`
37. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/03d_talk_to_songbird`
38. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03_songbird_meeting/04_talk_to_johnny`
39. **Go to Farida's clinic.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/00_go_see_farida`
   - Map pin: ref `#q304_mp_farida_entrance`; position `-1893.4512939453, -2485.1955566406, 29.806838989258`
40. **Wait a few hours for Reed to call.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/00b_wait_reed_call`
41. **Use the intercom.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/01_use_intercom`
   - Map pin: ref `#q304_mp_farida_intercom`; position `-1900.6208496094, -2478.6164550781, 25.576164245605`
42. **Talk to Farida.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/02_talk_with_farida`
   - Map pin: ref `#q304_mp_farida_intercom`; position `-1900.6208496094, -2478.6164550781, 25.576164245605`
43. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/02a_talk_with_reed`
44. **Talk to Farida.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/02b_talk_with_farida`
45. **Take the shard from Reed**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/02c_take_the_shard`
46. **Sit in the chair.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/03_sit_on_the_chair`
   - Map pin: ref `#q304_mp_farida_chair`; position `-1910.9818115234, -2466.21484375, 25.020900726318`
47. **Proceed with the operation.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/04_proceed_with_operation`
48. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/05_talk_with_johnny`
49. **Get up.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/06_get_up`
50. **Talk to Farida.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/06a_talk_with_farida`
51. **Exit the clinic.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03b_shard_pickup/07_exit_the_clinic`
   - Map pin: ref `#q304_mp_farida_entrance`; position `-1893.4512939453, -2485.1955566406, 29.806838989258`
52. **Reply to Alex's message.**  
   `Optional` · `ep1/quests/main_quest/q304_stadium/03c_alex_hear_to_heart/00_respond_to_alex_message`
53. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03c_alex_hear_to_heart/02_talk_to_alex`
54. **Sit.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03c_alex_hear_to_heart/02b_sit_down`
   - Map pin: ref `#q304_04e_mp_couch_sit_down`; position `-2431.2390136719, -2666.5505371094, 28.807952880859`
55. **Leave the bar.**  
   `Primary` · `ep1/quests/main_quest/q304_stadium/03c_alex_hear_to_heart/03_leave_bar`
   - Map pin: ref `#q304_04e_mp_leave_bar`; position `-2422.7373046875, -2669.4543457031, 29.090114593506`
56. **Meet Alex at The Moth.**  
   `Optional` · `ep1/quests/main_quest/q304_stadium/03c_alex_hear_to_heart/01_meet_alex_at_bar`
   - Map pin: ref `#q304_04e_mp_meet_alex`; position `-2431.7521972656, -2665.6821289063, 29.989957809448`

## Black Steel In The Hour of Chaos

- IGN walkthrough: [Black Steel in the Hour of Chaos](https://www.ign.com/wikis/cyberpunk-2077/Black_Steel_in_the_Hour_of_Chaos_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `283939362`
- Quest path: `ep1/quests/main_quest/q305_prison_convoy`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Not lookin' good, V. Alex is dead, Songbird's been nabbed by MaxTac and Reed… well, Reed still thinks he's got everything under control. But isn't this whole rescue op proof that he's lost the thread? I'll give him one thing - come hell or high water, he doesn't give up - keeps pushing forward till he gets his way. The key to success, you think? Guess we'll find out... long as we don't end up tossed into Los Padres first.

### Objective sequence

1. **Call Mr. Hands.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_mr_hands`
2. **Call back the netrunner or find another one.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_again`
3. **Call Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_mr_hand_not_optional`
4. **Call Mr. Hands back.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_mr_hands_again_not_optional`
5. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner`
6. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner1`
7. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner10`
8. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner11`
9. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner12`
10. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner13`
11. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner14`
12. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner2`
13. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner3`
14. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner4`
15. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner5`
16. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner6`
17. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner7`
18. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner8`
19. **Call a netrunner to help breach MaxTac.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_netrunner9`
20. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other`
21. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other1`
22. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other10`
23. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other11`
24. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other12`
25. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other13`
26. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other2`
27. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other3`
28. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other4`
29. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other5`
30. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other6`
31. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other7`
32. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other8`
33. **Call a different netrunner contact.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_other9`
34. **Send Reed a message with details.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_reed`
35. **Call Carol and convince her to help.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/get_carol`
36. **Call Chang-Hoon Nam and convince him to help.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/get_chang`
37. **Use the netrunner working for Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/get_mr_hands`
38. **Talk to Nix and convince him to help.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/get_nix`
39. **Talk to Sandra and convince her to help.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/get_sandra`
40. **Meet with Chang-Hoon.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/meet_chang`
41. **Meet with the netrunner.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/meet_lc_netrunner`
42. **Meet with Nix.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/meet_nix`
43. **Meet with Sandra.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/meet_sandra`
44. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_reed_ambush_info`
45. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_reed_ambush_info_nix`
46. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_reed_ambush_info_sandra`
47. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_reed_ambush_info_yoko`
48. **Send Reed a message with details.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/send_reed_ambush_info_chang`
49. **Send Reed a message with details.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/send_reed_ambush_info_nix`
50. **Send Reed a message with details.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/send_reed_ambush_info_sandra`
51. **Take the shard.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/take_shard`
52. **Talk to Sandra.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/talk_sandra`
53. **Call Carol back.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_carol`
54. **Call Chang-Hoon Nam back.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_chang`
55. **Call Mr. Hands back.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_mr_hands_again`
56. **Call Nix.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_nix`
57. **Call Sandra back.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/call_sandra`
58. **Take the shard.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/take_shard_chang`
59. **Talk to Yoko.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/talk_yoko`
60. **Read Chang-Hoon's message.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_message`
61. **Talk to Nix.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/talk_nix`
62. **Read Mr. Hands' message.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_message_mr_hands`
63. **Talk to Chang-Hoon.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/talk_chang`
64. **Read Nix's message.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_message_nix`
65. **Read Sandra's message.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/read_message_sandra`
66. **Wait 12 hours for Chang-Hoon to contact you.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_contact_chang`
67. **Listen to Yoko's proposal.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/yoko_job`
68. **Wait 6 hours for Nix's call.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_contact_nix`
69. **Wait 8 hours for Sandra's call.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_contact_sandra`
70. **Wait for Chang-Hoon.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_chang`
71. **Wait 10 hours for Mr. Hands' call.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_message_mr_hands`
72. **Wait for Nix.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_nix`
73. **Wait for Reed to text you.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_reed_message`
74. **Wait for Sandra.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_sandra`
75. **Wait for the netrunner.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_for_the_netrunner`
76. **Meet with Chang-Hoon in 12 hours.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_place_chang`
77. **Meet with Nix at the Arasaka Memorial in 6 hours.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_place_nix`
78. **Retrieve Carol's gift from the stash.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/01_task/pick_carol_gift`
79. **Meet Sandra at the park in 8 hours.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_place_sandra`
80. **Meet the netrunner in Kabuki in 10 hours.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/01_task/wait_place_yoko`
81. **Meet Reed at the abandoned hotel.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/01_meet_reed`
82. **Scan the ambush site.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/03_05_scan_around`
83. **Talk to Johnny.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/06_talk_to_johnny`
84. **Send Mr. Hands coordinates of the ambush site.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/08_message_mr_hands`
85. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/01a_wait_for_reed`
86. **Talk to the 6th Street gang.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/02_talk_6th_street`
87. **Take the shard.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/02a_take_shard`
88. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/03_05_first_talk_johnny`
89. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/03_talk_to_reed`
90. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/04_take_the_detonator`
91. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/05_follow_reed`
92. **Wait for the convoy.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/02_ambush_meeting/07_wait_for_convoy`
93. **Defeat the NCPD escort.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/01_kill_maxtac`
94. **Defeat the MaxTac operators.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/03a_defeat_maxtac`
95. **Use the "Ping" quickhack on MaxTac to upload Sandra's virus.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/02_sandra_ping`
96. **Open the truck's rear doors.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/04_check_truck`
97. **Check on Reed.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/04a_check_reed`
98. **Talk to Reed.**  
   `Optional` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/04b_talk_reed`
99. **Activate Sandra's quickhack on a MaxTac officer's body.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/02a_hack_on_corpse`
100. **Open the truck's rear doors.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/03_check_trunk`
101. **Follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03_ambush/05_chase_sb`
102. **Go back and follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03b_chase_intro/00_get_back_on_track`
103. **Follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_prison_convoy/03b_chase_intro/00a_chase_scenes`

## Disasterpiece

- IGN walkthrough: [Disasterpiece](https://www.ign.com/wikis/cyberpunk-2077/Disasterpiece_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `82370993`
- Quest path: `quests/main_quest/act_01/q105_03_braindance_studio`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`

### Objective sequence

1. **Watch the braindance or switch to Analysis Mode.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/00_watch_braindance`
2. **Analyze the braindance and find out where it was recorded.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/01_analyze_braindance`
3. **Look around for additional clues.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/02_look_for_clues`
4. **Meet Judy at her van.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/02_meet_judy_at_van`
5. **Exit the braindance when ready.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/04_leave_braindance`
6. **Enter the van.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/enter_van`
7. **Exit the van.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/exit_car`
8. **Put on the braindance gear.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/plug_in`
9. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/talk_judy2`
10. **Call Judy.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/02_blackmarket_braindance/00a_call_judy`
11. **Every city's got its shady neighborhoods and "no-go" zones. Stepping into these areas in Night City is like wading into the abyss and feeling it stare back through your soul. Anyone with an ounce of sense avoids these haunts altogether. Your average gonk's usually seen limping out, bleeding from one or more places. And you, V? Just make sure you come out intact.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/00_talk_judy`
12. **Gain access to the domain's underground twin.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01_look_web`
13. **Locate a terminal and find the Pleasures of NC domain.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01a_01_go_terminal`
14. **Take package.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01a_03_pick_package`
15. **Find an XBD dealer on the net.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01a_03_underground`
16. **Go to the pickup point.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01b_01_go_pickup`
   - Map pin: ref `#q105_mp_jigjig_pickup`; position `-597.97418212891, 860.14434814453, 17.115871429443`
17. **Open the Drop Point.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01b_02_open_compartment`
18. **Ask Wakako about the XBDs with the Death's-head moth.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01c_02_ask_about_braindances`
19. **Wait for details from Wakako.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01c_03_wait_coordinates`
20. **Buy an illegal braindance from the dealer.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01d_buy_braindance`
21. **Search the body.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01f_search_corpse`
22. **Ask around about XBDs on Jig-Jig Street.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/01a_00_optional_look`
   - Map pin: ref `#q105_tr_jigjig_street`; position `-639.60076904297, 882.01385498047, 15.259675979614`
23. **Call Wakako or visit her on Jig-Jig Street.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/call_wakado`
24. **Find the XBD dealer on Jig-Jig Street.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/look_for_dealer`
25. **Visit the sex shop on Jig-Jig Street.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/06_finding_studio/visit_shop`
26. **Go over to Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/15a_go_evelyn`
27. **Grab the cable.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/15b_take_cable`
28. **Yank the cable out of Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/15c_pull_cable`
29. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/15d_talk_judy`
30. **Get in the elevator.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/17_leave`
31. **Find an alternate route to the hallway.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/big_room_alternate`
32. **Neutralize the scavengers.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/big_room_takeout`
33. **Check on Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/check_evelyn`
34. **Lead Judy through the sub-levels.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/escort_judy_01`
   - Map pin: ref `#q105_mp_bd_leading_judy_first_door`; position `78.144912719727, -501.73260498047, -3.0362687110901`
35. **Enter the van.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/exit_car`
36. **Find a way to the sub-levels.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/find_entrance`
37. **Wait for Judy to distract the scavengers.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/transition_wait`
38. **Ride with Judy to the old power plant in Charter Hill.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/go_studio`
39. **Help Judy with Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/help_with_evelyn`
40. **Get to level -1.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/level_01`
41. **Find Evelyn.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/locate_evelyn`
42. **Reach the main building.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/main_building`
43. **Meet Judy in front of the old power plant in Charter Hill.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/meet_judy`
44. **Neutralize the scavengers.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/transition_kill`
45. **Meet with Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/reunion`
46. **Meet with Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/reunion1`
47. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/talk_judy`
48. **Distract the scavengers.**  
   `Optional` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/big_room_distraction`
49. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/talk_judy1`
50. **Wait for Judy to unlock the doors.**  
   `Primary` · `quests/main_quest/act_01/q105_03_braindance_studio/braindance/wait_door`

## Dog Eat Dog

- IGN walkthrough: [Dog Eat Dog](https://www.ign.com/wikis/cyberpunk-2077/Dog_Eat_Dog)
- Vanilla type: `MainQuest`
- Quest hash: `3125598773`
- Quest path: `ep1/quests/main_quest/q301_crash`
- District: Pacifica
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`

### Journal premise

Wow, this story's got it all! An unknown number, a mysterious caller, a shady meet-n-greet in the middle of fuckin' nowhere... And they say I'm the one always divin' headfirst into trouble. But sure, if it's not a trap, it's a one-in-a-trillion chance. Next stop: Dogtown. Can't wait to see how this shit unfolds.

### Objective sequence

1. **Go to the Dogtown border.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/get_to_combat_zone`
   - Map pin: ref `#q301_mp_hook_combat_zone`; position `-1333.8834228516, -1746.6179199219, 44.027248382568`
2. **Look for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/go_waiting_area`
3. **Sit.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/lean_on_truck`
   - Map pin: ref `#q301_mp_hook_sit_on_car`; position `-1358.6403808594, -1743.3969726563, 44.038414001465`
4. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/talk_johnny`
5. **Talk to the mystery caller.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/talk_songbird`
6. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/talk_songbird1`
7. **Sit and wait for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/00_hook/wait_for_mystery_calller`
   - Map pin: ref `#q301_00_mp_holocall_hook_wait`; position `-1349.7565917969, -1746.0275878906, 45.419998168945`
8. **Follow Songbird.**  
   `Optional` · `ep1/quests/main_quest/q301_crash/00_hook/follow_songbird`
9. **Go to the underground garage.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/access_garage`
10. **Connect to the access point.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/connect_access`
11. **Get onto the elevator platform.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/crane_platform`
12. **Eliminate all enemies.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/eliminate_all_enemies`
13. **Get onto the elevator platform.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/enter_elevator`
14. **Enter the elevator.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/enter_stadium_elevator`
15. **Find an access point.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/find_access_point`
16. **Find a way to restore power.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/find_power`
17. **Make your way to Dogtown through the garage.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/get_to_stadium`
18. **Reach the catwalk.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/reach_catwalk`
19. **Reach the car elevator platform.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/reach_crane_platform`
   - Map pin: ref `#q301_mp_border_garage_bridge`; position `-1321.4508056641, -1834.4913330078, 11.450000762939`
20. **Ride on the platform.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/ride_car_platform`
21. **Go to the garage.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/side_entrance`
22. **Talk to Songbird.**  
   `Optional` · `ep1/quests/main_quest/q301_crash/01_border/talk_songbird_catwalk`
23. **Sneak behind the car.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/side_entrance_behind_car`
24. **Enter the restricted area.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/side_entrance_entry`
25. **Find the entrance to the old parking garage.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/side_entrance_fence`
26. **Wait for further instructions.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/side_entrance_wait_for_songbird_instructions`
27. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/talk_johnny`
28. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/talk_songbird_return_johnny`
29. **Go to the stadium in Pacifica.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/travel_border`
30. **Start the generator.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/01_border/turn_on_generator`
31. **Go to the black market.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/02_stadium/blackmarket`
   - Map pin: ref `#q301_mp_stadium_blackmarket`; position `-1411.5014648438, -1998.5482177734, 76.290817260742`
32. **Go to the construction site.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/02_stadium/construction_site`
   - Map pin: ref `#q301_mp_stadium_circle_out`; position `-1344.5606689453, -2116.9853515625, 75.840003967285`
   - Map pin: ref `#q301_mp_stadium_construction`; position `-1284.6795654297, -2168.7055664063, 75.889999389648`
   - Map pin: ref `#q301_mp_stadium_construction_alt`; position `-1278.0096435547, -2157.5856933594, 79.199996948242`
   - Map pin: ref `#q301_mp_stadium_nl_loot`; position `-1345.5291748047, -2152.921875, 74.309997558594`
   - Map pin: ref `#q301_mp_stadium_to_circle_03`; position `-1372.6534423828, -2072.6630859375, 75.840003967285`
33. **Reset the power.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/02_stadium/lift_repair`
   - Map pin: ref `#q301_tr_stadium_powerbox`; position `-1266.9071044922, -2173.2902832031, 80.401008605957`
34. **Get up onto the roof.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/02_stadium/roof`
   - Map pin: ref `#q301_mp_stadium_guidance_01`; position `-1267.9195556641, -2165.2556152344, 80.050003051758`
   - Map pin: ref `#q301_mp_stadium_guidance_02`; position `-1282.0561523438, -2175.9240722656, 82.330001831055`
   - Map pin: ref `#q301_mp_stadium_guidance_03`; position `-1284.0201416016, -2174.6376953125, 128.66000366211`
   - Map pin: ref `#q301_mp_stadium_guidance_04`; position `-1300.5681152344, -2197.4145507813, 141.51000976563`
   - Map pin: ref `#q301_mp_stadium_guidance_05`; position `-1356.3084716797, -2233.1137695313, 146.05879211426`
   - Map pin: ref `#q301_mp_stadium_roof`; position `-1373.6511230469, -2209.1484375, 155.74000549316`
35. **Talk to Songbird.**  
   `Optional` · `ep1/quests/main_quest/q301_crash/02_stadium/talk_to_songbird`
36. **Go to the crash site.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/03_crash/reach_crashsite`
   - Map pin: ref `#q301_mp_way_to_crashsite_chute`; position `-1408.6370849609, -2262.591796875, 131.51898193359`
   - Map pin: ref `#q301_mp_crashsite_bottom`; position `-2013.0998535156, -2688.1628417969, 37.430011749268`
37. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/03_crash/talk_johnny`
38. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/03_crash/talk_songbird`
39. **Jump down the chute.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/03_crash/trash_chute`
   - Map pin: ref `#q301_mp_way_to_crashsite_chute`; position `-1408.6370849609, -2262.591796875, 131.51898193359`
40. **Sit and wait for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_crash/03_crash/wait_morning`
   - Map pin: ref `#q301_mp_crash_wait`; position `-1367.8294677734, -2202.1958007813, 154.10614013672`

## Down on the Street

- IGN walkthrough: [Down on the Street](https://www.ign.com/wikis/cyberpunk-2077/Down_on_the_Street_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3514555831`
- Quest path: `quests/main_quest/act_01/q112_01_old_friend`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `vehicle sequence`

### Journal premise

If someone told me I'd be taking calls from Saburo Arasaka's fucking bodyguard, I'd've laughed in their face. And now we're supposed to meet with some Takemura? Hand over all our detes? I'm not even gonna pretend like this is a good idea. But fuck it – sometimes you just gotta go all in.

### Objective sequence

1. **Meet with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00a_meet_takemura`
2. **If someone told me I'd be taking calls from Saburo Arasaka's fucking bodyguard, I'd've laughed in their face. And now we're supposed to meet with some Takemura? Hand over all our detes? I'm not even gonna pretend like this is a good idea. But fuck it – sometimes you just gotta go all in.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00ab_talk_phone`
3. **Lean on the barrier and wait for Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00b2_sit_takemura`
4. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00b_talk_takemura`
5. **Talk to Oda.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00c_talk_oda`
6. **Call Wakako.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00d_wait_takemura`
7. **Call Wakako.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00e_call_wakako_back`
8. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00_secret_meeting/00f_send_takemura`
9. **Go to Wakako.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00c_wakako/00c_01_meet_wakako`
   - Map pin: ref `#q112_mp_wakakos_pachinko_parlor`; position `-657.33172607422, 826.69134521484, 19.521728515625`
10. **Get into Takemura's van.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00c_wakako/00c_01b_join`
   - Map pin: ref `#q112_00b_mp_takemura_passenger_seat`; position `-929.05010986328, 1346.7999267578, 6.9000000953674`
11. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00c_wakako/00c_02_talk_takemura`
12. **Talk to Wakako.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00c_wakako/00c_03_talk_wakako`
13. **Wait for Takemura's call.**  
   `Primary` · `quests/main_quest/act_01/q112_01_old_friend/00c_wakako/00c_04_wait`

## Firestarter

- IGN walkthrough: [Firestarter](https://www.ign.com/wikis/cyberpunk-2077/Firestarter_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `422364849`
- Quest path: `ep1/quests/main_quest/q304_deal`
- District: Pacifica
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Journal premise

Think it's clear by now this ain't one of those stories that comes out all giggles and hugs. It's like I said – finger's on the trigger, just gotta decide who you got down your sights. Assumin' Hansen doesn't pull one on you first, of course. Good luck. And choose wisely.

### Objective sequence

1. **View the dossier.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/10b_test_dossier`
2. **Drive to the stadium.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/11_drive_to_the_stadium_driver`
   - Map pin: ref `#q304_mp_stadium_garage_checkpoint`; position `-1485.9827880859, -2072.5632324219, 29.016986846924`
   - Map pin: ref `#q304_mp_stadium_garage_entance_gate`; position `-1532.53125, -2209.650390625, 33.321773529053`
   - Map pin: ref `#q304_mp_stadium_garage_entance_gate_part2_right`; position `-1467.6696777344, -2150.7094726563, 29.217304229736`
   - Map pin: ref `#q304_mp_stadium_garage_entance_gate_part2_left`; position `-1458.1917724609, -2165.5932617188, 29.217304229736`
   - Map pin: ref `#q304_mp_stadium_garage_outter_checkpoint`; position `-1506.5397949219, -2288.6901855469, 40.570003509521`
3. **Park the car.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/11_drive_to_the_stadium_driver1`
   - Map pin: ref `#q304_mp_stadium_garage_parking_spot`; position `-1465.8565673828, -2020.2239990234, 29.172340393066`
4. **Get out of the car.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/11_get_out_of_the_car`
5. **Lose your pursuers.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/11_loose_enemies`
6. **Wait for vehicle ID verification.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/11b_id_check`
7. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/12_talk_to_alex`
8. **View the netrunner's dossier.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/12b_test_dossier`
9. **Follow Alex.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/13_follow_alex`
10. **Take the elevator to the ground floor.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/04_entering_stadium/14_take_elevator_up`
   - Map pin: ref `#q304_mp_pz_elevator_lift_panel`; position `-1452.9000244141, -2015.3999023438, 29.999996185303`
11. **Get in the elevator.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/03b_take_your_place_in_the_elevator`
   - Map pin: ref `#q304_mp_pz_elevator_spot`; position `-1455.13671875, -2013.5073242188, 29.789627075195`
12. **Take the elevator with Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/04_take_the_lift`
13. **Talk to Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/06_talk_to_murphy`
14. **Deposit your weapons.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/12_deposit_weapons`
   - Map pin: ref `#q304_mp_weapns_locker`; position `-1360.8305664063, -1931.9104003906, 65.056427001953`
15. **Talk to Hansen.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/14_talk_to_kurt`
16. **Follow Hansen.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/15_follow_kurt`
17. **Sit.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/16_sit_down`
   - Map pin: ref `#q304_mp_deal_sit_down`; position `-1289.1906738281, -1880.3514404297, 63.520233154297`
18. **Talk to Hansen.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/17_talk_to_kurt`
19. **Get up.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/18_get_up`
20. **Follow Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/follow_kruger`
21. **Follow Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/follow_kruger1`
22. **Talk to Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/talk_to_kruger`
23. **Talk to Murphy.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06_deal/talk_to_kruger1`
24. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/01_follow_songbird`
25. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/02_talk_to_songbird`
26. **Take your place by the mainframe.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/02b_take_place`
27. **Connect to the mainframe.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/03_connect_to_core`
28. **Follow Songbird's instructions.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/04_work_with_songbird`
29. **Decide whose side you'll take.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/06b_lab/05_decide`
30. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/01_talk_to_songbird`
31. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/01b_follow_songbird`
32. **Escape the secured area with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/02_escape_vip_area`
33. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/02b_help_songbird_up`
34. **Wait for Songbird to open the door.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/02c_wait_for_door`
35. **Reach the market exit with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/03_cross_the_market`
36. **Escape the stadium with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/04_escape_the_stadium`
37. **Move the crates to open a path.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07a_songbird_escape/04b_move_crates`
38. **Retrieve your gear from the locker.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/00_get_your_gear`
   - Map pin: ref `#q304_mp_weapns_locker_escape`; position `-1360.8251953125, -1931.8918457031, 64.99959564209`
   - Map pin: ref `#q304_mp_weapns_locker_escape_reed`; position `-1359.3184814453, -1933.1832275391, 64.62866973877`
39. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/01_talk_to_johnny`
40. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/02_talk_to_reed`
41. **Get up.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/02b_get_up`
42. **Escape the secured area.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/03_escape_vip_area`
43. **Reach the market exit.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/04_cross_the_market`
44. **Neutralize Hansen.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/04b_defeat_kurt`
45. **Neutralize Hansen and his soldiers.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/04bb_defeat_kurt_and_soldiers`
46. **Search Hansen.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/04c_loot_security_shard_from_kurt`
47. **Meet with Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/05_reach_reed`
48. **Escape the market.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/05b_escape_the_black_barket`
49. **Take the elevator to the garage.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/07b_reed_escape/05c_take_the_elevator`
50. **Open the sewer grate.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08a_songbird_finale/00a_open_grate`
   - Map pin: ref `#q304_mp_open_the_grate`; position `-1273.4453125, -2362.015625, 46.089393615723`
51. **Jump out of sewer to the ground.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08a_songbird_finale/00b_jump_down`
   - Map pin: ref `#q304_mp_homless_camp_jump_down`; position `-1271.50390625, -2367.650390625, 41.09375`
52. **Lead Songbird out of the homeless camp.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08a_songbird_finale/02_lead_to_exit`
   - Map pin: ref `#q304_mp_homless_camp_exit`; position `-1230.2055664063, -2376.1223144531, 41.581317901611`
53. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08a_songbird_finale/03_talk_to_songbird_failsafe`
54. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08a_songbird_finale/05_talk_to_songbird`
55. **Get in the car.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08b_reed_finale/00_get_into_van`
56. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08b_reed_finale/01_talk_to_reed`
57. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q304_deal/08b_reed_finale/02_talk_to_johnny`

## For Whom the Bell Tolls

- IGN walkthrough: [For Whom The Bell Tolls](https://www.ign.com/wikis/cyberpunk-2077/For_Whom_The_Bell_Tolls_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `425364669`
- Quest path: `quests/main_quest/act_01/q115_afterlife`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`

### Objective sequence

1. **V? Don't know if you can hear me. Not even sure you're aware what's going on. What I do know is you got serious guts to make the decision you did. And I promise I'm not gonna fuck this up. I'll convince Rogue to take Arasaka Tower for one more wild ride.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/00_meet_rogue`
2. **Gear up.**  
   `Optional` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01c_grab_equipment`
3. **Talk to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01_talk_rogue`
4. **Prepare for combat.**  
   `Optional` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/06c_prepare_for_fight`
5. **Follow Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01a_follow_rogue`
6. **Take the retrothrusters.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01b_grab_thrusters`
7. **Take the shard.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01d_grab_splinter`
8. **Talk to Weyland.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01e_talk_weyland`
9. **Stand.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01f_get_up`
10. **Follow Weyland.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/01g_follow_weyland`
11. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02_talk_alt`
   - Map pin: ref `#q115_mp_alt_white_room_marker`; position `-1654.6489257813, 1583.9084472656, -554.98004150391`
12. **Sit in the netrunner's chair.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02a_connect_to_chair`
   - Map pin: ref `#q115_mp_afterlife_get_on_chair`; position `-1448.4437255859, 996.82250976563, 17.376859664917`
13. **Talk to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02a_talk_rogue`
14. **Put on the netrunner suit.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02b_put_on_suit`
   - Map pin: ref `#q115_mp_netrunner_suit`; position `-1447.9543457031, 999.86437988281, 18.207412719727`
15. **Stand.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02c2_get_up`
16. **Go to the netrunners' room.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02c_go_net_room`
   - Map pin: ref `#q115_mp_netrunner_room`; position `-1446.7979736328, 996.98626708984, 17.887861251831`
17. **Talk to Nix.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02e_talk_nix`
18. **Wait for Nix to connect you.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/02f_wait_nix`
19. **Go to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/03_go_to_rogue`
20. **Talk to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/04_talk_with_rogue`
21. **Follow Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/06_follow_rogue`
22. **Take the elevator to the roof.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/06b_elevator`
   - Map pin: ref `#q115_mp_afterlife_elevator`; position `-1463.6495361328, 1032.1547851563, 18.378648757935`
23. **Get in the AV.**  
   `Primary` · `quests/main_quest/act_01/q115_afterlife/02_afterlife/07_get_in_av`
   - Map pin: ref `#q115_mp_afterlife_get_in_av`; position `-1443.7813720703, 1025.0521240234, 88.209320068359`

## Forward to Death

- IGN walkthrough: [Forward To Death](https://www.ign.com/wikis/cyberpunk-2077/Forward_To_Death_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2877463751`
- Quest path: `quests/main_quest/act_01/q114_02_maglev_line_assault`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`

### Objective sequence

1. **Talk to Saul and Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/brief_nomads`
2. **Use the drone to survey the construction site.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/drone`
3. **Follow Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/panam`
4. **Enter the panzer when you're ready.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/panzer1`
5. **Talk to Panam and Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/plan1`
6. **Take the shard from Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/splinter`
7. **Get ready to fight.**  
   `Optional` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/gear_up`
8. **Last stop on the line. Little does the corp know that this train's not going back. It's a shame I won't be there with you, 'cuz it's looking to be one helluva ride. But hey, that's what family's for, right? Anyway, once you get to the Arasaka sublevels, that crater filled with chrome and concrete, just take a second to remember that Johnny was there. Then mow down anyone in your way and get to Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/03_planning/talk_to_panam`
9. **Enter the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/board_panzer`
10. **Break through the obstacles.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/break_through`
   - Map pin: ref `#q114_mp_barriers`; position `2088.7768554688, 2715.6818847656, 126.82600402832`
11. **Ram your way through the bridge.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/clear_bridge`
12. **Eliminate all enemies in the area.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/clear_courtyard`
13. **Drive onto the construction site.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/continue_approach`
   - Map pin: ref `#q114_mp_construction`; position `249.13703918457, 2428.7822265625, 67.081176757813`
14. **Destroy the intercepting drones.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/convoy`
15. **Protect the panzer during repair.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/defend_panzer`
16. **Drive onto the construction site.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/drive`
   - Map pin: ref `#q114_mp_construction`; position `249.13703918457, 2428.7822265625, 67.081176757813`
17. **Ram the gate.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/gate`
   - Map pin: ref `#q114_mp_gate_001`; position `249.95065307617, 2430.748046875, 70.084129333496`
18. **Exit the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/leave_panzer`
19. **Follow Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/santiago`
20. **Destroy the turrets.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/04_approach/turrets`
21. **Drive to the tunnel entrance.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/approach_controls`
22. **Prepare for enemy reinforcements.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/av`
23. **Enter the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/board_panzer`
24. **Neutralize all enemies.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/cleanup_site`
25. **Drive onto the construction site.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/construction`
   - Map pin: ref `#q114_mp_construction`; position `249.13703918457, 2428.7822265625, 67.081176757813`
26. **Neutralize Militech's forces.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/defeat_dropteam`
27. **Neutralize Militech's forces.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/defend`
28. **Escort Mitch and Carol.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/escort`
29. **Intercept Militech's strike team.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/intercept`
   - Map pin: ref `#q114_mp_tank_battle_waypoint`; position `292.60833740234, 2473.0356445313, 67.259948730469`
30. **Exit the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/leave_panzer`
31. **Neutralize Militech's strike team.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/panzer`
32. **Enter the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/return`
33. **Return to the construction site.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/return_to_construction`
   - Map pin: ref `#q114_mp_construction`; position `249.13703918457, 2428.7822265625, 67.081176757813`
34. **Drive through the tunnel.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/tunnel1`
35. **Wait at the tunnel entrance.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/tunnel_wait`
36. **Wait for Mitch and Carol.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/wait_mitch_carol`
37. **Wait for the Aldecaldos to regroup.**  
   `Primary` · `quests/main_quest/act_01/q114_02_maglev_line_assault/05_construction/wait_regroup`

## Four Score and Seven

- IGN walkthrough: [Four Score and Seven](https://www.ign.com/wikis/cyberpunk-2077/Four_Score_and_Seven_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3474490875`
- Quest path: `ep1/quests/main_quest/q305_reed_epilogue`
- District: Dogtown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`

### Journal premise

A message from Reed… A welcome surprise or a reason to nibble my nails raw? He wants to meet at the place where it all kicked off – symbolism's fucking plain as day. Problem with symbols is that they can mean a shitload of different things. 'Specially when it's an FIA agent extending the invitation.

### Objective sequence

1. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/00_read_message`
2. **Reply to Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/00a_answer_reed_messages`
3. **Wait for Reed to contact you.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/00b_wait_for_message_from_reed`
4. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/00c_wait_for_reed`
5. **Meet with Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/01_meet_reed`
6. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_reed_epilogue/10_reed_finale/02_talk_to_reed`

## From Her to Eternity

- IGN walkthrough: [From Her to Eternity](https://www.ign.com/wikis/cyberpunk-2077/From_Her_to_Eternity_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `922330340`
- Quest path: `ep1/quests/main_quest/q306_postcontent`
- Candidate building blocks: `phone/message contact`, `search/investigate`, `retrieve/collect item`

### Journal premise

Wonder how Songbird's doin'. Maybe we ougha raised a toast to her too? Never really understood why people love to gawk at the moon with those vacant, dreamy expressions. But now... might have to give it a try myself. Meanwhile, you keep your nose to the ground so you don't step in any shit.

### Objective sequence

1. **Decrypt Songbird's shard.**  
   `Optional` · `ep1/quests/main_quest/q306_postcontent/00_common/00_decrypt_shard`
2. **Read the message from the unknown sender.**  
   `Primary` · `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message`
3. **Search the area around the provided coordinates.**  
   `Primary` · `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache`
   - Map pin: ref `#q306_songbird_epilogue_cache`; position `-1733.1640625, -2678.5827636719, 78.012153625488`
   - Map pin: ref `#q306_tr_cache_search_area`; position `-1734.1005859375, -2677.6748046875, 77.917945861816`
4. **Collect the contents of the container.**  
   `Primary` · `ep1/quests/main_quest/q306_postcontent/00_common/00_loot_cache`
   - Map pin: ref `#q306_songbird_epilogue_cache`; position `-1733.1640625, -2678.5827636719, 78.012153625488`
5. **Play Songbird's message on your computer.**  
   `Primary` · `ep1/quests/main_quest/q306_postcontent/00_common/01_listen_to_recording`
   - Map pin: ref `#q306_mp_computer`; position `-1387.0181884766, 1273.5141601563, 124.30208587646`
6. **Distribute So Mi's mementos around your apartment.**  
   `Primary` · `ep1/quests/main_quest/q306_postcontent/00_common/02_place_mementos`
   - Map pin: ref `#q306_mp_mementos_spot`; position `-1378.8194580078, 1268.5186767578, 123.06481170654`

## Get It Together

- IGN walkthrough: [Get It Together](https://www.ign.com/wikis/cyberpunk-2077/Get_It_Together)
- Vanilla type: `MainQuest`
- Quest hash: `686544125`
- Quest path: `ep1/quests/main_quest/q303_hands`
- District: Dogtown
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Your missing uber-netrunner got snared by Dogtown’s head honcho. What a lovely plot twist. Dunno how you wanna get into the Black Sapphire or if it’s even possible, but that’s not the thing I worry about. What does worry me is what you’re gonna do once you get inside. Thoughts?

### Objective sequence

1. **Call Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/01a_call_hands`
2. **Talk to Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/01b_talk_mr_hands_phone`
3. **Complete at least three gigs for Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/01c_complete_gigs`
4. **Go to the Heavy Hearts club.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/01d_go_to_pyramid`
   - Map pin: ref `#q303_mp_meet_hands_pyramid`; position `-1609.2811279297, -2327.4777832031, 43.050861358643`
5. **Wait a few hours for Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/02a_wait`
6. **Read the message from Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/02b_read_message`
7. **Go to the elevator at the Heavy Hearts.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/03_follow_reed`
8. **Reach the private floor.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/03a_press_the_floor`
   - Map pin: ref `#q303_mp_press_second_floor`; position `-1569.0565185547, -2348.0373535156, 45.411327362061`
9. **Enter code 2589 on the terminal.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/03b_enter_code`
10. **Talk to Mr. Hands.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/04_talk_mr_hands`
11. **Leave the club.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/04a_leave_pyramid`
   - Map pin: ref `#q303_mp_exit_pyramid`; position `-1614.7624511719, -2320.0544433594, 43.038543701172`
12. **Call Reed and send him the data.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/04_mr_hands/05_call_reed`
13. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/00_wait_nighthawks`
   - Map pin: ref `#q303_mp_nighthawks_wait`; position `-2421.8239746094, -2671.470703125, 28.441886901855`
14. **Meet with Reed at The Moth.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/01_go_nighthawks`
15. **Get armed.**  
   `Optional` · `ep1/quests/main_quest/q303_hands/05_safehouse/05_gather_loot`
16. **Sit down.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/02_sit_down`
   - Map pin: ref `#q303_mp_safehouse_nighthawks_sit`; position `-2433.021484375, -2670.0297851563, 28.411138534546`
17. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/02a_talk_reed`
18. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/02b_follow_reed`
19. **Ride the elevator down.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/03_ride_down`
   - Map pin: ref `#q303_mp_safehouse_lift_terminal`; position `-2434.2651367188, -2646.9084472656, 29.209722518921`
20. **Talk to Alex and Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/04_talk_alex`
21. **Sit down.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/04a_sit_down`
22. **Follow Alex.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/04b_follow_alex`
23. **Examine the contents of the box.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/05b_majesty`
24. **Grab the diving suit.**  
   `Primary` · `ep1/quests/main_quest/q303_hands/05_safehouse/05c_suit`
   - Map pin: ref `#q303_05_mp_diving_suit`; position `-2416.9094238281, -2662.8408203125, 13.039999008179`

## Ghost Town

- IGN walkthrough: [Ghost Town](https://www.ign.com/wikis/cyberpunk-2077/Ghost_Town_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3062825933`
- Quest path: `quests/main_quest/act_01/q103_warhead`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Collect €$15,000**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/gather_money`
2. **Wanna track down Hellman? Start at The Afterlife. Sure, the place has changed over the years, but one thing never will: you got a question you just can't shake, head to The Afterlife. Always someone there to whisper the answer in your ear... for the right price. And if that someone's Rogue – shit, I wouldn't miss this meet for the world.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/go_afterlife`
   - Map pin: ref `#q103_mp_afterlife_exterior`; position `-1465.1546630859, 1046.9714355469, 22.759357452393`
3. **Return to Rogue with 15000 €$.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/pay_rogue`
4. **Sit next to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/sit_down`
   - Map pin: ref `#q103_mp_rogue_sofa`; position `-1421.0095214844, 1014.0298461914, 17.350004196167`
5. **Talk to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/talk_rogue`
6. **Wait until Rogue is ready.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/wait_1_day`
   - Map pin: ref `#q103_mp_wait_rogue`; position `-1437.7058105469, 1009.2124633789, 17.304002761841`
7. **Wait for Rogue to finish her conversation.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/afterlife/wait_for_rogue`
8. **Break the window and enter.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/break_window`
   - Map pin: ref `#q103_mp_power_glass`; position `2594.8120117188, -57.297435760498, 83.31999206543`
9. **Take box.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/carry_box`
10. **Connect the cables to the battery.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/connect_battery`
   - Map pin: ref `#q103_mp_gt_hood`; position `2603.890625, -76.873092651367, 81.593002319336`
11. **Decide on a plan with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/decide_aft_ghost`
12. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/drive_away`
13. **Leave Rocky Ridge.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/escape`
14. **Get the key to Panam's car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/find_key`
15. **Follow Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/follow_panam`
16. **Get in the car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/get_in_car`
17. **Wait for Panam by the power substation.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/go_power_station`
   - Map pin: ref `#q103_mp_power_station`; position `2600.5126953125, -73.992736816406, 80.780006408691`
18. **Discuss the plan with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/gt_talk_panam`
19. **Go to the roof.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/head_rooftop`
20. **Get into position.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/hide_ledge`
   - Map pin: ref `#q103_mp_power_lever`; position `2591.2241210938, -52.682628631592, 85.499992370605`
21. **Defeat the Raffen Shiv.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/kill_raffen_shiv`
22. **Leave the car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/leave_car`
23. **Turn on the lights at the intersection.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/light_city`
24. **Take the passenger seat.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/passenger_seat`
25. **Take the jumper cables.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/pickup_cables`
26. **Place the box in the trunk.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/put_box_away`
   - Map pin: ref `#q103_mp_nomads_box_away`; position `3376.2277832031, -343.91192626953, 134.33111572266`
27. **Go to the meeting point.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/rendezvous_gt_north1`
28. **Restore power in the switchgear.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/restore_power`
29. **Just when you think you've solved your problem, your solution goes and starts making fucking demands. Looks like Panam'll only scratch your back if you scratch hers. Could've expected that, coming from a nomad. Know what, though? I've got a good feeling about this sand-swept desert dame. Let's see where our newfound friendship takes us. Preferably to that weasely fuck, Hellman.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/ride_camp`
30. **Go to Rocky Ridge with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/ride_to_ghost_town`
   - Map pin: ref `#q103_mp_ghost_town`; position `2580.3017578125, -41.797267913818, 80.810005187988`
31. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/scout`
32. **Take Panam's car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/steal_car`
33. **Switch seats with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/switch_seats`
34. **Talk to Mitch and Scorpion.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/talk_scorp_mitch`
35. **Call Panam when you're ready.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/tell_panam_ready`
36. **Wait for Panam in the car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/wait_panam_in_car`
37. **Wait for the Raffen Shiv.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town/wait_raffen`
38. **Search the meeting area.**  
   `Optional` · `quests/main_quest/act_01/q103_warhead/ghost_town/check_area`
39. **Take down the Raffen by Panam's car.**  
   `Optional` · `quests/main_quest/act_01/q103_warhead/ghost_town/takedown_veh_guard`
40. **Scan the transformer.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town_recon/01_02_scan_transformer`
41. **Scan the devices in the area.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town_recon/01_scan_cables`
42. **Scan the power source.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town_recon/02_scan_fusebox`
43. **Go back to the car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/ghost_town_recon/03_back_car`
44. **Rogue's alive and kicking at The Afterlife. That part doesn't surprise me – but why she's throwing you at some ex-nomad who can't get her shit together? Rogue's working an angle here, I just can't see it. Fuck, maybe I'm just being paranoid. That or Rogue was telling the truth – Panam's all you can afford right now. Oh well, just talk to her and find Hellman. No point wasting time on conspiracy theories.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/panam/call_panam`
45. **Take the passenger seat.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/panam/get_in_car`
   - Map pin: ref `#q103_mp_meet_pan_car_entry`; position `693.60900878906, -640.01995849609, 10.470003128052`
46. **Meet with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/panam/go_to_panam`
47. **Go to Rocky Ridge with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/panam/ride`
48. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/panam/talk_panam`
49. **Lie down.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/bed_downstairs`
   - Map pin: ref `#q103_mp_bed_downstairs`; position `1659.1318359375, -791.10021972656, 50.340000152588`
50. **Lie down.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/bed_upstairs`
   - Map pin: ref `#q103_mp_bed_upstairs`; position `1592.3619384766, -797.06030273438, 54.270000457764`
51. **Follow Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/follow_panam_bar`
52. **Follow Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/follow_panam_room`
53. **Go to your room.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/go_to_room`
   - Map pin: ref `#q103_mp_motel_room`; position `1662.6805419922, -791.50994873047, 49.819999694824`
54. **Leave the car.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/leave_car`
55. **Go to the Sunset Motel with Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/ride`
56. **Sit at the bar.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/sit_stool`
   - Map pin: ref `#q103_mp_roadhouse_stool`; position `1636.9637451172, -798.13562011719, 54.712791442871`
57. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/talk_panam`
58. **Wait for Panam to strike a deal.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/roadhouse/wait_convo_maelstrom`
59. **Defeat Nash and his people.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/defeat_boss`
60. **Take the passenger seat.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/get_back_to_car`
61. **Go to the Raffen Shiv hideout.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/ride`
62. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/summarize_panam`
63. **Join Panam.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/wait_panam`
64. **Wait for Panam to finish her conversation.**  
   `Primary` · `quests/main_quest/act_01/q103_warhead/tunnels/wait_panam_call`

## Gimme Danger

- IGN walkthrough: [Gimme Danger](https://www.ign.com/wikis/cyberpunk-2077/Gimme_Danger_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3503651879`
- Quest path: `quests/main_quest/act_01/q112_02_industrial_park`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `wait/time gate`, `search/investigate`, `hack/breach/download`, `retrieve/collect item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Wait for Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01a1_wait_takemura`
   - Map pin: ref `#q112_mp_market_wait_takemura`; position `-402.2395324707, 707.69549560547, 115.57498931885`
2. **Our crazed ronin shows no signs of slowing his roll. We barely get intel from Wakako about the parade and Takemura's already hatching some harebrained scheme in Japantown. He wants to meet at the market? Fine, let's parley, but you already know where I stand. Don't let him strong-arm you into anything. Who knows how many loose screws are bouncing around in that skull of his at this point...**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01a_meet_takemura`
   - Map pin: ref `#q112_mp_market_takemura_node`; position `-415.31991577148, 714.65014648438, 116.25`
3. **Go over the plan with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01a_meet_takemura1`
4. **Take the shard.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01b_2`
5. **Sit beside Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01c_sit_down`
   - Map pin: ref `#q112_mp_01_market_sit_market_stand`; position `-431.79678344727, 670.62548828125, 115.68328094482`
6. **Get up.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01e_get_up`
7. **Watch the news on TV.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01f_hanako_report`
8. **Break into the security room.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01h_infiltrate_security`
   - Map pin: ref `#q112_mp_01_market_security_room`; position `-436.21255493164, 651.26470947266, 116.05464172363`
9. **Infect the security system.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/01_market/01i_code`
10. **So we're really doing this – breaking into Arasaka Industrial Park to hack Hanako's float for the parade in honor of her corpo-vampire daddy. All this just so Takemura can get an audience with her! You know, I've done a lotta gonk shit in my day, but I never got in the same bed as the fucking ENEMY. I dunno what's waiting for us at the end of this road, but I'm waiving all responsibility. This is on YOU.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02a_drive_to_arroyo`
11. **Look through the scope.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02b2_scope`
12. **Get onto the roof.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02b_get_to_roof`
13. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02c2_observe_done`
14. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02c2_talk_takemura`
15. **Scan the area.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02c_observe`
16. **Go over the plan with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02d_explosives`
17. **So we're really doing this – breaking into Arasaka Industrial Park to hack Hanako's float for the parade in honor of her corpo-vampire daddy. All this just so Takemura can get an audience with her! You know, I've done a lotta gonk shit in my day, but I never got in the same bed as the fucking ENEMY. I dunno what's waiting for us at the end of this road, but I'm waiving all responsibility. This is on YOU.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02e_wait`
18. **Follow Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02f_follow_takemura`
19. **Get in the car.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02g_get_in_car`
20. **Keep scanning.**  
   `Optional` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02c4_observe_optional`
21. **Wait for Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/02_reconnaissance/02h_wait_takemura`
22. **Wait with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/03_takemura/03a_spend_time`
23. **Return to street level.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/03_takemura/03b_return`
24. **Get up.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/03_takemura/03c_get_up`
25. **Take the shard.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04a_take_code`
26. **Steal the truck.**  
   `Optional` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04g_use_truck`
27. **Get inside the warehouse.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04d2_get_warehouse`
28. **Drive into Arasaka Industrial Park.**  
   `Optional` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04g2_drive_truck`
   - Map pin: ref `#q112_mp_truck_drive_inside`; position `-209.25668334961, -1454.2150878906, 7.5999436378479`
29. **Leave Arasaka Industrial Park.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04h_leave`
30. **Convince the guard to let you in.**  
   `Optional` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/4f_use_nomad`
31. **Meet with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04b_meet_takemura`
32. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04c_talk_takemura`
33. **Break into Arasaka Industrial Park.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04d_get_inside`
34. **Hack the float.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04e_hack`
35. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_02_industrial_park/04_infiltration/04i_talk_takemura_no_mp`

## Hole in the Sky

- IGN walkthrough: [Hole in the Sky](https://www.ign.com/wikis/cyberpunk-2077/Hole_in_the_Sky)
- Vanilla type: `MainQuest`
- Quest hash: `2713613091`
- Quest path: `ep1/quests/main_quest/q301_finding_myers`
- District: Pacifica
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`, `hack/breach/download`, `combat/neutralize`

### Journal premise

Songbird. Real pretty handle for the lethal netjock who just blasted into the Relic from a hijacked plane. Which just crash landed in that dump called Dogtown. Go on li'l soldier, run along and rescue NUS President Rosalind Myers. Assumin' it's not too late. If I missed anything, it's 'cause I'm busy writin' all this shit down for posterity – I don't like our chances here one bit.

### Objective sequence

1. **Go to the crash site.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/00_way_to_crashsite/reach_crashsite`
   - Map pin: ref `#q301_mp_crashsite_bottom`; position `-2013.0998535156, -2688.1628417969, 37.430011749268`
2. **Jump down the chute.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/00_way_to_crashsite/trash_chute`
   - Map pin: ref `#q301_mp_way_to_crashsite_chute`; position `-1408.6370849609, -2262.591796875, 131.51898193359`
3. **Get on the bike.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/00_way_to_crashsite/take_bike`
   - Map pin: ref `#q301_mp_way_to_crashsite_bike_hacking`; position `-1621.2687988281, -2462.08984375, 40.525096893311`
4. **Get off the bike.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/00_way_to_crashsite/unmount_bike`
5. **Get onto the crane arm.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/climb_crane`
   - Map pin: ref `#q301_mp_crashsite_crane_arm`; position `-2104.2329101563, -2662.4758300781, 90.84001159668`
6. **Follow the construction worker.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/constr_worker_follow`
7. **Talk to the construction worker.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/constr_worker_talk`
8. **Go to the crane.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/reach_crane`
   - Map pin: ref `#q301_mp_crashsite_crane`; position `-2100.4987792969, -2662.5930175781, 87.790008544922`
   - Map pin: ref `#q301_mp_crashsite_ladder`; position `-2098.9455566406, -2658.9328613281, 69.940010070801`
   - Map pin: ref `#q301_mp_crashsite_scaffolding`; position `-2081.3095703125, -2694.54296875, 45.680011749268`
   - Map pin: ref `#q301_mp_crashsite_scaffolding_02`; position `-2093.7497558594, -2679.3635253906, 51.360012054443`
9. **Hack the AV using your personal link.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/hack_av`
10. **Go to the wreckage.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/reach_shuttle`
   - Map pin: ref `#q301_mp_crashsite_broken_crane`; position `-2210.91015625, -2723.35546875, 66.860015869141`
   - Map pin: ref `#q301_mp_crashsite_crane_hole`; position `-2115.1088867188, -2667.8720703125, 91.077125549316`
   - Map pin: ref `#q301_mp_crashsite_shuttle_entrance`; position `-2293.8686523438, -2773.3537597656, 51.839008331299`
11. **Hack the mech using your personal link.**  
   `Optional` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/hack_mech`
12. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/01_crashsite/talk_songbird`
   - Map pin: ref `#q301_mp_crashsite_crane_hack`; position `-2105.7094726563, -2664.1928710938, 90.670013427734`
13. **Open the door.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/02_shuttle/arrival_door`
   - Map pin: ref `#q301_mp_crashsite_shuttle_open_door`; position `-2269.6713867188, -2759.5869140625, 51.940013885498`
   - Map pin: ref `#q301_mp_crashsite_shuttle_open_door`; position `-2269.6713867188, -2759.5869140625, 51.940013885498`
14. **Enter the wreckage.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/02_shuttle/arrival_enter_shuttle`
15. **Find Rosalind Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/02_shuttle/arrival_survivors`
16. **Talk to President Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/02_shuttle/arrival_talk_myers`
17. **Defeat the attackers.**  
   `Primary` · `ep1/quests/main_quest/q301_finding_myers/02_shuttle/combat_defeat_enemies`

## I Walk the Line

- IGN walkthrough: [I Walk the Line](https://www.ign.com/wikis/cyberpunk-2077/I_Walk_the_Line_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2217802542`
- Quest path: `quests/main_quest/act_01/q110_voodoo`
- District: Pacifica
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **I'm sick of this Placide motherfucker as much as you, but at least the fog has lifted, the goal is clear. You find a netrunner in the GIM and the Voodoo goons will set up a meet-n-greet with their queen. Pros? Maybe I'll actually get to see a legit netrunner, 'cause it's sure starting to feel like an extinct species these days. Someone who's got the guts to square off against the Voodoos has given me some hope, at least. But the cons? Damn near any minute your brain could start dripping out your ears. Afraid we won't have time to make pilgrimmages to the monuments of Pacifica's Golden Age.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/01_exit_the_hotel`
   - Map pin: ref `#q110_mp_netrunners_den_back_elevator_room`; position `-1882.1378173828, -1871.7698974609, 58.972541809082`
   - Map pin: ref `#q110_mp_netrunners_den_back_exit`; position `-1863.4848632813, -1875.0810546875, 44.619995117188`
   - Map pin: ref `#q110_mp_netrunners_den_exit_lift`; position `-1877.0062255859, -1879.7650146484, 58.93155670166`
   - Map pin: ref `#q110_mp_netrunners_den_exit_lift_panel`; position `-1877.1442871094, -1877.0822753906, 59.204566955566`
   - Map pin: ref `#q110_mp_netrunners_den_exit_lift_panel_inside`; position `-1875.3713378906, -1878.6026611328, 59.138809204102`
   - Map pin: ref `#q110_mp_netrunners_den_front_staircase`; position `-1924.8642578125, -1904.10546875, 58.658290863037`
2. **Meet with Placide's people.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/01b_meet_placides_men`
   - Map pin: ref `#q110_mp_voodoo_boy_lookout`; position `-2231.0197753906, -2242.8120117188, 13.349418640137`
3. **Talk to Placide's people.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/01c_talk_to_voodoo_boy`
   - Map pin: ref `#q110_mp_voodoo_boy_lookout`; position `-2231.0197753906, -2242.8120117188, 13.349418640137`
4. **Enter the mall.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/02_get_inside_the_mall`
   - Map pin: ref `#q110_mp_mall_back_entrance`; position `-2393.12890625, -2054.7685546875, 11.456039428711`
   - Map pin: ref `#q110_mp_mall_garage_entrance`; position `-2351.1831054688, -2190.591796875, 13.275085449219`
5. **Follow Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/03_follow_placide`
6. **Find the van in the lobby.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/03_locate_the_truck`
   - Map pin: ref `#q110_mp_gym_corridor`; position `-2386.4772949219, -2037.4360351563, 15.18132019043`
7. **Reach the van.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/03a_get_to_truck`
   - Map pin: ref `#q110_mp_truck`; position `-2285.8120117188, -2060.8930664063, 15.969047546387`
   - Map pin: ref `#q110_mp_truck`; position `-2285.8120117188, -2060.8930664063, 15.969047546387`
8. **Deal with the enemies near the van.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/03b_eliminate_hostiles_near_truck`
   - Map pin: ref `#q110_mp_truck`; position `-2285.8120117188, -2060.8930664063, 15.969047546387`
9. **Connect to the van.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/04_inflitrate_the_truck`
10. **Talk to Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/04_talk_to_placide`
11. **Find the agent in the cinema.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05_find_netwatch_agent`
   - Map pin: ref `#q110_mp_agent_ad_hacking_001`; position `-2292.3352050781, -2036.3594970703, 16.489845275879`
   - Map pin: ref `#q110_mp_agent_ad_hacking_002`; position `-2252.9172363281, -2054.8908691406, 22.03369140625`
   - Map pin: ref `#q110_mp_agent_gate_hacking_ui_001`; position `-2271.7709960938, -2062.1782226563, 16.276000976563`
   - Map pin: ref `#q110_mp_agent_gate_hacking_ui_002`; position `-2270.8344726563, -2071.3247070313, 17.253509521484`
   - Map pin: ref `#q110_mp_agent_in_cinema`; position `-2303.7885742188, -1971.7990722656, 23.801788330078`
   - Map pin: ref `#q110_mp_elevator_shaft_stealth`; position `-2293.625, -2100.6044921875, 21.735046386719`
   - Map pin: ref `#q110_mp_agent_cinema_lobby`; position `-2266.9782714844, -2011.1885986328, 21.297439575195`
   - Map pin: ref `#110_mp_placide_gate_hacking`; position `-2296.3752441406, -2043.8596191406, 16.607749938965`
   - Map pin: ref `#q110_mp_after_bossfight_shutter_opening_001`; position `-2276.7763671875, -1988.3332519531, 22.150405883789`
   - Map pin: ref `#q110_mp_after_bossfight_shutter_opening_002`; position `-2282.4645996094, -1993.4270019531, 22.150405883789`
   - Map pin: ref `#q110_mp_agent_gate_hacking_ui_001`; position `-2271.7709960938, -2062.1782226563, 16.276000976563`
12. **Deal with Sasquatch.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05a_kill_animals_boss`
13. **Confront the agent.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05b_talk_to_agent`
   - Map pin: ref `#q110_mp_agent_in_cinema_confront`; position `-2311.0202636719, -1976.2652587891, 23.685241699219`
14. **Confront the netrunner.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05c_talk_to_netrunner`
15. **Jack into the agent.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05d_jack_into_agent`
16. **Take the shard.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05e_take_shard`
17. **Talk to the agent.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/03_mall_job/05f_talk_to_netrunner`
18. **Leave the Grand Imperial Mall.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/00_leave_the_mall`
   - Map pin: ref `#q110_mp_mall_exit`; position `-2273.2358398438, -2105.5478515625, 14.073165893555`
19. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/00_talk_to_johnny`
20. **Talk to Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/00b_talk_to_placide`
21. **Head to Batty's Hotel.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01_go_to_netrunners_den`
   - Map pin: ref `#q110_mp_netrunners_den_front_staircase`; position `-1924.8642578125, -1904.10546875, 58.658290863037`
22. **Meet with Placide's people.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01b_meet_placides_men`
23. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01b_talk_to_brigitte`
24. **Talk to the guards.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01b_talk_to_guards`
25. **Get into the back seat.**  
   `Optional` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01c_fastravel_to_netrunners_den1`
26. **Get into the back seat.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01c_fastravel_to_netrunners_den`
27. **Meet with Placide in Batty's Hotel.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/01c_meet_placide`
   - Map pin: ref `#q110_mp_confrontation_room_entrance`; position `-1899.4405517578, -1888.8333740234, 59.002254486084`
28. **Talk to Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/02_talk_to_placide`
29. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_voodoo/04_confrontation/02a_talk_to_brigitte`

## I've Seen That Face Before

- IGN walkthrough: [I've Seen That Face Before](https://www.ign.com/wikis/cyberpunk-2077/I%27ve_Seen_That_Face_Before_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1960400309`
- Quest path: `ep1/quests/main_quest/q304_netrunners`
- District: Pacifica
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `vehicle sequence`, `leave/escape area`

### Journal premise

So, plan is to dupe an ex-military, international arms mogul in his own house. First, just gotta abduct and impersonate a pair of pro criminal 'runners specializin' in the long-lost secrets of cyberspace... Sound too easy? Good, 'cause they're makin' ya do it from inside a locked trunk. Nova, right?

### Objective sequence

1. **Wait for the signal from Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/00_wait_for_reed`
2. **Call Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/00b_call_reed`
3. **Go to the Dogtown entrance.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/01_go_to_border`
   - Map pin: ref `#q304_mp_combat_zone_entrance`; position `-1908.4705810547, -2470.0466308594, 35.783542633057`
4. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/01b_talk_to_reed`
5. **Go to the vantage point.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/02_go_to_vantage_point`
   - Map pin: ref `#q304_mp_cz_entrance_vantage_point`; position `-1908.7652587891, -2443.6428222656, 50.610542297363`
6. **Wait for the netrunners' car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/03_wait`
7. **Scan vehicles at the intersection.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/04_scan_incoming_cars`
8. **Intercept the netrunners' car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/03c_cz_border/05_follow_the_netrunner_car`
9. **Call Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/01_call_reed`
10. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/02_talk_to_reed`
11. **Scan vehicles to find the netrunners' car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/02b_go_to_parking_lot`
12. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/02c_talk_to_reed`
13. **Go to the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/02d_get_close_to_the_car`
14. **Return to the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/02e_return_to_the_car`
15. **Scan the IDs of passing vehicles to find the netrunners car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/03_scan_cars`
16. **Open the trunk.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/04_open_the_car`
17. **Check the cameras.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/04b_check_the_cameras`
18. **Get in the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/05_get_into_the_car`
19. **Wait for the right moment to take control of the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/06_wait`
20. **Take control of the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/06b_take_control_of_the_car`
21. **Drive to the meeting point.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/06c_drive_to_the_ambush`
   - Map pin: ref `#q304_mp_to_ambush_point`; position `-2091.37109375, -2643.8295898438, 25.126949310303`
   - Map pin: ref `#q304_mp_to_roundabout`; position `-1694.8397216797, -2353.8400878906, 39.509998321533`
22. **Get out of the trunk.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/07b_get_out_of_the_trunk`
23. **Get in the car.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/07c_sit_in_the_car`
24. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/08_talk_to_reed`
25. **Put on the netrunner's outfit.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/08b_put_on_outfit`
   - Map pin: ref `#q304_mp_netrunners_outfit`; position `-2081.2502441406, -2652.5219726563, 24.893848419189`
26. **Download Cynosure mainframe access codes from Aurore.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/08bb_download_firmware_key`
27. **Activate the behavioral imprint.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/08d_insert_shard`
28. **Talk to Alex and Reed.**  
   `Primary` · `ep1/quests/main_quest/q304_netrunners/04_entering_stadium/09b_talk_to_alex`

## Knockin' on Heaven's Door

- IGN walkthrough: [Knockin' On Heaven's Door](https://www.ign.com/wikis/cyberpunk-2077/Knockin%27_On_Heaven%27s_Door_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `929099020`
- Quest path: `quests/main_quest/act_01/q115_rogues_last_flight`
- District: City Center / Corpo Plaza
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`

### Objective sequence

1. **Worst is behind us now. Rogue was shaking worse than all those corpodicks put together, I could tell. But she still said yes in the end. We're going back to Arasaka Tower and this time… we finish things right. We'll cut Alt loose in the Tower's system and she'll punch our ticket to Mikoshi. Fuck, how I wish you could see it!**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/03_jump/00_fly`
2. **Jump from the AV.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/03_jump/01_jump_out`
3. **Talk to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/00_talk_to_rogue`
4. **Help Rogue rescue Weyland.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/02b_help_rogue_with_weyland`
5. **Defeat the commanding officer.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/06_takedown_commander`
6. **Search the officer's body.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/07_loot_commander`
7. **Get in the elevator.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/08_get_to_elevator`
   - Map pin: ref `#q115_mp_jungle_elevator_terminal`; position `-1386.3325195313, 163.28321838379, 327.85653686523`
8. **Return to Rogue.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/02c_return_to_rogue`
9. **Talk to Rogue.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/02d_talk_rogue`
10. **Take down one of the guards.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/02e_takedown_first_guards`
11. **Find the commanding officer.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/01_find_commander`
   - Map pin: ref `#q115_mp_jungle_commander`; position `-1442.3912353516, 194.82815551758, 328.56796264648`
12. **Take down one of the guards.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/06b_takedown_commander`
13. **Wait for Rogue and Weyland.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/08b_wait_rogue_weyland`
   - Map pin: ref `#q115_mp_jungle_elevator_terminal`; position `-1386.3325195313, 163.28321838379, 327.85653686523`
14. **Take the elevator to the atrium.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/09_take_elevator_down`
   - Map pin: ref `#q115_mp_jungle_elevator_terminal`; position `-1386.3325195313, 163.28321838379, 327.85653686523`
15. **Follow Rogue.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/02_follow_rogue`
16. **Talk to Rogue.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/03_talk_rogue`
17. **Take down one of the guards.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/04_takedown_av_guard`
18. **Talk to Rogue and Weyland.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/05_talk_weyland`
19. **Follow Rogue.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/06c_follow_rogue_to_commander`
20. **Jump down the elevator shaft.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/10_jump_down_shaft`
   - Map pin: ref `#q115_marker_jungle_elevator`; position `-1386.3803710938, 162.2534942627, 329.04598999023`
21. **Open the elevator hatch.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/11_get_in_elevator`
22. **Jump into the elevator.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/04_jungle/12_jump_into_elev`
23. **Follow Rogue.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/0000_follow_rogue`
24. **Get to the atrium.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/000_atrium`
   - Map pin: ref `#q115_mp_atrium_top`; position `-1436.1058349609, 103.22324371338, 291.3459777832`
25. **Reach the security level.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/00_get_down`
   - Map pin: ref `#q115_mp_atrium_bottom`; position `-1447.3905029297, 77.20622253418, 243.34599304199`
   - Map pin: ref `#q115_mp_atrium_bottom_jump`; position `-1447.2709960938, 80.019416809082, 256.94589233398`
   - Map pin: ref `#q115_mp_atrium_jump_point_000a`; position `-1457.6079101563, 98.94108581543, 292.49618530273`
   - Map pin: ref `#q115_mp_atrium_jump_point_000b`; position `-1455.6240234375, 97.269577026367, 279.3479309082`
   - Map pin: ref `#q115_mp_atrium_jump_point_001a`; position `-1434.6323242188, 97.943473815918, 280.48190307617`
   - Map pin: ref `#q115_mp_atrium_jump_point_001b`; position `-1436.1650390625, 96.279113769531, 267.34799194336`
   - Map pin: ref `#q115_mp_atrium_jump_point_002a`; position `-1457.3474121094, 99.077499389648, 268.63040161133`
   - Map pin: ref `#q115_mp_atrium_jump_point_002b`; position `-1456.0372314453, 97.111679077148, 255.34799194336`
26. **Get to the security room.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/01_security_room`
   - Map pin: ref `#q115_mp_atrium_security`; position `-1457.0594482422, 126.80337524414, 243.34599304199`
27. **Open the server room doors.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/02_lockdown`
28. **Connect Alt to the system.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/02b_connect_alt`
   - Map pin: ref `#q115_mp_alt_tag_000`; position `-1456.3913574219, 140.15560913086, 244.65016174316`
   - Map pin: ref `#q115_mp_alt_tag_001`; position `-1466.9071044922, 135.69023132324, 244.61047363281`
   - Map pin: ref `#q115_mp_alt_tag_002`; position `-1461.4399414063, 131.20141601563, 244.94866943359`
   - Map pin: ref `#q115_mp_alt_tag_003`; position `-1456.8460693359, 124.45234680176, 244.67666625977`
   - Map pin: ref `#q115_mp_alt_tag_004`; position `-1464.2856445313, 125.41186523438, 244.5267791748`
   - Map pin: ref `#q115_mp_alt_tag_005`; position `-1468.0399169922, 124.75978088379, 245.2306060791`
   - Map pin: ref `#q115_mp_alt_tag_006`; position `-1462.1082763672, 118.55736541748, 244.48393249512`
   - Map pin: ref `#q115_mp_alt_tag_007`; position `-1458.0588378906, 118.38537597656, 244.48393249512`
   - Map pin: ref `#q115_mp_alt_tag_008`; position `-1467.4266357422, 115.49096679688, 244.48393249512`
29. **Get to the elevator.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/03_elevator`
   - Map pin: ref `#q115_mp_alt_tag_010`; position `-1447.3516845703, 68.707504272461, 245.04907226563`
   - Map pin: ref `#q115_mp_alt_tag_011`; position `-1438.0333251953, 146.37699890137, 238.41078186035`
   - Map pin: ref `#q115_mp_alt_tag_012`; position `-1442.3956298828, 184.57666015625, 238.5951385498`
   - Map pin: ref `#q115_mp_alt_tag_009`; position `-1465.6719970703, 108.567527771, 244.48393249512`
   - Map pin: ref `#q115_mp_atrium_elevator`; position `-1442.4444580078, 182.63290405273, 238.22541809082`
30. **Take the elevator to the netrunner's nest.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/05_atrium/04_take_elevator`
   - Map pin: ref `#q115_mp_atrium_elevator_terminal`; position `-1441.3568115234, 184.20010375977, 238.62716674805`
31. **Get to Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/00_access_mikoshi`
32. **Open the gate.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/00b_wait_for_alt`
   - Map pin: ref `#q116_mp_open_gate`; position `-1407.2750244141, 145.1993560791, -24.96167755127`
33. **Defeat Adam Smasher.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/01_defeat_adam`
34. **Get to the Mikoshi Access Point.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/03_go_to_access`
   - Map pin: ref `#q116_mp_mikoshi_access`; position `-1301.1682128906, 140.60104370117, -25.506830215454`
35. **Talk to Weyland.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/04b_talk_to_weyland`
36. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/04_talk_to_alt`
37. **Decide Adam Smasher's fate.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/02_decide_adam`
38. **Connect to Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/05_jack_in`
   - Map pin: ref `#q116_mp_mikoshi_access`; position `-1301.1682128906, 140.60104370117, -25.506830215454`
39. **Pick up Rogue's gun.**  
   `Optional` · `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/02b_rogue_gun`

## Last Caress

- IGN walkthrough: [Last Caress](https://www.ign.com/wikis/cyberpunk-2077/Last_Caress_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1104352978`
- Quest path: `quests/main_quest/act_01/q113_rescuing_hanako`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **That's all, folks! Little Johnny can go to sleep while the grown-ups fix their big ol' mess. All I know's that you cut a deal with Arasaka – you help Hanako knock Yorinobu off his pedestal in return for help with the Relic. You already know where I stand. You've got better things to dream about then a rockerboy's mad ravings. Just make sure this little dream of yours doesn't turn into a nightmare.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/00_to_estate/06_drive_to_estate`
2. **Deal with the guards.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/00_to_estate/06b_deal_guard`
3. **Talk to Hellman.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/00_to_estate/06c_hellman`
4. **Talk to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/00_to_estate/06d_hanako`
5. **Exit the car.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/00_to_estate/07_get_out`
6. **Head to the estate.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/00_enter_estate`
   - Map pin: ref `#q113_mp_estate`; position `294.84359741211, 1030.2742919922, 230.60797119141`
7. **Find Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/01_find_hanako`
8. **Neutralize the elite guards.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/01b_defeat_guards`
9. **Neutralize the rest of the guards.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/01c_defeat_rest`
10. **Talk to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/02_talk_hanako`
11. **Follow Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/02b_follow_hanako`
12. **Enter the AV.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/03_get_in_av`
13. **Follow Takemura.**  
   `Optional` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/01d_takemura`
14. **Fly to Arasaka Tower.**  
   `Primary` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/04_fly_to_arasaka`
15. **Take down one of the guards.**  
   `Optional` · `quests/main_quest/act_01/q113_rescuing_hanako/01_estate/01d2_takedown`

## Leave in Silence

- IGN walkthrough: [Leave in Silence](https://www.ign.com/wikis/cyberpunk-2077/Leave_in_Silence_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1431760905`
- Quest path: `ep1/quests/main_quest/q305_border_crossing`
- District: Southern Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `wait/time gate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Well, you've gone and got her. The netrunner-agent-friend-traitor-chick who bet on herself, fought against all odds and lost it all... Who was Songbird, really? Who was she to you? I think I already know the answer. In a second you'll hand her over to Myers and her entourage of suits. You won, great teamwork - and for what? What price'll you pay for your reward? You think you've already paid it? C'mon, V. We know each other enough by now. We both know things'll only get more complicated.

### Objective sequence

1. **Ride to the border with Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/01_drive_to_border`
2. **Get out of the car.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/02_exit_vehicle`
3. **Approach Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/02b_approach_reed`
4. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/03_walk_with_songbird`
5. **Carry Songbird from the car.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/04_1_take_songbird_out_of_car`
6. **Take Songbird's body from the car.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/04_take_songbirds_corpse`
7. **Carry Songbird to the stretcher.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/05_carry_songbirds_corpse`
8. **Wait for the surgeons to take Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/05b_observe`
9. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/06_talk_to_myers`
10. **Place Songbird on the stretcher.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/07_place_corpse_on_stretcher`
11. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/09_talk_to_reed`
12. **Sit next to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/09b_sit_reed`
13. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/10_talk_to_johnny`
14. **Watch Myers' departure.**  
   `Primary` · `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/11_wait_for_them_to_leave`

## Life During Wartime

- IGN walkthrough: [Life During Wartime](https://www.ign.com/wikis/cyberpunk-2077/Life_During_Wartime_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3809244301`
- Quest path: `quests/main_quest/act_01/q104_02_av_chase`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Go back to the car.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/back_car`
2. **Finally doing things my way: we grab that 'Saka son-of-a-bitch by his corposuit collar, leave a bloody trail of destruction in our wake. Toss in a swipe at Kang Tao, too. Look at you, V. Just might make something of you yet. Anyway, one thing's for sure – we're close. Sure hope Hellman spills what he's got. And that what he's got is answers.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/chase_av`
3. **Finally doing things my way: we grab that 'Saka son-of-a-bitch by his corposuit collar, leave a bloody trail of destruction in our wake. Toss in a swipe at Kang Tao, too. Look at you, V. Just might make something of you yet. Anyway, one thing's for sure – we're close. Sure hope Hellman spills what he's got. And that what he's got is answers.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones`
4. **Finally doing things my way: we grab that 'Saka son-of-a-bitch by his corposuit collar, leave a bloody trail of destruction in our wake. Toss in a swipe at Kang Tao, too. Look at you, V. Just might make something of you yet. Anyway, one thing's for sure – we're close. Sure hope Hellman spills what he's got. And that what he's got is answers.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/drive_canyon`
5. **An AV full of corpo-rats drowned in the dust and sand – a beautiful sight. Sucks for the nomads though, especially Panam. Looks like our dame keeps losing everything she loves. Correction – almost everything. In other news, Hellman's surely shitting his pants knowing that the game's up. He's all yours. Just be careful – those Kang Tao pissheads won't be going down without a fight.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/follow_av`
6. **An AV full of corpo-rats drowned in the dust and sand – a beautiful sight. Sucks for the nomads though, especially Panam. Looks like our dame keeps losing everything she loves. Correction – almost everything. In other news, Hellman's surely shitting his pants knowing that the game's up. He's all yours. Just be careful – those Kang Tao pissheads won't be going down without a fight.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/panam_patch`
7. **Find the AV.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/av_chase/track_av`
   - Map pin: ref `#q104_mp_av_crash`; position `-669.65368652344, -5006.2924804688, 74.518096923828`
8. **Follow the Kang Tao's tracks.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks`
   - Map pin: ref `#q104_mp_airstrip_tracks_000`; position `-1276.7955322266, -5208.8735351563, 83.391036987305`
   - Map pin: ref `#q104_mp_airstrip_tracks_001`; position `-1358.8140869141, -5158.419921875, 82.978057861328`
   - Map pin: ref `#q104_mp_airstrip_tracks_002`; position `-1422.2509765625, -5102.3383789063, 82.978057861328`
   - Map pin: ref `#q104_mp_airstrip_tracks_003`; position `-1444.3626708984, -5034.5947265625, 82.916633605957`
   - Map pin: ref `#q104_mp_airstrip_tracks_004`; position `-1479.6962890625, -5022.6127929688, 83.04174041748`
9. **Call Takemura.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/call_takemura`
10. **Take Anders outside.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/carry_haru_outside`
   - Map pin: ref `#q104_mp_carry_anders_out`; position `-1841.5018310547, -4300.2451171875, 74.120002746582`
11. **Confront Hellman.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/confront_anders`
12. **Take out the turret.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/deal_av_turret`
13. **Defeat the Kang Tao operatives.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/defeat_gas_station`
14. **Disconnect from the drone.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/disconnect_drone`
15. **Find Anders Hellman.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/find_courier`
16. **Find Hellman at the gas station.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/find_courier_gas`
17. **Get to the upper floor of the gas station to find Hellman.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/find_courier_gas_precise`
18. **Follow Panam to the gas station.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_pan_gas`
19. **Follow Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_panam`
20. **Follow Kang Tao.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks`
   - Map pin: ref `#q104_mp_tracks_to_airstrip_000`; position `-754.00921630859, -5046.4755859375, 79.416915893555`
   - Map pin: ref `#q104_mp_tracks_to_airstrip_001`; position `-876.638671875, -5095.7983398438, 80.170455932617`
   - Map pin: ref `#q104_mp_tracks_to_airstrip_002`; position `-997.23895263672, -5135.1440429688, 83.368453979492`
   - Map pin: ref `#q104_mp_tracks_to_airstrip_003`; position `-1139.2567138672, -5184.0712890625, 86.243682861328`
   - Map pin: ref `#q104_mp_tracks_to_airstrip_004`; position `-1266.6323242188, -5194.169921875, 83.564476013184`
21. **Follow the next set of Kang Tao tracks.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_001`; position `-1500.9505615234, -4992.73046875, 78.977180480957`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_002`; position `-1466.8748779297, -4898.6240234375, 76.257591247559`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_003`; position `-1450.7932128906, -4816.5546875, 73.437591552734`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_004`; position `-1438.1026611328, -4722.7412109375, 70.820930480957`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_005`; position `-1441.2901611328, -4636.552734375, 69.326728820801`
   - Map pin: ref `#q104_mp_tracks_to_gas_station_006`; position `-1483.4501953125, -4528.8637695313, 66.895843505859`
22. **Go to the gas station with Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/gas_station_vantage_point`
   - Map pin: ref `#q104_mp_gas_station`; position `-1759.8286132813, -4315.5966796875, 82.56534576416`
23. **Talk to Mitch.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_info_from_mitch`
24. **Get in the AV.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_inside_av`
   - Map pin: ref `#q104_mp_av_door`; position `-668.08441162109, -5008.7802734375, 71.147979736328`
25. **Get on the motorcycle.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_on_bike`
26. **Get on the motorcycle.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_on_bike_tracking`
27. **Defeat the Kang Tao operatives on the airstrip.**  
   `Optional` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao`
28. **Eliminate the Kang Tao pilot.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/kill_av_pilot`
29. **Defeat the Kang Tao operatives.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/kill_petrochem_av`
30. **Get on the motorcycle.**  
   `Optional` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_take_bike`
31. **Leave the room.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/leave_roadhouse`
   - Map pin: ref `#q104_mp_roadhouse_exit_ending`; position `1600.2662353516, -792.65289306641, 54.152996063232`
32. **Scan the crashed AV.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_turret`
33. **Scan the area for signs of the Aldecaldos.**  
   `Optional` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_aldecados`
34. **Scan the combat drones.**  
   `Optional` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_drones`
35. **Pick Hellman up.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/pickup_haru`
36. **Check out the crash site.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/recon_crashsite_w_panam`
37. **Talk to the pilot.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/resolve_hostage_situation`
38. **Scan the tracks.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/scan_tire_tracks`
39. **Talk to Hellman.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/talk_with_courier`
40. **Wait for Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/wait_panam`
41. **Scan the Kang Tao operatives.**  
   `Optional` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_zetatech`
42. **Scan the area for Mitch.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_mitch`
43. **Put Hellman down.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/put_haru_on_bike`
44. **Get inside the gas station.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/reach_gas_station`
   - Map pin: ref `#q104_mp_gas_station_building`; position `-1836.5678710938, -4269.4038085938, 74.024528503418`
45. **Knock Hellman out.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/subdue_haru`
46. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/talk_panam_gas_station`
47. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_02_av_chase/finding_courier/tracking_plan`

## Lightning Breaks

- IGN walkthrough: [Lightning Breaks](https://www.ign.com/wikis/cyberpunk-2077/Lightning_Breaks_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2185001813`
- Quest path: `quests/main_quest/act_01/q104_01_sabotage`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`

### Objective sequence

1. **Shoot the target using the turret.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/calibrate_turret`
2. **Take the passenger seat.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/car1`
3. **Go to the satwave power plant.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/drive`
4. **Go to the hill with Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/drive_panam_hill`
5. **Go to the satwave power plant.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/drive_plant`
6. **Get to the terminal.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/go_bottom_bunker1`
   - Map pin: ref `#q104_pplant_cooling_terminal_marker`; position `-195.30206298828, -2838.3259277344, 22.798517227173`
7. **Panam Palmer. Gotta say, I like her. Girl's got a pair – and clearly a plan, too. Let's see if it's enough to grab Hellman. Honestly, V, never thought I'd ride with the nomads again. I know, I know she left the Aldecaldos, but you can feel it too, can't you? Clan's in her blood and bones. In her heart. Don't think she'll let us down.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam`
   - Map pin: ref `#q104_mp_sunset_garage`; position `1706.1873779297, -755.859375, 49.80078125`
   - Map pin: ref `#q104_mp_wait_roadhouse`; position `1705.0899658203, -753.12994384766, 50.469997406006`
8. **Take out the power plant security.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security`
9. **Connect to Panam's car.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/plug_in`
10. **Shoot down the AV.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/shoot_av`
11. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam`
   - Map pin: ref `#q104_mp_sunset_garage`; position `1706.1873779297, -755.859375, 49.80078125`
12. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam1`
13. **Overheat the terminals.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/terminal_control`
14. **Wait for the AV.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/wait_for_av`
15. **Wait for Panam.**  
   `Primary` · `quests/main_quest/act_01/q104_01_sabotage/preparations/wait_for_panam`

## Love Like Fire

- IGN walkthrough: [Love Like Fire](https://www.ign.com/wikis/cyberpunk-2077/Love_Like_Fire_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `657461329`
- Quest path: `quests/main_quest/act_01/q101_01_firestorm`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`

### Journal premise

It often happens that our memories are superseded by people's stories. Someone presents us a beginning, middle and an end, and soon enough we start believing that we really were there – that WE did all those things. But who we are is built on the past, and the past is built on lies.\n\nIn 2023 Johnny Silverhand carried out an attack on Arasaka Tower. Fifty years later, those events became the memories of a certain V.

### Objective sequence

1. **Get in the helicopter.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/av_enter`
   - Map pin: ref `#q101_mp_enter_heli_backalley`; position `5694.1787109375, -1496.9002685547, 220.65914916992`
2. **Return to the rooftop.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/back_to_heli`
   - Map pin: ref `#q101_mp_back_to_heli_pre`; position `-1466.7884521484, 179.66299438477, 600.8095703125`
3. **Connect to the Access Point.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/connect_splinter`
   - Map pin: ref `#q101_mp_hidden_arasaka_ap`; position `-1504.7270507813, 168.69163513184, 600.81884765625`
4. **Get to the chopper!**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/enter_av`
5. **Find the elevator.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/follow_rogue`
6. **Follow Spider Murphy.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/follow_spider_murphy`
7. **Exit the helicopter.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/get_off_the_heli`
8. **Wait for the virus to upload into the network.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/hack_arasaka_ap`
   - Map pin: ref `#q101_mp_spider_hacking_icon1`; position `-1447.9239501953, 194.46290588379, 611.9453125`
   - Map pin: ref `#q101_mp_hidden_arasaka_ap`; position `-1504.7270507813, 168.69163513184, 600.81884765625`
9. **Talk to Kerry.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/kerry`
10. **Defeat the Arasaka guards.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/kill_arasakas_office`
11. **Defeat Arasaka's forces.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/kill_arasakas_rooftop`
12. **Defeat the Arasaka guards.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/kill_arasakas_stairs`
13. **Wait for the helicopter to descend.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/landing`
14. **Exit the elevator.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/leave_elevator`
15. **Grab the microphone.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/microphone`
   - Map pin: ref `#q101_mp_microphone`; position `5669.8798828125, -1535.4635009766, 215.23582458496`
16. **Deploy and arm the bomb in the elevator.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/place_bomb`
   - Map pin: ref `#q101_mp_place_bomb_elevator`; position `-1448.7955322266, 169.43222045898, 594.44458007813`
17. **Go outside.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/rooftop`
   - Map pin: ref `#q101_mp_backstage_door`; position `5701.0439453125, -1511.7390136719, 220.0470123291`
18. **Find an Access Point to the network.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/server`
   - Map pin: ref `#q101_mp_hidden_arasaka_ap`; position `-1504.7270507813, 168.69163513184, 600.81884765625`
19. **Shoot the elevator mechanism.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/shoot_cables`
   - Map pin: ref `#q101_mp_arasaka_elev_mechanism`; position `-1448.8146972656, 170.97200012207, 596.37225341797`
20. **Go on stage.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/stage`
   - Map pin: ref `#q101_mp_concert_stage`; position `5668.982421875, -1533.5554199219, 214.47265625`
21. **Tell Rogue about your plan.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/tell_rogue_plan`
22. **Wait.**  
   `Primary` · `quests/main_quest/act_01/q101_01_firestorm/johnny/wait_elevator`
   - Map pin: ref `#q101_mp_spider_hacking_elev_term`; position `-1448.7026367188, 172.55476379395, 595.75427246094`

## Lucretia My Reflection

- IGN walkthrough: [Lucretia My Reflection](https://www.ign.com/wikis/cyberpunk-2077/Lucretia_My_Reflection)
- Vanilla type: `MainQuest`
- Quest hash: `2021481073`
- Quest path: `ep1/quests/main_quest/q302_reed`
- District: Dogtown
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Ahhh, back to the land of the livin'… Shame Songbird was the price to pay. Think she really kicked the bucket? My gut tells me this fiasco's nothin' but a small setback, although my nose did catch the unmistakable whiff of a 'runner's deep-fried gray matter... Now all that's left is surviving NC's most twisted district while babysittin' Madam Prez herself... Shit, V, take on a simpler gig next time, would ya?

### Objective sequence

1. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/000_a_talk_to_myers`
2. **Open the container.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/000_help_myers`
   - Map pin: ref `#q302_mp_container_door`; position `-2065.8701171875, -2412.6203613281, -6.5199999809265`
3. **Find an entrance to the subway tunnels.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/00_find_entrance_to_tunnels`
4. **Cross the service tunnel.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/00a_dark_service_tunnel`
   - Map pin: ref `#q302_mp_service_tunnel`; position `-2155.4152832031, -2558.2153320313, -8.6199979782104`
   - Map pin: ref `#q302_mp_service_tunnel_exit`; position `-2178.3020019531, -2552.8549804688, -8.2199974060059`
5. **Exit the container through the roof hatch.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/00a_exit_container_roof`
   - Map pin: ref `#q302_mp_subway_container_exit`; position `-2081.7993164063, -2426.0795898438, -4.7599997520447`
6. **Clear a way to the service tunnel.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/00b_dark_service_tunnel_forklift`
7. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/02a_talk_to_johnny`
8. **Shut off the steam.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/03_subway/00b_light_find_valve`
9. **Take the Chimera's core.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/pick_the_core`
10. **Wipe the camera recordings.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/03_subway/00b_wipe_recording`
   - Map pin: ref `#q302_mp_wipe_data`; position `-2181.0302734375, -2527.4990234375, -7.4000000953674`
11. **Take the elevator to the 8th floor with Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/03_elevator`
12. **Find a way out of the tunnels.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/03_elevator1`
   - Map pin: ref `#q302_mp_light_way`; position `-2167.6896972656, -2494.08984375, -7.1199998855591`
   - Map pin: ref `#q302_mp_dark_way`; position `-2146.8894042969, -2514.7092285156, -7.5899996757507`
13. **Lead Myers out of the tunnels.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/03_elevator2`
   - Map pin: ref `#q302_mp_elevator_subway`; position `-2217.4997558594, -2543.4396972656, -1.7738137245178`
14. **Lead Myers through the subway tunnels.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/follow_myers`
   - Map pin: ref `#q302_mp_back_cart`; position `-2084.619140625, -2427.7883300781, -6.2199993133545`
   - Map pin: ref `#q302_mp_2nd_cart`; position `-2111.2800292969, -2442.4392089844, -6.6900000572205`
15. **Wait for Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/follow_myers1`
16. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/follow_myers2`
17. **Leave the room so Myers can change.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/03_subway/follow_myers3`
   - Map pin: ref `#q302_mp_outside_cob`; position `-2203.8952636719, -2532.5166015625, -1.7738132476807`
18. **Scan your surroundings to find a working battery.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02a_search_squot3`
19. **Remove the drone's battery.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02f_get_the_battery`
20. **Fix the gas installation.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/04_squot/02a_search_squot2`
   - Map pin: ref `#q302_mp_gas`; position `-2222.4812011719, -2556.3442382813, 81.624061584473`
21. **Scan to find a power source for the generator.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02g_scan_battery`
22. **Connect the battery.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02h_insert_the_battery`
23. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02h_talk_to_johnny`
24. **Restore power to the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03_elevator3`
   - Map pin: ref `#q302_mp_generator`; position `-2242.8498535156, -2565.0676269531, 81.725921630859`
25. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03c_talk_to_myers`
26. **Defeat the strangers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03d_get_rid_of_misfits`
27. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03d_talk_to_myers`
28. **Get rid of the bodies.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03e_throw_out_misfits`
29. **Scan the pipes.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/08_scan_the_pipes`
   - Map pin: ref `#q302_mp_water_pipe`; position `-2242.5004882813, -2549.1799316406, 81.69002532959`
30. **Pick up the bodies.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers13`
   - Map pin: ref `#q302_mp_dumpster`; position `-2227.2770996094, -2538.1677246094, 81.21280670166`
31. **Sit next to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers14`
   - Map pin: ref `#q302_mp_mattress`; position `-2222.6069335938, -2568.9379882813, 81.314361572266`
32. **Fix the water pump.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/04_squot/02a_search_squot1`
   - Map pin: ref `#q302_mp_water`; position `-2242.4916992188, -2551.2326660156, 81.860771179199`
33. **Talk to Taylor.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers11`
34. **Talk to Jacob.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers12`
35. **Find a way to restore power.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/02a_search_squot`
36. **Scan the generator.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03_elevator1`
   - Map pin: ref `#q302_mp_generator`; position `-2242.8498535156, -2565.0676269531, 81.725921630859`
37. **Open the door to the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/03_elevator2`
38. **Find where the pipes lead.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/08a_follow_the_pipes`
39. **Walk with Myers to the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers`
40. **Enter the hideout with Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers1`
41. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers10`
   - Map pin: ref `#q302_mp_mattress`; position `-2222.6069335938, -2568.9379882813, 81.314361572266`
42. **Talk to the strangers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers2`
43. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers3`
44. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers4`
45. **Join Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers5`
46. **Go to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers6`
47. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers7`
48. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers8`
49. **Defeat the strangers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/04_squot/follow_myers9`
50. **Enter Capitán Caliente.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/01b_enter_caliente`
   - Map pin: ref `#q302_mp_bar`; position `-1664.6622314453, -2442.2702636719, 40.075477600098`
51. **Follow the cables to the fusebox.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/05_bar/01d_follow_cables`
   - Map pin: ref `#q302_mp_fusebox`; position `-1718.6065673828, -2393.9604492188, 62.629943847656`
52. **Override the fusebox to open the door to Capitán Caliente.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/05_bar/01d_use_fusebox`
53. **Hack the generator to restore power.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/05_bar/01e_hack_generator`
54. **Scan around to find the power source.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/05_bar/01e_scan_power`
   - Map pin: ref `#q302_tr_caliente_interior`; position `-1669.9449462891, -2434.2868652344, 39.056964874268`
55. **Find an entrance to the Capitán Caliente restaurant.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/01c_get_inside_bar`
   - Map pin: ref `#q302_tr_caliente_main_entrance`; position `-1674.6395263672, -2427.990234375, 39.909996032715`
56. **Move the shelf.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/02a_move_shelf`
   - Map pin: ref `#q302_mp_caliente_shelve`; position `-1663.6014404297, -2449.1809082031, 41.143768310547`
57. **Head to the Capitán Caliente restaurant.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/03_elevator`
   - Map pin: ref `#q302_mp_bar`; position `-1664.6622314453, -2442.2702636719, 40.075477600098`
   - Map pin: ref `#q302_mp_exit_elevator`; position `-2217.7580566406, -2543.2592773438, 80.504081726074`
   - Map pin: ref `#q302_mp_squot_base_level`; position `-2218.4343261719, -2543.765625, 26.567798614502`
   - Map pin: ref `#q302_mp_squot_exit_building`; position `-2239.5495605469, -2563.90625, 26.567798614502`
   - Map pin: ref `#q302_mp_hallway`; position `-2239.9697265625, -2553.51953125, 80.300971984863`
   - Map pin: ref `#q302_mp_squot_exit_building_area`; position `-2082.8081054688, -2614.7268066406, 26.058841705322`
58. **Scan the area to find the old telephone.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/03_elevator1`
   - Map pin: ref `#q302_tr_caliente_interior`; position `-1669.9449462891, -2434.2868652344, 39.056964874268`
59. **Call the number: 0931.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/03_elevator2`
   - Map pin: ref `#q302_mp_phone`; position `-1662.9678955078, -2448.8742675781, 41.492195129395`
60. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/04_talk_on_phone`
61. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/05_talk_johnny`
62. **Answer the phone.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/05_bar/06_pick_up`
   - Map pin: ref `#q302_mp_phone`; position `-1662.9678955078, -2448.8742675781, 41.492195129395`
63. **Talk to the stranger.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/01_talk_reed`
64. **Go to the Black Thorton.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/01_talk_reed1`
65. **Get in the car.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/01_talk_reed2`
66. **Sit and wait for the meeting.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/02b_sit_and_wait`
   - Map pin: ref `#q302_mp_basketball_sit`; position `-1807.2614746094, -2725.0964355469, 73.483772277832`
67. **Go to the basketball court.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/03_elevator`
   - Map pin: ref `#q302_mp_basketball`; position `-1797.5600585938, -2722.990234375, 73.42000579834`
68. **Sit.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/03_elevator1`
   - Map pin: ref `#q302_mp_basketball_sit`; position `-1807.2614746094, -2725.0964355469, 73.483772277832`
69. **Wait.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06_basketball/03_wait`
70. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/01_talk_reed`
71. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/01_talk_reed1`
72. **Enter the car.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/01_talk_reed2`
73. **Defeat Hansen's soldiers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/02a_ambush`
74. **Reach the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/02d_get_to_squat`
   - Map pin: ref `#q302_mp_squat_entrance`; position `-2240.744140625, -2567.2341308594, 25.229698181152`
75. **Exit the car.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/03_leave`
76. **Ride with Reed to the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/03_wait`
77. **Wait.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/06a_ride/03_wait1`
78. **Enter the elevator with Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01_enter_elevator`
   - Map pin: ref `#q302_mp_squot_elevator_ground_floor`; position `-2218.08984375, -2543.6218261719, 25.200004577637`
79. **Take the elevator to the 8th floor.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01a_take_elevator`
   - Map pin: ref `#q302_mp_squot_elevator_ground_floor_panel`; position `-2219.3049316406, -2542.5759277344, 26.043048858643`
80. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01b_talk_to_reed`
81. **Talk to the homeless.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01c_talk_to_homeless`
82. **Talk to Jacob.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01d_talk_to_jacob`
83. **Lead Reed to the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/01e_lead_reed`
84. **Defeat Hansen's soldiers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/02a_search_squot`
85. **Enter the building with Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/03_elevator1`
   - Map pin: ref `#q302_mp_squot_elevator_ground_floor`; position `-2218.08984375, -2543.6218261719, 25.200004577637`
86. **Enter the hideout.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/03_elevator2`
   - Map pin: ref `#q302_mp_squot_meet_myers`; position `-2238.9521484375, -2555.3212890625, 81.46752166748`
87. **Talk to Myers and Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/04_talk_to_myers_and_reed`
88. **Lean against the table.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/05_lean_on_the_table`
   - Map pin: ref `#q302_mp_table`; position `-2233.5502929688, -2574.5202636719, 81.186882019043`
89. **Wait until Myers and Reed leave.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/06_wait_for_reed_to_leave`
90. **Exit the building.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/06a_leave_building`
   - Map pin: ref `#q302_mp_squot_elevator_ground_floor`; position `-2218.08984375, -2543.6218261719, 25.200004577637`
91. **Exit the elevator.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/06b_exit_the_elevator`
92. **Head back to the building near Elizabeth Kress Street.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/07_return_peaceful`
93. **Return to the hideout and help Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/08_return_hostile`
94. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/07_oath/follow_myers2`
95. **Leave the building.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/08_call/00_leave_squat`
96. **Look for extra gigs in Dogtown.**  
   `Optional` · `ep1/quests/main_quest/q302_reed/08_call/00_b_pursue_other_activities`
97. **Reply to Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/08_call/01_reply_message`
98. **Wait two days for Reed's phonecall.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/08_call/01_wait_call`
99. **Wait for a message from Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/08_call/01_wait_message`
100. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q302_reed/08_call/02_talk_reed`

## M'ap Tann Pèlen

- IGN walkthrough: [M'ap Tann Pelen](https://www.ign.com/wikis/cyberpunk-2077/M%27ap_Tann_Pelen_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3997108866`
- Quest path: `quests/main_quest/act_01/q110_01_voodooboys`
- District: Pacifica
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`

### Objective sequence

1. **Well, we know the Voodoo Boys were behind all this, so that's one step forward. Problem is, now we have to reach them somehow – two steps back. There are a lot of things to be found in Pacifica, just usually not what you're looking for. Good news is you already got your fixer: a man without a face to help you find this fart in the wind. Sounds like a fun fuckin' delight.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/01_fixer/01_call_fixer`
2. **Talk to Mr. Hands.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/01_fixer/02_talk_to_fixer`
3. **Keep busy until Mr. Hands calls back.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/01_fixer/02b_wait_for_fixer_to_call_back`
4. **Answer the call from Mr. Hands.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/01_fixer/03_answer_call_from_fixer`
5. **Talk to Mr. Hands.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/01_fixer/04_talk_to_fixer_about_details`
6. **Follow Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/01_follow_placide`
7. **Go to the chapel.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/01_go_to_chapel`
   - Map pin: ref `#q110_mp_chapel_altar`; position `-1741.1525878906, -1908.8250732422, 63.348213195801`
   - Map pin: ref `#q110_mp_chapel_entrance`; position `-1751.1016845703, -1930.3198242188, 62.992294311523`
8. **Wait for the church to reopen the next day.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/01b_wait_till_chapel_open`
9. **Meet with your contact at the altar.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/02_wait_for_sermon_to_end`
   - Map pin: ref `#q110_mp_chapel_altar`; position `-1741.1525878906, -1908.8250732422, 63.348213195801`
10. **Talk to the contact.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/03_talk_to_contact`
11. **Go to the butcher shop.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/06_go_to_butcher_shop`
   - Map pin: ref `#q110_butcher_shop_enterance`; position `-1818.2357177734, -1977.0598144531, 53.545269012451`
12. **Ask the vendor for Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/06b_talk_to_vendor`
13. **Look into the camera.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/06c_look_at_camera`
   - Map pin: ref `#q110_mp_butcher_shop_scan_camera`; position `-1822.0073242188, -1968.6439208984, 54.93383026123`
14. **Talk to the vendor.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/06d_talk_to_vendor`
15. **Find Placide in the back of the shop.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/07_look_for_placide`
16. **Talk to Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/08_talk_to_placide`
17. **Talk to Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/09_talk_to_placide`
18. **Sit.**  
   `Primary` · `quests/main_quest/act_01/q110_01_voodooboys/02_make_contact/09b_sit_down`
   - Map pin: ref `#q110_mp_placide_office_sit_down`; position `-1902.9285888672, -1889.3751220703, 58.596668243408`

## Never Fade Away

- IGN walkthrough: [Never Fade Away](https://www.ign.com/wikis/cyberpunk-2077/Never_Fade_Away_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `154780279`
- Quest path: `quests/main_quest/act_01/q108_johnny`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **You get nightmares, don't you V? The stubborn kind that keep coming back, night after night, like they wanna make sure you never forget a single detail, sight or touch? The kind where you can barely breathe because you know what comes next?\n\nYou ever get those? I know you do. So here – welcome to mine.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/01_concert/01_go_backstage`
2. **Talk to Kerry.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/01_concert/02_talk_with_kerry`
3. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/01_concert/03_talk_with_alt`
4. **Look for drugs.**  
   `Optional` · `quests/main_quest/act_01/q108_johnny/01_concert/04_look_for_drugs`
5. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/02_backalley/01_talk_with_alt`
6. **Protect Alt from the thugs.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/02_backalley/02_fight_thugs`
7. **Talk to the ripperdoc.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/03_ripperdoc/01_talk_with_ripper`
8. **Talk to Thompson.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/03_ripperdoc/02_talk_with_thompson`
9. **Leave the ripperdoc clinic.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/03_ripperdoc/03_walk_out`
   - Map pin: ref `#q108_mp_ripper_doors_exit`; position `-2277.2902832031, -639.74426269531, -102.24017333984`
10. **Go to the Atlantis.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/00_go_atlantis`
11. **Find Rogue.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/01_find_rogue`
12. **Talk to the bouncer.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/01b_talk_with_bouncer`
13. **Convince Rogue to help.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/02_convince_rogue_to_help`
14. **Sit next to Rogue.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/02a_sit_down`
   - Map pin: ref `#q108_14_ch_well_hello_there`; position `-747.01483154297, 1115.1011962891, 67.578330993652`
15. **Fight for your life.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/03_kill_arasaka`
16. **Fix the machine.**  
   `Optional` · `quests/main_quest/act_01/q108_johnny/04_atlantis/01c_help_vending_machine`
   - Map pin: ref `#q108_mp_vending_machine`; position `-750.14251708984, 1077.0142822266, 68.38646697998`
17. **Defeat the Arasaka agents.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/03a_defeat_agents`
18. **Escape from the Atlantis.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/04_follow_rogue`
19. **Ask around for Rogue.**  
   `Optional` · `quests/main_quest/act_01/q108_johnny/04_atlantis/01a_ask_aroud`
20. **Call the elevator.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/05a_call_lift`
   - Map pin: ref `#q108_mp_terminal_lift_atlantis_right`; position `-751.24987792969, 1107.0007324219, 62.479995727539`
21. **Enter the elevator.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/05b_enter_lift`
22. **Take the elevator down to the parking lot.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/05c_pick_parking`
   - Map pin: ref `#q108_mp_terminal_lift_atlantis_pick_floor`; position `-750.35992431641, 1106.8104248047, 62.479995727539`
23. **Wait for Santiago and Rogue.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/04_atlantis/05c_wait_for_others`
24. **Get in Johnny's Porsche.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/01_get_to_car`
25. **Get in Johnny's Porsche.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/01a_enter_car`
26. **Escape from the Arasaka agents.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/02_escape_atlantis`
27. **Defeat the Arasaka agents.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/02_protect_car`
28. **Down the Arasaka helicopter.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/02_protect_car1`
29. **Plan your next move.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/05_escape_from_atlantis/03_plan_action`
30. **Talk to the rest of the crew.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/00_talk_with_team`
31. **Find Alt.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/01_find_alt`
32. **Find the mainframe.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02_get_to_mainframe`
   - Map pin: ref `#q108_mp_mainframe_entrance`; position `-1462.4790039063, 160.47204589844, 210.10870361328`
   - Map pin: ref `#q108_mp_door_to_server_room_a`; position `-1417.8619384766, 172.88174438477, 207.74641418457`
   - Map pin: ref `#q108_mp_door_to_server_room_b`; position `-1419.5999755859, 131.50730895996, 207.77973937988`
   - Map pin: ref `#q108_mp_door_to_server_room_b3`; position `-1435.6958007813, 130.26858520508, 207.75810241699`
   - Map pin: ref `#q108_mp_door_to_server_room_c`; position `-1434.7320556641, 152.25720214844, 207.74908447266`
33. **Destroy the turret by the door to the mainframe.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02a_destroy_turret`
34. **Open the door to the mainframe.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02b_open_doors`
35. **Destroy the turret.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02c_destroy_turret`
36. **Take the explosives from Thompson.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02c_take_explosives`
37. **Plant the explosives.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02d_plant_explosives`
38. **Arm the explosives.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02e_arm_explosives`
39. **Get out of range.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/02e_move_away`
40. **Defeat the Arasaka agents.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/03_kill_toshiro`
41. **Check on Alt.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/04_check_on_alt`
42. **Unplug Alt.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/05_unplug_alt`
43. **Talk to Thompson.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/06_talk_thompson`
44. **Defeat the Arasaka agents.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/07_kill_reinforcements`
45. **Get ready to fight more enemies.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/06_arasaka_tower/07a_prepare_reinforcements`
46. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/07_finale/01_talk_with_johnny`
47. **Go back to the Voodoo Boys' BBS.**  
   `Primary` · `quests/main_quest/act_01/q108_johnny/07_finale/02_leave_to_bbs`

## Nocturne Op55N1

- IGN walkthrough: [Nocturne Op55N1](https://www.ign.com/wikis/cyberpunk-2077/Nocturne_Op55N1_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2639096790`
- Quest path: `quests/meta/02_sickness`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **We both knew this time would come. If we don't think of something quick, you will die – and I'll go with you. It's time for our final meeting.**  
   `Primary` · `quests/meta/02_sickness/q101_victor/01_find_a_way`
2. **Call Hanako.**  
   `Primary` · `quests/meta/02_sickness/q115/00_call_hanako`
3. **Talk to Hanako Arasaka.**  
   `Primary` · `quests/meta/02_sickness/q115/01_talk_with_hanako`
4. **Meet Hanako at Embers.**  
   `Primary` · `quests/meta/02_sickness/q115/02_meet_hanako`
   - Map pin: ref `#q115_mp_fancy_restaurant_elevator_bottom`; position `-1794.7518310547, -535.94818115234, 11.340503692627`
   - Map pin: ref `#q115_mp_fancy_restaurant_street`; position `-1790.1635742188, -481.79223632813, 12.228702545166`
   - Map pin: ref `#q115_mp_fancy_restaurant_elevator_terminal_bottom`; position `-1793.0300292969, -536.80798339844, 11.549812316895`
5. **Sit with Hanako Arasaka.**  
   `Primary` · `quests/meta/02_sickness/q115/03_sit_hanako`
6. **Talk to Hanako Arasaka.**  
   `Primary` · `quests/meta/02_sickness/q115/04_talk_hanako`
7. **Leave the restaurant.**  
   `Primary` · `quests/meta/02_sickness/q115/05_leave_restaurant`
   - Map pin: ref `#q115_mp_fancy_restaurant_elevator_top`; position `-1794.7521972656, -535.94866943359, 75.432563781738`
   - Map pin: ref `#q115_mp_fancy_restaurant_elevator_top_terminal`; position `-1793.0209960938, -536.80676269531, 75.392166137695`
8. **Talk to Johnny.**  
   `Primary` · `quests/meta/02_sickness/q115/06_talk_johnny`
9. **Reactivate the elevator.**  
   `Primary` · `quests/meta/02_sickness/q115/07_reactivate_elevator`
10. **Talk to Viktor.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/00_talk_johnny`
11. **Talk to Johnny.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/00b_talk_johnny`
12. **Leave Viktor's clinic.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_0_leave_ripperdoc`
   - Map pin: ref `#q115_mp_misty_shop`; position `-1543.3624267578, 1210.1396484375, 16.473239898682`
13. **Talk to Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_1_talk_to_misty`
14. **Take the pills.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_2_grab_inhalers`
15. **Follow Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_3_follow_misty`
16. **Take the elevator to the roof.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_3b_elevator`
   - Map pin: ref `#q115_mp_ripper_elevator_roof`; position `-1550.0556640625, 1204.8616943359, 17.199151992798`
17. **Follow Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_3c_follow`
18. **Sit by Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_4_sit`
   - Map pin: ref `#q115_mp_sit_next_to_misty`; position `-1541.1435546875, 1201.7796630859, 57.767807006836`
19. **Decide what comes next.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01_decide_johnny`
20. **Talk to Johnny.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/01b_talk_johnny`
21. **Talk to River.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/02a1_call_river`
22. **Talk to Kerry.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/02a2_call_kerry`
23. **Talk to Judy.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/02a3_call_judy`
24. **Talk to Panam.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/02a4_call_panam`
25. **Let Johnny take control.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/02b_let_johnny_take_over`
26. **Call Panam.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/03a_call_panam`
27. **Call Hanako Arasaka.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/03b_call_hanako`
28. **Talk to Panam.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/04a_talk_to_panam`
29. **Talk to Hanako Arasaka.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/04b_talk_to_hanako`
30. **Head to Misty's Esoterica.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/05_leave_roof`
   - Map pin: ref `#q115_mp_misty_shop`; position `-1543.3624267578, 1210.1396484375, 16.473239898682`
   - Map pin: ref `#q115_mp_ripperdoc_roof_terminal_top`; position `-1549.9822998047, 1204.9033203125, 54.188934326172`
31. **Talk to Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/06_talk_to_misty`
32. **Follow Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/07_follow_misty`
33. **Talk to Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/07b_talk_misty`
34. **Sit.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/08_sit_misty`
35. **Receive a tarot card reading.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/09_reading_chakras`
36. **Talk to Misty.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/10_get_up`
37. **Wait for Takemura to arrive.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/11a_wait_for_takemura`
38. **Wait for an agent of Hanako Arasaka to arrive.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/11b_wait_for_takemura_2`
39. **Wait for Panam to arrive.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/11c_wait_for_panam`
40. **Talk to Hellman and Takemura.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/12a_talk_takemura`
41. **Talk to Hellman.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/12b_talk_takemura_2`
42. **Talk to Panam.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/12c_talk_panam`
43. **Leave Misty's shop.**  
   `Primary` · `quests/meta/02_sickness/q115_ripperdoc/13_leave_misty`

## Play It Safe

- IGN walkthrough: [Play It Safe](https://www.ign.com/wikis/cyberpunk-2077/Play_It_Safe_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1510899217`
- Quest path: `quests/main_quest/act_01/q112_03_dashi_parade`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `combat/neutralize`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Go to the bazaar in Japantown.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05a_go_parade`
2. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05b2_talk_takemura`
3. **Reach the first sniper.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05c1_first_sniper`
4. **Reach the second sniper.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05c2_second_sniper`
5. **Reach the third sniper.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05c3_third_sniper`
6. **Neutralize the snipers.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05c_kill_snipers`
   - Map pin: ref `#q112_mp_parade_path_01`; position `-450.98361206055, 744.03869628906, 135.57670593262`
   - Map pin: ref `#q112_mp_parade_path_10`; position `-506.88806152344, 790.25793457031, 139.66390991211`
   - Map pin: ref `#q112_mp_parade_path_11`; position `-528.71197509766, 790.46490478516, 167.5686340332`
   - Map pin: ref `#q112_mp_parade_path_02`; position `-457.16799926758, 769.43524169922, 135.40989685059`
   - Map pin: ref `#q112_mp_parade_path_03`; position `-485.40417480469, 758.48529052734, 159.46273803711`
   - Map pin: ref `#q112_mp_parade_path_04`; position `-510.77752685547, 730.68908691406, 170.58596801758`
   - Map pin: ref `#q112_mp_parade_path_05`; position `-496.68377685547, 714.2314453125, 159.37376403809`
   - Map pin: ref `#q112_mp_parade_path_06`; position `-487.98223876953, 708.30456542969, 115.79709625244`
   - Map pin: ref `#q112_mp_parade_path_07`; position `-513.96899414063, 716.98999023438, 116.84926605225`
   - Map pin: ref `#q112_mp_parade_path_08`; position `-539.32568359375, 748.90045166016, 123.51958465576`
   - Map pin: ref `#q112_mp_parade_path_09`; position `-528.17596435547, 789.58483886719, 121.92758178711`
7. **Disconnect the netrunner from the net.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05d2_jack_out`
8. **Reach the netrunner.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05d_get_in_position`
9. **Connect to the Access Point.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05e_hack`
10. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05f3_talk_takemura_no_mp`
11. **Defeat Oda.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05f_fight_cyberninja`
12. **Deactivate the security turret.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05g2_security`
13. **Decide what to do with Oda.**  
   `Optional` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05f2_decide_oda`
14. **Wait for Takemura to make his move.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05h_support_takemura`
15. **Scan Hanako Arasaka to hack her signal.**  
   `Optional` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05g_take_over_phone`
16. **Since I obviously wasn't invited to Saburo Arasaka's funeral, I guess this sad little parade will have to do – I'm just missing confetti. But in all seriousness, Takemura must have a death wish. He's just gonna jump onto Hanako's platform? Be my fucking guest – we'll deal with the snipers. Meanwhile, keep an eye out for an escape route. This is gonna go all kinds of wrong – I can feel it.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05i_wait_call`
17. **Escape the parade grounds.**  
   `Primary` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05k_flee`
18. **Talk to Johnny.**  
   `Optional` · `quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05l_johnny`

## Playing for Time

- IGN walkthrough: [Playing for Time](https://www.ign.com/wikis/cyberpunk-2077/Playing_for_Time_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1336846915`
- Quest path: `quests/main_quest/act_01/q101_resurrection`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Journal premise

Well, broder, looks like we got ourselves into a real fix. No chance in hell I'm wriggling myself out of this one, but you're still alive. And as Misty says, "As long as you're alive, there's hope." Fate's given you a second chance, so use it – get back on your feet. Do that, and consider your best friend's last wish fulfilled.

### Objective sequence

1. **Approach the stranger.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/cyberspace_approach`
2. **Look for a way out.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/cyberspace_way_out`
   - Map pin: ref `#q101_mp_whiteroom_mp1`; position `-1273.5147705078, 1589.7458496094, -577.50122070313`
   - Map pin: ref `#q101_mp_whiteroom_mp3`; position `-1254.8579101563, 1583.5457763672, -572.50024414063`
   - Map pin: ref `#q101_mp_whiteroom_mp_l2`; position `-1259.4677734375, 1604.2528076172, -575.45721435547`
   - Map pin: ref `#q101_mp_whiteroom_mp_r2`; position `-1270.671875, 1569.5548095703, -575.45721435547`
3. **Check your email.**  
   `Optional` · `quests/main_quest/act_01/q101_resurrection/base/check_emails`
   - Map pin: ref `#q101_mp_v_room_computer`; position `-1387.0349121094, 1273.5327148438, 124.30874633789`
4. **Find something to eat.**  
   `Optional` · `quests/main_quest/act_01/q101_resurrection/base/eat_something`
   - Map pin: ref `#q101_mp_eat_drink`; position `-1376.6978759766, 1270.705078125, 123.46489715576`
5. **Take the pills.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/eat_pills`
6. **Open your inventory and put on some clothes.**  
   `Optional` · `quests/main_quest/act_01/q101_resurrection/base/put_on_clothes`
7. **Stand**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/get_up`
8. **Crawl toward the pills.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/take_pills`
   - Map pin: ref `#q101_mp_anti_johnny_pills`; position `-1381.0197753906, 1271.1508789063, 123.09517669678`
9. **Stock up on ammo.**  
   `Optional` · `quests/main_quest/act_01/q101_resurrection/base/restock_ammo`
10. **Follow Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/follow`
11. **Talk to the stranger.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/johnny_talk`
12. **Leave the apartment.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/prepare_before_leave`
   - Map pin: ref `#q101_mp_leave_v_room`; position `-1389.6557617188, 1271.1151123047, 124.59104919434`
13. **Get some sleep.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/sleep`
14. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/talk`
15. **Talk to Viktor.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/base/victor`
16. **Call Delamain.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/chase/delamain`
17. **Exit the car.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/chase/get_out_from_car`
18. **Survive the attack.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/chase/kill_troy3`
19. **Wait.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/chase/ride_w_takemura`
20. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/chase/talk`
21. **Neutralize the motorcyclists.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/landfill/biker`
22. **Crawl to safety.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/landfill/dig`
23. **Wait for Takemura to neutralize the motorcyclists.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/landfill/ghost_hood`
24. **Neutralize the attacker.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/landfill/ghost_roof`
25. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/takemura/call_takemura`
26. **Meet with Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/takemura/meet_with_takemura`
   - Map pin: ref `#q101_mp_to_elev_helper2`; position `-1395.1827392578, 1318.3940429688, 120.15723419189`
   - Map pin: ref `#q101_mp_elevator_terminal_mb`; position `-1434.8538818359, 1314.5064697266, 120.81092834473`
   - Map pin: ref `#q101_mp_to_elev_helper1`; position `-1402.3829345703, 1289.4873046875, 120.47744750977`
27. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/takemura/talk_takemura`
   - Map pin: ref `#q101_mp_sit_tom_diner`; position `-1506.4808349609, 1146.607421875, 19.257753372192`
28. **Talk to Johnny Silverhand.**  
   `Primary` · `quests/main_quest/act_01/q101_resurrection/takemura/talk_with_johnny`
29. **Read the message from the Megabuilding H10 Administration**  
   `Optional` · `quests/main_quest/act_01/q101_resurrection/takemura/read_message_adm`

## Practice Makes Perfect

- IGN walkthrough: [Practice Makes Perfect](https://www.ign.com/wikis/cyberpunk-2077/Practice_Makes_Perfect_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `2914891760`
- Quest path: `quests/main_quest/prologue/q000_tutorial`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `combat/neutralize`, `stealth/avoid detection`

### Journal premise

Better to be prepared than dead. The street can be brutally unforgiving, so a quick brush-up on combat skills certainly coudn't hurt.

### Objective sequence

1. **Go to the window.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/01_approach_the_window`
   - Map pin: ref `#q000_vr_mp_course_01_patrol_room_window`; position `-516.8251953125, 347.71411132813, -216.43423461914`
2. **Tag all the guards.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/02_tag_the_guard`
3. **Enter the training area.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/03_enter_the_room`
   - Map pin: ref `#q000_vr_mp_course_01_patrol_room_entrance`; position `-512.00573730469, 357.14208984375, -220.48393249512`
4. **Hide from the guards.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/03b_hide_from_guard`
   - Map pin: ref `#q000_vr_mp_course_01_room_cover`; position `-509.4677734375, 352.92166137695, -221.36434936523`
5. **Sneak to the exit.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/04_reach_exit_of_the_room`
   - Map pin: ref `#q000_vr_mp_course_01_patrol_room_exit`; position `-518.06512451172, 370.39837646484, -219.64503479004`
6. **Enter the next training area.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/05_enter_next_area`
   - Map pin: ref `#q000_vr_mp_course_01_camera_room_entrance`; position `-528.80322265625, 372.37420654297, -218.49931335449`
7. **Tag the camera.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/06_tag_the_camera`
8. **Reach the exit without being detected by the camera.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/07_reach_exit_of_the_room`
   - Map pin: ref `#q000_vr_mp_course_01_camera_room_entrance_stairs`; position `-526.22924804688, 382.96060180664, -218.25430297852`
   - Map pin: ref `#q000_vr_mp_course_01_end`; position `-503.57095336914, 366.1106262207, -216.74887084961`
   - Map pin: ref `#q000_vr_mp_course_01_room_02_exit_stairs`; position `-508.4944152832, 375.24069213867, -218.7958984375`
9. **Step onto the platform.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_01/08_step_into_exit`
10. **Pick up the weapon.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01a_pick_weapon`
11. **Shoot all the targets.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01aa_hit_targets`
12. **Wait for the next round of targets.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01aaa_wait_for_next_round`
13. **Eliminate all enemies.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01b_kill_the_opponent`
14. **Take the inhaler.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01c_pick_up_reanimator`
15. **Use the inhaler to regain Health.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/01d_use_reanimator`
16. **Eliminate all enemies.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/02_kill_enemies`
17. **Enter the training area.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/02a_enter_arena`
   - Map pin: ref `#q000_vr_mp_course_02_arena`; position `-420.44116210938, 290.27536010742, -219.73495483398`
18. **Step onto the platform.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_02/03_step_into_exit`
19. **Approach the window.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/00a_enter_the_room`
   - Map pin: ref `#q000_vr_mp_course_03_hacking_room`; position `-319.46755981445, 333.35949707031, -217.22161865234`
20. **Open your scanner.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/00aa_turn_on_scanner`
21. **Scan two objects highlighted gold.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/00b_scan_all_targets`
   - Map pin: ref `#q000_vr_mp_course_03_stage_00_camera`; position `-316.6491394043, 339.53506469727, -216.98291015625`
   - Map pin: ref `#q000_vr_mp_course_03_stage_00_laptop`; position `-320.15441894531, 339.53506469727, -219.73904418945`
   - Map pin: ref `#q000_vr_mp_course_03_stage_00_server`; position `-315.38610839844, 338.53506469727, -217.93449401855`
22. **Hack the TV.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/01_scan_the_tv`
   - Map pin: ref `#q000_vr_mp_course_03_stage_01_tv`; position `-319.5, 350, -217.10000610352`
23. **Approach the window.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/01a_enter_the_room`
   - Map pin: ref `#q000_vr_mp_course_03_hacking_room`; position `-319.46755981445, 333.35949707031, -217.22161865234`
24. **Enter the training area.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/01a_enter_the_room1`
   - Map pin: ref `#q000_vr_mp_course_03_hacking_room`; position `-319.46755981445, 333.35949707031, -217.22161865234`
25. **Use the TV screen to distract your enemies.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/02_use_tv_to_distract`
26. **Sneak up to the guard.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/02b_approach_the_guard_silently`
27. **Eliminate the guard.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/03_eliminate_the_guard`
28. **Pick up the body.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/03b_pick_up_the_body`
29. **Hide the body.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/03c_hide_body`
   - Map pin: ref `#q000_vr_mp_first_body_container`; position `-324.65295410156, 349.38458251953, -218.63748168945`
30. **Sneak up to the guard.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/03d_approach_the_guard_02`
31. **Hack the guard in order to distract the other one.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/04_hack_first_npc`
32. **Take control of the camera.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/04aa_take_over_camera`
   - Map pin: ref `#q000_vr_mp_course_03_stage_02_camera`; position `-319.5, 350, -215.5`
33. **Use Breach Protocol on one of the guards.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/04bb_use_icebreaker`
34. **Take down the guard and hide the body.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/04c_eliminate_second_guard`
35. **Use the Call In quickhack to group the guards closely together.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/04c_use_call_in`
36. **Wait for the right moment to eliminate both guards.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/05_wait_for_right_moment`
37. **Hack one of the guards and use the "Detonate Grenade" quickhack.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/06_trigger_kill`
38. **Exit camera view.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/06b_exit_the_camera`
39. **Step onto the platform.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/07_enter_exit_pad`
40. **Connect to the Access Point.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_03/08_connect_to_ap`
   - Map pin: ref `#q000_vr_mp_course_03_hacking_room_access_point`; position `-319.07577514648, 333.21099853516, -216.67752075195`
41. **Enter the arena.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/01_enter_the_arena`
   - Map pin: ref `#q000_vr_mp_course_04_arena`; position `-244.51976013184, 341.58990478516, -220.99987792969`
42. **Sneak up to the enemy.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/01b_approach_enemy_silently`
43. **Grapple the enemy.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/01c_grapple_the_enemy`
44. **Wait for instructions.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/01d_wait_for_instructions`
45. **Defeat the enemy.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02_defeat_the_opponent`
46. **Hit the enemy 3 times with Fast Attacks.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02a_hit_opponent`
47. **Hit the enemy with a combo attack.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02b_hit_with_combo`
48. **Hit the enemy with a Strong Attack.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02bb_hit_with_strong_attack`
49. **Hit the enemy repeatedly until you run out of Stamina.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02bbb_hit_until_slowdown`
50. **Hit the blocking enemy 3 times with Fast Attacks.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02c_hit_blocking_enemy`
51. **Break the enemy's blocking stance with a Strong Attack.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02d_break_enemies_block`
52. **Block 3 enemy attacks.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02e_block_attacks`
53. **Block 2 Strong Attacks.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02ee_block_strong_attacks`
54. **Attack an enemy after blocking  2 times.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02f_perform_block_attack`
55. **Counter an enemy attack 2 times.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02f_perform_counterattack`
56. **Dodge 3 enemy attacks.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/02ff_dodge_attacks`
57. **Take the katana.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/03_pick_up_katana`
58. **Defeat the enemy.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/04_defeat_opponent`
59. **Defeat all enemies.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/05_defeat_all_opponents`
60. **Step into the training area to continue.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/05a_step_into_arena`
   - Map pin: ref `#q000_vr_mp_course_04_arena_final_fight`; position `-244.51976013184, 338.48156738281, -220.99987792969`
61. **Step onto the platform.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_course_04/06_enter_exit_pad`
62. **Talk to the drill sergeant.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_tutorial/q000_01_talk_to_sarge`
63. **Use the door to exit the simulation.**  
   `Optional` · `quests/main_quest/prologue/q000_tutorial/q000_tutorial/q000_03_exit_opt`
   - Map pin: ref `#q000_vr_mp_sim_exit`; position `-434.23336791992, 422.56719970703, -213.62335205078`
64. **Complete all training modules.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_tutorial/q000_02_complete_courses`
65. **Use the door to exit the simulation.**  
   `Primary` · `quests/main_quest/prologue/q000_tutorial/q000_tutorial/q000_03_exit`
   - Map pin: ref `#q000_vr_mp_sim_exit`; position `-434.23336791992, 422.56719970703, -213.62335205078`

## Run This Town

- IGN walkthrough: [Run This Town](https://www.ign.com/wikis/cyberpunk-2077/Run_This_Town_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3838929451`
- Quest path: `ep1/quests/minor_quest/mq304_succession`
- District: Pacifica
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Journal premise

Seems Hands has some work teed up for ya. Apparently of the urgent variety. Sounds like Dogtown's about to start sizzlin' up again. Hurry up and finish that other job you got from him first. Curiosity's killin' me.

### Objective sequence

1. **Complete the previous contract you received from Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/00_finish_sts`
2. **Wait for the Heavy Hearts club to open.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/00b_finish_sts_wait`
   - Map pin: ref `#mq304_mp_wait_heavy_hearts`; position `-1642.2314453125, -2300.2092285156, 40.10018157959`
3. **Meet with Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/01_meet_hands`
4. **Talk to Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/01a_talk_hands`
5. **Sit.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/01b_sitdown_hands`
6. **Look in the mirror.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/01c_mirror_hands`
7. **Leave the room.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/01d_leave_hands`
8. **Take Aguilar's imprint.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02_take_nicola_stuff`
   - Map pin: ref `#mq304_mp_nicola_stuff`; position `-1584.921875, -2340.28125, 58.2041015625`
9. **Take Aguilar's suit.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02a_take_aguilar_suit`
10. **Take Aguilar's gun.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02b_take_nicola_gun`
   - Map pin: ref `#mq304_mp_nicola_stuff`; position `-1584.921875, -2340.28125, 58.2041015625`
11. **Take the briefing shard.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02c_take_briefing`
12. **Familiarize yourself with the job details.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02d_read_briefing`
13. **Put on Aguilar's suit.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/01_meet_hands/02e_equip_suit`
14. **Go to the place where Jago will meet with the Voodoo Boys.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/01_go_to_meeting`
15. **Activate Aguilar's imprint and wait for the Voodoo Boys.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/01a_wait_voodoo`
   - Map pin: ref `#mq304_mp_jago_meeting_place`; position `-2010.6823730469, -2861.8305664063, 101.26573944092`
16. **Return to the meeting place before you fail the job.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/01b_return_meeting`
17. **Find a way to get rid of the Voodoo Boys.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/02_deal_with_vdb`
18. **Neutralize the Voodoo Boys.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/02b_defeat_voodoo`
19. **Wait for Jago.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/04_wait_jago`
   - Map pin: ref `#mq304_mp_wait_jago_spot`; position `-1976.0274658203, -2855.1171875, 98.686485290527`
20. **Talk to Jago.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/05_talk_to_jago`
21. **Shoot Jago's bodyguard.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/05a_kill_bodyguard`
22. **Talk to Johnny.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/06_talk_to_johnny`
23. **Deactivate Aguilar's imprint.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/02_jago/07_change_back`
24. **Call Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/03_report_hands/01_call_hands`
25. **Talk to Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/03_report_hands/02_talk_hands`
26. **Meet with Bennett before Kurt Hansen's wake.**  
   `Optional` · `ep1/quests/minor_quest/mq304_succession/04_bennett/01_go_to_spot`
27. **Deal with Bennett's driver.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/02_deal_with_driver`
28. **Activate Aguilar's imprint and wait.**  
   `Optional` · `ep1/quests/minor_quest/mq304_succession/04_bennett/01b_wait_bennett`
   - Map pin: ref `#mq304_mp_bennett_hide`; position `-2291.3603515625, 464.02655029297, 7.6282987594604`
29. **Hide the driver's body.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/02a_hide_driver`
30. **Return to the alley to finish your business with Bennett.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/02b_return_hide_driver`
31. **Get in Bennett's car.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/03_get_in_car`
32. **Wait for Bennett.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/03a_wait_for_bennett`
33. **Neutralize Bennett.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/04_defeat_bennett`
34. **Get out of the car.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/04b_leave_car`
35. **Talk to Bennett.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/05_talk_with_bennett`
36. **Step away and deactivate Aguilar's imprint.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/04_bennett/06_move_away`
   - Map pin: ref `#mq304_mp_ben_switchoff_shard`; position `-2292.1484375, 467.19793701172, 8.3173379898071`
37. **Go to the Black Sapphire.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/00_wait_for_wake`
38. **Activate Aguilar's imprint and wait for the wake to begin.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/00a_disguise_wake`
   - Map pin: ref `#mq304_mp_wait_wake_spot`; position `-1811.4012451172, -2326.7145996094, 40.479976654053`
39. **Talk to Johnny.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/00b_talk_johnny_b4_wake`
40. **!OBSOLETE**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/01_meet_bodyguards`
41. **Return to the wake before you fail the job.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/01b_return_bodyguards`
   - Map pin: ref `#mq304_combat_tower_entrance`; position `-1818.9412841797, -2315.1645507813, 40.861164093018`
42. **Enter the Black Sapphire.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/02_go_to_wake`
   - Map pin: ref `#mq304_combat_tower_entrance`; position `-1818.9412841797, -2315.1645507813, 40.861164093018`
43. **Wait for the elevator to arrive.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/02b2_wait_elevator`
44. **Take the elevator up to the wake.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/02b_use_elevator`
   - Map pin: ref `#mq304_mp_kurts_wake_terminal_downstairs`; position `-1936.8442382813, -2316.875, 44.95166015625`
45. **Attend Hansen's wake.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/02c_go_to_wake_upstairs`
   - Map pin: ref `#mq304_mp_kurts_wake`; position `-1893.4379882813, -2261.5622558594, 439.796875`
46. **Talk to Jago.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/03_approach_jago`
47. **Wait for Jago.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/03a_wait_for_jago`
48. **Follow Jago to meet with Bennett.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/04_go_to_bennett`
49. **Choose the new leader of Dogtown.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/04a_settle_succession`
   - Map pin: ref `#mq304_mp_wake_booth`; position `-1893.0587158203, -2249.0603027344, 440.73693847656`
50. **Gain a strong position in negotiations.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/05_sit_in_booth`
   - Map pin: ref `#mq304_mp_wake_booth`; position `-1893.0587158203, -2249.0603027344, 440.73693847656`
51. **Leave the wake.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/06_leave_wake`
   - Map pin: ref `#mq304_mp_kurts_wake_elevator_upstairs`; position `-1934.5830078125, -2316.8747558594, 443.09790039063`
52. **Wait for the elevator to arrive.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/06ab_wait_elevator_down`
53. **Leave the Black Sapphire.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/06ac_leave_combat_tower`
   - Map pin: ref `#mq304_combat_tower_entrance`; position `-1818.9412841797, -2315.1645507813, 40.861164093018`
54. **Deactivate Aguilar's imprint.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/06b_change_back`
   - Map pin: ref `#mq304_mp_end_wait_wake_spot`; position `-1811.2744140625, -2326.5532226563, 41.319976806641`
55. **Take the elevator down.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/06ba_take_elevator_down`
   - Map pin: ref `#mq304_mp_kurts_wake_terminal_upstairs`; position `-1936.8481445313, -2316.8747558594, 443.09790039063`
56. **Talk to Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/07_call_hands`
57. **Call Mr. Hands.**  
   `Primary` · `ep1/quests/minor_quest/mq304_succession/05_wake/07a_call_hands`

## Search and Destroy

- IGN walkthrough: [Search and Destroy](https://www.ign.com/wikis/cyberpunk-2077/Search_and_Destroy_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1544449885`
- Quest path: `quests/main_quest/act_01/q112_04_hideout`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Know what my downside is? No matter how much I might want to, I don't fucking make mistakes. Lo and behold! Our factory-reset ronin, hounded by every single Arasaka soldier in Night City for KIDNAPPING Saburo Arasaka's daughter. Kudos to him – I couldn't've fucked this plan up better myself. And after all this, he STILL wants you to drop by? I don't know who's more whacked – him or us. Just remember to knock four times. His head, preferably – against a fucking table.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06a_wait_call`
2. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06b_talk_takemura`
3. **Get to the hideout.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06c_go_safehouse`
4. **Knock on the door.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06d_knock`
5. **Try to save Takemura.**  
   `Optional` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06i_save`
6. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06f_follow_takemura`
7. **Return to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06g2_return`
8. **Check the door.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06g_check_door`
9. **Talk to Hanako Arasaka.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06g_interrogate_hanako`
10. **Leave the building.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06h_flee`
11. **Talk to Takemura.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06j_takemura`
12. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06k_johnny`
13. **Escape the apartment.**  
   `Optional` · `quests/main_quest/act_01/q112_04_hideout/06_safe_house/06c_use_shortcut`
14. **Approach the door.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/07_safe_house/07a2_check_door`
   - Map pin: ref `#q112_mp_motel_door`; position `1662.2496337891, -786.40057373047, 51`
15. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/07_safe_house/07a_guard_door`
16. **Talk to the stranger.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/07_safe_house/07b_take_call`
17. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q112_04_hideout/07_safe_house/07c_johnny`

## Somewhat Damaged

- IGN walkthrough: [Somewhat Damaged](https://www.ign.com/wikis/cyberpunk-2077/Somewhat_Damaged_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3704679420`
- Quest path: `ep1/quests/main_quest/q305_bunker`
- District: Dogtown
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

You're hot on the heels of a girl who's got nothing left to lose. Nothing can make a person more dangerous, but you probably already know that. Reed thinks he can still save her. Is he lying to himself on purpose? Or maybe he knows his old friend too well? What do you think? Who'll you find once you finally reach her? I've got a feeling even So Mi doesn't know the answer to that...

### Objective sequence

1. **Go back and follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/00_get_back_on_track`
2. **Send Mr. Hands details of the ambush.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/04_chase/inform_mr_hands`
3. **Follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/00a_chase_scenes`
4. **Investigate the area.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/01_investigate_crash`
5. **Find the MaxTac transport truck.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/01b_find_apc`
6. **Follow traces of the Blackwall left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/04a_before_jump`
7. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/04b_talk_johnny`
8. **Find a terminal.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/05a_find_terminal`
9. **Get out of the water.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/05a_out_of_water`
10. **Find Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/chase_songbird`
   - Map pin: ref `#q305_mappin_chase_song_01`; position `-2454.048828125, -2542.7543945313, 18.959999084473`
   - Map pin: ref `#q305_mappin_chase_song_02`; position `-2446.009765625, -2562.1726074219, -1.8800001144409`
   - Map pin: ref `#q305_mappin_chase_song_03`; position `-2443.0234375, -2552.3432617188, -7`
   - Map pin: ref `#q305_mappin_chase_song_04`; position `-2448.96484375, -2546.1323242188, -6.2699999809265`
   - Map pin: ref `#q305_mappin_chase_song_05`; position `-2428.8063964844, -2547.45703125, -5.7399997711182`
   - Map pin: ref `#q305_mappin_chase_song_06`; position `-2433.5170898438, -2587.4001464844, -5.8400001525879`
   - Map pin: ref `#q305_mappin_chase_song_07`; position `-2420.2104492188, -2601.8896484375, -55.990001678467`
   - Map pin: ref `#q305_mappin_chase_song_before_jump`; position `-2424.6706542969, -2593.3403320313, -6.6100001335144`
11. **Follow traces of the Blackwall left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/chase_songbird_02`
12. **Jump down the shaft.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/chase_songbird_03`
   - Map pin: ref `#q305_mappin_chase_song_before_jump`; position `-2424.6706542969, -2593.3403320313, -6.6100001335144`
13. **Look for Songbird in the truck.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/check_apc`
   - Map pin: ref `#q305_mappin_chase_song_02`; position `-2446.009765625, -2562.1726074219, -1.8800001144409`
14. **Connect to the terminal.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/connect_to_terminal`
15. **Gain access to the sealed-off area.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/follow_songbird`
   - Map pin: ref `#q305_mappin_chase_song_08`; position `-2429.1882324219, -2575.2502441406, -5.8400001525879`
   - Map pin: ref `#q305_mappin_chase_song_03`; position `-2443.0234375, -2552.3432617188, -7`
   - Map pin: ref `#q305_mappin_chase_song_04`; position `-2448.96484375, -2546.1323242188, -6.2699999809265`
   - Map pin: ref `#q305_mappin_chase_song_05`; position `-2428.8063964844, -2547.45703125, -5.7399997711182`
   - Map pin: ref `#q305_mappin_chase_song_06`; position `-2433.5170898438, -2587.4001464844, -5.8400001525879`
   - Map pin: ref `#q305_mappin_chase_song_07`; position `-2420.2104492188, -2601.8896484375, -55.990001678467`
16. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/talk_with_reed`
17. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/04_chase/talk_with_songbird`
18. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/00a_talk_reed`
19. **Open the airlock doors.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/012b_open_airlock`
20. **Follow the Blackwall traces.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/01a_exit_room`
21. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/02b_talk_with_johnny`
22. **Follow the Blackwall traces.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/03_follow_songbird_path`
23. **Take the elevator.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/03_use_the_elevator`
24. **Find a way around the gate.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/03b_go_around_gate`
25. **Listen to the conversation.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/04b_listen_to_coversation`
26. **Follow the Blackwall traces.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/06_follow_sungbird_further`
   - Map pin: ref `#q305_mappin_bunker_other_side_of_broken_gate`; position `-2142.5561523438, -2350.0500488281, -192.7202911377`
27. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/06b_talk_with_songbird`
28. **Check the console to find a way to lift the lockdown.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07a2_use_console`
29. **Scan for a way to lift the lockdown.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07a_use_kiroshi`
30. **Disable Dataterminal Alpha in the server room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07b2_disable_alfa_location`
31. **Disable Dataterminal Bravo in the server room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07b2_disable_bravo_location`
32. **Go to the server room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07b2_go_to_server`
33. **Locate dataterminals Alpha and Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07b_disable_alfa`
34. **Locate Dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07b_disable_bravo`
35. **Raise the shutters to access the server room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07c_open_gate_to_alfa`
36. **Use the computer to disable dataterminal Alpha.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07d_use_computer_alfa`
37. **Use your personal link to breach dataterminal Alpha.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07e_use_personal_link_alfa`
38. **Go to the room containing dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08b_get_to_bravo`
39. **Use the terminal to disable dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08c_use_computer_bravo`
40. **Use your personal link to breach dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08d_authorize_bravo`
41. **Crawl under dataterminal Bravo to manually disable it.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08e_crawl_into_bravo`
42. **Disable dataterminal bravo manually.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08f_destroy_bravo`
43. **Crawl back to the server room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/08h_crawl_back`
44. **Disable or destroy the backup dataterms.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09_destroy_backup_servers`
45. **Hide from the robot.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09_escape_the_robot`
46. **Use your personal link to breach dataterminal Sierra.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09a_authorize_sierra`
47. **Use the terminal to disable dataterminal Sierra.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09a_destroy_backup_server_01`
48. **Find dataterminal Sierra.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09a_find_sierra`
49. **Go to Engineering to disable dataterminal Sierra.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09a_go_to_sierra`
50. **Use your personal link to breach dataterminal Victor.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09b_authorize_victor`
51. **Use the terminal to disable dataterminal Victor.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09b_destroy_backup_server_02`
52. **Find dataterminal Victor.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09b_find_victor`
53. **Go to Security to disable dataterminal Victor.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09b_go_to_victor`
54. **Return to Engineering to disable dataterminal Sierra.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09c_return_sierra`
55. **Return to Security to disable dataterminal Victor.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09d_return_victor`
56. **Return to the sealed gate.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/10_go_back_to_gate`
57. **Use the terminal to open the gate to Sector 3.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/10_open_gate`
58. **Follow the Blackwall traces.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/10b_pursue_songbird_further`
59. **Outrun your pursuer across the bridge.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/11_escape_the_pursuit`
60. **Enter the airlock.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/13_enter_the_airlock`
61. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/capture_songbird`
62. **Find a way to lift the lockdown.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/disable_lockdown`
63. **Repair the workshop doors.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09x2_fix_repair_bay`
64. **Find a place to hide.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/12_hide_from_robot`
65. **Close the airlock door behind you.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/close_the_airlock`
66. **Scan for a way to destroy dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/disable_connection`
67. **Go to the room containing dataterminal Bravo.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/disable_second_server`
68. **Follow traces of the Blackwall left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/enter_bunker`
   - Map pin: ref `#q305_mapping_after_water_01`; position `-2394.1013183594, -2577.5895996094, -56.480010986328`
   - Map pin: ref `#q305_mapping_after_water_002`; position `-2395.2414550781, -2568.3500976563, -56.480010986328`
69. **Follow the Blackwall traces.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/find_songbird`
   - Map pin: ref `#q305_first_gate_mappin`; position `-2200.099609375, -2398.0615234375, -192.63000488281`
   - Map pin: ref `#q305_mappin_broken_gate`; position `-2146.0900878906, -2352.5703125, -191.1199798584`
   - Map pin: ref `#q305_mappin_bunker_top_of_big_elevator`; position `-2378.8996582031, -2537.1560058594, -69.580284118652`
   - Map pin: ref `#q305_mappin_bunker_other_side_of_broken_gate`; position `-2142.5561523438, -2350.0500488281, -192.7202911377`
   - Map pin: ref `#q305_mappin_bunker_past_robot`; position `-2110.2272949219, -2323.146484375, -192.73030090332`
   - Map pin: ref `#q305_mappin_bunker_into_cold`; position `-2076.1740722656, -2241.9165039063, -194.21028137207`
   - Map pin: ref `#q305_mappin_bunker_command_room`; position `-2069.8439941406, -2202.4467773438, -193.85052490234`
   - Map pin: ref `#q305_side_entrance_mappin`; position `-2194.0603027344, -2405.0903320313, -191.13999938965`
   - Map pin: ref `#q305_walkway_mappin`; position `-2203.6896972656, -2384.7602539063, -187.13000488281`
70. **Check the console to find a way to lift the lockdown.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07a2_use_console1`
71. **Go through the gate to Sector 3.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/into_inner_bunker`
   - Map pin: ref `#q305_mappin_bunker_other_side_of_broken_gate`; position `-2142.5561523438, -2350.0500488281, -192.7202911377`
72. **Scan for a way to lift the lockdown.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/07a_use_kiroshi1`
73. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/talk_to_songbird`
74. **Talk to Johnny.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/01b_talk_with_johnny`
75. **Bring back power to the control panel near the maintenance room.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09_fix_repair_bay_terminal`
76. **Open the door to the maintenance room.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/06_outer_bunker/09b_open_repair_bay`
77. **Follow traces left by Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/01_songbird_traces`
78. **Pick up Songbird's trail deeper within the facility.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/01b_follow_songbird`
79. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/01c_talk_to_songbird`
80. **Use the terminal to access the core's controls.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/02_gain_access`
81. **Use the terminal to shut down the core's subsystems.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/02b2_shut_support_systems`
82. **Check the shut down procedure's progress using the terminal.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/02b3_check_computer`
83. **Initiate the core shutdown procedure.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/02b_start_shutdown`
84. **Shut down the core's remaining subsystems.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/03_engage_system_reset`
85. **Use the terminal to shut down the Neural Network mainframe.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04_interrupt_thermal`
86. **Find the Neural Network Room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04a_find_neural`
87. **Use the terminal to check the subsystem's status.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04b_check_terminal_neural`
88. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04b_hack_neural`
89. **Find another way to shut down the Neural Network mainframe.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04b_interrupt_thermal_alt`
90. **Return to the Neural Network room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04c_get_back_to_neural`
91. **Scan for a way to disable the Neural Network stabilizers.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04c_use_kiroshi_neural`
92. **Unplug the cables from the Neural Network system.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04d_disconnect_cables_neural`
   - Map pin: ref `#q305_neural_01_mappin`; position `-2099.25, -2224.08984375, -194.42001342773`
   - Map pin: ref `#q305_neural_02_mappin`; position `-2094.3395996094, -2224.3999023438, -194.42001342773`
   - Map pin: ref `#q305_neural_03_mappin`; position `-2088.8898925781, -2230.73046875, -194.42001342773`
93. **Disonnect all Neural Network Stabilizers.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/04d_disconnect_neural`
94. **Use the terminal to shut down the Thermic Control System.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05_interrupt_coolant`
95. **Find the Thermic Control room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05a_find_thermal`
96. **Use your personal link to breach the Thermic Control terminal.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05b_hack_thermal`
97. **Find another way to shut down the Thermic Control system.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05b_interrupt_coolant_alternative`
98. **Return to the Thermic Control room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05c_get_back_to_thermal`
99. **Shut down all Thermic Control processes.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/05d_disconnect_thermal`
100. **Use the terminal to check the subsystem's status.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06_check_terminal_datafort`
101. **Use the terminal to shut down the Datafort Central Command.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06_interrupt_datafort`
102. **Find the Datafort Central Command room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06a_find_datafort`
103. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06c_close_datafort`
104. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06c_disable_datafort`
105. **Use your personal link to breach the Thermic Control terminal.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06b_disengage_coolant_alt`
106. **Scan the firewall device.**  
   `Optional` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06c_use_kiroshi_datafort`
107. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06b_hack_datafort`
108. **Return to the Datafort Central Command room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06c_get_back_to_datafort`
109. **Destroy the firewall device to disable the subsystem.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06d_destroy_firewalls`
110. **Hide from the robot until it leaves the room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06g_hide_from_cerberus`
111. **PLACEHOLDER TIMER**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/06x_temp_clock`
112. **Use the computer to complete the shutdown procedure.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/07_engage_system_reset`
113. **Return to the Core Control room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/07a_get_back_to_command`
114. **Stop the robot from pursuing you further**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07_inner_bunker/08_stop_the_robot`
115. **Examine the record player.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/check_gramophone`
116. **Find the source of the sound.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/check_the_sound`
117. **See how the situation unfolds.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/explore`
118. **Look around the room.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/look_around_the_room`
119. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/talk_with_songbird`
120. **Witness Songbird's memories.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07b_brooklyn/witness_other_memories`
121. **Check Songbird's vitals.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/check_songbird`
122. **Use the terminal to complete the shutdown procedure.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/finish_shutdown`
123. **Enter the core.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/go_to_core`
   - Map pin: ref `#q305_mappin_doors_to_cynosure_bridge`; position `-2068.7995605469, -2208.8405761719, -193.30000305176`
   - Map pin: ref `#q305_mappin_road_to_cynosure`; position `-2069.98046875, -2211.5002441406, -197.00001525879`
   - Map pin: ref `#q305_mappin_cynosurecore`; position `-2068.0366210938, -2161.537109375, -198.25921630859`
   - Map pin: ref `#q305_mappin_cynosurecore_001`; position `-2069.490234375, -2177.8122558594, -196.6865234375`
124. **Help Songbird to her feet.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/help_songbird`
125. **Help Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/pick_up_songbird`
126. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/talk_with_reed`
127. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/talk_with_songbird`
128. **Unplug Songbird.**  
   `Primary` · `ep1/quests/main_quest/q305_bunker/07c_cynosure_core/unplug_songbird`
   - Map pin: ref `#q305_mappin_cynosurecore_unplug`; position `-2069.1489257813, -2163.6708984375, -197.52000427246`

## Spider and the Fly

- IGN walkthrough: [Spider and the Fly](https://www.ign.com/wikis/cyberpunk-2077/Spider_and_the_Fly)
- Vanilla type: `MainQuest`
- Quest hash: `4263219230`
- Quest path: `ep1/quests/main_quest/q301_q302_rescue_myers`
- District: Pacifica
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

Ooph, rough landing for Rosalind Myers. Kurt Hansen almost wiped her... at least this time, "almost" was all we needed. Since our dear prez survived, better get her out, drop her off somewhere safe and regroup with Songbird. Fingers fuckin' crossed you get it done quick – bein' cut off's gettin' real old.

### Objective sequence

1. **Talk to President Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/arrival_talk_myers`
2. **Defeat the attackers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/combat_defeat_enemies`
3. **Lead Myers to safety.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/escape_follow`
   - Map pin: ref `#q301_mp_crashsite_shuttle_lead_myers_01`; position `-2271.7390136719, -2767.44921875, 51.940013885498`
   - Map pin: ref `#q301_mp_crashsite_shuttle_lead_myers_02`; position `-2254.7651367188, -2776.974609375, 51.010013580322`
   - Map pin: ref `#q301_mp_crashsite_shuttle_lead_myers_03`; position `-2241.77734375, -2779.5278320313, 64.550010681152`
   - Map pin: ref `#q301_mp_crashsite_shuttle_lead_myers_04`; position `-2230.8833007813, -2804.0544433594, 64.550010681152`
4. **Help Myers open the door.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/escape_gate_open`
5. **Go through the door.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/escape_gate_slip`
6. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/escape_talk_songbird`
7. **Neutralize the drone.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_defeat_drone`
8. **Follow Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_follow`
9. **Hide from the drone.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_hide_drone`
10. **Help Myers remove the tracker.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_remove_tracker`
11. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_talk`
12. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/myers_talk_again`
13. **Return to Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_shuttle/return_myers`
14. **Take the elevator down to the subway.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/attach_the_explosives_04`
   - Map pin: ref `#q302_02_mp_sec_2_elevator_panel`; position `-2024.0635986328, -2423.3083496094, 47.604885101318`
   - Map pin: ref `#q302_02_mp_explosive_003`; position `-2025.224609375, -2424.716796875, 47.260704040527`
15. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/check_on_somi`
16. **Check the computer.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/check_pc`
   - Map pin: ref `#q302_02_mp_lobby_pc`; position `-1973.8402099609, -2493.1608886719, 29.789999008179`
17. **Connect Songbird to the terminal.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/connect_songbird`
18. **Destroy the repair drones.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/destroy_all_drones`
19. **Destroy all of the Chimera's weak points.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/destroy_weakspots`
20. **Defeat the Chimera.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/disable_the_turret`
21. **Go through the Expo.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/explore_building`
   - Map pin: ref `#q302_mp_myers_stop_1`; position `-1983.7037353516, -2475.2377929688, 30.200691223145`
   - Map pin: ref `#q302_02_mp_to_dealership`; position `-2038.0328369141, -2470.7602539063, 36.080688476563`
22. **Defeat the Chimera.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/face_damaged_spidertank`
23. **Fight off Hansen's soldiers until Songbird is ready.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/fend_off_enemies`
24. **Find a way through.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/find_a_passage`
25. **Enter the subway tunnels.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/get_to_the_subway`
26. **Enter the elevator.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/hall_elevator`
27. **Flee the Chimera.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/hide_wait`
   - Map pin: ref `#q302_mp_cover`; position `-2044.9769287109, -2405.1633300781, 40.420696258545`
   - Map pin: ref `#q302_02_mp_gate_1`; position `-2040.0073242188, -2460.4289550781, 34.75`
   - Map pin: ref `#q302_02_mp_gate_2`; position `-2080.9104003906, -2418.1306152344, 34`
28. **Exit the elevator.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/leave_the_elevator`
   - Map pin: ref `#q302_mp_hall`; position `-1981.2802734375, -2504.6896972656, 35.060001373291`
29. **Open the door.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/move_obstacle`
   - Map pin: ref `#q302_mp_obstacle`; position `-2002.2984619141, -2463.9484863281, 34.930686950684`
30. **Get ready to fight.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/prepare_for_attack`
31. **Shoot the cables holding the chandelier.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/shoot_cables`
   - Map pin: ref `#q302_02_shoot_cables`; position `-2043.3010253906, -2407.5405273438, 57.5`
32. **Support the Chimera in the fight against Hansen's people.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/support_the_spidertank`
33. **Jump onto the Chimera and finish it off.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/takedown`
34. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/talk_with_myers`
35. **Survive against the Chimera until the elevator arrives.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/wait_for_elevator`
36. **Wait for Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/02_spidertank/wait_for_myers`
37. **Find an alternative route to the fusebox.**  
   `Optional` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/around_the_door`
   - Map pin: ref `#q302_mp_open_door`; position `-2211.013671875, -2834.4580078125, 64.445465087891`
38. **Avoid the drone.**  
   `Optional` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/get_past_the_drone`
   - Map pin: ref `#q302_mp_get_past_drone`; position `-2166.5473632813, -2847.3012695313, 127.08548736572`
39. **Hide.**  
   `Optional` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/hide_from_convoy`
   - Map pin: ref `#q302_mp_hide`; position `-1998.2863769531, -2637.5908203125, 35.675483703613`
40. **Take the elevator and leave the parking lot.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/enter_through_parking`
   - Map pin: ref `#q302_av_building_elevator`; position `-1985.5263671875, -2512.2009277344, 20.765483856201`
41. **Reset the fusebox.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/fix_the_elevator`
   - Map pin: ref `#q302_mp_open_door`; position `-2211.013671875, -2834.4580078125, 64.445465087891`
42. **Find the fusebox in the utility room.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/get_into_utility_room`
   - Map pin: ref `#q302_mp_find_utility`; position `-2205.6735839844, -2843.8081054688, 64.18546295166`
   - Map pin: ref `#q302_mp_around_door`; position `-2223.2619628906, -2840.4282226563, 59.335479736328`
   - Map pin: ref `#q302_mp_unused_hallway`; position `-2202.8864746094, -2832.2707519531, 61.485492706299`
43. **Lose the tail before reaching the building.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/lose_the_tail`
   - Map pin: ref `#q302_around_gate_008`; position `-1986.0145263672, -2474.0107421875, 19.315483093262`
44. **Talk to Myers.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/talk_to_myers`
45. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/talk_to_songbird`
46. **Take the BARGHEST car.**  
   `Optional` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/steal_car`
47. **Clear the area of enemies.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/deal_with_enemies`
48. **Connect to the access point to allow Songbird to distract the drone.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/disable_the_drone`
   - Map pin: ref `#q302_drone_distraction_001`; position `-2154.4267578125, -2842.5510253906, 124.77547454834`
49. **Take the elevator to the upper floor.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/get_to_elevator`
   - Map pin: ref `#q302_mp_elevator`; position `-2208.9267578125, -2854.5004882813, 64.565483093262`
50. **Reach the building while avoiding the patrols.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/hide_and_pass_checkpoint`
   - Map pin: ref `#q302_around_gate_008`; position `-1986.0145263672, -2474.0107421875, 19.315483093262`
   - Map pin: ref `#q302_around_gate_008`; position `-1986.0145263672, -2474.0107421875, 19.315483093262`
   - Map pin: ref `#q302_av_building_entrance`; position `-2031.1961669922, -2518.4599609375, 29.545490264893`
   - Map pin: ref `#q302_av_building_entrance_001`; position `-1986.8663330078, -2473.5805664063, 19.62548828125`
51. **Escort Myers safely through the building.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/reach_the_streets`
   - Map pin: ref `#q302_drone_door`; position `-2202.2048339844, -2844.4807128906, 124.30548095703`
   - Map pin: ref `#q302_akebono_exit`; position `-2136.5852050781, -2840.7507324219, 123.06548309326`
   - Map pin: ref `#q302_akebono_exit_001`; position `-2129.8852539063, -2883.0700683594, 115.21548461914`
   - Map pin: ref `#q302_akebono_exit_002`; position `-2151.365234375, -2882.3500976563, 115.33548736572`
52. **Open the blocked door.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/unlock_the_door`
   - Map pin: ref `#q302_mp_get_access_code`; position `-2215.4267578125, -2841.7705078125, 64.195487976074`
53. **Find the car in the parking lot.**  
   `Optional` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/steal_car_alt`
54. **Wait for Myers in the parking lot.**  
   `Primary` · `ep1/quests/main_quest/q301_q302_rescue_myers/placeholder/wait_for_myers_to_join`

## Tapeworm

- IGN walkthrough: [Tapeworm](https://www.ign.com/wikis/cyberpunk-2077/Tapeworm_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `189903109`
- Quest path: `quests/side_quest/sq032_tapeworm`
- Level: 60
- Candidate building blocks: `travel/reach location`, `follow/escort`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Take the Omega Blockers.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill`
2. **Looks like "know thyself" has become a two-for-one deal. If it's true we're becoming one person, I suggest we keep an open dialogue. And by the way, I'd be happy to explain why the only shot you got to survive is to reach Mikoshi and stay in one piece along the way. You'd be doing me a huge favor. After all, if you're not good at following my instructions, I have to inherit whatever's left of you.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny`
3. **Sit and rest.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/01_sit_down`
4. **Follow Johnny.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/02_follow_johnny`
5. **Enter through the window.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/03_break_window`
   - Map pin: ref `#sq032_mp_window`; position `-2639.7504882813, -2476.2685546875, 36.423736572266`
6. **Open the cache.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/04_open_cache`
   - Map pin: ref `#sq032_mp_secret_cache`; position `-2634.1489257813, -2469.3537597656, 35.237880706787`
7. **Take the dogtags.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/05_take_dogtags`
8. **Leave the hotel through the window.**  
   `Primary` · `quests/side_quest/sq032_tapeworm/00_johnny/06_leave_motel_room`
   - Map pin: ref `#sq032_mp_window`; position `-2639.7504882813, -2476.2685546875, 36.423736572266`

## The Corpo-Rat

- IGN walkthrough: [The Corpo](https://www.ign.com/wikis/cyberpunk-2077/The_Corpo)
- Vanilla type: `MainQuest`
- Quest hash: `2305237100`
- Quest path: `quests/main_quest/prologue/q000_corpo`
- District: City Center
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`, `leave/escape area`

### Journal premise

So to recap – Abernathy is Jenkins' boss, Jenkins is your boss and he ordered you to off Abernathy. It's a classic damned if you do, damned if you don't situation. You kill her – you're fucked. You tell Abernathy – you're even more fucked. Why? Because for the past few years you've been batting for Jenkins' team. If you get the job done, and do it well, you might get a promotion, but forget sleeping at night, because who knows how soon you'll be in someone's crosshairs. Only proves the wide variety of opportunities Arasaka has to offer.

### Objective sequence

1. **Head to Lizzie's.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/01_meet_contact`
   - Map pin: ref `#q000_corpo_mp_lizzies_entrance`; position `-1186.8830566406, 1592.1033935547, 32.17569732666`
2. **Deal with the locals.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/01b_deal_with_locals`
3. **Have a drink with Jackie.**  
   `Optional` · `quests/main_quest/prologue/q000_corpo/lizzies/04_grab_drink`
4. **Talk to the bouncer.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/01c_talk_to_bouncer`
5. **Meet with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/02_find_jackie`
   - Map pin: ref `#q000_corpo_mp_lizzies_entrance`; position `-1186.8830566406, 1592.1033935547, 32.17569732666`
6. **Sit with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/02_give_shard`
   - Map pin: ref `#q000_corpo_mp_lizzies_sofa_sit_down`; position `-1173.263671875, 1554.5732421875, 23.966903686523`
7. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/03_talk_jackie`
8. **Talk to the agents.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/05_talk_corpo`
9. **Hand over the datashard.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/06_give_up_shard`
10. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lizzies/08_talk_to_jackie`
11. **Talk to your old acquaintance.**  
   `Optional` · `quests/main_quest/prologue/q000_corpo/lobby/03a_talk_friend`
12. **Sometimes I wonder what it's like to work for Arasaka, y'know? Way I figure it, it's like playin' Russian roulette for a million eddies. Give it a spin, pull the trigger. You hear it click, you strike it rich. And if you don't, well... the mess is someone else's problem.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lobby/00_leave_the_toilet`
   - Map pin: ref `#q000_corpo_mp_toilet_door`; position `-1476.3898925781, 227.20008850098, 17.73999786377`
13. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lobby/01_talk_with_jackie`
14. **Talk to Jenkins.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/lobby/05_talk_with_jenkins`
15. **Read the report on your personal terminal.**  
   `Optional` · `quests/main_quest/prologue/q000_corpo/office/01_to_desk`
   - Map pin: ref `#q000_corpo_mp_vs_desk_mappin`; position `-1408.6811523438, 128.51409912109, 142.81701660156`
16. **Head to Jenkins' office.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/02_to_jenkins_office`
   - Map pin: ref `#q000_corpo_mp_jenkins_office_outer_door`; position `-1415.0548095703, 122.33618164063, 143.1976776123`
   - Map pin: ref `#q000_corpo_mp_lobby_lift`; position `-1437.3922119141, 183.8856048584, 16.826284408569`
   - Map pin: ref `#q000_corpo_mp_jenkins_office_door`; position `-1415.5570068359, 110.17832946777, 143.44598388672`
17. **Sit.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/02b_sit_down`
   - Map pin: ref `#q000_corpo_jenkins_office_chair`; position `-1416.7033691406, 98.34521484375, 142.44813537598`
18. **Watch the vote.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/03_observe_conference`
19. **Talk to Jenkins.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/03_talk_jenkins`
20. **Open the case.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/04b_open_box`
21. **Take the datashard.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/05_take_shard`
   - Map pin: ref `#q000_corpo_mp_jenkins_table`; position `-1405.4982910156, 93.401885986328, 141.69439697266`
22. **Take the money.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/05a_take_money`
   - Map pin: ref `#q000_corpo_mp_jenkins_money`; position `-1405.4421386719, 93.603546142578, 141.73263549805`
23. **Leave Jenkins' office.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/05b_leave_the_office`
   - Map pin: ref `#q000_corpo_mp_jenkins_office_outer_door_02`; position `-1415.0549316406, 120.34928894043, 143.1976776123`
24. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/06_set`
25. **Go to the AV garage.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/07_go_to_hangar`
   - Map pin: ref `#q000_corpo_mp_door_hangar`; position `-1490.3415527344, 143.65385437012, 143.26177978516`
   - Map pin: ref `#q000_corpo_mp_hangar`; position `-1501.0587158203, 147.98303222656, 142.51403808594`
26. **Get in Jenkins' AV.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/08_get_into_av`
27. **Set the AV's course for Lizzie's.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/09_tell_av_where_to_go`
28. **Fly to Lizzie's.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/10_fly_to_lizzies`
   - Map pin: ref `#q000_corpo_mp_lizzies_front_entrance`; position `-1201.9047851563, 1562.2587890625, 24.273834228516`
29. **Exit the AV.**  
   `Primary` · `quests/main_quest/prologue/q000_corpo/office/11_exit_the_av`

## The Damned

- IGN walkthrough: [The Damned](https://www.ign.com/wikis/cyberpunk-2077/The_Damned)
- Vanilla type: `MainQuest`
- Quest hash: `1956232992`
- Quest path: `ep1/quests/main_quest/q303_baron`
- District: Dogtown
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Journal premise

The plot thickens, the cast is expanding, and the drama becomes a farce. Don’t you think that one more secret agent in this motley crew of downed presidents, missing netrunners and sleeper pigs is one too many? Stay on top of them, V – don’t let yourself get dragged into an even bigger mess. Like, next-corporate-war-big.

### Objective sequence

1. **Answer Reed’s call.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/01_call_reed`
2. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/01_talk_reed`
3. **Go to The Moth bar.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/03_go_to_nighthawks`
4. **Wait until the evening.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/03a_wait_opening`
   - Map pin: ref `#q303_mp_nighthawks_wait`; position `-2421.8239746094, -2671.470703125, 28.441886901855`
5. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/03b_wait_reed`
   - Map pin: ref `#q303_mp_nighthawks_wait`; position `-2421.8239746094, -2671.470703125, 28.441886901855`
6. **Talk to the bartender.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/04_talk_bartender`
7. **Sit by the bar.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/05_sit_down`
   - Map pin: ref `#q303_mp_nighthawks_sitdown`; position `-2431.2099609375, -2666.5187988281, 28.785852432251`
8. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/05_talk_bartender`
9. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/05_talk_reed`
10. **Talk to Alex and Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/05_talk_reed_and_alex`
11. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/02_nighthawks/12_silverhand`
12. **Meet with Reed near Slider’s hideout.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/01_meet_reed`
   - Map pin: ref `#q303_mp_voodoo_wait`; position `-1679.7595214844, -2724.3020019531, 104.06999206543`
13. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/02_talk_reed`
14. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/02b_follow_reed`
15. **Talk to the guards.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04_talk_guards`
16. **Find a way into the ventilation shafts.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04b_follow_reed`
   - Map pin: ref `#q303_mp_voodoo_entrance_scaffolding`; position `-1680.9936523438, -2748.1499023438, 108.75221252441`
   - Map pin: ref `#q303_mp_vdb_duct_entrance`; position `-1680.3985595703, -2762.3046875, 107.64999389648`
17. **Wait for Reed to help you escape.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04b_leave_trap`
18. **Use code 230598 to open the side door.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04b_open_vent_door`
19. **Find Slider.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04c_find_baron`
   - Map pin: ref `#q303_mp_vdb_duct_path_1`; position `-1664.0621337891, -2772.1564941406, 108.650390625`
   - Map pin: ref `#q303_mp_vdb_duct_path_002`; position `-1662.8319091797, -2783.9877929688, 108.6494140625`
20. **Destroy the server cores to sever the Voodoo Boys connection.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04e_destroy_server`
21. **Reach Slider.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/04f_reach_baron`
22. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/05a_follow_reed`
23. **Take out the guards.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/05a_kill_guards`
24. **Jack into Slider’s device.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/05b_connect_net`
   - Map pin: ref `#q303_mp_vdb_baron_chair`; position `-1622.3159179688, -2801.5876464844, 98.145660400391`
25. **Talk to Slider.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/06_talk_baron`
26. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/06_talk_songbird`
27. **Leave the Voodoo Boys hideout with Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/07_leave`
28. **Look at the Black Sapphire.**  
   `Primary` · `ep1/quests/main_quest/q303_baron/03_voodoo_boys/08_look_at_tower`
   - Map pin: ref `#q303_mp_vdb_combat_tower_lookat`; position `-1838.140625, -2389.830078125, 347.91262817383`

## The Heist

- IGN walkthrough: [The Heist](https://www.ign.com/wikis/cyberpunk-2077/The_Heist_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1130542605`
- Quest path: `quests/main_quest/prologue/q005_heist`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

So that's how it ends… at least for me. In the backseat of a limo with hot corporate lead wedged in my gut. You know, all things considered, that ain't a half-bad way for a Welles to go. Most sons of Heywood tap out without all those fireworks. But what can I say, Night City's chewed up names way bigger than mine before. Not you, though – you still got work to do. Cut a fat deal (heh) with Dex in my honor. And don't piss it all away in vain, or I'll be rollin' in my grave until I hit the east coast. I won't give you a minute of goddamn peace, mano. This is the last favor we owe ourselves.

### Objective sequence

1. **Retrieve the Flathead from Maelstrom.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/00_before/finish_q003`
2. **Go over heist with Evelyn Parker.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/00_before/finish_q004`
3. **Scan for a way into the vents.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/04_room_a_find_grate`
4. **Scan for hackable devices.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/05_room_a_find_distraction`
5. **Order Flathead to go to the terrarium.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/06_room_a_use_distraction`
6. **Wait for housekeeping to move.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/07_room_a_wait_for_maid_to_clear_out`
7. **Enter the vent using Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/08_room_a_use_grate`
8. **Wait for Flathead to finish.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/10_wait_for_flathead_action`
9. **Order Flathead to move the cart.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/11_flathead_push_cart`
10. **Wait for T-Bug to switch cam view.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/cam_switch`
11. **Consult with T-Bug.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/consult_with_tbug`
12. **Scan for a way into the vents.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/room_b_find_grate`
13. **Scan for a way into the vents.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/room_b_find_grate1`
14. **Use Flathead to open the ventilation grate.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/room_b_use_grate`
15. **Use Flathead to open the ventilation grate.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03a_spiderbot/room_b_use_grate1`
16. **Use your personal link on the safe.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/connect_to_safe`
   - Map pin: ref `#q005_mrk_safe_mappin`; position `-2202.0546875, 1756.9931640625, 308.79959106445`
17. **Scan for a hidden switch.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/find_safe_release_switch`
   - Map pin: ref `#q005_mp_safe_hidden_mappin`; position `-2202.0546875, 1756.9931640625, 307.93692016602`
   - Map pin: ref `#q005_mp_safe_hidden_mappin`; position `-2202.0546875, 1756.9931640625, 307.93692016602`
18. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/follow_jackie`
19. **Hide inside the maintenance shaft.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/hide`
   - Map pin: ref `#q005_mp_penthouse_utility_room`; position `-2211.8483886719, 1755.8426513672, 309.43435668945`
20. **Leave your hiding place.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/leave_hideout`
21. **Observe the meeting.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/observe_arasakas`
22. **Go to the safe.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/open_cabinet`
   - Map pin: ref `#q005_mp_safe_hidden_mappin`; position `-2202.0546875, 1756.9931640625, 307.93692016602`
23. **Get to the safe.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/return_to_safe`
   - Map pin: ref `#q005_mrk_safe_mappin`; position `-2202.0546875, 1756.9931640625, 308.79959106445`
24. **Talk to T-Bug and Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/talk_tbug_jackie`
   - Map pin: ref `#q005_mrk_tbug_window_hack`; position `-2214.9333496094, 1746.1944580078, 309.47015380859`
25. **Use the switch.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/use_safe_switch`
26. **Wait for T-Bug to hack the safe.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/wait_for_hack`
27. **Wait for Jackie to check the Relic.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/wait_for_jackie_take_suitcase`
28. **Wait.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/03b_penthouse/wait_in_hideout`
29. **Return to the penthouse.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00f_return_to_penthouse`
   - Map pin: ref `#q005_mrk_landing_pad_exit_mappin`; position `-2203.4260253906, 1764.8962402344, 312.048828125`
30. **Get to the ladder.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00g_reach_ladder`
   - Map pin: ref `#q005_mp_escape_ladder`; position `-2209.1328125, 1778.3081054688, 309.08935546875`
31. **Go to the balcony door.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00h_goto_window`
   - Map pin: ref `#q005_mrk_tbug_window_hack`; position `-2214.9333496094, 1746.1944580078, 309.47015380859`
32. **Descend the ladder.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/01b_use_ladder`
   - Map pin: ref `#q005_mp_escape_ladder`; position `-2209.1328125, 1778.3081054688, 309.08935546875`
33. **Jump.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/01c_jump`
34. **Call Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/03b_call_evelyn`
35. **Talk to Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/03c_talk_to_evelyn`
36. **Fend of the attackers until Delamain arrives.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/06b_survive_until_delamain_arrives`
37. **Wait for Delamain.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/06c_wait_for_delamain_to_arrive`
38. **Get rid of the drones.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/14b_defeat_drones`
39. **Head to the lobby.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/15_enter_the_lobby`
   - Map pin: ref `#q005_mp_escape_elevator_to_lobby`; position `-2188.7358398438, 1700.8100585938, 268.24639892578`
40. **Reach the elevator to the garage.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/16_reach_garage_elevator`
   - Map pin: ref `#q005_mp_garage_elevator_out`; position `-2249.5256347656, 1726.1082763672, 20.171405792236`
41. **Wait for Jackie in the elevator.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/17_wait_jackie_in_elevator`
   - Map pin: ref `#q005_mp_lobby_elevator_inside_cab`; position `-2249.845703125, 1728.4736328125, 19.068449020386`
   - Map pin: ref `#q005_mp_escape_elevator_to_lobby`; position `-2188.7358398438, 1700.8100585938, 268.24639892578`
42. **Get to the AV landing pad.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00b_goto_landing_pad`
   - Map pin: ref `#q005_mrk_landing_pad_exit_mappin`; position `-2203.4260253906, 1764.8962402344, 312.048828125`
   - Map pin: ref `#q005_mrk_landing_pad_staircase_top_mappin`; position `-2216.857421875, 1775.4816894531, 320.0426940918`
43. **Get rid of AV security.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00c_defeat_rooftop_guards`
44. **Get to Saburo's AV.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00d_get_to_av`
45. **Hide from the guards.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/08_hide_before_guards`
   - Map pin: ref `#q005_mr_hide_spot_002`; position `-2185.732421875, 1790.3726806641, 267.99951171875`
46. **Escape the penthouse through the window.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00a_escape_penthouse`
   - Map pin: ref `#q005_mrk_tbug_window_hack`; position `-2214.9333496094, 1746.1944580078, 309.47015380859`
47. **Examine the AV.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/00d_check_av`
48. **Search the equipment in Yorinobu's penthouse.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/09_find_loot`
49. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/01_follow_jackie`
50. **Defeat the Arasaka soldiers.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/02_kill_suitcase_squad`
51. **Wait for an opportunity to take out the guards.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_escape/11_take_care_of_guards`
   - Map pin: ref `#q005_mp_guards_001`; position `-2167.0087890625, 1794.0051269531, 269.16436767578`
52. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/03_talk_to_jackie`
53. **Reach the elevator.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/04_get_to_lobby`
   - Map pin: ref `#q005_mp_escape_elevator_to_lobby`; position `-2188.7358398438, 1700.8100585938, 268.24639892578`
   - Map pin: ref `#q005_mp_escape_elevator_to_lobby_fake`; position `-2228.1123046875, 1768.9952392578, 268.33639526367`
   - Map pin: ref `#q005_mp_first_encounter_floor_004`; position `-2173.0463867188, 1774.5469970703, 268.33639526367`
   - Map pin: ref `#q005_mp_second_encounter_floor_004`; position `-2158.2561035156, 1748.6551513672, 268.33639526367`
   - Map pin: ref `#q005_mp_third_encounter_floor_004`; position `-2145.3171386719, 1738.2854003906, 268.33639526367`
   - Map pin: ref `#q005_mp_4th_encounter_floor_004`; position `-2168.9812011719, 1723.5152587891, 268.33639526367`
   - Map pin: ref `#q005_mp_5th_encounter_floor_004`; position `-2178.900390625, 1740.9675292969, 268.33639526367`
   - Map pin: ref `#q005_mp_6th_encounter_floor_005`; position `-2189.4470214844, 1759.1390380859, 268.33639526367`
   - Map pin: ref `#q005_mp_7th_encounter_floor_004`; position `-2203.6286621094, 1769.2875976563, 268.33639526367`
54. **Talk to Delamain.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/04_talk_to_delamain`
55. **Take the elevator to the garage.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/06_get_to_elevator`
   - Map pin: ref `#q005_mrk_garage_mappin`; position `-2248.3251953125, 1726.0264892578, 7.1100006103516`
56. **Enter the Delamain.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/07_get_to_delamain`
57. **Search the Arasaka officer.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/12_arasaka_officer`
58. **Deal with the guards.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_escape/13_kill_the_guards`
59. **Check in at reception.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/check_in`
60. **Place your hand on the panel.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/check_in_authentication`
61. **Connect to CCTV using Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/connect_to_cctv`
62. **Exit the Delamain.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/exit_delamain`
63. **Scan for the CCTV Access Point.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/find_cctv_access_point`
64. **Scan for an entry point for the Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/find_entry_point`
65. **Scan for a grate in the floor.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/find_flathead_entry_sec`
66. **Scan the CCTV camera in the dweller's room.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/find_flathead_passage`
67. **Scan for a path for the Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/find_flathead_passage_net`
68. **Wait.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/flathead_wait`
69. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/follow_jackie`
70. **Head to your room.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/go_to_room`
   - Map pin: ref `#q005_mrk_hotel_lobby_elevators`; position `-2229.1394042969, 1770.8049316406, 20.249578475952`
   - Map pin: ref `#q005_mrk_booked_room`; position `-2199.4208984375, 1776.3408203125, 164.35656738281`
   - Map pin: ref `#q005_mrk_booked_room_door_terminal`; position `-2197.0637207031, 1777.4440917969, 164.62773132324`
71. **Head to Yorinobu's penthouse.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/go_to_suite`
   - Map pin: ref `#q005_mrk_penthouse_entrance`; position `-2228.2746582031, 1769.3009033203, 307.99890136719`
72. **Head to the elevator.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/goto_lobby_elevator`
   - Map pin: ref `#q005_mrk_lobby_elevator_front`; position `-2228.021484375, 1768.8137207031, 20.090160369873`
73. **Hack the dweller using Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/hack_netrunner`
74. **Use Flathead to enter the dweller's room.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/open_fake_door`
75. **Use Flathead to open the ventilation grate.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/open_grate_sec_room`
76. **Get through security.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/security_gate`
77. **Sit.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/sit_table`
   - Map pin: ref `#q005_mrk_sit_table_mappin`; position `-2207.1181640625, 1787.6727294922, 163.50723266602`
78. **Stand in the scanner.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/stand_inside_scanner`
79. **Switch cam view.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/switch_cam_view`
80. **Take the control shard.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/take_control_chip`
81. **Take the elevator to the 42nd floor.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/take_elevator_to_42_floor`
   - Map pin: ref `#q005_mrk_2nd_floor_elevators`; position `-2227.9973144531, 1768.9543457031, 163.22473144531`
82. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/talk_jackie`
83. **Talk to the guard.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/talk_with_concierge`
84. **Talk to T-Bug.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/talk_with_tbug`
85. **Check out the hotel bar.**  
   `Optional` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/visit_hotel_bar`
86. **Steal the Relic.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/vip_apartment`
87. **Wait for T-Bug to link you to CCTV.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/wait_for_connection`
88. **Wait for the Flathead to breach the system.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/wait_for_flathead`
89. **Talk to Jackie and T-Bug.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/wait_for_flathead_return`
90. **Wait for Jackie to take Flathead.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/wait_for_jackie_trunk`
91. **Wait for Yorinobu to leave the penthouse.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/arasaka_undercover/wait_to_lure`
92. **Enter the Delamain.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/get_in_delamain`
   - Map pin: ref `#q005_mp_afterlife_get_into_delamain`; position `-1484.3137207031, 1048.1204833984, 23.66135597229`
93. **Stash your weapons.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/hide_weapons`
94. **Take the suit.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/loot_disguise`
95. **Put on the Militech blazer.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/put_on_blazer`
96. **Put on the Militech slacks.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/put_on_pants`
97. **Put on the Militech shoes.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/put_on_shoes`
98. **Put on the Militech suit.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/put_on_suit`
99. **Drive to Konpeki Plaza.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/talk`
100. **Wait for Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/cab_ride/wait_for_jackie`
101. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/01_talk_to_jackie`
102. **Exit the vehicle.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/02_leave_delamain`
103. **Leave the bathroom.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/exit_toilet`
   - Map pin: ref `#q005_mp_notell_bathroom_door`; position `-1133.2523193359, 1328.0311279297, 29.41318321228`
104. **Go to the bathroom.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/go_to_bathroom`
   - Map pin: ref `#q005_mp_notell_bathroom_door`; position `-1133.2523193359, 1328.0311279297, 29.41318321228`
105. **Wash your face.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/prepare`
106. **Use Delamain to escape.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/return_notell`
107. **Head to room 204.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/room`
   - Map pin: ref `#q005_mappin_no_tell_back_door`; position `-1160.8588867188, 1309.1782226563, 21.135166168213`
   - Map pin: ref `#q005_mrk_motel_room_mappin`; position `-1127.4320068359, 1321.6197509766, 29.288795471191`
108. **Talk to Dex.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/return/talk_dex`
109. **Join Dex in the booth.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/enter_meeting_capsule`
   - Map pin: ref `#q005_mrk_booth_door`; position `-1436.6569824219, 977.02954101563, 16.882549285889`
110. **Follow Dex's bodyguard.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/follow_bodyguard`
111. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/follow_jackie`
112. **Get up.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/get_up_from_bar`
113. **Head to The Afterlife.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/goto_meeting_location`
   - Map pin: ref `#q005_mrk_afterlife_entrance_mappin`; position `-1465.1549072266, 1046.9714355469, 22.759357452393`
114. **Sit next to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/join_jackie`
   - Map pin: ref `#q005_mp_afterlife_bar_chair`; position `-1442.2808837891, 1011.2370605469, 17.367206573486`
115. **Take part in the briefing.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/participate_briefing`
   - Map pin: ref `#q005_mrk_booth_door`; position `-1436.6569824219, 977.02954101563, 16.882549285889`
   - Map pin: ref `#q005_mrk_booth_seat`; position `-1437.1087646484, 978.22253417969, 17.249141693115`
   - Map pin: ref `#q005_mrk_dex_lounge_mappin`; position `-1439.294921875, 977.57635498047, 16.848819732666`
116. **Put Flathead in the briefcase.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/put_spiderbot`
117. **Talk to the bouncer.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/talk_emmerick`
118. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/talk_jackie`
119. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q005_heist/the_plan/wait_for_dex`

## The Information

- IGN walkthrough: [The Information](https://www.ign.com/wikis/cyberpunk-2077/The_Information_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1974078802`
- Quest path: `quests/main_quest/prologue/q004_braindance`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `leave/escape area`

### Journal premise

Evelyn knows more than she's willing to spill. Only question is whether she thinks we're worthy of her trust... that's where you come in. Chick's gotta be seriously well-connected to have the kind of intel we need for this op. Make sure to squeeze every last drop out of her, V. And remember – major league's just around the corner.

### Objective sequence

1. **Examine the braindance in Analysis Mode to find the Relic.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/01_analyze_braindance`
2. **In the audio layer, scan Yorinobu's phone as he talks.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/01b_eavesdrop`
3. **Listen in on Yorinobu.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/01c_listen_call`
4. **In the visual layer, scan Yorinobu's datapad while it's turned on.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/02_find_documents`
5. **Scan for thermal clues to find the Relic.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/03_use_thermal_vision`
6. **Exit the braindance when you're ready.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/braindance/04_leave_braindance`
7. **Watch the whole recording from Evelyn's point of view.**  
   `Optional` · `quests/main_quest/prologue/q004_braindance/braindance/00b_watch_recording`
8. **Scan the apartment's security systems.**  
   `Optional` · `quests/main_quest/prologue/q004_braindance/braindance/00c_scan_security`
9. **Enter the VIP room.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/enter_vip_room`
   - Map pin: ref `#q004_mp_nightclub_vip_room`; position `-1165.1831054688, 1568.7183837891, 22.915107727051`
10. **Sit at the bar and ask about Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/find_evelyn`
   - Map pin: ref `#q004_mrk_talk_to_bartender_mappin`; position `-1172.4157714844, 1571.3625488281, 23.91491317749`
11. **Talk to Evelyn in the VIP room.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/find_evelyn_vip_room`
12. **Follow Evelyn to the VIP room.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/follow_evelyn`
   - Map pin: ref `#q004_mp_nightclub_vip_room`; position `-1165.1831054688, 1568.7183837891, 22.915107727051`
13. **Follow Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/follow_evelyn_to_judy`
14. **Go to Lizzie's Bar between 6:00 PM and 6:00 AM.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/go_to_nightclub`
   - Map pin: ref `#q004_mp_nightclub_entrance`; position `-1200.9880371094, 1562.3128662109, 24.239709854126`
   - Map pin: ref `#q004_mp_nightclub_entrance_2`; position `-1190.4670410156, 1566.9528808594, 24.235906600952`
15. **Look at Judy.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/look_at_judy`
16. **Talk to Evelyn Parker.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/meet_employer`
17. **Sit.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/sit_couch`
18. **Talk to the bouncers.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/talk_bouncers`
19. **Talk to Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/talk_with_evelyn`
20. **Talk to Judy.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/talk_with_judy`
21. **Sit.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/evelyn/use_editor`
22. **Call Dex.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/call_dex`
23. **Call Jackie.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/call_jackie`
24. **Leave Judy's workshop.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/exit_judy_workshop`
25. **Follow Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/follow_evelyn_again`
26. **Talk to Judy and Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/sum_up`
27. **Talk to Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/talk_evelyn`
28. **Talk to Dex.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/finale/talk_to_dex`
29. **Test the editor controls.**  
   `Optional` · `quests/main_quest/prologue/q004_braindance/tutorial/bd_controls`
30. **Approach the barrier.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/approach_bubble`
   - Map pin: ref `#q004_mrk_bubble_mappin`; position `-1717.4774169922, -1230.4788818359, 22.146596908569`
31. **Approach the robbers.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/approach_robbers`
32. **Call T-Bug.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/call_tbug`
33. **Switch to the audio layer.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/change_layer`
34. **Switch to the visual layer.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/change_layer_back`
35. **Scan the audio source and listen.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/eavesdrop`
36. **Exit the braindance.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/eit_bd`
37. **Observe the events.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/experience_tut_bd`
38. **Follow Judy's instructions.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/follow_instructions`
39. **Pause the recording.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/pause_bd`
40. **Play the recording until you spot the gun.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/play_until_gun_visible`
41. **Reset the recording.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/reset`
42. **Reset the recording to proceed.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/reset_to_proceed`
43. **Rewind until the CCTV screen appears.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/rewind_until_cctv`
44. **Fast forward to where the customer is hit.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/rewind_until_client_ko`
45. **Fast forward to where the robber is shot.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/rewind_until_thug_shot`
46. **Scan the CCTV screen.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/scan_cctv_screen`
47. **Resume the recording to see who fired the shot.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/scan_ganger`
48. **Scan and inspect the gun.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/scan_gun`
49. **Scan and inspect the hurt customer.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/scan_npc`
50. **Rewind to the beginning.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/slow_down`
51. **Fast forward.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/speed_up`
52. **Talk to Judy.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/talk_judy`
53. **Talk to Judy and Evelyn.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/talk_judy_and_evelyn`
54. **Unpause the recording.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/unpase_bd`
55. **Unpause the recording and watch the scene.**  
   `Primary` · `quests/main_quest/prologue/q004_braindance/tutorial/upause_and_let_play`

## The Killing Moon

- IGN walkthrough: [Killing Moon](https://www.ign.com/wikis/cyberpunk-2077/Killing_Moon_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1860734169`
- Quest path: `ep1/quests/main_quest/q306_devils_bargain`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

They asked you to choose, so you chose. You weren't driven by a desire to save anyone's life – Reed and Songbird both offered you treatment. Maybe you realized that no matter what your choice, you'd be betraying someone, so the best thing you could do was not betray yourself in the process. That's why you stood by the chick who was fighting to survive, just like you. Did I get that right? Yeah, think I did. Would I have chosen any different? Luckily, I don't have to sweat over those kinds of questions. Good luck, V. You and Songbird both need it.

### Objective sequence

1. **Wait for news from Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/00_wait_for_songbird_call`
2. **Read the message from Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/01_talk_to_songbird`
3. **Meet with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/02_go_to_meeting`
   - Map pin: ref `#q306_mp_meeting_point`; position `-2316.9897460938, 306.30999755859, 11.420000076294`
4. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/02b_talk_to_reed`
5. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/03_talk_to_songbird_holo`
6. **!OBSOLETE**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/03b_debug_wait_for_song`
7. **Get in the van.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/04_enter_songbird_car`
8. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/05_talk_to_songbird`
9. **Drive to NCX.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/05b_drive_to_spaceport`
   - Map pin: ref `#q306_mp_parking_spot`; position `-3527.4797363281, 389.89016723633, 32.299999237061`
   - Map pin: ref `#q306_mp_parking_spot_midway`; position `-2395.1896972656, 367.04016113281, 32.299999237061`
10. **Leave your weapons in the van.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/05c_leave_weapons`
11. **Escape the Law.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/05d_lose_heat`
12. **Get out of the van.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/00_hook/06_exit_songbird_car`
13. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_failstate/01_talk_song`
   - Map pin: ref `#q306_mp_failstate_cell_door`; position `-3620.8564453125, 360.38629150391, 35.540000915527`
14. **Jack into the intercom.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_failstate/02_jack_in`
15. **Escape the security room.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_failstate/03_getout`
   - Map pin: ref `#q306_mp_failstate_security_door`; position `-3632.9362792969, 353.90628051758, 35.330005645752`
16. **Avoid any Orbital Air security guards.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_failstate/03b_guards`
17. **Proceed through the security gate.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/01_proceed_to_gate`
   - Map pin: ref `#q306_mp_gate`; position `-3601.8696289063, 382.52624511719, 39.10326385498`
18. **Stall to buy Songbird time to hack the biometric database.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/01aa_stall`
19. **Look at the camera.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/01b_camera`
20. **Jack in with your personal link.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/01c_link`
21. **Reach the Tycho Terminal via the maglev train tunnel.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/03_opt_maglev`
   - Map pin: ref `#q306_mp_toilet_maglev`; position `-3648.6662597656, 278.52618408203, 45.439994812012`
22. **Talk to the guard.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/01a_processed`
23. **Enter the service shaft.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/03_opt_shaft`
   - Map pin: ref `#q306_mp_mech_shaft`; position `-3663.5163574219, 351.01623535156, 37.96000289917`
   - Map pin: ref `#q306_mp_grass_shaft`; position `-3661.7163085938, 361.10610961914, 35.463264465332`
24. **Find a way to get into the Tycho Terminal.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/02_find_entrance_to_restricted`
25. **Reach the end of the service shaft.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/03_opt_shaft_proceed`
   - Map pin: ref `#q306_mp_mech_shaft_exit`; position `-3649.2563476563, 352.90625, 38.330001831055`
26. **Sneak behind the tarps.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/03_opt_tarp`
   - Map pin: ref `#q306_mp_tarps`; position `-3644.1196289063, 364.99017333984, 34.770000457764`
   - Map pin: ref `#q306_mp_tarps_001`; position `-3653.3662109375, 361.93627929688, 34.770000457764`
27. **Enter the ventilation shaft in the restroom.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/03_opt_toilet`
   - Map pin: ref `#q306_mp_toilet_shaft`; position `-3596.15625, 411.29623413086, 49.519996643066`
28. **Collect the suitcase. Use 930604 as the code.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/04_opt_luggage_checkout`
   - Map pin: ref `#q306_mp_dataterm_01`; position `-3615.2561035156, 379.31625366211, 36.020000457764`
29. **Search the suitcase from Songbird's contact.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/04_opt_luggage_loot`
   - Map pin: ref `#q306_mp_polbruk`; position `-3608.2062988281, 381.84628295898, 35.569999694824`
30. **Find a discreet spot to change into the Corp-Bud uniform.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/01_public_entry/04_opt_luggage_spot`
31. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/00_talk`
32. **Reach the rooftop elevator through the construction site.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/01_proceed_to_roof`
   - Map pin: ref `#q306_mp_elevator_restricted_area`; position `-3630.4897460938, 274.24627685547, 31.573265075684`
33. **Take the elevator to the roof.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/02_proceed_to_elevator`
   - Map pin: ref `#q306_mp_elevator_restricted_bottom`; position `-3608.4096679688, 284.57629394531, 39.723262786865`
   - Map pin: ref `#q306_mp_elevator_restricted_top`; position `-3610.6796875, 286.00628662109, 87.620002746582`
34. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/02b_talk_to_song`
35. **Help Songbird join you on the roof.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/03_drop_elevator`
   - Map pin: ref `#q306_mp_elevator_songbird`; position `-3566.2297363281, 316.03628540039, 80.183258056641`
36. **Look for Songbird on the roof below.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/03a_find_songbird`
   - Map pin: ref `#q306_mp_elevator_songbird`; position `-3566.2297363281, 316.03628540039, 80.183258056641`
37. **Search the area for a way to pull Songbird up.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/03b_find_rope`
38. **Use the fire hose to pull Songbird up.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/03c_use_hose`
39. **Defeat all Orbital Air Security staff.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/03d_get_rid_guards`
40. **Pull Songbird up onto the roof.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/04_wait_for_songbird`
41. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/05_follow_songbird`
42. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/05a_talk_to_songbird`
43. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/06_talk_to_songbird`
44. **Reequip your weapons.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/02_restricted_entry/07_reequip`
45. **Enter the ventilation shaft.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/01_hide`
   - Map pin: ref `#q306_mp_roof_hiding_spot`; position `-3616.759765625, 353.39630126953, 86.163261413574`
46. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/02_observe_scene`
47. **Hide from the guards.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/02a_hide_from_the_operators`
   - Map pin: ref `#q306_mp_tunnel_operators`; position `-3603.7858886719, 344.8427734375, 85.005058288574`
48. **Grip a fan blade and stop the fan's rotation.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/02b_stop_the_fan`
49. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/03_talk_to_songbird`
50. **Take the elevator to the roof.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/03_rooftop/09_go_to_public`
   - Map pin: ref `#q306_mp_elevator_security_to_public_bot`; position `-3618.419921875, 404.54626464844, 37.673259735107`
   - Map pin: ref `#q306_mp_elevator_security_to_public_top`; position `-3618.2998046875, 407.83630371094, 85.67325592041`
51. **Observe the situation.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/01_observe_scene`
52. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/02_get_to_the_elevator`
   - Map pin: ref `#q306_mp_elevator_security_to_public_top`; position `-3618.2998046875, 407.83630371094, 85.67325592041`
53. **Take the elevator to the roof.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/02_proceed_to_moon_terminal`
   - Map pin: ref `#q306_mp_revisited_waypoint_public`; position `-3652.8154296875, 360.2116394043, 33.725914001465`
   - Map pin: ref `#q306_mp_revisited_waypoint_restricted`; position `-3656.0754394531, 285.02163696289, 33.625915527344`
54. **Take the elevator to the main hall of the spaceport.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/02a_take_the_elevator`
   - Map pin: ref `#q306_mp_elevator_security_to_public_bot`; position `-3618.419921875, 404.54626464844, 37.673259735107`
55. **Return to the Tycho Terminal.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/02b_return_to_moon_terminal`
   - Map pin: ref `#q306_mp_elevator_restricted_area`; position `-3630.4897460938, 274.24627685547, 31.573265075684`
   - Map pin: ref `#q306_mp_revisited_waypoint_public`; position `-3652.8154296875, 360.2116394043, 33.725914001465`
   - Map pin: ref `#q306_mp_revisited_waypoint_restricted`; position `-3656.0754394531, 285.02163696289, 33.625915527344`
56. **Take the elevator to Departures.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/03_ascend_to_departures`
   - Map pin: ref `#q306_mp_revisited_elev_bot`; position `-3624.8391113281, 245.18864440918, 35.58325958252`
   - Map pin: ref `#q306_mp_revisited_elev_top`; position `-3611.3930664063, 241.80163574219, 49.075912475586`
57. **Get to the elevator.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/03_get_to_elevator`
   - Map pin: ref `#q306_mp_revisited_elev_bot`; position `-3624.8391113281, 245.18864440918, 35.58325958252`
58. **Wait for the elevator.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/03a_wait_for_elevator`
   - Map pin: ref `#q306_mp_revisited_elev_bot`; position `-3624.8391113281, 245.18864440918, 35.58325958252`
59. **Follow Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/04_proceed_through_departures`
60. **Check the room for hostiles.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/04a_check_shop`
61. **Wait for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/04b_wait_for_songbird`
62. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/05_talk_to_songbird`
63. **Find water for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/06_find_meds`
64. **Find water for Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/06a_find_water`
65. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/07_talk_to_songbird`
66. **Proceed through the Tycho Terminal.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/04_public_return/08_proceed_to_maglev`
   - Map pin: ref `#q306_mp_viewing_gallery_entrance`; position `-3586.0256347656, 238.10159301758, 49.075912475586`
   - Map pin: ref `#q306_mp_maglev_gallery_exit`; position `-3492.17578125, 175.21160888672, 49.075912475586`
67. **Fight off the chopper.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/00_get_rid_of_choppa`
68. **Reach the maglev station with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/01_reach_station`
   - Map pin: ref `#q306_mp_maglev_station_entrance`; position `-3546.0100097656, 110.10003662109, 49.090019226074`
69. **Defeat all NUSA operatives to reach the control tower.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/02a_kill_all_enemies`
70. **Protect Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/04a_defend_songbird_hacking`
71. **Pick up Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/05a_pickup_songbird`
72. **Carry Songbird to the train..**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06_aaa_put_songbird_in_train`
73. **Destroy the assault copter.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06aa_destroy_the_chopper`
74. **Survive until the train arrives.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06aa_wait_for_the_train_to_arrive`
75. **Check on Songbird in the control tower.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06aaa_hide_in_control_tower`
   - Map pin: ref `#q306_mp_control_tower`; position `-3588.3798828125, 116.60003662109, 55.100002288818`
76. **Defeat the remaining Black Ops operatives.**  
   `Optional` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06b_destroy_opposition`
77. **Reach the control tower with Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/02_reach_control_tower`
   - Map pin: ref `#q306_mp_control_tower`; position `-3588.3798828125, 116.60003662109, 55.100002288818`
78. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/03_talk_to_songbird`
79. **Jack into the control panel.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/04_connect_to_console`
80. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/05_talk_to_songbird`
81. **Tag hostiles to unleash Blackwall Ais on them.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06_target_chopper`
82. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/06a_talk_to_songbird`
83. **Get on the train.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/07_go_to_train`
84. **Board the train.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/08_enter_train`
85. **Help Songbird into the train.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/05_maglev_station/09_sit_songbird`
86. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/01_talk_to_songbird`
87. **Carry Songbird to the shuttle.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/02_carry_songbird`
   - Map pin: ref `#q306_mp_carry_songbird_to_rocket`; position `-4698.810546875, -259.47994995117, 60.099998474121`
88. **Carry Songbird to the launchpad and hand her over to Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/02a_carry_song_to_reed`
   - Map pin: ref `#q306_mp_carry_songbird_to_rocket`; position `-4698.810546875, -259.47994995117, 60.099998474121`
89. **Lay Songbird on the ground.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/02a_put_songbird_down`
   - Map pin: ref `#q306_10_sm_songbird_place`; position `-4692.609375, -267.82366943359, 60.103267669678`
90. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/03_talk_to_reed`
91. **Check on Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/03a_check_on_songbird`
92. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/03a_follow_reed`
93. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/03a_talk_to_johnny`
94. **Deal with Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/04_deal_with_reed`
95. **Pick up Songbird.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/04a_pickup_songbird`
96. **Carry Songbird to the shuttle.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/05_carry_songbird_final`
   - Map pin: ref `#q306_mp_carry_songbird_to_rocket`; position `-4698.810546875, -259.47994995117, 60.099998474121`
97. **Place Songbird in the shuttle.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/06_place_songbird`
   - Map pin: ref `#q306_mp_place_songbird_rocket`; position `-4699.5004882813, -260.76998901367, 60.559993743896`
98. **Prepare Songbird for takeoff.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/06a_prepare_songbird`
99. **Go to the observation deck.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/07_leave_for_control_room`
   - Map pin: ref `#q306_mp_launchpad_observation_deck`; position `-4678.4204101563, -289.86996459961, 60.549995422363`
100. **Sit down.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/07a_sit_down`
   - Map pin: ref `#q306_mp_launchpad_observation_deck`; position `-4678.4204101563, -289.86996459961, 60.549995422363`
101. **Watch the shuttle launch.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/08_observe_launch`
102. **Watch Reed and Songbird depart on the AV.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/08a_observe_takeoff`
103. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q306_devils_bargain/06_finale/09_talk_to_johnny`

## The Nomad

- IGN walkthrough: [The Nomad](https://www.ign.com/wikis/cyberpunk-2077/The_Nomad)
- Vanilla type: `MainQuest`
- Quest hash: `388514850`
- Quest path: `quests/main_quest/prologue/q000_nomad`
- District: Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

A good kid from Heywood with stolen corporate cargo in hand, border guards breathing down your neck and a brutal heat haze melting the horizon. This is what freedom looks like. And if smuggling's what it takes to live it, then smuggling it is. But if that's not motivation enough, there's a fat stack of eddies waiting at the end of it too. All that needs doin' is moving the package from A to B. Simple.

### Objective sequence

1. **Yo, V, every story's gotta start somewhere, right? Even if it means that "somewhere" is in the middle of nowhere and the most nova place to hang is a dusty-ass fuel stop. You abandoned your nomad family to come find the dude who hired you, to smuggle something for him 'cross the border. This guy will change your life, mano.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/01_talk_to_the_mechanic`
2. **Talk to the mechanic.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/01_talk_to_the_mechanic1`
3. **Fix the engine.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/02_fix_car_engine`
   - Map pin: ref `#q000_nomad_mp_car_engine`; position `-3969.1062011719, -6481.6005859375, 76.734985351563`
4. **Get in the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/03_get_into_car`
5. **Start the engine.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/04_start_car_engine`
6. **Get out of the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/04b_get_out_of_the_car`
7. **Talk to the mechanic.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/04c_talk_to_mechanic`
8. **Connect to the telecom tower.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/04d_connect_radio`
9. **Talk to the sheriff.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/05_talk_to_sheriff`
10. **Leave the garage.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/06_leave_the_garage`
   - Map pin: ref `#q000_nomad_mp_exit_garage`; position `-3969.796875, -6487.1811523438, 77.558586120605`
11. **Go to the telecom tower.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/07_go_to_radio_tower`
   - Map pin: ref `#q000_nomad_mp_radio_tower_area`; position `-4087.9453125, -6626.4643554688, 89.234962463379`
12. **Climb the telecom tower and locate the control box.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/08_climb_the_tower`
   - Map pin: ref `#q000_nomad_mp_radio_tower_top`; position `-4073.7810058594, -6639.7138671875, 111.67686462402`
13. **Connect your sat phone to the telecom tower.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/09b_jack_in`
   - Map pin: ref `#q000_nomad_mp_circut_box`; position `-4073.7800292969, -6639.7138671875, 111.42002868652`
14. **Call McCoy.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/10_call_fixer`
15. **Talk to McCoy.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/10b_talk_to_fixer`
16. **Return to the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/01_roadhouse/11_return_to_car`
17. **Head to the meeting place.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/01_drive_to_the_meeting_spot`
   - Map pin: ref `#q000_mp_protein_farm_meeting`; position `-3239.349609375, -6736.6547851563, 108.39653015137`
18. **Get out of the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/02_get_out_of_car`
19. **Meet Jackie Welles.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/02b_look_for_jackie`
20. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/03_talk_to_jackie`
21. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/04_follow_jackie`
22. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/05_talk_to_jackie`
23. **Drive closer to the trailer.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/05b_bring_around_the_car`
   - Map pin: ref `#q000_mp_protein_farm_meeting`; position `-3239.349609375, -6736.6547851563, 108.39653015137`
24. **Open the trunk.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/06_open_trunk`
   - Map pin: ref `#q000_nomad_mp_jackie_trailor_car_trunk`; position `-3240.927734375, -6736.9306640625, 109.22388458252`
25. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/08b_talk_to_jackie`
26. **Get in the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/02_meeting_jackie/09_get_into_car`
27. **Drive to the border.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/01_drive_to_the_border`
   - Map pin: ref `#q000_nomad_mp_border_crossing`; position `-2836.1555175781, -5663.158203125, 102.69371032715`
28. **Return to the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/01b_get_back_to_car`
29. **Drive into the checkpoint.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/02_enter_checkpoint`
   - Map pin: ref `#q000_nomad_mp_border_crossing_checkpoint`; position `-2823.0576171875, -5645.8120117188, 101.40409088135`
30. **Talk to Jackie while waiting for the security check to finish.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03_wait_for_security_check_to_end`
31. **Get out of the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03b_leave_the_car`
32. **Enter the border security building.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03bb_enter_the_building`
   - Map pin: ref `#q000_nomad_mp_border_office_hall`; position `-2809.5212402344, -5660.33984375, 102.46190643311`
33. **Deposit your weapons at the front desk.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03bbb_leave_weapon`
   - Map pin: ref `#q000_nomad_mp_border_leave_weapon`; position `-2810.1918945313, -5662.87109375, 102.21862792969`
34. **Head to room 2.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03c_go_to_office`
   - Map pin: ref `#q000_nomad_mp_border_office`; position `-2805.4689941406, -5668.2353515625, 101.92049407959`
   - Map pin: ref `#q000_nomad_mp_border_office_door`; position `-2808.2995605469, -5667.4248046875, 102.61148071289`
35. **Sit.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03d_sit_down`
36. **Talk to the border guard.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03e_talk_to_officer`
37. **Collect your weapons at the front desk.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/03f_pick_up_weapon`
   - Map pin: ref `#q000_nomad_mp_border_leave_weapon`; position `-2810.1918945313, -5662.87109375, 102.21862792969`
38. **Return to the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/04_get_back_to_car`
   - Map pin: ref `#q000_nomad_mp_before_chase_car_door`; position `-2824.072265625, -5648.66796875, 101.93158721924`
39. **Depart the border crossing.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/04b_drive_with_jackie`
40. **Fight off your pursuers.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/04c_stop_arasaka`
41. **Lean out.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/05_lean_out`
42. **Go to a safe location with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/03_border/07_to_hideout`
43. **Get out of the car.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/04_hideout/00_get_out_of_car`
44. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/04_hideout/01_talk_to_jackie`
45. **Take the iguana.**  
   `Primary` · `quests/main_quest/prologue/q000_nomad/04_hideout/02_take_the_iguana`

## The Pickup

- IGN walkthrough: [The Pickup](https://www.ign.com/wikis/cyberpunk-2077/The_Pickup_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `796156855`
- Quest path: `quests/main_quest/prologue/q003_maelstrom`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Journal premise

Every corp has a Gilchrist. First he steals from them, turns a fat profit on the goods, lies about it, narrowly avoids the chopping block, gets rid of all witnesses, makes someone else take the fall from him, and to top it all off – he gets a promotion. Can't help feeling sorry for the Maelstrom gonks in this scenario... but only a little.

### Objective sequence

1. **Pass through the maintenance tunnel.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/01_leave_office`
   - Map pin: ref `#q003_mp_conveyor_platform`; position `-887.98168945313, 2210.2966308594, 69.239540100098`
2. **Talk to Dum Dum.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/06a_talk_to_dumdum`
3. **Take the s-keef from Dum Dum.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/06b_take_skiff_dumdum`
4. **Find the case containing the Flathead.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/10_find_flathead`
5. **Defeat the Militech agents.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/19_defeat_militech`
6. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/finish`
7. **Open the case.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/finish1`
   - Map pin: ref `#q003_mp_flathead_box_no_deal`; position `-869.81286621094, 2197.5913085938, 61.863216400146`
8. **Sneak past Royce.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/04b_sneak_past_royce`
   - Map pin: ref `#q003_mp_maelstrom_exit`; position `-761.11712646484, 2165.3891601563, 53.534290313721`
9. **Find a way to free Brick.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/14_save_brick`
10. **Turn on the production line to clear passage.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/02_turn_on_conveyor`
   - Map pin: ref `#q003_mp_conveyor_button`; position `-889.70697021484, 2210.9067382813, 69.285202026367`
11. **Use code 9691 to free Brick.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/14_save_brick1`
   - Map pin: ref `#q003_mp_brick_prison_door_terminal`; position `-876.23498535156, 2265.3872070313, 59.307640075684`
12. **Escape from All Foods.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/03_escape_allfoods`
   - Map pin: ref `#q003_mp_lab_entrance`; position `-884.67816162109, 2225.1318359375, 61.831359863281`
   - Map pin: ref `#q003_mp_transition`; position `-846.26818847656, 2202.392578125, 55.788707733154`
   - Map pin: ref `#q003_mp_garage`; position `-812.41625976563, 2195.4350585938, 54.236301422119`
   - Map pin: ref `#q003_mp_allfoods_exit`; position `-783.91967773438, 2186.4609375, 53.696804046631`
13. **Defeat Royce and his crew.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/04_kill_royce`
14. **Follow Dum Dum.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/06_follow_dumdum`
15. **Talk to Brick.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/15_talk_to_brick`
16. **Disarm the trap preventing Brick's escape.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/15_talk_to_brick1`
17. **Talk to Brick.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/15_talk_to_brick2`
18. **Leave the premises of All Foods.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/03_escape/05_leave_allfoods`
   - Map pin: ref `#q003_mp_maelstrom_exit`; position `-761.11712646484, 2165.3891601563, 53.534290313721`
   - Map pin: ref `#q003_mp_maelstrom_exit_jackie`; position `-765.49694824219, 2163.5498046875, 53.534290313721`
19. **Dismantle the trap.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/03_escape/15_talk_to_brick5`
20. **Wait for Jackie by All Foods.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/00_wait_jackie`
   - Map pin: ref `#q003_mp_wait_jackie_entrance`; position `-738.84057617188, 2159.7941894531, 53.737682342529`
21. **Meet with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/01_meet_jackie`
22. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/01_meet_jackie1`
23. **Enter All Foods with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/01_meet_jackie2`
24. **Go to the gate of All Foods.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/03_go_to_intercom`
   - Map pin: ref `#q003_mp_allfoods_intercom`; position `-769.76281738281, 2203.5375976563, 52.383926391602`
25. **Use the intercom.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/03_go_to_intercom1`
   - Map pin: ref `#q003_mp_allfoods_intercom`; position `-769.76281738281, 2203.5375976563, 52.383926391602`
26. **Talk with Maelstrom via the intercom.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/04a_talk_through_intercom`
   - Map pin: ref `#q003_mp_allfoods_intercom`; position `-769.76281738281, 2203.5375976563, 52.383926391602`
27. **Get in the elevator.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/06_go_to_elevator`
   - Map pin: ref `#q003_mp_elevator`; position `-863.78643798828, 2221.2551269531, 55.915061950684`
28. **Enter the elevator with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/06_go_to_elevator1`
   - Map pin: ref `#q003_mp_elevator`; position `-863.78643798828, 2221.2551269531, 55.915061950684`
29. **Get to main production floor of All Foods.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/06_go_to_elevator2`
   - Map pin: ref `#q003_mp_main_hall`; position `-856.35522460938, 2229.0627441406, 55.915061950684`
30. **Wait with Jackie in the elevator.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/06_go_to_elevator3`
   - Map pin: ref `#q003_mp_elevator`; position `-863.78643798828, 2221.2551269531, 55.915061950684`
31. **Meet with Royce.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/07_get_to_meeting`
   - Map pin: ref `#q003_mp_meeting`; position `-867.70031738281, 2216.4658203125, 61.637512207031`
32. **Go to Royce's office.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/07_get_to_meeting1`
   - Map pin: ref `#q003_mp_meeting`; position `-867.70031738281, 2216.4658203125, 61.637512207031`
33. **Talk to the Maelstromers.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/08_make_deal`
34. **Sit on the couch.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/08_make_deal1`
35. **Attack a Maelstromer.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/09_attack_any_maelstrom`
36. **Talk to the Maelstromers.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/08_make_deal2`
37. **Defeat the Maelstromers.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/10_kill_deal`
38. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/11_talk_to_jackie`
39. **Take the Flathead.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/12_get_raven`
   - Map pin: ref `#q003_mp_flathead_box`; position `-867.26995849609, 2211.1672363281, 61.356212615967`
   - Map pin: ref `#q003_mp_flathead_box_no_deal`; position `-869.81286621094, 2197.5913085938, 61.863216400146`
40. **Talk to Dum Dum.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/15_talk_to_dumdum`
41. **Take the elevator down with Dum Dum.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/16_dumdum_elevator`
42. **Defeat Maelstrom.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/17_survive_main_hall`
43. **Talk to Anthony Gilchrist.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/01_talk_to_gilchrist`
44. **Call Dex.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/call_dex`
45. **Talk to Dex.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/call_dex1`
46. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/finish`
47. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/finish1`
48. **Talk to Meredith Stout.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/maelstrom_end/militech`
49. **Call Militech agent Meredith Stout.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/militech/01_call_militech`
50. **Talk to the Militech agent.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/militech/02_meet_militech1`
51. **Remove the virus from the chip.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/militech/04_remove_malware`
52. **Call Jackie.**  
   `Primary` · `quests/main_quest/prologue/q003_maelstrom/militech/00_call_jackie`
53. **Meet with the Militech agent.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/militech/02_meet_militech`
54. **Wait for the Militech agent.**  
   `Optional` · `quests/main_quest/prologue/q003_maelstrom/militech/02_meet_militech2`
   - Map pin: ref `#q003_mp_sit_storm_drain`; position `-814.31439208984, 1969.1778564453, 30.374713897705`

## The Rescue

- IGN walkthrough: [The Rescue](https://www.ign.com/wikis/cyberpunk-2077/The_Rescue_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `771252797`
- Quest path: `quests/main_quest/prologue/q001_intro`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `hack/breach/download`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`

### Journal premise

Wakako Okada's got us a gig. Fixer got an SOS call from one of her clients, Sandra Dorsett. All signs point to her having been plucked off the street by scavengers. Motherfuckers are in the biz of carving people up and selling their implants on the black market. Think it's time we paid them a visit. Whaddaya say, ese?

### Objective sequence

1. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/back_to_jackie`
2. **Hack the radio.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/distraction_tutorial`
3. **Hack the camera.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/hack_camera`
4. **Call Wakako.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/call_wakako`
5. **Examine the woman's body.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/check_dead_girl`
6. **Check for vital signs.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/check_girl`
7. **Examine the body.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/check_the_bodies`
8. **Find Sandra Dorsett.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/deal_scavengers`
9. **Defeat all enemies.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/deal_with_the_rest_however_you_want`
10. **Wait while staying unnoticed.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/wait_until_scavs_pass_you`
11. **Defeat the scavengers.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/deal_with_the_scavengers`
12. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/follow_jackie`
13. **Defeat the scavenger leader.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/get_rid_of_the_scavengers_leader`
   - Map pin: ref `#q001_mp_boss_door_hack_icon`; position `-457.14517211914, 416.46630859375, 133.49600219727`
14. **Get to an Access Point.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/get_to_access_point`
15. **Head to the apartment.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/get_to_apartment`
16. **Go up to the terminal.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/get_to_door`
17. **Get to the next room.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/get_to_takedown_room`
   - Map pin: ref `#q001_mp_door_takedown_room`; position `-483.37731933594, 389.61911010742, 133.46006774902`
   - Map pin: ref `#q001_mp_takedown_room_new`; position `-475.97064208984, 389.85208129883, 132.01976013184`
18. **Return to the main room.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/go_back_to_main_room`
19. **Search the bathroom.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/go_bathroom`
20. **Enter the elevator.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/goto_elevator1`
   - Map pin: ref `#q001_mp_lift_terminal`; position `-437.00531005859, 415.62509155273, 133.14128112793`
21. **Breach the Access Point.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/hack_access_point`
22. **Carry Sandra to the terrace.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/help_girl_av`
23. **Save Sandra.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/help_sandra_with_tbug`
24. **Sneak up to the scavenger.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/approach_scavenger_remaining_in_stealth`
25. **Meet with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/meet_jackie`
26. **Place Sandra on the stretcher.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/put_girl_stretcher`
27. **Save Sandra Dorsett**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/rescue_girl`
28. **Shoot the scavenger through wall.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/shoot_boss_through_wall`
29. **Wait by the door to the terrace.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/trauma_team_back`
   - Map pin: ref `#q001_mp_trauma_team_move_away`; position `-459.3678894043, 428.28271484375, 132.0103302002`
30. **Distract the scavenger leader.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/distract_boss`
31. **Neutralize the scavenger.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/double_takedown_tutorial`
32. **Hide the body.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/drag_the_body_out_of_the_way`
33. **Go onto the terrace.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/go_balcony`
34. **Hide the body in freezer.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/hide_the_body`
35. **Use the path marked by T-Bug.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/use_stealth_path`
36. **Wait for T-Bug to hack the door.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/wait_door`
37. **Wait for Trauma Team to help Sandra.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/wait_girl_tt`
38. **Hide from the scavengers.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/hide_and_let_the_scavs_pass_you`
39. **Neutralize the scavenger.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger`
40. **Neutralize the scavenger.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger2`
41. **Hide from the scavengers.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/mission0/wait_for_the_scavengers_to_finish`
42. **Scan the area for a weak point.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/scan_weak_spot`
43. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/talk_jackie`
44. **Talk to T-Bug.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/talk_to_tbug`
45. **Talk to Wakako.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/talk_to_wakako`
46. **Hack the door.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/tutorial_hack_door`
   - Map pin: ref `#q001_mp_door_mission0_left`; position `-467.3798828125, 376.79168701172, 133.3688659668`
47. **Wait for Trauma Team.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/wait_tt_arrival`
48. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/mission0/what_next_jackie`
49. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/premission0/01_talk_to_jackie`
50. **Exit the car.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/premission0/01b_exit_the_car`
51. **Follow Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/premission0/02_follow_jackie`
52. **Enter the elevator with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/premission0/03_enter_the_elevator`
   - Map pin: ref `#q000_vr_mp_scav_elevator`; position `-438.29791259766, 414.02352905273, 24.403137207031`
   - Map pin: ref `#q000_vr_mp_tbug_lift_hack`; position `-439.6162109375, 413.6555480957, 24.739242553711`
53. **Wait for Jackie in the elevator.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/00_wait_for_jackie`
54. **Press for the garage level.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/01_get_to_garage`
55. **Wait.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/01a_get_to_garage_floor`
56. **Get into the passenger seat.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/02_get_inside_car`
57. **Ride back with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/03_ride_w_jackie`
58. **Defeat the scavengers.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/03b_fight_off_scavs`
59. **Exit the car.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/04_leave_the_car`
60. **Go home.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/05_go_to_vroom`
   - Map pin: ref `#q001_mp_elevator_terminal_mb_grg`; position `-1375.8159179688, 1289.6895751953, 31.10661315918`
   - Map pin: ref `#q001_mp_v_room`; position `-1383.2524414063, 1270.5031738281, 123.06470489502`
61. **Go to bed.**  
   `Primary` · `quests/main_quest/prologue/q001_intro/ride_to_mb/06_sleep`
   - Map pin: ref `#q001_go_to_sleep`; position `-1377.5382080078, 1275.5920410156, 123.72491455078`
62. **Check your weapons stash.**  
   `Optional` · `quests/main_quest/prologue/q001_intro/ride_to_mb/05a_stash`
   - Map pin: ref `#q001_mp_vroom_stash`; position `-1380.9011230469, 1262.1702880859, 124.84394836426`

## The Ride

- IGN walkthrough: [The Ride](https://www.ign.com/wikis/cyberpunk-2077/The_Ride_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3890953698`
- Quest path: `quests/main_quest/prologue/q001_02_dex`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `vehicle sequence`

### Journal premise

High risk, high reward – as Dexter DeShawn likes to say. First rule of The Afterlife. So this is it, V. Time to go in, grab the bull by the horns and make a name for ourselves. But first, let's hear what Dex DeShawn has to say.

### Objective sequence

1. **Call Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/00_call_jackie`
2. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/00_talk_jackie`
3. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/ask_jackie`
4. **Get into Dex's limo.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/enter_dex_car`
5. **Meet with Dex.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/go_to_dex`
6. **Exit the limo.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/leave_dex_car`
7. **Talk to Dex.**  
   `Primary` · `quests/main_quest/prologue/q001_02_dex/dex/ride_with_dex`

## The Ripperdoc

- IGN walkthrough: [The Ripperdoc](https://www.ign.com/wikis/cyberpunk-2077/The_Ripperdoc_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1377961062`
- Quest path: `quests/main_quest/prologue/q001_01_victor`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `search/investigate`, `retrieve/collect item`, `vehicle sequence`

### Journal premise

If you're on the hunt for chrome, you won't find a better ripper than Viktor. Well, all right, maybe you could, but you sure as hell can't afford them, ése. Not like Vik can afford you, either, but you're lucky he's got a soft spot – says you've got a good heart, like him. But before we pay ol' Vik a visit, we gotta decide what comes next.

### Objective sequence

1. **Put on the jacket.**  
   `Optional` · `quests/main_quest/prologue/q001_01_victor/megabuilding/get_jacket`
2. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/call_jackie`
3. **Get in the driver's seat.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/get_inside_car`
4. **Meet with Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/go_to_jackie`
5. **Call up your car.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/summon_car`
6. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/talk_jackie`
7. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/megabuilding/talk_jackie_person`
8. **Check your weapons stash.**  
   `Optional` · `quests/main_quest/prologue/q001_01_victor/megabuilding/05a_stash`
   - Map pin: ref `#q001_mp_vroom_stash`; position `-1380.9011230469, 1262.1702880859, 124.84394836426`
9. **Take the gun.**  
   `Optional` · `quests/main_quest/prologue/q001_01_victor/megabuilding/get_gun`
10. **Check your email.**  
   `Optional` · `quests/main_quest/prologue/q001_01_victor/megabuilding/read_email_muamar`
11. **Drive to the ripperdoc.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/go_to_rd_by_car`
12. **Meet with the ripperdoc.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/go_to_ripperdoc`
13. **Install new cyberware.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/install_cyberware`
14. **Scan Viktor.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/scan_viktor`
15. **Take a seat.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/sit_chair`
16. **Talk to Viktor.**  
   `Primary` · `quests/main_quest/prologue/q001_01_victor/ripperdoc/talk_to_viktor`

## The Space in Between

- IGN walkthrough: [The Space In Between](https://www.ign.com/wikis/cyberpunk-2077/The_Space_In_Between_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `4031805797`
- Quest path: `quests/main_quest/act_01/q105_02_jigjig`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `combat/neutralize`

### Objective sequence

1. **Go to Fingers' clinic.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/02b_go_to_clinic`
   - Map pin: ref `#q105_mp_jigjig_fingers`; position `-588.27105712891, 804.80474853516, 20.201585769653`
2. **Sit and talk to the joytoys.**  
   `Optional` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/04c_talk_prostitutes`
3. **Find a way into Fingers' office.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/04b_wait_queue`
4. **Wait until Fingers finishes operating.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/04d_wait_queue`
5. **Call Judy.**  
   `Optional` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/01a_call_judy`
6. **Defeat the thugs.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/defeat_goons`
7. **Enter the clinic.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/enter_fingers`
8. **Interrogate Fingers.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/evelyn`
9. **Follow Fingers into his office.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/follow_fingers`
10. **Talk to Judy.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/info_judy`
11. **If I've learned one thing from joyhouses, it's to quit while the going's good. Stare at those fake smiles too long, and all you'll see is misery. As far as clubs go they're all pretty pathetic, but at least it's in their own way. You know the chances of finding Evelyn are close to zilch, right? Like that's gonna change your mind... Anyway, let's go pay a visit to this so-called Fingers. But if we don't find Parker, you owe me a drink.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/location`
   - Map pin: ref `#q105_mp_jigjig_entrance_01`; position `-641.42657470703, 886.84326171875, 19.841585159302`
12. **Find Fingers' clinic.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/look_for_address`
   - Map pin: ref `#q105_mp_jigjig_fingers`; position `-588.27105712891, 804.80474853516, 20.201585769653`
13. **Talk to Fingers.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/meet_fingers`
14. **Talk to the thugs.**  
   `Primary` · `quests/main_quest/act_01/q105_02_jigjig/jigjig/talk_goons`

## The Streetkid

- IGN walkthrough: [The Street Kid](https://www.ign.com/wikis/cyberpunk-2077/The_Street_Kid)
- Vanilla type: `MainQuest`
- Quest hash: `150337889`
- Quest path: `quests/main_quest/prologue/q000_street_kid`
- District: Heywood
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Journal premise

If there was an ad for Night City, it'd have Kirk's dumb, grinning face on it. He's slick, thinks he's smarter than he really is and is kind of an asshole, but whenever you call him, he's got the next Big Job that'll rake in millions – like stealing a car from a secure parking garage. 'Cause obviously the millionaires of the future are sitting in the Coyote Cojo scarfing down chili burgers... right?

### Objective sequence

1. **Hows it feel bein' back home, V? C'mon, admit it – you missed Heywood. What, between all the dealers, hookers and total lack of opportunities, it's got its charm, don't it? You're born in Heywood, you die in Heywood. Unless you're one of the lucky ones, that is. What about you, mano? That include you?**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/01_meet_your_fixer`
   - Map pin: ref `#q000_kid_mk_stairs`; position `-1249.8081054688, -1006.2229614258, 13.107246398926`
2. **Talk to the bartender.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/01a_opt_talk_to_bartender`
3. **Talk to Kirk.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/02_talk_to_kirk`
4. **Sit with Kirk.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/03_sit_down`
   - Map pin: ref `#q000_kid_mk_chair`; position `-1268.6687011719, -989.39086914063, 16.648914337158`
5. **Leave the bar.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/05_leave_coyote`
   - Map pin: ref `#q000_kid_mp_coyote_exit`; position `-1236.8966064453, -1003.6744384766, 12.617245674133`
6. **Go to Embers.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/05a_get_to_the_street`
   - Map pin: ref `#q000_kid_mp_street`; position `-1299.4595947266, -1006.0581054688, 13.567246437073`
7. **Talk to Padre.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/06_talk_with_marcus`
8. **Get in Padre's car.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/07_get_inside_the_car`
   - Map pin: ref `#q000_kid_mk_car_door`; position `-1286.9919433594, -1011.173034668, 13.407246589661`
9. **Ride with Padre to Embers.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/08_drive_downtown`
10. **Get out of the car.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/09_get_out`
11. **Take the elevator to the garage.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/01_new_job/10_go_inside_elevator`
   - Map pin: ref `#q000_kid_mk_elevator`; position `-1826.4416503906, -558.23162841797, 8.6774559020996`
   - Map pin: ref `#q000_kid_mp_garage_entrance`; position `-1840.724609375, -528.09906005859, -3.3983161449432`
   - Map pin: ref `#q000_kid_mk_elevator`; position `-1826.4416503906, -558.23162841797, 8.6774559020996`
12. **Enter the underground parking lot.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/01_find_garage_entrance`
   - Map pin: ref `#q000_kid_mp_garage_entrance`; position `-1840.724609375, -528.09906005859, -3.3983161449432`
13. **Get in the car.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/05_get_into_the_car`
   - Map pin: ref `#q000_kid_mrk_corpo_car`; position `-1859.5509033203, -471.33810424805, -4.9816098213196`
14. **Talk to the thief.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/06_defend_yourself`
15. **Talk to the police officers.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/07_confront_the_corporate`
16. **Find Rick.**  
   `Optional` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/02_talk_with_guard`
17. **Find the Rayfield.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/03_find_the_car`
18. **Disable the lock using Kirk's device.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/04_connect`
   - Map pin: ref `#q000_kid_mrk_corpo_car`; position `-1859.5509033203, -471.33810424805, -4.9816098213196`
19. **Steal the Rayfield.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/02_steal_car/05a_steal_car`
20. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/prologue/q000_street_kid/03_return/01_talk_with_jackie`

## Things Done Changed

- IGN walkthrough: [Things Done Changed](https://www.ign.com/wikis/cyberpunk-2077/Things_Done_Changed_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3310831952`
- Quest path: `ep1/quests/main_quest/q307_tomorrow`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `deliver/deposit item`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Know what you're thinkin' – all is lost, right? Could be true in some way, I guess. But it's just as true that you get to live on.\nDunno, somebody out there might be lookin' out for you to come back. Start callin' – friends, acquaintances, associates, even. Then get back to NC. You'll build a new life for yourself, one with new meaning, I know you will. Or you'll find some traces of your old life and purpose.\nAnd if none of that pans out, set out and see what's beyond the horizon. 'Cause there's always somethin' there, V. Always.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/01_talk_reed`
2. **Listen to the radio show.**  
   `Optional` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/06a_listen_radio`
3. **Go to the window.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/02_go_chair`
4. **Call other friends.**  
   `Optional` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/03b_call_more_friends`
5. **Stand up.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/02a_get_up`
6. **Call your friends and decide who to visit.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/03_call_friends`
7. **Use the intercom to leave the clinic.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/04_call_receptionist`
8. **Talk to Delamain.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/04_talk_delamain`
9. **Meet with Viktor.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/05_meet_viktor`
10. **Wait for the medical orderly.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/05_wait_pickup`
11. **Exit the cab.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/01_hospital_cabride/06b_leave_delamain`
12. **Talk to the receptionist.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/00_talk_zetatech`
13. **Talk to Viktor.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/01_talk_viktor`
14. **Sit in the ripper's chair.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/01b_sit_viktor`
   - Map pin: ref `#q307_mp_viktor_chair`; position `-1546.6688232422, 1234.6737060547, 12.300699234009`
15. **Leave Viktor’s clinic.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/02_leave_viktor`
16. **Return to Delamain.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/03_return_delamain`
17. **Deal with the back-alley thugs.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/03a_deal_thugs`
18. **Wait for help.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/03b_wait_help`
19. **Talk to Misty.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/04_talk_misty`
20. **Walk with Misty.**  
   `Primary` · `ep1/quests/main_quest/q307_tomorrow/02_mistys_alley/05_take_walk`

## Through Pain to Heaven

- IGN walkthrough: [Through Pain to Heaven](https://www.ign.com/wikis/cyberpunk-2077/Through_Pain_to_Heaven_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `172105197`
- Quest path: `ep1/quests/main_quest/q306_reed_epilogue`
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`

### Journal premise

Silence... Finally. Every time I think back to that first meeting with Songbird, I feel like I'm gonna blow chunks. The moment she made me fade out... A feeling worse than death. Believe me, I'm an expert on the subject. But now? Nothing. Not a peep. Not even an echo. As if she's far, far away, or... I dunno. Looks like it's just the two of us again. But for how long now, I wonder.

### Objective sequence

1. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/0000_read_reed`
2. **Reply to Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/000_answer_reeds_message`
3. **Find something to do until Reed contacts you.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed`
4. **Answer the holocall.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/01_answer_phone`
5. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/02_talk_to_reed`
6. **Meet Reed at the CHOOH2 station.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03_meet_reed`
   - Map pin: ref `#q306_mp_gas_station`; position `-151.87364196777, -1973.1083984375, 6.5958490371704`
7. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03a_wait_for_reed`
   - Map pin: ref `#q306_wait_reed`; position `-149.16003417969, -1956.3499755859, 7.0299997329712`
8. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/04_talk_to_reed`
9. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny`
10. **(unnamed objective)**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/06_decrypt_shard`
11. **Read Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_00_read`
12. **Reply to Reed's message.**  
   `Primary` · `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_01_respond`

## Totalimmortal

- IGN walkthrough: [Totalimmortal](https://www.ign.com/wikis/cyberpunk-2077/Totalimmortal_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `1087901543`
- Quest path: `quests/main_quest/act_01/q113_corpo`
- District: City Center
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `choice/decision`

### Objective sequence

1. **Follow Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00_follow_hanako`
2. **Go to hell, V. You're on your own, got that? Stage is all yours. I'll just stand in the wings and watch you meet certain death, 'cause that's how this little coup against Yorinobu is gonna end. That is, unless our porcelain doll's got any aces up her sleeve. But if things go south, just jump out the window. Don't give them the satisfaction – don't let the fuckers take you alive.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00b_get_out`
3. **Talk to Hanako and Saburo.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00c2_talk`
4. **Talk to Jackie.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00c3_talk_jackie`
5. **Talk to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00c_talk_to_hanako`
6. **Enter the elevator.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00d_get_in_elevator`
   - Map pin: ref `#q113_mp_office__secret_elevator`; position `-1358.4375, 110.13232421875, 550.38214111328`
7. **Sit next to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/00e_sit_mikoshi`
   - Map pin: ref `#q113_mp_mikoshi_seat`; position `-1367.1883544922, 122.19689178467, 417.79721069336`
8. **Give your testimony.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/01_meeting`
9. **Find a seat.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/01a_shoo`
10. **Sit next to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/01b_sit`
11. **Fend off the attackers.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/02_survive`
12. **Defeat Yorinobu's forces.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/02b_rest`
13. **Talk to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/02c_hanako`
   - Map pin: ref `#q113_mp_office__secret_elevator`; position `-1358.4375, 110.13232421875, 550.38214111328`
14. **Well I'll be a corporat on a stick. Yorinobu tried to take out the entire Arasaka board in one fell swoop. I'd buy the gonk a beer if I could. No doubt, the sight of Arasakas lunging at each other's throats is a thing of beauty, but it kinda throws a wrench in our plans. Now you gotta take care of Yorinobu on Hanako's terms. Looks like Lil Sis is done playing around – crazy Big Bro's gonna give up Arasaka Tower one way or the other. Still, isn't it weird that we're not allowed to hurt a hair on his pretty little head after he marked her for DEATH? Maybe Hanako wants to "neutralize" him herself? One thing's for sure – the path to Yorinobu's office leads through a lot of levels... and a LOT of bodies.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/03_elevator`
   - Map pin: ref `#q113_mp_jungle_to_atrium_elevator`; position `-1387.2867431641, 162.64033508301, 388.302734375`
15. **Wait for Takemura.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/02_arasaka_tower/03b_wait_takemura`
16. **Reach the elevator.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/05_top_atrium/01_get_to_elevator`
17. **Head to Yorinobu's office.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/02_go_to_boss`
   - Map pin: ref `#q113_mp_ceo_floor_door_001`; position `-1442.1162109375, 190.64462280273, 566.50604248047`
   - Map pin: ref `#q113_mp_ceo_floor_door_002`; position `-1442.3654785156, 184.70979309082, 566.53607177734`
   - Map pin: ref `#q113_mp_bossroom`; position `-1443.7502441406, 151.94973754883, 565.34600830078`
18. **Defeat Smasher's forces.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/03c_defeat_men`
19. **Talk to Hanako.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/05b_hanako`
20. **Take the elevator down.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/06_kasai`
   - Map pin: ref `#q113_mp_yorinobu_elevator`; position `-1430.6127929688, 73.947204589844, 570.31896972656`
21. **Decide Smasher's fate.**  
   `Optional` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/03b_decide_adam`
22. **Defeat Yorinobu's forces.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/02b_defeat_men`
   - Map pin: ref `#q113_mp_ceo_floor_turret_001`; position `-1434.0592041016, 191.4794921875, 569.23101806641`
   - Map pin: ref `#q113_mp_ceo_floor_turret_002`; position `-1450.6236572266, 191.92953491211, 569.23101806641`
   - Map pin: ref `#q113_mp_ceo_floor_turret_003`; position `-1448.1379394531, 212.38446044922, 569.12603759766`
   - Map pin: ref `#q113_mp_ceo_floor_turret_004`; position `-1434.7277832031, 212.3844909668, 569.12603759766`
23. **Defeat Adam Smasher.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/03_defeat_adam`
24. **Confront Yorinobu.**  
   `Primary` · `quests/main_quest/act_01/q113_corpo/06_ceo_floor/05_confront_yorinobu`
   - Map pin: ref `#q113_mp_ceo_floor_door_003`; position `-1444.7744140625, 128.0251159668, 570.64105224609`
   - Map pin: ref `#q113_mp_ceo_floor_door_004`; position `-1446.3181152344, 91.740180969238, 570.50103759766`

## Transmission

- IGN walkthrough: [Transmission](https://www.ign.com/wikis/cyberpunk-2077/Transmission_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `495629330`
- Quest path: `quests/main_quest/act_01/q110_03_cyberspace`
- District: Pacifica
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `follow/escort`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Journal premise

It actually fucking worked. Working with the Voodoo Boys, Brigitte… It leads us straight to Alt. Looks like your troubles are over, kid. Fixing your head is gonna be a walk in the park for Alt, that I guarantee. You just do what Brigitte says for now – I'll handle the rest.

### Objective sequence

1. **Meet Brigitte behind the chapel altar.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/00_meet_brigitte`
   - Map pin: ref `#q110_mp_behind_altar`; position `-1733.6878662109, -1902.6057128906, 63.782886505127`
2. **Follow Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/01_follow_queen`
3. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/01_talk_to_queen`
4. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/02_talk_to_queen`
5. **Return to Brigitte to accept her offer.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/03_accept_offer`
6. **Get in the ice bath.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/03_sit_down_in_chair`
7. **Call Brigitte to accept her help.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/04_call_brigitte`
8. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/04_talk_to_alt`
9. **Wait for the connection.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/05_talk_to_queen`
10. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/05b_talk_to_queen`
11. **Unblock Johnny's memories.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/05c_unlock_memories`
12. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/06a_talk_to_queen`
13. **Touch the Blackwall.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/06aa_touch_the_blackwall`
   - Map pin: ref `#q110_mp_blackwall_touch`; position `-1654.1547851563, -1857.6398925781, 56.744667053223`
14. **Investigate the source of the noises.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/05_alt/06c_investigate_sounds`
   - Map pin: ref `#q110_mp_sound_source_2`; position `-1691.4046630859, -1881.1954345703, 57.747867584229`
   - Map pin: ref `#q110_mp_sound_source_1`; position `-1679.1053466797, -1868.3841552734, 56.447868347168`
15. **Talk to Brigitte.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/01b_talk_to_brigitte`
16. **Defeat Placide.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/01c_deal_with_placide`
17. **Take the key from Placide's body.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/01d_loot_door_key`
18. **Leave the chapel.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/02b_leave_the_chapel`
   - Map pin: ref `#q110_mp_leave_chapel`; position `-1750.1345214844, -1928.33984375, 63.426765441895`
19. **Hide from the guards.**  
   `Optional` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/4_hide_from_guards`
20. **Escape the Voodoo Boys' hideout.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/03_escape`
21. **Talk to Johnny.**  
   `Primary` · `quests/main_quest/act_01/q110_03_cyberspace/06_wrap_up/03_talk_to_johnny`

## Unfinished Sympathy

- IGN walkthrough: [Unfinished Sympathy](https://www.ign.com/wikis/cyberpunk-2077/Unfinished_Sympathy_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `112432573`
- Quest path: `ep1/quests/main_quest/q306_somi_epilogue`
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`

### Journal premise

Think this is it? The end of the story? Can we finally stop looking over our shoulders? Are we... free? I'd like to think so, but somethin' tells me this is only the beginning. You uncovered mysteries you didn't know existed. You made decisions whose consequences you couldn't anticipate. Most importantly, though, you still don't know how to save yourself. Always one step forward, two steps back. Same old shit.

### Objective sequence

1. **Wait for the FIA to make a move.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/00_wait_for_call_alex`
2. **Answer the holocall.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/01_answer_phone`
3. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/02_talk_to_alex`
4. **Meet up with Alex.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/03_meet_alex`
   - Map pin: ref `#q306_mp_epilogue_meeting_nighthawks`; position `-2427.01953125, -2664.8488769531, 29.080003738403`
5. **Wait for Alex.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/03a_wait_opening`
   - Map pin: ref `#q306_mp_wait_outside`; position `-2419.0112304688, -2668.9331054688, 29.042045593262`
6. **Sit by the bar.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/04_sit_down`
   - Map pin: ref `#q306_mp_nighthawks_sitdown`; position `-2426.7395019531, -2665.3391113281, 28.790004730225`
7. **(unnamed objective)**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/05_talk_to_alex`
8. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q306_somi_epilogue/00_epilogue/06_talk_to_johnny`

## We Gotta Live Together

- IGN walkthrough: [We Gotta Live Together](https://www.ign.com/wikis/cyberpunk-2077/We_Gotta_Live_Together)
- Vanilla type: `MainQuest`
- Quest hash: `485705918`
- Quest path: `quests/main_quest/act_01/q114_01_nomad_initiation`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `interact/use device`, `combat/neutralize`, `vehicle sequence`, `choice/decision`

### Objective sequence

1. **Enter Panam's car.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/enter_car`
2. **Follow Mitch.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/follow_mitch`
3. **Go to Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/meet_panam`
4. **Talk to Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/plan`
5. **Go to the Aldecaldos camp.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/travel_nomad_camp`
   - Map pin: ref `#q114_mp_nomad_camp`; position `1840.8797607422, 2236.869140625, 181.1392364502`
6. **I was gonna say that this time you'd have to go it alone, but it looks like the Aldecaldos've got some fight in them after all. Wonder what you see in them: a partner? Friend? Family? Something tells me sooner or later you're gonna have to choose one of the above, especially if it's thanks to them you get into Mikoshi.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/new_camp_wake_up/wake_up_talk_panam`
7. **Step up to the line.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/line`
   - Map pin: ref `#q114_mp_shooting_line_001`; position `1845.8955078125, 2222.28125, 180.14080810547`
8. **Join up with Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/sit_down`
9. **Talk to the nomads.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/party`
10. **Shoot at least 12 bottles in 15 seconds.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/shoot_bottles`
   - Map pin: ref `#q114_mp_shooting_bottles`; position `1845.1844482422, 2215.2634277344, 180.95014953613`
11. **Join Panam when you're ready.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/find_panam`
12. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/party/talk_panam`
13. **Enter the Basilisk.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/board_panzer`
14. **Talk to Dakota.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/dakota_alt_prep`
15. **Talk to Dakota and Carol.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/dakota_carol_wrap`
16. **Destroy the car wrecks.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/destroywrecks`
17. **Drive to the location marked by Mitch.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/drive_to_spot`
   - Map pin: ref `#q114_mp_afterburner_spot`; position `2273.359375, 2063.2299804688, 179.20478820801`
18. **Get in the tub.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/enter_bathtub`
19. **Follow Saul and Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/follow_to_initiation`
20. **Talk to Mitch.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/mitch_panzer_prep`
21. **Talk to Mitch and the veterans.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/mitch_panzer_talk`
22. **Use the nitro.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/punch_through`
   - Map pin: ref `#q114_mp_afterburner_goal`; position `2330.9926757813, 2066.5249023438, 179.45712280273`
23. **Return to the camp.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/return_to_camp`
   - Map pin: ref `#q114_mp_garage`; position `1889.0179443359, 2232.4606933594, 179.2628326416`
24. **Talk to Saul and Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/return_to_saulpanam`
25. **Talk to Mitch.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/panzer`
26. **Talk to Saul.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/take_part_in_initiation`
   - Map pin: ref `#q114_mp_join_initiation`; position `1817.9370117188, 2250.1557617188, 181.05101013184`
27. **Talk to Alt.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/talk_alt`
28. **Talk to the nomads.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/talk_to_crowd`
29. **Talk to Mitch.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/talk_about_panzer`
30. **Talk to Panam.**  
   `Primary` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/talk_to_panam_initiation`
31. **Talk to the vendor.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/vendor`
32. **Drive to the marked location.**  
   `Optional` · `quests/main_quest/act_01/q114_01_nomad_initiation/preparations/warm_up`
   - Map pin: ref `#q114_mp_train_area`; position `2188.4055175781, 2030.6955566406, 178.56500244141`

## Who Wants to Live Forever

- IGN walkthrough: [Who Wants to Live Forever](https://www.ign.com/wikis/cyberpunk-2077/Who_Wants_to_Live_Forever_Walkthrough)
- Vanilla type: `MainQuest`
- Quest hash: `3455145467`
- Quest path: `ep1/quests/main_quest/q307_before_tomorrow`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `vehicle sequence`

### Objective sequence

1. **So, here it is, the finale, though grand sure ain't the word for it. Our story ends not with a bang but a scalpel. I die so you can live on.\nTo tell ya the truth, V, kinda always suspected it'd turn out like this. I mean, your body, your life is how I've seen it throughout. Now, I can't claim to know what'll happen with you now that I’m gone, but if you don't mind my droppin' one last nugget o' wisdom on you as I go, it’s this – no matter what happens, V, no matter how bad the bastards bitch at you, stay fuckin' true to your fuckin' self and no one else.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/00_wait_text`
2. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/00b_read_text`
3. **So, here it is, the finale, though grand sure ain't the word for it. Our story ends not with a bang but a scalpel. I die so you can live on.\nTo tell ya the truth, V, kinda always suspected it'd turn out like this. I mean, your body, your life is how I've seen it throughout. Now, I can't claim to know what'll happen with you now that I’m gone, but if you don't mind my droppin' one last nugget o' wisdom on you as I go, it’s this – no matter what happens, V, no matter how bad the bastards bitch at you, stay fuckin' true to your fuckin' self and no one else.**  
   `Optional` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02b_confirm_again`
4. **Get up and tend to other matters.**  
   `Optional` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02c_leave_rooftop`
5. **Call Reed.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/01_call_reed`
6. **Tell Reed you want to undergo surgery.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02_confirm_pickup`
7. **Talk to Johnny.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02c_talk_johnny`
8. **Go back to rooftop above Misty's Esoterica and meet Reed.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02d_return_rooftop`
9. **Sit in the chair.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02e_sit_down_agan`
10. **Text your friends about leaving Night City for a while.**  
   `Optional` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/03c_text_friends`
11. **Sit in the chair.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02g_sit_down_rooftop`
12. **Head to the rooftop above Misty's Esoterica.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/03_meet_rooftop`
13. **Wait for the FIA agents.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/03a_wait_fia`
14. **Tell Johnny you won't call Reed.**  
   `Optional` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/02f_q115_abort`
15. **Talk to the FIA agent.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/03b_talk_fia`
16. **Get in the AV.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/04_enter_av`
17. **Wait for the AV to arrive at the clinic.**  
   `Primary` · `ep1/quests/main_quest/q307_before_tomorrow/00_hook/05_go_clinic`

## You Know My Name

- IGN walkthrough: [You Know My Name](https://www.ign.com/wikis/cyberpunk-2077/You_Know_My_Name)
- Vanilla type: `MainQuest`
- Quest hash: `1967265692`
- Quest path: `ep1/quests/main_quest/q303_songbird`
- District: Dogtown
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Nothing’s impossible, huh? Not only you managed to get Mr. Hands to help you, but even got old Solomon Reed to confide in you. You’re on a hot streak, V – it seems that even breaking into the best-guarded fortress in Dogtown (maybe even all of Night City) is actually possible. And if you do manage to get Songbird out of there, you should consider buying a bunch of scratch tickets, ‘cause Lady Luck is clearly on your side.

### Objective sequence

1. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/01_recon`
2. **Talk to the soldier.**  
   `Optional` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/11b_talk_tech_guy`
3. **Join Reed at the bar once you’re ready.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/01a_join_reed_bar`
4. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/01a_talk_reed`
5. **Enjoy the party until Songbird makes contact.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/01b_find_netrunners`
6. **Read the message from Songbird.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/01c_read_message`
7. **Approach Songbird.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/02_go_to_somi`
8. **Talk to Songbird.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/03_talk_songbird`
9. **Take the shard from the glass.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/03a_get_shard`
   - Map pin: ref `#q303_mp_paradise_songbird_shard`; position `-1870.5308837891, -2256.150390625, 445.90475463867`
10. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/03b_talk_reed`
11. **Follow the netrunners.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/04_follow_netrunners`
   - Map pin: ref `#q303_mp_paradise_casino`; position `-1840.8625488281, -2291.0483398438, 439.76431274414`
12. **Scan Aurore.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/05_scan_netrunners`
13. **Scan Aymeric.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/05_scan_netrunners1`
14. **Join Reed at the bar.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/06a_join_bar`
   - Map pin: ref `#q303_mp_paradise_casino_bar_sit`; position `-1843.0115966797, -2294.111328125, 440.35580444336`
15. **Buy at least €$80,000 worth of casino chips for roulette.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/06c_get_chips`
16. **Play roulette with the netrunners.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/07_play_the_game`
   - Map pin: ref `#q303_mp_paradise_casino_table`; position `-1833.5158691406, -2300.1689453125, 441.81457519531`
17. **Wait until the round is over to join the game.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/07b_wait_round`
18. **Get through the confrontation with Hansen.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/08_survive_kurt`
19. **Leave the Black Sapphire through the lobby.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/09_exit_paradise`
   - Map pin: ref `#q303_mp_leaving_paradise_exit`; position `-1815.2092285156, -2315.4338378906, 40.059722900391`
   - Map pin: ref `#q303_mp_leaving_paradise_top_lift`; position `-1934.3527832031, -2316.8466796875, 441.75289916992`
20. **Cash out your winnings.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/09b_cash_out`
21. **Talk to Alex.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/09b_contact_alex`
22. **Talk to the guards.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/10_talk_guards`
23. **Follow the guard to the exit.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/11_walk_out`
   - Map pin: ref `#q303_mp_leaving_paradise_exit`; position `-1815.2092285156, -2315.4338378906, 40.059722900391`
24. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/11a_follow_reed`
25. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/11c_talk_reed_ending`
26. **Exit the Black Sapphire.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/12_lobby_combat`
   - Map pin: ref `#q303_mp_leaving_paradise_exit`; position `-1815.2092285156, -2315.4338378906, 40.059722900391`
   - Map pin: ref `#q303_mp_leaving_paradise_exit_scanner_gates`; position `-1856.5396728516, -2315.7805175781, 41.181823730469`
27. **Leave the Black Sapphire area.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/12a_leave_area`
28. **Lose your tail.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06_paradise_restaurant/12a_loose_chase`
29. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/02_talk_reed`
30. **Use the panel to open the path.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/05a_open_path`
31. **Talk to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/05b_talk_reed_comms`
32. **Defeat the warehouse guards.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06a_clear_warehouse`
33. **Connect to the CCTV through the security computer.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06b_find_reed_on_camera`
34. **Switch between cameras to track Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06b_switch_cameras`
35. **Track down Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06c_find_reed`
36. **Open the entry gate.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06d_scan_open_gate`
37. **Go to the meeting point.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09a_walk_nest`
   - Map pin: ref `#q303_mp_tech_sniper_position`; position `-1864.94921875, -2316.0793457031, 345.42535400391`
38. **Neutralize the sniper.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09b_clear_balcony`
39. **Open the door for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09c_open_path`
40. **Scan the area for more mines.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10a_mines`
41. **Scan the floor for potential threats.**  
   `Optional` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09f_search_obstacles`
42. **Enter the flooded tunnels.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/03_enter_tunnels`
   - Map pin: ref `#q303_mp_safehouse_nighthawks_exit_lift`; position `-2436.14453125, -2647.9604492188, 11.800003051758`
   - Map pin: ref `#q303_mp_tower_technical_tunnels_entrance`; position `-1762.7947998047, -2299.4592285156, 31.264320373535`
   - Map pin: ref `#q303_mp_tower_technical_tunnels_interior`; position `-1790.2520751953, -2304.7092285156, 30.028898239136`
43. **Put the diving suit on before diving.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/04_pickup_suit`
44. **Proceed down the tunnels.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/05_follow_tunnels`
   - Map pin: ref `#q303_mp_tower_technical_warehouse`; position `-1857.5004882813, -2352.5310058594, 46.035186767578`
   - Map pin: ref `#q303_mp_tunnel_back_water`; position `-1833.5679931641, -2346.1682128906, 26.267833709717`
45. **Find a way to progress.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/05g_find_way`
46. **Open the door for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/06_unlock_door`
47. **Take the elevator to the maintenance area.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/07_enter_lift`
   - Map pin: ref `#q303_mrk_ct_tech_floor_floor_01`; position `-1850.1462402344, -2343.0659179688, 40.494316101074`
48. **Ride the elevator.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/08_ride_lift`
49. **Follow Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09_follow_reed`
50. **Jack in.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09d_connect_sniper_nest`
51. **Let Reed know you’re ready.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09e_let_know`
52. **Use Kiroshi to find the meeting point.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/09g_find_rendezvous_point`
   - Map pin: ref `#q303_mp_tech_bridge`; position `-1865.8468017578, -2339.9926757813, 346.97045898438`
53. **Identify immediate threats to Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10_secure_reed`
54. **Wait until the patrol walks past Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10b_wait_patrol`
55. **Find the progress route for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10b_way_pass`
56. **Take out the guard.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10c_takedown_guard`
57. **Wait for Reed to pass through.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10d_wait_pass`
58. **Handle the guard above Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10e_deal_above`
59. **Use the CCTV system to locate the guard blocking Reed’s progress.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10f_locate_npc`
60. **Handle the guard blocking Reed’s progress.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10g_deal_block`
61. **Handle the sniper on the balcony.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10h_deal_sniper`
62. **Find a way to open the passage for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10i_open_passage`
63. **Destroy the power source for gate security systems.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10j_destroy_gate_battery`
64. **Deal with the incoming guards.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/10k_clear_passage`
65. **Defeat the guards.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/11_combat_floor`
66. **Cover Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/11_combat_tower_a`
67. **Take out the hostile snipers.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/11a_combat_snipers`
68. **Take out the hostile drones.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/11b_combat_drones`
69. **Join Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/11b_join_reed`
70. **Take the elevator to the top floor.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/12_enter_lift`
   - Map pin: ref `#q303_mp_tower_technical_final_lift`; position `-1879.9849853516, -2356.5759277344, 340.26431274414`
71. **Go to the party.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/13_enter_paradise`
   - Map pin: ref `#q303_mp_tower_floor_guide_to_rest_002`; position `-1887.3146972656, -2281.6608886719, 444.76403808594`
72. **Put on your eveningwear.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/13_suit_up`
73. **Grab your outfit.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/13a_pickup_suit`
   - Map pin: ref `#q303_06b_sm_paradise_technical_floor_bag_spawn_marker`; position `-1897.2404785156, -2358.0400390625, 447.31887817383`
74. **Wait for Reed.**  
   `Primary` · `ep1/quests/main_quest/q303_songbird/06b_paradise_technical/14a_wait_reed`
