# NO_TITLE

Journal: `quests/minor_quest/mq009_loser` · `MinorQuest` · hash `1908626717`.

**Coverage: journal-linked.** 26 exact journal-linked nodes in 1 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/01_approach_loser` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/02_sit_loser` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_drive_loser` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_get_in_car` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/04_shoot` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/05_follow` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/07_come_back` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/08_talk` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_hook/01_beat` |
|  (Primary) | `quests/minor_quest/mq009_loser/mq009_hook/02_talk_loser` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq009.questphase / h0 / 26` (Journal) | `quests/minor_quest/mq009_loser` | 16:end_quest_out → 26:Succeeded; 23:Out1 → 26:Succeeded; 26:Out → 44:In1 |
| `mq009.questphase / h12 / 32` (Journal) | `quests/minor_quest/mq009_loser/mq009_hook/02_talk_loser` | 28:Out1 → 32:Succeeded |
| `mq009.questphase / h12 / 47` (Journal) | `quests/minor_quest/mq009_loser` | 9:Out → 47:Active |
| `mq009.questphase / h12 / 54` (Journal) | `quests/minor_quest/mq009_loser/mq009_hook/02_talk_loser` | 54:Out → 20:In; 52:Out → 54:Active |
| `mq009.questphase / h216 / 8` (Journal) | `quests/minor_quest/mq009_loser/mq009_hook/01_beat` | 0:Out → 8:Active |
| `mq009.questphase / h216 / 12` (Journal) | `quests/minor_quest/mq009_loser/mq009_hook/01_beat` | 11:Out1 → 12:Succeeded; 12:Out → 13:Active |
| `mq009.questphase / h216 / 13` (Journal) | `quests/minor_quest/mq009_loser/mq009_hook/02_talk_loser` | 13:Out → 1:In; 12:Out → 13:Active |
| `mq009.questphase / h357 / 16` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/01_approach_loser` | 6:Out → 16:Active |
| `mq009.questphase / h357 / 17` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/01_approach_loser` | 8:Out → 17:Succeeded |
| `mq009.questphase / h357 / 18` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/02_sit_loser` | 11:approaches_out → 18:Active |
| `mq009.questphase / h357 / 19` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/02_sit_loser` | 73:Out → 19:Succeeded; 19:Out → 99:Active |
| `mq009.questphase / h357 / 85` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/07_come_back` | 11:mq009_suspended → 85:Active; 85:Out → 86:In |
| `mq009.questphase / h357 / 89` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/07_come_back` | 88:back_out' → 89:Succeeded; 89:Out → 93:Active |
| `mq009.questphase / h357 / 93` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/02_sit_loser` | 93:Out → 12:sit_in; 89:Out → 93:Active |
| `mq009.questphase / h357 / 99` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/08_talk` | 19:Out → 99:Active; 99:Out → 87:In |
| `mq009.questphase / h357 / 100` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/08_talk` | 78:Out → 100:Succeeded; 100:Out → 95:In |
| `mq009.questphase / h357 / 101` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/08_talk` | 101:Out → 68:In; 82:Out → 101:Succeeded |
| `mq009.questphase / h720 / 6` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_get_in_car` | 58:Out → 6:Active |
| `mq009.questphase / h720 / 8` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_get_in_car` | 5:Out → 8:Succeeded; 8:Out → 9:Active |
| `mq009.questphase / h720 / 9` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_drive_loser` | 8:Out → 9:Active |
| `mq009.questphase / h720 / 28` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_drive_loser` | 14:Out1 → 28:Succeeded; 28:Out → 29:Active |
| `mq009.questphase / h720 / 29` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/05_follow` | 28:Out → 29:Active |
| `mq009.questphase / h720 / 30` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/05_follow` | 20:Out → 30:Succeeded; 30:Out → 31:Active |
| `mq009.questphase / h720 / 31` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/04_shoot` | 30:Out → 31:Active |
| `mq009.questphase / h720 / 32` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/04_shoot` | 54:Out → 32:Succeeded; 32:Out → 56:In |
| `mq009.questphase / h720 / 57` (Journal) | `quests/minor_quest/mq009_loser/mq009_2nd_meeting/04_shoot` | 26:ken_lives_out → 57:Inactive; 57:Out → 56:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq009.questphase / h12 / 5` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 7:Out → 5:help_in |
| `mq009.questphase / h12 / 8` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 7:Out → 8:kicking_in |
| `mq009.questphase / h12 / 19` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 40:Out → 19:thank_in; 19:pills_yes_out → 24:story_pill_in; 19:pills_yes_out → 21:In; 19:pills_no_out → 24:story_nopill_in; 19:pills_no_out → 21:In |
| `mq009.questphase / h12 / 24` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 19:pills_yes_out → 24:story_pill_in; 19:pills_no_out → 24:story_nopill_in; 24:story_pill_out → 28:In1; 24:story_nopill_out → 28:In2 |
| `mq009.questphase / h216 / 3` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 4:Out → 3:kick_ass_in |
| `mq009.questphase / h216 / 5` | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`; `#mq009_01_sm_hook` | 0:Out → 5:wtf_in |
| `mq009.questphase / h357 / 5` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 8:CutSource → 5:CutDestination; 6:Out → 5:meeting_in |
| `mq009.questphase / h357 / 11` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 8:Out → 11:approaches_in; 11:approaches_out → 12:sit_in; 11:approaches_out → 18:Active; 11:approaches_out → 22:In; 11:mq009_suspended → 85:Active; 11:mq009_suspended → 90:In |
| `mq009.questphase / h357 / 12` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 11:approaches_out → 12:sit_in; 93:Out → 12:sit_in; 12:sit_out → 73:In |
| `mq009.questphase / h357 / 15` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 74:Out → 15:story_in; 15:agree_out → 78:In; 15:refuse_out → 82:In |
| `mq009.questphase / h357 / 70` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 2:Out → 70:teleport_in; 70:teleport_no → 4:In; 70:teleport_yes → 69:In |
| `mq009.questphase / h357 / 88` | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`; `#mq009_02_sm_second_meeting` | 86:Out → 88:back_in; 88:back_out' → 89:Succeeded |
| `mq009.questphase / h720 / 19` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 16:Out → 19:follow_in; 55:Out → 19:follow_in |
| `mq009.questphase / h720 / 24` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 21:Out → 24:execution_in |
| `mq009.questphase / h720 / 26` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 25:Out → 26:death_in; 26:death_out → 41:In; 26:death_out → 47:In; 26:ken_lives_out → 57:Inactive |
| `mq009.questphase / h720 / 43` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 44:Out → 43:cartalk_in |
| `mq009.questphase / h720 / 49` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 48:True → 49:leaving_in; 49:leaving_out → 52:In |
| `mq009.questphase / h720 / 53` | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`; `#mq009_03_sm_execution` | 51:Out → 53:suicide_in; 53:suicide_out → 56:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq009\mq009.questphase` / h12 / 5 | `mq009_01_hook.scene` | 7: Checkpoint; 7:Out → 5:help_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h12 / 8 | `mq009_01_hook.scene` | 7: Checkpoint; 7:Out → 8:kicking_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h12 / 19 | `mq009_01_hook.scene` | 40: PauseCondition; 40:Out → 19:thank_in; 19:pills_yes_out → 24:story_pill_in; 19:pills_yes_out → 21:In; 19:pills_no_out → 24:story_nopill_in; 19:pills_no_out → 21:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h12 / 24 | `mq009_01_hook.scene` | 19: Scene: mq009_01_hook.scene; 19: Scene: mq009_01_hook.scene; 19:pills_yes_out → 24:story_pill_in; 19:pills_no_out → 24:story_nopill_in; 24:story_pill_out → 28:In1; 24:story_nopill_out → 28:In2 |
| `base\quest\minor_quests\mq009\mq009.questphase` / h216 / 3 | `mq009_01_hook.scene` | 4: PauseCondition: {"seconds": 1, "miliseconds": 500}; 4:Out → 3:kick_ass_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h216 / 5 | `mq009_01_hook.scene` | 0: Input; 0:Out → 5:wtf_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 5 | `mq009_02_second_meeting.scene` | 8: CutControl; 6: SpawnManager; 8:CutSource → 5:CutDestination; 6:Out → 5:meeting_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 11 | `mq009_02_second_meeting.scene` | 8: CutControl; 8:Out → 11:approaches_in; 11:approaches_out → 12:sit_in; 11:approaches_out → 18:Active; 11:approaches_out → 22:In; 11:mq009_suspended → 85:Active; 11:mq009_suspended → 90:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 12 | `mq009_02_second_meeting.scene` | 11: Scene: mq009_02_second_meeting.scene; 93: Journal; 11:approaches_out → 12:sit_in; 93:Out → 12:sit_in; 12:sit_out → 73:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 15 | `mq009_02_second_meeting.scene` | 74: PauseCondition: {"miliseconds": 30}; 74:Out → 15:story_in; 15:agree_out → 78:In; 15:refuse_out → 82:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 70 | `mq009_02_second_meeting.scene` | 2: SpawnManager; 2:Out → 70:teleport_in; 70:teleport_no → 4:In; 70:teleport_yes → 69:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 88 | `mq009_02_second_meeting.scene` | 86: Checkpoint; 86:Out → 88:back_in; 88:back_out' → 89:Succeeded |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 19 | `mq009_03_execution.scene` | 16: PauseCondition; 55: Input; 16:Out → 19:follow_in; 55:Out → 19:follow_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 24 | `mq009_03_execution.scene` | 21: PauseCondition; 21:Out → 24:execution_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 26 | `mq009_03_execution.scene` | 25: PauseCondition: {"seconds": 4}; 25:Out → 26:death_in; 26:death_out → 41:In; 26:death_out → 47:In; 26:ken_lives_out → 57:Inactive |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 43 | `mq009_03_execution.scene` | 44: PauseCondition: {"seconds": 3}; 44:Out → 43:cartalk_in |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 49 | `mq009_03_execution.scene` | 48: Condition; 48:True → 49:leaving_in; 49:leaving_out → 52:In |
| `base\quest\minor_quests\mq009\mq009.questphase` / h720 / 53 | `mq009_03_execution.scene` | 51: PauseCondition: #mq009_tr_leaving; 51:Out → 53:suicide_in; 53:suicide_out → 56:In |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq009_01_hook.scene` | help_in, story_pill_in, story_nopill_in, kicking_in, wtf_in, kick_ass_in, thank_in → help_out, story_pill_out, story_nopill_out, kicking_out, wtf_out, kick_ass_out, pills_yes_out, pills_no_out | Ken_Lee; Homeless_1; Homeless_2; Johnny; Player; 47 nodes / 49 edges |
| `mq009_02_second_meeting.scene` | meeting_in, approaches_in, sit_in, story_in, teleport_in, back_in → meeting_out, approaches_out, sit_out, agree_out, refuse_out, mq009_suspended, teleport_yes, teleport_no, back_out' | Ken_Lee; Player; 54 nodes / 54 edges |
| `mq009_03_execution.scene` | leaving_in, suicide_in, follow_in, execution_in, death_in, cartalk_in → leaving_out, suicide_out, follow_out, ken_lives_out, execution_out, death_out, cartalk_out | Ken_Lee; Player; 33 nodes / 33 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq009_01_hook.scene / n25 / 0` | Zgoda. (``) | No option-level predicate stored | 0:0 → 127:0:0 |
| `mq009_01_hook.scene / n25 / 1` | Najpierw powiedz, o co chodzi. (``) | No option-level predicate stored | 0:1 → 130:0:0 |
| `mq009_01_hook.scene / n57 / 0` | Kendachi słynie z samobójstw. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:0 → 153:0:0 |
| `mq009_01_hook.scene / n57 / 1` | Mam ci wyjaśnić jej decyzję? (``) | No option-level predicate stored | 0:1 → 156:0:0 |
| `mq009_01_hook.scene / n57 / 2` | Wymarzony projekt Enid. (``) | No option-level predicate stored | 0:2 → 172:0:1 |
| `mq009_01_hook.scene / n57 / 3` | Znała wcześniej kogoś z Biotechniki? (``) | No option-level predicate stored | 0:3 → 175:0:0 |
| `mq009_01_hook.scene / n82 / 0` | Potrzebowałeś pomocy. (``) | No option-level predicate stored | 0:0 → 84:0:0 |
| `mq009_01_hook.scene / n82 / 1` | Powinieneś mi się odwdzięczyć. (``) | No option-level predicate stored | 0:1 → 86:0:0 |
| `mq009_01_hook.scene / n91 / 0` | Nie brzmisz, jak bezdomny. (``) | No option-level predicate stored | 0:0 → 98:0:0 |
| `mq009_01_hook.scene / n91 / 1` | Sprowokowałeś ich? (``) | No option-level predicate stored | 0:1 → 95:0:0 |
| `mq009_01_hook.scene / n110 / 0` | Coś mi jednak zawdzięczasz. (``) | No option-level predicate stored | 0:0 → 101:0:0 |
| `mq009_01_hook.scene / n110 / 1` | Myślałeś, że nikt nie zwróci na ciebie uwagi? (``) | No option-level predicate stored | 0:1 → 103:0:0 |
| `mq009_01_hook.scene / n137 / 0` | Nie chciałbym mieć takiego ojca. (``) | No option-level predicate stored | 0:0 → 135:0:0 |
| `mq009_01_hook.scene / n137 / 1` | Nie zrobiłeś nic złego. (``) | No option-level predicate stored | 0:1 → 136:0:0 |
| `mq009_01_hook.scene / n137 / 2` | Chyba zeszliśmy z tematu... (``) | No option-level predicate stored | 0:2 → 143:0:0 |
| `mq009_02_second_meeting.scene / n10 / 0` | [db_db]Sit. (``) | No option-level predicate stored | 0:0 → 12:0:0 |
| `mq009_02_second_meeting.scene / n27 / 0` | [db_db]Agree. (``) | No option-level predicate stored | 0:0 → 28:0:0 |
| `mq009_02_second_meeting.scene / n27 / 1` | [db_db]Refuse. (``) | No option-level predicate stored | 0:1 → 29:0:0 |
| `mq009_02_second_meeting.scene / n75 / 0` | Yes (``) | No option-level predicate stored | 0:0 → 38:0:0 |
| `mq009_02_second_meeting.scene / n75 / 1` | No (``) | No option-level predicate stored | 0:1 → 39:0:0 |
| `mq009_02_second_meeting.scene / n83 / 0` | W porządku. (``) | No option-level predicate stored | 0:0 → 185:0:0 |
| `mq009_02_second_meeting.scene / n83 / 1` | Może później. (``) | No option-level predicate stored | 0:1 → 85:0:0 |
| `mq009_02_second_meeting.scene / n100 / 0` | Wróciłem. (``) | No option-level predicate stored | 0:0 → 97:0:0 |
| `mq009_02_second_meeting.scene / n127 / 0` | Zasłużyłeś na to. (``) | No option-level predicate stored | 0:0 → 165:0:0 |
| `mq009_02_second_meeting.scene / n127 / 1` | Przykro mi. (``) | No option-level predicate stored | 0:1 → 163:0:0 |
| `mq009_02_second_meeting.scene / n127 / 2` | Czemu kazał zabić Enid? (``) | No option-level predicate stored | 0:2 → 158:0:0 |
| `mq009_02_second_meeting.scene / n127 / 3` | Zabiłbym go. (``) | No option-level predicate stored | 0:3 → 182:0:0 |
| `mq009_02_second_meeting.scene / n137 / 0` | Enid nie żyje, prawda? (``) | No option-level predicate stored | 0:0 → 142:0:0 |
| `mq009_02_second_meeting.scene / n137 / 1` | Czemu wcześniej na mnie naskoczyłeś? (``) | No option-level predicate stored | 0:1 → 139:0:0 |
| `mq009_02_second_meeting.scene / n144 / 0` | Jesteś chujem. (``) | No option-level predicate stored | 0:0 → 150:0:0 |
| `mq009_02_second_meeting.scene / n144 / 1` | Trochę cię rozumiem. (``) | No option-level predicate stored | 0:1 → 146:0:0 |
| `mq009_02_second_meeting.scene / n187 / 0` | [Poczęstuj Kena papierosem.] (``) | No option-level predicate stored | 0:0 → 189:0:0 |
| `mq009_02_second_meeting.scene / n187 / 1` | Nie palę. (``) | No option-level predicate stored | 0:1 → 191:0:0 |
| `mq009_03_execution.scene / n33 / 0` | Jesteś pewien? (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:0 → 46:0:0 |
| `mq009_03_execution.scene / n33 / 1` | Żegnaj, Ken. (``) | No option-level predicate stored | 0:1 → 49:0:0 |
| `mq009_03_execution.scene / n33 / 2` | Zasłużyłeś na to. (``) | No option-level predicate stored | 0:2 → 36:0:0 |
| `mq009_03_execution.scene / n33 / 3` | A co z dziobakami? (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq009_01_13_Platypus", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:3 → 24:0:0; 0:3 → 65:0:0 |
| `mq009_03_execution.scene / n72 / 0` | Enid uznałaby cię za tchórza. (``) | No option-level predicate stored | 0:0 → 74:0:0 |
| `mq009_03_execution.scene / n72 / 1` | Możesz spełnić marzenie Enid. (``) | No option-level predicate stored | 0:1 → 76:0:0 |
| `mq009_03_execution.scene / n86 / 0` | Nie wiem. (``) | No option-level predicate stored | 0:0 → 88:0:0 |
| `mq009_03_execution.scene / n86 / 1` | Nie chodzi o dziobaki. (``) | No option-level predicate stored | 0:1 → 90:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `mq009_01_09_Agree_Deal` | mq009_01_hook.scene / scene / 169 | mq009_03_execution.scene / scene / 57 |
| `mq009_01_13_Platypus` | mq009_01_hook.scene / scene / 172 | mq009_03_execution.scene / scene / 33 |
| `mq009_active` | mq009.questphase / h12 / 6; mq009.questphase / h1229 / 3 | No reader in selected context |
| `mq009_done` | mq009.questphase / h1229 / 4 | No reader in selected context |
| `mq009_execution_start` | mq009.questphase / h0 / 24; mq009.questphase / h0 / 43; mq009.questphase / h1229 / 2 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>48 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq009.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq009_tr_homeless_area"}}` | 15:Out1 → 29:In; 29:Out → 30:In |
| `mq009.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":3}}}` | 45:Out → 16:In1; 30:Out → 45:In |
| `mq009.questphase / h12 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_hook_start"}}` | 2:Out → 4:In; 4:Out → 6:In |
| `mq009.questphase / h12 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_hook_wtf"}}` | 7:Out → 9:In; 9:Out → 53:In1; 9:Out → 47:Active |
| `mq009.questphase / h12 / 28` | `questLogicalXorNodeDefinition` `{}` | 24:story_pill_out → 28:In1; 24:story_nopill_out → 28:In2; 28:Out1 → 26:In; 28:Out1 → 32:Succeeded |
| `mq009.questphase / h12 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 40:Out → 19:thank_in; 20:Out → 40:In |
| `mq009.questphase / h216 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 0:Out → 4:In; 4:Out → 3:kick_ass_in |
| `mq009.questphase / h216 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Homeless_1"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:Out → 9:In; 9:Out → 11:In1 |
| `mq009.questphase / h216 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Homeless_2"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:Out → 10:In; 10:Out → 11:In2 |
| `mq009.questphase / h216 / 11` | `questLogicalAndNodeDefinition` `{}` | 9:Out → 11:In1; 10:Out → 11:In2; 11:Out1 → 12:Succeeded |
| `mq009.questphase / h357 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_corner"}}` | 8:CutSource → 4:CutDestination; 10:Out → 4:In; 69:Out → 4:In; 70:teleport_no → 4:In; 4:Out → 6:In |
| `mq009.questphase / h357 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 6:Out → 7:In; 7:Out → 8:In |
| `mq009.questphase / h357 / 8` | `questCutControlNodeDefinition` `{}` | 8:CutSource → 4:CutDestination; 8:CutSource → 5:CutDestination; 7:Out → 8:In; 8:Out → 17:Succeeded; 8:Out → 11:approaches_in; 8:CutSource → 9:CutDestination |
| `mq009.questphase / h357 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#mq009_tr_corner"}}` | 6:Out → 9:In; 8:CutSource → 9:CutDestination; 9:Out → 10:In |
| `mq009.questphase / h357 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":30}}}` | 74:Out → 15:story_in; 87:Out → 74:In |
| `mq009.questphase / h357 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}}}` | 22:Out → 83:In |
| `mq009.questphase / h357 / 94` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq009_tr_spawn_corner"}}` | 0:Out → 94:In; 94:Out → 2:In |
| `mq009.questphase / h720 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mounted_vehicle"},"childIsPlayer":true,"role":"Driver"}}}` | 60:Out → 2:In; 2:Out → 35:In |
| `mq009.questphase / h720 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mounted_vehicle"},"childRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"role":"Passenger"}}}` | 4:Out → 5:In; 5:Out → 8:Succeeded; 5:Out → 10:In; 5:Out → 11:In; 5:Out → 44:In |
| `mq009.questphase / h720 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_execution"}}` | 5:Out → 10:In; 10:Out → 14:In1 |
| `mq009.questphase / h720 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_execution","activatorRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"isPlayerActivator":false}}` | 5:Out → 11:In; 11:Out → 14:In2 |
| `mq009.questphase / h720 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpeed_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mounted_vehicle"},"speed":1.0,"comparisonType":"CT_LESS"}}}` | 13:Out → 12:In; 12:Out → 15:In |
| `mq009.questphase / h720 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpeed_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mounted_vehicle"},"speed":2.0,"comparisonType":"CT_GREATER"}}}` | 13:Out → 12:In; 14:Out1 → 13:In |
| `mq009.questphase / h720 / 14` | `questLogicalAndNodeDefinition` `{}` | 10:Out → 14:In1; 11:Out → 14:In2; 14:Out1 → 13:In; 14:Out1 → 17:In; 14:Out1 → 28:Succeeded |
| `mq009.questphase / h720 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mounted_vehicle"},"childRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"condition":"OnUnmount","role":"Passenger"}}}` | 15:Out → 16:In; 16:Out → 18:In; 16:Out → 19:follow_in |
| `mq009.questphase / h720 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq009_tr_death","activatorRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"isPlayerActivator":false}}` | 23:Out → 20:In; 20:Out → 25:In; 20:Out → 30:Succeeded |
| `mq009.questphase / h720 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":4.0},"comparisonType":"LessOrEqual"}}}` | 45:Out → 21:In; 21:Out → 22:In; 21:Out → 24:execution_in |
| `mq009.questphase / h720 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 20:Out → 25:In; 25:Out → 26:death_in |
| `mq009.questphase / h720 / 35` | `questCutControlNodeDefinition` `{}` | 2:Out → 35:In; 35:Out → 4:In; 35:CutSource → 34:CutDestination |
| `mq009.questphase / h720 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]}}}}` | 42:Out → 38:In; 38:Out → 40:In |
| `mq009.questphase / h720 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` |  |
| `mq009.questphase / h720 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"isPlayer":false}}}` |  |
| `mq009.questphase / h720 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 5:Out → 44:In; 44:Out → 43:cartalk_in |
| `mq009.questphase / h720 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#mq009_tr_leaving"}}` | 26:death_out → 47:In; 54:CutSource → 47:CutDestination; 47:Out → 48:In |
| `mq009.questphase / h720 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq009_com_homeless","names":["Loser"]},"comparisonType":"Greater"}}}` | 47:Out → 48:In; 48:True → 49:leaving_in |
| `mq009.questphase / h720 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq009_tr_leaving"}}` | 54:CutSource → 51:CutDestination; 52:Out → 51:In; 51:Out → 53:suicide_in |
| `mq009.questphase / h720 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 49:leaving_out → 52:In; 52:Out → 51:In |
| `mq009.questphase / h720 / 54` | `questCutControlNodeDefinition` `{}` | 54:Out → 32:Succeeded; 40:Out → 54:In; 54:CutSource → 47:CutDestination; 54:CutSource → 51:CutDestination |
| `mq009.questphase / h720 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#owned_vehicle"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 60:Out → 2:In; 58:Out → 60:In |
| `mq009.questphase / h720 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 62:Out → 61:In |
| `mq009.questphase / h1229 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq009_tr_cleanup"}}` | 7:Out → 2:In; 5:Out → 7:In |
| `mq009.questphase / h1229 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 12:Out → 8:In; 8:Out → 10:In |
| `mq009.questphase / h1229 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq009_tr_cleanup"}}` | 8:Out → 10:In; 10:Out → 9:In |
| `mq009_02_second_meeting.scene / scene / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 45:0:0 → 46:0:1; 46:0:0 → 25:0:0 |
| `mq009_02_second_meeting.scene / scene / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 52:0:0 → 26:0:0; 152:0:0 → 52:0:1 |
| `mq009_02_second_meeting.scene / scene / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 60:0:0 → 63:0:1; 63:0:0 → 32:0:0 |
| `mq009_02_second_meeting.scene / scene / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 67:0:0 → 68:0:1; 68:0:0 → 137:0:0 |
| `mq009_03_execution.scene / scene / 57` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq009_01_09_Agree_Deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 9:0:0 → 57:0:1; 57:0:0 → 55:0:0; 57:0:1 → 8:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq009.questphase / h357 / 83; mq009.questphase / h720 / 60 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq009.questphase / h12 / 22; mq009.questphase / h12 / 27; mq009.questphase / h720 / 23; mq009.questphase / h720 / 34 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `choice_gate` | mq009_01_hook.scene / scene / 110; mq009_01_hook.scene / scene / 137; mq009_01_hook.scene / scene / 25; mq009_01_hook.scene / scene / 57; +14 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq009.questphase / h216 / 6; mq009.questphase / h216 / 7 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq009.questphase / h0 / 30; mq009.questphase / h0 / 47; mq009.questphase / h12 / 2; mq009.questphase / h12 / 20; +11 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq009_03_execution.scene / scene / 33; mq009_03_execution.scene / scene / 57 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq009.questphase / h1229 / 14 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `elapsed_time` | mq009.questphase / h0 / 45 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `mount_state` | mq009.questphase / h720 / 16; mq009.questphase / h720 / 2; mq009.questphase / h720 / 5 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq009.questphase / h216 / 11; mq009.questphase / h720 / 14 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq009.questphase / h0 / 24; mq009.questphase / h0 / 43; mq009.questphase / h12 / 6; mq009.questphase / h1229 / 2; +4 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq009.questphase / h12 / 28 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq009.questphase / h1229 / 8; mq009.questphase / h216 / 4; mq009.questphase / h357 / 74; mq009.questphase / h720 / 25; +7 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq009.questphase / h357 / 8; mq009.questphase / h720 / 35; mq009.questphase / h720 / 54 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scene_interface` | mq009.questphase / h12 / 19; mq009.questphase / h12 / 24; mq009.questphase / h12 / 5; mq009.questphase / h12 / 8; +14 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq009.questphase / h216 / 10; mq009.questphase / h216 / 9; mq009.questphase / h720 / 37 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq009.questphase / h720 / 15; mq009.questphase / h720 / 17; mq009.questphase / h720 / 4; mq009.questphase / h720 / 58; +1 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq009\mq009.questphase` | content candidate; journal anchor | `base-mq009` |
| `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` | content candidate; forward dependency | `base-mq009` |
| `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene` | content candidate; forward dependency | `base-mq009` |
| `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene` | content candidate; forward dependency | `base-mq009` |

Evidence shards for this dossier (including parent context): [base-mq009](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq009.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
