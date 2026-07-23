# Cyberpunk 2077 Side Jobs

Source index: [IGN — Side Jobs](https://www.ign.com/wikis/cyberpunk-2077/Side_Jobs)

This is a structural reference derived from IGN's walkthrough index and
the local [`quest.json`](../../../quest.json) journal export. It summarizes
vanilla quest objectives and links to IGN; it does not reproduce IGN's
walkthrough prose.

Matched quests: **85**

## Quick index

| Quest | Vanilla type | Quest path | Building blocks |
|---|---|---|---|
| [A Cool Metal Fire](#a-cool-metal-fire) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/A_Cool_Metal_Fire)) | SideQuest | `quests/side_quest/sq031_smack_my_bitch_up` | meet/contact conversation, travel/reach location, wait/time gate, retrieve/collect item, deliver/deposit item, choice/decision, leave/escape area |
| [A Day In The Life](#a-day-in-the-life) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/A_Day_In_The_Life)) | MinorQuest | `quests/minor_quest/mq013_punks` | meet/contact conversation, combat/neutralize, choice/decision |
| [A Like Supreme](#a-like-supreme) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/A_Like_Supreme)) | SideQuest | `quests/side_quest/sq011_concert` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, retrieve/collect item, leave/escape area |
| [Beat on the Brat](#beat-on-the-brat) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat)) | MinorQuest | `quests/minor_quest/mq025_psycho_brawl` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, retrieve/collect item, combat/neutralize |
| [Beat on the Brat: Arroyo](#beat-on-the-brat-arroyo) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_Arroyo)) | MinorQuest | `quests/minor_quest/mq025_03_arroyo` | combat/neutralize |
| [Beat on the Brat: Kabuki](#beat-on-the-brat-kabuki) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat:_Kabuki)) | MinorQuest | `quests/minor_quest/mq025_02_kabuki` | combat/neutralize |
| [Beat on the Brat: Pacifica](#beat-on-the-brat-pacifica) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat:_Pacifica)) | MinorQuest | `quests/minor_quest/mq025_06_pacifica` | meet/contact conversation, combat/neutralize |
| [Beat on the Brat: Rancho Coronado](#beat-on-the-brat-rancho-coronado) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_Rancho_Coronado)) | MinorQuest | `quests/minor_quest/mq025_07_fight_club` | combat/neutralize |
| [Beat on the Brat: The Glen](#beat-on-the-brat-the-glen) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_The_Glen)) | MinorQuest | `quests/minor_quest/mq025_05_glen` | retrieve/collect item, combat/neutralize |
| [Big in Japan](#big-in-japan) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Big_in_Japan)) | MinorQuest | `quests/minor_quest/mq038_neweridentity` | meet/contact conversation, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Blistering Love](#blistering-love) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Blistering_Love)) | SideQuest | `quests/side_quest/sq031_cinema` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, interact/use device, retrieve/collect item, vehicle sequence, leave/escape area |
| [Boat Drinks](#boat-drinks) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Boat_Drinks)) | SideQuest | `quests/side_quest/sq028_kerry_romance` | meet/contact conversation, wait/time gate, choice/decision, leave/escape area |
| [Both Sides, Now](#both-sides-now) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Both_Sides,_Now)) | SideQuest | `quests/side_quest/sq026_01_suicide` | meet/contact conversation, wait/time gate, deliver/deposit item, leave/escape area |
| [Burning Desire](#burning-desire) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Burning_Desire)) | MinorQuest | `quests/minor_quest/mq012_stud` | phone/message contact, meet/contact conversation, retrieve/collect item, combat/neutralize, vehicle sequence, choice/decision |
| [Chippin' In](#chippin-in) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Chippin%27_In)) | SideQuest | `quests/side_quest/sq031_rogue` | phone/message contact, meet/contact conversation, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, vehicle sequence, leave/escape area |
| [Coin Operated Boy](#coin-operated-boy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Coin_Operated_Boy)) | MinorQuest | `quests/minor_quest/mq037_brendan` | meet/contact conversation, search/investigate |
| [Don't Lose Your Mind](#dont-lose-your-mind) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Don%27t_Lose_Your_Mind)) | SideQuest | `quests/side_quest/sq025b_delamain_insurgence` | phone/message contact, meet/contact conversation, travel/reach location, search/investigate, interact/use device, hack/breach/download, deliver/deposit item, vehicle sequence, choice/decision, leave/escape area |
| [Dream On](#dream-on) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Dream_On)) | SideQuest | `quests/side_quest/sq006_dream_on` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, leave/escape area |
| [Epistrophy](#epistrophy) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy)) | SideQuest | `quests/side_quest/sq025_delamain` | meet/contact conversation, follow/escort, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Epistrophy: Badlands](#epistrophy-badlands) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Badlands)) | SideQuest | `quests/side_quest/sq025c06_mean` | meet/contact conversation, wait/time gate, search/investigate, vehicle sequence, leave/escape area |
| [Epistrophy: Coastview](#epistrophy-coastview) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Coastview)) | SideQuest | `quests/side_quest/sq025c03_mean` | meet/contact conversation, wait/time gate, combat/neutralize |
| [Epistrophy: North Oak](#epistrophy-north-oak) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_North_Oak)) | SideQuest | `quests/side_quest/sq025c02_sad` | meet/contact conversation, wait/time gate, vehicle sequence, leave/escape area |
| [Epistrophy: Northside](#epistrophy-northside) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Northside)) | SideQuest | `quests/side_quest/sq025c05_scared` | meet/contact conversation, follow/escort, wait/time gate, search/investigate |
| [Epistrophy: Rancho Coronado](#epistrophy-rancho-coronado) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Rancho_Coronado)) | SideQuest | `quests/side_quest/sq025c04_manic` | meet/contact conversation, wait/time gate, search/investigate |
| [Epistrophy: The Glen](#epistrophy-the-glen) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_The_Glen)) | SideQuest | `quests/side_quest/sq025c07_suicidal` | meet/contact conversation, wait/time gate, search/investigate, deliver/deposit item, vehicle sequence |
| [Ex-Factor](#ex-factor) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Ex-Factor)) | SideQuest | `quests/side_quest/sq026_02_maiko` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, interact/use device, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Ezekiel Saw the Wheel](#ezekiel-saw-the-wheel) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Ezekiel_Saw_The_Wheel)) | MinorQuest | `quests/minor_quest/mq022_ezekiel` | meet/contact conversation |
| [Following the River](#following-the-river) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Following_The_River)) | SideQuest | `quests/side_quest/sq029_sobchak_romance` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize |
| [Fool on the Hill](#fool-on-the-hill) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Fool_on_the_Hill)) | MinorQuest | `quests/minor_quest/mq033_tarot` | meet/contact conversation, search/investigate |
| [Fortunate Son](#fortunate-son) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Fortunate_Son)) | MinorQuest | `quests/minor_quest/mq021_guide` | meet/contact conversation, retrieve/collect item, combat/neutralize |
| [Full Disclosure](#full-disclosure) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Full_Disclosure)) | MinorQuest | `quests/minor_quest/mq024_sandra` | meet/contact conversation, search/investigate, retrieve/collect item, combat/neutralize |
| [Gun Music](#gun-music) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Gun_Music)) | MinorQuest | `quests/minor_quest/mq002_veterans` | meet/contact conversation, interact/use device, combat/neutralize |
| [Happy Together](#happy-together) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Happy_Together)) | MinorQuest | `quests/minor_quest/mq010_barry` | meet/contact conversation, search/investigate |
| [Heroes](#heroes) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Heroes)) | SideQuest | `quests/side_quest/sq018_jackie` | phone/message contact, meet/contact conversation, travel/reach location, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, choice/decision, leave/escape area |
| [Holdin' On](#holdin-on) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Holdin_On)) | SideQuest | `quests/side_quest/sq011_kerry` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, retrieve/collect item |
| [Human Nature](#human-nature) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Human_Nature)) | SideQuest | `quests/side_quest/sq025_0_pickup` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, vehicle sequence, leave/escape area |
| [I Can See Clearly Now](#i-can-see-clearly-now) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I_Can_See_Clearly_Now)) | MinorQuest | `quests/minor_quest/mq037_brendan_dumpster` | meet/contact conversation, interact/use device |
| [I Don't Wanna Hear It](#i-dont-wanna-hear-it) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I_Don%27t_Wanna_Hear_It)) | SideQuest | `quests/side_quest/sq017_01_riot_club` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, deliver/deposit item, leave/escape area |
| [I Fought the Law](#i-fought-the-law) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I_Fought_the_Law)) | SideQuest | `quests/side_quest/sq012_lost_girl` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, combat/neutralize, stealth/avoid detection, vehicle sequence, leave/escape area |
| [I Really Want to Stay at Your House](#i-really-want-to-stay-at-your-house) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/I_Really_Want_to_Stay_at_Your_House)) | MinorQuest | `quests/minor_quest/mq055_romance_apartment` | phone/message contact, meet/contact conversation, wait/time gate, deliver/deposit item, leave/escape area |
| [I'm in Love with My Car](#im-in-love-with-my-car) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Ken_Block_Car_Location)) | MinorQuest | `quests/minor_quest/mq050_ken_block_tribute` | search/investigate, vehicle sequence |
| [Imagine](#imagine) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Imagine)) | MinorQuest | `quests/minor_quest/mq014_zen` | meet/contact conversation |
| [Killing In The Name](#killing-in-the-name) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Killing_in_the_Name)) | MinorQuest | `quests/minor_quest/mq018_writer` | phone/message contact, meet/contact conversation, travel/reach location, search/investigate, interact/use device, hack/breach/download, deliver/deposit item, choice/decision, leave/escape area |
| [Machine Gun](#machine-gun) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Machine_Gun)) | MinorQuest | `quests/minor_quest/mq007_smartgun` | meet/contact conversation, search/investigate |
| [Off the Leash](#off-the-leash) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Off_The_Leash)) | SideQuest | `quests/side_quest/sq017_02_lounge` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate |
| [Only Pain](#only-pain) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Only_Pain)) | MinorQuest | `quests/minor_quest/mq005_alley` | meet/contact conversation |
| [Paid in Full](#paid-in-full) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Paid_in_Full)) | MinorQuest | `quests/minor_quest/mq045_victor_debt` | objective sequence |
| [Pisces](#pisces) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Pisces)) | SideQuest | `quests/side_quest/sq026_04_hiromi` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Poem Of The Atoms](#poem-of-the-atoms) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Poem_of_the_Atoms)) | MinorQuest | `quests/minor_quest/mq014_03_third` | meet/contact conversation, interact/use device |
| [Psycho Killer](#psycho-killer) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Psycho_Killer)) | MinorQuest | `quests/minor_quest/mq043_cyberpsychos` | meet/contact conversation, wait/time gate, retrieve/collect item, combat/neutralize |
| [Pyramid Song](#pyramid-song) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Pyramid_Song)) | SideQuest | `quests/side_quest/sq030_judy_romance` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item |
| [Queen of the Highway](#queen-of-the-highway) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Queen_of_the_Highway)) | SideQuest | `quests/side_quest/sq027_02_raffen_shiv_attack` | phone/message contact, meet/contact conversation, follow/escort, wait/time gate, vehicle sequence |
| [Raymond Chandler Evening](#raymond-chandler-evening) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Raymond_Chandler_Evening)) | MinorQuest | `quests/minor_quest/mq040_biosculpt` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, search/investigate, deliver/deposit item, combat/neutralize, choice/decision, leave/escape area |
| [Rebel! Rebel!](#rebel-rebel) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Rebel_Rebel)) | SideQuest | `quests/side_quest/sq017_kerry` | meet/contact conversation, travel/reach location, follow/escort, wait/time gate, retrieve/collect item, vehicle sequence, leave/escape area |
| [Riders on the Storm](#riders-on-the-storm) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Riders_on_the_Storm)) | SideQuest | `quests/side_quest/sq004_riders_on_the_storm` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, vehicle sequence, leave/escape area |
| [Sacrum Profanum](#sacrum-profanum) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sacrum_Profanum)) | MinorQuest | `quests/minor_quest/mq032_sacrum` | meet/contact conversation, retrieve/collect item, combat/neutralize |
| [Second Conflict](#second-conflict) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Second_Conflict)) | SideQuest | `quests/side_quest/sq011_johnny` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, search/investigate, interact/use device, deliver/deposit item, combat/neutralize, vehicle sequence, leave/escape area |
| [Send in the Clowns](#send-in-the-clowns) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Send_in_the_Clowns)) | MinorQuest | `quests/minor_quest/mq035_ozob` | phone/message contact, meet/contact conversation, wait/time gate, search/investigate, combat/neutralize, vehicle sequence |
| [Sex On Wheels](#sex-on-wheels) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sex_On_Wheels)) | MinorQuest | `quests/minor_quest/mq044_jakes_vehicle` | deliver/deposit item, vehicle sequence, leave/escape area |
| [Shape of a Pony](#shape-of-a-pony) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Shape_of_a_Pony)) | MinorQuest | `quests/minor_quest/mws_se5_07` | phone/message contact, search/investigate, combat/neutralize, vehicle sequence |
| [Shoot To Thrill](#shoot-to-thrill) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Shoot_to_Thrill)) | MinorQuest | `quests/minor_quest/mq011_wilson` | meet/contact conversation, travel/reach location, wait/time gate, interact/use device, retrieve/collect item, vehicle sequence |
| [Sinnerman](#sinnerman) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sinnerman)) | SideQuest | `quests/side_quest/sq023_hit_order` | phone/message contact, meet/contact conversation, follow/escort, wait/time gate, retrieve/collect item, combat/neutralize, vehicle sequence |
| [Small Man, Big Mouth](#small-man-big-mouth) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Small_Man,_Big_Mouth)) | MinorQuest | `quests/minor_quest/mq017_streetkid` | meet/contact conversation, travel/reach location, wait/time gate, search/investigate, retrieve/collect item, combat/neutralize |
| [Space Oddity](#space-oddity) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Space_Oddity)) | MinorQuest | `quests/minor_quest/mq003_orbitals` | meet/contact conversation, travel/reach location, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, choice/decision |
| [Spray Paint](#spray-paint) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Spray_Paint)) | MinorQuest | `quests/minor_quest/mq037_brendan_hooligan001` | meet/contact conversation |
| [Stadium Love](#stadium-love) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Stadium_Love)) | MinorQuest | `quests/minor_quest/mq008_party` | meet/contact conversation, travel/reach location, retrieve/collect item |
| [Stairway To Heaven](#stairway-to-heaven) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Stairway_to_Heaven)) | MinorQuest | `quests/minor_quest/mq014_02_second` | meet/contact conversation |
| [Sweet Dreams](#sweet-dreams) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Sweet_Dreams)) | MinorQuest | `quests/minor_quest/mq036_overload` | meet/contact conversation, follow/escort, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, leave/escape area |
| [Talkin' 'bout a Revolution](#talkin-bout-a-revolution) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Talking_Bout_A_Revolution)) | SideQuest | `quests/side_quest/sq026_03_pizza` | meet/contact conversation, travel/reach location, wait/time gate, interact/use device, deliver/deposit item, leave/escape area |
| [The Ballad of Buck Ravers](#the-ballad-of-buck-ravers) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Ballad_of_Buck_Ravers)) | MinorQuest | `quests/minor_quest/mq023_bootleg` | meet/contact conversation, travel/reach location, search/investigate |
| [The Beast In Me](#the-beast-in-me) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Beast_In_Me)) | SideQuest | `quests/meta/07_nc_underground` | phone/message contact, meet/contact conversation, wait/time gate, retrieve/collect item, vehicle sequence |
| [The Gift](#the-gift) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Gift)) | SideQuest | `quests/side_quest/sq_q001_tbug` | search/investigate, interact/use device, hack/breach/download, retrieve/collect item |
| [The Gig](#the-gig) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Gig_(Side_Gig))) | SideQuest | `quests/side_quest/sq_q001_wakako` | retrieve/collect item |
| [The Gun](#the-gun) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Gun)) | SideQuest | `quests/side_quest/sq_q001_wilson` | meet/contact conversation, travel/reach location, retrieve/collect item |
| [The Highwayman](#the-highwayman) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Highwayman)) | MinorQuest | `quests/minor_quest/mq029_tourist` | search/investigate, interact/use device, retrieve/collect item |
| [The Hunt](#the-hunt) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Hunt)) | SideQuest | `quests/side_quest/sq021_sick_dreams` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, combat/neutralize, vehicle sequence, choice/decision, leave/escape area |
| [The Prophet's Song](#the-prophets-song) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/The_Prophet%27s_Song)) | MinorQuest | `quests/minor_quest/mq026_conspiracy` | meet/contact conversation, wait/time gate, search/investigate, combat/neutralize |
| [There Is A Light That Never Goes Out](#there-is-a-light-that-never-goes-out) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/There_Is_A_Light_That_Never_Goes_Out)) | SideQuest | `quests/side_quest/sq023_bd_passion` | meet/contact conversation, follow/escort, wait/time gate, vehicle sequence |
| [These Boots Are Made for Walkin'](#these-boots-are-made-for-walkin) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/These_Boots_Are_Made_For_Walkin%27)) | MinorQuest | `quests/minor_quest/mq042_nomad` | meet/contact conversation, travel/reach location, search/investigate, interact/use device, retrieve/collect item, vehicle sequence |
| [They Won't Go When I Go](#they-wont-go-when-i-go) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/They_Won%27t_Go_When_I_Go)) | SideQuest | `quests/side_quest/sq023_real_passion` | meet/contact conversation, wait/time gate, search/investigate, interact/use device, retrieve/collect item, deliver/deposit item, leave/escape area |
| [Tune Up](#tune-up) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Tune_Up)) | SideQuest | `quests/side_quest/sq025_compensation` | phone/message contact, meet/contact conversation |
| [Venus in Furs](#venus-in-furs) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Venus_in_Furs)) | MinorQuest | `quests/main_quest/prologue/q003_stout` | meet/contact conversation |
| [Violence](#violence) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/Violence)) | MinorQuest | `quests/minor_quest/mq019_paparazzi` | phone/message contact, meet/contact conversation, travel/reach location, wait/time gate, search/investigate, hack/breach/download, deliver/deposit item, leave/escape area |
| [War Pigs](#war-pigs) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/War_Pigs)) | MinorQuest | `quests/minor_quest/mq041_corpo` | meet/contact conversation, interact/use device |
| [With a Little Help from My Friends](#with-a-little-help-from-my-friends) ([IGN](https://www.ign.com/wikis/cyberpunk-2077/With_a_Little_Help_From_My_Friends)) | SideQuest | `quests/side_quest/sq027_01_basilisk_convoy` | phone/message contact, meet/contact conversation, travel/reach location, follow/escort, wait/time gate, search/investigate, interact/use device, retrieve/collect item, combat/neutralize, vehicle sequence, leave/escape area |

## A Cool Metal Fire

- IGN walkthrough: [A Cool Metal Fire](https://www.ign.com/wikis/cyberpunk-2077/A_Cool_Metal_Fire)
- Vanilla type: `SideQuest`
- Quest hash: `653340120`
- Quest path: `quests/side_quest/sq031_smack_my_bitch_up`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `retrieve/collect item`, `deliver/deposit item`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Now, I don't ask you for much, but I gotta zero Smasher myself. That motherfucker thinks he's invincible. Worse, so does Rogue. All these years, Arasaka Tower's been haunting her. Enough's enough. I'm taking control this one time, I'm finding him, I'm wiping Adam Smasher off the face of the earth.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/01_afterlife/01_bug_drags`
   - Map pin: ref `#sq031_mp_smack_afterlife_chair`; position `-1447.8774414063, 1012.0923461914, 17.300113677979`
2. **Talk to Cassius.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/02_smack_tattoo/01_get_tattoo`
3. **Watch Ruby dance.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease`
4. **Talk to Ruby.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease2`
5. **Talk to Ruby.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease3`
6. **Talk to Ruby.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease4`
7. **Buy champagne at the bar.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/02_buy_champagne`
8. **Drink with Ruby.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne`
9. **Drink with the others in the club.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne1`
10. **Choose a pill.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne2`
11. **Take a pill to keep control over V's body.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne3`
12. **Go to the bathroom.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/04_find_toilet`
   - Map pin: ref `#sq031_mp_toilet`; position `-1612.5213623047, 372.91564941406, 9.1202373504639`
13. **Talk to the bouncers.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons`
14. **Take Ruby back to your place.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/08_drive_streapper`
15. **Wait for Ruby to leave the club.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/09_wait_for_streapper`
16. **Have fun.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/13_enjoy_evening`
17. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/01_talk_to_stranger1`
18. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/03_talk_to_johnny`

## A Day In The Life

- IGN walkthrough: [A Day In The Life](https://www.ign.com/wikis/cyberpunk-2077/A_Day_In_The_Life)
- Vanilla type: `MinorQuest`
- Quest hash: `3309160730`
- Quest path: `quests/minor_quest/mq013_punks`
- District: Santo Domingo / Arroyo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `combat/neutralize`, `choice/decision`

### Objective sequence

1. **Gonna sound like my gramps for a sec, but you know, in my time, being a punk meant something different. People fought against the system whatever way they could, frying the biggest fish they could catch, tearing down palaces brick by brick. Now every random gonk-brain fool thinks they're a hero for flatlining an unarmed normie. This isn't your beef, I get it... But are you sure don't wanna teach those worms a lesson?**  
   `Primary` · `quests/minor_quest/mq013_punks/00_punks/00_talk_shopkeep`
2. **Decide if you'll help the vendor.**  
   `Primary` · `quests/minor_quest/mq013_punks/00_punks/01_decide`
3. **Talk to the thugs.**  
   `Primary` · `quests/minor_quest/mq013_punks/00_punks/02_deal_with_punks`
4. **Defeat the thugs.**  
   `Primary` · `quests/minor_quest/mq013_punks/00_punks/03_defeat_punks`
5. **Talk to the vendor.**  
   `Primary` · `quests/minor_quest/mq013_punks/00_punks/04_talk_shopkeep`

## A Like Supreme

- IGN walkthrough: [A Like Supreme](https://www.ign.com/wikis/cyberpunk-2077/A_Like_Supreme)
- Vanilla type: `SideQuest`
- Quest hash: `517687328`
- Quest path: `quests/side_quest/sq011_concert`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `retrieve/collect item`, `leave/escape area`

### Journal premise

Fuck, this might be the first time I just wanna play a decent gig, not use it as an excuse to go rioting in the streets afterward. No more "Death to Arasaka!" no more anarchist bullshit. Everything just like Kerry always wanted. You might even have a good time, too.

### Objective sequence

1. **Talk to Nancy.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/00_talk_to_nancy`
2. **Leave Denny's villa and wait a day for Nancy's call.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/00_wait_for_call`
3. **Call Nancy.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/00c_call_nancy`
4. **Go to Red Dirt in the evening.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/01_red_dirt`
   - Map pin: ref `#sq011_mp_red_dirt`; position `-725.06317138672, -991.85125732422, 9.2962636947632`
5. **Go to the bathroom and take the pills.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/01_red_dirt1`
   - Map pin: ref `#sq011_mp_red_dirt_toilet`; position `-729.74969482422, -990.25933837891, 9.254581451416`
6. **Go back to the main room in Red Dirt.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/01_red_dirt2`
   - Map pin: ref `#sq011_mp_red_dirt`; position `-725.06317138672, -991.85125732422, 9.2962636947632`
7. **Wait until evening.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/01a_red_dirt_wait`
   - Map pin: ref `#sq011_mp_red_dirt_wait`; position `-720.24786376953, -988.46240234375, 7.8455085754395`
8. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/02_talk_to_kerry`
9. **Talk to Nancy.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/02_talk_to_nancy`
10. **Call Kerry.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/03_call_kerry`
11. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/03_talk_to_johnny`
12. **Take the pills to give Johnny control.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/03_talk_to_johnny1`
13. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/04_talk_to_kerry`
14. **Perform with Kerry.**  
   `Primary` · `quests/side_quest/sq011_concert/05_concert/06_play_concert`

## Beat on the Brat

- IGN walkthrough: [Beat on the Brat](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat)
- Vanilla type: `MinorQuest`
- Quest hash: `688092372`
- Quest path: `quests/minor_quest/mq025_psycho_brawl`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

You're gettin' noticed, V. People can sense that hunger in you – one that can't be satiated. You want everything right now, and if you don't do it... you fight for it. You're a warrior, V. And the warrior's place is in the ring. Show 'em what you're made of. Knock the bolts off this training bot. And then, well... we'll see.

### Objective sequence

1. **Find the ring in Arroyo.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/find_fights/fin_arroyo`
   - Map pin: ref `#mq025_mp_03_arroyo`; position `-979.17657470703, -1589.4934082031, 10.929514884949`
2. **Find the club where the fights take place.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/find_fights/find_club`
   - Map pin: ref `#mq025_mp_07_fight_club`; position `-494.63442993164, -1931.0693359375, 8.5298929214478`
3. **Find the ring in the Glen.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/find_fights/find_glen`
   - Map pin: ref `#mq025_mp_05_glen`; position `-1788.9991455078, -1268.1921386719, 22.450578689575`
4. **Find the ring in Kabuki.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/find_fights/find_kabuki`
   - Map pin: ref `#mq025_mp_02_kabuki_01`; position `-1051.7836914063, 1848.341796875, 38.88525390625`
   - Map pin: ref `#mq025_mp_02_kabuki_02`; position `-1035.9919433594, 1837.0895996094, 42.81421661377`
   - Map pin: ref `#mq025_mp_02_kabuki_03`; position `-1029.7739257813, 1810.626953125, 46.174198150635`
5. **Find the ring in Pacifica.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/find_fights/find_pacifica`
   - Map pin: ref `#mq025_mp_06_pacifica`; position `-2119.3581542969, -1999.7661132813, 16.282173156738`
6. **Enter the ring.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/enter_ring`
   - Map pin: ref `#q001_mp_fistfight_ring_area`; position `-1430.8653564453, 1331.28515625, 119.30596160889`
7. **Defeat the training robot.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/fight`
8. **Get ready to fight.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/ready`
9. **Repeat the training.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/repeat_until_win`
10. **Talk to Razor Hughes.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/talk_razor`
11. **Talk to the coach.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/fistfight/talk_trainer`
12. **Take part in more fights after the Watson lockdown is lifted.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/barricade`
13. **Defeat Razor Hughes.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/fight_mrellis`
14. **Get ready to fight.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/prepare`
15. **Let the coach know when you're ready.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/ready`
16. **Go to the final fight.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/return`
   - Map pin: ref `#mq025_mp_08_finale_01`; position `-2274.900390625, -2103.4213867188, 14.727172851563`
   - Map pin: ref `#mq025_mp_08_finale_02`; position `-2359.9228515625, -2026.0932617188, 15.307174682617`
17. **Sit in your corner.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/ring`
   - Map pin: ref `#mq025_mp_08_ring`; position `-2363.0007324219, -2026.3239746094, 15.811195373535`
18. **Talk to the coach.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/talk`
19. **Follow the coach.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/talk1`
20. **Talk to Viktor.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/victor`
21. **Wait for Fred to send the list of opponents.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/wait`
22. **Take care of other things until Fred calls you back.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/wait_02`
23. **Wait for the final fight.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/wait_03`
   - Map pin: ref `#mq025_mp_fight_night_wait`; position `-2285.0168457031, -2115.2121582031, 13.927169799805`
24. **Defeat all opponents to get to the final round.**  
   `Primary` · `quests/minor_quest/mq025_psycho_brawl/psycho_brawl/win_fights`

## Beat on the Brat: Arroyo

- IGN walkthrough: [Beat On The Brat: Arroyo](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_Arroyo)
- Vanilla type: `MinorQuest`
- Quest hash: `2421816651`
- Quest path: `quests/minor_quest/mq025_03_arroyo`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `combat/neutralize`

### Objective sequence

1. **Heard somewhere the champ of Arroyo is a grade-A prick. Good news – should make beatin' his ass all the more fun.**  
   `Primary` · `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight`
   - Map pin: ref `#mq025_mp_03_arroyo`; position `-979.17657470703, -1589.4934082031, 10.929514884949`
2. **Defeat Buck.**  
   `Primary` · `quests/minor_quest/mq025_03_arroyo/arroyo/03_fight`
3. **Heard somewhere the champ of Arroyo is a grade-A prick. Good news – should make beatin' his ass all the more fun.**  
   `Primary` · `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk`

## Beat on the Brat: Kabuki

- IGN walkthrough: [Beat on the Brat: Kabuki](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat:_Kabuki)
- Vanilla type: `MinorQuest`
- Quest hash: `3900882952`
- Quest path: `quests/minor_quest/mq025_02_kabuki`
- District: Watson
- Level: 60
- Candidate building blocks: `combat/neutralize`

### Objective sequence

1. **Don't overthink this one. You have to defeat the champion of Kabuki. You know the stakes, you know the place. Now get your ass over there and win.**  
   `Primary` · `quests/minor_quest/mq025_02_kabuki/kabuki/02_kabuki_fight`
   - Map pin: ref `#mq025_mp_02_kabuki_01`; position `-1051.7836914063, 1848.341796875, 38.88525390625`
   - Map pin: ref `#mq025_mp_02_kabuki_02`; position `-1035.9919433594, 1837.0895996094, 42.81421661377`
   - Map pin: ref `#mq025_mp_02_kabuki_03`; position `-1029.7739257813, 1810.626953125, 46.174198150635`
2. **Don't overthink this one. You have to defeat the champion of Kabuki. You know the stakes, you know the place. Now get your ass over there and win.**  
   `Primary` · `quests/minor_quest/mq025_02_kabuki/kabuki/02_talk`
3. **Defeat the twins.**  
   `Primary` · `quests/minor_quest/mq025_02_kabuki/kabuki/04_fight`

## Beat on the Brat: Pacifica

- IGN walkthrough: [Beat on the Brat: Pacifica](https://www.ign.com/wikis/cyberpunk-2077/Beat_on_the_Brat:_Pacifica)
- Vanilla type: `MinorQuest`
- Quest hash: `4204938432`
- Quest path: `quests/minor_quest/mq025_06_pacifica`
- District: Pacifica
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `combat/neutralize`

### Objective sequence

1. **Defeat Ozob.**  
   `Primary` · `quests/minor_quest/mq025_06_pacifica/pacifica/06_fight_ozob`
2. **A throwdown in Pacifica, huh? Wonder who you're up against. I'd say a Haitian, though I guess that much is probably obvious. Careful, those Pacificans don't fight for first blood – they fight for last blood.**  
   `Primary` · `quests/minor_quest/mq025_06_pacifica/pacifica/06_pacifica_fight`
   - Map pin: ref `#mq025_mp_06_pacifica`; position `-2119.3581542969, -1999.7661132813, 16.282173156738`
3. **Talk to the referee.**  
   `Primary` · `quests/minor_quest/mq025_06_pacifica/pacifica/06_talk_announcer`
4. **A throwdown in Pacifica, huh? Wonder who you're up against. I'd say a Haitian, though I guess that much is probably obvious. Careful, those Pacificans don't fight for first blood – they fight for last blood.**  
   `Primary` · `quests/minor_quest/mq025_06_pacifica/pacifica/06_talk_ozob`

## Beat on the Brat: Rancho Coronado

- IGN walkthrough: [Beat On The Brat: Rancho Coronado](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_Rancho_Coronado)
- Vanilla type: `MinorQuest`
- Quest hash: `2411514388`
- Quest path: `quests/minor_quest/mq025_07_fight_club`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `combat/neutralize`

### Objective sequence

1. **A fight in an Animals' club? Oof… feel sorry for you, I do. These guys play hard, V. It won't be easy… and it won't be fun.**  
   `Primary` · `quests/minor_quest/mq025_07_fight_club/club/07_club_fight`
   - Map pin: ref `#mq025_mp_07_fight_club`; position `-494.63442993164, -1931.0693359375, 8.5298929214478`
2. **Defeat Rhino.**  
   `Primary` · `quests/minor_quest/mq025_07_fight_club/club/07_fight`
3. **A fight in an Animals' club? Oof… feel sorry for you, I do. These guys play hard, V. It won't be easy… and it won't be fun.**  
   `Primary` · `quests/minor_quest/mq025_07_fight_club/club/07_talk`

## Beat on the Brat: The Glen

- IGN walkthrough: [Beat On The Brat: The Glen](https://www.ign.com/wikis/cyberpunk-2077/Beat_On_The_Brat:_The_Glen)
- Vanilla type: `MinorQuest`
- Quest hash: `456123091`
- Quest path: `quests/minor_quest/mq025_05_glen`
- District: Heywood
- Level: 60
- Candidate building blocks: `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **Defeat César.**  
   `Primary` · `quests/minor_quest/mq025_05_glen/glen/05_fight`
2. **Time for another rumble – this time in the Glen. I'd put money on their champ being a Valentino. Yeah, I can see him now: two golden fists and a machete across his back… y'know, in case things get dicey and take a turn for the unsportsmanlike.**  
   `Primary` · `quests/minor_quest/mq025_05_glen/glen/05_glen_fight`
   - Map pin: ref `#mq025_mp_05_glen`; position `-1788.9991455078, -1268.1921386719, 22.450578689575`
3. **Time for another rumble – this time in the Glen. I'd put money on their champ being a Valentino. Yeah, I can see him now: two golden fists and a machete across his back… y'know, in case things get dicey and take a turn for the unsportsmanlike.**  
   `Primary` · `quests/minor_quest/mq025_05_glen/glen/05_talk`

## Big in Japan

- IGN walkthrough: [Big in Japan](https://www.ign.com/wikis/cyberpunk-2077/Big_in_Japan)
- Vanilla type: `MinorQuest`
- Quest hash: `1453594350`
- Quest path: `quests/minor_quest/mq038_neweridentity`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Find the package, and deliver it from A to B. Simple job, huh? But then why not just book some delivery guy? And why not go through a fixer? Something smells off about this one, V.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village`
2. **Find and open the container with "No Future" graffiti'd on it.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02_find_dumpster`
3. **Talk to Dennis.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl`
4. **Pick up the body.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body`
5. **Carry the body to the car.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car`
6. **Put the body in the trunk.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk`
7. **Deliver the body to the specified coordinates.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside`
   - Map pin: ref `#mq038_mp_delivery`; position `-1333.4299316406, 2016.9798583984, 18.180000305176`
8. **Get in Dennis' car.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_enter_car`
9. **Talk to Dennis.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/08_talk_cargo`
10. **Leave the car.**  
   `Primary` · `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/09_leave_car`

## Blistering Love

- IGN walkthrough: [Blistering Love](https://www.ign.com/wikis/cyberpunk-2077/Blistering_Love)
- Vanilla type: `SideQuest`
- Quest hash: `292281615`
- Quest path: `quests/side_quest/sq031_cinema`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Can't even remember why Rogue and I were always at each other's throats. All I remember is the good times – and how few of them there were. Now I've got one night to make it up to her. Yeah, a movie date sounds boring, but hell, we never did normal, boring things. Better late than never, right?**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00_call_rogue`
2. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00_talk_to_rogue`
3. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00_talk_to_rogue1`
4. **Spend the evening with Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00_talk_to_rogue2`
5. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00_talk_to_rogue3`
6. **Get a car to take Rogue out on a date.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/00e_obtain_any_car`
7. **Go pick up Rogue at the Afterlife in the evening.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/01_pick_up_rogue_afterlife`
   - Map pin: ref `#sq011_mp_afterlife_rogue_wait`; position `-1466.8190917969, 1047.0938720703, 23.688293457031`
8. **Wait until evening.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/01a_afterlife_wait`
   - Map pin: ref `#sq011_mp_afterlife_wait`; position `-1462.8157958984, 1047.6774902344, 22.658027648926`
9. **Go to the drive-in movie theater with Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/02_get_to_cinema`
   - Map pin: ref `#sq031_mp_cinema`; position `-83.597412109375, 1981.8669433594, 102.37887573242`
10. **Find a way in the drive-in movie theater.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/02_get_to_cinema1`
11. **Use code 0000 to unlock the door.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/02_get_to_cinema2`
   - Map pin: ref `#sq031_mp_cinema_panel`; position `-80.99201965332, 1978.8071289063, 102.41887664795`
12. **Enter the drive-in movie theater.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/04_free_slot`
   - Map pin: ref `#sq031_mp_cinema_enter`; position `-81.610443115234, 1976.1791992188, 102.37887573242`
13. **Get in the car.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/04_get_into_porsche`
14. **Sit next to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/04_set_next_to_rogue`
15. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/06_talk_to_johnny`
16. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/06_talk_to_rogue`
17. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/06_talk_to_rogue1`
18. **Take the pills to give Johnny control.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/09a_take_pills`
19. **Get out of the car.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/10_leave_car`
20. **Get into the projection booth.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/11_look_around`
   - Map pin: ref `#sq031_mp_cinema_area`; position `-98.302642822266, 1952.9350585938, 100.52621459961`
   - Map pin: ref `#sq031_mp_control_room`; position `-76.158874511719, 1966.0550537109, 108.48887634277`
21. **Search the storage area.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/13_check_storage`
22. **Go back to Rogue.**  
   `Primary` · `quests/side_quest/sq031_cinema/bushidox/14_go_back_car1`

## Boat Drinks

- IGN walkthrough: [Boat Drinks](https://www.ign.com/wikis/cyberpunk-2077/Boat_Drinks)
- Vanilla type: `SideQuest`
- Quest hash: `2905849433`
- Quest path: `quests/side_quest/sq028_kerry_romance`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `choice/decision`, `leave/escape area`

### Journal premise

The marina, huh? Wonder what Kerry's got up his sleeve this time. Maybe he wants to get rid of someone – toss their body parts in the bay. Or maybe he just wants an audience while he waxes poetic about yachts over shrimp cocktails. Oh well, he's your problem now. Not mine.

### Objective sequence

1. **Leave with Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/aftermath`
2. **Swim to the shore.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/escape`
3. **Help Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/help_kerry`
4. **(Optional) Join Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/join_song`
5. **(Optional) Set the yacht on fire.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/light_match`
6. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry`
7. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry2`
8. **Wait for Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry`
9. **Break whatever you find!**  
   `Optional` · `quests/side_quest/sq028_kerry_romance/cruiser/break_shit`
   - Map pin: ref `#sq028_mp_coffee_machine`; position `-2455.2326660156, 3466.3813476563, 2.6538574695587`
   - Map pin: ref `#sq028_mp_gramophone`; position `-2449.884765625, 3467.3544921875, 2.6558449268341`
   - Map pin: ref `#sq028_mp_painting`; position `-2452.7456054688, 3461.4714355469, 3.1857817173004`
10. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3`
11. **Wait for Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things`
12. **Go onto the deck.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/marina/climb_aboard`
   - Map pin: ref `#sq028_mp_cabin_cruiser`; position `-2485.8559570313, -37.640949249268, 2.4162864685059`
13. **Meet Kerry at the marina at 7:00 PM.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/marina/meet_kerry`
   - Map pin: ref `#sq028_mp_wait_kerry_marina`; position `-2462.7448730469, -20.01224899292, 3.5358400344849`
14. **Talk to Kerry on the holo.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/marina/phone_call`
15. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq028_kerry_romance/marina/talk_kerry`

## Both Sides, Now

- IGN walkthrough: [Both Sides, Now](https://www.ign.com/wikis/cyberpunk-2077/Both_Sides,_Now)
- Vanilla type: `SideQuest`
- Quest hash: `3338893283`
- Quest path: `quests/side_quest/sq026_01_suicide`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/00_holocall/talk_judy`
2. **You ever hear the saying "No good deed goes unpunished"? You hold your hand out to someone, you get bitten. You help a poor soul in need, you get fleeced for all you're worth. Save someone's life? Fill in the blank.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/apartment`
   - Map pin: ref `#sq026_mp_judys_apartment`; position `-904.87945556641, 1868.4906005859, 43.871696472168`
3. **Close the bedroom door.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/close_door`
   - Map pin: ref `#sq026_dvc_judys_door_bedroom`; position `-900.60717773438, 1859.9619140625, 42.370010375977`
4. **Lay down Evelyn on the bed.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/evelyn_bed`
   - Map pin: ref `#sq026_tr_judys_bed`; position `-896.51007080078, 1857.1680908203, 42.250015258789`
5. **Carry Evelyn to the bedroom.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/evelyn_carry`
   - Map pin: ref `#sq026_tr_judys_bedroom`; position `-897.56414794922, 1859.5980224609, 42.160011291504`
6. **Lift up Evelyn.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/evelyn_pick_up`
7. **Leave the bedroom.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/leave_bedroom`
   - Map pin: ref `#sq026_tr_judys_living_room`; position `-903.68023681641, 1863.7836914063, 41.700012207031`
8. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/talk_judy`
9. **Wait for Judy to finish.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/01_suicide/wait_judy`
   - Map pin: ref `#sq026_tr_judys_bedroom`; position `-897.56414794922, 1859.5980224609, 42.160011291504`
10. **Cover Evelyn.**  
   `Optional` · `quests/side_quest/sq026_01_suicide/01_suicide/cover_evelyn`
11. **Join Judy on the rooftop.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/02_roof/join_roof`
   - Map pin: ref `#sq026_tr_01b_close`; position `-904.8095703125, 1857.494140625, 46.160011291504`
12. **Leave the building.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/02_roof/leave`
   - Map pin: ref `#sq026_mp_judys_exit`; position `-906.78930664063, 1846.6743164063, 36.560012817383`
13. **Sit on the couch.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/02_roof/sit_couch`
14. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_01_suicide/02_roof/talk_judy`

## Burning Desire

- IGN walkthrough: [Burning Desire](https://www.ign.com/wikis/cyberpunk-2077/Burning_Desire)
- Vanilla type: `MinorQuest`
- Quest hash: `1070867500`
- Quest path: `quests/minor_quest/mq012_stud`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `choice/decision`

### Objective sequence

1. **Neutralize or lose pursuing enemies.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/000_lose_heat`
2. **That's the great thing about Night City – no chance you'll ever get bored here. Where else could you have some dude with a smoking crotch jump into your car askin' to hitch a ride? Come on, V, show some sympathy. Get this guy to a ripper before his dick explodes all over your dashboard.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/00_find_out`
3. **Talk to the distressed man.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/01_talk_man`
4. **Decide whether or not to help.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/01b_help`
5. **Grab a car and pick up the distressed man.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/02_get_car`
6. **Go back to the car.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/02b_return_to_car`
7. **Take the distressed man to a ripperdoc.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/03_drive_ripperdoc`
   - Map pin: ref `#mq012_mp_ripperdoc_path`; position `-1598.9576416016, 2380.5729980469, 18.19970703125`
   - Map pin: ref `#mq012_mp_ripperdoc_path`; position `-1598.9576416016, 2380.5729980469, 18.19970703125`
8. **Stop in front of the ripperdoc clinic.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/04_stop_at_ripper`
9. **Keep busy while waiting for a call from the distressed man.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/05_wait_for_call`
10. **Talk to the distressed man.**  
   `Primary` · `quests/minor_quest/mq012_stud/00_stud/06_talk_to_stud`

## Chippin' In

- IGN walkthrough: [Chippin' In](https://www.ign.com/wikis/cyberpunk-2077/Chippin%27_In)
- Vanilla type: `SideQuest`
- Quest hash: `2659801358`
- Quest path: `quests/side_quest/sq031_rogue`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Wait a day for Rogue to call.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/00_wait_for_rogue_call`
2. **Call Rogue back.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/00a_call_rogue_back`
3. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife`
4. **Meet Rogue at the Afterlife.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife1`
   - Map pin: ref `#sq031_mp_afterlife_exterior`; position `-1465.1545410156, 1046.9713134766, 22.759357452393`
5. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife2`
6. **Follow Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife3`
7. **Get in Rogue's car.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife4`
8. **Drive with Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife5`
9. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife6`
10. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife7`
11. **Meet Rogue at the Afterlife.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/01_go_to_afterlife8`
12. **Take the gift from the trunk.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/05_pick_present`
13. **Get out of Rogue's car.**  
   `Primary` · `quests/side_quest/sq031_rogue/02_afterlife/07_leave_car`
14. **This is it, Rogue's in for the kill – she's ready to stop running from her past and catch Smasher. And when we catch the bastard, I wanna be the one to pull the trigger. But for now – you're in charge. Happy hunting!**  
   `Primary` · `quests/side_quest/sq031_rogue/afterlife/01_go_to_afterlife`
   - Map pin: ref `#sq031_mp_afterlife`; position `-1457.8620605469, 1020.3382568359, 17.746793746948`
15. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_rogue/afterlife/02_talk_to_johnny`
   - Map pin: ref `#sq031_mp_afterlife`; position `-1457.8620605469, 1020.3382568359, 17.746793746948`
16. **Drive to the oil fields.**  
   `Primary` · `quests/side_quest/sq031_rogue/grave/01_travel_to_grave`
   - Map pin: ref `#sq031_mp_oil_fields`; position `-1845.3988037109, 3855.27734375, 7.4420413970947`
17. **Get out of the car.**  
   `Primary` · `quests/side_quest/sq031_rogue/grave/02_leave_car`
18. **Find Johnny's grave.**  
   `Primary` · `quests/side_quest/sq031_rogue/grave/03_check_area`
   - Map pin: ref `#sq031_mp_oil_fields`; position `-1845.3988037109, 3855.27734375, 7.4420413970947`
19. **Sit next to Johnny.**  
   `Primary` · `quests/side_quest/sq031_rogue/grave/04_sit_grave`
20. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_rogue/grave/06_talk_to_johnny`
21. **Open Cargo Door**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/00a_open_door`
   - Map pin: ref `#sq031_mp_open_door`; position `-1562.6346435547, 2986.0224609375, 11.58158493042`
22. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/01_go_to_afterlife1`
23. **Talk to Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/01_go_to_afterlife2`
24. **Follow Rogue.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/01_go_to_afterlife3`
25. **Find the Dataterm.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/01_search_ebunike_area`
26. **Check the Dataterm.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/01_search_ebunike_area1`
27. **Look for Smasher on the Ebunike.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/02_seach_ebunike_deck`
   - Map pin: ref `#sq031_mp_ebumike_deck`; position `-1541.2966308594, 3086.0512695313, 16.551902770996`
   - Map pin: ref `#sq031_mp_to_ebumike_deck`; position `-1574.6842041016, 3068.2346191406, 9.2330827713013`
28. **Defeat Grayson.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/03_defeat_grayson`
29. **Question Grayson about Smasher.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/03_defeat_grayson1`
30. **Take Johnny's gun.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/04a_pick_malorian`
31. **Lower the crane.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/06_find_car`
32. **Open the container.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/06_find_car1`
   - Map pin: ref `#sq031_mp_open_cargo`; position `-1540.8646240234, 3053.3276367188, 9.322452545166`
33. **Remove the canvas cover.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/08_remove_cloth`
   - Map pin: ref `#sq031_mp_cloth`; position `-1543.5874023438, 3055.3474121094, 8.0756855010986`
34. **Get in Johnny's Porsche.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/09_get_into_porsche`
35. **Listen to the recordings.**  
   `Optional` · `quests/side_quest/sq031_rogue/malorian/02a_listen_audio_database`
36. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq031_rogue/malorian/09a_talk_to_johnny`

## Coin Operated Boy

- IGN walkthrough: [Coin Operated Boy](https://www.ign.com/wikis/cyberpunk-2077/Coin_Operated_Boy)
- Vanilla type: `MinorQuest`
- Quest hash: `3012986478`
- Quest path: `quests/minor_quest/mq037_brendan`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`

### Objective sequence

1. **All right, so I'm feeling like a sucker for this story. Do you really think Brendan is just spitting out the sentences is was programmed for? The stuff some marketing guru thinks customers want to hear? That'd be pretty fucked even by Night City standards. In any case, we won't know until you find him.**  
   `Primary` · `quests/minor_quest/mq037_brendan/mq037_brendan/01_go_to_service`
   - Map pin: ref `#mq037_mrk_service_point_mappin`; position `-1938.3715820313, -958.85119628906, 7.7307362556458`
2. **Find Brendan.**  
   `Primary` · `quests/minor_quest/mq037_brendan/mq037_brendan/02_find_brendan`
   - Map pin: ref `#mq037_tr_service_point_area_mappin`; position `-1945.5948486328, -958.58868408203, 7.7018609046936`
3. **Talk to the clerk.**  
   `Optional` · `quests/minor_quest/mq037_brendan/mq037_brendan/02b_ask_clerk`
4. **Destroy the turret.**  
   `Primary` · `quests/minor_quest/mq037_brendan/mq037_brendan/02c_destroy_turret`
5. **Talk to Brendan.**  
   `Primary` · `quests/minor_quest/mq037_brendan/mq037_brendan/03_talk_brendan`
6. **Talk to Theo.**  
   `Primary` · `quests/minor_quest/mq037_brendan/mq037_brendan/04_talk_theo`

## Don't Lose Your Mind

- IGN walkthrough: [Don't Lose Your Mind](https://www.ign.com/wikis/cyberpunk-2077/Don%27t_Lose_Your_Mind)
- Vanilla type: `SideQuest`
- Quest hash: `4231528668`
- Quest path: `quests/side_quest/sq025b_delamain_insurgence`
- District: Heywood
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `search/investigate`, `interact/use device`, `hack/breach/download`, `deliver/deposit item`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Find Delamain's core.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_00_go_core`
2. **Call Delamain.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_01_call_delamain`
3. **Search the office for a way to open the door.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_03b_use_computer`
   - Map pin: ref `#sq025_mp_delamain_garage_manager`; position `-954.54705810547, -91.874626159668, 9.0577945709229`
4. **Find a way into the control room.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_08_go_core`
   - Map pin: ref `#sq025_mp_delamain_garage_controls`; position `-967.75170898438, -156.17868041992, 8.6119556427002`
5. **Hear out the Delamains.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_08b_listen_delamain`
6. **Reset the core to restore the original Delamain.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_09_01_reset_core`
7. **Destroy the core to liberate the divergent Delamains.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_09_02_destroy_core`
8. **Your buddy Delamain appears to be having some personal issues. How else do you explain his cabs standing in the middle of the road and blocking traffic? Better give him a call. Besides, you're short on friends (present imaginary company excluded).**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_02_go_garage`
   - Map pin: ref `#sq025_mp_delamain_garage_entrance`; position `-943.82696533203, -81.245407104492, 9.0097923278809`
9. **Find a way inside Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_03_get_inside`
   - Map pin: ref `#sq025_delamain_garage_private_area`; position `-960.35632324219, -94.004180908203, 7.5097951889038`
10. **Find a way into the workshop.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_05_enter_workshop`
   - Map pin: ref `#sq025_mp_delamain_garage_repair_entry_01`; position `-944.90435791016, -104.45613861084, 9.0097913742065`
11. **Find a way to the stairs.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_01_stairs`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_otherside`; position `-920.71997070313, -120.86001586914, 9.2499990463257`
12. **Proceed down the hallway.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_04_enter_garage`
   - Map pin: ref `#sq025_mp_delamain_garage_office_exit_02`; position `-958.72662353516, -103.15785217285, 9.1199111938477`
13. **Cross the room.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_03_bigleft`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_left_big`; position `-934.98986816406, -139.91998291016, 8.5999994277954`
14. **Go on the catwalk.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_04_catwalk`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_catwalk`; position `-951.54986572266, -144.08010864258, 14.340000152588`
15. **Head to the hangar.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_05_hangar`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_hangar`; position `-973.62994384766, -128.8503112793, 14.009999275208`
16. **Enter the shaft.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_06_shaft`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_shaft_control`; position `-985.35992431641, -149.41012573242, 12.25`
17. **Go downstairs.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_gen_backdown`
   - Map pin: ref `#sq025_mp_gen_delamain_garage_shaft_down`; position `-955.65997314453, -110.95017242432, 12.059999465942`
18. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_08c_talk_johnny_core`
19. **Decide Delamain's fate.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_09_resolution`
20. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_09b_talk`
21. **Investigate the source of the noises coming from the side exit.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_10_follow_noise`
   - Map pin: ref `#sq025_mp_delamain_garage_core_exit`; position `-978.78900146484, -160.04034423828, 9.4217958450317`
   - Map pin: ref `#sq025_mp_delamain_garage_look_entry`; position `-987.76031494141, -153.75854492188, 11.425989151001`
   - Map pin: ref `#sq025_mp_delamain_garage_look_window`; position `-993.27178955078, -150.19702148438, 11.762449264526`
22. **Leave through the side exit.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_10_follow_noise1`
23. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_10b_johnny_hangar`
24. **Leave the garage.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_11a_leave_look`
   - Map pin: ref `#sq025_mp_delamain_garage_look_exit`; position `-999.05627441406, -158.54325866699, 11.325080871582`
25. **Leave Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_12_leave`
26. **Approach the car.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_13_check_delamain`
27. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_13b_talk_delamain`
28. **Get in the driver's seat.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_14_enter_car`
29. **Hack the core to merge all of the Delamains.**  
   `Optional` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_09_03_merge_core`
30. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04_showdown/04_14_enter_car1`
31. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04a_resurgence/03b_02_talk_johnny`
32. **Your buddy Delamain appears to be having some personal issues. How else do you explain his cabs standing in the middle of the road and blocking traffic? Better give him a call. Besides, you're short on friends (present imaginary company excluded).**  
   `Primary` · `quests/side_quest/sq025b_delamain_insurgence/04a_resurgence/03b_check_traffic`

## Dream On

- IGN walkthrough: [Dream On](https://www.ign.com/wikis/cyberpunk-2077/Dream_On)
- Vanilla type: `SideQuest`
- Quest hash: `3216693788`
- Quest path: `quests/side_quest/sq006_dream_on`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `leave/escape area`

### Objective sequence

1. **Call Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/after_ambush/call_elizabeth`
2. **Call Jefferson.**  
   `Primary` · `quests/side_quest/sq006_dream_on/after_ambush/call_jefferson`
3. **Consult with Johnny.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/disccus_with_johnny`
4. **Escape the ambush.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/escape_ambush`
5. **Meet with Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/find_elizabeth`
6. **Go to the ramen shop.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/ramen_shop`
7. **Sit with Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/sit_with_elizabeth`
   - Map pin: ref `#sq006_mappin_sit_ramen_shop`; position `-649.91204833984, 934.30023193359, 10.199999809265`
8. **Talk to Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/clandestine_elizabeth/speak_to_elizabeth`
9. **Meet with Jefferson.**  
   `Primary` · `quests/side_quest/sq006_dream_on/conclusion/return_to_apartment`
   - Map pin: ref `#sq006_mappin_park`; position `-1694.8518066406, -190.05090332031, 13.427742004395`
10. **Talk to Jefferson.**  
   `Primary` · `quests/side_quest/sq006_dream_on/conclusion/sq006_speak_to_jefferson`
11. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq006_dream_on/conclusion/talk_to_johnny`
12. **Analyze the data**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/analyze_data`
13. **Neutralize the attackers.**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/defeat_ambush`
14. **Follow the surveillance van.**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/follow_truck`
15. **Look for the surveillance van.**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/go_to_parking_lot`
   - Map pin: ref `#sq006_mappin_parking_lot`; position `-422.03454589844, 51.124477386475, 17.597272872925`
16. **Leave the apartment.**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/leave_apartment`
17. **Connect to the van's Access Point.**  
   `Primary` · `quests/side_quest/sq006_dream_on/find_surveillance/search_truck`
18. **Use the intercom.**  
   `Primary` · `quests/side_quest/sq006_dream_on/intro/02_use_intercom`
   - Map pin: ref `#sq006_use_mappin_use_intercom`; position `-66.655738830566, -97.134262084961, 8.7029113769531`
19. **Take the elevator.**  
   `Primary` · `quests/side_quest/sq006_dream_on/intro/03_take_elevator`
   - Map pin: ref `#sq006_mappin_apartment_elevator`; position `-72.312362670898, -114.27572631836, 8.7589111328125`
   - Map pin: ref `#sq006_mp_top_floor`; position `-72.305549621582, -114.07197570801, 112.41729736328`
20. **Call Jefferson back.**  
   `Primary` · `quests/side_quest/sq006_dream_on/intro/call_jefferson`
21. **!OBSOLETE**  
   `Primary` · `quests/side_quest/sq006_dream_on/intro/sq006_go_to_apartment`
22. **Find the hidden room.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_find_locked_room`
   - Map pin: ref `#sq006_mappin_hidden_door`; position `-66.900405883789, -120.94534301758, 116.59729766846`
23. **Find the transmission source.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_find_transmitter`
   - Map pin: ref `#sq006_mappin_parking_lot`; position `-422.03454589844, 51.124477386475, 17.597272872925`
24. **Follow the blood trail.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_follow_blood_stains`
   - Map pin: ref `#sq006_mappin_bloodstain_01`; position `-68.976737976074, -106.19723510742, 115.16729736328`
   - Map pin: ref `#sq006_mappin_bloodstain_02`; position `-65.766525268555, -120.49411010742, 115.15729522705`
25. **Search the security room for a way to open the hidden door.**  
   `Optional` · `quests/side_quest/sq006_dream_on/investigation/sq006_look_for_a_way_in`
   - Map pin: ref `#sq006_mappin_security_office`; position `-66.68611907959, -105.87232208252, 113.05729675293`
26. **Follow the cables.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_follow_cables`
27. **Examine the apartment.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_investigate_apartment`
   - Map pin: ref `#sq006_mappin_bedroom`; position `-77.705726623535, -130.15283203125, 116.65729522705`
   - Map pin: ref `#sq006_mappin_entertainment_room`; position `-73.657752990723, -105.62967681885, 116.49729919434`
   - Map pin: ref `#sq006_mappin_kitchen`; position `-61.513244628906, -121.68995666504, 112.72729492188`
   - Map pin: ref `#sq006_mappin_main_office`; position `-91.842864990234, -121.76766204834, 116.61729431152`
   - Map pin: ref `#sq006_mappin_security_office`; position `-66.68611907959, -105.87232208252, 113.05729675293`
28. **Find another way into the locked room.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_keep_looking`
29. **Scan to find where the trail of blood leads.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_look_for_where_stains_go`
30. **Scan the strange computer.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_scan_electronics`
31. **Scan for signs of break in.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_signs_of_breakin`
32. **Open the secret door.**  
   `Primary` · `quests/side_quest/sq006_dream_on/investigation/sq006_unlock_door`
33. **Follow Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_follow_elizabeth`
34. **Sit**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_sit_down`
   - Map pin: ref `#sq006_mp_sit_apartment`; position `-94.96501159668, -123.13321685791, 111.61729431152`
35. **Talk to Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_talk_about_investigation`
36. **Talk to Elizabeth.**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_talk_to_elizabeth`
37. **Talk to the Peralezes.**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_talk_to_peralezs`
38. **Let Elizabeth show you around.**  
   `Primary` · `quests/side_quest/sq006_dream_on/meeting/sq006_tour_with_liz`

## Epistrophy

- IGN walkthrough: [Epistrophy](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy)
- Vanilla type: `SideQuest`
- Quest hash: `3422781529`
- Quest path: `quests/side_quest/sq025_delamain`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Cars didn't talk back in my day, and now this one wants to give you a job? What a time to be alive… What're you waiting for?**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_00_talk_delamain`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`
2. **Follow Delamain's Drone.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_01_follow_delamain`
3. **Take the scanner.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_01c_take_scanner`
4. **Leave the garage.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_02_leave_garage`
   - Map pin: ref `#sq025_mp_delamain_garage_entrance`; position `-943.82696533203, -81.245407104492, 9.0097923278809`
5. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_02b_talk_delamain`
   - Map pin: ref `#sq025_mp_center_screen_controlroom`; position `-969.36987304688, -158.80001831055, 10.549999237061`
6. **Return to Delamain and talk with the receptionist.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_03_refused`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`
7. **Return later to Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_03a_return_later`
8. **(unnamed objective)**  
   `Primary` · `quests/side_quest/sq025_delamain/02_briefing/02_04_refused_talk`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`
9. **Get in your vehicle and begin driving.**  
   `Primary` · `quests/side_quest/sq025_delamain/03_scan/03_01_find_delamain`
10. **Reestablish connection between Delamain and his divergent forms.**  
   `Primary` · `quests/side_quest/sq025_delamain/03_scan/03_02_scan_delamains`
11. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025_delamain/03_scan/03_03_scan_talk`
12. **Return to Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025_delamain/04_scan_types/04_01_return`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`
13. **Place the scanner in the box.**  
   `Primary` · `quests/side_quest/sq025_delamain/04_scan_types/04_02_return_scanner`
14. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025_delamain/04_scan_types/04_03_talk_del`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`

## Epistrophy: Badlands

- IGN walkthrough: [Epistrophy: Badlands](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Badlands)
- Vanilla type: `SideQuest`
- Quest hash: `3766414125`
- Quest path: `quests/side_quest/sq025c06_mean`
- District: Southern Badlands
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Over the mountains, through the woods, nestled on the hills beyond North Oak – that's where your pal Delamain lost one of his cabs. He's a goddamn talking car himself and, apparently, has more cars of his own. I dunno, but I just say we continue this little fairy tale, find that cab, save the princess and claim half the kingdom.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06_find_mean`
2. **Approach the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06a_scan_deep`
3. **Talk to the divergent Delamain.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06b_disable_deep`
4. **Get in the cab.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06bb_enter_deep`
5. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06c_return_deep`
6. **Get out of the cab.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06d_exit_deep`
7. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06w_wait_deep`
8. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c06_mean/06_find_mean/06x_complete_deep`

## Epistrophy: Coastview

- IGN walkthrough: [Epistrophy: Coastview](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Coastview)
- Vanilla type: `SideQuest`
- Quest hash: `3319795592`
- Quest path: `quests/side_quest/sq025c03_mean`
- District: Pacifica
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `combat/neutralize`

### Objective sequence

1. **Ever been to Coastview? Not too shabby. Had an output from there once. Sure, maybe she liked to wheeze, jab, pop and snort a little too much, but who wasn't in those days? Her name was Amanda or Amelie or something, I don't remember. Remind me to tell you the shooting range story sometime.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03_find_mean`
2. **Approach the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03a_scan_mean`
3. **Stay within signal range.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03b_disable_mean`
4. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03c_return_mean`
5. **Talk to the divergent Delamain.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03e_talk`
6. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03w_wait_mean`
7. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/03x_complete_mean`
8. **Defeat the gangoons.**  
   `Primary` · `quests/side_quest/sq025c03_mean/03_find_mean/04_defeat_goons`

## Epistrophy: North Oak

- IGN walkthrough: [Epistrophy: North Oak](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_North_Oak)
- Vanilla type: `SideQuest`
- Quest hash: `504159030`
- Quest path: `quests/side_quest/sq025c02_sad`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **A taxi in distress calls for a hero like you, V. If you want to become a legend, set out on this quest for ultimate glory. The Afterlife awaits!**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02_find_sad`
2. **Approach the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02a_scan_sad`
3. **Stay close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02b_disable_sad`
4. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02c_return_sad`
5. **Drive the cab back to Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02c_return_sad1`
6. **Get back in the car.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02d_2_return_car_sad`
7. **Get in the driver's seat.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02d_enter_car`
8. **Slowly drive the cab back to Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02e_drive_home`
9. **Get out of the cab.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02g_leave_sad`
10. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02w_wait_sad`
11. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c02_sad/02_find_sad/02x_complete_sad`

## Epistrophy: Northside

- IGN walkthrough: [Epistrophy: Northside](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Northside)
- Vanilla type: `SideQuest`
- Quest hash: `4123501517`
- Quest path: `quests/side_quest/sq025c05_scared`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `wait/time gate`, `search/investigate`

### Objective sequence

1. **I kinda like this Delamain. He's comfortable in his own code, not ashamed to be a talking car. He's asked you to find one of his rides in Northside, so I say we do him a favor.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05_find_scared`
2. **Find the hidden Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05a_scan_scared`
3. **Follow the Delamain cab until it stops.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05b_disable_scared`
4. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05c_return_scared`
5. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05w_wait_scared`
6. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c05_scared/05_find_scared/05x_complete_scared`

## Epistrophy: Rancho Coronado

- IGN walkthrough: [Epistrophy: Rancho Coronado](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_Rancho_Coronado)
- Vanilla type: `SideQuest`
- Quest hash: `3225381716`
- Quest path: `quests/side_quest/sq025c04_manic`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`

### Objective sequence

1. **Never been a fan of Rancho Coronado, personally. If you really gotta find a cab out there, just do it quick and get back into the city, OK?**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04_find_manic`
2. **Approach the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04a_scan_manic`
3. **Stay within signal range.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04b_disable_manic`
4. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04c_return_manic`
5. **Destroy the flamingos.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04d_destroy_flamingos`
6. **Talk to the divergent Delamain.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04e_talk_manic`
7. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/04w_wait_manic`
8. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c04_manic/04_find_manic/05x_complete_manic`

## Epistrophy: The Glen

- IGN walkthrough: [Epistrophy: The Glen](https://www.ign.com/wikis/cyberpunk-2077/Epistrophy:_The_Glen)
- Vanilla type: `SideQuest`
- Quest hash: `1593954720`
- Quest path: `quests/side_quest/sq025c07_suicidal`
- District: Heywood
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`, `deliver/deposit item`, `vehicle sequence`

### Objective sequence

1. **Wait for Delamain to call.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/071w_wait_suidial`
2. **Ahh, the Glen. You know this used to be a college campus? Some thought that taking out colossal loans and enrolling in a biotech degree would make their lives better. Then the harsh reality kicked in – it was easier to throw yourself off a bridge than get into a corporate research lab. Makes you wonder why our rogue Delamain cab chose this place of all places.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/07_find_suicidal`
3. **Approach the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/07a_scan_suicidal`
4. **Stay within signal range.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/07b_disable_suicidal`
5. **Get back close to the Delamain cab.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/07c_return_suicidal`
6. **Talk to Delamain.**  
   `Primary` · `quests/side_quest/sq025c07_suicidal/07_find_suicidal/07x_complete_suicidal`

## Ex-Factor

- IGN walkthrough: [Ex-Factor](https://www.ign.com/wikis/cyberpunk-2077/Ex-Factor)
- Vanilla type: `SideQuest`
- Quest hash: `638462496`
- Quest path: `quests/side_quest/sq026_02_maiko`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `interact/use device`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Someone once said, "No man ever steps in the same river twice." No clue who said it, but he was a smart dude. Now, there are lots of rivers in this world (most of them toxic, but whatever) – places you could explore instead of stomping over the same ol' grounds. And lots and lots of joyhouses. What's this one got that the others don't?

### Objective sequence

1. **Call Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/00_holocall/call_judy`
2. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/00_holocall/talk_judy`
3. **Enter office.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/enter_office`
4. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/follow_judy`
5. **Exit Clouds.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/leave_dollhouse`
6. **Meet Judy on Clouds' terrace in early morning.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/meet_megabuilding`
7. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/reunite_judy`
8. **Talk to Judy and Maiko.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/talk_maiko`
9. **Ride the Elevator to Clouds.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/use_elevator`
10. **Wait until early morning.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/01_maiko/wait_judy`
11. **Exit the elevator.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/exit_elevator`
12. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/follow_judy`
13. **Leave the megabuilding with Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/leave_megabuilding`
14. **Open the elevator doors.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/open_door`
15. **Defeat Woodman.**  
   `Optional` · `quests/side_quest/sq026_02_maiko/02_ambush/defeat_ambush`
16. **Ride the elevator to the ground floor.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/take_elevator_down`
17. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_02_maiko/02_ambush/talk_judy`
18. **Ride the elevator to the maintenance level.**  
   `Optional` · `quests/side_quest/sq026_02_maiko/02_ambush/take_elevator_maintenance`
19. **Confront Woodman.**  
   `Optional` · `quests/side_quest/sq026_02_maiko/02_ambush/talk_woodman`

## Ezekiel Saw the Wheel

- IGN walkthrough: [Ezekiel Saw The Wheel](https://www.ign.com/wikis/cyberpunk-2077/Ezekiel_Saw_The_Wheel)
- Vanilla type: `MinorQuest`
- Quest hash: `3697221403`
- Quest path: `quests/minor_quest/mq022_ezekiel`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **Identify the gunmen.**  
   `Primary` · `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/01_diner`
2. **Here's a joke for you: V walks into a bar… and gets robbed. The end.\n\nJesus, you and your shit luck. You better figure something out quick or our epic story's about to get cut short in the stupidest way imaginable. Accidental deaths don't jive too well with me. Or with the birth of legends.**  
   `Primary` · `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide`
   - Map pin: ref `#mq022_tr_restricted_area`; position `-539.74401855469, -740.87994384766, 7.804000377655`
3. **Talk to the diner owner.**  
   `Primary` · `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome`

## Following the River

- IGN walkthrough: [Following The River](https://www.ign.com/wikis/cyberpunk-2077/Following_The_River)
- Vanilla type: `SideQuest`
- Quest hash: `1678974732`
- Quest path: `quests/side_quest/sq029_sobchak_romance`
- District: Southern Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **Stir the soy meat.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/01_stir_soya`
   - Map pin: ref `#sq029_mappin_cooking_pot`; position `1237.677734375, -500.10073852539, 37.394054412842`
2. **Take the rice to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/02_bring_rice`
3. **Find rice in the kitchen.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/02a_take_rice`
   - Map pin: ref `#sq029_mp_kitchen_area`; position `1242.3505859375, -532.59033203125, 37.845897674561`
4. **Add rice to pot.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/03_add_rice`
   - Map pin: ref `#sq029_mappin_cooking_pot`; position `1237.677734375, -500.10073852539, 37.394054412842`
5. **Add spices.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/04_add_spices`
6. **Tell Joss the food is ready.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/05_find_joss`
7. **Take the rice.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/06_rice`
8. **Sit with River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/07_sit_down`
   - Map pin: ref `#sq029_mappin_patio_chair`; position `1236.890625, -513.35961914063, 37.970001220703`
9. **Talk to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/02_cooking/08_talk_river`
10. **Kids' Score:**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/00_kids_score`
11. **Adults' Score:**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/00_player_score`
12. **Talk to River and the kids.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/02a_talk_river`
13. **Eliminate all targets in the AR combat area.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/04_round_1`
   - Map pin: ref `#sq029_tr_ar_round_01`; position `1218.9073486328, -480.10293579102, 35.179016113281`
14. **Go to the starting position for a new round.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/04_round_start`
15. **Let the kids win.**  
   `Optional` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/03a_kids_win`
16. **Eliminate all targets in the AR combat area.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/05_round_2`
   - Map pin: ref `#sq029_tr_ar_round_02`; position `1190.8996582031, -495.24996948242, 33.080017089844`
17. **Go to the starting position for a new round.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/05_round_start`
18. **Eliminate all targets in the AR combat area.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/06_round_3`
   - Map pin: ref `#sq029_tr_ar_round_03`; position `1202.7496337891, -520.58996582031, 33.360015869141`
   - Map pin: ref `#sq029_tr_ar_round_03a`; position `1223.5296630859, -530.33996582031, 33.360015869141`
   - Map pin: ref `#sq029_tr_ar_round_03b`; position `1232.2255859375, -532.35400390625, 33.360015869141`
   - Map pin: ref `#sq029_tr_ar_round_03a`; position `1223.5296630859, -530.33996582031, 33.360015869141`
   - Map pin: ref `#sq029_tr_ar_round_03b`; position `1232.2255859375, -532.35400390625, 33.360015869141`
19. **Go to the starting position for a new round.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/06_round_start`
20. **Confront El Chamuco Endiablado and his goons.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/07_final_round`
   - Map pin: ref `#sq029_tr_ar_round_04`; position `1228.119140625, -517.66015625, 36.110004425049`
21. **Talk to River about the AR game.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/08_river_abt_game`
22. **Head over to the kids.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/kids`
23. **Play the AR game.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/vr_game`
24. **Grab the AR game gear.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/07_ar_game/vr_game1`
25. **Join Joss at the table.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/bbq/01_go_to_table`
26. **Eat jambalaya with River's family.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/bbq/eat_dinner_with_fam`
27. **Sit.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/bbq/sit_down`
   - Map pin: ref `#sq029_mappin_bbq_seat`; position `1239.5029296875, -502.46347045898, 37.219295501709`
28. **See what River's up to.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/breakfast/join_river`
29. **Talk to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/breakfast/talk_with_river`
30. **Call River to organize a dinner at Joss's.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/burial/bury_the_dog`
31. **Talk to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/05_talk_river`
32. **Open the gate.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/06_gate`
   - Map pin: ref `#sq029_mappin_gate`; position `1256.2747802734, -452.65447998047, 45.300045013428`
33. **Find a way through the fence.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/06a_fenced_area`
   - Map pin: ref `#sq029_tr_fenced_area`; position `1258.6746826172, -446.39004516602, 44.189994812012`
34. **Climb up the tower with River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/07_climb_tower`
   - Map pin: ref `#sq029_mappin_tower`; position `1241.4494628906, -449.88986206055, 68.239990234375`
35. **Follow River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/go_with_river`
36. **Sit with River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/hang_out_with_river`
37. **Walk with River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/drink_with_river/spend_time_with_river`
38. **Wait for River by the barrels.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/01a_wait_at_place`
   - Map pin: ref `#sq029_mappin_wait_lean`; position `1223.7844238281, -470.64663696289, 36.919033050537`
39. **Talk to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/05_talk_to_river`
40. **The Peter Pan case is done and closed, so you do know you never have to see this badge again… right? OK, fine, I get it, you crawled through shit and fire together, and now you wanna kick back and celebrate your victory. But a family dinner? Fuckin' seriously? Can't just find a decent dive to grab a tequila or ten? Smash the bottle over some corpocunt's face? You're getting soft, V.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/go_to_joss_house`
   - Map pin: ref `#sq029_mappin_yard`; position `1235.6107177734, -503.4621887207, 37.001033782959`
41. **Head over to River.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/help_river_with_grill`
42. **Join River and Joss.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/join_river_with_fam`
43. **Talk to Joss.**  
   `Optional` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/join_joss_inside`
44. **Talk to River and Joss.**  
   `Primary` · `quests/side_quest/sq029_sobchak_romance/join_river_with_fam/talk_to_joss_and_river`

## Fool on the Hill

- IGN walkthrough: [Fool on the Hill](https://www.ign.com/wikis/cyberpunk-2077/Fool_on_the_Hill)
- Vanilla type: `MinorQuest`
- Quest hash: `1050173186`
- Quest path: `quests/minor_quest/mq033_tarot`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`

### Journal premise

Maybe these strange images that you're seein' really do exist. Or maybe the biochip's already turned your brain into scop and salmon casserole. Whatever the case, spotting these symbols in unexpected places feels like a mystery beggin' to be solved. In your shoes, I'd have a word with Viktor or that chakra chick about these. Should interest at least one of 'em.

### Objective sequence

1. **Talk to Misty.**  
   `Primary` · `quests/minor_quest/mq033_tarot/mq033_tarot/01_talk_to_misty`
2. **Find all the tarot graffiti in the city.**  
   `Primary` · `quests/minor_quest/mq033_tarot/mq033_tarot/02_find_all_murals`
3. **Press RB to teleport**  
   `Optional` · `quests/minor_quest/mq033_tarot/mq033_tarot/00_debug_teleport_hint`
4. **Talk to Misty.**  
   `Primary` · `quests/minor_quest/mq033_tarot/mq033_tarot/03_talk_to_misty`
5. **Talk to Viktor.**  
   `Optional` · `quests/minor_quest/mq033_tarot/mq033_tarot/01_talk_to_victor`
   - Map pin: ref `#ws_victor_vector_default`; position `-1542.5921630859, 1230.2431640625, 11.519449234009`

## Fortunate Son

- IGN walkthrough: [Fortunate Son](https://www.ign.com/wikis/cyberpunk-2077/Fortunate_Son)
- Vanilla type: `MinorQuest`
- Quest hash: `3933167984`
- Quest path: `quests/minor_quest/mq021_guide`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **Kidney failure. In the city, nothing that a stack of eddies and a few minutes won't solve. But in the Badlands… a death sentence. That is, unless a gentle soul somewhere feels like playin' guardian angel. Someone that'll get him the implant he needs before it's too late. Well, V? Think there's anyone out there like that?**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/04_meeting`
   - Map pin: ref `#mq021_mp_hospital`; position `-1310.7009277344, 1842.4840087891, 18.190002441406`
2. **Meet with the hospital employee.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting`
3. **Defeat the police.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/06_defend`
4. **Take the briefcase with the implant.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/07_2_get_suitcase`
5. **Confront the hospital employee.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor`
6. **Return to the Aldecaldos camp.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/08_outcome`
   - Map pin: ref `#mq021_mp_drop_case`; position `1801.0911865234, 2245.7124023438, 180.6686706543`
7. **Kill the hospital employee.**  
   `Optional` · `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor`
8. **Talk to Bob.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/09_ending`
9. **Return to the camp in eight hours' time, when the operation is complete.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/10_ending_wait`
10. **Read Bob's message.**  
   `Primary` · `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read`

## Full Disclosure

- IGN walkthrough: [Full Disclosure](https://www.ign.com/wikis/cyberpunk-2077/Full_Disclosure)
- Vanilla type: `MinorQuest`
- Quest hash: `1278009373`
- Quest path: `quests/minor_quest/mq024_sandra`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

Sandra Dorsett… that chick you pulled out of a scavs' nest? Man, give someone an inch and they take a mile… This databank must be pretty special to her if she ain't even willing to go through a fixer. Well, damn… now I'm kinda curious. Gonna help out – or play by the rules of the game?

### Objective sequence

1. **Find Sandra's databank.**  
   `Primary` · `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier`
   - Map pin: ref `#mq024_mp_data_carrier_area`; position `-1113.0070800781, 2147.9089355469, 13.303318977356`
2. **Sandra Dorsett who we rescued from scavengers called V and asked to find and retrieve her data carrier.**  
   `Primary` · `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra`
3. **Meet with Sandra.**  
   `Primary` · `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra`
   - Map pin: ref `#mq024_mp_sandra_door`; position `-1283.1962890625, 1518.6813964844, 46.545330047607`
4. **Defeat Sandra.**  
   `Primary` · `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra`

## Gun Music

- IGN walkthrough: [Gun Music](https://www.ign.com/wikis/cyberpunk-2077/Gun_Music)
- Vanilla type: `MinorQuest`
- Quest hash: `255487383`
- Quest path: `quests/minor_quest/mq002_veterans`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `interact/use device`, `combat/neutralize`

### Objective sequence

1. **The Aldecaldos must really be desperate. To come this close to the city, and deal with scavs no less… Risky move. Sounds like they could use a hand.**  
   `Primary` · `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro`
   - Map pin: ref `#mq002_mp_deal`; position `-357.26000976563, -952.35980224609, 6.6199998855591`
2. **Help the nomads negotiate a deal.**  
   `Primary` · `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal`
3. **Defeat the scavengers.**  
   `Primary` · `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight`
   - Map pin: ref `#mq002_tr_start`; position `-352.25338745117, -957.52447509766, 6.6199994087219`
4. **Talk to Carol.**  
   `Primary` · `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary`

## Happy Together

- IGN walkthrough: [Happy Together](https://www.ign.com/wikis/cyberpunk-2077/Happy_Together)
- Vanilla type: `MinorQuest`
- Quest hash: `313901610`
- Quest path: `quests/minor_quest/mq010_barry`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`

### Journal premise

Seems like the PD's taken an interest in a neighbor of yours. Even sounded like they knew each other. Will you assume the mantle of a concerned, responsible citizen and ask what's going on? I mean, if you got a potential psycho for a neighbor, wouldn't you want to know?

### Objective sequence

1. **Talk to the cops.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/01_hook`
2. **Talk to the cops.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/05_tell_police`
3. **Check on Barry.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/06_see_what_happened`
   - Map pin: ref `#mq010_mp_barry_door`; position `-1393.8206787109, 1301.7896728516, 120.40999603271`
4. **Find Andrew's niche before talking to the cops.**  
   `Optional` · `quests/minor_quest/mq010_barry/mq010_barry/04_columbarium`
5. **Try talking to Barry in a few hours.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/02_wait_for_barry`
6. **Talk to Johnny.**  
   `Optional` · `quests/minor_quest/mq010_barry/mq010_barry/04a_andrew_plaque`
7. **Talk to Barry.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/03_talk_to_barry`
   - Map pin: ref `#mq010_mp_barry_door`; position `-1393.8206787109, 1301.7896728516, 120.40999603271`
8. **Try talking to Barry.**  
   `Primary` · `quests/minor_quest/mq010_barry/mq010_barry/03a_try_talking_to_barry`
   - Map pin: ref `#mq010_mp_barry_door`; position `-1393.8206787109, 1301.7896728516, 120.40999603271`

## Heroes

- IGN walkthrough: [Heroes](https://www.ign.com/wikis/cyberpunk-2077/Heroes)
- Vanilla type: `SideQuest`
- Quest hash: `2495848031`
- Quest path: `quests/side_quest/sq018_jackie`
- District: Heywood
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `choice/decision`, `leave/escape area`

### Journal premise

I don't usually give advice, but... fuck it, here goes. Don't make the same mistake I made – say goodbye to the people you love. You know what I mean, right? Jackie Welles was your best choom, and you don't find a lot of straight-up peeps like that in NC. Best thing you can do is remember them. Oh, and one more thing. If anyone asks, I didn't just say all that to you. Got it?

### Objective sequence

1. **Read the message from Mama Welles.**  
   `Optional` · `quests/side_quest/sq018_jackie/00_holocall/01_read_messages`
2. **Read the message from Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/00_holocall/01_read_messages1`
3. **Call Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/00_holocall/02_call_mama_welles`
4. **Collect the package from Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/00_holocall/03_get_package`
5. **Talk to Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/00_holocall/04_talk_with_mama_welles`
6. **Meet Mama Welles at El Coyote Cojo.**  
   `Primary` · `quests/side_quest/sq018_jackie/01_mama_welles/01_visit_el_coyote`
   - Map pin: ref `#sq018_mp_el_coyote_entrance`; position `-1260.3474121094, -984.17456054688, 13.267246246338`
7. **Talk to Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/01_mama_welles/02_talk_with_mama_welles`
8. **Sit.**  
   `Primary` · `quests/side_quest/sq018_jackie/01_mama_welles/02a_sit_down`
   - Map pin: ref `#sq018_mp_sit_down`; position `-1252.9501953125, -991.46014404297, 13.220001220703`
9. **Take the keys to Jackie's garage.**  
   `Primary` · `quests/side_quest/sq018_jackie/01_mama_welles/03_take_keycard`
10. **Go to Jackie's garage.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/01_got_to_jackies_storage`
11. **Open the garage.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/04_open_storage`
12. **Find the key to Jackie's room.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/04a_find_a_key`
13. **Open Jackie's room.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/04b_open_door`
14. **Talk to Misty.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/05_talk_with_misty`
15. **Choose an offering for the ofrenda.**  
   `Primary` · `quests/side_quest/sq018_jackie/02_storage/06_pick_things_for_ofrenda`
16. **Scan and search the garage.**  
   `Optional` · `quests/side_quest/sq018_jackie/02_storage/05_go_through_jackies_stuff`
17. **Talk to Misty.**  
   `Optional` · `quests/side_quest/sq018_jackie/02_storage/05a_optional_talk_misty`
18. **Take part in the ofrenda at El Coyote Cojo.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/01_go_to_el_coyote`
   - Map pin: ref `#sq018_mp_el_coyote_back_entrance`; position `-1236.5842285156, -1003.5142211914, 13.587245941162`
19. **Talk to Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/02_talk_with_mama_welles`
20. **Leave an offering in Jackie's memory.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/03_leave_things_ofrenda`
21. **Take part in the ofrenda.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/03_take_part_in_ceremony`
22. **Sit.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/03a_sit_down`
   - Map pin: ref `#sq018_mp_ofrenda_sit_down`; position `-1244.169921875, -1003.0599975586, 12.869999885559`
23. **Take a drink from Mama Welles.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/03b_drink`
24. **Raise a toast to Jackie.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/03c_make_toast`
25. **Leave the bar.**  
   `Primary` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/07_leave_funeral`
   - Map pin: ref `#sq018_mp_el_coyote_entrance`; position `-1260.3474121094, -984.17456054688, 13.267246246338`
26. **Talk to the Valentinos.**  
   `Optional` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/04_talk_with_valentinos`
27. **Talk to Padre.**  
   `Optional` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/04b_talk_with_padre`
28. **Talk to the bartender.**  
   `Optional` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/04c_talk_with_pepe`
   - Map pin: ref `#sq018_03d_sm_talk_to_barman`; position `-1260.7022705078, -1000.6484375, 12.889941215515`
29. **Talk to Misty.**  
   `Optional` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/05_talk_with_misty`
30. **Talk to Viktor.**  
   `Optional` · `quests/side_quest/sq018_jackie/03_el_coyote_funeral/06_talk_with_victor_vector`

## Holdin' On

- IGN walkthrough: [Holdin On](https://www.ign.com/wikis/cyberpunk-2077/Holdin_On)
- Vanilla type: `SideQuest`
- Quest hash: `1157787686`
- Quest path: `quests/side_quest/sq011_kerry`
- District: Westbrook
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `retrieve/collect item`

### Journal premise

The whole time I was flat on my digital ass in Mikoshi, Kerry was out there forging his glittering solo career. He'd better be real fucking chill after all these years, right? But something tells me deep down, he's still the same. Anyway, come on, guy's gonna shit himself when he sees me.

### Objective sequence

1. **Meet Johnny by the North Oak sign.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/01_get_to_park`
   - Map pin: ref `#sq011_mp_johnny_park`; position `106.39575195313, 827.90631103516, 129.38088989258`
2. **Sit and drink with Kerry.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/01_get_to_park1`
3. **Enter Kerry's property.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/01_get_to_villa`
   - Map pin: ref `#sq011_mp_villa_gate`; position `153.69729614258, 1069.3605957031, 204.30075073242`
4. **Find Kerry in his villa.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/02_look_around_in_villa`
   - Map pin: ref `#sq011_mp_kerry_interior`; position `128.57116699219, 1088.6265869141, 201.86912536621`
5. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/02_talk_to_johnny`
6. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/02_talk_to_johnny1`
7. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/02_talk_to_johnny2`
8. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/02_talk_to_kerry`
9. **Take Kerry's guitar.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/03_pick_kerry_guitar`
10. **Play to lure Kerry out.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/05_play_guitar`
11. **Follow Kerry.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/07_follow_kerry`
12. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/08_talk_to_kerry`
13. **Call Nancy.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/12_talk_to_nancy`
14. **Talk to Nancy.**  
   `Primary` · `quests/side_quest/sq011_kerry/01_hook/12_talk_to_nancy1`

## Human Nature

- IGN walkthrough: [Human Nature](https://www.ign.com/wikis/cyberpunk-2077/Human_Nature)
- Vanilla type: `SideQuest`
- Quest hash: `549818347`
- Quest path: `quests/side_quest/sq025_0_pickup`
- District: Watson
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **When a person dies, the world keeps chugging along without skipping a beat. Eventually, all traces of that person fade into nothing. Long story short, that's why your wheels were towed. Want my opinion? The best way to convince the world you're alive and kicking is to get your wheels back. Hell, maybe it's not the most ambitious goal, but for a minor-league merc like you, at least it's a start.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/00_debug_trigger`
   - Map pin: ref `#sq025_mp_crash_parking`; position `-1349.25, 1271.90625, 29.4990234375`
2. **Go to the parking lot.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/00a_go_parking_lot`
3. **Drive out of the parking garage.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/00b_debug_spawn`
   - Map pin: ref `#sq025_mp_parking_exit`; position `-1371.9395751953, 1253.2814941406, 24.157060623169`
4. **Talk to Johnny Silverhand.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/00c_talk_johnny`
5. **Get out of the damaged car.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/01_leave_car`
6. **Read the message from Delamain.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/02_read_msg`
7. **Keep busy while you wait for the car to be repaired.**  
   `Primary` · `quests/side_quest/sq025_0_pickup/pickup/03_wait`

## I Can See Clearly Now

- IGN walkthrough: [I Can See Clearly Now](https://www.ign.com/wikis/cyberpunk-2077/I_Can_See_Clearly_Now)
- Vanilla type: `MinorQuest`
- Quest hash: `993438947`
- Quest path: `quests/minor_quest/mq037_brendan_dumpster`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `interact/use device`

### Objective sequence

1. **Now THIS is the big job you've been hunting for: Moving a container because it's making a vending machine sad.\n\nWhat're you waiting for? Help the poor bastard!**  
   `Primary` · `quests/minor_quest/mq037_brendan_dumpster/mq037_brendan_dumpster/00_push_dumpster`
2. **Talk to Brendan.**  
   `Primary` · `quests/minor_quest/mq037_brendan_dumpster/mq037_brendan_dumpster/01_talk_brendan`

## I Don't Wanna Hear It

- IGN walkthrough: [I Don't Wanna Hear It](https://www.ign.com/wikis/cyberpunk-2077/I_Don%27t_Wanna_Hear_It)
- Vanilla type: `SideQuest`
- Quest hash: `1718319965`
- Quest path: `quests/side_quest/sq017_01_riot_club`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `deliver/deposit item`, `leave/escape area`

### Journal premise

And the crisis continues! Though Kerry might be barking mad up the wrong tree – those Us Cracks girls are a symptom, not the cause. Could wipe 'em off the face of the earth, and those MSM bastards would still find some other two-bit gonk to sing his song. We're dime-a-dozen whores to them, all of us. Chew up, spit out, rinse and repeat. On the other hand, world's crazy enough that even Eurodyne might be right. You're about to find out.

### Objective sequence

1. **Drop the ladder.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/drop_ladder`
   - Map pin: ref `#sq017_mp_ladder_riot`; position `-1658.1271972656, 1010.7619628906, 29.744079589844`
2. **Find a way into the club.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/enter_club`
3. **Look for a staff ID badge.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/find_badge_locker`
4. **Follow Kerry.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/find_us_cracks`
5. **Find a way backstage.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/find_way_backstage`
6. **Go backstage.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/go_backstage`
   - Map pin: ref `#sq017_mp_riot_elev_terminal`; position `-1627.1318359375, 1005.875793457, 26.350929260254`
7. **Leave the club with Kerry.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/leave_with_kerry`
8. **Meet Kerry at Riot around 7 PM.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/meet_kerry`
   - Map pin: ref `#sq017_mp_wait_kerry_club`; position `-1661.9904785156, 962.7333984375, 24.381004333496`
9. **Sit.**  
   `Optional` · `quests/side_quest/sq017_01_riot_club/nightclub/sit_down_us_cracks`
10. **Answer the phone.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/phone_call`
11. **Return to Kerry.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/return_to_kerry`
12. **Scan the fans and steal two tickets.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/scan_for_tickets`
13. **Talk to Kerry in private.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/talk_kerry_rail`
   - Map pin: ref `#sq017_mp_riot_railing_spot`; position `-1635.9758300781, 1012.3687744141, 29.628969192505`
14. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/talk_kerry_roadie`
15. **Talk to the roadie.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/talk_to_roadie`
16. **Try to get concert tickets.**  
   `Optional` · `quests/side_quest/sq017_01_riot_club/nightclub/buy_tickets`
17. **Talk to Us Cracks.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/talk_us_cracks`
18. **Enter with the tickets.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/tickets`
19. **Wait for Kerry.**  
   `Primary` · `quests/side_quest/sq017_01_riot_club/nightclub/wait_for_kerry`

## I Fought the Law

- IGN walkthrough: [I Fought the Law](https://www.ign.com/wikis/cyberpunk-2077/I_Fought_the_Law)
- Vanilla type: `SideQuest`
- Quest hash: `2923681177`
- Quest path: `quests/side_quest/sq012_lost_girl`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `combat/neutralize`, `stealth/avoid detection`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Talk to Jefferson.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/after_braindance/talk_peralez`
2. **Watch the braindance and look for clues.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/braindance/examine_braindance`
3. **Exit the braindance.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/braindance/exit_braindance`
4. **Listen to the conversation.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/braindance/listen_conversation`
5. **Rewind to the beginning of the conversation.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/braindance/rewind_braindance`
6. **Confront Detective Han.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/confront_yu/confront_yu`
7. **So the mayor snuffs it in a kink club and his successor sweeps the whole thing under the rug...\nIf I were you, I wouldn't call it quits just yet. Keep digging and I guarantee you this goes way deeper – I'm talking sublevels upon sublevels of weird.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/confront_yu/go_with_river`
8. **Meet with River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/confront_yu/meet_river`
   - Map pin: ref `#sq012_mappin_diner_confrontation`; position `-1193.5843505859, -1186.6062011719, 33.764274597168`
9. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/confront_yu/talk_to_river`
10. **Use the intercom.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/03_use_intercom`
11. **Take the elevator to the penthouse.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/04_elevator_to_penthouse`
   - Map pin: ref `#sq012_mappin_elevator`; position `-72.300979614258, -114.28085327148, 8.7612762451172`
12. **Talk to Elizabeth and Jefferson.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/05_meet_with_the_peralezes`
13. **Sit.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/05_sit`
   - Map pin: ref `#sq012_mappin_sit_apartment`; position `-94.967269897461, -123.13883972168, 111.61729431152`
14. **Leave the building.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/07_leave_apartment`
   - Map pin: ref `#sq012_mappin_elevator_top`; position `-72.305557250977, -114.07205200195, 112.41729736328`
   - Map pin: ref `#sq012_mappin_peralez_apartment_outer_door`; position `-65.244079589844, -98.193336486816, 8.7160568237305`
15. **Call Elizabeth Peralez.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/call_elizabeth`
16. **Go to the Peralezes' apartment.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/final_meeting/go_to_peralez`
   - Map pin: ref `#sq012_mappin_peralez_apartment_outer_door`; position `-65.244079589844, -98.193336486816, 8.7160568237305`
17. **Deal with the Tyger Claws.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/deal_with_tcs`
18. **Ask the vendors about Christine Markov.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/find_christine`
19. **Follow River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/follow_river`
20. **Get in River's car.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/get_in_car`
21. **Question Christine Markov.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/question_vendor`
22. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/talk_to_river`
23. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/talk_to_river_before`
24. **Go to the Japantown market.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/travel_to_market`
   - Map pin: ref `#sq012_mappin_market`; position `-702.01806640625, 947.16760253906, 13.470000267029`
25. **Ride with River to the Japantown market.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/travel_with_river_to_market`
26. **Wait for River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/market_scenes/wait_for_river`
   - Map pin: ref `#sq012_mappin_market_wait_for_river`; position `-688.89184570313, 932.27062988281, 12.189999580383`
27. **Call Elizabeth back.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_peralez/call_elizabeth`
28. **Get in the car.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_peralez/get_in`
   - Map pin: ref `#sq012_mp_intro_limo_seat`; position `-1822.7172851563, -176.34533691406, 8.5970020294189`
29. **Look, if a job starts like a classic whodunit – some femme fatale calls you up, refuses to give detes and just calls a meet – one of three things is going down: you're dreaming, you're scrollin' a shit BD or someone's hazing you good. Think you can scratch the first two.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_peralez/go_to_meeting`
   - Map pin: ref `#sq012_mappin_meeting_location`; position `-1825.8392333984, -175.92010498047, 9.2200031280518`
30. **Listen to the offer.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_peralez/listen_to_peralez`
31. **Wait for your contact.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_peralez/wait_for_peralez`
   - Map pin: ref `#sq012_mappin_wait_for_peralez`; position `-1835.1401367188, -180.40960693359, 8.6800012588501`
32. **First rule of "top secret" jobs – don't take 'em.\nFirst rule of working with politicians – don't do it.\nFirst rule of contacting the police – avoid it.\nAnd what do you do? Break 'em all at once. Gotta say, V, I'm a little impressed.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_river/call_river`
33. **Get in River's car.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_river/get_in_car`
   - Map pin: ref `#sq012_mp_rivers_car_diner`; position `-1206.1011962891, -1198.1116943359, 33.475273132324`
34. **Meet with Detective Ward.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_river/go_to_river`
   - Map pin: ref `#sq012_mappin_diner`; position `-1216.0766601563, -1175.1060791016, 34.9372215271`
35. **You think "good cops" really exist in this city? Don't crack me up. Gonk like this is either made-up, a collective hallucination or an urban legend. Sooner or later he'll do what badges do best – plant a bullet between your eyes.\nYou really want to team up and run an investigation with some figment of the imagination? Am I not enough for you?**  
   `Primary` · `quests/side_quest/sq012_lost_girl/meet_river/ride_with_river`
36. **Find a way into the Red Queen's Race.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/access_rqr`
   - Map pin: ref `#sq012_mappin_rqr_access`; position `652.12377929688, -467.38012695313, 10.964190483093`
37. **Call the elevator.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/call_elevator`
   - Map pin: ref `#sq012_mappin_use_elevator`; position `641.76629638672, -470.23129272461, 8.3566675186157`
38. **Check the computer.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/check_computer`
39. **Defeat the Animals.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/defeat_all`
40. **Enter the Red Queen's Race.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/enter_rqr`
   - Map pin: ref `#sq012_mappin_enter_RQR`; position `640.15924072266, -469.44778442383, 6.7241654396057`
   - Map pin: ref `#sq012_mappin_lower_level`; position `647.99462890625, -468.07998657227, -3.1225185394287`
41. **Enter the warehouse.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/enter_warehouse`
   - Map pin: ref `#sq012_mappin_warehouse_point`; position `658.26519775391, -465.69445800781, 11.557503700256`
42. **Interrogate the Animal boss.**  
   `Optional` · `quests/side_quest/sq012_lost_girl/red_queen_race/question_boss`
43. **Go to the address given by the informant.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/go_rqr`
   - Map pin: ref `#sq012_mappin_river_rendezvous`; position `704.07440185547, -589.93640136719, 10.969999313354`
44. **Look for the office.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/look_office`
45. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/meet_river`
46. **Open the door.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/open_door`
47. **Find a way into the club.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/scan_for_entrance`
48. **Incapacitate the Animal boss.**  
   `Optional` · `quests/side_quest/sq012_lost_girl/red_queen_race/incapacitate_boss`
49. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/talk_to_river`
50. **Go with River to the Red Queen's Race.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/travel_to_rqr_with_river`
51. **Wait for River to get in the elevator.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/wait_for_elevator`
52. **Talk to the Alpha Animal.**  
   `Optional` · `quests/side_quest/sq012_lost_girl/red_queen_race/talk_6_street`
53. **Wait for River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/wait_for_river`
   - Map pin: ref `#sq012_mappin_wait_river_RQR`; position `710.23962402344, -608.05035400391, 10.409999847412`
54. **Watch the security recording.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/red_queen_race/watch_video`
55. **Ask the informant about the Red Queen's Race.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/ask_about_igor`
56. **Chase the informant.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/chase_clerk`
57. **Enter the store.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/enter_shop`
   - Map pin: ref `#sq012_mappin_sex_shop`; position `-863.58264160156, 130.26937866211, 8.6115589141846`
58. **Get in River's car.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/get_in_river_car`
59. **Interrogate the informant.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/interrogate_clerk`
60. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/talk_to_river`
61. **Talk to River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/talk_to_river_02`
62. **Meet River near his informant.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/travel_to_shop`
   - Map pin: ref `#sq012_mappin_sex_shop`; position `-863.58264160156, 130.26937866211, 8.6115589141846`
63. **Go with River to meet with his informant.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/travel_with_river`
64. **Wait for River.**  
   `Primary` · `quests/side_quest/sq012_lost_girl/sex_shop/wait_for_river`
   - Map pin: ref `#sq012_mappin_wait_for_river_at_sex_shop`; position `-868.40606689453, 117.91520690918, 8.2400007247925`

## I Really Want to Stay at Your House

- IGN walkthrough: [I Really Want to Stay at Your House](https://www.ign.com/wikis/cyberpunk-2077/I_Really_Want_to_Stay_at_Your_House)
- Vanilla type: `MinorQuest`
- Quest hash: `3675012209`
- Quest path: `quests/minor_quest/mq055_romance_apartment`
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `wait/time gate`, `deliver/deposit item`, `leave/escape area`

### Journal premise

Gonna have a little date, huh? Knock yourself out. And don't worry – I'll close my eyes and plug my ears.

### Objective sequence

1. **Read and reply to the message from Judy.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/judy_read`
2. **Read and reply to the message from Kerry.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/kerry_read`
3. **Read and reply to the message from Panam.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/panam_read`
4. **Read and reply to the message from River.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/river_read`
5. **Wait for your partner to message you.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/romance_wait`
6. **Wait for your partner to message you.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/00_text/romance_wait_male`
7. **Meet Judy at your megabuilding apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/01_megabuilding/judy_megabuilding`
   - Map pin: ref `#mq055_mp_megabuilding_apartment`; position `-1382.8798828125, 1270.6202392578, 123.05999755859`
8. **Meet Kerry at your megabuilding apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/01_megabuilding/kerry_megabuilding`
   - Map pin: ref `#mq055_mp_megabuilding_apartment`; position `-1382.8798828125, 1270.6202392578, 123.05999755859`
9. **Meet Panam at your megabuilding apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/01_megabuilding/panam_megabuilding`
   - Map pin: ref `#mq055_mp_megabuilding_apartment`; position `-1382.8798828125, 1270.6202392578, 123.05999755859`
10. **Meet River at your megabuilding apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/01_megabuilding/river_megabuilding`
   - Map pin: ref `#mq055_mp_megabuilding_apartment`; position `-1382.8798828125, 1270.6202392578, 123.05999755859`
11. **Meet Judy at your Northside apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/02_northside/judy_northside`
   - Map pin: ref `#mq055_mp_northside_apartment`; position `-1505.3001708984, 2230.0710449219, 22.199998855591`
12. **Meet Kerry at your Northside apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/02_northside/kerry_northside`
   - Map pin: ref `#mq055_mp_northside_apartment`; position `-1505.3001708984, 2230.0710449219, 22.199998855591`
13. **Meet Panam at your Northside apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/02_northside/panam_northside`
   - Map pin: ref `#mq055_mp_northside_apartment`; position `-1505.3001708984, 2230.0710449219, 22.199998855591`
14. **Meet River at your Northside apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/02_northside/river_northside`
   - Map pin: ref `#mq055_mp_northside_apartment`; position `-1505.3001708984, 2230.0710449219, 22.199998855591`
15. **Meet Judy at your Japantown apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/03_japantown/judy_japantown`
   - Map pin: ref `#mq055_mp_japantown_apartment`; position `-787.31970214844, 976.09973144531, 28.209999084473`
16. **Meet Kerry at your Japantown apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/03_japantown/kerry_japantown`
   - Map pin: ref `#mq055_mp_japantown_apartment`; position `-787.31970214844, 976.09973144531, 28.209999084473`
17. **Meet Panam at your Japantown apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/03_japantown/panam_japantown`
   - Map pin: ref `#mq055_mp_japantown_apartment`; position `-787.31970214844, 976.09973144531, 28.209999084473`
18. **Meet River at your Japantown apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/03_japantown/river_japantown`
   - Map pin: ref `#mq055_mp_japantown_apartment`; position `-787.31970214844, 976.09973144531, 28.209999084473`
19. **Meet Judy at your Glen apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/04_heywood/judy_heywood`
   - Map pin: ref `#mq055_mp_heywood_apartment`; position `-1519.8902587891, -976.55999755859, 86.75`
20. **Meet Kerry at your Glen apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/04_heywood/kerry_heywood`
   - Map pin: ref `#mq055_mp_heywood_apartment`; position `-1519.8902587891, -976.55999755859, 86.75`
21. **Meet Panam at your Glen apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/04_heywood/panam_heywood`
   - Map pin: ref `#mq055_mp_heywood_apartment`; position `-1519.8902587891, -976.55999755859, 86.75`
22. **Meet River at your Glen apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/04_heywood/river_heywood`
   - Map pin: ref `#mq055_mp_heywood_apartment`; position `-1519.8902587891, -976.55999755859, 86.75`
23. **Meet Judy at your Corpo Plaza apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/05_downtown/judy_downtown`
   - Map pin: ref `#mq055_mp_downtown_apartment`; position `-1601.0899658203, 356.79000854492, 48.619998931885`
24. **Meet Kerry at your Corpo Plaza apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/05_downtown/kerry_downtown`
   - Map pin: ref `#mq055_mp_downtown_apartment`; position `-1601.0899658203, 356.79000854492, 48.619998931885`
25. **Meet Panam at your Corpo Plaza apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/05_downtown/panam_downtown`
   - Map pin: ref `#mq055_mp_downtown_apartment`; position `-1601.0899658203, 356.79000854492, 48.619998931885`
26. **Meet River at your Corpo Plaza apartment.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/05_downtown/river_downtown`
   - Map pin: ref `#mq055_mp_downtown_apartment`; position `-1601.0899658203, 356.79000854492, 48.619998931885`
27. **Hang out with Judy.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/judy_hang`
28. **Read and reply to the message from Judy.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/judy_text`
29. **Wait for Judy.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/judy_wait`
   - Map pin: ref `#mq055_mp_downtown_wait`; position `-1601.8098144531, 357.77001953125, 49.060001373291`
   - Map pin: ref `#mq055_mp_heywood_wait`; position `-1519.1103515625, -975.11999511719, 87.180000305176`
   - Map pin: ref `#mq055_mp_japantown_wait`; position `-785.63989257813, 975.88989257813, 28.910001754761`
   - Map pin: ref `#mq055_mp_megabuilding_wait`; position `-1380.6398925781, 1270.0802001953, 123.47999572754`
   - Map pin: ref `#mq055_mp_northside_wait`; position `-1506.240234375, 2228.580078125, 22.609996795654`
30. **Hang out with Kerry.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/kerry_hang`
31. **Read and reply to the message from Kerry.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/kerry_text`
32. **Wait for Kerry.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/kerry_wait`
   - Map pin: ref `#mq055_mp_downtown_wait`; position `-1601.8098144531, 357.77001953125, 49.060001373291`
   - Map pin: ref `#mq055_mp_heywood_wait`; position `-1519.1103515625, -975.11999511719, 87.180000305176`
   - Map pin: ref `#mq055_mp_japantown_wait`; position `-785.63989257813, 975.88989257813, 28.910001754761`
   - Map pin: ref `#mq055_mp_megabuilding_wait`; position `-1380.6398925781, 1270.0802001953, 123.47999572754`
   - Map pin: ref `#mq055_mp_northside_wait`; position `-1506.240234375, 2228.580078125, 22.609996795654`
33. **Leave the area to end the date.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/leave_end`
34. **Hang out with Panam.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/panam_hang`
35. **Read and reply to the message from Panam.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/panam_text`
36. **Wait for Panam.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/panam_wait`
   - Map pin: ref `#mq055_mp_downtown_wait`; position `-1601.8098144531, 357.77001953125, 49.060001373291`
   - Map pin: ref `#mq055_mp_heywood_wait`; position `-1519.1103515625, -975.11999511719, 87.180000305176`
   - Map pin: ref `#mq055_mp_japantown_wait`; position `-785.63989257813, 975.88989257813, 28.910001754761`
   - Map pin: ref `#mq055_mp_megabuilding_wait`; position `-1380.6398925781, 1270.0802001953, 123.47999572754`
   - Map pin: ref `#mq055_mp_northside_wait`; position `-1506.240234375, 2228.580078125, 22.609996795654`
37. **Hang out with River.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/river_hang`
38. **Read and reply to the message from River.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/river_text`
39. **Wait for River.**  
   `Primary` · `quests/minor_quest/mq055_romance_apartment/06_date/river_wait`
   - Map pin: ref `#mq055_mp_downtown_wait`; position `-1601.8098144531, 357.77001953125, 49.060001373291`
   - Map pin: ref `#mq055_mp_heywood_wait`; position `-1519.1103515625, -975.11999511719, 87.180000305176`
   - Map pin: ref `#mq055_mp_japantown_wait`; position `-785.63989257813, 975.88989257813, 28.910001754761`
   - Map pin: ref `#mq055_mp_megabuilding_wait`; position `-1380.6398925781, 1270.0802001953, 123.47999572754`
   - Map pin: ref `#mq055_mp_northside_wait`; position `-1506.240234375, 2228.580078125, 22.609996795654`

## I'm in Love with My Car

- IGN walkthrough: [I'm in Love With My Car - Ken Block Car Location](https://www.ign.com/wikis/cyberpunk-2077/Ken_Block_Car_Location)
- Vanilla type: `MinorQuest`
- Quest hash: `2765329288`
- Quest path: `quests/minor_quest/mq050_ken_block_tribute`
- District: Watson
- Level: 60
- Candidate building blocks: `search/investigate`, `vehicle sequence`

### Journal premise

Ain't you a little old to be dreamin' about a pro racing career? Still… be a damn shame to let a preem set of wheels like this go to waste. Just let the mayor know if you wanna shut down any city streets.Or don't – fuck that guy.

### Objective sequence

1. **Get in the car.**  
   `Primary` · `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car`
   - Map pin: ref `#mq050_spwn_vehicle`; position `-728.96978759766, 3147.2395019531, 7.4700002670288`
2. **Search the warehouse.**  
   `Primary` · `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate`
   - Map pin: ref `#mq050_tr_investigation`; position `-728.19006347656, 3139.25, 7.1799998283386`

## Imagine

- IGN walkthrough: [Imagine](https://www.ign.com/wikis/cyberpunk-2077/Imagine)
- Vanilla type: `MinorQuest`
- Quest hash: `657207495`
- Quest path: `quests/minor_quest/mq014_zen`
- District: City Center
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **In Night City, there's no shortage of gonks, hustlers and just plain assholes. And if you stopped to talk to each one, you might just cross the last of your wires, too. But if that's what your gut's tellin' you to do, by all means. Just watch for sticky fingers.**  
   `Primary` · `quests/minor_quest/mq014_zen/01_hook/01_approach_master`
2. **Talk to the stranger.**  
   `Primary` · `quests/minor_quest/mq014_zen/01_hook/02_talk_sranger`
3. **Return to strange monk.**  
   `Primary` · `quests/minor_quest/mq014_zen/01_hook/03_come_back`
4. **Meditate with Zen master.**  
   `Primary` · `quests/minor_quest/mq014_zen/01_hook/04_earth`

## Killing In The Name

- IGN walkthrough: [Killing in the Name](https://www.ign.com/wikis/cyberpunk-2077/Killing_in_the_Name)
- Vanilla type: `MinorQuest`
- Quest hash: `391781538`
- Quest path: `quests/minor_quest/mq018_writer`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `search/investigate`, `interact/use device`, `hack/breach/download`, `deliver/deposit item`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Call Nancy (Bes Isis) and ask about Swedenborg.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/02b_call_nancy`
2. **Go to Nancy's coordinates.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/03_find_place`
   - Map pin: ref `#mq018_tr_brooklyn`; position `-28.33251953125, -1739.1123046875, -12.201286315918`
3. **Scan the area for clues.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/04_find_relay`
   - Map pin: ref `#mq018_tr_brooklyn`; position `-28.33251953125, -1739.1123046875, -12.201286315918`
4. **Hack the router.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/05_access_relay`
5. **Read the message you received.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/05a_read_brooklyn`
6. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/05b_call_nancy`
7. **Go to the signal's source.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/06_find_relay_powerplant`
8. **Scan the area for clues.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/07_find_relay_powerplant`
9. **Hack the router.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/08_access_relay_powerplant`
10. **Read the message you received.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/08a_read_solar`
11. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/08b_johnny_protein`
12. **Go to the signal's source.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/09_find_place_protein`
   - Map pin: ref `#mq018_tr_protein`; position `-3315.44140625, -4884.669921875, 67.433898925781`
   - Map pin: ref `#mq018_mp_protein_gate`; position `-2913.5576171875, -5193.5805664063, 72.056625366211`
13. **Scan the area for clues.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/09_find_relay_protein`
   - Map pin: ref `#mq018_tr_protein`; position `-3315.44140625, -4884.669921875, 67.433898925781`
14. **Hack the router.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/10_access_relay_protein`
15. **Go to the signal's source.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/11_find_place_fortuneteller`
   - Map pin: ref `#mq018_tr_johnny_amusment_intro`; position `-2729.5500488281, -2433.5576171875, 18.029998779297`
16. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/11_johnny_protein`
17. **Read the message you received.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/11a_read_protein`
18. **Scan the area for clues.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/12_find_fortuneteller`
   - Map pin: ref `#mq018_tr_amusement`; position `-2652.2265625, -2430.8303222656, 13.340584754944`
19. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/12b_talk_johnny`
20. **Hack the router.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/13_access_fortuneteller`
21. **Search the area.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/13b_interact_fortuneteller`
   - Map pin: ref `#mq018_tr_amusement`; position `-2652.2265625, -2430.8303222656, 13.340584754944`
22. **Scan the fortuneteller bot to see if it's been manipulated.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/13c_scan_fortuneteller`
   - Map pin: ref `#mq018_02_sm_fortuneteller_screen`; position `-2663.7099609375, -2425.7797851563, 19.749998092651`
23. **Approach the fortuneteller bot.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/13d_really_interact`
   - Map pin: ref `#mq018_02_sm_fortuneteller_screen`; position `-2663.7099609375, -2425.7797851563, 19.749998092651`
24. **Decide what to do with the fortuneteller bot.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/14_decide_fate_swedenborg`
   - Map pin: ref `#mq018_02_sm_fortuneteller_screen`; position `-2663.7099609375, -2425.7797851563, 19.749998092651`
25. **Read the message you received.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/14a_read_fortuneteller`
26. **Listen to the fortuneteller bot.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/14b_listen_fortuneteller`
   - Map pin: ref `#mq018_02_sm_fortuneteller_screen`; position `-2663.7099609375, -2425.7797851563, 19.749998092651`
27. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/14c_talk_johnny`
28. **Call Nancy.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/15_call_nancy`
29. **Connect to the fortuneteller bot to modify the algorithm.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/15a_manipulate`
30. **Tell Johnny you'll leave the fortuneteller bot alone.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/15b_johnny_stop`
31. **Pay to hear your fortune.**  
   `Optional` · `quests/minor_quest/mq018_writer/mq018_writer/14d_pay_fortuneteller`
   - Map pin: ref `#mq018_02_sm_fortuneteller_screen`; position `-2663.7099609375, -2425.7797851563, 19.749998092651`
32. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/15c_talk_jonny`
33. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/16a_talk_johnny`
34. **I'm curious about this Swedenborg-Riviera. To write that kinda nonsense, you've gotta have a good head. "Humanity is nothing but a pyramid scheme hidden behind a facade of tears…" Well, fuck me. What's this guy on? And where can I get some?**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/access_website`
   - Map pin: ref `#q101_mp_v_room_computer`; position `-1387.0349121094, 1273.5327148438, 124.30874633789`
35. **Call Nancy about Swedenborg.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/blocked_02_again`
36. **Call Bes Isis about Swedenborg.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/call_number`
37. **Complete other jobs until Bes Isis, aka Nancy, is available to call.**  
   `Primary` · `quests/minor_quest/mq018_writer/mq018_writer/wait`

## Machine Gun

- IGN walkthrough: [Machine Gun](https://www.ign.com/wikis/cyberpunk-2077/Machine_Gun)
- Vanilla type: `MinorQuest`
- Quest hash: `2827590896`
- Quest path: `quests/minor_quest/mq007_smartgun`
- District: Heywood
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `search/investigate`

### Objective sequence

1. **So, what, you're giving Skippy to Regina? Too bad. Not every day find a gun you can share your deepest and darkest with. And have it reciprocate, that is. On the other hand, I get you… Already got enough voices in your head, amirite?**  
   `Primary` · `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy`
   - Map pin: ref `#mq007_mp_mq036_locker`; position `-478.13732910156, 406.95190429688, 133.35372924805`
   - Map pin: ref `#mq007_mp_q105_locker`; position `-634.328125, 807.21856689453, 129.74368286133`
   - Map pin: ref `#mq007_mp_regina_jones_elevator_panel`; position `-1154.7015380859, 1580.8796386719, 24.984817504883`
   - Map pin: ref `#mq007_mp_regina_jones_intercom`; position `-1159.9948730469, 1584.6628417969, 24.706268310547`
   - Map pin: ref `#mq007_mp_regina_jones_office`; position `-1160.5059814453, 1582.9370117188, 24.366008758545`
   - Map pin: ref `#mq007_mp_skippy_in_stash`; position `-1380.8782958984, 1262.5563964844, 124.83888244629`
2. **Set Skippy down.**  
   `Primary` · `quests/minor_quest/mq007_smartgun/mq007_smartgun/02_put_skippy_down`
   - Map pin: ref `#mq007_mp_giving_skippy`; position `-1141.9534912109, 1569.2800292969, 72.879959106445`
3. **Talk to Regina.**  
   `Primary` · `quests/minor_quest/mq007_smartgun/mq007_smartgun/03_talk_to_regina`

## Off the Leash

- IGN walkthrough: [Off The Leash](https://www.ign.com/wikis/cyberpunk-2077/Off_The_Leash)
- Vanilla type: `SideQuest`
- Quest hash: `3513022215`
- Quest path: `quests/side_quest/sq017_02_lounge`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`

### Journal premise

You know, Kerry's whole escapade makes me think. People do change. He did. I mean – he made it to a crossroads, and now I can see his rockerboy heart pushing him down the right path. The problem, you ask? Kerry might've changed, but the city hasn't. And I think he knows it. Hell, so do you.

### Objective sequence

1. **Talk to the bouncer.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/pachinko/countersign`
2. **Go to the given address.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/pachinko/go_pachinko`
3. **Look for Kerry.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry`
   - Map pin: ref `#sq017_mp_kerry_stage_lounge`; position `-331.3362121582, 223.64179992676, 190.08319091797`
4. **Answer the phone.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/pachinko/phone_call`
5. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/party/enjoy`
6. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/party/find_kerry`
   - Map pin: ref `#sq017_mp_kerry_stage_lounge`; position `-331.3362121582, 223.64179992676, 190.08319091797`
7. **Follow Kerry.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/party/follow_kerry`
8. **Wait for Kerry.**  
   `Primary` · `quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available`
   - Map pin: ref `#sq017_mp_kerry_stage_lounge`; position `-331.3362121582, 223.64179992676, 190.08319091797`

## Only Pain

- IGN walkthrough: [Only Pain](https://www.ign.com/wikis/cyberpunk-2077/Only_Pain)
- Vanilla type: `MinorQuest`
- Quest hash: `1268818328`
- Quest path: `quests/minor_quest/mq005_alley`
- District: Heywood
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **"To serve and protect…" Funny, would've thought "To extort and torture" might fit better. Not sure what this guy's beef is with badges, but if you don't step in, they'll be scrapin' him off the sidewalk. Once they smear him there first, of course. But I dunno... maybe it's for the best? After all, no one's in Night City's dyin' an innocent soul.**  
   `Primary` · `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops`
2. **Wake the corpo.**  
   `Primary` · `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo`
3. **Talk to the corpo.**  
   `Primary` · `quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo`

## Paid in Full

- IGN walkthrough: [Paid in Full](https://www.ign.com/wikis/cyberpunk-2077/Paid_in_Full)
- Vanilla type: `MinorQuest`
- Quest hash: `3692983722`
- Quest path: `quests/minor_quest/mq045_victor_debt`
- District: Watson
- Level: 60
- Candidate building blocks: `objective sequence`

### Journal premise

I don't know many rippers who'd install Kiroshi optics on credit and faith. In fact, I only know one – Viktor.  Maybe once you're on top you don't forget about the old guy, yeah? Pay the good doc his 21 thou.

### Objective sequence

1. **Pay off your debt to Viktor – 21000 €$**  
   `Primary` · `quests/minor_quest/mq045_victor_debt/mq045_debt/mq045_pay_off_victor`
   - Map pin: ref `#ws_victor_vector_default`; position `-1542.5921630859, 1230.2431640625, 11.519449234009`

## Pisces

- IGN walkthrough: [Pisces](https://www.ign.com/wikis/cyberpunk-2077/Pisces)
- Vanilla type: `SideQuest`
- Quest hash: `997261986`
- Quest path: `quests/side_quest/sq026_04_hiromi`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

What's worse than a corpo? A wannabe corpo.\n\nYou know what? I'm not even surprised you let yourself get talked into this little uprising. Hey, back in my day I would've bum rushed the riot shields in the name of joytoys' freedom or whatever... But this Maiko chick? I've got a bad feeling about her.

### Objective sequence

1. **What's worse than a corpo? A wannabe corpo.\n\nYou know what? I'm not even surprised you let yourself get talked into this little uprising. Hey, back in my day I would've bum rushed the riot shields in the name of joytoys' freedom or whatever... But this Maiko chick? I've got a bad feeling about her.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/00_holocall/holocall_wait`
2. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/00_holocall/talk_judy`
3. **Get to the roof.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/access_roof`
4. **Defeat the Tyger Claws.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/clear_maintenance`
5. **Go into the freight elevator.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/enter_elevator`
6. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/follow_judy`
7. **Go to Megabuilding H8 in the afternoon.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/go_megabuilding`
8. **Meet with Judy and the dolls.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/meet_judy`
9. **Ride the elevator to the maintenance level.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/take_elevator`
10. **Talk to the group.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/talk_group`
11. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/talk_judy`
12. **Wait until the afternoon.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/01_to_penthouse/wait_afternoon`
13. **Defeat Maiko.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/defeat_maiko`
14. **Defeat the Tyger Claws guards.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/defeat_security`
15. **Defeat Tyger Claw bosses.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/defeat_tc`
16. **Find a way into Hiromi's penthouse.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/find_entry`
17. **Talk to the Tyger Claw bosses.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/hiromi`
18. **Join the meeting.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/join_meeting`
19. **Leave the apartment.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/leave`
20. **Get into Hiromi's office.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/office`
21. **Sit.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/sit_down`
22. **Ride the elevator to ground floor.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/take_elevator`
23. **Talk to Maiko.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/02_penthouse/talk_maiko`
24. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/03_end/talk_johnny`
25. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_04_hiromi/03_end/talk_judy`

## Poem Of The Atoms

- IGN walkthrough: [Poem of the Atoms](https://www.ign.com/wikis/cyberpunk-2077/Poem_of_the_Atoms)
- Vanilla type: `MinorQuest`
- Quest hash: `252425116`
- Quest path: `quests/minor_quest/mq014_03_third`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `interact/use device`

### Objective sequence

1. **You really enjoy this meditation thing? Calms your nerves, does it? 'Cause it somehow reminds me of is those black-tie musicians they stick next to the towels and mouthwash in monochromer joints so you can get taste of culture after you let out a shit. But hey, to each their own.**  
   `Primary` · `quests/minor_quest/mq014_03_third/03_third/01_approach_master`
2. **Talk to the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_03_third/03_third/02_talk_sranger`
3. **Return to the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_03_third/03_third/03_come_back`
4. **Meditate with the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_03_third/03_third/04_earth`

## Psycho Killer

- IGN walkthrough: [Psycho Killer](https://www.ign.com/wikis/cyberpunk-2077/Psycho_Killer)
- Vanilla type: `MinorQuest`
- Quest hash: `2681247412`
- Quest path: `quests/minor_quest/mq043_cyberpsychos`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **Ever heard of a fixer by the name of Regina Jones? Not exactly the same league as Dex, but she must've heard about you since she wants to turn you into a one-man army in the fight against cyberpsychosis. Understandable, seeing as most of our heroic badges seem to vanish from the scene at the mention of "cyberpsycho."\n\nDo not fuck this up – one happy fixer will make three others interested in your services.\n\nI still don't get why Regina wants them alive, but I guess the higher you go, the weirder the contracts get. That's the Afterlife for you.**  
   `Primary` · `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina`
2. **Wait for update from Regina about the Cyberpsycho Sighting.**  
   `Primary` · `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_a_wait_regina`
3. **Meet with Regina.**  
   `Primary` · `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina`
   - Map pin: ref `#reggie_dd_mappin_marker`; position `-1143.08984375, 1568.9799804688, 71.709999084473`
4. **Collect your reward.**  
   `Primary` · `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/03_take_reward`

## Pyramid Song

- IGN walkthrough: [Pyramid Song](https://www.ign.com/wikis/cyberpunk-2077/Pyramid_Song)
- Vanilla type: `SideQuest`
- Quest hash: `1916384977`
- Quest path: `quests/side_quest/sq030_judy_romance`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`

### Journal premise

Everyone knows you can't just count on yourself in this goddamn city. You always gotta have a few chooms who owe you a favor. And a few you've got dirt on too. But when you've got the kind of choom who starts asking you for weirder and weirder shit? That's when problems start.

### Objective sequence

1. **Call Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/call_judy`
2. **Go to the lake's edge with Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/follow_judy`
3. **Connect to the terminal.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/get_up`
   - Map pin: ref `#sq030_mp_scroll`; position `1113.8051757813, -3462.5549316406, 181.5479888916`
4. **Dive into the water.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/into_water`
5. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/judy`
6. **Meet Judy in the early evening.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/location`
7. **Take the wetsuit.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/loot_gear`
8. **Meet with Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/meetup`
9. **Wait for Judy to get ready.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/preparations`
10. **Sit.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/sit_down`
11. **Put on the wetsuit.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/suit_up`
12. **Wait for Judy to calibrate your gear.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/wait_judy`
13. **Wait for Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/dam/wait_start`
14. **Check on Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/check_judy`
15. **Enter the cottage.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/enter_hut`
16. **Find Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/find_judy`
17. **Go to the cottage.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/follow_judy`
18. **Start the generator.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/generator`
19. **Get up.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/get_up`
20. **Sit beside Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/sit_morning`
21. **Sit on the water's edge.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/sit_pier`
22. **Go to bed.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/sleep`
23. **Stand.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/stand_up`
24. **Take your clothes.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/stuff`
25. **Grab your clothes.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/stuff1`
26. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/talk`
27. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/talk1`
28. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/hut/talk_johnny`
29. **Turn on the braindance recorder.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/bd_start`
30. **Search for clues near the gas station.**  
   `Optional` · `quests/side_quest/sq030_judy_romance/lake/exploration_church`
31. **Search for clues near the diner and Judy's house.**  
   `Optional` · `quests/side_quest/sq030_judy_romance/lake/exploration_diner`
32. **Scan the area around the gas station.**  
   `Optional` · `quests/side_quest/sq030_judy_romance/lake/explore`
33. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/exploration`
34. **Scan the area around the diner and Judy's house.**  
   `Optional` · `quests/side_quest/sq030_judy_romance/lake/explore_diner_house`
35. **Look for a path into the church.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/explore_church_entrance`
36. **Face Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/face_judy`
37. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/follow`
38. **Follow Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/follow2`
39. **Go back.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/get_back`
40. **Stand in position.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/position`
41. **Guess the song's name.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/song`
42. **Circle around Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/swim_circle`
43. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/talk_judy`
44. **Calibrate your gear.**  
   `Primary` · `quests/side_quest/sq030_judy_romance/lake/test`

## Queen of the Highway

- IGN walkthrough: [Queen of the Highway](https://www.ign.com/wikis/cyberpunk-2077/Queen_of_the_Highway)
- Vanilla type: `SideQuest`
- Quest hash: `1191436512`
- Quest path: `quests/side_quest/sq027_02_raffen_shiv_attack`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `follow/escort`, `wait/time gate`, `vehicle sequence`

### Objective sequence

1. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/000_talk_to_panam_call`
2. **Once you finally hit it big, always turns out you fucked something else up – Night City's golden rule. Panam got her Basilisk all right, but Saul's sure to toss her out before she even gets a chance to enjoy it. If you really like this girl, now's a good time to have her back.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/00_talk_to_panam`
3. **Call Panam back.**  
   `Optional` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/000_call_panam_back`
4. **Once you finally hit it big, always turns out you fucked something else up – Night City's golden rule. Panam got her Basilisk all right, but Saul's sure to toss her out before she even gets a chance to enjoy it. If you really like this girl, now's a good time to have her back.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/01_wait_for_construction`
5. **Meet with Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/02_return_to_panam`
6. **Talk to Panam and the veterans.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/03_talk_to_panam`
7. **Get in the Basilisk.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/01_camp/04_board_basilisk`
8. **Follow Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_mobile/01_follow_panam`
9. **Talk to nomads.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_mobile/02_talk_to_nomads`
10. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_mobile/03_talk_to_panam`
11. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/00_talk_panam`
12. **Get the Basilisk in position.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/01_move_panzer`
   - Map pin: ref `#sq027_mp_drive_basilisk_001`; position `3449.1752929688, -755.40356445313, 115.85208129883`
13. **Swerve to the left.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/02_test_strafing_left`
14. **Swerve to the right.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/02_test_strafing_right`
15. **Drive past the wind turbines.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/03_drive_for_panam`
   - Map pin: ref `#sq027_mp_course_001`; position `3528.6892089844, -704.07067871094, 115.15544128418`
   - Map pin: ref `#sq027_mp_course_001_l`; position `3548.1867675781, -662.29083251953, 117.4690322876`
   - Map pin: ref `#sq027_mp_course_001_r`; position `3570.03515625, -696.716796875, 116.22807312012`
   - Map pin: ref `#sq027_mp_course_002`; position `3694.2719726563, -591.24261474609, 126.37493896484`
   - Map pin: ref `#sq027_mp_course_002_l`; position `3719.6291503906, -543.1796875, 127.84887695313`
   - Map pin: ref `#sq027_mp_course_002_r`; position `3739.9340820313, -579.88842773438, 132.12493896484`
   - Map pin: ref `#sq027_mp_course_003`; position `3873.2421875, -486.40673828125, 148.20179748535`
   - Map pin: ref `#sq027_mp_course_003_l`; position `3885.560546875, -455.92904663086, 147.54739379883`
   - Map pin: ref `#sq027_mp_course_003_r`; position `3905.7153320313, -481.65899658203, 151.14483642578`
16. **Shoot at the targets.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/04_shoot_targets`
17. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/05_talk_panam_again`
18. **Get the Basilisk in position.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/06_drive_panzer_to_shooting`
   - Map pin: ref `#sq027_mp_drive_basilisk_shooting`; position `3963.0053710938, -448.63952636719, 154.42086791992`
19. **All right, looks like the fun's over. Your little joyrides come to an end. Now it's time to see what this baby can do. Which is blast some Raffens to smithereens. And by the way – feel a little sorry for Panam. Gotta feel like shit, seeing Saul proved right.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/01_defend_the_camp`
20. **All right, looks like the fun's over. Your little joyrides come to an end. Now it's time to see what this baby can do. Which is blast some Raffens to smithereens. And by the way – feel a little sorry for Panam. Gotta feel like shit, seeing Saul proved right.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/01_defend_the_camp1`
21. **All right, looks like the fun's over. Your little joyrides come to an end. Now it's time to see what this baby can do. Which is blast some Raffens to smithereens. And by the way – feel a little sorry for Panam. Gotta feel like shit, seeing Saul proved right.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/01_defend_the_camp2`
22. **All right, looks like the fun's over. Your little joyrides come to an end. Now it's time to see what this baby can do. Which is blast some Raffens to smithereens. And by the way – feel a little sorry for Panam. Gotta feel like shit, seeing Saul proved right.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/01_defend_the_camp3`
23. **Return to the nomad camp.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02_drive_up_to_the_camp`
   - Map pin: ref `#sq027_mp_drive_panzer_to_camp`; position `3476.4040527344, -350.01623535156, 134.64080810547`
24. **Follow Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02_follow_panam`
25. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02_talk_to_panam`
26. **Talk to Saul.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02_talk_to_saul`
27. **Meet with Saul.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02a_meet_with_saul`
28. **Wait for Panam.**  
   `Primary` · `quests/side_quest/sq027_02_raffen_shiv_attack/05_camp_attack/02aa_wait_for_panam`

## Raymond Chandler Evening

- IGN walkthrough: [Raymond Chandler Evening](https://www.ign.com/wikis/cyberpunk-2077/Raymond_Chandler_Evening)
- Vanilla type: `MinorQuest`
- Quest hash: `3170691335`
- Quest path: `quests/minor_quest/mq040_biosculpt`
- District: Heywood
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `deliver/deposit item`, `combat/neutralize`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Usually it's the customers spillin' the ugly personal stories to the bartender, yet there we were, seeing it the other way around. Pepe thinks his wife is cheating on him and he's looking for someone to confirm his worst suspicions. Classic. A cuckold, a beautiful woman, a city shrouded in darkness... Get the feeling I've read this story before.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/01_bar_encounter`
   - Map pin: ref `#mq040_mp_commotion`; position `-1255.2883300781, -994.20928955078, 13.599998474121`
2. **Decide whether to intervene.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/01a_intervene_decide`
3. **Defeat the gangoons.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/02_fight`
   - Map pin: ref `#mq040_tr_elcoyote`; position `-1259.5587158203, -988.78985595703, 11.999999046326`
4. **Talk to the corpo.**  
   `Optional` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03_talk_corpo`
5. **Go to the area where Pepe's wife works during the day.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03a_go_to_trail_location`
   - Map pin: ref `#mq040_mp_trail_location`; position `-1003.7302856445, -870.48010253906, 8.4799995422363`
6. **Talk to Pepe.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03b_talk_pepe`
7. **Scan and identify Pepe's wife.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/04_identify_wife`
   - Map pin: ref `#mq040_tr_wife_scan_area`; position `-988.40893554688, -855.24566650391, 7.9999990463257`
8. **Follow Pepe's wife from a safe distance.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/05_trail_wife`
9. **Follow Pepe's wife into the building.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07_follow_inside`
   - Map pin: ref `#mq040_mp_building_entrance`; position `-870.00946044922, -668.75048828125, 9.8127422332764`
10. **Find Pepe's wife.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07a_find_wife`
   - Map pin: ref `#mq040_mp_apartment_door`; position `-883.71948242188, -669.21014404297, 13.962741851807`
11. **Talk to Cynthia.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08_confront_wife`
12. **Leave the building.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08a_corpo_report_back`
   - Map pin: ref `#mq040_mp_building_entrance`; position `-870.00946044922, -668.75048828125, 9.8127422332764`
13. **Call Pepe.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08b_report_back`
14. **Inform Pepe of your findings.**  
   `Primary` · `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/09_choose_side`

## Rebel! Rebel!

- IGN walkthrough: [Rebel Rebel](https://www.ign.com/wikis/cyberpunk-2077/Rebel_Rebel)
- Vanilla type: `SideQuest`
- Quest hash: `2831654127`
- Quest path: `quests/side_quest/sq017_kerry`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `retrieve/collect item`, `vehicle sequence`, `leave/escape area`

### Journal premise

Look, I don't know if Kerry's just having a real late-life crisis, or whether his shrink's got him some on some sweet new meds, but I do know one thing: this gon' be good. Just meet with the guy. Won't be bored, I guarantee it. And Kerry needs some help. Always did. I got nothing against it, either. A friend in need is a friend indeed, and I've never been jealous of that second fiddle in my life.

### Objective sequence

1. **Follow Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/caliente/follow_kerry`
2. **Drink coffee with Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/caliente/have_breakfast`
3. **Sit.**  
   `Primary` · `quests/side_quest/sq017_kerry/caliente/sit_down`
4. **Take Kerry to the given address.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/drive_kerry`
5. **See what Kerry's plans are.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/follow_kerry`
6. **Follow Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/follow_to_hide`
7. **Get in Kerry's car.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/get_back_to_car`
8. **Grab the keys.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/grab_keys`
   - Map pin: ref `#sq017_mp_truck_keys`; position `1326.1423339844, -771.34777832031, 45.451747894287`
9. **Hide.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/hide_with_kerry`
10. **Get out of the car.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/leave_car`
11. **Lose your tail.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/lose_pursuers`
12. **Check out the truck's cargo.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/open_truck`
13. **Take the things from the trunk.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/pick_gasoline`
14. **Throw a grenade at the truck.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/set_fire`
15. **Set up the stingers.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/set_spike_trap`
16. **Take the things from the trunk.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/take_suitcase`
17. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/talk_kerry`
18. **Tell the passenger to get out.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/tell_roadie_getout`
19. **Wait with Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/wait_for_truck`
20. **Wait for Kerry's instructions.**  
   `Primary` · `quests/side_quest/sq017_kerry/highwaymen/wait_kerry_instructions`
21. **Buy two coffees to go.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/buy_coffee`
22. **See where Kerry takes you.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/chat`
23. **Get in Kerry's car.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/get_into_car`
24. **Go to the meeting point between 12:30 and 3:30 AM.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/go_to_the_meeting_point`
25. **Answer the phone.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/phone_call`
26. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/talk_with_kerry_phone`
27. **Wait for Kerry.**  
   `Primary` · `quests/side_quest/sq017_kerry/intro/wait`

## Riders on the Storm

- IGN walkthrough: [Riders on the Storm](https://www.ign.com/wikis/cyberpunk-2077/Riders_on_the_Storm)
- Vanilla type: `SideQuest`
- Quest hash: `57791510`
- Quest path: `quests/side_quest/sq004_riders_on_the_storm`
- District: Southern Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Talk with Panam and Mitch.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/all_clear`
   - Map pin: ref `#sq004_mp_panam_n_saul_briefing`; position `3457.2570800781, -355.29016113281, 136.66110229492`
2. **Head to the Raffen Shiv camp.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drive`
   - Map pin: ref `#sq004_mp_raffen_shiv_camp`; position `3007.7243652344, -2385.0578613281, 124.62998199463`
3. **Disconnect from the drone.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_disconnect`
4. **Observe the camp gate and perimeter.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_gate`
   - Map pin: ref `#sq004_mp_drone_01_gate`; position `3012.1301269531, -2350.9907226563, 123.06999206543`
   - Map pin: ref `#sq004_mp_drone_01a_guardhouse`; position `3023.5798339844, -2352.7109375, 123.06999206543`
5. **Observe the main building.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_main_building`
   - Map pin: ref `#sq004_mp_drone_03_main`; position `2981.1721191406, -2402.5307617188, 127.38000488281`
6. **Observe the garage.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_passage`
   - Map pin: ref `#sq004_mp_drone_05_passage`; position `2981.1706542969, -2375.0812988281, 127.53999328613`
7. **Scan the vehicle tracks.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_tracks`
8. **Scan the truck.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/drone_truck`
9. **Call Panam back.**  
   `Optional` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/quest_delayed`
10. **Finalize preparations.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/finish_preparation`
11. **Get out of the van.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/get_out`
12. **Lean against the car.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/lean_car`
   - Map pin: ref `#sq004_mp_nomad_camp_veterans`; position `3456.7326660156, -375.76803588867, 134.66799926758`
13. **Follow Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/learn_situation`
14. **Park your vehicle.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/lookout_spot`
   - Map pin: ref `#sq004_mp_raffen_camp_lookout`; position `3079.6723632813, -2292.9011230469, 128.46000671387`
15. **Meet with Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/lookout_spot_wait`
16. **Return to Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/return`
17. **OK, this must actually be pretty serious. Tough chick like Panam wouldn't call you up for some chump chore. Must be something important. Wouldn't waste any time on this one if I were you. To the Aldecaldos' camp we go.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/roadhouse_briefing`
   - Map pin: ref `#sq004_mp_nomad_camp`; position `3379.8293457031, -356.44012451172, 137.46000671387`
18. **Take the shard.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/splinter`
19. **Take SuperJet.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/take_superjet`
20. **Talk with the veterans.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/talk_veterans`
   - Map pin: ref `#sq004_mp_nomad_camp_veterans`; position `3456.7326660156, -375.76803588867, 134.66799926758`
21. **Get in the van.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/01_camp/transmission_van`
22. **Find Saul.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/find_saul`
23. **Free Saul.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/free_saul`
   - Map pin: ref `#sq004_mp_basement_entrance`; position `2981.0266113281, -2417.5908203125, 117.00899505615`
24. **Get out of the van.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/get_out_jammer`
25. **Get inside the camp.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/infiltrate`
   - Map pin: ref `#sq004_mp_raffen_shiv_camp`; position `3007.7243652344, -2385.0578613281, 124.62998199463`
26. **Check the security feed.**  
   `Optional` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/security_computer`
27. **Find info on Saul.**  
   `Optional` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/security_room`
28. **Leave the building.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/out`
29. **Go to the main building.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/prison`
   - Map pin: ref `#sq004_mp_raffen_shiv_prison`; position `2979.701171875, -2404.0825195313, 123.88000488281`
30. **Find a safe way out.**  
   `Optional` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/stealth_out`
31. **Leave via the maintenance tunnel.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/stealth_out_known`
32. **Get in the back of the van.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/02_infiltration/truck`
33. **Follow Saul.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/cover`
34. **Get out of the van.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/exit_van`
35. **Sit on the couch.**  
   `Optional` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/sit_down`
36. **Defend against the attackers.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/defend`
37. **Escape from the camp.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/escape`
38. **Restore power to the farm.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/farm_prep`
39. **Turn up the heat.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/fire`
40. **Use the external panel.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/heating_external`
41. **Return to Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/kill_time`
42. **Talk with Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/morning_after`
43. **Find shelter.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/no_chase`
   - Map pin: ref `#sq004_tel_farmhouse`; position `1834.6097412109, -1085.8173828125, 57.894805908203`
44. **Talk with Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/panam_talk`
45. **Talk with Panam.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/return`
46. **Take the sniper rifle.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/reward`
47. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/talk_johnny`
48. **Talk to Panam and Saul.**  
   `Primary` · `quests/side_quest/sq004_riders_on_the_storm/03_escape/talk_saul`

## Sacrum Profanum

- IGN walkthrough: [Sacrum Profanum](https://www.ign.com/wikis/cyberpunk-2077/Sacrum_Profanum)
- Vanilla type: `MinorQuest`
- Quest hash: `1306283341`
- Quest path: `quests/minor_quest/mq032_sacrum`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `retrieve/collect item`, `combat/neutralize`

### Journal premise

You know, you could deal with our problems first, 'stead of helping every gonk that comes your way. But, well, since you're so hell-bent on saving that monk in distress, delta your ass over to the warehouse. Maybe you can still save him before they slice him. Kinda curious how you'll do it, actually. Gonna go all tree-hugging pacifist, or you gonna just get the job done?

### Objective sequence

1. **You know, you could deal with our problems first, 'stead of helping every gonk that comes your way. But, well, since you're so hell-bent on saving that monk in distress, delta your ass over to the warehouse. Maybe you can still save him before they slice him. Kinda curious how you'll do it, actually. Gonna go all tree-hugging pacifist, or you gonna just get the job done?**  
   `Primary` · `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook`
2. **Defeat the gangoons.**  
   `Primary` · `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom`
   - Map pin: ref `#mq032_tr_maelstrom`; position `-2167.0390625, 2873.5695800781, 7.10986328125`
3. **Talk to the monk.**  
   `Primary` · `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`
4. **Take Maelstrom's gear.**  
   `Primary` · `quests/minor_quest/mq032_sacrum/mq032_sacrum/04_loot`

## Second Conflict

- IGN walkthrough: [Second Conflict](https://www.ign.com/wikis/cyberpunk-2077/Second_Conflict)
- Vanilla type: `SideQuest`
- Quest hash: `3025872767`
- Quest path: `quests/side_quest/sq011_johnny`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `search/investigate`, `interact/use device`, `deliver/deposit item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Journal premise

Ah, just like old times. Never knew until we stepped onstage whether we'd have a full crew or not, whether Henry was too high outta his mind or whether Denny was locked up again. Most important thing is to find Nancy – she'll take care of everything. Always did, always will. And you wanna see Samurai on stage, don't you?

### Objective sequence

1. **Go to Denny's mansion.**  
   `Primary` · `quests/side_quest/sq011_johnny/03_denny/01_visit`
   - Map pin: ref `#sq011_mp_dennys_house`; position `512.09802246094, 1249.2041015625, 230.51875305176`
2. **Find Denny and Henry.**  
   `Primary` · `quests/side_quest/sq011_johnny/03_denny/02_find_denny`
   - Map pin: ref `#sq011_tr_dennys_house`; position `502.71621704102, 1292.8026123047, 234.47496032715`
3. **Talk to Denny and Henry.**  
   `Primary` · `quests/side_quest/sq011_johnny/03_denny/03_talk_to_denny`
4. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_johnny/03_denny/04_talk_to_kerry`
5. **Use the intercom to call Denny's house.**  
   `Optional` · `quests/side_quest/sq011_johnny/03_denny/01_visit1`
6. **Enter the Totentanz.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/01_get_to_totentanz`
   - Map pin: ref `#sq011_mp_totentanz_door`; position `-1749.2894287109, 2247.5275878906, 19.412740707397`
   - Map pin: ref `#sq011_mp_totentanz_elevator_1st_floor`; position `-1743.5225830078, 2230.0688476563, 23.18726348877`
   - Map pin: ref `#sq011_mp_totentanz_entrance`; position `-1731.7457275391, 2218.4272460938, 91.11051940918`
7. **Talk to Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/01_talk_to_nancy`
8. **Talk to Nancy and Brick.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/01_talk_to_nancy1`
9. **Talk to Patricia about Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/01_talk_to_patricia_about_nancy`
10. **Free Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/02_free_nancy`
11. **Talk to Dum Dum.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/02_talk_to_dumdum`
12. **Talk to Maelstromers.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/02_talk_to_gangsters`
13. **Go to the Totentanz bathroom.**  
   `Optional` · `quests/side_quest/sq011_johnny/04_nancy/07_get_to_toilet`
   - Map pin: ref `#sq011_mp_toilet`; position `-1699.2779541016, 2214.5207519531, 87.284759521484`
14. **Talk to Nancy off to the side.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/02_talk_to_nancy_privately`
15. **Go out the window.**  
   `Optional` · `quests/side_quest/sq011_johnny/04_nancy/08_get_on_ledge`
   - Map pin: ref `#sq011_mp_ledge`; position `-1694.4974365234, 2217.3933105469, 87.284759521484`
16. **Follow Dum Dum.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/03_follow_dumdum`
17. **Go out on the balcony.**  
   `Optional` · `quests/side_quest/sq011_johnny/04_nancy/09_get_to_tarrace`
   - Map pin: ref `#sq011_mp_terrace`; position `-1713.3345947266, 2237.3237304688, 87.284759521484`
18. **Get Nancy out of the Totentanz.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/03_get_nancy_out`
19. **Talk to Patricia.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/03_talk_to_patricia`
20. **Escort Nancy to the exit.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/04_escort_nancy`
   - Map pin: ref `#sq011_mp_elevator_totentanz`; position `-1742.6466064453, 2228.6079101563, 87.222747802734`
21. **Escort Nancy to the car.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/04_escort_nancy_car`
22. **Follow Patricia.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/04_follow_patricia`
23. **Defeat the Maelstromers.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/04_follow_patricia1`
24. **Talk to Royce and Dum Dum.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/04_talk_to_dumdum_royce`
25. **Enter the room where Nancy is waiting.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/05_walk_into_nancy_room`
26. **Get in the car.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/06_get_to_car`
27. **Leave the Totentanz.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/08_escort_nancy_car`
   - Map pin: ref `#sq011_mp_totentanz_elevator_1st_floor`; position `-1743.5225830078, 2230.0688476563, 23.18726348877`
28. **Get in Nancy's car.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/08_escort_nancy_car1`
29. **Get in the car.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/09_get_to_car`
30. **Go to N54 News with Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/10_drive_to_news54`
   - Map pin: ref `#sq011_mp_news54`; position `-724.59460449219, 650.07495117188, 35.477237701416`
31. **Enter the elevator.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/11_get_into_elevator`
   - Map pin: ref `#sq011_mp_elevator_totentanz`; position `-1742.6466064453, 2228.6079101563, 87.222747802734`
32. **Go to the elevator to leave the Totentanz.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/12_get_to_elevator`
   - Map pin: ref `#sq011_mp_elevator_totentanz`; position `-1742.6466064453, 2228.6079101563, 87.222747802734`
33. **Follow Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/12a_follow_nancy_out_totentanz`
34. **Get out of Nancy's car.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/15_leave_car`
35. **Call Kerry.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/15_talk_to_kerry`
36. **Talk to Kerry.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/15_talk_to_kerry1`
37. **Talk to Nancy.**  
   `Primary` · `quests/side_quest/sq011_johnny/04_nancy/15_talk_to_nancy`

## Send in the Clowns

- IGN walkthrough: [Send in the Clowns](https://www.ign.com/wikis/cyberpunk-2077/Send_in_the_Clowns)
- Vanilla type: `MinorQuest`
- Quest hash: `3198790588`
- Quest path: `quests/minor_quest/mq035_ozob`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `wait/time gate`, `search/investigate`, `combat/neutralize`, `vehicle sequence`

### Objective sequence

1. **Ozob… Quite the name. Don't know why, but the sound of it gets creepy circus music stuck in my head. Maybe the dude was an acrobat or lion tamer or some shit. Never know in this city. And we won't know till we call him and find out.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/00_call_ozob`
2. **Ozob asked V to pick him up from Japan Town market and drive him to a few places in the city.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/02_meet_ozob`
3. **Drive Ozob to Little China.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/03_drive_to_casino`
   - Map pin: ref `#mq035_mrk_robbery_parking_spot`; position `-1572.9195556641, 1213.5726318359, 17.522167205811`
4. **Wait for Ozob.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/04_wait`
5. **Drive Ozob to the given location.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/05_drive_to_ambush`
   - Map pin: ref `#mq035_mrk_ambush_parking_spot`; position `-1472.4375, 2363.1875, 18.1904296875`
6. **Defeat all enemies.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/06_kill_enemies`
7. **Talk to Ozob.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/07_talk_ozob`
8. **Honk.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/honk`
9. **Return to the car.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/return_to_car`
10. **Wait for Ozob.**  
   `Primary` · `quests/minor_quest/mq035_ozob/mq035_ozob/wait_for_ozob_to_get_in_car`

## Sex On Wheels

- IGN walkthrough: [Sex On Wheels](https://www.ign.com/wikis/cyberpunk-2077/Sex_On_Wheels)
- Vanilla type: `MinorQuest`
- Quest hash: `522295962`
- Quest path: `quests/minor_quest/mq044_jakes_vehicle`
- District: Santo Domingo
- Candidate building blocks: `deliver/deposit item`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **Who ever said no to a free car? Not to mention it's a Quadra Turbo Fuckin' R. So quit picking your nose, head down to Rancho Coronado and get behind that wheel.**  
   `Primary` · `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage`
2. **Get in the car.**  
   `Primary` · `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car`
3. **Leave the area.**  
   `Primary` · `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/04_leave_area`
   - Map pin: ref `#mq044_tr_area`; position `497.4375, -664.59375, 8.8935546875`

## Shape of a Pony

- IGN walkthrough: [Shape of a Pony](https://www.ign.com/wikis/cyberpunk-2077/Shape_of_a_Pony)
- Vanilla type: `MinorQuest`
- Quest hash: `1052046523`
- Quest path: `quests/minor_quest/mws_se5_07`
- District: Badlands
- Candidate building blocks: `phone/message contact`, `search/investigate`, `combat/neutralize`, `vehicle sequence`

### Journal premise

I dunno if I should be flattered or embarrassed. It's a fine line beween superfan and superpsycho. But only a gonk says no to a Porsche 911 Turbo (930) – and a convertible at that. Especially if it's already bought and paid for.

### Objective sequence

1. **Go the car's last known location.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07/corpse`
   - Map pin: ref `#mws_se5_07_insvestigation`; position `-720.33001708984, -2271.2397460938, 14.14999961853`
2. **Inspect the body for clues.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1`
3. **Read and reply to the message from Muamar.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07a/objective`
4. **Find the car.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07c/objective`
   - Map pin: ref `#mws_se5_07_car_search`; position `-1069.9899902344, -2438.3999023438, 25.369998931885`
5. **Defeat the Wraiths and recover the key.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1`
   - Map pin: ref `#mws_se5_07_combat`; position `-1093.2501220703, -2430.8701171875, 28.370004653931`
6. **Get in the car.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2`
   - Map pin: ref `#mws_se5_07_ws_porsche`; position `-1104.7098388672, -2424.4304199219, 25.469999313354`
7. **Text Muamar about recovering the car.**  
   `Primary` · `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3`

## Shoot To Thrill

- IGN walkthrough: [Shoot to Thrill](https://www.ign.com/wikis/cyberpunk-2077/Shoot_to_Thrill)
- Vanilla type: `MinorQuest`
- Quest hash: `4084099381`
- Quest path: `quests/minor_quest/mq011_wilson`
- District: Watson / Little China
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`

### Journal premise

A shooting range competition? Ho-ho, wonder what fun prizes are up for grabs. Giant teddy bear? Inflatable sword? Tiny plastic football? Whatever it is, enjoy yourself, 'cause I'm sittin' this one out. Don't much like it when people treat weapons like toys.

### Objective sequence

1. **A shooting range competition? Ho-ho, wonder what fun prizes are up for grabs. Giant teddy bear? Inflatable sword? Tiny plastic football? Whatever it is, enjoy yourself, 'cause I'm sittin' this one out. Don't much like it when people treat weapons like toys.**  
   `Primary` · `quests/minor_quest/mq011_wilson/00_wilson/00_talk_wilson`
2. **Go to Wilson's shooting range.**  
   `Primary` · `quests/minor_quest/mq011_wilson/00_wilson/01_go_to_wilson`
   - Map pin: ref `#mq011_mp_gun_range`; position `-1454.7772216797, 1310.70703125, 119.07958984375`
3. **Talk to Wilson.**  
   `Primary` · `quests/minor_quest/mq011_wilson/00_wilson/02_talk_to_wilson`
4. **Enter the shooting range.**  
   `Primary` · `quests/minor_quest/mq011_wilson/00_wilson/03_enter_range`
   - Map pin: ref `#mq011_tr_inside_range`; position `-1455.3453369141, 1305.4464111328, 119.00875091553`
5. **Listen to Wilson's instructions.**  
   `Primary` · `quests/minor_quest/mq011_wilson/00_wilson/04_listen_instructions`
6. **Get into position.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/000_wait`
   - Map pin: ref `#mq011_tr_shooting_position`; position `-1455.6585693359, 1302.3236083984, 119.0645904541`
7. **Wait for the competition to begin.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/000b_wait`
8. **Shoot the targets.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/00_shoot`
9. **Draw and aim your weapon.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/00b_ready`
10. **Go to Wilson.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/01_go_wilson`
11. **Talk to Wilson.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/01b_talk_to_wilson`
12. **Collect your reward from Wilson.**  
   `Primary` · `quests/minor_quest/mq011_wilson/01_competition/02_grab_prize`

## Sinnerman

- IGN walkthrough: [Sinnerman](https://www.ign.com/wikis/cyberpunk-2077/Sinnerman)
- Vanilla type: `SideQuest`
- Quest hash: `2699075783`
- Quest path: `quests/side_quest/sq023_hit_order`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `follow/escort`, `wait/time gate`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`

### Objective sequence

1. **Sit and wait for Bill Jablonsky.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/03a_wait_4_bill`
2. **Get behind the wheel of Bill Jablonsky's truck.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/13_enter_car`
3. **Get in the NCPD vehicle.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/14_join_joshua`
4. **Follow the car.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/attack_joshua`
5. **Call Wakako Okada to take the job.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/call_fixer`
6. **Call Wakako Okada.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/call_wakako_money`
7. **Follow Bill Jablonsky.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/follow_bill`
8. **Return to Joshua Stephenson.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/go_back`
9. **Return to Bill Jablonsky's truck.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/go_back_car`
10. **Neutralize Joshua Stephenson.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/kill_joshua`
11. **Exit car.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/leave_car`
12. **Stop the car.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/stop_car`
13. **Talk to Bill Jablonsky.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/talk_briefing`
14. **Talk to Joshua Stephenson.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/talk_joshua`
15. **You're right about one thing – this job from Wakako stinks to high heaven. Besides, you're above doing plain ol' hit jobs. Probably no harm in talking to Bill Jablonsky and seeing what his deal is. But if I were you? I'd take a hard pass.**  
   `Primary` · `quests/side_quest/sq023_hit_order/hook/talk_wakako`

## Small Man, Big Mouth

- IGN walkthrough: [Small Man, Big Mouth](https://www.ign.com/wikis/cyberpunk-2077/Small_Man,_Big_Mouth)
- Vanilla type: `MinorQuest`
- Quest hash: `2418655775`
- Quest path: `quests/minor_quest/mq017_streetkid`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `retrieve/collect item`, `combat/neutralize`

### Objective sequence

1. **Kirk called to say he had a job for you? That this time everything'll go smooth? Totally safe, zero risk, and big payout? What're you waiting for? Sounds like nothing could possibly go wrong!**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/01_meet_kirk`
2. **Talk to Johnny.**  
   `Optional` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/01a_talk_with_johnny`
3. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/01a_talk_with_johnny1`
4. **Talk to Kirk.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/02_talk_with_kirk`
5. **Talk to Kirk.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03__a_talk_with_kirk`
6. **Sit next to Kirk.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03__b_sit_down_on_the_couch`
   - Map pin: ref `#mq017_mk_couch`; position `-1268.4293212891, -989.73968505859, 16.51000213623`
7. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03_cc_talk_with_johnny`
8. **Go to the meeting with Kirk.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03_follow_kirk`
   - Map pin: ref `#mq017_mk_meeting_point`; position `-968.21978759766, -1659.830078125, 10.410352706909`
9. **Look for the truck containing the goods.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03a_look_for_delivery_truck`
10. **Defeat the guards.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03aa_neutralize_garage_guard`
11. **See what's inside the truck.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03b_look_inside`
   - Map pin: ref `#mq017_mk_truck_door`; position `-1034.9603271484, -1703.0402832031, 12.440351486206`
12. **Take the goods.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03c_open_container`
13. **Return to Kirk.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/03d_get_back_to_kirk`
   - Map pin: ref `#mq017_mk_dead_kirk`; position `-970.16979980469, -1656.7800292969, 10.410352706909`
14. **Confront the gangoons.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/04_confront_thugs`
15. **Defeat the gangoons.**  
   `Primary` · `quests/minor_quest/mq017_streetkid/mq017_streetkid/05_defeat_thugs`

## Space Oddity

- IGN walkthrough: [Space Oddity](https://www.ign.com/wikis/cyberpunk-2077/Space_Oddity)
- Vanilla type: `MinorQuest`
- Quest hash: `3243328375`
- Quest path: `quests/minor_quest/mq003_orbitals`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `choice/decision`

### Objective sequence

1. **Every bum in this town dreams someday they'll hit the jackpot on something they dug up in a dumpster and it'll transform their life. A briefcase stuffed with eddies, a shard holding big company secrets, a cuttin' edge implant that'll pawn for a few dozen Gs. Problem is, usually whoever "misplaced" the thing to begin with is probably still lookin' for it – and they ain't in a good mood. Do these poor street rats a favor and take this case off their hands. Before the previous owner shows up and decides to make target practice out of 'em.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/01_homeless_question`
   - Map pin: ref `#mq003_mp_homeless`; position `-286.86468505859, -1951.2421875, 11.031002044678`
2. **Find the body of the briefcase's owner.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/05_find_corpse`
   - Map pin: ref `#mq003_tr_02_corpse_area`; position `-278.54724121094, -1986.3715820313, 8.7400007247925`
3. **Buy the briefcase from the bums.**  
   `Optional` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/01b_buy_suitcase`
   - Map pin: ref `#mq003_mp_homeless`; position `-286.86468505859, -1951.2421875, 11.031002044678`
4. **Scan the area for clues.**  
   `Optional` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/05a_clues`
   - Map pin: ref `#mq003_tr_02_corpse_area`; position `-278.54724121094, -1986.3715820313, 8.7400007247925`
5. **Examine the body.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/05b_examine_corpse`
6. **Take the access shard.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/05c_take_shard`
7. **Examine the briefcase.**  
   `Optional` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/03_suitcase_grab`
8. **Slot the access shard into the briefcase.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/06_suitcase_unlock`
9. **Browse the files on the computer.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/06a_suitcase_examine`
10. **Activate orbital drop when ready.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/06b_suitcase_activate`
11. **Go to the drop point.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/07_landing_loc`
   - Map pin: ref `#mq003_mp_landing_loc`; position `-1025.7705078125, -3636.3098144531, 49.160011291504`
12. **Defeat all enemies.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/08_eliminate_enemies`
   - Map pin: ref `#mq003_tr_03_landing_loc`; position `-1025.9398193359, -3636.5598144531, 49.410011291504`
13. **Open the package.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/09_retrieve_pod`
14. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq003_orbitals/mq003_orbitals/10_talk_johnny`

## Spray Paint

- IGN walkthrough: [Spray Paint](https://www.ign.com/wikis/cyberpunk-2077/Spray_Paint)
- Vanilla type: `MinorQuest`
- Quest hash: `1300734810`
- Quest path: `quests/minor_quest/mq037_brendan_hooligan001`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **Stop the vandal.**  
   `Primary` · `quests/minor_quest/mq037_brendan_hooligan001/mq037_brendan_hooligan/00_deal_with_the_hooligan`
2. **Talk to Brendan.**  
   `Primary` · `quests/minor_quest/mq037_brendan_hooligan001/mq037_brendan_hooligan/01_talk_with_brendan`

## Stadium Love

- IGN walkthrough: [Stadium Love](https://www.ign.com/wikis/cyberpunk-2077/Stadium_Love)
- Vanilla type: `MinorQuest`
- Quest hash: `4108321249`
- Quest path: `quests/minor_quest/mq008_party`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `retrieve/collect item`

### Objective sequence

1. **Hey, if you wanna crash that party, I can respect that. Sometimes those parties kick the most ass. Just watch yourself – this ain't your uncle's birthday barbecue. One wrong word, one false step… there could be blood.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/01_check_whats_up`
2. **Talk to the 6th Street leader.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/02_speak_rep`
3. **Take the gun.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/02a_take_gun`
4. **Go to the first station.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/03_first_spot`
   - Map pin: ref `#mq008_marker_glass_01`; position `516.07568359375, -2132.9174804688, 31.344532012939`
5. **Go to the second station.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/03_first_spot1`
   - Map pin: ref `#mq008_marker_glass_02`; position `542.36303710938, -2121.974609375, 35.663379669189`
6. **Go to the third station.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/03_first_spot2`
   - Map pin: ref `#mq008_marker_glass_03`; position `553.20513916016, -2174.79296875, 39.116207122803`
7. **Go to the final station.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/03_first_spot3`
   - Map pin: ref `#mq008_marker_glass_04`; position `584.61291503906, -2181.076171875, 47.830455780029`
8. **Get as many points as possible.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/03a_points`
9. **Drink the shot.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/04_drink_spot1`
   - Map pin: ref `#mq008_marker_glass_01`; position `516.07568359375, -2132.9174804688, 31.344532012939`
10. **Drink the shot.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/04_drink_spot2`
   - Map pin: ref `#mq008_marker_glass_02`; position `542.36303710938, -2121.974609375, 35.663379669189`
11. **Drink the shot.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/04_drink_spot3`
   - Map pin: ref `#mq008_marker_glass_03`; position `553.20513916016, -2174.79296875, 39.116207122803`
12. **Drink the shot.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/04_drink_spot4`
   - Map pin: ref `#mq008_marker_glass_04`; position `584.61291503906, -2181.076171875, 47.830455780029`
13. **Hit as many targets as you can in 12 seconds.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles1`
14. **Hit as many targets as you can in 12 seconds.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles2`
15. **Hit as many targets as you can in 12 seconds.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles3`
16. **Hit as many targets as you can in 12 seconds.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles4`
17. **Return to the 6th Street leader.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/15_back_to_rep`
18. **Ask about your results.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/16_talk_results`
19. **Collect your reward.**  
   `Primary` · `quests/minor_quest/mq008_party/mq008_party/17_pick_up_the_reward`

## Stairway To Heaven

- IGN walkthrough: [Stairway to Heaven](https://www.ign.com/wikis/cyberpunk-2077/Stairway_to_Heaven)
- Vanilla type: `MinorQuest`
- Quest hash: `549579593`
- Quest path: `quests/minor_quest/mq014_02_second`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **Look at that, your Zen master has reappeared. Some advertising shtick, no doubt. Thing is, I don't know fuck all about what he's trying to sell you. Stay sharp around characters like him.**  
   `Primary` · `quests/minor_quest/mq014_02_second/02_second/01_approach_master`
2. **Talk to the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_02_second/02_second/02_talk_sranger`
3. **Return to the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_02_second/02_second/03_come_back`
4. **Meditate with the Zen master.**  
   `Primary` · `quests/minor_quest/mq014_02_second/02_second/04_earth`

## Sweet Dreams

- IGN walkthrough: [Sweet Dreams](https://www.ign.com/wikis/cyberpunk-2077/Sweet_Dreams)
- Vanilla type: `MinorQuest`
- Quest hash: `1178950195`
- Quest path: `quests/minor_quest/mq036_overload`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `leave/escape area`

### Objective sequence

1. **Everyone knows the most gut-twisting, brain-blitzing, 'dorph-jacking braindances aren't bought in stores or feeders, but on the streets, outside normal circulation. Take our fine man Stefan, here, as proof. Seems he's got the rawest BDs in the city – not for the faint of heart. Whaddaya say? Wanna take that rush to the next level?**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/00_talk_stefan`
2. **Play Stefan's BD.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/01_experience_bd`
3. **Ask Stefan about the corrupted BD.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/02_ask_stefan`
4. **Follow Stefan.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/03_follow_stefan`
5. **Use Stefan's BD player.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/04_use_stefan_player`
6. **Find and retrieve the equipment.**  
   `Optional` · `quests/minor_quest/mq036_overload/mq036_overload/05b_retrieve_equipment`
   - Map pin: ref `#mq036_tr_stolen_equipment_area_mappin`; position `-468.61120605469, 401.04544067383, 130.98266601563`
7. **Escape the scav hideout.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/05_escape_hideout`
   - Map pin: ref `#mq036_mrk_hideout_elevator`; position `-439.01089477539, 412.83831787109, 133.20248413086`
   - Map pin: ref `#mq036_mrk_hideout_exit`; position `-467.42401123047, 376.82833862305, 132.00006103516`
8. **Retrieve the equipment.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/05c_retrieve_equipment_2`
   - Map pin: ref `#mq036_mrk_stolen_equipment`; position `-478.11611938477, 406.78735351563, 133.42697143555`
9. **Confront Stefan.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/06_confront_stefan`
10. **Kill Stefan.**  
   `Primary` · `quests/minor_quest/mq036_overload/mq036_overload/07_kill_stefan`

## Talkin' 'bout a Revolution

- IGN walkthrough: [Talking Bout A Revolution](https://www.ign.com/wikis/cyberpunk-2077/Talking_Bout_A_Revolution)
- Vanilla type: `SideQuest`
- Quest hash: `117729654`
- Quest path: `quests/side_quest/sq026_03_pizza`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `interact/use device`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Talk to Judy.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/00_holocall/talk_judy`
2. **There's no such thing as a free lunch, V. If someone invites you to a chow-down, someone's gonna pay. Who knows, maybe the bad guys'll saddle up – answer for all the bad shit they've done. But you know what I think? I think you're the one who's paying. And that check's well on its way.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/00_holocall/wait_call`
3. **Discuss Judy's plan.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/discussion`
4. **Enter the apartment.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/enter_apartment`
   - Map pin: ref `#sq026_tr_08_judys_enter`; position `-900.64978027344, 1864.2322998047, 42.191398620605`
5. **Stay the night.**  
   `Optional` · `quests/side_quest/sq026_03_pizza/01_pizza_night/stay_night`
6. **Get up.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/get_up_kitchen`
7. **Use the intercom.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/intercom`
   - Map pin: ref `#sq026_dvc_judys_intercom`; position `-905.51452636719, 1867.6087646484, 43.910011291504`
8. **Join the others in the kitchen.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/join_kitchen`
   - Map pin: ref `#sq026_tr_08_kitchen`; position `-904.93145751953, 1860.4886474609, 42.156021118164`
9. **Leave the building.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/leave`
   - Map pin: ref `#sq026_mp_judys_exit`; position `-906.78930664063, 1846.6743164063, 36.560012817383`
10. **Go to Judy's apartment in the evening.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/location`
   - Map pin: ref `#sq026_mp_judys_apartment`; position `-904.87945556641, 1868.4906005859, 43.871696472168`
11. **Sit on the stool.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/sit_kitchen`
12. **Test out Tom's combat skills.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/sparing`
13. **Talk to the others.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/talk_judy_roxanne`
14. **Eat breakfast.**  
   `Optional` · `quests/side_quest/sq026_03_pizza/01_pizza_night/breakfast`
15. **Talk to Judy in private.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/talk_private`
16. **Wait until evening.**  
   `Primary` · `quests/side_quest/sq026_03_pizza/01_pizza_night/wait_evening`
   - Map pin: ref `#sq026_07_wait`; position `-911.82733154297, 1868.4095458984, 43.447635650635`

## The Ballad of Buck Ravers

- IGN walkthrough: [The Ballad of Buck Ravers](https://www.ign.com/wikis/cyberpunk-2077/The_Ballad_of_Buck_Ravers)
- Vanilla type: `MinorQuest`
- Quest hash: `140985621`
- Quest path: `quests/minor_quest/mq023_bootleg`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`

### Journal premise

Don't think I've gone all sentimental or anything. Honestly, I couldn't give a shit if I've got any fans left in this city. If someone hears one of my tracks and they get the itch to take to the streets, then that's fuckin' nova, but those old recordings don't matter anymore. Find 'em, listen to 'em, I don't care. Although, while we're on the subject... Wonder how things are over at Rainbow Cadenza...

### Objective sequence

1. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny`
2. **Go to the Rainbow Cadenza club.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue`
   - Map pin: ref `#mq023_mk_diner`; position `-657.79235839844, 924.44226074219, 12.499999046326`
3. **Ask the staff about the club.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff`
4. **Talk to the cook.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/03a_talk_with_waiter`
5. **Find the vendor selling the tapes.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor`
6. **Talk to the vendor.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim`
7. **Persuade the vendor to give you the tapes.**  
   `Primary` · `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim`

## The Beast In Me

- IGN walkthrough: [The Beast In Me](https://www.ign.com/wikis/cyberpunk-2077/The_Beast_In_Me)
- Vanilla type: `SideQuest`
- Quest hash: `4262647041`
- Quest path: `quests/meta/07_nc_underground`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `wait/time gate`, `retrieve/collect item`, `vehicle sequence`

### Journal premise

No one in Night City is only one layer deep. Take Claire for example – an Afterlife bartender who likes to burn rubber in illegal street races when she's on break. If you get the itch for a little adrenaline, I think you can scratch it at her garage.

### Objective sequence

1. **No one in Night City is only one layer deep. Take Claire for example – an Afterlife bartender who likes to burn rubber in illegal street races when she's on break. If you get the itch for a little adrenaline, I think you can scratch it at her garage.**  
   `Primary` · `quests/meta/07_nc_underground/00_hook/01_talk_claire`
2. **Send a message to Claire.**  
   `Primary` · `quests/meta/07_nc_underground/00_hook/03_text_claire`
3. **Visit Claire at her garage during the day.**  
   `Primary` · `quests/meta/07_nc_underground/01_garage/00a_claire_garage`
   - Map pin: ref `#sq024_mp_garage`; position `-644.14172363281, -1258.1007080078, 11.173746109009`
4. **Talk to Claire in her garage.**  
   `Primary` · `quests/meta/07_nc_underground/01_garage/01_talk_to_clair`
   - Map pin: ref `#sq024_mp_garage`; position `-644.14172363281, -1258.1007080078, 11.173746109009`
5. **Wait for Claire to contact you.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000_wait_city`
6. **Read the message from Claire.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000a1_read_message`
7. **Read the message from Claire.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000a_read_message`
8. **Wait for Claire to contact you.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000a_wait_badlands`
9. **Read the message from Claire.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000b1_read_message`
10. **Wait for Claire to contact you.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/000b_wait_santo`
11. **Wait for Claire to contact you.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/00_wait_for_cal`
12. **Read the message from Claire.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/02a_read_message`
13. **Send a message to Claire.**  
   `Primary` · `quests/meta/07_nc_underground/02_big_race_call/03_text_claire`
14. **Complete the qualifying races.**  
   `Primary` · `quests/meta/07_nc_underground/03_races/00_beat_races`
15. **Finish "The Big Race."**  
   `Primary` · `quests/meta/07_nc_underground/03_races/01_complete_big_race`
   - Map pin: ref `#sq024_mp_big_race`; position `63.470703125, 3.9735107421875, 14.378021240234`
16. **Confront Sampson at Claire's side.**  
   `Primary` · `quests/meta/07_nc_underground/06_sampson/05_confront_sampson`
17. **Talk to Claire.**  
   `Primary` · `quests/meta/07_nc_underground/06_sampson/07_talk_claire`
18. **Get in Claire's ride.**  
   `Primary` · `quests/meta/07_nc_underground/07_forlorn_hope/000_get_in`
19. **Talk to Claire.**  
   `Primary` · `quests/meta/07_nc_underground/07_forlorn_hope/03_talk_claire`
20. **Return to Claire's garage.**  
   `Primary` · `quests/meta/07_nc_underground/07_forlorn_hope/04_drive`

## The Gift

- IGN walkthrough: [The Gift](https://www.ign.com/wikis/cyberpunk-2077/The_Gift)
- Vanilla type: `SideQuest`
- Quest hash: `2549135402`
- Quest path: `quests/side_quest/sq_q001_tbug`
- District: Watson
- Level: 60
- Candidate building blocks: `search/investigate`, `interact/use device`, `hack/breach/download`, `retrieve/collect item`

### Journal premise

T-Bug's prolly the last person you'd expect to do presents. She's not the kind of gal who goes around buyin' novelty coffee mugs or t-shirts of your favorite comic book hero. But a netrunner program...? For you? For the job? Shit... she must really like you, ese.

### Objective sequence

1. **Equip the Ping quickhack in your inventory and upload it to the camera.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just`
2. **Equip the Ping quickhack in your inventory.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping`
3. **Retrieve the Ping quickhack from the netrunner.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms`
4. **Equip the Ping quickhack in your inventory and upload it to the camera in order to locate an Access Point.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping`
5. **Use your personal link to connect to the Access Point and hack it.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point`
6. **Upload Ping to the camera to find the Access Point.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap`
7. **Upload Ping to the camera.**  
   `Primary` · `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just`

## The Gig

- IGN walkthrough: [The Gig (Side Gig)](https://www.ign.com/wikis/cyberpunk-2077/The_Gig_(Side_Gig))
- Vanilla type: `SideQuest`
- Quest hash: `3861473594`
- Quest path: `quests/side_quest/sq_q001_wakako`
- Level: 60
- Candidate building blocks: `retrieve/collect item`

### Objective sequence

1. **Whenever we go see Wakako and walk into that pachinko salon of hers, I get this weird, like, tingling feeling on the back of my neck. I dunno, V, she's all kinds of weird. Anyway, she promised a special reward for this job with Sandra Dorsett. All we have to do is go see her on Jig-Jig Street.**  
   `Primary` · `quests/side_quest/sq_q001_wakako/wakako/00_reward`
2. **Collect your reward from Wakako.**  
   `Primary` · `quests/side_quest/sq_q001_wakako/wakako/01_reward`
3. **Collect your free reward from Cassius Ryder's ripperdoc shop inventory.**  
   `Primary` · `quests/side_quest/sq_q001_wakako/wakako/02_reward`

## The Gun

- IGN walkthrough: [The Gun](https://www.ign.com/wikis/cyberpunk-2077/The_Gun)
- Vanilla type: `SideQuest`
- Quest hash: `3374603296`
- Quest path: `quests/side_quest/sq_q001_wilson`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `retrieve/collect item`

### Journal premise

We've got this tradition in Heywood – on your sixteenth birthday your dad gives you a gun. I didn't get one, cuz I had a shitty dad. But you're way past your sixteenth, aren't ya? High time to get yourself a solid piece of iron.

### Objective sequence

1. **Talk to Wilson.**  
   `Primary` · `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson`
2. **Enter the shooting range.**  
   `Primary` · `quests/side_quest/sq_q001_wilson/wilson/03_enter_range`
   - Map pin: ref `#q001_mp_shooting_range`; position `-1463.9645996094, 1303.4479980469, 120.40370941162`
3. **Collect your gun from Wilson.**  
   `Primary` · `quests/side_quest/sq_q001_wilson/wilson/meet_wilson`

## The Highwayman

- IGN walkthrough: [The Highwayman](https://www.ign.com/wikis/cyberpunk-2077/The_Highwayman)
- Vanilla type: `MinorQuest`
- Quest hash: `3398058209`
- Quest path: `quests/minor_quest/mq029_tourist`
- Level: 60
- Candidate building blocks: `search/investigate`, `interact/use device`, `retrieve/collect item`

### Objective sequence

1. **Josie hid the Tyger boss's bike somewhere in the city, near the All Foods factory in Maelstrom turf. Said to look for a "ghost horse." All right then… Think of it like a scavenger hunt, though not the kind fixers in Night City usually pay you for.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_bike`
2. **The nomad Josie was lured into a trap by a Tyger Claw named James.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_body`
3. **Find out what happened to Josie.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_garage`
4. **Josie… Pretty name. Cute girl. Ugly end. This Tyger from the still… better have a word with him, V. Can't let slide what he did to this poor girl.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_james`
5. **Josie… Pretty name. Cute girl. Ugly end. This Tyger from the still… better have a word with him, V. Can't let slide what he did to this poor girl.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james`
6. **Josie hid the Tyger boss's bike somewhere in the city, near the All Foods factory in Maelstrom turf. Said to look for a "ghost horse." All right then… Think of it like a scavenger hunt, though not the kind fixers in Night City usually pay you for.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike`
7. **That chick, Josie, wrote something about a garage, didn't she? Somewhere near the dam. Not like it's any of my biz, but if I were you, I'd go check it out. Something tells me it'll give you a boost in the right direction. A sixth sense, shall we say. On the other hand, I am basically dead, which would mean I don't think, so don't hold me to that.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage`
8. **There's a still of some young guy in the garage – the heartbreaker type. Emails on the computer are from a certain James –  don't have to be a genius to connect the dots. Might be worth looking for our Romeo – especially in Japantown. Got a feeling the still was snapped there. Wouldn't surprise me – kids go on dates there all the time. Shit... it always starts off so cute, doesn't it? Rarely ever ends that way.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james`
9. **Another mystery, another missing person in Night City. Used to be the cops would put out a search for people like her. Today, her fate's in your hands.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new`
   - Map pin: ref `#mq029_tr_mappin_area_josie_corpse`; position `-1345.25, -639.375, 7.703125`
10. **Pick up the still.**  
   `Primary` · `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_pick_up_photo`

## The Hunt

- IGN walkthrough: [The Hunt](https://www.ign.com/wikis/cyberpunk-2077/The_Hunt)
- Vanilla type: `SideQuest`
- Quest hash: `3670998070`
- Quest path: `quests/side_quest/sq021_sick_dreams`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `combat/neutralize`, `vehicle sequence`, `choice/decision`, `leave/escape area`

### Objective sequence

1. **Choose a farm.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/after_bd/04_choose_farm`
2. **Wait for River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/after_bd/05_wait_for_river`
3. **Plan the next move with River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/after_bd/after_bd`
4. **Get to River's car.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/after_bd/car`
5. **Drive to the farm with River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/after_bd/listen`
6. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/aftermath/talk`
7. **Talk to Joss.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bbq/enjoy`
8. **Follow River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bbq/help`
9. **Follow River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bbq/joss`
10. **Go to bed.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bbq/sleep`
11. **Relive the braindance.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/05_school_listen`
12. **Exit the braindance.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/06_leave_bd`
13. **Exit the braindance to proceed to the next section.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/07_cartoon_watched`
14. **Exit the braindance to proceed to the next section.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/08_leave_school`
15. **Relive the braindance.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/10_relive_bd_nc`
16. **Scan for clues.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/find`
17. **Follow Harris in his braindances.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/follow`
18. **Scan for clues.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/get_there`
19. **Look for clues to help find Randy.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/bd/09_texas_clues`
20. **Relive the braindance.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/bd/hospital`
21. **Watch the BD to the end.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/bd/05a_watch_school_optional`
22. **Free Randy.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/06_pull_pipe`
   - Map pin: ref `#sq021_mp_pipe`; position `2475.0119628906, -1369.0986328125, 64.710388183594`
23. **Look around the barn.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/07_look_around`
24. **Return to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/08_go_back_river`
25. **Wait for instructions from River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/09_wait_river`
26. **Disable security on the computer.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/finale/10_security_computer`
27. **Help River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/11_help_river`
   - Map pin: ref `#sq021_mp_pipe`; position `2475.0119628906, -1369.0986328125, 64.710388183594`
28. **Return to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/22_go_back_to_river`
29. **Find a way into the barn.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/barn`
30. **Find the farm's security control system.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/finale/security`
   - Map pin: ref `#sq021_tr_security_mp`; position `2405.2844238281, -1364.544921875, 61.839183807373`
31. **Go to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/lift`
32. **Turn off the braindance machine.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/stop_bd`
33. **Help the other victims.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/finale/victims`
34. **NCPD boy in blue gives you a holler and you come runnin' like an obedient dog? This ain't gonna become a habit is it? Well, whatever – sounds like he's got an errand for you, real personal kind. Least it's better than chasing dead politicians. Just do me a favor – don't get used to it.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/001_talk_river_start`
35. **Wait for the coordinates from River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/01_wait_for_coordinates`
36. **Find braindances of Peter Pan in the lab.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/04_find_braindance`
37. **Return to River's car.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/05_go_back_to_car`
38. **Talk to Yawen Packard.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/05_go_to_mitsuko`
39. **Go to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/07_come_closer`
40. **Meet with River Ward in the evening.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/11_go_to_crossing`
   - Map pin: ref `#sq021_lab_crossing_marker`; position `-1484.8664550781, -620.62664794922, 7.868344783783`
41. **Read the message from River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/12_read_the_message`
42. **Get in River's car.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/13_get_in_the_car`
43. **So some depraved maniac's kidnapping boys, and lo and behold, your badge is caught up in the middle of it. Gotta be honest, this doesn't look good. Peter Pan's just another manifestation of this fucked up city – probably already ended those poor brats. But on the off-chance Randy's still alive... If I were you, I'd go save him. Especially if "breaking the law" is involved.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/14_leave_car`
44. **Follow River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/15_follow_river`
45. **Get inside the lab.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/16_get_into_the_lab`
46. **Use Kiroshi to find the right cabinet.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/17_look_for_a_room`
47. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/18_talk_river`
48. **Find the braindances of Anthony Harris.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/19_find_bd`
49. **Search the cabinets.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/20_help_river`
50. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/21_talk_river`
51. **Return to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/22_go_back_to_river`
52. **Sit and wait for River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/23_wait_for_river`
   - Map pin: ref `#sq021_lab_sit_and_wait`; position `-1470.5183105469, -673.99249267578, 8.2819566726685`
53. **Wait for River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/24_wait_for_river`
54. **Search the room.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/car`
55. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/learn`
56. **Talk to Johnny.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/hook/meet`
57. **Find a way inside the lab.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/hook/hook`
58. **Talk to Joss.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/08_talk_joss`
59. **Sit at the computer.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/11_sit_by_computer`
60. **Get Harris's IP address.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/randys_room/10_check_ip`
61. **Check the cartoon in the file folder.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/09_check_file`
62. **View the page Randy mentioned.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/12_check_web`
63. **Click on the image on the Drugs Are Bad site.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/13_click_link`
64. **Go through Anthony Harris's hidden page.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/14_search_hidden_page`
65. **Wait for River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/15_wait_river`
66. **Gain access to Randy's computer.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/16_hack_laptop`
67. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/17_talk_river`
68. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/closer`
69. **Follow River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/go_to`
70. **Open the locked cabinet.**  
   `Optional` · `quests/side_quest/sq021_sick_dreams/randys_room/drawer`
71. **Look for clues to help find Randy.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/investigation`
   - Map pin: ref `#sq021_mp_tp_randy_trailer`; position `1216.5900878906, -501.03103637695, 37.429981231689`
72. **Follow River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/joss`
73. **Search Randy's computer for his activity on the Net.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/messages`
74. **Learn the password to the computer.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/randys_room/password`
75. **Get out of the car.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/04_leave_car`
76. **Wait for River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/06_wait_for_river`
77. **Return to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/22_go_back_to_river`
78. **Check out the barn.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/barn`
79. **Drive to the farm with River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/car`
80. **Get to River's car.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/car1`
81. **Defeat all enemies.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/revenge/follow`
82. **Ride with River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/ride/02_drive_river`
83. **Talk to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/ride/learn`
84. **Listen to River.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/ride_back/listen`
85. **Watch the recording.**  
   `Primary` · `quests/side_quest/sq021_sick_dreams/ride_back/plug_computer`

## The Prophet's Song

- IGN walkthrough: [The Prophet's Song](https://www.ign.com/wikis/cyberpunk-2077/The_Prophet%27s_Song)
- Vanilla type: `MinorQuest`
- Quest hash: `444138064`
- Quest path: `quests/minor_quest/mq026_conspiracy`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`, `combat/neutralize`

### Objective sequence

1. **A clandestine meeting of reptilians at midnight? V, we're not missing this. If you want answers to the questions plaguing humankind for eons, this might be your only shot. Is there life in the cosmos? Is there anyone pulling the strings? If so, why? And why the fuck do they let all this evil shit happen? And to think the Universe's greatest secrets could be found in some old factory in our humble little Night City...**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_01_find_stash`
2. **Return to the old factory.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_01b_return_factory`
3. **Defeat the conspirators.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_02_find_stash`
4. **Keep a lookout.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_02a_suspicious`
5. **Search the body.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_03_loot_corpse`
6. **Confront the conspirators before they leave.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_04_confront`
7. **Find somewhere to hide.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_05_hide`
8. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_05a_talk`
9. **Wait until dusk.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_05b_wait`
10. **Seize the conspirators' chip.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_06b_take_out_carrier`
11. **Show the mystery chip to the prophet.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_07_return`
   - Map pin: ref `#mq026_mp_prophet`; position `-1554.5659179688, 1197.3286132813, 17.150201797485`
12. **Talk to the prophet's disciple.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_07b_disciple`
13. **Ask the prophet's disciple about the chip.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_08_what`
14. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq026_conspiracy/stash/01_09_johnny`

## There Is A Light That Never Goes Out

- IGN walkthrough: [There Is A Light That Never Goes Out](https://www.ign.com/wikis/cyberpunk-2077/There_Is_A_Light_That_Never_Goes_Out)
- Vanilla type: `SideQuest`
- Quest hash: `3215414478`
- Quest path: `quests/side_quest/sq023_bd_passion`
- District: Santo Domingo
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `follow/escort`, `wait/time gate`, `vehicle sequence`

### Objective sequence

1. **Get in the NCPD vehicle.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/enter`
2. **Return to the car.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/exit`
3. **Follow Joshua Stephenson.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/follow_joshua`
4. **Follow Zuleikha.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/follow_zuleikha`
5. **Go inside the house.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/meet`
6. **Talk to Zuleikha.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/talk`
7. **Wait for Joshua.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/glorias_house/wait_4_joshua`
8. **Talk to Joshua.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/restaurant/enjoy`
9. **Sit down at the table in PieZ.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/restaurant/goto`
10. **Exit the car.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/restaurant/leave_car`
11. **Talk to Rachel.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/restaurant/spear`
12. **Talk to Johnny.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/restaurant/tlk_johnny`
13. **I love these WTF situations. A guy hires you to off some other guy, and then that first guy dies, but then the second guy hires you to go somewhere with him for who the fuck knows what. But hey, it's not like you're short on work. Just don't fuck this one up, OK? I know you wanna know how this all plays out.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/ride/01_ride_to_gloria`
14. **I love these WTF situations. A guy hires you to off some other guy, and then that first guy dies, but then the second guy hires you to go somewhere with him for who the fuck knows what. But hey, it's not like you're short on work. Just don't fuck this one up, OK? I know you wanna know how this all plays out.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/ride/enter_limo_start`
15. **Ride with Joshua.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/ride/just_ride`
16. **Talk to Joshua.**  
   `Primary` · `quests/side_quest/sq023_bd_passion/ride/ride`

## These Boots Are Made for Walkin'

- IGN walkthrough: [These Boots Are Made For Walkin'](https://www.ign.com/wikis/cyberpunk-2077/These_Boots_Are_Made_For_Walkin%27)
- Vanilla type: `MinorQuest`
- Quest hash: `3369099861`
- Quest path: `quests/minor_quest/mq042_nomad`
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `travel/reach location`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `vehicle sequence`

### Objective sequence

1. **Here you thought your old ride was totaled for good – yet here you are now. Like a phoenix from the ashes, it lives again. But how? Why now? You'd already closed that chapter of kickin' up sand with nomads out in the desert… But I mean, it'd be stupid if you didn't check it out... right? You never can underestimate the past. Because it sure as shit likes to take revenge.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone`
2. **Go to the indicated location.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location`
   - Map pin: ref `#mq042_nomad_spwn_v_nomad_car`; position `1396.7999267578, -1726.2445068359, 49.540004730225`
3. **Look under the hood.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood`
   - Map pin: ref `#mq042_nomad_mk_hood`; position `1397.0856933594, -1724.7124023438, 49.906402587891`
4. **Check the engine.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/02b_inspect_the_engine`
   - Map pin: ref `#mq042_nomad_mk_hood`; position `1397.0856933594, -1724.7124023438, 49.906402587891`
5. **Close the hood.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/02c_close_the_hood`
   - Map pin: ref `#mq042_nomad_mk_hood`; position `1397.0856933594, -1724.7124023438, 49.906402587891`
6. **Scan your old car.**  
   `Optional` · `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car`
   - Map pin: ref `#mq042_nomad_mk_hood`; position `1397.0856933594, -1724.7124023438, 49.906402587891`
7. **Talk to the stranger.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger`
8. **Confront the stranger.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/03a_confront_stranger`
9. **Get in your old car.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car`
   - Map pin: ref `#mq042_nomad_spwn_v_nomad_car`; position `1396.7999267578, -1726.2445068359, 49.540004730225`
10. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/05_talk_with_johnny`
11. **Return to the landfill.**  
   `Primary` · `quests/minor_quest/mq042_nomad/mq042_nomad/06_get_back`
   - Map pin: ref `#mq042_mp_dumpster_zone`; position `1391.0098876953, -1726.6900634766, 49.200004577637`

## They Won't Go When I Go

- IGN walkthrough: [They Won't Go When I Go](https://www.ign.com/wikis/cyberpunk-2077/They_Won%27t_Go_When_I_Go)
- Vanilla type: `SideQuest`
- Quest hash: `78612194`
- Quest path: `quests/side_quest/sq023_real_passion`
- District: Westbrook
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Take the hammer and nail.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/15_take_hammer`
   - Map pin: ref `#sq023_mk_bd_hammer`; position `-151.61685180664, 1161.0737304688, 66.362998962402`
2. **Take part in the crucifixion.**  
   `Optional` · `quests/side_quest/sq023_real_passion/objectives/participate_optional`
3. **Wait by the cross.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/audience`
   - Map pin: ref `#sq023_mk_cross_place`; position `-153.59819030762, 1157.4337158203, 65.794357299805`
4. **Talk to Rachel.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/bd_director`
5. **Talk to Vasquez.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/find_vasquez`
6. **Go inside the braindance studio.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/getinside`
7. **Help Joshua record the BD.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/join`
8. **Stay with Joshua until he dies.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/joshua_on_the_cross`
9. **Leave the braindance studio.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/leave_studio`
   - Map pin: ref `#sq023_mk_leave`; position `-162.14233398438, 1129.7763671875, 65.406890869141`
10. **Nail Joshua to the cross.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/nail`
11. **Stay with Joshua until he dies.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/participate`
12. **Raise the cross.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/rise`
   - Map pin: ref `#sq023_mk_bd_button`; position `-156.56890869141, 1157.5098876953, 66.39608001709`
13. **Sit on the chair.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/sit`
14. **Talk to Joshua Stephenson.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/talk`
15. **Well, whaddaya know. This corpo-slut from the crucifixion BD wants you to come back to give her star a pep talk, massage his fucking shoulders and whatnot. Normally I'd tell you to drop it, find something more fun to do, but... I dunno, seems like this Jesus freak could really use your help.**  
   `Primary` · `quests/side_quest/sq023_real_passion/objectives/talk_wakako`

## Tune Up

- IGN walkthrough: [Tune Up](https://www.ign.com/wikis/cyberpunk-2077/Tune_Up)
- Vanilla type: `SideQuest`
- Quest hash: `4277885699`
- Quest path: `quests/side_quest/sq025_compensation`
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`

### Objective sequence

1. **Fender benders are a dime a dozen in Night City. A Delamain though? A first, I'm guessing. But now he wants to hand out compensation for damages? That's just downright suspect. Way I see it, he's got the AI equivalent of a gun pointed at his head, and this message is nothing but a coded cry for help. Nobody, and I mean nobody, doles out compensation for a little chipped paintwork. Go and see what this is about – worst case you come out a little richer.**  
   `Primary` · `quests/side_quest/sq025_compensation/01_hook/01_01_collect_reward`
   - Map pin: ref `#sq025_mp_delamain_garage_entrance`; position `-943.82696533203, -81.245407104492, 9.0097923278809`
2. **Go inside Delamain HQ.**  
   `Primary` · `quests/side_quest/sq025_compensation/01_hook/01_02_get_inside`
   - Map pin: ref `#sq025_mp_delamain_garage_entrance`; position `-943.82696533203, -81.245407104492, 9.0097923278809`
3. **Talk to the receptionist.**  
   `Primary` · `quests/side_quest/sq025_compensation/01_hook/01_02_receptionist`
   - Map pin: ref `#sq025_mp_delamain_garage_receptionist`; position `-945.54071044922, -86.671997070313, 9.366003036499`

## Venus in Furs

- IGN walkthrough: [Venus in Furs](https://www.ign.com/wikis/cyberpunk-2077/Venus_in_Furs)
- Vanilla type: `MinorQuest`
- Quest hash: `275936375`
- Quest path: `quests/main_quest/prologue/q003_stout`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`

### Objective sequence

1. **Meredith Stout invited you over to her room at the No-Tell Motel? Shit, V, don't know whether to give you props or talk you out of it... Either way, you're telling me your secret for picking up corpo chicks.**  
   `Primary` · `quests/main_quest/prologue/q003_stout/stout/01_go_to_notell`
   - Map pin: ref `#q003_mp_no_tell_stout`; position `-1201.9061279297, 1330.9293212891, 21.269653320313`
2. **Spend the night at the No-Tell Motel.**  
   `Primary` · `quests/main_quest/prologue/q003_stout/stout/02_enjoy_evening`
3. **Talk to Meredith Stout.**  
   `Primary` · `quests/main_quest/prologue/q003_stout/stout/02_meet_militech1`

## Violence

- IGN walkthrough: [Violence](https://www.ign.com/wikis/cyberpunk-2077/Violence)
- Vanilla type: `MinorQuest`
- Quest hash: `3632722309`
- Quest path: `quests/minor_quest/mq019_paparazzi`
- District: Watson
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `wait/time gate`, `search/investigate`, `hack/breach/download`, `deliver/deposit item`, `leave/escape area`

### Objective sequence

1. **Unknown number, anonymous client, a secret hotel meet-up… The aura of mystery 'round this one's so thick I need a machete to hack my way through it. Wonder what'll happen next… and what that means for you.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/00_hook/01_read_message`
2. **Meet with the mysterious client at No-Tell Motel.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/01_notell_motel/01_go_to_notell_motel`
   - Map pin: ref `#mq019_mp_notell_motel`; position `-1159.2006835938, 1333.6895751953, 20.074811935425`
3. **Talk to the client.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/01_notell_motel/02_talk_with_client`
4. **Sit down.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/01_notell_motel/02a_sit_down`
   - Map pin: ref `#mq019_01_ch_sit_down`; position `-1200.0101318359, 1314.9245605469, 28.516519546509`
5. **Wait for a message from Lizzy Wizzy.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/00_suspend_quest`
6. **Go to Riot in the evening and ask for Liam.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/01_go_to_riot`
7. **Find proof of Liam's betrayal.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/02_find_liam`
8. **Break into Riot's security room.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/02b_break_into_security`
9. **Confront Liam.**  
   `Optional` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/03a_confront_liam`
10. **Check the security computer.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/02c_check_computer`
11. **Check the cameras linked to the computer.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/02d_check_cameras`
12. **Ask about Liam.**  
   `Optional` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/02_ask_about_liam`
13. **Go to the VIP area.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/03_check_vip_lounge`
14. **Escape the VIP area.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/03b_defeat_security`
15. **Leave the VIP area.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/03b_leave_vip_lounge`
16. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/04_talk_with_johnny`
17. **Steal the club's surveillance data.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/03_riot_night_club/05_steal_recordings`
18. **Call Lizzy.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/05_holocall/01_call_client`
19. **Send the stolen data.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/05_holocall/02_send_data`
20. **Answer Lizzy.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/06_finale/01_pick_up`
21. **Go to the motel room.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/06_finale/02_go_to_notell`
   - Map pin: ref `#mq019_tr_enter_room`; position `-1199.4786376953, 1323.7839355469, 28`
   - Map pin: ref `#mq019_tr_notell_motel`; position `-1157.9732666016, 1333.8671875, 19.980003356934`
22. **Talk to Lizzy.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/06_finale/03_talk_with_client`
23. **Get rid of body.**  
   `Primary` · `quests/minor_quest/mq019_paparazzi/06_finale/04_move_body`
24. **Ask Lizzy about Liam's injuries.**  
   `Optional` · `quests/minor_quest/mq019_paparazzi/06_finale/04a_ask_about_wounds`

## War Pigs

- IGN walkthrough: [War Pigs](https://www.ign.com/wikis/cyberpunk-2077/War_Pigs)
- Vanilla type: `MinorQuest`
- Quest hash: `479196099`
- Quest path: `quests/minor_quest/mq041_corpo`
- District: Watson
- Level: 60
- Candidate building blocks: `meet/contact conversation`, `interact/use device`

### Objective sequence

1. **A voice from beyond the grave, the promise of dirt on old enemies… I'll admit, I'm a little curious. But in your shoes, I'd be careful with this one. Corpos are like wasps – they can sting even after they're dead.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase`
   - Map pin: ref `#mq041_mk_dumpster`; position `-1136.7600097656, 1841.4602050781, 36.209999084473`
2. **Talk to Johnny.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny`
3. **Move the dumpster.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/01b_lift_the_dumpster`
   - Map pin: ref `#mq041_mk_dumpster`; position `-1136.7600097656, 1841.4602050781, 36.209999084473`
4. **Open the briefcase.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/02_open_the_briefcase`
5. **Talk to the stranger.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger`
6. **Confront Frank.**  
   `Primary` · `quests/minor_quest/mq041_corpo/corpo/04_confront_frank`
7. **Talk to Johnny.**  
   `Optional` · `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1`

## With a Little Help from My Friends

- IGN walkthrough: [With a Little Help From My Friends](https://www.ign.com/wikis/cyberpunk-2077/With_a_Little_Help_From_My_Friends)
- Vanilla type: `SideQuest`
- Quest hash: `2148266169`
- Quest path: `quests/side_quest/sq027_01_basilisk_convoy`
- District: Badlands
- Level: 60
- Candidate building blocks: `phone/message contact`, `meet/contact conversation`, `travel/reach location`, `follow/escort`, `wait/time gate`, `search/investigate`, `interact/use device`, `retrieve/collect item`, `combat/neutralize`, `vehicle sequence`, `leave/escape area`

### Objective sequence

1. **The great nomad saga continues: Panam's up to something. That girl just doesn't know when to quit – and my God, I love her for it. You don't seem to know either, considering you wanna go back out there. Maybe you could save us all some time, pitch a tent out in the desert? Think we both know this isn't just about the job anymore.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/01_go_to_snake_nation_camp`
   - Map pin: ref `#sq027_mp_nomad_camp`; position `3433.2463378906, -359.65631103516, 138.05485534668`
2. **The great nomad saga continues: Panam's up to something. That girl just doesn't know when to quit – and my God, I love her for it. You don't seem to know either, considering you wanna go back out there. Maybe you could save us all some time, pitch a tent out in the desert? Think we both know this isn't just about the job anymore.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/02_talk_to_panam`
3. **Follow Panam and Mitch.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/03_follow_panam`
4. **Drive over to the veterans.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/03a_join_nomads_in_car`
   - Map pin: ref `#sq027_mp_nomad_camp_departure`; position `3390.1381835938, -436.45355224609, 130.31210327148`
5. **Wait for the nomads.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/03b_wait_for_nomads`
6. **Get in Panam's car.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/03c_get_in_panam_car`
7. **Talk to Panam and the veterans.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/04_talk_to_panam_2`
8. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/talk_to_panam_phone`
9. **The great nomad saga continues: Panam's up to something. That girl just doesn't know when to quit – and my God, I love her for it. You don't seem to know either, considering you wanna go back out there. Maybe you could save us all some time, pitch a tent out in the desert? Think we both know this isn't just about the job anymore.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/01_nomad_camp/000_call_panam_back`
10. **Wait for a message from Saul.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/01_wait_for_saul_call`
11. **Tell Saul about Panam's plan.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/00_talk_to_saul`
12. **Reply to Saul's message.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/01a_respond_to_saul`
13. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/02_talk_to_panam`
14. **Call Panam back.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/02a_call_panam`
15. **Pick up the car from the Sunset Motel.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/03_retrieve_car`
   - Map pin: ref `#sq027_mp_nomad_car_reward`; position `1713.0908203125, -754.27917480469, 50.526351928711`
16. **Go to the train station.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/01_travel_to_junction`
   - Map pin: ref `#sq027_mp_junction`; position `3004.3232421875, -1819.9840087891, 102.03853607178`
17. **Get out of the car.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/01a_leave_car`
18. **Find the entrance to the control tower.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03a_find_entrance`
   - Map pin: ref `#sq027_mp_approach_generic`; position `3033.2836914063, -1843.4342041016, 108.98974609375`
   - Map pin: ref `#sq027_mp_approach_solo`; position `3015.7780761719, -1851.0018310547, 115.5797958374`
19. **Find a punch card.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03b_search_punchcard`
20. **Take the punchcard.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03c_pickup_punchcard`
21. **Join the nomads at the junction.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/05_join_nomads_downstairs`
   - Map pin: ref `#sq027_mp_junction`; position `3004.3232421875, -1819.9840087891, 102.03853607178`
22. **Talk to Carol.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/02_talk_to_huxley`
23. **Look at the stars.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/05a_look_at_stars`
24. **Scan the generator.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/04_scan_transformer`
25. **Talk to Bob and Mitch.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/04_talk_to_bob_and_mitch`
26. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/02_talk_to_panam`
27. **Discuss the plan with the nomads.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03_talk_to_panam`
28. **Go up the control tower.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03a_talk_panam`
   - Map pin: ref `#sq027_mp_tower_top`; position `3025.3930664063, -1838.9392089844, 113.80265045166`
29. **Talk to the nomads.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/talk_to_the_nomads`
30. **Activate the locomotive from the control panel.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03d_activate_locomotive`
   - Map pin: ref `#sq027_mp_locomotive_controls`; position `3017.5522460938, -1846.7736816406, 114.52934265137`
31. **Talk to Teddy and Cassidy.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/04_talk_to_teddy_cassidy`
32. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03e_talk_to_panam_view`
33. **Talk to the veterans by the campfire.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/05_camp_with_nomads`
34. **Wait for the nomads to take their positions.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/wait_for_place`
35. **Defeat the Militech escort.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/defeat_escorts`
36. **Shoot at the train car coupler.**  
   `Optional` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/shoot_clamp`
37. **Escort the trucks to the nomad camp.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/defend_convoy`
   - Map pin: ref `#sq027_05a_sm_transport_delivered`; position `3371.4772949219, -343.24829101563, 133.50538635254`
38. **Get in the vehicle.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/get_in_car`
39. **Get in position and wait for the nomads.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/get_in_position`
40. **Follow the train.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/intercept_the_convoy`
41. **Join Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/03_ambush/join_panam`
42. **Talk to Panam.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/04_return/talk_to_panam`
43. **Meet with Saul.**  
   `Primary` · `quests/side_quest/sq027_01_basilisk_convoy/04_return/talk_to_saul`
