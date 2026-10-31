# Gig: The Heisenberg Principle

Journal: `quests/street_stories/watson/little_china/sts_wat_lch_06` · `StreetStory` · hash `4009599336`.

Journal premise: Gig type: Agent Saboteur\nObjective: Destroy the glitter lab\nLocation: Building on Rovinj St.\nDetails\n\nUnless you've been living under a rock, you've heard of Glitter. Word is that if you take it, you're hooked for life, but apparently it's easier to OD on than neo-fentanyl.\n\nIt was only a matter of time before some zit-faced, rich kid fried his skull sponge. Kid's mother was Arati Kapoor, co-owner of the Masala Studios restaurant franchise. Needless to say, she's pretty torn up about it, but she's not the kind to wallow in her grief – she's got a plan.\n\nThe lab where glitter is cooked has to be wiped off the face of the earth. And if some of those dipshits making it expire on the spot? I think you know the answer.\n\nFlicking you the coords now. FYI – the place might be guarded by Tyger Claws.

**Coverage: journal-linked.** 56 exact journal-linked nodes in 6 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 7 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`; `base\quest\demos\handson_2020\handson_2020_little_china.quest`; `base\quest\demos\handson_2020\handson_2020_speed_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Destroy the equipment used to make glitter. (Primary) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` |
| Enter the basement. (Primary) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` |
| Enter the building. (Primary) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` |
| Leave the area. (Primary) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` |
| Find the lab. (Primary) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 12` (Condition) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 12:True → 2:In; 5:Out → 12:In |
| `sts_wat_lch_06_combat.questphase / h250 / 10` (Condition) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 0:Out → 10:In; 10:True → 3:In; 10:False → 11:In |
| `sts_wat_lch_06_combat.questphase / h250 / 11` (PauseCondition) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 11:Out → 3:In; 10:False → 11:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 7` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 29:Out → 7:Active; 7:Out → 12:In; 7:Out → 13:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 8` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 27:Out → 8:Active; 8:Out → 28:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 18` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 31:Out → 18:Active; 18:Out → 19:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 20` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 19:Out → 20:Succeeded; 20:Out → 21:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 21` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06` | 20:Out → 21:Succeeded; 21:Out → 35:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 24` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 3:Out → 24:Active; 24:Out → 5:In; 24:Out → 26:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 27` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 27:Out → 8:Active; 25:Out1 → 27:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 29` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 29:Out → 7:Active; 28:Out → 29:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 31` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_lab` | 16:Out1 → 31:Succeeded; 31:Out → 18:Active |
| `sts_wat_lch_06_openworld.questphase / h30 / 32` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2` | 13:Out → 32:Inactive; 32:Out → 16:In1 |
| `sts_wat_lch_06_openworld.questphase / h30 / 33` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_1` | 12:Out → 33:Inactive; 33:Out → 16:In2 |
| `sts_wat_lch_06_ow.questphase / h76 / 7` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 29:Out → 7:Active; 7:Out → 71:Active; 7:Out → 89:Inactive |
| `sts_wat_lch_06_ow.questphase / h76 / 8` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 150:Out → 8:Active; 8:Out → 28:In |
| `sts_wat_lch_06_ow.questphase / h76 / 18` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 31:Out → 18:Active; 18:Out → 19:In |
| `sts_wat_lch_06_ow.questphase / h76 / 20` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 19:Out → 20:Succeeded; 20:Out → 21:Succeeded |
| `sts_wat_lch_06_ow.questphase / h76 / 21` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06` | 20:Out → 21:Succeeded; 21:Out → 105:In |
| `sts_wat_lch_06_ow.questphase / h76 / 24` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 42:Out → 24:Active; 24:Out → 158:In |
| `sts_wat_lch_06_ow.questphase / h76 / 27` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 159:Out → 27:Succeeded; 27:Out → 157:In |
| `sts_wat_lch_06_ow.questphase / h76 / 29` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 29:Out → 7:Active; 161:Out → 29:Succeeded |
| `sts_wat_lch_06_ow.questphase / h76 / 31` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 31:Out → 18:Active; 130:Out → 31:Succeeded; 143:Out → 31:Succeeded; 31:Out → 154:Succeeded |
| `sts_wat_lch_06_ow.questphase / h76 / 42` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 42:Out → 24:Active; 45:Out → 42:Succeeded |
| `sts_wat_lch_06_ow.questphase / h76 / 43` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 48:True → 43:Active; 43:Out → 45:In |
| `sts_wat_lch_06_ow.questphase / h76 / 49` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 49:Out → 45:In; 48:False → 49:Active |
| `sts_wat_lch_06_ow.questphase / h76 / 84` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2` | 86:Out1 → 84:Active; 84:Out → 87:Inactive |
| `sts_wat_lch_06_ow.questphase / h76 / 87` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/main_room_mappin` | 84:Out → 87:Inactive |
| `sts_wat_lch_06_ow.questphase / h76 / 71` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/main_room_mappin` | 7:Out → 71:Active; 71:Out → 78:In; 71:Out → 79:In; 71:Out → 80:In; 71:Out → 121:In2 |
| `sts_wat_lch_06_ow.questphase / h76 / 89` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2` | 7:Out → 89:Inactive |
| `sts_wat_lch_06_ow.questphase / h76 / 107` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/brief` | 0:Out → 107:Active; 107:Out → 148:In |
| `sts_wat_lch_06_ow.questphase / h76 / 119` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 131:Out1 → 119:Inactive |
| `sts_wat_lch_06_ow.questphase / h76 / 154` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 31:Out → 154:Succeeded |
| `sts_wat_little_china.questphase / h2470 / 10` (Condition) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 0:Out → 10:In; 10:True → 3:In; 10:False → 11:In |
| `sts_wat_little_china.questphase / h2470 / 11` (PauseCondition) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 11:Out → 3:In; 10:False → 11:In |
| `sts_wat_little_china.questphase / h2642 / 7` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 29:Out → 7:Active; 7:Out → 71:Active; 7:Out → 89:Inactive |
| `sts_wat_little_china.questphase / h2642 / 8` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 150:Out → 8:Active; 8:Out → 28:In |
| `sts_wat_little_china.questphase / h2642 / 18` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 31:Out → 18:Active; 18:Out → 19:In |
| `sts_wat_little_china.questphase / h2642 / 20` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out` | 19:Out → 20:Succeeded; 20:Out → 21:Succeeded |
| `sts_wat_little_china.questphase / h2642 / 21` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06` | 20:Out → 21:Succeeded; 21:Out → 105:In |
| `sts_wat_little_china.questphase / h2642 / 24` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 42:Out → 24:Active; 24:Out → 158:In |
| `sts_wat_little_china.questphase / h2642 / 27` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement` | 159:Out → 27:Succeeded; 27:Out → 157:In |
| `sts_wat_little_china.questphase / h2642 / 29` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 29:Out → 7:Active; 161:Out → 29:Succeeded |
| `sts_wat_little_china.questphase / h2642 / 31` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line` | 31:Out → 18:Active; 130:Out → 31:Succeeded; 143:Out → 31:Succeeded; 31:Out → 154:Succeeded |
| `sts_wat_little_china.questphase / h2642 / 42` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 42:Out → 24:Active; 45:Out → 42:Succeeded |
| `sts_wat_little_china.questphase / h2642 / 43` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 48:True → 43:Active; 43:Out → 45:In |
| `sts_wat_little_china.questphase / h2642 / 49` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building` | 49:Out → 45:In; 48:False → 49:Active |
| `sts_wat_little_china.questphase / h2642 / 84` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2` | 86:Out1 → 84:Active; 84:Out → 87:Inactive |
| `sts_wat_little_china.questphase / h2642 / 87` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/main_room_mappin` | 84:Out → 87:Inactive |
| `sts_wat_little_china.questphase / h2642 / 71` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/main_room_mappin` | 7:Out → 71:Active; 71:Out → 78:In; 71:Out → 79:In; 71:Out → 80:In; 71:Out → 121:In2 |
| `sts_wat_little_china.questphase / h2642 / 89` (MappinManager) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2` | 7:Out → 89:Inactive |
| `sts_wat_little_china.questphase / h2642 / 107` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/brief` | 0:Out → 107:Active; 107:Out → 148:In |
| `sts_wat_little_china.questphase / h2642 / 119` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 131:Out1 → 119:Inactive |
| `sts_wat_little_china.questphase / h2642 / 154` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room` | 31:Out → 154:Succeeded |
| `open_world_bugfixing.questphase / h116 / 84` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06` | 40:True → 84:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 84` (Journal) | `quests/street_stories/watson/little_china/sts_wat_lch_06` | 40:True → 84:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wat_lch_06_combat.questphase / h109 / 2` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene`; `#sts_sm_wat_lch_06_chats` | 33:Out → 2:entrance_chat_start; 4:Out → 2:below_chat_001_start; 8:Out → 2:main_hall_chat_start; 2:entrance_chat_end → 26:In; 2:below_chat_001_end → 34:In |
| `sts_wat_lch_06_ow.questphase / h76 / 104` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene`; `#sts_sm_wat_lch_06_holocall_prebrief` | 104:End 0 → 103:Active; 104:rejected_out → 103:Active; 106:True → 104:Start 0; 104:End 0 → 110:In; 104:Holocall INT → 109:In; 104:Holocall RET → 108:In |
| `sts_wat_lch_06_ow.questphase / h902 / 25` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene`; `#sts_sm_wat_lch_06_holocall_debrief` | 25:End 0 → 4:In; 39:False → 25:Start 0; 25:rejected_out → 38:Active; 25:Holocall INT → 27:In; 25:Holocall RET → 26:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_little_china_bugfixing.questphase` / h0 / 20 | `sts_wat_lch_06_bugfixing.questphase` | 19: DeletionMarker; 19:Out → 20:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest` / h0 / 12 | `sts_wat_lch_06_bugfixing.questphase` | 1: Start; 1:Out → 12:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06.questphase` / h0 / 18 | `sts_wat_lch_06_combat.questphase` | 0: Input; 0:Out → 18:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h2548 / 18 | `sts_wat_lch_06_combat.questphase` | 0: Input; 0:Out → 18:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06.questphase` / h0 / 24 | `sts_wat_lch_06_ow.questphase` | 0: Input; 0:Out → 24:In1; 24:Out1 → 16:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h2548 / 24 | `sts_wat_lch_06_ow.questphase` | 0: Input; 0:Out → 24:In1; 24:Out1 → 16:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h109 / 2 | `sts_wat_lch_06_chats.scene` | 33: PauseCondition: #lch_06_tr_entrance_chat_scene; 4: PauseCondition: #lch_06_tr_chat_001; 8: PauseCondition: #lch_06_tr_main_hall; 33:Out → 2:entrance_chat_start; 4:Out → 2:below_chat_001_start; 8:Out → 2:main_hall_chat_start; 2:entrance_chat_end → 26:In; 2:below_chat_001_end → 34:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h2329 / 2 | `sts_wat_lch_06_chats.scene` | 33: PauseCondition: #lch_06_tr_entrance_chat_scene; 4: PauseCondition: #lch_06_tr_chat_001; 8: PauseCondition: #lch_06_tr_main_hall; 33:Out → 2:entrance_chat_start; 4:Out → 2:below_chat_001_start; 8:Out → 2:main_hall_chat_start; 2:entrance_chat_end → 26:In; 2:below_chat_001_end → 34:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h902 / 25 | `sts_wat_lch_06_holocall_debrief.scene` | 39: Condition; 25:End 0 → 4:In; 39:False → 25:Start 0; 25:rejected_out → 38:Active; 25:Holocall INT → 27:In; 25:Holocall RET → 26:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h3468 / 25 | `sts_wat_lch_06_holocall_debrief.scene` | 39: Condition; 25:End 0 → 4:In; 39:False → 25:Start 0; 25:rejected_out → 38:Active; 25:Holocall INT → 27:In; 25:Holocall RET → 26:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h76 / 104 | `sts_wat_lch_06_holocall_prebrief.scene` | 106: Condition; 104:End 0 → 103:Active; 104:rejected_out → 103:Active; 106:True → 104:Start 0; 104:End 0 → 110:In; 104:Holocall INT → 109:In; 104:Holocall RET → 108:In |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h2642 / 104 | `sts_wat_lch_06_holocall_prebrief.scene` | 106: Condition; 104:End 0 → 103:Active; 104:rejected_out → 103:Active; 106:True → 104:Start 0; 104:End 0 → 110:In; 104:Holocall INT → 109:In; 104:Holocall RET → 108:In |
| `base\open_world\street_stories\watson\sts_watson.questphase` / h0 / 3 | `sts_wat_little_china.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 4 | `sts_wat_little_china.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h255 / 5 | `sts_wat_little_china.questphase` | 0: Input; 0:Out → 5:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 34 | `sts_little_china_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 34:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest` / h0 / 9 | `sts_wat_lch_06.questphase` | 10: FactsDBManager: lch_06_testdef; 9:Out1 → 3:In; 10:Out → 9:In1 |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` / h0 / 10 | `sts_wat_lch_06.questphase` | 20: Journal; 45: Journal; 20:Out → 10:In1; 45:Out → 10:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 7 | `sts_watson.questphase` | 0: Input; 0:Out → 7:In1 |
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
| `sts_wat_lch_06_chats.scene` | main_hall_chat_start, entrance_chat_start, below_chat_001_start → main_hall_chat_end, entrance_chat_end, below_chat_001_end | enemy_up; enemy_officer; enemy_1st_room_2; enemy_main_1; enemy_main_2; enemy_main_3; enemy_1st; Player; 13 nodes / 13 edges |
| `sts_wat_lch_06_holocall_debrief.scene` | Start 0 → End 0, rejected_out | fixer; 23 nodes / 30 edges |
| `sts_wat_lch_06_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-622409` | sts_wat_lch_06_bugfixing.questphase / h17 / 4 | sts_wat_lch_06_bugfixing.questphase / h17 / 2 |
| `CYB-653249` | sts_wat_lch_06_bugfixing.questphase / h79 / 7 | sts_wat_lch_06_bugfixing.questphase / h79 / 6 |
| `glossary_glitter` | sts_wat_lch_06_ow.questphase / h76 / 51 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wat_lch_06_holocall_prebrief.scene / scene / 279 |
| `holo_reggie_calls_v_end_activate` | sts_wat_lch_06_holocall_debrief.scene / scene / 68; sts_wat_lch_06_holocall_prebrief.scene / scene / 63; sts_wat_lch_06_ow.questphase / h76 / 109; sts_wat_lch_06_ow.questphase / h902 / 27 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | sts_wat_lch_06_holocall_debrief.scene / scene / 66; sts_wat_lch_06_holocall_prebrief.scene / scene / 59 | sts_wat_lch_06_holocall_debrief.scene / scene / 65; sts_wat_lch_06_holocall_prebrief.scene / scene / 58 |
| `holo_reggie_calls_v_rejectable` | sts_wat_lch_06_holocall_debrief.scene / scene / 279; sts_wat_lch_06_holocall_prebrief.scene / scene / 254; sts_wat_lch_06_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | sts_wat_lch_06_holocall_debrief.scene / scene / 281; sts_wat_lch_06_holocall_prebrief.scene / scene / 256 | sts_wat_lch_06_holocall_debrief.scene / scene / 283; sts_wat_lch_06_holocall_prebrief.scene / scene / 258 |
| `holo_reggie_calls_v_start_activate` | sts_wat_lch_06_holocall_debrief.scene / scene / 260; sts_wat_lch_06_holocall_debrief.scene / scene / 61; sts_wat_lch_06_holocall_prebrief.scene / scene / 283; sts_wat_lch_06_holocall_prebrief.scene / scene / 62; sts_wat_lch_06_ow.questphase / h76 / 108; sts_wat_lch_06_ow.questphase / h902 / 26 | sts_wat_lch_06_holocall_debrief.scene / scene / 254 |
| `holo_reggie_calls_v_start_done` | sts_wat_lch_06_holocall_debrief.scene / scene / 59; sts_wat_lch_06_holocall_prebrief.scene / scene / 57 | sts_wat_lch_06_holocall_debrief.scene / scene / 249; sts_wat_lch_06_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_wat_lch_06_holocall_debrief.scene / scene / 254; sts_wat_lch_06_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wat_lch_06_holocall_debrief.scene / scene / 254; sts_wat_lch_06_holocall_prebrief.scene / scene / 279 |
| `lch_06_cylinders_destroyed_double` | Producer outside selected context | sts_wat_lch_06_openworld.questphase / h30 / 13 |
| `lch_06_cylinders_destroyed_triple` | Producer outside selected context | sts_wat_lch_06_openworld.questphase / h30 / 12 |
| `lch_06_entrance_chat_ends` | sts_wat_lch_06_chats.scene / scene / 7 | No reader in selected context |
| `lch_06_finished` | sts_wat_lch_06_openworld.questphase / h30 / 36; sts_wat_lch_06_ow.questphase / h902 / 3 | open_world_bugfixing.questphase / h116 / 40; open_world_bugfixing.questphase / h2878 / 40 |
| `lch_06_gang_retaliation` | sts_wat_lch_06_combat.questphase / h93 / 9 | sts_wat_lch_06_ow.questphase / h902 / 40 |
| `lch_06_start` | sts_wat_lch_06_ow.questphase / h76 / 50 | sts_wat_lch_06_bugfixing.questphase / h17 / 3; sts_wat_lch_06_openworld.questphase / h7 / 2 |
| `lch_06_testdef` | Producer outside selected context | sts_wat_lch_06_ow.questphase / h76 / 48; sts_wat_little_china.questphase / h2642 / 48 |
| `sts_tygerclaws_retaliation` | sts_wat_lch_06_ow.questphase / h902 / 41 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sts_wat_lch_06_bugfixing.questphase / h0 / 16 |
| `wat_achievement` | sts_wat_lch_06_ow.questphase / h902 / 7 | sts_wat_lch_06_ow.questphase / h902 / 31 |
| `welcome_holocall_skipped` | sts_wat_lch_06_ow.questphase / h76 / 110 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>93 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wat_lch_06_bugfixing.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 17:Out → 16:In |
| `sts_wat_lch_06_bugfixing.questphase / h17 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-622409"}}}` | 0:Out → 2:In; 2:False → 4:In |
| `sts_wat_lch_06_bugfixing.questphase / h17 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_start"}}}` | 4:Out → 3:In; 3:True → 5:In |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 3:Out → 1:In; 2:Out → 3:In; 4:Out → 3:In |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-653249"}}}` | 0:Out → 6:In; 6:False → 7:In |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#lch_06_dvc_lab_appl_triple"}}` | 7:Out → 8:In; 8:Out → 13:In |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement"}}` | 9:False → 4:In; 9:True → 5:In; 13:Out → 9:In |
| `sts_wat_lch_06_bugfixing.questphase / h79 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded","inverted":true}}}` | 12:True → 2:In; 5:Out → 12:In |
| `sts_wat_lch_06_combat.questphase / h7 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_com_combat"},"comparisonParams":{"$type":"questComparisonParam","count":9,"comparisonType":"GreaterOrEqual"}}}}` | 3:Out → 1:In; 5:Out → 3:In; 3:Out → 9:In; 3:Out → 10:In |
| `sts_wat_lch_06_combat.questphase / h93 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#lch_06_dvc_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 5:In; 5:Out → 9:In |
| `sts_wat_lch_06_combat.questphase / h109 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_chat_001"}}` | 0:Out → 4:In; 4:Out → 2:below_chat_001_start |
| `sts_wat_lch_06_combat.questphase / h109 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_entrance_chat"}}` | 0:Out → 5:In; 5:Out → 32:In |
| `sts_wat_lch_06_combat.questphase / h109 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"}}` | 0:Out → 8:In; 8:Out → 2:main_hall_chat_start |
| `sts_wat_lch_06_combat.questphase / h109 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_entrance_chat_scene"}}` | 0:Out → 33:In; 33:Out → 2:entrance_chat_start |
| `sts_wat_lch_06_combat.questphase / h109 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 36:Out → 28:In; 32:Out → 36:In |
| `sts_wat_lch_06_combat.questphase / h250 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement"}}` | 3:False → 1:In; 11:Out → 3:In; 10:True → 3:In; 3:True → 12:In |
| `sts_wat_lch_06_combat.questphase / h250 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_com_combat","names":["#lch_06_ws_above_enemy_002"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 5:In; 5:False → 8:In |
| `sts_wat_lch_06_combat.questphase / h250 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_com_combat","names":["#lch_06_ws_above"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 6:In; 6:False → 7:In |
| `sts_wat_lch_06_combat.questphase / h250 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 10:In; 10:True → 3:In; 10:False → 11:In |
| `sts_wat_lch_06_combat.questphase / h250 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 11:Out → 3:In; 10:False → 11:In |
| `sts_wat_lch_06_openworld.questphase / h7 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_start","value":1,"comparisonType":"GreaterOrEqual"}}}` | 2:Out → 1:In; 3:Out → 2:In |
| `sts_wat_lch_06_openworld.questphase / h30 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement_entered_002"}}` | 24:Out → 5:In; 5:Out → 25:In1 |
| `sts_wat_lch_06_openworld.questphase / h30 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_cylinders_destroyed_triple","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 12:In; 12:Out → 33:Inactive |
| `sts_wat_lch_06_openworld.questphase / h30 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_cylinders_destroyed_double","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 13:In; 13:Out → 32:Inactive |
| `sts_wat_lch_06_openworld.questphase / h30 / 16` | `questLogicalAndNodeDefinition` `{}` | 32:Out → 16:In1; 33:Out → 16:In2; 16:Out1 → 31:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_leaving"}}` | 18:Out → 19:In; 19:Out → 20:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 25` | `questLogicalXorNodeDefinition` `{}` | 5:Out → 25:In1; 26:Out → 25:In2; 25:Out1 → 27:Succeeded |
| `sts_wat_lch_06_openworld.questphase / h30 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement_entered_001"}}` | 24:Out → 26:In; 26:Out → 25:In2 |
| `sts_wat_lch_06_openworld.questphase / h30 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"}}` | 8:Out → 28:In; 28:Out → 29:Succeeded |
| `sts_wat_lch_06_ow.questphase / h12 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_quest_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}}]}}` | 10:Out → 1:In; 4:Out → 10:In |
| `sts_wat_lch_06_ow.questphase / h12 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_quest_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 16:Out → 9:In; 17:Out → 16:In |
| `sts_wat_lch_06_ow.questphase / h76 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#lch_06_tr_area_leave"}}` | 18:Out → 19:In; 19:Out → 20:Succeeded |
| `sts_wat_lch_06_ow.questphase / h76 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"}}` | 8:Out → 28:In; 118:CutSource → 28:CutDestination; 28:Out → 160:In |
| `sts_wat_lch_06_ow.questphase / h76 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_entrance"}}` | 45:Out → 42:Succeeded; 43:Out → 45:In; 49:Out → 45:In; 45:Out → 116:In1 |
| `sts_wat_lch_06_ow.questphase / h76 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_testdef","value":1,"comparisonType":"GreaterOrEqual"}}}` | 48:True → 43:Active; 51:Out → 48:In; 48:False → 49:Active |
| `sts_wat_lch_06_ow.questphase / h76 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_com_combat"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 59:In; 59:Out → 61:In |
| `sts_wat_lch_06_ow.questphase / h76 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#lch_06_tr_building"}}` | 72:Out → 74:In; 74:Out → 73:In |
| `sts_wat_lch_06_ow.questphase / h76 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_building"}}` | 75:Out → 72:In; 73:Out → 75:In; 103:Out → 75:In |
| `sts_wat_lch_06_ow.questphase / h76 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_dvc_lab_appl_triple"}}}}` | 118:CutSource → 78:CutDestination; 71:Out → 78:In; 78:Out → 86:In3 |
| `sts_wat_lch_06_ow.questphase / h76 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_dvc_lab_appl_triple"},"timeInterval":3.0,"angleTolerance":15.0}},{"$type":"questTriggerCondition","triggerAreaRef":"#lch_01_tr_main_computer_room_001"}]}}` | 118:CutSource → 79:CutDestination; 71:Out → 79:In; 79:Out → 86:In2 |
| `sts_wat_lch_06_ow.questphase / h76 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall_002"}}` | 118:CutSource → 80:CutDestination; 71:Out → 80:In; 80:Out → 86:In1 |
| `sts_wat_lch_06_ow.questphase / h76 / 86` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 78:Out → 86:In3; 79:Out → 86:In2; 80:Out → 86:In1; 86:Out1 → 84:Active |
| `sts_wat_lch_06_ow.questphase / h76 / 106` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 106:False → 103:Active; 106:True → 104:Start 0; 162:False → 106:In |
| `sts_wat_lch_06_ow.questphase / h76 / 118` | `questCutControlNodeDefinition` `{}` | 118:CutSource → 28:CutDestination; 118:CutSource → 78:CutDestination; 118:CutSource → 79:CutDestination; 118:CutSource → 80:CutDestination; 143:Out → 118:In |
| `sts_wat_lch_06_ow.questphase / h76 / 121` | `questLogicalXorNodeDefinition` `{}` | 71:Out → 121:In2; 117:Out1 → 121:In1; 121:Out1 → 120:In |
| `sts_wat_lch_06_ow.questphase / h76 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sts_wat_lch_06_sabotage_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 132:Out → 124:In; 124:Out → 126:In |
| `sts_wat_lch_06_ow.questphase / h76 / 130` | `questCutControlNodeDefinition` `{"permanent":true}` | 130:Out → 31:Succeeded; 127:Out → 130:In; 130:Out → 131:In1; 130:CutSource → 143:CutDestination |
| `sts_wat_lch_06_ow.questphase / h76 / 138` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 123:Out → 138:In; 138:Out → 132:In |
| `sts_wat_lch_06_ow.questphase / h76 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\little_china\\sts_wat_lch_06\\scenes\\sts_wat_lch_06_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 139:Out → 1:In; 105:Out → 139:In |
| `sts_wat_lch_06_ow.questphase / h76 / 143` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#lch_06_dvc_lab_appl_triple","deviceControllerClass":"GenericDeviceControllerPS","deviceConditionFunction":"IsDisabled"}}]}}` | 143:Out → 31:Succeeded; 143:Out → 118:In; 130:CutSource → 143:CutDestination; 143:Out → 131:In2; 145:Out → 143:In |
| `sts_wat_lch_06_ow.questphase / h76 / 157` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#lch_06_dvc_lab_appl_triple"}}` | 27:Out → 157:In; 157:Out → 150:In |
| `sts_wat_lch_06_ow.questphase / h76 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement"}}` | 159:Out → 27:Succeeded; 158:Out → 159:In |
| `sts_wat_lch_06_ow.questphase / h76 / 162` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 162:In; 162:True → 103:Active; 162:False → 106:In |
| `sts_wat_lch_06_ow.questphase / h427 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 0:Out → 26:In; 26:Out → 24:In1 |
| `sts_wat_lch_06_ow.questphase / h902 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#lch_06_tr_quest_start"}}` | 28:Out → 8:In; 29:Out → 28:In |
| `sts_wat_lch_06_ow.questphase / h902 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 29:Out → 28:In; 30:Out → 29:In |
| `sts_wat_lch_06_ow.questphase / h902 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 37:Out → 35:In; 35:Out → 39:In |
| `sts_wat_lch_06_ow.questphase / h902 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 39:False → 25:Start 0; 35:Out → 39:In; 39:True → 38:Active |
| `sts_wat_lch_06_ow.questphase / h902 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 40:In; 40:False → 31:In; 40:True → 41:In |
| `sts_wat_lch_06_chats.scene / scene / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\little_china\\sts_wat_lch_06\\scenes\\sts_wat_lch_06_chats.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 1:0:0 → 58:0:1; 58:0:0 → 7:0:1 |
| `sts_wat_lch_06_chats.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\little_china\\sts_wat_lch_06\\scenes\\sts_wat_lch_06_chats.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 9:0:0 → 61:0:1; 61:0:0 → 10:0:0 |
| `sts_wat_lch_06_chats.scene / scene / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\little_china\\sts_wat_lch_06\\scenes\\sts_wat_lch_06_chats.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 26:0:0 → 64:0:1; 64:0:0 → 66:0:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 65:0:0 → 66:0:1; 68:0:0 → 65:0:1 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 58:666:0 → 249:0:1; 249:0:0 → 272:0:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 252` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4,"miliseconds":200}}}` | 58:666:0 → 252:0:1; 252:0:0 → 254:0:1; 262:0:0 → 252:0:1; 272:1:0 → 252:0:0; 272:1:0 → 252:1026:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 252:0:0 → 254:0:1; 254:0:0 → 256:0:1; 272:1:0 → 254:0:0; 272:1:0 → 254:1026:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4,"miliseconds":200}}}` | 254:0:0 → 256:0:1; 256:0:0 → 258:0:1; 272:1:0 → 256:0:0; 272:1:0 → 256:1026:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 258` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 256:0:0 → 258:0:1; 258:0:0 → 260:0:1; 258:0:1 → 262:0:0 |
| `sts_wat_lch_06_holocall_debrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 61:0:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 58:0:0 → 59:0:1; 63:0:0 → 58:0:1 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 62:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 56:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 56:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_lch_06_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_little_china.questphase / h2470 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement"}}` | 3:False → 1:In; 11:Out → 3:In; 10:True → 3:In; 3:True → 12:In |
| `sts_wat_little_china.questphase / h2470 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 10:In; 10:True → 3:In; 10:False → 11:In |
| `sts_wat_little_china.questphase / h2470 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 11:Out → 3:In; 10:False → 11:In |
| `sts_wat_little_china.questphase / h2642 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#lch_06_tr_area_leave"}}` | 18:Out → 19:In; 19:Out → 20:Succeeded |
| `sts_wat_little_china.questphase / h2642 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"}}` | 8:Out → 28:In; 118:CutSource → 28:CutDestination; 28:Out → 160:In |
| `sts_wat_little_china.questphase / h2642 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_entrance"}}` | 45:Out → 42:Succeeded; 43:Out → 45:In; 49:Out → 45:In; 45:Out → 116:In1 |
| `sts_wat_little_china.questphase / h2642 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_testdef","value":1,"comparisonType":"GreaterOrEqual"}}}` | 48:True → 43:Active; 51:Out → 48:In; 48:False → 49:Active |
| `sts_wat_little_china.questphase / h2642 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_dvc_lab_appl_triple"}}}}` | 118:CutSource → 78:CutDestination; 71:Out → 78:In; 78:Out → 86:In3 |
| `sts_wat_little_china.questphase / h2642 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#lch_06_dvc_lab_appl_triple"},"timeInterval":3.0,"angleTolerance":15.0}},{"$type":"questTriggerCondition","triggerAreaRef":"#lch_01_tr_main_computer_room_001"}]}}` | 118:CutSource → 79:CutDestination; 71:Out → 79:In; 79:Out → 86:In2 |
| `sts_wat_little_china.questphase / h2642 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall_002"}}` | 118:CutSource → 80:CutDestination; 71:Out → 80:In; 80:Out → 86:In1 |
| `sts_wat_little_china.questphase / h2642 / 86` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 78:Out → 86:In3; 79:Out → 86:In2; 80:Out → 86:In1; 86:Out1 → 84:Active |
| `sts_wat_little_china.questphase / h2642 / 121` | `questLogicalXorNodeDefinition` `{}` | 71:Out → 121:In2; 117:Out1 → 121:In1; 121:Out1 → 120:In |
| `sts_wat_little_china.questphase / h2642 / 130` | `questCutControlNodeDefinition` `{"permanent":true}` | 130:Out → 31:Succeeded; 127:Out → 130:In; 130:Out → 131:In1; 130:CutSource → 143:CutDestination |
| `sts_wat_little_china.questphase / h2642 / 143` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_main_hall"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#lch_06_dvc_lab_appl_triple","deviceControllerClass":"GenericDeviceControllerPS","deviceConditionFunction":"IsDisabled"}}]}}` | 143:Out → 31:Succeeded; 143:Out → 118:In; 130:CutSource → 143:CutDestination; 143:Out → 131:In2; 145:Out → 143:In |
| `sts_wat_little_china.questphase / h2642 / 157` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#lch_06_dvc_lab_appl_triple"}}` | 27:Out → 157:In; 157:Out → 150:In |
| `sts_wat_little_china.questphase / h2642 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#lch_06_tr_basement"}}` | 159:Out → 27:Succeeded; 158:Out → 159:In |
| `open_world_bugfixing.questphase / h116 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_finished"}}}` | 0:Out → 40:In; 40:True → 84:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"lch_06_finished"}}}` | 0:Out → 40:In; 40:True → 84:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wat_lch_06_combat.questphase / h7 / 3 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sts_wat_lch_06_combat.questphase / h109 / 22 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sts_wat_lch_06_openworld.questphase / h30 / 34; sts_wat_lch_06_openworld.questphase / h30 / 35; sts_wat_lch_06_ow.questphase / h12 / 9; sts_wat_lch_06_ow.questphase / h902 / 2 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_wat_lch_06_combat.questphase / h109 / 26; sts_wat_lch_06_combat.questphase / h109 / 28; sts_wat_lch_06_combat.questphase / h109 / 34; sts_wat_lch_06_combat.questphase / h109 / 35; +7 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h116 / 40; open_world_bugfixing.questphase / h2878 / 40; sts_wat_lch_06_bugfixing.questphase / h0 / 16; sts_wat_lch_06_bugfixing.questphase / h17 / 2; +16 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wat_lch_06_ow.questphase / h76 / 105; sts_wat_lch_06_ow.questphase / h76 / 72; sts_wat_lch_06_ow.questphase / h76 / 73; sts_wat_lch_06_ow.questphase / h902 / 24; +3 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_wat_lch_06_bugfixing.questphase / h17 / 5; sts_wat_lch_06_bugfixing.questphase / h79 / 2; sts_wat_lch_06_ow.questphase / h76 / 100; sts_wat_lch_06_ow.questphase / h76 / 132; +10 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wat_lch_06_bugfixing.questphase / h79 / 13; sts_wat_lch_06_bugfixing.questphase / h79 / 4; sts_wat_lch_06_bugfixing.questphase / h79 / 5; sts_wat_lch_06_combat.questphase / h7 / 12; +15 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_wat_lch_06_combat.questphase / h93 / 5; sts_wat_lch_06_ow.questphase / h76 / 124; sts_wat_lch_06_ow.questphase / h76 / 143; sts_wat_little_china.questphase / h2642 / 143 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_wat_lch_06_ow.questphase / h902 / 29 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h116 / 84; open_world_bugfixing.questphase / h2878 / 84; sts_wat_lch_06_openworld.questphase / h30 / 18; sts_wat_lch_06_openworld.questphase / h30 / 20; +41 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | sts_wat_lch_06_combat.questphase / h7 / 10; sts_wat_lch_06_combat.questphase / h7 / 9 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `parallel_join` | sts_wat_lch_06_openworld.questphase / h30 / 16 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_wat_lch_06_bugfixing.questphase / h17 / 4; sts_wat_lch_06_bugfixing.questphase / h79 / 7; sts_wat_lch_06_chats.scene / scene / 7; sts_wat_lch_06_combat.questphase / h93 / 9; +26 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wat_lch_06_openworld.questphase / h30 / 25; sts_wat_lch_06_ow.questphase / h76 / 121; sts_wat_lch_06_ow.questphase / h76 / 86; sts_wat_little_china.questphase / h2642 / 121; +1 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wat_lch_06_bugfixing.questphase / h79 / 3; sts_wat_lch_06_combat.questphase / h109 / 36; sts_wat_lch_06_holocall_debrief.scene / scene / 252; sts_wat_lch_06_holocall_debrief.scene / scene / 256; +5 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_wat_lch_06_ow.questphase / h76 / 118; sts_wat_lch_06_ow.questphase / h76 / 130; sts_wat_little_china.questphase / h2642 / 130 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_wat_lch_06_ow.questphase / h902 / 4 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_wat_lch_06_ow.questphase / h76 / 78; sts_wat_little_china.questphase / h2642 / 78 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_wat_lch_06_combat.questphase / h109 / 2; sts_wat_lch_06_ow.questphase / h76 / 104; sts_wat_lch_06_ow.questphase / h902 / 25 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wat_lch_06_bugfixing.questphase / h79 / 9; sts_wat_lch_06_combat.questphase / h109 / 33; sts_wat_lch_06_combat.questphase / h109 / 4; sts_wat_lch_06_combat.questphase / h109 / 5; +26 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_wat_lch_06_combat.questphase / h250 / 5; sts_wat_lch_06_combat.questphase / h250 / 6; sts_wat_lch_06_ow.questphase / h76 / 59 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sts_wat_lch_06_combat.questphase / h250 / 12 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sts_wat_lch_06_combat.questphase / h109 / 29 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_wat_lch_06_combat.questphase / h7 / 4; sts_wat_lch_06_ow.questphase / h427 / 2; sts_wat_lch_06_ow.questphase / h427 / 60; sts_wat_lch_06_ow.questphase / h427 / 61; +3 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase` | repair; journal anchor | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` | content candidate; journal anchor | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` | content candidate; journal anchor | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` | content candidate; journal anchor | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` | content candidate; forward dependency | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wat-lch-06` |
| `base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wat-lch-06.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

246 repeated typed/socket path signatures in this selected graph context; 25 distinct direct resource identities; 15 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `598920ee48558917ab4e` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h902 / 2 -> 3 -> 7 | questCheckpointNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `20a77143a898bc753a26` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h7 / 14 -> 15 -> 5 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 61 -> 283 -> 281 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h902 / 30 -> 29 -> 28 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 67 -> 68 -> 65 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2e1ee5a1324dbeeb9071` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h7 / 15 -> 5 -> 3 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 59 -> 60 -> 26 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 26 -> 67 -> 68 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h7 / 3 -> 2 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` / scene / 9 -> 40 -> 10 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 279 -> 61 -> 283 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase` / h0 / 5 | `h17` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase` / h0 / 8 | `h63` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase` / h0 / 15 | `h79` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h0 / 2 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h0 / 3 | `h93` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h93 / 3 | `h109` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h93 / 4 | `h213` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h0 / 9 | `h250` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h0 / 2 | `h7` | [{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":3,"socketName":"In"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h0 / 3 | `h30` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h0 / 4 | `h221` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h0 / 2 | `h12` | [{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":3,"socketName":"In"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h0 / 3 | `h76` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h76 / 101 | `h427` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h0 / 4 | `h902` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.gamedef` | content candidate | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06_test_def.gamedef` | content candidate | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest |
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
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\phases\sts_wat_lch_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\phases\sts_wat_lch_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\phases\sts_wat_lch_03_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_f_02_jap_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_f_05_jap_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_m_02_jap_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_m_06_jap_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_m_07_jap_25_mt.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_m_08_jap_30_mt.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\gang_tcl_m_09_jap_40_mt.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_chats\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_holocall_debrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\lipsync\en\sts_wat_lch_06_holocall_prebrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_glitter` | base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h2642 / 51; 1 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 186; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 379; 194 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 375; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; 74 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 395; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 412; 102 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 403; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; 63 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 185; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 378; 253 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 373; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; 69 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `lch_06_finished` | base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h3468 / 3; 1 total source locations in compressed evidence |
| `lch_06_gang_retaliation` | base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h2313 / 9; 1 total source locations in compressed evidence |
| `lch_06_start` | base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h2642 / 50; 1 total source locations in compressed evidence |
| `lch_06_testdef` | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest / h0 / 10; 1 total source locations in compressed evidence |
| `sts_tygerclaws_retaliation` | base\open_world\street_stories\street_stories_gang_retaliation.questphase / h2439 / 23; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h5350 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h1874 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h3468 / 41; 12 total source locations in compressed evidence |
| `wat_achievement` | base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase / h0 / 81; base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase / h0 / 89; base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase / h0 / 50; base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase / h0 / 66; 67 total source locations in compressed evidence |
| `welcome_holocall_skipped` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h1701 / 275; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h3924 / 125; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h4664 / 232; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h5754 / 195; 41 total source locations in compressed evidence |

NodeRef uses: 187; TweakDB binding uses: 6. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` | 3 / 23 | scnDialogLineEvent: 23 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
