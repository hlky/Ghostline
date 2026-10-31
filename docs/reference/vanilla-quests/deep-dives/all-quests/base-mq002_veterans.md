# Gun Music

Journal: `quests/minor_quest/mq002_veterans` · `MinorQuest` · hash `255487383`.

**Coverage: journal-linked.** 22 exact journal-linked nodes in 5 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| The Aldecaldos must really be desperate. To come this close to the city, and deal with scavs no less… Risky move. Sounds like they could use a hand. (Primary) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro` |
| Help the nomads negotiate a deal. (Primary) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` |
| Defeat the scavengers. (Primary) | `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight` |
| Talk to Carol. (Primary) | `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq002_quest_bugfixes.questphase / h30 / 4` (PauseCondition) | `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary` | 3:Out → 4:In; 4:Out → 7:In |
| `mq002.questphase / h0 / 124` (Journal) | `quests/minor_quest/mq002_veterans` | 123:Out1 → 124:Succeeded; 124:Out → 125:In |
| `mq002.questphase / h0 / 134` (Condition) | `quests/minor_quest/mq002_veterans` | 151:Out → 134:In; 134:True → 135:Failed; 134:False → 142:In1 |
| `mq002.questphase / h0 / 135` (Journal) | `quests/minor_quest/mq002_veterans` | 134:True → 135:Failed; 135:Out → 142:In1 |
| `mq002.questphase / h0 / 137` (Journal) | `quests/minor_quest/mq002_veterans` | 137:Out → 125:In; 140:Out1 → 137:Failed |
| `mq002.questphase / h0 / 147` (Condition) | `quests/minor_quest/mq002_veterans` | 102:Out1 → 147:In; 147:True → 146:In1; 147:False → 152:In1 |
| `mq002_beginning.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro` | 39:Out → 14:Active; 14:Out → 38:Active |
| `mq002_beginning.questphase / h0 / 21` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro` | 28:Out → 21:Succeeded; 21:Out → 22:Active |
| `mq002_beginning.questphase / h0 / 22` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` | 21:Out → 22:Active; 22:Out → 24:Start 0 |
| `mq002_beginning.questphase / h0 / 25` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` | 24:to_combat → 25:Succeeded; 25:Out → 52:Active |
| `mq002_beginning.questphase / h0 / 36` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` | 24:to_outcome → 36:Succeeded; 36:Out → 35:In |
| `mq002_beginning.questphase / h0 / 38` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro/mq002_description` | 14:Out → 38:Active; 38:Out → 20:In |
| `mq002_beginning.questphase / h0 / 48` (Condition) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` | 48:False → 47:In1; 50:Out → 48:In; 51:False → 48:In; 48:True → 49:Inactive |
| `mq002_beginning.questphase / h0 / 49` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal` | 49:Out → 47:In1; 48:True → 49:Inactive |
| `mq002_beginning.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro` | 50:Out → 48:In; 51:True → 50:Inactive |
| `mq002_beginning.questphase / h0 / 51` (Condition) | `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro` | 51:False → 48:In; 51:True → 50:Inactive; 74:Out1 → 51:In |
| `mq002_beginning.questphase / h0 / 52` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight` | 25:Out → 52:Active; 47:Out1 → 52:Active; 52:Out → 55:In |
| `mq002_combat.questphase / h0 / 10` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight` | 10:Out → 1:In; 42:Out → 10:Succeeded |
| `mq002_combat.questphase / h621 / 10` (Condition) | `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight` | 10:False → 1:In; 10:True → 2:In; 10:True → 3:In; 10:True → 4:In; 9:Out → 10:In; 10:True → 11:In |
| `mq002_combat.questphase / h621 / 12` (Condition) | `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight` | 12:True → 5:In; 12:True → 6:In; 12:True → 7:In; 11:Out → 12:In; 12:True → 13:In1; 12:False → 15:In1 |
| `mq002_ending.questphase / h0 / 5` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary` | 0:Out → 5:Active; 5:Out → 11:Start 0 |
| `mq002_ending.questphase / h0 / 10` (Journal) | `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary` | 10:Out → 1:In; 26:Out → 10:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq002.questphase / h0 / 121` | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` | 121:sq027_suspension → 153:In; 121:to_combat → 122:In1; 128:Out1 → 121:In1; 121:to_outcome → 123:In1; 121:quest_fails → 138:In1 |
| `mq002.questphase / h0 / 122` | `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` | 121:to_combat → 122:In1; 122:Out1 → 123:In1; 127:Out → 122:In1; 122:quest_fails → 139:In1 |
| `mq002.questphase / h0 / 123` | `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` | 109:Out → 123:In1; 121:to_outcome → 123:In1; 122:Out1 → 123:In1; 123:Out1 → 124:Succeeded; 123:quest_fails → 140:In1 |
| `mq002.questphase / h661 / 7` | `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene`; `#mq002_04_sm_nomads_fluff` | 6:Out → 7:Start 0 |
| `mq002.questphase / h661 / 20` | `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene`; `#mq002_04_sm_nomads_fluff` | 19:Out → 20:Start 0 |
| `mq002_beginning.questphase / h0 / 23` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`; `#mq002_01_sm_deal` | 8:Out → 23:background_overhead; 28:CutSource → 23:CutDestination |
| `mq002_beginning.questphase / h0 / 24` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`; `#mq002_01_sm_deal` | 22:Out → 24:Start 0; 24:to_combat → 25:Succeeded; 24:to_outcome → 36:Succeeded |
| `mq002_beginning.questphase / h0 / 31` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`; `#mq002_01_sm_deal` | 28:CutSource → 31:CutDestination; 30:Out → 31:entered_area; 31:entered_area_out → 37:In2 |
| `mq002_beginning.questphase / h0 / 57` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`; `#mq002_01_sm_deal` | 30:Out → 57:idles |
| `mq002_combat.questphase / h0 / 14` | `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene`; `#mq002_02_sm_combat` | 144:False → 14:combat_starts; 14:combat_starts_out → 15:In |
| `mq002_combat.questphase / h0 / 16` | `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene`; `#mq002_02_sm_combat` | 15:Out → 16:veterans_banter; 144:True → 16:veterans_banter |
| `mq002_combat.questphase / h0 / 38` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`; `#mq002_01_sm_deal` | 37:True → 38:interruption_combat |
| `mq002_ending.questphase / h0 / 11` | `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene`; `#mq002_03_sm_summary` | 5:Out → 11:Start 0; 11:End 0 → 29:In; 11:End 0 → 26:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 23 | `mq002_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 23:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 12 | `mq002.questphase` | 173: Condition: mq002_done GreaterOrEqual 1; 173:False → 12:In1 |
| `base\quest\minor_quests\mq002\mq002.quest` / h0 / 25 | `mq002.questphase` | 14: Phase; 14: Phase; 21: UIManager; 25:Out1 → 3:In; 14:combat_out → 25:combat_in; 14:ending_out → 25:ending_in; 21:Out → 25:In1 |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 121 | `mq002_beginning.questphase` | 128: Phase; 121:sq027_suspension → 153:In; 121:to_combat → 122:In1; 128:Out1 → 121:In1; 121:to_outcome → 123:In1; 121:quest_fails → 138:In1 |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 122 | `mq002_combat.questphase` | 121: Phase: mq002_beginning.questphase; 127: Input; 121:to_combat → 122:In1; 122:Out1 → 123:In1; 127:Out → 122:In1; 122:quest_fails → 139:In1 |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 123 | `mq002_ending.questphase` | 109: Input; 121: Phase: mq002_beginning.questphase; 122: Phase: mq002_combat.questphase; 109:Out → 123:In1; 121:to_outcome → 123:In1; 122:Out1 → 123:In1; 123:Out1 → 124:Succeeded; 123:quest_fails → 140:In1 |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 23 | `mq002_01_deal.scene` | 8: PauseCondition: #mq002_tr_start; 28: CutControl; 8:Out → 23:background_overhead; 28:CutSource → 23:CutDestination |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 24 | `mq002_01_deal.scene` | 22: Journal; 22:Out → 24:Start 0; 24:to_combat → 25:Succeeded; 24:to_outcome → 36:Succeeded |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 31 | `mq002_01_deal.scene` | 28: CutControl; 30: PauseCondition: #mq002_tr_deal_area; 28:CutSource → 31:CutDestination; 30:Out → 31:entered_area; 31:entered_area_out → 37:In2 |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 57 | `mq002_01_deal.scene` | 30: PauseCondition: #mq002_tr_deal_area; 30:Out → 57:idles |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 38 | `mq002_01_deal.scene` | 37: Condition: mq002_deal_broken_combat; 37:True → 38:interruption_combat |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 14 | `mq002_02_combat.scene` | 144: Condition; 144:False → 14:combat_starts; 14:combat_starts_out → 15:In |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 16 | `mq002_02_combat.scene` | 15: PauseCondition: {"seconds": 2}; 144: Condition; 15:Out → 16:veterans_banter; 144:True → 16:veterans_banter |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h0 / 11 | `mq002_03_summary.scene` | 5: Journal; 5:Out → 11:Start 0; 11:End 0 → 29:In; 11:End 0 → 26:In |
| `base\quest\minor_quests\mq002\mq002.questphase` / h661 / 7 | `mq002_04_nomads_fluff.scene` | 6: PauseCondition; 6:Out → 7:Start 0 |
| `base\quest\minor_quests\mq002\mq002.questphase` / h661 / 20 | `mq002_04_nomads_fluff.scene` | 19: PauseCondition; 19:Out → 20:Start 0 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq002_01_deal.scene` | Start 0, background_overhead, idles, interruption_combat, entered_area → background_overhead_out, to_combat, to_outcome, interruption_combat_out, entered_area_out | Carol; Teddy; Cassidy; Scav_leader; nomad_01; nomad_02; scav_sniper; scav_02; scav_03; scav_04; scav_01; scav_05; van; Player; 130 nodes / 154 edges |
| `mq002_02_combat.scene` | veterans_banter, combat_starts → veterans_banter_out, combat_starts_out | Teddy; Cassidy; Carol; Player; 6 nodes / 4 edges |
| `mq002_03_summary.scene` | Start 0, Start 2, Start1, Start 3 → End 0 | Carol; Cassidy; Teddy; van; nomad_car_1; nomad_car_2; Player; 85 nodes / 94 edges |
| `mq002_04_nomads_fluff.scene` | Start 0 → End 0 | Nomad_01; Nomad_02; Player; 11 nodes / 13 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq002_01_deal.scene / n18 / 0` | They call me V. (`v`) | No option-level predicate stored | 0:0 → 20:0:0 |
| `mq002_01_deal.scene / n18 / 1` | Why do you need to know? (`why_care`) | No option-level predicate stored | 0:1 → 25:0:0 |
| `mq002_01_deal.scene / n18 / 2` | Something about this deal stinks. (`streetkid`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:2 → 128:0:0 |
| `mq002_01_deal.scene / n84 / 0` | Fuck... Sniper! (`sniper`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq002_sniper_noticed"}}, "bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127114866875", "buildId": "92409620733", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 87:0:0 |
| `mq002_01_deal.scene / n96 / 0` | Have it your way. (`attack`) | No option-level predicate stored | 0:0 → 98:0:0 |
| `mq002_01_deal.scene / n96 / 1` | That had nothing to do with the Aldecaldos. (`convince`) | No option-level predicate stored | 0:1 → 101:0:0 |
| `mq002_01_deal.scene / n96 / 2` | I'd think real hard about your next move. (`solo`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127114866875", "buildId": "75476658533", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 327:0:1 |
| `mq002_01_deal.scene / n110 / 0` | I came here alone. (`nope`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127114866875", "buildId": "92409620733", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 114:0:0 |
| `mq002_01_deal.scene / n110 / 1` | Why do I get the feeling something isn't right? (`problems`) | No option-level predicate stored | 0:1 → 112:0:0 |
| `mq002_01_deal.scene / n121 / 0` | I'll take a look and see what's going on. (`will check`) | No option-level predicate stored | 0:0 → 120:0:0 |
| `mq002_01_deal.scene / n121 / 1` | Dealing with the scavs never ends well. (`scavs deal`) | No option-level predicate stored | 0:1 → 125:0:0 |
| `mq002_01_deal.scene / n133 / 0` | You can't trust the scavs. (`donttrust`) | No option-level predicate stored | 0:0 → 136:0:0 |
| `mq002_01_deal.scene / n133 / 1` | Your guy outside was freaking out. (`worried`) | {"questCondition": {"$type": "questLogicalCondition", "operation": "OR", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq002_taco_guard_met"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq002_jeff_guard_met"}}]}} | 0:1 → 138:0:0 |
| `mq002_01_deal.scene / n133 / 2` | I could smell the trap from a mile away. (`streetkid`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:2 → 140:0:0 |
| `mq002_01_deal.scene / n245 / 0` | I came here alone. (`nope`) | No option-level predicate stored | 0:0 → 247:0:0 |
| `mq002_01_deal.scene / n245 / 1` | Why do I get the feeling something isn't right? (`problems`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127114866875", "buildId": "92409620733", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 246:0:0 |
| `mq002_01_deal.scene / n250 / 0` | I'll take a look and see what's going on. (`will check`) | No option-level predicate stored | 0:0 → 249:0:0 |
| `mq002_01_deal.scene / n250 / 1` | Dealing with the scavs never ends well. (`scavs deal`) | No option-level predicate stored | 0:1 → 251:0:0 |
| `mq002_03_summary.scene / n6 / 0` | I just wanted to help. (``) | No option-level predicate stored | 0:0 → 8:0:0 |
| `mq002_03_summary.scene / n6 / 1` | It would've ended up like this anyway. (``) | No option-level predicate stored | 0:1 → 10:0:0 |
| `mq002_03_summary.scene / n24 / 0` | You can pay me back some other time. (``) | No option-level predicate stored | 0:0 → 27:0:0 |
| `mq002_03_summary.scene / n24 / 1` | I don't abandon friends in need. (``) | No option-level predicate stored | 0:1 → 29:0:0 |
| `mq002_04_nomads_fluff.scene / n10 / 0` | Nie ma za co. (``) | No option-level predicate stored | 0:0 → 12:0:0 |
| `mq002_04_nomads_fluff.scene / n10 / 1` | Ratowanie ludziom dupy to moja specjalność. (``) | No option-level predicate stored | 0:1 → 15:0:0 |
| `mq002_04_nomads_fluff.scene / n28 / 0` | Nie ma za co. (``) | No option-level predicate stored | 0:0 → 29:0:0 |
| `mq002_04_nomads_fluff.scene / n28 / 1` | Ratowanie ludziom dupy to moja specjalność. (``) | No option-level predicate stored | 0:1 → 30:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | mq002_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-567649` | mq002_quest_bugfixes.questphase / h154 / 3 | mq002_quest_bugfixes.questphase / h154 / 2 |
| `CYB-599080` | mq002_quest_bugfixes.questphase / h96 / 3 | mq002_quest_bugfixes.questphase / h96 / 2 |
| `CYB-599403` | mq002_quest_bugfixes.questphase / h30 / 3 | mq002_quest_bugfixes.questphase / h30 / 2 |
| `carol_default_on` | mq002.questphase / h16 / 41; mq002.questphase / h295 / 21; mq002.questphase / h566 / 37 | No reader in selected context |
| `cassidy_default_on` | mq002.questphase / h16 / 43; mq002.questphase / h295 / 23; mq002.questphase / h566 / 39 | No reader in selected context |
| `mq002_active` | mq002.questphase / h0 / 125; mq002.questphase / h443 / 20; mq002.questphase / h566 / 44; mq002_beginning.questphase / h0 / 9; mq002_beginning.questphase / h81 / 20 | mq002_quest_bugfixes.questphase / h154 / 11; mq002_quest_bugfixes.questphase / h96 / 4 |
| `mq002_deal_broken_combat` | mq002_01_deal.scene / scene / 315 | mq002_combat.questphase / h0 / 37 |
| `mq002_deal_proceeded` | mq002_01_deal.scene / scene / 107 | mq002_03_summary.scene / scene / 16; mq002_ending.questphase / h0 / 23 |
| `mq002_done` | mq002.questphase / h0 / 126 | mq002_quest_bugfixes.questphase / h154 / 10 |
| `mq002_escaped` | mq002_beginning.questphase / h0 / 29; mq002_ending.questphase / h0 / 22 | No reader in selected context |
| `mq002_escaped_combat` | mq002_combat.questphase / h0 / 19 | No reader in selected context |
| `mq002_interruption_canceled` | mq002_01_deal.scene / scene / 327 | mq002_01_deal.scene / scene / 321 |
| `mq002_jeff_guard_met` | mq002_01_deal.scene / scene / 203 | mq002_01_deal.scene / scene / 133; mq002_04_nomads_fluff.scene / scene / 6 |
| `mq002_sniper_noticed` | mq002_01_deal.scene / scene / 149; mq002_beginning.questphase / h0 / 34 | mq002_01_deal.scene / scene / 152; mq002_01_deal.scene / scene / 84 |
| `mq002_taco_guard_met` | mq002_01_deal.scene / scene / 200 | mq002_01_deal.scene / scene / 133 |
| `nomad_camp_01_active_combat` | Producer outside selected context | mq002.questphase / h661 / 17 |
| `q115_point_of_no_return` | Producer outside selected context | mq002.questphase / h0 / 133; mq002.questphase / h661 / 4; mq002_quest_bugfixes.questphase / h154 / 13 |
| `sq004_done` | Producer outside selected context | mq002.questphase / h0 / 129; mq002_quest_bugfixes.questphase / h154 / 18 |
| `sq027_active` | Producer outside selected context | mq002.questphase / h0 / 153; mq002.questphase / h295 / 35; mq002_beginning.questphase / h0 / 10; mq002_quest_bugfixes.questphase / h154 / 17 |
| `sq027_camp_abandoned` | Producer outside selected context | mq002.questphase / h0 / 133; mq002.questphase / h0 / 153; mq002.questphase / h661 / 14; mq002_quest_bugfixes.questphase / h154 / 13; mq002_quest_bugfixes.questphase / h154 / 17 |
| `sq027_camp_moved` | Producer outside selected context | mq002.questphase / h16 / 58; mq002.questphase / h661 / 13 |
| `sq027_done` | Producer outside selected context | mq002.questphase / h295 / 37; mq002_beginning.questphase / h0 / 13 |
| `teddy_default_on` | mq002.questphase / h16 / 42; mq002.questphase / h295 / 22; mq002.questphase / h566 / 38 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | mq002_quest_bugfixes.questphase / h0 / 20 |

## Exact gates, joins and cancellation

<details><summary>130 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq002_quest_bugfixes.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 21:Out → 20:In |
| `mq002_quest_bugfixes.questphase / h30 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-599403"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq002_quest_bugfixes.questphase / h30 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans/mq002_veterans/04_summary","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 3:Out → 4:In; 4:Out → 7:In |
| `mq002_quest_bugfixes.questphase / h30 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_escape"}}` | 7:False → 1:In; 4:Out → 7:In; 7:True → 6:In |
| `mq002_quest_bugfixes.questphase / h30 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 6:Out → 10:In; 10:Out → 11:In |
| `mq002_quest_bugfixes.questphase / h96 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-599080"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq002_quest_bugfixes.questphase / h96 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_active","comparisonType":"Equal"}}}` | 3:Out → 4:In; 4:Out → 13:In |
| `mq002_quest_bugfixes.questphase / h154 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-567649"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq002_quest_bugfixes.questphase / h154 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_done"}}}` | 18:True → 10:In; 10:False → 11:In |
| `mq002_quest_bugfixes.questphase / h154 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_active"}}}` | 10:False → 11:In; 11:False → 12:In |
| `mq002_quest_bugfixes.questphase / h154 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterWorkspot_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#carol"},"spotRef":"#mq002_ws_carol_deal"}}}` | 12:False → 6:In; 11:False → 12:In |
| `mq002_quest_bugfixes.questphase / h154 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}]}}` | 3:Out → 13:In; 13:False → 17:In |
| `mq002_quest_bugfixes.questphase / h154 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_active","comparisonType":"Equal"}}]}}` | 13:False → 17:In; 17:Out → 18:In |
| `mq002_quest_bugfixes.questphase / h154 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq004_done"}}}` | 18:True → 10:In; 17:Out → 18:In |
| `mq002.questphase / h0 / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq004_done"}}}` | 2:Out → 129:In; 129:Out → 128:In1 |
| `mq002.questphase / h0 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}]}}` | 2:Out → 133:In; 133:Out → 151:Inactive |
| `mq002.questphase / h0 / 134` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 151:Out → 134:In; 134:True → 135:Failed; 134:False → 142:In1 |
| `mq002.questphase / h0 / 147` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 102:Out1 → 147:In; 147:True → 146:In1; 147:False → 152:In1 |
| `mq002.questphase / h0 / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_active","comparisonType":"Equal"}}]}}` | 121:sq027_suspension → 153:In; 128:sq027_suspension → 153:In; 153:Out → 128:In1 |
| `mq002.questphase / h16 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 49:Out → 23:In; 23:Out → 31:In; 23:Out → 32:In; 23:Out → 33:In |
| `mq002.questphase / h16 / 34` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 31:Out → 34:In1; 32:Out → 34:In2; 33:Out → 34:In3; 34:Out1 → 51:In |
| `mq002.questphase / h16 / 44` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 44:Out1 → 1:In; 41:Out → 44:In1; 42:Out → 44:In2; 43:Out → 44:In3 |
| `mq002.questphase / h16 / 58` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_moved","comparisonType":"Equal"}}}` | 58:True → 24:In; 58:False → 55:In; 70:Out1 → 58:In |
| `mq002.questphase / h16 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 50:Out → 61:In; 61:Out → 70:In1 |
| `mq002.questphase / h16 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_02"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 50:Out → 62:In; 62:Out → 70:In2 |
| `mq002.questphase / h16 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_01"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 67:Out → 68:In; 68:Out → 71:In1 |
| `mq002.questphase / h16 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_02"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 67:Out → 69:In; 69:Out → 71:In2 |
| `mq002.questphase / h16 / 70` | `questLogicalAndNodeDefinition` `{}` | 70:Out1 → 58:In; 61:Out → 70:In1; 62:Out → 70:In2 |
| `mq002.questphase / h16 / 71` | `questLogicalAndNodeDefinition` `{}` | 71:Out1 → 27:In; 68:Out → 71:In1; 69:Out → 71:In2 |
| `mq002.questphase / h295 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 8:Out → 11:In; 11:Out → 9:In |
| `mq002.questphase / h295 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 9:Out → 12:In; 12:Out → 33:In |
| `mq002.questphase / h295 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_nomads"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 14:Out → 15:In; 15:Out → 39:In |
| `mq002.questphase / h295 / 24` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 21:Out → 24:In1; 22:Out → 24:In2; 23:Out → 24:In3; 24:Out1 → 32:In |
| `mq002.questphase / h295 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_active"}}}` | 37:False → 35:In; 35:Out → 38:In1 |
| `mq002.questphase / h295 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_done"}}}` | 31:Out → 37:In; 37:False → 35:In |
| `mq002.questphase / h566 / 40` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 37:Out → 40:In1; 38:Out → 40:In2; 39:Out → 40:In3; 40:Out1 → 44:In |
| `mq002.questphase / h661 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_nomads"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 6:In |
| `mq002.questphase / h661 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 0:Out → 4:In; 4:Out → 15:In1 |
| `mq002.questphase / h661 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 3:Out → 6:In; 6:Out → 7:Start 0 |
| `mq002.questphase / h661 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_moved","comparisonType":"Equal"}}}` | 13:True → 2:In; 14:True → 13:In; 13:True → 17:In; 13:False → 16:In |
| `mq002.questphase / h661 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned","comparisonType":"Equal"}}}` | 0:Out → 14:In; 14:True → 13:In; 14:False → 15:In1 |
| `mq002.questphase / h661 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nomad_camp_01_active_combat"}}}` | 17:Out → 10:In; 13:True → 17:In |
| `mq002.questphase / h661 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_nomads"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 16:Out → 18:In; 18:Out → 19:In |
| `mq002.questphase / h661 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 18:Out → 19:In; 19:Out → 20:Start 0 |
| `mq002_beginning.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_start"}}` | 9:Out → 8:In; 8:Out → 23:background_overhead; 8:Out → 37:In1 |
| `mq002_beginning.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_active"}}}` | 13:False → 10:In; 10:Out → 16:In1 |
| `mq002_beginning.questphase / h0 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_done"}}}` | 0:Out → 13:In; 13:False → 10:In |
| `mq002_beginning.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 28:Out → 18:In; 18:Out → 27:In |
| `mq002_beginning.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_interruption"}}` | 38:Out → 20:In; 20:Out → 28:In |
| `mq002_beginning.questphase / h0 / 28` | `questCutControlNodeDefinition` `{}` | 28:Out → 18:In; 20:Out → 28:In; 28:Out → 21:Succeeded; 28:CutSource → 23:CutDestination; 28:CutSource → 31:CutDestination |
| `mq002_beginning.questphase / h0 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_deal_area"}}` | 0:Out → 30:In; 30:Out → 31:entered_area; 30:Out → 57:idles |
| `mq002_beginning.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_06_sniper"]},"timeInterval":3.0,"angleTolerance":5.0}}}` | 0:Out → 32:In; 32:Out → 34:In |
| `mq002_beginning.questphase / h0 / 37` | `questLogicalXorNodeDefinition` `{}` | 8:Out → 37:In1; 31:entered_area_out → 37:In2; 37:Out1 → 39:Inactive |
| `mq002_beginning.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans/mq002_veterans/02_deal","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 48:False → 47:In1; 50:Out → 48:In; 51:False → 48:In; 48:True → 49:Inactive |
| `mq002_beginning.questphase / h0 / 51` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans/mq002_veterans/01_intro","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 51:False → 48:In; 51:True → 50:Inactive; 74:Out1 → 51:In |
| `mq002_beginning.questphase / h0 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cassidy"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 60:In; 60:Out → 43:In |
| `mq002_beginning.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#teddy"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 61:In; 61:Out → 44:In |
| `mq002_beginning.questphase / h0 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 64:Out → 62:In; 62:Out → 65:In |
| `mq002_beginning.questphase / h0 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_escape"}}` | 0:Out → 63:In; 65:Out → 63:In; 63:Out → 64:In |
| `mq002_beginning.questphase / h0 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers"}}}}` | 67:Out → 66:In; 66:Out → 74:In1 |
| `mq002_beginning.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["leader"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 68:In; 68:Out → 74:In2 |
| `mq002_beginning.questphase / h0 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_01"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 69:In; 69:Out → 74:In3 |
| `mq002_beginning.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_02"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 70:In; 70:Out → 74:In4 |
| `mq002_beginning.questphase / h0 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_03"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 71:In; 71:Out → 74:In5 |
| `mq002_beginning.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_04"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 72:In; 72:Out → 74:In6 |
| `mq002_beginning.questphase / h0 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_05"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 67:Out → 73:In; 73:Out → 74:In7 |
| `mq002_beginning.questphase / h0 / 74` | `questLogicalXorNodeDefinition` `{"inputSocketCount":7}` | 74:Out1 → 51:In; 66:Out → 74:In1; 68:Out → 74:In2; 69:Out → 74:In3; 70:Out → 74:In4; 71:Out → 74:In5; 72:Out → 74:In6; 73:Out → 74:In7 |
| `mq002_beginning.questphase / h402 / 14` | `questLogicalAndNodeDefinition` `{"inputSocketCount":5}` | 14:Out1 → 1:In; 2:Out → 14:In1; 10:Out → 14:In2; 11:Out → 14:In3; 12:Out → 14:In4; 13:Out → 14:In5 |
| `mq002_beginning.questphase / h402 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 15:In; 15:Out → 2:In; 15:Out → 10:In; 15:Out → 11:In; 15:Out → 12:In; 15:Out → 13:In |
| `mq002_combat.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["leader"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 9:In; 9:Out → 36:In1 |
| `mq002_combat.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 14:combat_starts_out → 15:In; 15:Out → 16:veterans_banter |
| `mq002_combat.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 24:In; 24:Out → 36:In3 |
| `mq002_combat.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 25:In; 25:Out → 36:In4 |
| `mq002_combat.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_04"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 26:In; 26:Out → 36:In5 |
| `mq002_combat.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_05"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 27:In; 27:Out → 36:In6 |
| `mq002_combat.questphase / h0 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_06_sniper"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 43:Out → 28:In; 28:Out → 36:In7 |
| `mq002_combat.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 40:Out → 35:In; 35:Out → 36:In2 |
| `mq002_combat.questphase / h0 / 36` | `questLogicalAndNodeDefinition` `{"inputSocketCount":7}` | 9:Out → 36:In1; 24:Out → 36:In3; 25:Out → 36:In4; 26:Out → 36:In5; 27:Out → 36:In6; 28:Out → 36:In7; 35:Out → 36:In2; 36:Out1 → 129:In; 36:Out1 → 130:In; 36:Out1 → 131:In |
| `mq002_combat.questphase / h0 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_deal_broken_combat"}}}` | 0:Out → 37:In; 37:True → 38:interruption_combat |
| `mq002_combat.questphase / h0 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 135:Out → 4:In; 136:Out → 135:In |
| `mq002_combat.questphase / h0 / 143` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 143:Out1 → 42:In; 129:Success → 143:In3; 130:Success → 143:In2; 131:Success → 143:In1 |
| `mq002_combat.questphase / h0 / 144` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_06_sniper"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 144:In; 144:False → 14:combat_starts; 144:True → 16:veterans_banter |
| `mq002_combat.questphase / h621 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_deal_area"}}` | 0:Out → 9:In; 14:Out1 → 9:In; 9:Out → 10:In |
| `mq002_combat.questphase / h621 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans/mq002_veterans/03_fight","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:False → 1:In; 10:True → 2:In; 10:True → 3:In; 10:True → 4:In; 9:Out → 10:In; 10:True → 11:In |
| `mq002_combat.questphase / h621 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq002_tr_deal_area"}}` | 10:True → 11:In; 11:Out → 12:In |
| `mq002_combat.questphase / h621 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq002_veterans/mq002_veterans/03_fight","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 12:True → 5:In; 12:True → 6:In; 12:True → 7:In; 11:Out → 12:In; 12:True → 13:In1; 12:False → 15:In1 |
| `mq002_ending.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq002_tr_escape"}}` | 0:Out → 3:In; 29:CutSource → 3:CutDestination; 3:Out → 4:In; 3:Out → 30:In |
| `mq002_ending.questphase / h0 / 23` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_deal_proceeded"}}}` | 0:Out → 23:In; 23:True → 25:In1 |
| `mq002_ending.questphase / h0 / 29` | `questCutControlNodeDefinition` `{}` | 29:CutSource → 3:CutDestination; 11:End 0 → 29:In; 29:Out → 27:In1 |
| `mq002_ending.questphase / h81 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_06_sniper"]},"timeInterval":2.0,"onScreenTest":true,"inverted":true}}}` | 33:Out → 2:In; 2:Out → 5:In |
| `mq002_ending.questphase / h81 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_01"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_01"]}}}}` | 6:Out → 10:In; 10:Out → 14:In1 |
| `mq002_ending.questphase / h81 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_01"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_02"]}}}}` | 7:Out → 11:In; 11:Out → 14:In2 |
| `mq002_ending.questphase / h81 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_01"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["leader"]}}}}` | 8:Out → 12:In; 12:Out → 14:In3 |
| `mq002_ending.questphase / h81 / 14` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 10:Out → 14:In1; 11:Out → 14:In2; 12:Out → 14:In3; 14:Out1 → 18:In |
| `mq002_ending.questphase / h81 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_01"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 40:Out → 17:In; 17:Out → 28:In2 |
| `mq002_ending.questphase / h81 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 14:Out1 → 18:In; 18:Out → 15:In |
| `mq002_ending.questphase / h81 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_02"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_03"]}}}}` | 19:Out → 21:In; 21:Out → 23:In1 |
| `mq002_ending.questphase / h81 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_02"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_04"]}}}}` | 20:Out → 22:In; 22:Out → 23:In2 |
| `mq002_ending.questphase / h81 / 23` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 21:Out → 23:In1; 22:Out → 23:In2; 30:Out → 23:In3; 23:Out1 → 24:In |
| `mq002_ending.questphase / h81 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 23:Out1 → 24:In; 24:Out → 25:In |
| `mq002_ending.questphase / h81 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_02"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 41:Out → 27:In; 27:Out → 28:In3 |
| `mq002_ending.questphase / h81 / 28` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 5:Out → 28:In1; 17:Out → 28:In2; 27:Out → 28:In3; 28:Out1 → 34:In |
| `mq002_ending.questphase / h81 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["scav_02"]},"childRef":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_05"]}}}}` | 30:Out → 23:In3; 29:Out → 30:In |
| `mq002_ending.questphase / h388 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"childRef":{"$type":"gameEntityReference","reference":"#cassidy"},"enterAnimationFinished":true}}}` | 6:Out → 10:In; 10:Out → 14:In1 |
| `mq002_ending.questphase / h388 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"childRef":{"$type":"gameEntityReference","reference":"#teddy"},"enterAnimationFinished":true}}}` | 7:Out → 11:In; 11:Out → 14:In2 |
| `mq002_ending.questphase / h388 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_02"]},"childRef":{"$type":"gameEntityReference","reference":"#carol"},"enterAnimationFinished":true}}}` | 8:Out → 12:In; 12:Out → 57:In |
| `mq002_ending.questphase / h388 / 14` | `questLogicalAndNodeDefinition` `{}` | 10:Out → 14:In1; 11:Out → 14:In2; 14:Out1 → 58:In |
| `mq002_ending.questphase / h388 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 56:Out → 17:In; 17:Out → 41:In |
| `mq002_ending.questphase / h388 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_02"]},"timeInterval":15.0,"onScreenTest":true,"inverted":true}}}` | 55:Out → 27:In; 27:Out → 40:In |
| `mq002_ending.questphase / h388 / 28` | `questLogicalAndNodeDefinition` `{}` | 43:Out → 28:In1; 44:Out → 28:In2; 28:Out1 → 59:In |
| `mq002_ending.questphase / h388 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 64:Out → 46:In; 64:Out → 56:In; 58:Out → 64:In |
| `mq002_ending.questphase / h388 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 65:Out → 55:In; 57:Out → 65:In; 65:Out → 68:In |
| `mq002_ending.questphase / h388 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"childRef":{"$type":"gameEntityReference","reference":"#cassidy"}}}}` | 65:Out → 68:In; 68:Out → 69:In |
| `mq002_ending.questphase / h388 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 69:Out → 47:In; 68:Out → 69:In |
| `mq002_01_deal.scene / scene / 67` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0},"comparisonType":"LessOrEqual"}}}` | 66:0:0 → 67:0:1; 67:0:0 → 200:0:1; 67:0:1 → 69:0:1 |
| `mq002_01_deal.scene / scene / 69` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_02"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0},"comparisonType":"LessOrEqual"}}}` | 67:0:1 → 69:0:1; 69:0:0 → 203:0:1 |
| `mq002_01_deal.scene / scene / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4,"miliseconds":500}}}` | 37:0:0 → 89:0:1; 89:0:0 → 56:0:0; 89:0:0 → 84:1:0; 89:0:0 → 87:1:0; 90:1:0 → 89:0:0 |
| `mq002_01_deal.scene / scene / 152` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_sniper_noticed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 147:0:0 → 152:0:1; 152:0:0 → 154:0:0; 152:0:1 → 156:0:0 |
| `mq002_01_deal.scene / scene / 307` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["leader"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 301:0:0 → 307:0:1; 307:0:0 → 571:0:1; 322:1:0 → 307:0:0 |
| `mq002_01_deal.scene / scene / 321` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_interruption_canceled"}}}` | 301:0:0 → 321:0:1; 321:0:0 → 322:0:0 |
| `mq002_01_deal.scene / scene / 330` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["leader"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 330:0:0 → 18:1:0; 330:0:0 → 331:0:1; 335:0:0 → 330:0:1; 338:1:0 → 330:0:0 |
| `mq002_01_deal.scene / scene / 567` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq002_com_scavengers","names":["scav_06_sniper"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 301:0:0 → 567:0:1; 322:1:0 → 567:0:0; 567:0:0 → 571:0:0 |
| `mq002_03_summary.scene / scene / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_deal_proceeded"}}}` | 1:0:0 → 16:0:1; 16:0:0 → 23:0:0; 16:0:1 → 4:0:0 |
| `mq002_03_summary.scene / scene / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_01"]},"timeInterval":5.0,"inverted":true}}}` | 78:0:0 → 90:0:1; 90:0:0 → 96:0:1 |
| `mq002_03_summary.scene / scene / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq002_com_nomads","names":["nomad_02"]},"timeInterval":5.0,"inverted":true}}}` | 80:0:0 → 92:0:1; 92:0:0 → 94:0:1 |
| `mq002_03_summary.scene / scene / 152` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterEquippedItem_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#teddy"},"itemID":"123639056143"}}}` | 1:0:0 → 152:0:1; 152:0:0 → 46:0:1; 152:0:1 → 150:0:1; 232:0:0 → 152:0:1 |
| `mq002_03_summary.scene / scene / 326` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"childRef":{"$type":"gameEntityReference","reference":"#cassidy"}}}}` | 316:0:0 → 326:0:1; 326:0:0 → 306:0:2 |
| `mq002_03_summary.scene / scene / 327` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_01"]},"childRef":{"$type":"gameEntityReference","reference":"#teddy"}}}}` | 318:0:0 → 327:0:1; 327:0:0 → 306:0:1 |
| `mq002_03_summary.scene / scene / 328` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq002_com_deal_vehicles","names":["nomad_main_02"]},"childRef":{"$type":"gameEntityReference","reference":"#carol"}}}}` | 322:0:0 → 328:0:1; 328:0:0 → 306:0:0 |
| `mq002_04_nomads_fluff.scene / scene / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq002_jeff_guard_met"}}}` | 1:0:0 → 6:0:1; 6:0:0 → 8:0:0; 6:0:1 → 27:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq002.questphase / h295 / 11; mq002.questphase / h295 / 12; mq002.questphase / h295 / 15; mq002.questphase / h661 / 18; +4 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq002_03_summary.scene / scene / 304; mq002_03_summary.scene / scene / 308; mq002_03_summary.scene / scene / 312; mq002_03_summary.scene / scene / 42; +2 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq002_combat.questphase / h0 / 20 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | mq002.questphase / h0 / 143 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq002_01_deal.scene / scene / 110; mq002_01_deal.scene / scene / 121; mq002_01_deal.scene / scene / 133; mq002_01_deal.scene / scene / 18; +8 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq002_combat.questphase / h0 / 100; mq002_combat.questphase / h0 / 101; mq002_combat.questphase / h0 / 102; mq002_combat.questphase / h0 / 103; +41 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq002.questphase / h16 / 27; mq002.questphase / h16 / 29; mq002.questphase / h16 / 39; mq002.questphase / h16 / 66; +27 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq002.questphase / h0 / 129; mq002.questphase / h0 / 133; mq002.questphase / h0 / 153; mq002.questphase / h16 / 58; +26 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq002.questphase / h0 / 148; mq002.questphase / h16 / 49; mq002.questphase / h443 / 23; mq002_beginning.questphase / h0 / 64; +3 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq002_combat.questphase / h0 / 40; mq002_combat.questphase / h0 / 43; mq002_combat.questphase / h0 / 46; mq002_combat.questphase / h0 / 49 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `journal_transition` | mq002.questphase / h0 / 124; mq002.questphase / h0 / 135; mq002.questphase / h0 / 137; mq002.questphase / h0 / 151; +18 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | mq002_03_summary.scene / scene / 326; mq002_03_summary.scene / scene / 327; mq002_03_summary.scene / scene / 328; mq002_ending.questphase / h388 / 10; +9 locations in catalogue.json | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq002.questphase / h16 / 34; mq002.questphase / h16 / 44; mq002.questphase / h16 / 70; mq002.questphase / h16 / 71; +10 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq002.questphase / h0 / 125; mq002.questphase / h0 / 126; mq002.questphase / h16 / 41; mq002.questphase / h16 / 42; +25 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq002_beginning.questphase / h0 / 37; mq002_beginning.questphase / h0 / 74 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq002_01_deal.scene / scene / 89; mq002_combat.questphase / h0 / 15; mq002_ending.questphase / h388 / 64; mq002_ending.questphase / h388 / 65; +3 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq002_beginning.questphase / h0 / 28; mq002_ending.questphase / h0 / 29 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq002_ending.questphase / h0 / 26 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq002.questphase / h661 / 20; mq002.questphase / h661 / 7; mq002_beginning.questphase / h0 / 23; mq002_beginning.questphase / h0 / 24; +6 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq002.questphase / h16 / 23; mq002_beginning.questphase / h0 / 18; mq002_beginning.questphase / h0 / 20; mq002_beginning.questphase / h0 / 30; +9 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq002_combat.questphase / h0 / 144; mq002_combat.questphase / h0 / 24; mq002_combat.questphase / h0 / 25; mq002_combat.questphase / h0 / 26; +4 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq002_03_summary.scene / scene / 316; mq002_03_summary.scene / scene / 318; mq002_03_summary.scene / scene / 322; mq002_ending.questphase / h388 / 46; +12 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq002_01_deal.scene / scene / 271; mq002_01_deal.scene / scene / 273; mq002_01_deal.scene / scene / 275; mq002_01_deal.scene / scene / 276; +67 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq002.questphase / h16 / 50; mq002.questphase / h295 / 34; mq002.questphase / h443 / 24; mq002.questphase / h566 / 45; +4 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` | repair; journal anchor | `base-mq002` |
| `base\quest\minor_quests\mq002\mq002.questphase` | content candidate; journal anchor | `base-mq002` |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` | content candidate; journal anchor | `base-mq002` |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` | content candidate; journal anchor | `base-mq002` |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` | content candidate; journal anchor | `base-mq002` |
| `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` | content candidate; forward dependency | `base-mq002` |
| `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene` | content candidate; forward dependency | `base-mq002` |
| `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene` | content candidate; forward dependency | `base-mq002` |
| `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene` | content candidate; forward dependency | `base-mq002` |

Evidence shards for this dossier (including parent context): [base-mq002](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq002.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

350 repeated typed/socket path signatures in this selected graph context; 76 distinct direct resource identities; 15 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `20a77143a898bc753a26` | `base\quest\minor_quests\mq002\mq002.questphase` / h16 / 27 -> 29 -> 39 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 311 -> 305 -> 312 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h30 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `10de5d2a81ab97879de5` | `base\quest\minor_quests\mq002\mq002.questphase` / h16 / 42 -> 44 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out -> In2; Out1 -> In |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h0 / 19 -> 21 -> 20 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `a53561b4c002bc02b58a` | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 14 -> 38 -> 20 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> Active; Out -> In |
| `3fe0ae98a8cf5496b004` | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 64 -> 62 -> 65 | questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]; Out -> In; Out -> In |
| `eb252b7e42db30cea85d` | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 63 -> 64 -> 62 | questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 395 -> 385 -> 387 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 248 -> 250 -> 249 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `02ad6c50ebc6c8472fdf` | `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h96 / 2 -> 3 -> 4 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; False -> In; Out -> In |
| `276aca4a2dc348a877d5` | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 30 -> 13 -> 271 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h0 / 12 | `h30` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h0 / 17 | `h96` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h0 / 23 | `h154` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 102 | `h16` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 128 | `h295` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":36,"socketName":"sq027_suspension"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h295 / 38 | `h443` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 142 | `h566` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 146 | `h661` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\mq002.questphase` / h0 / 152 | `h802` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 16 | `h81` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 59 | `h402` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 137 | `h621` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h0 / 25 | `h81` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h0 / 27 | `h388` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq002\mq002.gamedef` | content candidate | base\quest\minor_quests\mq002\mq002.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\corpo_male\interactive_scene\corpo_male__stand__rh_gun.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_rifle__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__r_shoulder_rifle__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand_wall_lean180__2h_rifle__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand_wall_lean180__rh_rifle__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy_big\interactive_scene\dirtboy_big__stand__2h_rifle__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__rh_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\open_world\generic_female_average_work__stand__rh_windshield_wiper__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male__stand__rh_gun_aim__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_back__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_gun__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average__stand__lh_hip_rh_phone__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q003\q003_03_deal\body\q003_03_deal__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq006\sq006_01a_apartment_welcome\sq006_01a_apartment_welcome__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\carol.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\cassidy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\gang_ald_m_02_arb_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\gang_ald_m_03_nat_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\gang_scv_m_08_rus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\teddy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_01_deal\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_02_combat\carol.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_02_combat\cassidy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_02_combat\teddy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_02_combat\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_03_summary\carol.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_03_summary\cassidy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_03_summary\teddy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_03_summary\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_04_nomads_fluff\gang_ald_m_02_arb_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_04_nomads_fluff\gang_ald_m_03_nat_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\lipsync\en\mq002_04_nomads_fluff\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\dirtboy\dirtboy__stand_rifle__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\bodyguard__stand_ground__2h_front__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\dirtboy__stand_ground_rifle__guard__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\dirtboy__stand_ground_rifle__guard__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__guard__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__phone_talk__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__10.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_gun__nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_window__clean__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\dirt__stand_wall_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\dirt__stand_wall_lean_back_riffle__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\dirt__stand_wall_lean_back_riffle__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\ground\player__stand__handgun__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q202\q202_05_convoy\q202__river__stand_wall_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `carol_default_on` | base\quest\main_quests\part1\q114\phases\debug\q114_debug_setup.questphase / h75 / 6; base\quest\main_quests\part1\q114\phases\q114_new_camp.questphase / h201 / 6; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 11; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 12; 23 total source locations in compressed evidence |
| `cassidy_default_on` | base\quest\main_quests\part1\q114\phases\debug\q114_debug_setup.questphase / h75 / 7; base\quest\main_quests\part1\q114\phases\q114_new_camp.questphase / h201 / 7; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 5; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 6; 26 total source locations in compressed evidence |
| `mq002_done` | ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 630; ep1\quest\test\ep1_chicken_test.scene / scene / 251; ep1\quest\test\ep1_chicken_test.scene / scene / 253; ep1\quest\test\ep1_chicken_test.scene / scene / 255; 4 total source locations in compressed evidence |
| `nomad_camp_01_active_combat` | base\open_world\community\badlands\inland_avenue\bad_ina_phase.questphase / h2494 / 23; base\open_world\community\badlands\inland_avenue\bad_ina_phase.questphase / h2494 / 32; base\open_world\community\badlands\inland_avenue\bad_ina_phase.questphase / h3452 / 11; base\quest\side_quests\sq027\phases\sq027_05_camp_attack.questphase / h411 / 69; 6 total source locations in compressed evidence |
| `q115_point_of_no_return` | base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase / h1024 / 46; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 239; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.questphase / h0 / 139; base\quest\main_quests\epilogue\q204\q204_reborn.quest / h0 / 7; 19 total source locations in compressed evidence |
| `sq004_done` | base\quest\minor_quests\mq001\mq001.quest / h0 / 26; base\quest\minor_quests\mq002\mq002.quest / h0 / 27; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 187; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 225; 12 total source locations in compressed evidence |
| `sq027_active` | base\quest\side_quests\sq027\phases\sq027_01_nomad_camp.questphase / h0 / 85; base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest / h0 / 44; base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h173 / 77; 3 total source locations in compressed evidence |
| `sq027_camp_abandoned` | base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h491 / 4; base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h578 / 4; 2 total source locations in compressed evidence |
| `sq027_camp_moved` | base\quest\minor_quests\mq021\mq021.quest / h0 / 22; base\quest\main_quests\part1\q114\phases\debug\q114_debug_setup.questphase / h0 / 26; base\quest\main_quests\part1\q114\phases\q114_01_main_nomad_camp.questphase / h83 / 13; base\quest\main_quests\part1\q114\phases\q114_01_main_nomad_camp.questphase / h148 / 14; 19 total source locations in compressed evidence |
| `sq027_done` | base\quest\minor_quests\mq021\mq021.quest / h70 / 11; base\quest\minor_quests\mq026\test\mq026_00_chickentest.scene / scene / 239; base\quest\main_quests\part1\q115\test\q115_00_chickentest.scene / scene / 577; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 185; 6 total source locations in compressed evidence |
| `teddy_default_on` | base\quest\main_quests\part1\q114\phases\debug\q114_debug_setup.questphase / h75 / 8; base\quest\main_quests\part1\q114\phases\q114_new_camp.questphase / h201 / 8; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 9; base\quest\main_quests\part1\q114\phases\subphases\q114_nomad_scenes.questphase / h7 / 10; 26 total source locations in compressed evidence |

NodeRef uses: 485; TweakDB binding uses: 92. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` | 33 / 262 | scnAudioEvent: 11; scnChangeIdleAnimEvent: 11; scnDialogLineEvent: 84; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 45; scnPlaySkAnimEvent: 48; scnUnmountEvent: 1; scneventsEquipItemToPerformer: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 54; scneventsUnequipItemFromPerformer: 1; scneventsVFXDurationEvent: 2 |
| `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene` | 2 / 3 | scnDialogLineEvent: 3 |
| `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene` | 14 / 139 | scnChangeIdleAnimEvent: 8; scnDialogLineEvent: 19; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtEvent: 24; scnPlaySkAnimEvent: 28; scnPoseCorrectionEvent: 4; scnUnmountEvent: 3; scneventsEquipItemToPerformer: 4; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 33; scneventsUnequipItemFromPerformer: 1; scneventsUnequipItemFromPerformerByItem: 3 |
| `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene` | 6 / 22 | scnDialogLineEvent: 10; scnLookAtEvent: 12 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
