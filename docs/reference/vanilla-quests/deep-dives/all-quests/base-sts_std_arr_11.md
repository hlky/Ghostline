# Gig: Hacking the Hacker

Journal: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` · `StreetStory` · hash `70279251`.

Journal premise: Gig type: Agent Saboteur\nObjective: Infect 6th Street computer with a virus\nLocation: 6th Street hideout on MLK Blvd\nDetails:\n\nThose boys and girls from 6th Street think they got wicked smarts, that they can jump a Militech transport in my hood without me knowing about it. They think they can crack corpo weapons and tip the balance of power in this city to their favor. It's time they got a rude awakening.\n\nI'll snap you the location of the 6th St hideout and the door code. Job's simple – find a way in, look for the comp they use to jailbreak corpo tech, upload the virus I'll supply to you and voila, their fancy new weapon melts into a sparkly new slagheap.\n\nOne more thing. If you happen to find a Lucius Thoran, do me a favor and make his ass disappear, will ya? Thoran's a techie – came up with this gonk plan, which makes him a real thorn in my ass. Pun intended.\n\nStay safe and have fun.

**Coverage: journal-linked.** 60 exact journal-linked nodes in 4 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Upload the virus onto 6th Street netrunner's computer. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete` |
| Find 6th Street netrunner's computer. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/find` |
| Get inside 6th Street's hideout. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` |
| Enter the megabuilding. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` |
| Leave the 6th Street hideout. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` |
| Go to the Drop Point. (Primary) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point` |
| Kill Lucius. (Optional) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_std_arr_11_gameplay.questphase / h88 / 33` (PauseCondition) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 35:Work Started → 33:In; 33:Out → 34:In |
| `sts_std_arr_11_gameplay.questphase / h289 / 34` (PauseCondition) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 36:Work Started → 34:In; 34:Out → 35:In |
| `sts_std_arr_11_openworld.questphase / h12 / 5` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 73:Out → 5:Succeeded; 5:Out → 55:In; 5:Out → 81:In |
| `sts_std_arr_11_openworld.questphase / h12 / 7` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 60:True → 7:Active; 7:Out → 78:In |
| `sts_std_arr_11_openworld.questphase / h12 / 8` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 8:Out → 4:In; 75:Out → 8:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 14` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete` | 43:Out → 14:Succeeded; 14:Out → 47:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 43` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete/computer_001` | 43:Out → 14:Succeeded; 88:Out → 43:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 47` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 14:Out → 47:Active; 47:Out → 142:In; 47:Out → 144:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 49` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 141:Out → 49:Succeeded; 49:Out → 69:In; 49:Out → 73:In |
| `sts_std_arr_11_openworld.questphase / h12 / 61` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 60:False → 61:Active; 61:Out → 78:In |
| `sts_std_arr_11_openworld.questphase / h12 / 62` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/brief` | 56:Out → 62:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 70` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point` | 74:Out → 70:Active; 70:Out → 72:In; 70:Out → 97:In |
| `sts_std_arr_11_openworld.questphase / h12 / 75` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 75:Out → 8:Active; 77:Out → 75:Succeeded; 75:Out → 98:In; 75:Out → 127:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 79` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding/elevator` | 79:Out → 77:In; 78:Out → 79:Active; 79:Out → 135:In |
| `sts_std_arr_11_openworld.questphase / h12 / 80` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point/elevator` | 81:Out → 80:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 89` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point` | 71:Out → 89:Succeeded; 89:Out → 91:Succeeded |
| `sts_std_arr_11_openworld.questphase / h12 / 91` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 89:Out → 91:Succeeded; 91:Out → 92:In |
| `sts_std_arr_11_openworld.questphase / h12 / 96` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point/elevator` | 97:Out → 96:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 104` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 4:Out → 104:Succeeded; 104:Out → 138:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 127` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 75:Out → 127:Active; 127:Out → 128:In |
| `sts_std_arr_11_openworld.questphase / h12 / 129` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 191:Out → 129:Succeeded |
| `sts_std_arr_11_openworld.questphase / h12 / 130` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 141:Out → 130:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 133` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding/elevator` | 135:Out → 133:Inactive; 133:Out → 134:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 134` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 133:Out → 134:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 138` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete` | 138:Out → 85:In; 104:Out → 138:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 143` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/megabuilding` | 144:Out → 143:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 144` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/lab` | 47:Out → 144:Inactive; 144:Out → 143:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 145` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/megabuilding` | 142:Out → 145:Inactive; 145:Out → 146:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 146` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/lab` | 145:Out → 146:Active |
| `sts_std_arroyo.questphase / h4344 / 5` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 73:Out → 5:Succeeded; 5:Out → 55:In; 5:Out → 81:In |
| `sts_std_arroyo.questphase / h4344 / 7` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 60:True → 7:Active; 7:Out → 78:In |
| `sts_std_arroyo.questphase / h4344 / 8` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 8:Out → 4:In; 75:Out → 8:Active |
| `sts_std_arroyo.questphase / h4344 / 14` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete` | 43:Out → 14:Succeeded; 14:Out → 47:Active |
| `sts_std_arroyo.questphase / h4344 / 43` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete/computer_001` | 43:Out → 14:Succeeded; 88:Out → 43:Inactive |
| `sts_std_arroyo.questphase / h4344 / 47` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 14:Out → 47:Active; 47:Out → 142:In; 47:Out → 144:Inactive |
| `sts_std_arroyo.questphase / h4344 / 49` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 141:Out → 49:Succeeded; 49:Out → 69:In; 49:Out → 73:In |
| `sts_std_arroyo.questphase / h4344 / 61` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 60:False → 61:Active; 61:Out → 78:In |
| `sts_std_arroyo.questphase / h4344 / 62` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/brief` | 56:Out → 62:Active |
| `sts_std_arroyo.questphase / h4344 / 70` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point` | 74:Out → 70:Active; 70:Out → 72:In; 70:Out → 97:In |
| `sts_std_arroyo.questphase / h4344 / 75` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding` | 75:Out → 8:Active; 77:Out → 75:Succeeded; 75:Out → 98:In; 75:Out → 127:Active |
| `sts_std_arroyo.questphase / h4344 / 79` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding/elevator` | 79:Out → 77:In; 78:Out → 79:Active; 79:Out → 135:In |
| `sts_std_arroyo.questphase / h4344 / 80` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point/elevator` | 81:Out → 80:Inactive |
| `sts_std_arroyo.questphase / h4344 / 89` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point` | 71:Out → 89:Succeeded; 89:Out → 91:Succeeded |
| `sts_std_arroyo.questphase / h4344 / 91` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 89:Out → 91:Succeeded; 91:Out → 92:In |
| `sts_std_arroyo.questphase / h4344 / 96` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point/elevator` | 97:Out → 96:Inactive |
| `sts_std_arroyo.questphase / h4344 / 104` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 4:Out → 104:Succeeded; 104:Out → 138:Active |
| `sts_std_arroyo.questphase / h4344 / 127` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 75:Out → 127:Active; 127:Out → 128:In |
| `sts_std_arroyo.questphase / h4344 / 129` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 191:Out → 129:Succeeded |
| `sts_std_arroyo.questphase / h4344 / 130` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius` | 141:Out → 130:Inactive |
| `sts_std_arroyo.questphase / h4344 / 133` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding/elevator` | 135:Out → 133:Inactive; 133:Out → 134:Active |
| `sts_std_arroyo.questphase / h4344 / 134` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside` | 133:Out → 134:Active |
| `sts_std_arroyo.questphase / h4344 / 138` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete` | 138:Out → 85:In; 104:Out → 138:Active |
| `sts_std_arroyo.questphase / h4344 / 143` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/megabuilding` | 144:Out → 143:Active |
| `sts_std_arroyo.questphase / h4344 / 144` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/lab` | 47:Out → 144:Inactive; 144:Out → 143:Active |
| `sts_std_arroyo.questphase / h4344 / 145` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/megabuilding` | 142:Out → 145:Inactive; 145:Out → 146:Active |
| `sts_std_arroyo.questphase / h4344 / 146` (MappinManager) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/lab` | 145:Out → 146:Active |
| `sts_std_arroyo.questphase / h6505 / 33` (PauseCondition) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 35:Work Started → 33:In; 33:Out → 34:In |
| `sts_std_arroyo.questphase / h6706 / 34` (PauseCondition) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out` | 36:Work Started → 34:In; 34:Out → 35:In |
| `open_world_bugfixing.questphase / h864 / 13` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 12:True → 13:Succeeded |
| `open_world_bugfixing.questphase / h1999 / 13` (Journal) | `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11` | 12:True → 13:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_std_arr_11_gameplay.questphase / h198 / 11` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene`; `#sts_sm_std_arr_11_scene` | 42:Out → 11:arr_11_enemy_003_start; 11:arr_11_enemy_003_end → 32:In |
| `sts_std_arr_11_openworld.questphase / h12 / 152` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene`; `#sts_sm_std_arr_11_holocall_prebiref` | 152:End 0 → 100:Active; 152:rejected_out → 100:Active; 186:False → 152:Start 0; 152:Holocall INT → 163:In; 152:Holocall RET → 162:In |
| `sts_std_arr_11_openworld.questphase / h12 / 153` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene`; `#sts_sm_std_arr_11_holocall_debrief` | 153:End 0 → 65:In; 190:False → 153:Start 0; 153:rejected_out → 188:Active; 153:Holocall INT → 159:In; 153:Holocall RET → 158:In |
| `sts_std_arr_11_openworld.questphase / h12 / 154` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene`; `#sts_sm_std_arr_11_holocall_debrief` | 189:False → 154:Start 0; 154:rejected_out → 102:Active; 154:Holocall INT → 161:In; 154:Holocall RET → 160:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_phase.questphase` / h0 / 6 | `sts_std_arr_11_gameplay.questphase` | 0: Input; 0:Out → 6:In1 |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h3667 / 6 | `sts_std_arr_11_gameplay.questphase` | 0: Input; 0:Out → 6:In1 |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_phase.questphase` / h0 / 7 | `sts_std_arr_11_openworld.questphase` | 0: Input; 0:Out → 7:In1; 7:Out1 → 1:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h3667 / 7 | `sts_std_arr_11_openworld.questphase` | 0: Input; 0:Out → 7:In1; 7:Out1 → 1:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 153 | `sts_std_arr_11_holocall_debrief.scene` | 190: Condition; 153:End 0 → 65:In; 190:False → 153:Start 0; 153:rejected_out → 188:Active; 153:Holocall INT → 159:In; 153:Holocall RET → 158:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 154 | `sts_std_arr_11_holocall_debrief.scene` | 189: Condition; 189:False → 154:Start 0; 154:rejected_out → 102:Active; 154:Holocall INT → 161:In; 154:Holocall RET → 160:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h4344 / 153 | `sts_std_arr_11_holocall_debrief.scene` | 190: Condition; 153:End 0 → 65:In; 190:False → 153:Start 0; 153:rejected_out → 188:Active; 153:Holocall INT → 159:In; 153:Holocall RET → 158:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h4344 / 154 | `sts_std_arr_11_holocall_debrief.scene` | 189: Condition; 189:False → 154:Start 0; 154:rejected_out → 102:Active; 154:Holocall INT → 161:In; 154:Holocall RET → 160:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 152 | `sts_std_arr_11_holocall_prebiref.scene` | 186: Condition; 152:End 0 → 100:Active; 152:rejected_out → 100:Active; 186:False → 152:Start 0; 152:Holocall INT → 163:In; 152:Holocall RET → 162:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h4344 / 152 | `sts_std_arr_11_holocall_prebiref.scene` | 186: Condition; 152:End 0 → 100:Active; 152:rejected_out → 100:Active; 186:False → 152:Start 0; 152:Holocall INT → 163:In; 152:Holocall RET → 162:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h198 / 11 | `sts_std_arr_11_scene.scene` | 42: PauseCondition: #arr_11_ws_scene_talk; 42:Out → 11:arr_11_enemy_003_start; 11:arr_11_enemy_003_end → 32:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h6615 / 11 | `sts_std_arr_11_scene.scene` | 42: PauseCondition: #arr_11_ws_scene_talk; 42:Out → 11:arr_11_enemy_003_start; 11:arr_11_enemy_003_end → 32:In |
| `base\open_world\bugfixing\sts\sts_arroyo_bugfixing.questphase` / h73 / 2 | `sts_std_arroyo.questphase` | 3: PauseCondition: #arr_01_tr_sts_start; 18: PauseCondition: #arr_03_tr_sts_start; 3:Out → 2:arr_01 retro_signal; 18:Out → 2:arr_03 retro_signal |
| `base\open_world\street_stories\santo_domingo\sts_santo_domingo.questphase` / h0 / 2 | `sts_std_arroyo.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_quest.quest` / h0 / 2 | `sts_std_arr_11_phase.questphase` | 0: Start; 0:Out → 2:In1; 2:Out1 → 1:In |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` / h0 / 14 | `sts_std_arr_11_phase.questphase` | 60: Journal; 66: Journal; 60:Out → 14:In1; 66:Out → 14:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 43 | `sts_arroyo_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 43:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 6 | `sts_santo_domingo.questphase` | 0: Input; 0:Out → 6:In1 |
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
| `sts_std_arr_11_holocall_debrief.scene` | Start 0 → End 0, rejected_out | fixer; 25 nodes / 33 edges |
| `sts_std_arr_11_holocall_prebiref.scene` | Start 0 → End 0, rejected_out | fixer; 22 nodes / 25 edges |
| `sts_std_arr_11_scene.scene` | arr_11_enemy_003_start → arr_11_enemy_003_end | enemy_003; lucius; Player; 3 nodes / 2 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `arr_11__not_perfect` | sts_std_arr_11_openworld.questphase / h12 / 136 | No reader in selected context |
| `arr_11_achievement_added` | Producer outside selected context | sts_std_arr_11_openworld.questphase / h881 / 37 |
| `arr_11_finished` | sts_std_arr_11_openworld.questphase / h12 / 65; sts_std_arr_11_openworld.questphase / h12 / 95 | open_world_bugfixing.questphase / h1999 / 12; open_world_bugfixing.questphase / h864 / 12 |
| `arr_11_gang_chase` | sts_std_arr_11_openworld.questphase / h881 / 43 | No reader in selected context |
| `arr_11_lucius_dead` | sts_std_arr_11_openworld.questphase / h12 / 191; sts_std_arroyo.questphase / h4344 / 191 | sts_std_arr_11_openworld.questphase / h881 / 40 |
| `arr_11_perfect` | sts_std_arr_11_openworld.questphase / h12 / 137 | sts_std_arr_11_holocall_debrief.scene / scene / 258 |
| `arr_11_start` | sts_std_arr_11_openworld.questphase / h12 / 64 | No reader in selected context |
| `arr_11_track` | Producer outside selected context | sts_std_arr_11_openworld.questphase / h12 / 60; sts_std_arroyo.questphase / h4344 / 60 |
| `glossary_6thstreet` | sts_std_arr_11_openworld.questphase / h12 / 66 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_std_arr_11_holocall_prebiref.scene / scene / 279 |
| `holo_muamar_calls_v_end_activate` | sts_std_arr_11_holocall_debrief.scene / scene / 70; sts_std_arr_11_holocall_prebiref.scene / scene / 61; sts_std_arr_11_openworld.questphase / h12 / 159; sts_std_arr_11_openworld.questphase / h12 / 161; sts_std_arr_11_openworld.questphase / h12 / 163 | No reader in selected context |
| `holo_muamar_calls_v_end_done` | sts_std_arr_11_holocall_debrief.scene / scene / 69; sts_std_arr_11_holocall_prebiref.scene / scene / 57 | sts_std_arr_11_holocall_debrief.scene / scene / 68; sts_std_arr_11_holocall_prebiref.scene / scene / 56 |
| `holo_muamar_calls_v_rejectable` | sts_std_arr_11_holocall_debrief.scene / scene / 293; sts_std_arr_11_holocall_prebiref.scene / scene / 254; sts_std_arr_11_holocall_prebiref.scene / scene / 285 | No reader in selected context |
| `holo_muamar_calls_v_rejected` | sts_std_arr_11_holocall_debrief.scene / scene / 295; sts_std_arr_11_holocall_prebiref.scene / scene / 256 | sts_std_arr_11_holocall_debrief.scene / scene / 297; sts_std_arr_11_holocall_prebiref.scene / scene / 258 |
| `holo_muamar_calls_v_start_activate` | sts_std_arr_11_holocall_debrief.scene / scene / 271; sts_std_arr_11_holocall_debrief.scene / scene / 75; sts_std_arr_11_holocall_prebiref.scene / scene / 283; sts_std_arr_11_holocall_prebiref.scene / scene / 60; sts_std_arr_11_openworld.questphase / h12 / 158; sts_std_arr_11_openworld.questphase / h12 / 160; sts_std_arr_11_openworld.questphase / h12 / 162 | sts_std_arr_11_holocall_debrief.scene / scene / 273 |
| `holo_muamar_calls_v_start_done` | sts_std_arr_11_holocall_debrief.scene / scene / 74; sts_std_arr_11_holocall_prebiref.scene / scene / 55 | sts_std_arr_11_holocall_debrief.scene / scene / 263; sts_std_arr_11_holocall_prebiref.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_std_arr_11_holocall_debrief.scene / scene / 273; sts_std_arr_11_holocall_prebiref.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_std_arr_11_holocall_debrief.scene / scene / 273; sts_std_arr_11_holocall_prebiref.scene / scene / 279 |
| `std_achievement` | sts_std_arr_11_openworld.questphase / h881 / 10 | sts_std_arr_11_openworld.questphase / h881 / 33 |
| `sts_6thstreet_retaliation` | sts_std_arr_11_openworld.questphase / h881 / 41 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>84 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_std_arr_11_gameplay.questphase / h62 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_11_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 18:Out → 1:In; 20:Out → 18:In |
| `sts_std_arr_11_gameplay.questphase / h88 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 35:Work Started → 33:In; 33:Out → 34:In |
| `sts_std_arr_11_gameplay.questphase / h136 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":50}}}` | 33:Work Started → 23:In; 23:Out → 34:In |
| `sts_std_arr_11_gameplay.questphase / h136 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_first_room"}}` | 0:Out → 29:In; 29:Out → 33:In |
| `sts_std_arr_11_gameplay.questphase / h177 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_enter"}}` | 0:Out → 2:In; 2:Out → 12:In |
| `sts_std_arr_11_gameplay.questphase / h198 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_ws_scene_start"}}` | 0:Out → 2:In; 2:Out → 30:In |
| `sts_std_arr_11_gameplay.questphase / h198 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_ws_scene_talk"}}` | 42:Out → 11:arr_11_enemy_003_start; 33:Work Started → 42:In |
| `sts_std_arr_11_gameplay.questphase / h289 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 36:Work Started → 34:In; 34:Out → 35:In |
| `sts_std_arr_11_gameplay.questphase / h318 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_ws_look_at_player"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `sts_std_arr_11_gameplay.questphase / h357 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_inside_lab"}}` | 8:Out → 17:In; 17:Out → 16:In; 17:Out → 30:In1 |
| `sts_std_arr_11_gameplay.questphase / h357 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#arr_11_elevator_down_001"}}` | 25:Out → 7:In; 8:Out → 25:In; 25:Out → 26:In; 25:Out → 27:In |
| `sts_std_arr_11_openworld.questphase / h12 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_enter"}}` | 8:Out → 4:In; 4:Out → 104:Succeeded |
| `sts_std_arr_11_openworld.questphase / h12 / 60` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_track"}}}` | 60:True → 7:Active; 56:Out → 60:In; 60:False → 61:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false}}}` | 49:Out → 69:In; 69:Out → 74:In; 69:Out → 164:In |
| `sts_std_arr_11_openworld.questphase / h12 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_santo_domingo/arroyo/arroyo_drop_points_prefabZ4QJ2TA/drop_point_002_prefabUG2UVSY;#arr_11_drop_point","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 72:Out → 71:In; 71:Out → 89:Succeeded |
| `sts_std_arr_11_openworld.questphase / h12 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 73:Out → 5:Succeeded; 49:Out → 73:In; 74:CutSource → 73:CutDestination; 73:Out → 136:In |
| `sts_std_arr_11_openworld.questphase / h12 / 74` | `questCutControlNodeDefinition` `{}` | 69:Out → 74:In; 74:Out → 70:Active; 74:CutSource → 73:CutDestination; 74:Out → 137:In |
| `sts_std_arr_11_openworld.questphase / h12 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_get_to_megabuilding"}}` | 77:Out → 75:Succeeded; 79:Out → 77:In |
| `sts_std_arr_11_openworld.questphase / h12 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_ws_look_at_player"}}` | 7:Out → 78:In; 61:Out → 78:In; 78:Out → 79:Active |
| `sts_std_arr_11_openworld.questphase / h12 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_inside_elevator_top"}}` | 5:Out → 81:In; 81:Out → 80:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_11_dvc_computer_blueprints_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 138:Out → 85:In; 85:Out → 86:In |
| `sts_std_arr_11_openworld.questphase / h12 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_inside_elevator_top"}}` | 70:Out → 97:In; 97:Out → 96:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 75:Out → 98:In; 98:Out → 99:In |
| `sts_std_arr_11_openworld.questphase / h12 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_sts_content_lock"}}` | 100:Out → 106:In; 109:Out → 106:In; 106:Out → 108:In |
| `sts_std_arr_11_openworld.questphase / h12 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#arr_11_tr_sts_content_lock"}}` | 108:Out → 107:In; 107:Out → 109:In |
| `sts_std_arr_11_openworld.questphase / h12 / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 83:Out → 120:In; 120:Out → 121:In |
| `sts_std_arr_11_openworld.questphase / h12 / 122` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_11_dvc_computer_blueprints_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 84:Out → 122:In; 122:Out → 123:In |
| `sts_std_arr_11_openworld.questphase / h12 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 127:Out → 128:In; 128:Out → 191:In |
| `sts_std_arr_11_openworld.questphase / h12 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_santo_domingo/arroyo/sda_01/sda_01_env_prefabDEEDNSQ/sda_01_architecture_prefabZUXV55A/loc_megabuilding_h6_prefabGHAFGFQ/loc_megabuilding_h6_env_prefab2PXDIYA/lift_2_floors_prefabOOU25CY/lift_1","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsFloorSelected","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"floor","value":{"$type":"Variant","$rawData":"PQAIAAAAAQAAAA=="}}]}}}` | 79:Out → 135:In; 135:Out → 133:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#arr_11_tr_outside_02"}}` | 141:Out → 49:Succeeded; 141:Out → 130:Inactive; 142:Out → 141:In |
| `sts_std_arr_11_openworld.questphase / h12 / 142` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#arr_11_elevator_down"}}` | 47:Out → 142:In; 142:Out → 141:In; 142:Out → 145:Inactive |
| `sts_std_arr_11_openworld.questphase / h12 / 157` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 157:In; 157:False → 100:Active; 157:True → 186:In |
| `sts_std_arr_11_openworld.questphase / h12 / 174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 57:Out → 174:In; 174:Out → 176:In |
| `sts_std_arr_11_openworld.questphase / h12 / 175` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 93:Out → 175:In; 175:Out → 177:In |
| `sts_std_arr_11_openworld.questphase / h12 / 176` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\arroyo\\sts_std_arr_11\\scenes\\sts_std_arr_11_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 174:Out → 176:In; 176:Out → 179:In |
| `sts_std_arr_11_openworld.questphase / h12 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\arroyo\\sts_std_arr_11\\scenes\\sts_std_arr_11_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 175:Out → 177:In; 177:Out → 181:In |
| `sts_std_arr_11_openworld.questphase / h12 / 179` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\arroyo\\sts_std_arr_11\\scenes\\sts_std_arr_11_holocall_prebiref.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 179:Out → 1:In; 176:Out → 179:In |
| `sts_std_arr_11_openworld.questphase / h12 / 181` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\arroyo\\sts_std_arr_11\\scenes\\sts_std_arr_11_holocall_prebiref.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 181:Out → 90:In; 177:Out → 181:In |
| `sts_std_arr_11_openworld.questphase / h12 / 182` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 183:Out → 182:In; 182:Out → 190:In |
| `sts_std_arr_11_openworld.questphase / h12 / 185` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 184:Out → 185:In; 185:Out → 189:In |
| `sts_std_arr_11_openworld.questphase / h12 / 186` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 186:True → 100:Active; 186:False → 152:Start 0; 157:True → 186:In |
| `sts_std_arr_11_openworld.questphase / h12 / 189` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 189:False → 154:Start 0; 189:True → 102:Active; 185:Out → 189:In |
| `sts_std_arr_11_openworld.questphase / h12 / 190` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 190:False → 153:Start 0; 182:Out → 190:In; 190:True → 188:Active |
| `sts_std_arr_11_openworld.questphase / h808 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_sts_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 23:Out → 22:In; 22:Out → 25:In |
| `sts_std_arr_11_openworld.questphase / h881 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 19:Out → 18:In; 39:Out → 19:In |
| `sts_std_arr_11_openworld.questphase / h881 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 36:Out → 34:In; 34:Out → 35:In |
| `sts_std_arr_11_openworld.questphase / h881 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#arr_11_tr_sts_content_lock"}}` | 35:Out → 13:In; 35:Out → 14:In; 35:Out → 15:In; 34:Out → 35:In; 35:Out → 39:In |
| `sts_std_arr_11_openworld.questphase / h881 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_achievement_added"}}}` | 37:True → 9:In; 37:False → 10:In; 40:False → 37:In; 41:Out → 37:In |
| `sts_std_arr_11_openworld.questphase / h881 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_lucius_dead"}}}` | 0:Out → 40:In; 40:False → 37:In; 40:True → 43:In |
| `sts_std_arr_11_openworld.questphase / h1022 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_tenant_com","names":["tenant"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 2:In; 5:Out → 3:In |
| `sts_std_arr_11_holocall_debrief.scene / scene / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_end_done"}}}` | 68:0:0 → 69:0:1; 70:0:0 → 68:0:1 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 258` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_perfect"}}}` | 249:0:0 → 258:0:1; 258:0:0 → 28:0:0; 258:0:1 → 36:0:0 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_done"}}}` | 73:666:0 → 263:0:1; 263:0:0 → 266:0:0 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 73:666:0 → 269:0:1; 266:1:0 → 269:0:0; 266:1:0 → 269:1026:0; 269:0:0 → 273:0:1; 279:0:0 → 269:0:1 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 266:1:0 → 273:0:0; 266:1:0 → 273:1026:0; 269:0:0 → 273:0:1; 273:0:0 → 275:0:1 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 275` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 266:1:0 → 275:0:0; 266:1:0 → 275:1026:0; 273:0:0 → 275:0:1; 275:0:0 → 277:0:1 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 277` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 275:0:0 → 277:0:1; 277:0:0 → 271:0:1; 277:0:1 → 279:0:0 |
| `sts_std_arr_11_holocall_debrief.scene / scene / 297` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_rejected"}}}` | 75:0:0 → 297:0:1; 297:0:0 → 295:0:1 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_end_done"}}}` | 56:0:0 → 57:0:1; 61:0:0 → 56:0:1 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_rejected"}}}` | 60:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_done"}}}` | 54:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 54:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 283:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_std_arr_11_holocall_prebiref.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_std_arroyo.questphase / h4344 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_enter"}}` | 8:Out → 4:In; 4:Out → 104:Succeeded |
| `sts_std_arroyo.questphase / h4344 / 60` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_track"}}}` | 60:True → 7:Active; 56:Out → 60:In; 60:False → 61:Active |
| `sts_std_arroyo.questphase / h4344 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false}}}` | 49:Out → 69:In; 69:Out → 74:In; 69:Out → 164:In |
| `sts_std_arroyo.questphase / h4344 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_santo_domingo/arroyo/arroyo_drop_points_prefabZ4QJ2TA/drop_point_002_prefabUG2UVSY;#arr_11_drop_point","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 72:Out → 71:In; 71:Out → 89:Succeeded |
| `sts_std_arroyo.questphase / h4344 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 73:Out → 5:Succeeded; 49:Out → 73:In; 74:CutSource → 73:CutDestination; 73:Out → 136:In |
| `sts_std_arroyo.questphase / h4344 / 74` | `questCutControlNodeDefinition` `{}` | 69:Out → 74:In; 74:Out → 70:Active; 74:CutSource → 73:CutDestination; 74:Out → 137:In |
| `sts_std_arroyo.questphase / h4344 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_tr_get_to_megabuilding"}}` | 77:Out → 75:Succeeded; 79:Out → 77:In |
| `sts_std_arroyo.questphase / h4344 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_ws_look_at_player"}}` | 7:Out → 78:In; 61:Out → 78:In; 78:Out → 79:Active |
| `sts_std_arroyo.questphase / h4344 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_inside_elevator_top"}}` | 5:Out → 81:In; 81:Out → 80:Inactive |
| `sts_std_arroyo.questphase / h4344 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_11_dvc_computer_blueprints_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 138:Out → 85:In; 85:Out → 86:In |
| `sts_std_arroyo.questphase / h4344 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#arr_11_inside_elevator_top"}}` | 70:Out → 97:In; 97:Out → 96:Inactive |
| `sts_std_arroyo.questphase / h4344 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 75:Out → 98:In; 98:Out → 99:In |
| `sts_std_arroyo.questphase / h4344 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#arr_11_com","names":["lucius"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 127:Out → 128:In; 128:Out → 191:In |
| `sts_std_arroyo.questphase / h4344 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_santo_domingo/arroyo/sda_01/sda_01_env_prefabDEEDNSQ/sda_01_architecture_prefabZUXV55A/loc_megabuilding_h6_prefabGHAFGFQ/loc_megabuilding_h6_env_prefab2PXDIYA/lift_2_floors_prefabOOU25CY/lift_1","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsFloorSelected","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"floor","value":{"$type":"Variant","$rawData":"QwAIAAAAAQAAAA=="}}]}}}` | 79:Out → 135:In; 135:Out → 133:Inactive |
| `sts_std_arroyo.questphase / h4344 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#arr_11_tr_outside_02"}}` | 141:Out → 49:Succeeded; 141:Out → 130:Inactive; 142:Out → 141:In |
| `sts_std_arroyo.questphase / h4344 / 142` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#arr_11_elevator_down"}}` | 47:Out → 142:In; 142:Out → 141:In; 142:Out → 145:Inactive |
| `sts_std_arroyo.questphase / h6505 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 35:Work Started → 33:In; 33:Out → 34:In |
| `sts_std_arroyo.questphase / h6706 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 36:Work Started → 34:In; 34:Out → 35:In |
| `open_world_bugfixing.questphase / h864 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_finished"}}}` | 0:Out → 12:In; 12:True → 13:Succeeded |
| `open_world_bugfixing.questphase / h1999 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arr_11_finished"}}}` | 0:Out → 12:In; 12:True → 13:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_std_arr_11_openworld.questphase / h1022 / 3; sts_std_arr_11_openworld.questphase / h12 / 98; sts_std_arroyo.questphase / h4344 / 98 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_std_arr_11_openworld.questphase / h12 / 56; sts_std_arr_11_openworld.questphase / h12 / 57; sts_std_arr_11_openworld.questphase / h12 / 93; sts_std_arr_11_openworld.questphase / h881 / 17; +1 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | sts_std_arr_11_gameplay.questphase / h357 / 18; sts_std_arr_11_gameplay.questphase / h357 / 19; sts_std_arr_11_gameplay.questphase / h357 / 20; sts_std_arr_11_gameplay.questphase / h357 / 21; +5 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_std_arr_11_gameplay.questphase / h198 / 25; sts_std_arr_11_gameplay.questphase / h357 / 16; sts_std_arr_11_gameplay.questphase / h7 / 26; sts_std_arr_11_openworld.questphase / h1022 / 5; +2 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1999 / 12; open_world_bugfixing.questphase / h864 / 12; sts_std_arr_11_holocall_debrief.scene / scene / 258; sts_std_arr_11_holocall_debrief.scene / scene / 263; +11 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_std_arr_11_openworld.questphase / h0 / 10; sts_std_arr_11_openworld.questphase / h12 / 108; sts_std_arr_11_openworld.questphase / h12 / 109; sts_std_arr_11_openworld.questphase / h12 / 155; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_std_arr_11_gameplay.questphase / h62 / 20; sts_std_arr_11_openworld.questphase / h12 / 121; sts_std_arr_11_openworld.questphase / h12 / 123; sts_std_arr_11_openworld.questphase / h12 / 72; +5 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_std_arr_11_openworld.questphase / h12 / 116; sts_std_arr_11_openworld.questphase / h12 / 87; sts_std_arr_11_openworld.questphase / h12 / 88; sts_std_arr_11_openworld.questphase / h808 / 13; +5 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_std_arr_11_gameplay.questphase / h62 / 18; sts_std_arr_11_openworld.questphase / h12 / 122; sts_std_arr_11_openworld.questphase / h12 / 135; sts_std_arr_11_openworld.questphase / h12 / 71; +4 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_std_arr_11_openworld.questphase / h881 / 34 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1999 / 13; open_world_bugfixing.questphase / h864 / 13; sts_std_arr_11_openworld.questphase / h0 / 8; sts_std_arr_11_openworld.questphase / h12 / 100; +37 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | sts_std_arr_11_openworld.questphase / h12 / 99 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `persistent_decision` | sts_std_arr_11_holocall_debrief.scene / scene / 271; sts_std_arr_11_holocall_debrief.scene / scene / 293; sts_std_arr_11_holocall_debrief.scene / scene / 295; sts_std_arr_11_holocall_debrief.scene / scene / 69; +28 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_std_arr_11_gameplay.questphase / h136 / 23; sts_std_arr_11_holocall_debrief.scene / scene / 269; sts_std_arr_11_holocall_debrief.scene / scene / 275; sts_std_arr_11_holocall_prebiref.scene / scene / 273; +8 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_std_arr_11_openworld.questphase / h12 / 74; sts_std_arroyo.questphase / h4344 / 74 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_std_arr_11_openworld.questphase / h12 / 55; sts_std_arr_11_openworld.questphase / h12 / 92; sts_std_arroyo.questphase / h4344 / 55; sts_std_arroyo.questphase / h4344 / 92 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_std_arr_11_gameplay.questphase / h198 / 11; sts_std_arr_11_openworld.questphase / h12 / 152; sts_std_arr_11_openworld.questphase / h12 / 153; sts_std_arr_11_openworld.questphase / h12 / 154 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_std_arr_11_gameplay.questphase / h136 / 29; sts_std_arr_11_gameplay.questphase / h177 / 2; sts_std_arr_11_gameplay.questphase / h198 / 2; sts_std_arr_11_gameplay.questphase / h198 / 42; +21 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_std_arr_11_openworld.questphase / h12 / 120; sts_std_arr_11_openworld.questphase / h12 / 128; sts_std_arr_11_openworld.questphase / h12 / 69; sts_std_arroyo.questphase / h4344 / 128; +1 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_std_arr_11_gameplay.questphase / h136 / 33; sts_std_arr_11_gameplay.questphase / h198 / 27; sts_std_arr_11_gameplay.questphase / h198 / 33; sts_std_arr_11_gameplay.questphase / h289 / 35; +7 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` | content candidate; journal anchor | `base-sts-std-arr-11` |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` | content candidate; journal anchor | `base-sts-std-arr-11` |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-std-arr-11` |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` | content candidate; forward dependency | `base-sts-std-arr-11` |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene` | content candidate; forward dependency | `base-sts-std-arr-11` |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-std-arr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-std-arr-11.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

200 repeated typed/socket path signatures in this selected graph context; 23 distinct direct resource identities; 18 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h1022 / 0 -> 5 -> 3 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 75 -> 297 -> 295 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h881 / 36 -> 34 -> 35 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 250 -> 70 -> 68 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 297 -> 295 -> 299 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` / scene / 55 -> 58 -> 24 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 28 -> 250 -> 70 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene` / scene / 58 -> 60 -> 59 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 293 -> 75 -> 297 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 21 -> 293 -> 75 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 4 -> 104 -> 138 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 263 -> 266 -> 269 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h0 / 3 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h0 / 4 | `h28` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h28 / 4 | `h35` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h0 / 6 | `h50` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h50 / 2 | `h62` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 4 | `h88` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 5 | `h117` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 6 | `h136` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 7 | `h177` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 8 | `h198` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 11 | `h289` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h62 / 16 | `h318` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h0 / 7 | `h357` | [{"$type":"questInputNodeDefinition","id":8,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h357 / 30 | `h436` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":90,"socketName":"Out2"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h0 / 4 | `h808` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h0 / 6 | `h881` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":18,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h0 / 9 | `h1022` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_gamedef.gamedef` | content candidate | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_quest.quest |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_gamedef_test.gamedef` | content candidate | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_quest.quest |
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
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\phases\sts_std_arr_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\phases\sts_std_arr_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\sts_std_arr_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\lipsync\en\sts_std_arr_11_holocall_debrief\muamar_capitan_reyes.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\lipsync\en\sts_std_arr_11_holocall_prebiref\muamar_capitan_reyes.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\lipsync\en\sts_std_arr_11_scene\gang_6th_m_01_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\lipsync\en\sts_std_arr_11_scene\gang_6th_m_02_nat_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\lipsync\en\sts_std_arr_11_scene\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `arr_11__not_perfect` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 136; 1 total source locations in compressed evidence |
| `arr_11_achievement_added` | base\open_world\bugfixing\fixers\muamar_bugfixing.questphase / h22 / 39; 1 total source locations in compressed evidence |
| `arr_11_finished` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 65; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 95; 2 total source locations in compressed evidence |
| `arr_11_gang_chase` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h5213 / 43; 1 total source locations in compressed evidence |
| `arr_11_perfect` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 137; 1 total source locations in compressed evidence |
| `arr_11_start` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 64; 1 total source locations in compressed evidence |
| `arr_11_track` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_quest.quest / h0 / 6; 1 total source locations in compressed evidence |
| `glossary_6thstreet` | base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase / h0 / 104; base\quest\main_quests\part1\q103\phases\q103_05_roadhouse.questphase / h0 / 88; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h5744 / 118; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 66; 7 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_muamar_calls_v_end_activate` | base\open_world\fixers\el_capitan\phases\el_capitan.questphase / h0 / 58; base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 83; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 283; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 285; 88 total source locations in compressed evidence |
| `holo_muamar_calls_v_end_done` | base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 79; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 193; base\quest\holocalls\muamar\muamar_holocall.scene / scene / 42; base\quest\holocalls\muamar\muamar_holocall.scene / scene / 556; 37 total source locations in compressed evidence |
| `holo_muamar_calls_v_rejectable` | base\quest\holocalls\muamar\muamar_holocall.scene / scene / 635; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 314; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 327; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene / scene / 254; 34 total source locations in compressed evidence |
| `holo_muamar_calls_v_rejected` | base\quest\holocalls\muamar\muamar_holocall.scene / scene / 643; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 316; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 329; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene / scene / 256; 23 total source locations in compressed evidence |
| `holo_muamar_calls_v_start_activate` | base\open_world\fixers\el_capitan\phases\el_capitan.questphase / h0 / 57; base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 82; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 282; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 284; 107 total source locations in compressed evidence |
| `holo_muamar_calls_v_start_done` | base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 77; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h7953 / 6; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h8314 / 6; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 192; 37 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `std_achievement` | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase / h0 / 28; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase / h0 / 77; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase / h0 / 97; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase / h65 / 23; 80 total source locations in compressed evidence |
| `sts_6thstreet_retaliation` | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h5213 / 41; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h3667 / 128; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h13340 / 25; base\open_world\street_stories\street_stories_gang_retaliation.questphase / h439 / 23; 6 total source locations in compressed evidence |

NodeRef uses: 164; TweakDB binding uses: 12. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` | 2 / 4 | scnDialogLineEvent: 4 |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
