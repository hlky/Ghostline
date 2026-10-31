# Gig: Hothead

Journal: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09` · `StreetStory` · hash `3876941490`.

Journal premise: Gig type: SOS: Merc Needed\nObjective: Protect Walter Ozark\nLocation: Japantown\nDetails:\n\nV, urgent job for you. A client just called about a problem with his head. Someone is in it.\n\nClient's name is Walter Ozark, a corpo – didn't say where but it's an urgent request with good pay so I didn't ask. Like any mid-level manager, he was issued a memory backup implant. But Walter believes he has reason to suspect that it was laced with malware. In other words – he has someone listening in on his thoughts. Probably a rival colleague but – again – who cares.\n\nWalter plans to reboot his implant but says as soon as tampering begins, the person responsible will receive a signal. If so, they could send someone to intervene. Walter's decided the safest strategy is to carry out the operation in a moving car to buy more time. I already have a runner willing to burn out the malware, but I need you behind the wheel. And remember – there's a reason why I hired you for this rather than a normal chauffeur. I'll send you the coordinates.

**Coverage: journal-linked.** 41 exact journal-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Return to the parking lot. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/back_to_meet_point` |
| Defeat the remaining enemies. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies` |
| Enter the netrunner's car. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/get_into_car` |
| Drive to the indicated location to meet the netrunner. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/go_to_parking_lot` |
| Help Walter Ozark remove the tracing program. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark` |
| Exit (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/leave_vehicle` |
| Escape the pursuers. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/lose_tail` |
| Defend the vehicle from attackers. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car` |
| Give the signal to netrunner when you're ready. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/say_that_youre_ready` |
| Stop the vehicle. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/stop_vehicle` |
| Talk to the netrunner. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 2` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 43:Out → 2:Active; 2:Out → 3:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 4` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 3:Out → 4:Succeeded; 4:Out → 5:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 5` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/say_that_youre_ready` | 4:Out → 5:Active; 5:Out → 25:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 10` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/say_that_youre_ready` | 25:Out → 10:Succeeded; 10:Out → 26:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 26` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/get_into_car` | 10:Out → 26:Active; 26:Out → 27:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 28` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/get_into_car` | 27:Out → 28:Succeeded; 28:Out → 29:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 29` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car` | 28:Out → 29:Active; 29:Out → 70:In; 29:Out → 75:In; 29:Out → 146:In; 29:Out → 148:In; 29:Out → 149:In; 29:Out → 151:In; 29:Out → 153:In; 29:Out → 155:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 32` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/leave_vehicle` | 109:True → 32:Active; 32:Out → 33:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 34` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/leave_vehicle` | 33:Out → 34:Succeeded; 34:Out → 67:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 35` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09` | 67:Out → 35:Succeeded; 35:Out → 40:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 41` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/go_to_parking_lot` | 44:False → 41:Active; 41:Out → 42:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 43` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/go_to_parking_lot` | 43:Out → 2:Active; 42:Out → 43:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 45` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/go_to_parking_lot` | 45:Out → 42:In; 44:True → 45:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 47` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark` | 39:Out → 47:Active; 47:Out → 48:Active; 47:Out → 49:In; 47:Out → 159:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 48` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/brief` | 47:Out → 48:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 52` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/back_to_meet_point` | 51:Out → 52:Active; 52:Out → 53:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 54` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/back_to_meet_point` | 54:Out → 30:In; 53:Out → 54:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 55` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 30:Out → 55:Active; 55:Out → 58:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 57` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 58:Out → 57:Succeeded; 57:Out → 109:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 60` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/lose_tail` | 70:Out → 60:Active; 60:Out → 61:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 63` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car` | 74:Out → 63:Succeeded; 75:Out → 63:Succeeded; 63:Out → 94:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 65` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/lose_tail` | 61:Out → 65:Succeeded; 65:Out → 74:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 67` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark` | 34:Out → 67:Succeeded; 67:Out → 35:Succeeded; 109:False → 67:Succeeded; 67:Out → 124:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 78` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies` | 94:True → 78:Active; 78:Out → 85:In; 78:Out → 86:In; 78:Out → 87:In; 78:Out → 88:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 84` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies` | 83:Out1 → 84:Succeeded; 84:Out → 105:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 102` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark` | 117:Out → 102:Failed; 102:Out → 103:Failed |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 103` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09` | 102:Out → 103:Failed; 103:Out → 120:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 105` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 84:Out → 105:Active; 105:Out → 107:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 106` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/talk_with_netrunner` | 107:Out → 106:Succeeded; 106:Out → 109:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 159` (PauseCondition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car` | 47:Out → 159:In; 159:Out → 157:In; 158:Out → 159:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 160` (PauseCondition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark` | 157:Out → 160:In; 160:Out → 158:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 79` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies/enemy1c1` | 79:Out → 83:In1; 85:Out → 79:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 80` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies/enemy1c2` | 80:Out → 83:In2; 86:Out → 80:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 81` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies/enemy2c1` | 81:Out → 83:In3; 87:Out → 81:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 82` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/defeat_enemies/enemy2c2` | 82:Out → 83:In4; 88:Out → 82:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 145` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy01` | 146:Out → 145:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 147` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy02` | 148:Out → 147:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 150` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy03` | 149:Out → 150:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 152` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy04` | 151:Out → 152:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 154` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy05` | 153:Out → 154:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 156` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car/enemy06` | 155:Out → 156:Inactive |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wbr_jpn_09_openworld.questphase / h814 / 7` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`; `#sts_sm_wbr_jpn_09_netrunner` | 25:Out → 7:before; 7:before_end → 8:In; 7:before_end → 23:In |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 5` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`; `#sts_sm_wbr_jpn_09_netrunner` | 4:Out1 → 5:damage |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 6` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`; `#sts_sm_wbr_jpn_09_netrunner` | 24:Out1 → 6:enemy_seen |
| `sts_wbr_jpn_09_openworld.questphase / h946 / 2` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`; `#sts_sm_wbr_jpn_09_netrunner` | 3:Out → 2:almost_done |
| `sts_wbr_jpn_09_openworld.questphase / h946 / 5` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`; `#sts_sm_wbr_jpn_09_netrunner` | 7:Out → 5:done |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09.questphase` / h0 / 6 | `sts_wbr_jpn_09_openworld.questphase` | 0: Input; 0:Out → 6:In1; 6:Out1 → 9:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h814 / 7 | `sts_wbr_jpn_09_netrunner.scene` | 25: PauseCondition: #jpn_09_tr_netrunner; 25:Out → 7:before; 7:before_end → 8:In; 7:before_end → 23:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h866 / 5 | `sts_wbr_jpn_09_netrunner.scene` | 4: LogicalXor; 4:Out1 → 5:damage |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h866 / 6 | `sts_wbr_jpn_09_netrunner.scene` | 24: LogicalXor; 24:Out1 → 6:enemy_seen |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h946 / 2 | `sts_wbr_jpn_09_netrunner.scene` | 3: PauseCondition: {"seconds": 45}; 3:Out → 2:almost_done |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h946 / 5 | `sts_wbr_jpn_09_netrunner.scene` | 7: FactsDBManager: jpn_09_procedure_finished; 7:Out → 5:done |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\sts_wbr_jpn_09.quest` / h0 / 2 | `sts_wbr_jpn_09.questphase` | 3: FactsDBManager: jpn_09_testdef; 2:Out1 → 1:In; 3:Out → 2:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_wbr_jpn_09_netrunner.scene` | before, damage, enemy_seen, almost_done, done → before_end, final_end | netrunner; netrunner_truck; v; 60 nodes / 63 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_wbr_jpn_09_netrunner.scene / n82 / 0` | Where's the client? (``) | No option-level predicate stored | 0:0 → 84:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / n82 / 1` | What else do you know about this virus? (``) | No option-level predicate stored | 0:1 → 248:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / n89 / 0` | Alright. Let's get moving. (``) | No option-level predicate stored | 0:0 → 100:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / n89 / 1` | How is this virus linked up to its coder? (``) | No option-level predicate stored | 0:1 → 250:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / n89 / 2` | We can limit the virus's signal to the router. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "jpn_09_redirection_hinted"}}, "bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questStat_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "statType": "Hacking", "value": 12.0}}} | 0:2 → 251:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / n152 / 0` | No sweat. (``) | No option-level predicate stored | 0:0 → 158:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / n152 / 1` | What about the client? (``) | No option-level predicate stored | 0:1 → 268:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `jpn_09_chase_started` | sts_wbr_jpn_09_openworld.questphase / h814 / 9 | sts_wbr_jpn_09_openworld.questphase / h91 / 27 |
| `jpn_09_enemies_in_sight` | Producer outside selected context | sts_wbr_jpn_09_netrunner.scene / scene / 183; sts_wbr_jpn_09_openworld.questphase / h866 / 9; sts_wbr_jpn_09_openworld.questphase / h91 / 61; sts_wbr_jpn_09_openworld.questphase / h91 / 70 |
| `jpn_09_finished` | sts_wbr_jpn_09_openworld.questphase / h91 / 40 | No reader in selected context |
| `jpn_09_leave_car` | sts_wbr_jpn_09_netrunner.scene / scene / 176 | sts_wbr_jpn_09_openworld.questphase / h1006 / 4; sts_wbr_jpn_09_openworld.questphase / h91 / 107; sts_wbr_jpn_09_openworld.questphase / h91 / 58 |
| `jpn_09_need_to_stop` | sts_wbr_jpn_09_netrunner.scene / scene / 173 | sts_wbr_jpn_09_openworld.questphase / h91 / 51 |
| `jpn_09_never_left_parking` | Producer outside selected context | sts_wbr_jpn_09_netrunner.scene / scene / 195; sts_wbr_jpn_09_openworld.questphase / h866 / 21; sts_wbr_jpn_09_openworld.questphase / h91 / 94 |
| `jpn_09_procedure_finished` | sts_wbr_jpn_09_openworld.questphase / h946 / 7 | sts_wbr_jpn_09_openworld.questphase / h91 / 74; sts_wbr_jpn_09_openworld.questphase / h91 / 75 |
| `jpn_09_procedure_started` | sts_wbr_jpn_09_netrunner.scene / scene / 120 | sts_wbr_jpn_09_openworld.questphase / h91 / 25 |
| `jpn_09_redirection_hinted` | sts_wbr_jpn_09_netrunner.scene / scene / 96 | sts_wbr_jpn_09_netrunner.scene / scene / 89 |
| `jpn_09_redirection_implemented` | sts_wbr_jpn_09_netrunner.scene / scene / 119 | sts_wbr_jpn_09_netrunner.scene / scene / 130 |
| `jpn_09_situation_known` | sts_wbr_jpn_09_netrunner.scene / scene / 146 | sts_wbr_jpn_09_openworld.questphase / h91 / 3 |
| `jpn_09_start` | sts_wbr_jpn_09_openworld.questphase / h91 / 39 | No reader in selected context |
| `jpn_09_talk_with_umbrage` | sts_wbr_jpn_09_netrunner.scene / scene / 179 | sts_wbr_jpn_09_openworld.questphase / h91 / 30 |
| `jpn_09_testdef` | Producer outside selected context | sts_wbr_jpn_09_openworld.questphase / h91 / 44 |

## Exact gates, joins and cancellation

<details><summary>63 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wbr_jpn_09_openworld.questphase / h12 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner"},"comparisonParams":{"$type":"questComparisonParam","count":3,"comparisonType":"GreaterOrEqual"}}}}` | 7:Out → 8:In; 8:Out → 20:In |
| `sts_wbr_jpn_09_openworld.questphase / h12 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 19:Out → 10:In; 20:Out → 19:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_situation_known"}}}` | 2:Out → 3:In; 3:Out → 4:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_procedure_started"}}}` | 5:Out → 25:In; 25:Out → 10:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_chase_started"}}}` | 26:Out → 27:In; 27:Out → 28:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_talk_with_umbrage"}}}` | 54:Out → 30:In; 30:Out → 55:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner_truck"]},"childIsPlayer":true,"condition":"OnUnmount","role":"Driver"}}}` | 32:Out → 33:In; 33:Out → 34:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr_parking_lot"}}` | 41:Out → 42:In; 45:Out → 42:In; 42:Out → 43:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_testdef"}}}` | 44:False → 41:Active; 49:Out → 44:In; 44:True → 45:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 49:Out → 44:In; 47:Out → 49:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_need_to_stop"}}}` | 94:False → 51:In; 51:Out → 52:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr_parking_lot"}}` | 52:Out → 53:In; 53:Out → 54:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_leave_car"}}}` | 55:Out → 58:In; 58:Out → 57:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_enemies_in_sight","comparisonType":"Equal"}}}` | 60:Out → 61:In; 61:Out → 65:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_enemies_in_sight"}}}` | 29:Out → 70:In; 70:Out → 60:Active; 70:Out → 73:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 73` | `questCutControlNodeDefinition` `{"permanent":true}` | 70:Out → 73:In; 73:CutSource → 75:CutDestination |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_procedure_finished"}}}` | 74:Out → 63:Succeeded; 65:Out → 74:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_procedure_finished"}}}` | 29:Out → 75:In; 75:Out → 63:Succeeded; 73:CutSource → 75:CutDestination |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 94` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_never_left_parking","value":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":4,"comparisonType":"Less"}}}]}}` | 94:False → 51:In; 63:Out → 94:In; 94:True → 78:Active |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_leave_car"}}}` | 105:Out → 107:In; 107:Out → 106:Succeeded |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner_truck"]},"childIsPlayer":true,"role":"Driver"}}}` | 109:True → 32:Active; 57:Out → 109:In; 109:False → 67:Succeeded; 106:Out → 109:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner_truck"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 111:Out → 114:In; 114:Out → 115:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/protect_car","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 47:Out → 159:In; 159:Out → 157:In; 158:Out → 159:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 160` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09/sts_wbr_jpn_09/help_ozark","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active","inverted":true}}}` | 157:Out → 160:In; 160:Out → 158:In |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 83` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 83:Out1 → 84:Succeeded; 79:Out → 83:In1; 80:Out → 83:In2; 81:Out → 83:In3; 82:Out → 83:In4 |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking","names":["enemy_1c_1"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 78:Out → 85:In; 85:Out → 79:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 86` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking","names":["enemy_1c_2"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 78:Out → 86:In; 86:Out → 80:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking","names":["enemy_2c_1"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 78:Out → 87:In; 87:Out → 81:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking","names":["enemy_2c_2"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 78:Out → 88:In; 88:Out → 82:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_01","names":["enemy_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 146:In; 146:Out → 145:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 148` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_01","names":["enemy_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 148:In; 148:Out → 147:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_02","names":["enemy_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 149:In; 149:Out → 150:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 151` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_02","names":["enemy_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 151:In; 151:Out → 152:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_03","names":["enemy_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 153:In; 153:Out → 154:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h91 / 155` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_03","names":["enemy_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 155:In; 155:Out → 156:Inactive |
| `sts_wbr_jpn_09_openworld.questphase / h814 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner_truck"]},"childIsPlayer":true,"role":"Driver"}}}` | 8:Out → 10:In; 10:Out → 9:In |
| `sts_wbr_jpn_09_openworld.questphase / h814 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr_netrunner"}}` | 0:Out → 25:In; 25:Out → 7:before |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner_truck"]}}}}` | 0:Out → 2:In; 2:Out → 4:In1 |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isTargetPlayer":true}}}` | 0:Out → 3:In; 3:Out → 4:In2 |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 4` | `questLogicalXorNodeDefinition` `{}` | 2:Out → 4:In1; 3:Out → 4:In2; 4:Out1 → 5:damage |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_enemies_in_sight"}}}` | 0:Out → 9:In; 9:Out → 24:In1 |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_never_left_parking","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 21:In; 21:Out → 23:In |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr_parking_lot","activatorRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking"},"isPlayerActivator":false}}` | 21:Out → 23:In; 23:Out → 24:In2 |
| `sts_wbr_jpn_09_openworld.questphase / h866 / 24` | `questLogicalXorNodeDefinition` `{}` | 24:Out1 → 6:enemy_seen; 9:Out → 24:In1; 23:Out → 24:In2 |
| `sts_wbr_jpn_09_openworld.questphase / h946 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":45}}}` | 0:Out → 3:In; 3:Out → 2:almost_done; 3:Out → 4:In |
| `sts_wbr_jpn_09_openworld.questphase / h946 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 3:Out → 4:In; 4:Out → 7:In |
| `sts_wbr_jpn_09_openworld.questphase / h1006 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_leave_car"}}}` | 0:Out → 4:In; 4:Out → 5:In |
| `sts_wbr_jpn_09_openworld.questphase / h1006 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 6:Out → 7:In; 7:Out → 8:In |
| `sts_wbr_jpn_09_openworld.questphase / h1006 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 5:Out → 21:In; 21:Out → 6:In |
| `sts_wbr_jpn_09_openworld.questphase / h1006 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 8:Success → 22:In; 22:Out → 10:In |
| `sts_wbr_jpn_09_netrunner.scene / scene / 103` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"Hacking","value":12.0}}}` | 81:2:0 → 103:0:1; 103:0:0 → 105:0:0; 103:0:1 → 82:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 130` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_redirection_implemented"}}}` | 53:0:0 → 130:0:1; 130:0:0 → 132:0:0; 130:0:1 → 59:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_enemies_in_sight","comparisonType":"Equal"}}}` | 183:0:0 → 173:0:1; 195:0:1 → 183:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 191` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_09_tr_parking_lot"}}` | 173:0:0 → 191:0:1; 191:0:0 → 179:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 195` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_09_never_left_parking","value":1,"comparisonType":"GreaterOrEqual"}}}` | 63:0:0 → 195:0:1; 195:0:0 → 198:0:1; 195:0:1 → 183:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 198` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_09_com_enemies_parking"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 195:0:0 → 198:0:1; 198:0:0 → 179:0:1 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 205` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"Hacking","value":12.0}}}` | 84:0:0 → 205:0:1; 205:0:0 → 111:0:0; 205:0:1 → 115:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 209` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"Hacking","value":12.0}}}` | 158:0:0 → 209:0:1; 209:0:0 → 138:0:0; 209:0:1 → 139:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 248` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_09\\scenes\\sts_wbr_jpn_09_netrunner.scene","Flags":"Soft"},"sectionName":"sts_wbr_more_virus","type":"IsOutside"}}}` | 82:0:1 → 248:0:1; 248:0:0 → 85:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 250` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_09\\scenes\\sts_wbr_jpn_09_netrunner.scene","Flags":"Soft"},"sectionName":"sts_wbr_communicate","type":"IsOutside"}}}` | 89:0:1 → 250:0:1; 250:0:0 → 90:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_09\\scenes\\sts_wbr_jpn_09_netrunner.scene","Flags":"Soft"},"sectionName":"sts_wbr_restrict","type":"IsOutside"}}}` | 89:0:2 → 251:0:1; 251:0:0 → 94:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 268` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_09\\scenes\\sts_wbr_jpn_09_netrunner.scene","Flags":"Soft"},"sectionName":"sts_wbr_patient","type":"IsOutside"}}}` | 152:0:1 → 268:0:1; 268:0:0 → 154:0:0 |
| `sts_wbr_jpn_09_netrunner.scene / scene / 293` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#jpn_09_com_netrunner","names":["netrunner"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":13.0},"comparisonType":"LessOrEqual"}}}` | 1:0:0 → 293:0:1; 293:0:0 → 295:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wbr_jpn_09_openworld.questphase / h12 / 8 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_wbr_jpn_09_openworld.questphase / h12 / 18 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_wbr_jpn_09_netrunner.scene / scene / 152; sts_wbr_jpn_09_netrunner.scene / scene / 82; sts_wbr_jpn_09_netrunner.scene / scene / 89 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_wbr_jpn_09_openworld.questphase / h1006 / 10; sts_wbr_jpn_09_openworld.questphase / h12 / 7 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sts_wbr_jpn_09_netrunner.scene / scene / 130; sts_wbr_jpn_09_netrunner.scene / scene / 183; sts_wbr_jpn_09_netrunner.scene / scene / 195; sts_wbr_jpn_09_netrunner.scene / scene / 89; +16 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wbr_jpn_09_openworld.questphase / h0 / 9; sts_wbr_jpn_09_openworld.questphase / h91 / 157; sts_wbr_jpn_09_openworld.questphase / h91 / 158 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `journal_transition` | sts_wbr_jpn_09_openworld.questphase / h0 / 6; sts_wbr_jpn_09_openworld.questphase / h12 / 10; sts_wbr_jpn_09_openworld.questphase / h12 / 16; sts_wbr_jpn_09_openworld.questphase / h91 / 10; +30 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | sts_wbr_jpn_09_openworld.questphase / h814 / 10; sts_wbr_jpn_09_openworld.questphase / h91 / 109; sts_wbr_jpn_09_openworld.questphase / h91 / 33 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | sts_wbr_jpn_09_openworld.questphase / h91 / 83 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_wbr_jpn_09_netrunner.scene / scene / 119; sts_wbr_jpn_09_netrunner.scene / scene / 120; sts_wbr_jpn_09_netrunner.scene / scene / 146; sts_wbr_jpn_09_netrunner.scene / scene / 173; +7 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wbr_jpn_09_openworld.questphase / h866 / 24; sts_wbr_jpn_09_openworld.questphase / h866 / 4 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wbr_jpn_09_openworld.questphase / h1006 / 21; sts_wbr_jpn_09_openworld.questphase / h1006 / 7; sts_wbr_jpn_09_openworld.questphase / h91 / 49; sts_wbr_jpn_09_openworld.questphase / h946 / 3; +1 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_wbr_jpn_09_openworld.questphase / h91 / 73 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_wbr_jpn_09_openworld.questphase / h0 / 7 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_wbr_jpn_09_openworld.questphase / h814 / 7; sts_wbr_jpn_09_openworld.questphase / h866 / 5; sts_wbr_jpn_09_openworld.questphase / h866 / 6; sts_wbr_jpn_09_openworld.questphase / h946 / 2; +1 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wbr_jpn_09_netrunner.scene / scene / 191; sts_wbr_jpn_09_openworld.questphase / h12 / 19; sts_wbr_jpn_09_openworld.questphase / h814 / 25; sts_wbr_jpn_09_openworld.questphase / h866 / 23; +2 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_wbr_jpn_09_netrunner.scene / scene / 198; sts_wbr_jpn_09_openworld.questphase / h91 / 114; sts_wbr_jpn_09_openworld.questphase / h91 / 146; sts_wbr_jpn_09_openworld.questphase / h91 / 148; +9 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sts_wbr_jpn_09_openworld.questphase / h1006 / 5; sts_wbr_jpn_09_openworld.questphase / h1006 / 6; sts_wbr_jpn_09_openworld.questphase / h12 / 12; sts_wbr_jpn_09_openworld.questphase / h814 / 11; +3 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sts_wbr_jpn_09_netrunner.scene / scene / 217; sts_wbr_jpn_09_netrunner.scene / scene / 219; sts_wbr_jpn_09_netrunner.scene / scene / 230; sts_wbr_jpn_09_netrunner.scene / scene / 279; +4 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` | content candidate; journal anchor | `base-sts-wbr-jpn-09` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` | content candidate; forward dependency | `base-sts-wbr-jpn-09` |

Evidence shards for this dossier (including parent context): [base-sts-wbr-jpn-09](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wbr-jpn-09.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

100 repeated typed/socket path signatures in this selected graph context; 13 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h12 / 0 -> 7 -> 8 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 42 -> 43 -> 2 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `138cff49923a75e07348` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 41 -> 42 -> 43 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `19665e3783f6f51a7337` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` / scene / 1 -> 297 -> 299 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `415c2c7ab8d34be7e55a` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 70 -> 73 -> 75 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questCutControlNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; CutSource -> CutDestination |
| `1666d7526b9bab74f2e2` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 84 -> 105 -> 107 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> Active; Out -> In |
| `95d4997362b664c5c23b` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` / scene / 105 -> 82 -> 84 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `1d48bd7cbbaeca8257d2` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 67 -> 35 -> 40 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Succeeded; Out -> In |
| `1a9b8893087e174a603f` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h91 / 105 -> 107 -> 106 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `5e0fdd5c991cc4718977` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` / scene / 248 -> 85 -> 303 | questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `7ff0eae411231e617b77` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` / scene / 138 -> 139 -> 176 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `ebdaafaddefbc1080fe8` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` / scene / 82 -> 84 -> 279 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h0 / 3 | `h91` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":121,"socketName":"Failed"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h0 / 4 | `h814` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h814 / 21 | `h866` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h814 / 22 | `h946` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_openworld.questphase` / h0 / 5 | `h1006` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\sts_wbr_jpn_09.gamedef` | content candidate | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\sts_wbr_jpn_09.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\lipsync\en\sts_wbr_jpn_09_netrunner\merc_f_04_jap_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\lipsync\en\sts_wbr_jpn_09_netrunner\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `jpn_09_enemies_in_sight` | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_gameplay.questphase / h169 / 2; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_gameplay.questphase / h169 / 8; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_gameplay.questphase / h169 / 9; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_gameplay.questphase / h169 / 15; 6 total source locations in compressed evidence |
| `jpn_09_never_left_parking` | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\phases\sts_wbr_jpn_09_gameplay.questphase / h470 / 62; 1 total source locations in compressed evidence |
| `jpn_09_testdef` | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\sts_wbr_jpn_09.quest / h0 / 3; 1 total source locations in compressed evidence |

NodeRef uses: 65; TweakDB binding uses: 6. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene` | 21 / 122 | scnChangeIdleAnimEvent: 6; scnDialogLineEvent: 44; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 15; scnPlaySkAnimEvent: 37; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 15 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
