# Gig: Going Up or Down?

Journal: `quests/street_stories/heywood/glen/sts_hey_gle_05` · `StreetStory` · hash `940686843`.

Journal premise: Gig type: Thievery\nObjective: Scandium rods\nLocation: Megabuilding H1, Congress St.\nDetails:\n\nThis isn't your run-of-the-mill gig. Client this time is me. You know the H1 megabuilding in the Glen? City within a city – crumbling tower of concrete and faulty wiring. That it hasn't already collapsed is thanks to a guy named El Gallo. Brilliant techie, he was. Past tense.\n\nIt's the same old story. El Gallo's got a drug problem. A big one. He's completely lost touch with reality, goes from one score of syn-coke to another. Needless to say, he's in no state to repair any creaky doors. But for some reason he got it into his head that everything'll be better if he could just get his hands on some scandium rods, so he stole them from a corpo warehouse.\n\nThese rods are rare parts. Rare and very expensive. I wouldn't want to see them go to waste. Go to H1 (access code's already taken care of) and get them from El Gallo before that junkie pawns them. I don't care how you do it, so long as it gets done.

**Coverage: journal-linked.** 57 exact journal-linked nodes in 5 resources; 10 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Neutralize El Gallo. (Optional) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` |
| Talk to El Gallo. (Optional) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` |
| Deposit scandium rods in the Drop Point. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` |
| Go to El Gallo's workshop. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` |
| Go outside. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave` |
| Look for the scandium rods. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` |
| Take the scandium rods from the cache. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts` |
| Steal the scandium rods. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_05_combat.questphase / h247 / 25` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 24:Out → 25:Failed |
| `sts_hey_gle_05_openworld.questphase / h292 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 54:True → 3:Active; 3:Out → 104:In1 |
| `sts_hey_gle_05_openworld.questphase / h292 / 5` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 4:Out → 5:Succeeded; 5:Out → 168:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 8` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 60:Out → 8:Succeeded; 8:Out → 178:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 9` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05` | 87:Out → 9:Succeeded; 9:Out → 108:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 55` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 54:False → 55:Active; 55:Out → 104:In2 |
| `sts_hey_gle_05_openworld.questphase / h292 / 58` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 115:Out → 58:Active; 58:Out → 60:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 82` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave` | 98:Out → 82:Active; 82:Out → 166:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 84` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave` | 179:Out → 84:Succeeded; 84:Out → 85:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 85` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` | 84:Out → 85:Active; 85:Out → 128:In; 85:Out → 183:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 87` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` | 87:Out → 9:Succeeded; 183:Out → 87:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 107` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/brief` | 101:Out → 107:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 113` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 113:Out → 56:In; 119:False → 113:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 114` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 56:Out → 114:Succeeded; 114:Out → 172:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 115` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 115:Out → 58:Active; 120:False → 115:Failed |
| `sts_hey_gle_05_openworld.questphase / h292 / 116` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 116:Out → 98:In; 176:Out → 116:Inactive |
| `sts_hey_gle_05_openworld.questphase / h292 / 157` (Condition) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 83:Out → 157:In; 157:True → 158:Inactive |
| `sts_hey_gle_05_openworld.questphase / h292 / 158` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 157:True → 158:Inactive |
| `sts_hey_gle_05_openworld.questphase / h292 / 168` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 5:Out → 168:Active; 168:Out → 57:In; 168:Out → 64:In; 168:Out → 112:In; 168:Out → 146:In; 168:Out → 149:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 169` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 64:Out → 169:Succeeded; 169:Out → 175:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 170` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 150:Out1 → 170:Succeeded; 170:Out → 171:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 171` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 170:Out → 171:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 172` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 114:Out → 172:Succeeded; 172:Out → 174:Inactive |
| `sts_hey_gle_05_openworld.questphase / h292 / 173` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts` | 189:False → 173:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 174` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 172:Out → 174:Inactive; 174:Out → 189:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 175` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 169:Out → 175:Succeeded; 175:Out → 176:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 176` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts` | 176:Out → 116:Inactive; 175:Out → 176:Succeeded |
| `sts_hey_glenn.questphase / h1466 / 25` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 24:Out → 25:Failed |
| `sts_hey_glenn.questphase / h9908 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 54:True → 3:Active; 3:Out → 104:In1 |
| `sts_hey_glenn.questphase / h9908 / 5` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 4:Out → 5:Succeeded; 5:Out → 168:Active |
| `sts_hey_glenn.questphase / h9908 / 8` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 60:Out → 8:Succeeded; 8:Out → 178:In |
| `sts_hey_glenn.questphase / h9908 / 9` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05` | 87:Out → 9:Succeeded; 9:Out → 108:In |
| `sts_hey_glenn.questphase / h9908 / 55` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find` | 54:False → 55:Active; 55:Out → 104:In2 |
| `sts_hey_glenn.questphase / h9908 / 58` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 115:Out → 58:Active; 58:Out → 60:In |
| `sts_hey_glenn.questphase / h9908 / 82` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave` | 98:Out → 82:Active; 82:Out → 166:In |
| `sts_hey_glenn.questphase / h9908 / 84` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave` | 179:Out → 84:Succeeded; 84:Out → 85:Active |
| `sts_hey_glenn.questphase / h9908 / 85` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` | 84:Out → 85:Active; 85:Out → 128:In; 85:Out → 183:In |
| `sts_hey_glenn.questphase / h9908 / 87` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` | 87:Out → 9:Succeeded; 183:Out → 87:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 107` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/brief` | 101:Out → 107:Active |
| `sts_hey_glenn.questphase / h9908 / 113` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 113:Out → 56:In; 119:False → 113:Active |
| `sts_hey_glenn.questphase / h9908 / 114` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 56:Out → 114:Succeeded; 114:Out → 172:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 115` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 115:Out → 58:Active; 120:False → 115:Failed |
| `sts_hey_glenn.questphase / h9908 / 116` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo` | 116:Out → 98:In; 176:Out → 116:Inactive |
| `sts_hey_glenn.questphase / h9908 / 157` (Condition) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 83:Out → 157:In; 157:True → 158:Inactive |
| `sts_hey_glenn.questphase / h9908 / 158` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill` | 157:True → 158:Inactive |
| `sts_hey_glenn.questphase / h9908 / 168` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 5:Out → 168:Active; 168:Out → 57:In; 168:Out → 64:In; 168:Out → 112:In; 168:Out → 146:In; 168:Out → 149:In |
| `sts_hey_glenn.questphase / h9908 / 169` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 64:Out → 169:Succeeded; 169:Out → 175:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 170` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 150:Out1 → 170:Succeeded; 170:Out → 171:Active |
| `sts_hey_glenn.questphase / h9908 / 171` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 170:Out → 171:Active |
| `sts_hey_glenn.questphase / h9908 / 172` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores` | 114:Out → 172:Succeeded; 172:Out → 174:Inactive |
| `sts_hey_glenn.questphase / h9908 / 173` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts` | 189:False → 173:Active |
| `sts_hey_glenn.questphase / h9908 / 174` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 172:Out → 174:Inactive; 174:Out → 189:In |
| `sts_hey_glenn.questphase / h9908 / 175` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk` | 169:Out → 175:Succeeded; 175:Out → 176:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 176` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts` | 176:Out → 116:Inactive; 175:Out → 176:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 304` (Condition) | `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver` | 205:False → 304:In; 304:False → 210:In; 216:Out → 304:In; 304:True → 305:In |
| `open_world_bugfixing.questphase / h1127 / 14` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05` | 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 14` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_05` | 13:True → 14:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_05_combat.questphase / h79 / 16` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene`; `#sts_sm_hey_gle_05_el_gallo_conversation` | 16:gle_05_gallo_spotted_end → 15:In; 18:False → 16:gle_05_gallo_spotted_start |
| `sts_hey_gle_05_combat.questphase / h184 / 16` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene`; `#sts_sm_hey_gle_05_el_gallo_scene` | 21:False → 16:sequence_start |
| `sts_hey_gle_05_combat.questphase / h247 / 4` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene`; `#sts_sm_hey_gle_05_el_gallo_conversation` | 4:gle_05_gallo_combat_end → 1:In; 30:Success → 4:gle_05_gallo_vision_start; 4:gle_05_gallo_no_combat_end → 5:In; 4:gle_05_gallo_escape_end → 16:In |
| `sts_hey_gle_05_combat.questphase / h414 / 28` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene`; `#sts_sm_hey_gle_05_el_gallo_conversation` | 15:Out → 28:gle_05_gallo_lights_start |
| `sts_hey_gle_05_openworld.questphase / h83 / 5` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene`; `#sts_sm_hey_gle_05_opening_scene` | 3:Out → 5:homeless_start; 5:homeless_end → 8:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 44` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene`; `#sts_sm_hey_gle_05_holocall_debriefs` | 44:End 0 → 15:In; 57:False → 44:Start 0; 44:rejected_out → 56:Active; 44:Holocall INT → 46:In; 44:Holocall RET → 45:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 177` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene`; `#sts_sm_hey_gle_05_holocall_prebrief` | 177:End 0 → 145:Active; 177:rejected_out → 145:Active; 180:True → 177:Start 0; 177:Holocall INT → 182:In; 177:Holocall RET → 181:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase` / h0 / 4 | `sts_hey_gle_05_combat.questphase` | 8: Condition: gle_05_finished; 8:False → 4:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h9590 / 4 | `sts_hey_gle_05_combat.questphase` | 8: Condition: gle_05_finished; 8:False → 4:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase` / h0 / 3 | `sts_hey_gle_05_openworld.questphase` | 8: Condition: gle_05_finished; 3:Out1 → 1:In; 8:False → 3:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h9590 / 3 | `sts_hey_gle_05_openworld.questphase` | 8: Condition: gle_05_finished; 3:Out1 → 1:In; 8:False → 3:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h79 / 16 | `sts_hey_gle_05_el_gallo_conversation.scene` | 18: Condition: gle_05_talked; 16:gle_05_gallo_spotted_end → 15:In; 18:False → 16:gle_05_gallo_spotted_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h247 / 4 | `sts_hey_gle_05_el_gallo_conversation.scene` | 30: UseWorkspot; 4:gle_05_gallo_combat_end → 1:In; 30:Success → 4:gle_05_gallo_vision_start; 4:gle_05_gallo_no_combat_end → 5:In; 4:gle_05_gallo_escape_end → 16:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h414 / 28 | `sts_hey_gle_05_el_gallo_conversation.scene` | 15: MovePuppet; 15:Out → 28:gle_05_gallo_lights_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h1298 / 16 | `sts_hey_gle_05_el_gallo_conversation.scene` | 18: Condition: gle_05_talked; 16:gle_05_gallo_spotted_end → 15:In; 18:False → 16:gle_05_gallo_spotted_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h1466 / 4 | `sts_hey_gle_05_el_gallo_conversation.scene` | 30: UseWorkspot; 4:gle_05_gallo_combat_end → 1:In; 30:Success → 4:gle_05_gallo_vision_start; 4:gle_05_gallo_no_combat_end → 5:In; 4:gle_05_gallo_escape_end → 16:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h1633 / 28 | `sts_hey_gle_05_el_gallo_conversation.scene` | 15: MovePuppet; 15:Out → 28:gle_05_gallo_lights_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h184 / 16 | `sts_hey_gle_05_el_gallo_scene.scene` | 21: Condition: gle_05_start_talk; 21:False → 16:sequence_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h1403 / 16 | `sts_hey_gle_05_el_gallo_scene.scene` | 21: Condition: gle_05_start_talk; 21:False → 16:sequence_start |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h124 / 44 | `sts_hey_gle_05_holocall_debriefs.scene` | 57: Condition; 44:End 0 → 15:In; 57:False → 44:Start 0; 44:rejected_out → 56:Active; 44:Holocall INT → 46:In; 44:Holocall RET → 45:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h9740 / 44 | `sts_hey_gle_05_holocall_debriefs.scene` | 57: Condition; 44:End 0 → 15:In; 57:False → 44:Start 0; 44:rejected_out → 56:Active; 44:Holocall INT → 46:In; 44:Holocall RET → 45:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 177 | `sts_hey_gle_05_holocall_prebrief.scene` | 180: Condition; 177:End 0 → 145:Active; 177:rejected_out → 145:Active; 180:True → 177:Start 0; 177:Holocall INT → 182:In; 177:Holocall RET → 181:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h9908 / 177 | `sts_hey_gle_05_holocall_prebrief.scene` | 180: Condition; 177:End 0 → 145:Active; 177:rejected_out → 145:Active; 180:True → 177:Start 0; 177:Holocall INT → 182:In; 177:Holocall RET → 181:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h83 / 5 | `sts_hey_gle_05_opening_scene.scene` | 3: PauseCondition: #gle_05_tr_homeless; 3:Out → 5:homeless_start; 5:homeless_end → 8:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h9699 / 5 | `sts_hey_gle_05_opening_scene.scene` | 3: PauseCondition: #gle_05_tr_homeless; 3:Out → 5:homeless_start; 5:homeless_end → 8:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.quest` / h0 / 0 | `sts_hey_glenn.questphase` | 2: FactsDBManager: debug_sts_start; 2:Out → 0:In1 |
| `base\open_world\street_stories\heywood\sts_heywood.questphase` / h0 / 2 | `sts_hey_glenn.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.quest` / h0 / 11 | `sts_hey_gle_05.questphase` | 1: Start; 11:Out1 → 0:In; 1:Out → 11:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h0 / 14 | `sts_hey_gle_05.questphase` | 42: Journal; 50: Journal; 42:Out → 14:In1; 50:Out → 14:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 4 | `sts_heywood.questphase` | 0: Input; 21: Input; 0:Out → 4:In1; 21:Out → 4:sts_hey_rey_02_bugfixing |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 4 | `bugfixing.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:Out_res_act1 → 14:In; 4:to_mq025 → 6:to_mq025; 4:sq026_02_signal → 5:sq026_02_signal; 9:Out1 → 4:In1; 21:Out → 4:In1; 4:CYB-656199 → 15:In; 4:ep1_active_out → 23:In |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 44 | `bugfixing.questphase` | 11: Start; 11:Out → 44:In1 |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 47 | `bugfixing.questphase` | 0: Start; 0:Out → 47:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 76 | `bugfixing.questphase` | 0: Start; 0:Out → 76:In1 |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 23 | `bugfixing.questphase` | 0: Start; 0:Out → 23:In1 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 140 | `bugfixing.questphase` | 0: Start; 0:Out → 140:In1 |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 5 | `bugfixing.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1:Out1 → 5:In1; 1:conspiracy_out → 5:In1; 1:combat_out → 5:In1; 1:death_out → 5:In1 |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 61 | `bugfixing.questphase` | 0: Start; 0:Out → 61:In1 |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 20 | `bugfixing.questphase` | 0: Start; 0:Out → 20:In1 |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 68 | `bugfixing.questphase` | 49: Phase; 49:additional_content_out → 68:In1 |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 64 | `bugfixing.questphase` | 0: Start; 0:Out → 64:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 13 | `bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 13:In1 |
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\metro\ue_metro\ue_metro.quest` / h0 / 21 | `open_world_content.questphase` | 0: Start; 0:Out → 21:EP1_Standalone |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest` / h0 / 7 | `open_world_content.questphase` | 8: Scene: ma_bls_ina_07_chicken.scene; 8:start → 7:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_std_arr_tier_1; 2:Out → 3:In1 |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 4 | `open_world_content.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 4:In1 |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_wat_nid_tier_1; 2:Out → 3:In1 |
| `base\open_world\open_world_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\police_system\police_system_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` / h0 / 4 | `open_world_content.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 19 | `open_world_content.questphase` | 0: Input; 36: Input; 0:Out → 19:In1; 36:Out → 19:EP1_Standalone |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 10 | `additional_game_elements.questphase` | 1: Start; 1:Out → 10:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_bls_ina_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_bls_ina_tier_1; 4:Out → 6:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_cct_dtn_tier_1; 4:Out → 5:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_cct_dtn_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: Scene: ma_hey_spr_04_00_chickentest.scene; 4:End 0 → 6:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_hey_spr_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: ma_pac_cvi_08_00_chickentest.scene; 3:End 0 → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_pac_cvi_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest` / h0 / 3 | `additional_game_elements.questphase` | 2: Scene: mq_std_rcr_11_00_chickentest.scene; 2:End 0 → 3:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 6 | `additional_game_elements.questphase` | 1: Start; 1:Out → 6:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest` / h0 / 7 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 7:Input |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: Scene: ma_wat_lch_06_chicken_test.scene; 3:End 0 → 2:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: FactsDBManager: ow_psychos_intro_done; 9:Out → 8:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest` / h0 / 6 | `additional_game_elements.questphase` | 8: LogicalHub; 8:Out1 → 6:Input |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 20 | `additional_game_elements.questphase` | 25: LogicalHub; 25:Out1 → 20:Input |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 29 | `additional_game_elements.questphase` | 11: Start; 11:Out → 29:Input |
| `base\quest\main_quests\epilogue\q202\q202.quest` / h0 / 22 | `additional_game_elements.questphase` | 0: Start; 0:Out → 22:Input |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 30 | `additional_game_elements.questphase` | 27: FactsDBManager: q204_var_test_def; 27:Out → 30:Input |
| `base\quest\main_quests\epilogue\q204\q204_reborn.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 30 | `additional_game_elements.questphase` | 0: Start; 0:Out → 30:Input |
| `base\quest\main_quests\part1\q103\q103.quest` / h0 / 45 | `additional_game_elements.questphase` | 0: Start; 0:Out → 45:Input |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 40 | `additional_game_elements.questphase` | 58: LogicalHub; 58:Out1 → 40:Input |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\main_quests\part1\q113\q113.quest` / h0 / 40 | `additional_game_elements.questphase` | 36: FactsDBManager: q113_active; 36:Out → 40:Input |
| `base\quest\main_quests\part1\q114\q114_nomads.quest` / h0 / 16 | `additional_game_elements.questphase` | 0: Start; 0:Out → 16:Input |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 57 | `additional_game_elements.questphase` | 0: Start; 0:Out → 57:Input |
| `base\quest\main_quests\prologue\q000\q000.quest` / h0 / 10 | `additional_game_elements.questphase` | 2: Start; 2:Out → 10:Input |
| `base\quest\main_quests\prologue\q001\q001.quest` / h0 / 30 | `additional_game_elements.questphase` | 120: LogicalHub; 120:Out1 → 30:Input |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 26 | `additional_game_elements.questphase` | 0: Start; 0:Out → 26:Input |
| `base\quest\main_quests\prologue\q004\q004.quest` / h0 / 1087 | `additional_game_elements.questphase` | 24: Start; 24:Out → 1087:Input |
| `base\quest\main_quests\prologue\q005\q005_heist.quest` / h0 / 14 | `additional_game_elements.questphase` | 17: FactsDBManager: jackie_default_on write/default comparison 0; 17:Out → 14:Input |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 12 | `additional_game_elements.questphase` | 3: Scene: mq000_00_chickentest.scene; 3:out → 12:Input |
| `base\quest\minor_quests\mq001\mq001.quest` / h0 / 10 | `additional_game_elements.questphase` | 21: Start; 21:Out → 10:Input |
| `base\quest\minor_quests\mq003\mq003_orbitals.quest` / h0 / 7 | `additional_game_elements.questphase` | 2: Start; 2:Out → 7:Input |
| `base\quest\minor_quests\mq006\mq006.quest` / h0 / 7 | `additional_game_elements.questphase` | 6: Scene: mq006_chicken_test.scene; 6:End 0 → 7:Input |
| `base\quest\minor_quests\mq007\mq007.quest` / h0 / 10 | `additional_game_elements.questphase` | 0: Start; 0:Out → 10:Input |
| `base\quest\minor_quests\mq008\mq008.quest` / h0 / 14 | `additional_game_elements.questphase` | 0: Start; 0:Out → 14:Input |
| `base\quest\minor_quests\mq011\mq011.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq012\mq012.quest` / h0 / 9 | `additional_game_elements.questphase` | 1: Start; 1:Out → 9:Input |
| `base\quest\minor_quests\mq013\mq013.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\minor_quests\mq014\mq014.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\minor_quests\mq015\mq015_wizardbook.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq017\mq017_streetkid.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq018\mq018.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Phase: mq018_00_chickentest.questphase; 1:additional_content_out → 5:Input |
| `base\quest\minor_quests\mq019\mq019_paparazzi.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq021\mq021.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq022\mq022.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` / h0 / 11 | `additional_game_elements.questphase` | 1: Start; 1:Out → 11:Input |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.quest` / h0 / 4 | `additional_game_elements.questphase` | 10: FactsDBManager: disable_tutorials; 10:Out → 4:Input |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq028\mq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq028_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq030\mq030.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `base\quest\minor_quests\mq033\mq033_tarot.quest` / h0 / 2 | `additional_game_elements.questphase` | 0: Start; 0:Out → 2:Input |
| `base\quest\minor_quests\mq035\mq035_ozob.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: Scene: mq035_chicken_test.scene; 4:start → 5:Input |
| `base\quest\minor_quests\mq037\mq037_brendan.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\minor_quests\mq038\mq038.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq040\mq040_biosculpt.quest` / h0 / 10 | `additional_game_elements.questphase` | 22: Condition: mq040_add_ele_on Equal 1; 22:True → 10:Input |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq048\mq048.quest` / h0 / 12 | `additional_game_elements.questphase` | 1: Start; 1:Out → 12:Input |
| `base\quest\minor_quests\mq055\mq055.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: mq055_chicken.scene; 3:End 0 → 4:EP1_Standalone |
| `base\quest\side_quests\sq004\sq004_riders_quest.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq006\sq006.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq011\sq011.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 6 | `additional_game_elements.questphase` | 2: Start; 2:Out → 6:Input |
| `base\quest\side_quests\sq017\sq017.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\side_quests\sq018\sq018.quest` / h0 / 24 | `additional_game_elements.questphase` | 16: Start; 16:Out → 24:Input |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\side_quests\sq024\sq024.quest` / h0 / 29 | `additional_game_elements.questphase` | 0: Start; 0:Out → 29:Input |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 66 | `additional_game_elements.questphase` | 49: Phase; 49:additional_content_out → 66:Input |
| `base\quest\side_quests\sq026\sq026.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 8 | `additional_game_elements.questphase` | 0: Start; 0:Out → 8:Input |
| `base\quest\side_quests\sq028\sq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\side_quests\sq029\sq029.quest` / h0 / 20 | `additional_game_elements.questphase` | 1: Start; 1:Out → 20:Input |
| `base\quest\side_quests\sq030\sq030.quest` / h0 / 11 | `additional_game_elements.questphase` | 4: SceneManager; 4:Out → 11:Input |
| `base\quest\side_quests\sq031\sq031.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\side_quests\sq032\sq032.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 11 | `additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 11:Input |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 20 | `additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 20:EP1_Standalone |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Start; 1:Out → 5:Input |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: PauseCondition: q306_DEBUG_useBaseGameAdditionalGameElements; 9:Out → 8:Input |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 3:Input; 10:CutSource → 3:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 7 | `additional_game_elements.questphase` | 1: Start; 1:Out → 7:Input |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 2 | `additional_game_elements.questphase` | 0: Input; 0:Out → 2:Input |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 3:Input |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_hey_gle_05_el_gallo_conversation.scene` | gle_05_gallo_vision_start, gle_05_gallo_non_vision_start, gle_05_gallo_lights_start, gle_05_gallo_spotted_start → gle_05_gallo_combat_end, gle_05_gallo_no_combat_end, gle_05_gallo_lights_end, gle_05_gallo_spotted_end, gle_05_gallo_escape_end | gallo; Player; 71 nodes / 81 edges |
| `sts_hey_gle_05_el_gallo_scene.scene` | sequence_start →  | #gle_05_ws_gallo; Player; 8 nodes / 8 edges |
| `sts_hey_gle_05_holocall_debriefs.scene` | Start 0 → End 0, rejected_out | padre; 23 nodes / 30 edges |
| `sts_hey_gle_05_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | padre; 22 nodes / 25 edges |
| `sts_hey_gle_05_opening_scene.scene` | homeless_start → homeless_end | homeless_001; Player; 3 nodes / 2 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_hey_gle_05_el_gallo_conversation.scene / n3 / 0` | Let's talk. (`Option`) | No option-level predicate stored | 0:0 → 47:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n38 / 0` | You won't get anything fixed in that state. (`drugged`) | No option-level predicate stored | 0:0 → 40:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n38 / 1` | My client gave me the green light to end you. (`padre`) | No option-level predicate stored | 0:1 → 43:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n38 / 2` | I'll tell you how to fix them without rods. (`elevator`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "buildId": "85601791440", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 53:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n57 / 0` | Keep talking like that. (`yuor problem`) | No option-level predicate stored | 0:0 → 59:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n57 / 1` | Nope, none at all. (`no i dont`) | No option-level predicate stored | 0:1 → 62:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n113 / 0` | You have scandium rods, right? (`parts`) | {"questCondition": {"$type": "questObjectCondition", "type": {"$type": "questInventory_ConditionType", "itemID": "151969226370"}}} | 0:0 → 36:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n113 / 1` | Hey, relax. (`calm`) | No option-level predicate stored | 0:1 → 50:0:0 |
| `sts_hey_gle_05_el_gallo_conversation.scene / n113 / 2` | Nothing. Just leaving. (`Escape`) | No option-level predicate stored | 0:2 → 122:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `#gle_05_combat` | sts_hey_gle_05_combat.questphase / h664 / 16; sts_hey_gle_05_combat.questphase / h79 / 15; sts_hey_gle_05_combat.questphase / h79 / 5 | sts_hey_gle_05_el_gallo_conversation.scene / scene / 24 |
| `gle_05_el_gallo_killed` | sts_hey_gle_05_openworld.questphase / h292 / 178; sts_hey_glenn.questphase / h9908 / 178 | No reader in selected context |
| `gle_05_escape` | sts_hey_gle_05_el_gallo_conversation.scene / scene / 122 | sts_hey_gle_05_el_gallo_conversation.scene / scene / 119 |
| `gle_05_finished` | sts_hey_gle_05_openworld.questphase / h292 / 108; sts_hey_glenn.questphase / h9908 / 108 | open_world_bugfixing.questphase / h1127 / 13; open_world_bugfixing.questphase / h2262 / 13 |
| `gle_05_lighs_off` | sts_hey_gle_05_combat.questphase / h414 / 46 | sts_hey_gle_05_combat.questphase / h683 / 12 |
| `gle_05_start` | sts_hey_gle_05_openworld.questphase / h292 / 101; sts_hey_glenn.questphase / h9908 / 101 | No reader in selected context |
| `gle_05_start_talk` | sts_hey_gle_05_el_gallo_conversation.scene / scene / 129 | sts_hey_gle_05_combat.questphase / h184 / 15; sts_hey_gle_05_combat.questphase / h184 / 21; sts_hey_gle_05_combat.questphase / h79 / 23; sts_hey_gle_05_combat.questphase / h79 / 24; sts_hey_gle_05_openworld.questphase / h292 / 112; sts_hey_glenn.questphase / h9908 / 112 |
| `gle_05_talked` | sts_hey_gle_05_combat.questphase / h247 / 5; sts_hey_gle_05_el_gallo_conversation.scene / scene / 467 | sts_hey_gle_05_combat.questphase / h79 / 18; sts_hey_gle_05_openworld.questphase / h292 / 56; sts_hey_glenn.questphase / h9908 / 56 |
| `gle_05_track` | Producer outside selected context | sts_hey_gle_05_openworld.questphase / h292 / 54; sts_hey_glenn.questphase / h9908 / 54 |
| `hey_achievement` | sts_hey_gle_05_openworld.questphase / h124 / 34 | sts_hey_gle_05_openworld.questphase / h124 / 47 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_hey_gle_05_holocall_prebrief.scene / scene / 281 |
| `holo_padre_calls_v_end_activate` | sts_hey_gle_05_holocall_debriefs.scene / scene / 68; sts_hey_gle_05_holocall_prebrief.scene / scene / 68; sts_hey_gle_05_openworld.questphase / h124 / 46; sts_hey_gle_05_openworld.questphase / h292 / 182 | No reader in selected context |
| `holo_padre_calls_v_end_done` | sts_hey_gle_05_holocall_debriefs.scene / scene / 64; sts_hey_gle_05_holocall_prebrief.scene / scene / 64 | sts_hey_gle_05_holocall_debriefs.scene / scene / 63; sts_hey_gle_05_holocall_prebrief.scene / scene / 63 |
| `holo_padre_calls_v_rejectable` | sts_hey_gle_05_holocall_debriefs.scene / scene / 280; sts_hey_gle_05_holocall_prebrief.scene / scene / 254; sts_hey_gle_05_holocall_prebrief.scene / scene / 287 | No reader in selected context |
| `holo_padre_calls_v_rejected` | sts_hey_gle_05_holocall_debriefs.scene / scene / 282; sts_hey_gle_05_holocall_prebrief.scene / scene / 256 | sts_hey_gle_05_holocall_debriefs.scene / scene / 284; sts_hey_gle_05_holocall_prebrief.scene / scene / 258 |
| `holo_padre_calls_v_start_activate` | sts_hey_gle_05_holocall_debriefs.scene / scene / 270; sts_hey_gle_05_holocall_debriefs.scene / scene / 67; sts_hey_gle_05_holocall_prebrief.scene / scene / 285; sts_hey_gle_05_holocall_prebrief.scene / scene / 67; sts_hey_gle_05_openworld.questphase / h124 / 45; sts_hey_gle_05_openworld.questphase / h292 / 181 | sts_hey_gle_05_holocall_debriefs.scene / scene / 257 |
| `holo_padre_calls_v_start_done` | sts_hey_gle_05_holocall_debriefs.scene / scene / 62; sts_hey_gle_05_holocall_prebrief.scene / scene / 62 | sts_hey_gle_05_holocall_debriefs.scene / scene / 249; sts_hey_gle_05_holocall_prebrief.scene / scene / 269 |
| `holo_setup_active` | Producer outside selected context | sts_hey_gle_05_holocall_debriefs.scene / scene / 257; sts_hey_gle_05_holocall_prebrief.scene / scene / 281 |
| `holo_setup_started` | Producer outside selected context | sts_hey_gle_05_holocall_debriefs.scene / scene / 257; sts_hey_gle_05_holocall_prebrief.scene / scene / 281 |
| `sts_hey_gle_05_scandium_cores` | Producer outside selected context | sts_hey_gle_05_openworld.questphase / h292 / 183; sts_hey_glenn.questphase / h9908 / 183 |

## Exact gates, joins and cancellation

<details><summary>109 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_05_combat.questphase / h7 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 7:Out → 1:In; 16:Out → 7:In; 7:Out → 15:In; 7:Out → 17:In; 7:Out → 18:In |
| `sts_hey_gle_05_combat.questphase / h59 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 35:In; 35:Out → 34:In |
| `sts_hey_gle_05_combat.questphase / h79 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]}}}}` | 0:Out → 2:In; 2:Out → 5:In |
| `sts_hey_gle_05_combat.questphase / h79 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_elevator"}}` | 0:Out → 13:In; 13:Out → 25:In |
| `sts_hey_gle_05_combat.questphase / h79 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_talked"}}}` | 18:False → 16:gle_05_gallo_spotted_start; 25:Out → 18:In |
| `sts_hey_gle_05_combat.questphase / h79 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 19:In; 19:Out → 5:In |
| `sts_hey_gle_05_combat.questphase / h79 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAim_ConditionType","preciseAiming":true,"targetRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]}}}}` | 21:Out → 5:In; 23:Out → 21:In |
| `sts_hey_gle_05_combat.questphase / h79 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 0:Out → 23:In; 23:Out → 21:In; 23:Out → 26:In |
| `sts_hey_gle_05_combat.questphase / h79 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 24:False → 1:In; 5:Out → 24:In |
| `sts_hey_gle_05_combat.questphase / h79 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"isInstant":false}}}` | 13:Out → 25:In; 25:Out → 18:In |
| `sts_hey_gle_05_combat.questphase / h79 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]}}}}` | 26:Out → 5:In; 23:Out → 26:In |
| `sts_hey_gle_05_combat.questphase / h184 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_talk_start"}}` | 0:Out → 8:In; 8:Out → 13:In |
| `sts_hey_gle_05_combat.questphase / h184 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 8:Out → 13:In; 13:Out → 17:In |
| `sts_hey_gle_05_combat.questphase / h184 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 15:Out → 14:In; 17:Out → 15:In; 22:Out1 → 15:In |
| `sts_hey_gle_05_combat.questphase / h184 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 17:Out → 18:In; 18:Out → 21:In |
| `sts_hey_gle_05_combat.questphase / h184 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 21:False → 16:sequence_start; 18:Out → 21:In |
| `sts_hey_gle_05_combat.questphase / h247 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `sts_hey_gle_05_combat.questphase / h247 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]}}}}` | 2:Out → 3:In; 3:Out → 27:In |
| `sts_hey_gle_05_combat.questphase / h247 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 16:Out → 17:In; 17:Out → 24:In |
| `sts_hey_gle_05_combat.questphase / h354 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 41:In; 41:Out → 40:In |
| `sts_hey_gle_05_combat.questphase / h354 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 43:Out → 42:In; 44:Out → 43:In |
| `sts_hey_gle_05_combat.questphase / h354 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 45:Out → 44:In; 47:Out → 45:In |
| `sts_hey_gle_05_combat.questphase / h370 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"isPlayer":false,"percent":70.0,"comparisonType":"LessOrEqual"}}}` | 2:Out → 1:In; 3:Out → 2:In |
| `sts_hey_gle_05_combat.questphase / h370 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 0:Out → 3:In; 3:Out → 2:In |
| `sts_hey_gle_05_combat.questphase / h414 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 14:In; 14:Out → 56:In |
| `sts_hey_gle_05_combat.questphase / h414 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 47:Success → 31:In; 31:Out → 33:In |
| `sts_hey_gle_05_combat.questphase / h414 / 33` | `questCutControlNodeDefinition` `{}` | 33:Out → 22:In; 33:CutSource → 23:CutDestination; 31:Out → 33:In |
| `sts_hey_gle_05_combat.questphase / h414 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":2}}}` | 35:Out → 9:In; 42:Out → 35:In; 35:Out → 55:In |
| `sts_hey_gle_05_combat.questphase / h414 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 9:Out → 24:In; 24:Out → 25:In |
| `sts_hey_gle_05_combat.questphase / h414 / 55` | `questCutControlNodeDefinition` `{}` | 35:Out → 55:In; 55:CutSource → 36:CutDestination; 55:Out → 47:In |
| `sts_hey_gle_05_combat.questphase / h664 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_05_area_halon","deviceControllerClass":"VentilationAreaControllerPS","deviceConditionFunction":"IsAreaActive"}}}` | 0:Out → 15:In; 15:Out → 16:In |
| `sts_hey_gle_05_combat.questphase / h683 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","minutes":1}}}` | 2:Out → 4:In; 4:Out → 3:In |
| `sts_hey_gle_05_combat.questphase / h683 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","minutes":1}}}` | 3:Out → 5:In; 5:Out → 6:In1 |
| `sts_hey_gle_05_combat.questphase / h683 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_lighs_off"}}}` | 0:Out → 12:In; 12:Out → 1:In |
| `sts_hey_gle_05_openworld.questphase / h12 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_initialization"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 12:Out → 6:In; 13:Out → 12:In |
| `sts_hey_gle_05_openworld.questphase / h83 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_homeless"}}` | 0:Out → 3:In; 3:Out → 5:homeless_start |
| `sts_hey_gle_05_openworld.questphase / h83 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_com","names":["#gle_05_homeless_001"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 6:In; 6:Out → 7:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 15:Out → 14:In; 44:End 0 → 15:In; 56:Out → 15:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_05_tr_despawn"}}` | 43:Out → 26:In; 48:Out → 43:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 48:Out → 43:In; 49:Out → 48:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 54:Out → 53:In; 53:Out → 55:In |
| `sts_hey_gle_05_openworld.questphase / h124 / 57` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 57:False → 44:Start 0; 55:Out → 57:In; 57:True → 58:In1 |
| `sts_hey_gle_05_openworld.questphase / h292 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 105:Out → 4:In; 4:Out → 5:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 54` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_track"}}}` | 54:True → 3:Active; 101:Out → 54:In; 54:False → 55:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_talked"}}}` | 113:Out → 56:In; 56:Out → 114:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 168:Out → 57:In; 57:Out → 120:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 60:Out → 8:Succeeded; 58:Out → 60:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 168:Out → 64:In; 64:Out → 169:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 166:Out → 83:In; 83:Out → 157:In; 83:Out → 179:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 104` | `questLogicalXorNodeDefinition` `{}` | 3:Out → 104:In1; 55:Out → 104:In2; 104:Out1 → 105:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 168:Out → 112:In; 112:Out → 119:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 119` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 112:Out → 119:In; 119:False → 113:Active |
| `sts_hey_gle_05_openworld.questphase / h292 / 120` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 57:Out → 120:In; 120:False → 115:Failed |
| `sts_hey_gle_05_openworld.questphase / h292 / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_initialization"}}` | 143:Out → 140:In; 145:Out → 140:In; 140:Out → 142:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_05_tr_initialization"}}` | 142:Out → 141:In; 141:Out → 143:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_quest_loot"},"eventType":"Finished"}}}` | 168:Out → 146:In; 146:Out → 150:In2 |
| `sts_hey_gle_05_openworld.questphase / h292 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_quest_loot"}}},{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_look_for_cores"}]}}` | 168:Out → 149:In; 149:Out → 150:In1 |
| `sts_hey_gle_05_openworld.questphase / h292 / 150` | `questLogicalXorNodeDefinition` `{}` | 146:Out → 150:In2; 149:Out → 150:In1; 150:Out1 → 170:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 157` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 83:Out → 157:In; 157:True → 158:Inactive |
| `sts_hey_gle_05_openworld.questphase / h292 / 180` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 180:False → 145:Active; 180:True → 177:Start 0; 187:False → 180:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_hey_gle_05_scandium_cores"}}}` | 85:Out → 183:In; 183:Out → 87:Succeeded |
| `sts_hey_gle_05_openworld.questphase / h292 / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\glenn\\sts_hey_gle_05\\scenes\\sts_hey_gle_05_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 184:Out → 1:In; 144:Out → 184:In |
| `sts_hey_gle_05_openworld.questphase / h292 / 187` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 187:In; 187:False → 180:In; 187:True → 188:In1 |
| `sts_hey_gle_05_openworld.questphase / h292 / 189` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 189:False → 173:Active; 174:Out → 189:In |
| `sts_hey_gle_05_openworld.questphase / h698 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 0:Out → 2:In; 5:Out → 2:In; 2:Out → 3:In |
| `sts_hey_gle_05_openworld.questphase / h698 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 3:Out → 4:In; 4:Out → 5:In |
| `sts_hey_gle_05_openworld.questphase / h698 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 6:In; 6:Out → 8:In |
| `sts_hey_gle_05_openworld.questphase / h698 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 8:Out → 7:In; 7:Out → 9:In |
| `sts_hey_gle_05_el_gallo_conversation.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#gle_05_combat"}}}` | 1:0:0 → 24:0:1; 14:0:0 → 24:0:1; 24:0:0 → 153:0:1 |
| `sts_hey_gle_05_el_gallo_conversation.scene / scene / 119` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_escape"}}}` | 119:0:0 → 238:0:0; 119:0:1 → 5:0:0; 129:0:0 → 119:0:1 |
| `sts_hey_gle_05_el_gallo_scene.scene / scene / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_smoke","activatorRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"isPlayerActivator":false}}` | 43:0:0 → 44:0:1; 44:0:0 → 8:0:0; 118:0:0 → 44:0:1 |
| `sts_hey_gle_05_el_gallo_scene.scene / scene / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_shotgun","activatorRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"isPlayerActivator":false}}` | 8:0:0 → 47:0:1; 47:0:0 → 10:0:0 |
| `sts_hey_gle_05_el_gallo_scene.scene / scene / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_bed","activatorRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"isPlayerActivator":false}}` | 10:0:0 → 50:0:1; 50:0:0 → 52:0:0 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 63:0:0 → 64:0:1; 68:0:0 → 63:0:1 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 61:666:0 → 249:0:1; 249:0:0 → 252:0:0 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":100}}}` | 61:666:0 → 255:0:1; 252:1:0 → 255:0:0; 252:1:0 → 255:1026:0; 255:0:0 → 257:0:1; 273:0:0 → 255:0:1 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 257` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 252:1:0 → 257:0:0; 252:1:0 → 257:1026:0; 255:0:0 → 257:0:1; 257:0:0 → 261:0:1 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 261` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":100}}}` | 252:1:0 → 261:0:0; 252:1:0 → 261:1026:0; 257:0:0 → 261:0:1; 261:0:0 → 267:0:1 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 267` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 261:0:0 → 267:0:1; 267:0:0 → 270:0:1; 267:0:1 → 273:0:0 |
| `sts_hey_gle_05_holocall_debriefs.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 67:0:0 → 284:0:1; 284:0:0 → 282:0:1 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 63:0:0 → 64:0:1; 68:0:0 → 63:0:1 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 67:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 61:666:0 → 269:0:1; 269:0:0 → 272:0:0 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 275` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 61:666:0 → 275:0:1; 272:1:0 → 275:0:0; 275:0:0 → 281:0:1 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 281` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 275:0:0 → 281:0:1; 281:0:0 → 287:0:1; 281:0:1 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_hey_gle_05_holocall_prebrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 272:1:0 → 283:0:0; 281:0:1 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_hey_glenn.questphase / h9908 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 105:Out → 4:In; 4:Out → 5:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 54` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_track"}}}` | 54:True → 3:Active; 101:Out → 54:In; 54:False → 55:Active |
| `sts_hey_glenn.questphase / h9908 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_talked"}}}` | 113:Out → 56:In; 56:Out → 114:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 168:Out → 57:In; 57:Out → 120:In |
| `sts_hey_glenn.questphase / h9908 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_combat_com","names":["#gle_05_ws_gallo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 60:Out → 8:Succeeded; 58:Out → 60:In |
| `sts_hey_glenn.questphase / h9908 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 168:Out → 64:In; 64:Out → 169:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_05_tr_gallo_den"}}` | 166:Out → 83:In; 83:Out → 157:In; 83:Out → 179:In |
| `sts_hey_glenn.questphase / h9908 / 104` | `questLogicalXorNodeDefinition` `{}` | 3:Out → 104:In1; 55:Out → 104:In2; 104:Out1 → 105:In |
| `sts_hey_glenn.questphase / h9908 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_start_talk"}}}` | 168:Out → 112:In; 112:Out → 119:In |
| `sts_hey_glenn.questphase / h9908 / 119` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 112:Out → 119:In; 119:False → 113:Active |
| `sts_hey_glenn.questphase / h9908 / 120` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 57:Out → 120:In; 120:False → 115:Failed |
| `sts_hey_glenn.questphase / h9908 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_quest_loot"},"eventType":"Finished"}}}` | 168:Out → 146:In; 146:Out → 150:In2 |
| `sts_hey_glenn.questphase / h9908 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_05_quest_loot"}}},{"$type":"questTriggerCondition","triggerAreaRef":"#gle_05_tr_look_for_cores"}]}}` | 168:Out → 149:In; 149:Out → 150:In1 |
| `sts_hey_glenn.questphase / h9908 / 150` | `questLogicalXorNodeDefinition` `{}` | 146:Out → 150:In2; 149:Out → 150:In1; 150:Out1 → 170:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 157` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 83:Out → 157:In; 157:True → 158:Inactive |
| `sts_hey_glenn.questphase / h9908 / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_hey_gle_05_scandium_cores"}}}` | 85:Out → 183:In; 183:Out → 87:Succeeded |
| `sts_hey_glenn.questphase / h9908 / 189` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 189:False → 173:Active; 174:Out → 189:In |
| `mq036_quest_bugfixes.questphase / h870 / 205` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/drop","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 202:False → 205:In; 215:Out → 205:In; 205:True → 206:In; 205:False → 304:In |
| `mq036_quest_bugfixes.questphase / h870 / 210` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 210:True → 208:In; 308:Out → 210:In; 304:False → 210:In; 210:False → 211:In |
| `mq036_quest_bugfixes.questphase / h870 / 304` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 205:False → 304:In; 304:False → 210:In; 216:Out → 304:In; 304:True → 305:In |
| `mq036_quest_bugfixes.questphase / h870 / 305` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151969226370","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 304:True → 305:In; 305:True → 308:In; 305:False → 306:In |
| `open_world_bugfixing.questphase / h1127 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_05_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_hey_gle_05_combat.questphase / h7 / 7; sts_hey_gle_05_openworld.questphase / h83 / 6 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sts_hey_gle_05_combat.questphase / h414 / 15 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sts_hey_gle_05_openworld.questphase / h292 / 105; sts_hey_gle_05_openworld.questphase / h292 / 109 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_hey_gle_05_el_gallo_conversation.scene / scene / 113; sts_hey_gle_05_el_gallo_conversation.scene / scene / 3; sts_hey_gle_05_el_gallo_conversation.scene / scene / 38; sts_hey_gle_05_el_gallo_conversation.scene / scene / 57 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | sts_hey_gle_05_combat.questphase / h354 / 39; sts_hey_gle_05_combat.questphase / h370 / 16; sts_hey_gle_05_combat.questphase / h370 / 17; sts_hey_gle_05_combat.questphase / h414 / 22; +1 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_hey_gle_05_combat.questphase / h247 / 23; sts_hey_gle_05_combat.questphase / h247 / 24; sts_hey_gle_05_combat.questphase / h414 / 45; sts_hey_gle_05_combat.questphase / h7 / 16; +5 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1127 / 13; open_world_bugfixing.questphase / h2262 / 13; sts_hey_gle_05_combat.questphase / h184 / 15; sts_hey_gle_05_combat.questphase / h184 / 21; +22 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_hey_gle_05_openworld.questphase / h124 / 31; sts_hey_gle_05_openworld.questphase / h124 / 50; sts_hey_gle_05_openworld.questphase / h292 / 142; sts_hey_gle_05_openworld.questphase / h292 / 143; +3 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 216; sts_hey_gle_05_combat.questphase / h247 / 16; sts_hey_gle_05_combat.questphase / h247 / 27; sts_hey_gle_05_combat.questphase / h354 / 33; +13 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_hey_gle_05_combat.questphase / h683 / 2; sts_hey_gle_05_combat.questphase / h683 / 3; sts_hey_gle_05_combat.questphase / h7 / 17; sts_hey_gle_05_combat.questphase / h7 / 18; +3 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_hey_gle_05_combat.questphase / h664 / 15; sts_hey_gle_05_combat.questphase / h79 / 19; sts_hey_gle_05_openworld.questphase / h292 / 57; sts_hey_gle_05_openworld.questphase / h698 / 6; +1 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_hey_gle_05_combat.questphase / h414 / 35; sts_hey_gle_05_combat.questphase / h683 / 4; sts_hey_gle_05_combat.questphase / h683 / 5; sts_hey_gle_05_openworld.questphase / h124 / 48 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 305; sts_hey_gle_05_el_gallo_conversation.scene / scene / 113; sts_hey_gle_05_openworld.questphase / h292 / 119; sts_hey_gle_05_openworld.questphase / h292 / 120; +6 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1127 / 14; open_world_bugfixing.questphase / h2262 / 14; sts_hey_gle_05_combat.questphase / h247 / 25; sts_hey_gle_05_openworld.questphase / h12 / 5; +55 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | sts_hey_gle_05_combat.questphase / h7 / 15 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `mount_state` | sts_hey_gle_05_combat.questphase / h79 / 26 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | sts_hey_gle_05_combat.questphase / h247 / 5; sts_hey_gle_05_combat.questphase / h414 / 46; sts_hey_gle_05_combat.questphase / h664 / 16; sts_hey_gle_05_combat.questphase / h79 / 15; +30 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_hey_gle_05_openworld.questphase / h292 / 104; sts_hey_gle_05_openworld.questphase / h292 / 150; sts_hey_glenn.questphase / h9908 / 104; sts_hey_glenn.questphase / h9908 / 150 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_hey_gle_05_combat.questphase / h184 / 13; sts_hey_gle_05_combat.questphase / h247 / 17; sts_hey_gle_05_combat.questphase / h354 / 43; sts_hey_gle_05_combat.questphase / h354 / 45; +9 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_hey_gle_05_combat.questphase / h414 / 33; sts_hey_gle_05_combat.questphase / h414 / 55 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_hey_gle_05_openworld.questphase / h124 / 14 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_hey_gle_05_openworld.questphase / h292 / 146; sts_hey_glenn.questphase / h9908 / 146 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_hey_gle_05_combat.questphase / h184 / 16; sts_hey_gle_05_combat.questphase / h247 / 4; sts_hey_gle_05_combat.questphase / h414 / 28; sts_hey_gle_05_combat.questphase / h79 / 16; +3 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_hey_gle_05_combat.questphase / h184 / 18; sts_hey_gle_05_combat.questphase / h184 / 8; sts_hey_gle_05_combat.questphase / h247 / 2; sts_hey_gle_05_combat.questphase / h79 / 13; +16 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_hey_gle_05_combat.questphase / h354 / 41; sts_hey_gle_05_combat.questphase / h414 / 14; sts_hey_gle_05_combat.questphase / h59 / 35; sts_hey_gle_05_openworld.questphase / h292 / 60; +2 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_hey_gle_05_combat.questphase / h247 / 30; sts_hey_gle_05_combat.questphase / h414 / 36; sts_hey_gle_05_combat.questphase / h414 / 47; sts_hey_gle_05_el_gallo_conversation.scene / scene / 228; +18 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_hey_gle_05_combat.questphase / h354 / 42; sts_hey_gle_05_combat.questphase / h354 / 44; sts_hey_gle_05_combat.questphase / h414 / 25; sts_hey_gle_05_combat.questphase / h414 / 9 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` | content candidate; journal anchor | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` | content candidate; journal anchor | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` | content candidate; forward dependency | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene` | content candidate; forward dependency | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene` | content candidate; forward dependency | `base-sts-hey-gle-05` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-gle-05](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-gle-05.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

281 repeated typed/socket path signatures in this selected graph context; 38 distinct direct resource identities; 17 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h7 / 0 -> 16 -> 7 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 67 -> 284 -> 282 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h124 / 49 -> 48 -> 43 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 66 -> 68 -> 63 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 284 -> 282 -> 286 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 62 -> 65 -> 25 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 25 -> 66 -> 68 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h683 / 0 -> 12 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` / scene / 106 -> 69 -> 103 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `c8705a8da51824b73252` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 0 -> 101 -> 54 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 280 -> 67 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 1 -> 280 -> 67 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h0 / 2 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h0 / 3 | `h59` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h59 / 15 | `h79` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h59 / 28 | `h184` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":14,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h59 / 29 | `h247` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h0 / 4 | `h354` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h354 / 28 | `h370` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h354 / 30 | `h414` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h0 / 5 | `h655` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h655 / 3 | `h664` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` / h655 / 6 | `h683` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h0 / 3 | `h76` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h76 / 2 | `h83` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h0 / 4 | `h124` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h0 / 5 | `h292` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 160 | `h698` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest |
| `base\quest\minor_quests\mq000\mq000.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq000\mq000_thank_you.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq001\mq001.gamedef` | content candidate | base\quest\minor_quests\mq001\mq001.quest |
| `base\quest\minor_quests\mq003\mq003_orbitals.gamedef` | content candidate | base\quest\minor_quests\mq003\mq003_orbitals.quest |
| `base\quest\minor_quests\mq006\mq006.gamedef` | content candidate | base\quest\minor_quests\mq006\mq006.quest |
| `base\quest\minor_quests\mq007\mq007.gamedef` | content candidate | base\quest\minor_quests\mq007\mq007.quest |
| `base\quest\minor_quests\mq008\mq008.gamedef` | content candidate | base\quest\minor_quests\mq008\mq008.quest |
| `base\quest\minor_quests\mq011\mq011.gamedef` | content candidate | base\quest\minor_quests\mq011\mq011.quest |
| `base\quest\minor_quests\mq012\mq012.gamedef` | content candidate | base\quest\minor_quests\mq012\mq012.quest |
| `base\quest\minor_quests\mq013\mq013.gamedef` | content candidate | base\quest\minor_quests\mq013\mq013.quest |
| `base\quest\minor_quests\mq014\mq014.gamedef` | content candidate | base\quest\minor_quests\mq014\mq014.quest |
| `base\quest\minor_quests\mq015\mq015_wizardbook.gamedef` | content candidate | base\quest\minor_quests\mq015\mq015_wizardbook.quest |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | base\quest\minor_quests\mq016\mq016_bartmoss.quest |
| `base\quest\minor_quests\mq017\mq017_streetkid.gamedef` | content candidate | base\quest\minor_quests\mq017\mq017_streetkid.quest |
| `base\quest\minor_quests\mq018\mq018.gamedef` | content candidate | base\quest\minor_quests\mq018\mq018.quest |
| `base\quest\minor_quests\mq019\mq019_paparazzi.gamedef` | content candidate | base\quest\minor_quests\mq019\mq019_paparazzi.quest |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | base\quest\minor_quests\mq021\mq021.quest |
| `base\quest\minor_quests\mq022\mq022.gamedef` | content candidate | base\quest\minor_quests\mq022\mq022.quest |
| `base\quest\minor_quests\mq023\mq023_bootleg.gamedef` | content candidate | base\quest\minor_quests\mq023\mq023_bootleg.quest |
| `base\quest\minor_quests\mq024\mq024.gamedef` | content candidate | base\quest\minor_quests\mq024\mq024.quest |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.gamedef` | content candidate | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq028\mq028.gamedef` | content candidate | base\quest\minor_quests\mq028\mq028.quest |
| `base\quest\minor_quests\mq030\mq030.gamedef` | content candidate | base\quest\minor_quests\mq030\mq030.quest |
| `base\quest\minor_quests\mq032\mq032_sacrum.gamedef` | content candidate | base\quest\minor_quests\mq032\mq032_sacrum.quest |
| `base\quest\minor_quests\mq033\mq033_tarot.gamedef` | content candidate | base\quest\minor_quests\mq033\mq033_tarot.quest |
| `base\quest\minor_quests\mq035\mq035_ozob.gamedef` | content candidate | base\quest\minor_quests\mq035\mq035_ozob.quest |
| `base\quest\minor_quests\mq037\mq037_brendan.gamedef` | content candidate | base\quest\minor_quests\mq037\mq037_brendan.quest |
| `base\quest\minor_quests\mq038\mq038.gamedef` | content candidate | base\quest\minor_quests\mq038\mq038.quest |
| `base\quest\minor_quests\mq040\mq040_biosculpt.gamedef` | content candidate | base\quest\minor_quests\mq040\mq040_biosculpt.quest |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | base\quest\minor_quests\mq041\mq041_corpo.quest |
| `base\quest\minor_quests\mq048\mq048.gamedef` | content candidate | base\quest\minor_quests\mq048\mq048.quest |
| `base\quest\minor_quests\mq055\mq055.gamedef` | content candidate | base\quest\minor_quests\mq055\mq055.quest |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest |
| `base\quest\main_quests\prologue\q000\q000.gamedef` | content candidate | base\quest\main_quests\prologue\q000\q000.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q003\q003.gamedef` | content candidate | base\quest\main_quests\prologue\q003\q003.quest |
| `base\quest\main_quests\prologue\q005\q005_heist.gamedef` | content candidate | base\quest\main_quests\prologue\q005\q005_heist.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q103\q103.gamedef` | content candidate | base\quest\main_quests\part1\q103\q103.quest |
| `base\quest\main_quests\part1\q105\q105_main.gamedef` | content candidate | base\quest\main_quests\part1\q105\q105_main.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\open_world\community\heywood\glen\hey_gle_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\pacifica\west_wind_estate\pac_wwd_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\arroyo\std_arr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\rancho_coronado\std_rcr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\little_china\wat_lch_prolog_ow_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\northside\wat_nid_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test_03_02.gamedef` | content candidate | base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq004\sq004_riders_on_the_storm.gamedef` | content candidate | base\quest\side_quests\sq004\sq004_riders_quest.quest |
| `base\quest\side_quests\sq006\sq006.gamedef` | content candidate | base\quest\side_quests\sq006\sq006.quest |
| `base\quest\side_quests\sq011\sq011.gamedef` | content candidate | base\quest\side_quests\sq011\sq011.quest |
| `base\quest\side_quests\sq012\sq012_the_law.gamedef` | content candidate | base\quest\side_quests\sq012\sq012_the_law.quest |
| `base\quest\side_quests\sq017\sq017.gamedef` | content candidate | base\quest\side_quests\sq017\sq017.quest |
| `base\quest\side_quests\sq018\sq018.gamedef` | content candidate | base\quest\side_quests\sq018\sq018.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq024\sq024.gamedef` | content candidate | base\quest\side_quests\sq024\sq024.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq026\sq026.gamedef` | content candidate | base\quest\side_quests\sq026\sq026.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `base\quest\side_quests\sq028\sq028.gamedef` | content candidate | base\quest\side_quests\sq028\sq028.quest |
| `base\quest\side_quests\sq029\sq029.gamedef` | content candidate | base\quest\side_quests\sq029\sq029.quest |
| `base\quest\side_quests\sq030\sq030.gamedef` | content candidate | base\quest\side_quests\sq030\sq030.quest |
| `base\quest\side_quests\sq031\sq031.gamedef` | content candidate | base\quest\side_quests\sq031\sq031.quest |
| `base\quest\side_quests\sq032\sq032.gamedef` | content candidate | base\quest\side_quests\sq032\sq032.quest |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.quest |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05_test_def.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\metro\ue_metro\ue_metro.gamedef` | content candidate | base\open_world\metro\ue_metro\ue_metro.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand__2h_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_el_gallo_conversation\el_gallo.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_el_gallo_conversation\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_el_gallo_scene\el_gallo.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_el_gallo_scene\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_holocall_debriefs\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_holocall_prebrief\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_opening_scene\civ_low_m_05_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\lipsync\en\sts_hey_gle_05_opening_scene\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\big__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__08.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q000\q000_kid_03_back_to_bar\q000__jackie_stand__2h_on_hips__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `#gle_05_combat` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1298 / 5; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1298 / 15; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1883 / 16; 3 total source locations in compressed evidence |
| `gle_05_lighs_off` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1633 / 46; 1 total source locations in compressed evidence |
| `gle_05_talked` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1466 / 5; 1 total source locations in compressed evidence |
| `gle_05_track` | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.quest / h0 / 12; 1 total source locations in compressed evidence |
| `hey_achievement` | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase / h0 / 42; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase / h0 / 34; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase / h89 / 8; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase / h0 / 40; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_padre_calls_v_end_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 54; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 148; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 145; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 146; 77 total source locations in compressed evidence |
| `holo_padre_calls_v_end_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 144; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 213; base\quest\holocalls\padre\padre_holocall.scene / scene / 42; base\quest\holocalls\padre\padre_holocall.scene / scene / 541; 24 total source locations in compressed evidence |
| `holo_padre_calls_v_rejectable` | base\quest\holocalls\padre\padre_holocall.scene / scene / 664; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 283; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 269; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 308; 30 total source locations in compressed evidence |
| `holo_padre_calls_v_rejected` | base\quest\holocalls\padre\padre_holocall.scene / scene / 672; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 287; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 273; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene / scene / 289; 20 total source locations in compressed evidence |
| `holo_padre_calls_v_start_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 53; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 147; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 141; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 143; 93 total source locations in compressed evidence |
| `holo_padre_calls_v_start_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 142; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 212; base\quest\holocalls\padre\padre_holocall.scene / scene / 41; base\quest\holocalls\padre\padre_holocall.scene / scene / 527; 24 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |

NodeRef uses: 172; TweakDB binding uses: 27. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` | 15 / 118 | scnAudioEvent: 1; scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 30; scnLookAtEvent: 9; scnPlaySkAnimEvent: 46; scneventsSocket: 25 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene` | 3 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene` | 1 / 1 | scnDialogLineEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
