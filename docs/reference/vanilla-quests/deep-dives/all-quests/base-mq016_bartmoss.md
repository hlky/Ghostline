# KOLD MIRAGE

Journal: `quests/minor_quest/mq016_bartmoss` · `MinorQuest` · hash `2044425594`.

**Coverage: journal-linked.** 35 exact journal-linked nodes in 6 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| See where the coordinates lead. (Primary) | `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill` |
| Always somethin' interesting to be found at the dump. Take a half-dead, half-brain merc with an experimental chip in their head for example. Or, in this case, a freezer from 2020… a glimpse into the past. (Primary) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` |
| Talk to Johnny. (Primary) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` |
| Scan the freezer. (Primary) | `quests/minor_quest/mq016_bartmoss/01_warehouse/03_scan_coffin` |
| Take the deck. (Primary) | `quests/minor_quest/mq016_bartmoss/01_warehouse/04_take_cyberdeck` |
| Go to the Afterlife and talk to Nix. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix` |
| Follow Nix. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/02_follow_nix` |
| Place the deck on Nix's desk. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/03_give_nix` |
| Wait for Nix to finish the decryption. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/04_wait_for_nix` |
| Find a way to save Nix. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/05_find_way_to_help` |
| Talk to Nix. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/06_talk_with_nix` |
| Talk to Nix if you change your mind. (Optional) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix1` |
| Open your inventory and examine Bartmoss' deck. (Primary) | `quests/minor_quest/mq016_bartmoss/02_afterlife/06_watch_bartmoss_log` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq016_bartmoss.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq016_bartmoss` | 3:Out1 → 8:Succeeded; 8:Out → 13:In |
| `mq016_00_shard.questphase / h0 / 6` (Condition) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin`; `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` | 6:True → 2:In; 3:Out → 6:In; 6:False → 8:Active |
| `mq016_00_shard.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill` | 8:Out → 2:In; 6:False → 8:Active |
| `mq016_01_freezer.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` | 9:Out → 4:in; 14:False → 9:Active; 13:Out → 9:Active; 9:Out → 15:Active |
| `mq016_01_freezer.questphase / h0 / 14` (Condition) | `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill` | 8:Out → 14:In; 14:False → 9:Active; 14:True → 13:Succeeded |
| `mq016_01_freezer.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill` | 13:Out → 9:Active; 14:True → 13:Succeeded |
| `mq016_01_freezer.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin/description` | 9:Out → 15:Active |
| `mq016_01_freezer.questphase / h12 / 13` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill` | 13:Out → 7:In; 11:Out → 13:Active |
| `mq016_02_afterlife.questphase / h0 / 10` (MappinManager) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix/nix` | 12:Out → 10:Active |
| `mq016_02_afterlife.questphase / h12 / 7` (MappinManager) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix/nix` | 7:Out → 1:In; 5:Out → 7:Active |
| `mq016_01_freezer.scene / scene / 26` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` | 26:0:0 → 296:0:1; 193:0:0 → 26:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 30` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` | 591:0:0 → 30:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 45` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` | 45:0:0 → 642:0:3; 461:0:0 → 45:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 47` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/03_scan_coffin` | 47:0:0 → 522:0:1; 642:0:0 → 47:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 155` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/04_take_cyberdeck` | 155:0:0 → 470:0:0; 312:0:0 → 155:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 161` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/04_take_cyberdeck` | 161:0:0 → 453:0:1; 294:0:0 → 161:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 308` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/03_scan_coffin` | 174:0:0 → 308:0:3; 308:0:0 → 310:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 310` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` | 308:0:0 → 310:0:1; 310:0:0 → 457:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 312` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` | 312:0:0 → 155:0:1; 620:0:0 → 312:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 453` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix` | 161:0:0 → 453:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 636` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` | 638:0:0 → 636:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 638` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny` | 90:0:0 → 638:0:3; 638:0:0 → 636:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_01_freezer.scene / scene / 642` (Journal) | `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin` | 45:0:0 → 642:0:3; 642:0:0 → 47:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 76` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/03_give_nix` | 76:0:0 → 69:0:0; 934:0:0 → 76:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 158` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix` | 155:0:0 → 158:0:2; 158:0:0 → 160:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 160` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix1` | 158:0:0 → 160:0:1; 160:0:0 → 499:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 251` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix` | 49:0:0 → 251:0:3; 251:0:0 → 173:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 254` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix1` | 152:0:0 → 254:0:3; 254:0:0 → 173:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 389` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/03_give_nix` | 276:0:0 → 389:0:3; 389:0:0 → 391:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 391` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/04_wait_for_nix` | 389:0:0 → 391:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 393` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/04_wait_for_nix` | 64:2:0 → 393:0:2; 393:0:0 → 395:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 395` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/05_find_way_to_help` | 393:0:0 → 395:0:1; 395:0:0 → 654:0:1; 395:0:0 → 1040:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 450` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/05_find_way_to_help` | 447:0:0 → 450:0:3; 450:0:0 → 995:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 457` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/06_talk_with_nix` | 457:0:0 → 348:0:0; 1014:0:0 → 457:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq016_02_afterlife.scene / scene / 465` (Journal) | `quests/minor_quest/mq016_bartmoss/02_afterlife/06_talk_with_nix` | 383:0:0 → 465:0:3; 465:0:0 → 102:0:0; 465:0:0 → 772:0:1; 465:0:0 → 1107:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq016_bartmoss.questphase / h0 / 2` | `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` | 0:Out → 2:In1; 12:Out → 2:In1; 2:Out1 → 6:In |
| `mq016_bartmoss.questphase / h0 / 3` | `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` | 4:Out → 3:In1; 6:Out → 3:In1; 3:Out1 → 8:Succeeded |
| `mq016_bartmoss.questphase / h0 / 11` | `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` | 0:Out → 11:In1; 12:Out → 11:In1 |
| `mq016_01_freezer.questphase / h0 / 4` | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene`; `#mq016_01_sm_freezer` | 4:out → 1:In; 9:Out → 4:in |
| `mq016_02_afterlife.questphase / h0 / 3` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene`; `#mq016_02_sm_afterlife` | 3:out_decrypted → 1:In; 12:Out → 3:in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 5 | `mq016_bartmoss.questphase` | 135: FactsDBManager: mq016_active; 135:Out → 5:In1 |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` / h0 / 3 | `mq016_bartmoss.questphase` | 2: Scene: mq016_00_chickentest.scene; 2: Scene: mq016_00_chickentest.scene; 2: Scene: mq016_00_chickentest.scene; 3:Out1 → 1:In; 2:out_landfill → 3:In1; 2:out_shard → 3:InShard; 2:out_afterlife → 3:InAfterlife |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 11 | `mq016_00_shard.questphase` | 0: Input; 12: Input; 0:Out → 11:In1; 12:Out → 11:In1 |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 2 | `mq016_01_freezer.questphase` | 0: Input; 12: Input; 0:Out → 2:In1; 12:Out → 2:In1; 2:Out1 → 6:In |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 3 | `mq016_02_afterlife.questphase` | 4: Input; 6: Checkpoint; 4:Out → 3:In1; 6:Out → 3:In1; 3:Out1 → 8:Succeeded |
| `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` / h0 / 4 | `mq016_01_freezer.scene` | 9: Journal; 4:out → 1:In; 9:Out → 4:in |
| `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` / h0 / 3 | `mq016_02_afterlife.scene` | 12: PauseCondition: #mq016_tr_afterlife_entrance; 3:out_decrypted → 1:In; 12:Out → 3:in |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq016_01_freezer.scene` | in → out, End 1 | johnny; Player; 97 nodes / 105 edges |
| `mq016_02_afterlife.scene` | in → out_clean_up, out_decrypted | nix; johnny; Player; 138 nodes / 162 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq016_01_freezer.scene / n40 / 0` | Who? (`who`) | No option-level predicate stored | 0:0 → 85:0:0 |
| `mq016_01_freezer.scene / n40 / 1` | The Rache Bartmoss?! (`bartmoss`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "126816093667", "buildId": "95189197130", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 82:0:0 |
| `mq016_01_freezer.scene / n88 / 0` | I'll think about it. (`search`) | No option-level predicate stored | 0:0 → 90:0:0 |
| `mq016_01_freezer.scene / n88 / 1` | Even if there is, it's bound to be bunk. (`broken`) | No option-level predicate stored | 0:1 → 93:0:0 |
| `mq016_01_freezer.scene / n287 / 0` | [Close] That stench... (`close`) | No option-level predicate stored | 0:0 → 284:0:0; 0:0 → 409:0:1; 0:0 → 486:0:1; 0:0 → 487:0:1; 0:0 → 661:0:1 |
| `mq016_01_freezer.scene / n331 / 0` | [Open] (`open`) | No option-level predicate stored | 0:0 → 193:0:1; 0:0 → 292:0:1; 0:0 → 330:0:1; 0:0 → 482:0:1; 0:0 → 483:0:1 |
| `mq016_01_freezer.scene / n461 / 0` | [Open] (`open`) | No option-level predicate stored | 0:0 → 45:0:3; 0:0 → 460:0:1; 0:0 → 473:0:1; 0:0 → 476:0:1 |
| `mq016_01_freezer.scene / n470 / 0` | [Take cyberdeck] (`Option`) | No option-level predicate stored | 0:0 → 631:0:1; 0:0 → 671:0:1 |
| `mq016_01_freezer.scene / n564 / 0` |  l-pl[zamknij] (`close`) | No option-level predicate stored | 0:0 → 557:0:1 |
| `mq016_02_afterlife.scene / n10 / 0` | Found Bartmoss' deck. (`found`) | No option-level predicate stored | 0:0 → 1019:0:1 |
| `mq016_02_afterlife.scene / n40 / 0` | Fine. Get to it. (`decrypt`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq016_02_changed_mind", "comparisonType": "Equal"}}} | 0:0 → 49:0:0; 0:0 → 618:0:0 |
| `mq016_02_afterlife.scene / n40 / 1` | Changed my mind. Give it a shot. (`changed_mind`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq016_02_changed_mind"}}} | 0:1 → 152:0:0; 0:1 → 618:0:0 |
| `mq016_02_afterlife.scene / n40 / 2` | Think the disk might be infected? (`netrunner`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq016_02_changed_mind", "comparisonType": "Equal"}}, "bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "126816093667", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 89:0:0 |
| `mq016_02_afterlife.scene / n40 / 3` | Best let it be. (`nope`) | No option-level predicate stored | 0:3 → 44:0:0 |
| `mq016_02_afterlife.scene / n69 / 0` | [Set down deck] (`give`) | No option-level predicate stored | 0:0 → 276:0:1; 0:0 → 747:0:0 |
| `mq016_02_afterlife.scene / n302 / 0` | Found it in a fridge. (`freezer`) | No option-level predicate stored | 0:0 → 304:0:0 |
| `mq016_02_afterlife.scene / n302 / 1` | Not your biz. (`noneofyourb`) | No option-level predicate stored | 0:1 → 306:0:0 |
| `mq016_02_afterlife.scene / n360 / 0` | Rather have died? (`youd rather die`) | No option-level predicate stored | 0:0 → 368:0:0 |
| `mq016_02_afterlife.scene / n360 / 1` | Could be for the best. (`regret`) | No option-level predicate stored | 0:1 → 370:0:0 |
| `mq016_02_afterlife.scene / n362 / 0` | Yep. Know the net inside out. (`thebest`) | No option-level predicate stored | 0:0 → 366:0:0 |
| `mq016_02_afterlife.scene / n362 / 1` | Got lucky. (`luck`) | No option-level predicate stored | 0:1 → 364:0:0 |
| `mq016_02_afterlife.scene / n922 / 0` | [Show deck] Take a look. (`Option`) | No option-level predicate stored | 0:0 → 297:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `codex_nix` | mq016_02_afterlife.questphase / h12 / 12 | No reader in selected context |
| `mq015_05_rude_to_nix` | Producer outside selected context | mq016_01_freezer.scene / scene / 113; mq016_02_afterlife.scene / scene / 290 |
| `mq016_02_changed_mind` | mq016_02_afterlife.scene / scene / 155 | mq016_02_afterlife.scene / scene / 40 |
| `mq016_active` | mq016_01_freezer.questphase / h0 / 16; mq016_bartmoss.questphase / h0 / 13 | No reader in selected context |
| `mq016_cryofreezer_opened` | mq016_01_freezer.scene / scene / 654; mq016_01_freezer.scene / scene / 657 | No reader in selected context |
| `mq016_dbg_afterlife` | Producer outside selected context | mq016_02_afterlife.questphase / h12 / 4 |
| `mq016_dbg_shard` | Producer outside selected context | mq016_00_shard.questphase / h44 / 11 |
| `mq016_dbg_test_def` | Producer outside selected context | mq016_01_freezer.questphase / h12 / 10; mq016_02_afterlife.questphase / h12 / 8 |
| `mq016_done` | mq016_bartmoss.questphase / h0 / 5 | No reader in selected context |
| `mq016_fusebox_active` | mq016_02_afterlife.scene / scene / 491 | No reader in selected context |
| `mq016_hacked` | mq016_02_afterlife.scene / scene / 351 | mq016_02_afterlife.scene / scene / 354 |
| `mq016_recognized_bartmoss` | mq016_01_freezer.scene / scene / 539 | mq016_01_freezer.scene / scene / 542 |
| `mq016_saved_life` | mq016_02_afterlife.scene / scene / 383 | No reader in selected context |
| `nix_default_on` | mq016_02_afterlife.questphase / h12 / 11; mq016_02_afterlife.scene / scene / 1002; mq016_02_afterlife.scene / scene / 192; mq016_02_afterlife.scene / scene / 499; mq016_02_afterlife.scene / scene / 502 | No reader in selected context |
| `nix_old_school_expert` | Producer outside selected context | mq016_01_freezer.scene / scene / 104 |
| `q305_haunted_weapon_random_whisper_02` | mq016_01_freezer.questphase / h0 / 18 | No reader in selected context |
| `q305_haunted_weapon_random_whisper_02_used` | Producer outside selected context | mq016_01_freezer.questphase / h0 / 17 |

## Exact gates, joins and cancellation

<details><summary>38 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq016_bartmoss.questphase / h83 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#afterlife_interior_area_inside"}}` | 0:Out → 3:In; 3:Out → 4:In |
| `mq016_00_shard.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_quest/mq016_bartmoss/mq016_data_shard/mq016_00_data_shard","fileEntryIndex":5,"className":"gameJournalOnscreen"},"visited":true}}}` | 10:Out1 → 3:In; 3:Out → 6:In |
| `mq016_00_shard.questphase / h0 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 6:True → 2:In; 3:Out → 6:In; 6:False → 8:Active |
| `mq016_00_shard.questphase / h44 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_dbg_shard"}}}` | 0:Out → 11:In; 11:False → 1:In; 11:True → 12:In |
| `mq016_01_freezer.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq016_tr_freezer"},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq016_cryofreezer"}}}]}}` | 7:Out → 5:In; 5:Out → 8:Inactive |
| `mq016_01_freezer.questphase / h0 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 8:Out → 14:In; 14:False → 9:Active; 14:True → 13:Succeeded |
| `mq016_01_freezer.questphase / h0 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q305_haunted_weapon_random_whisper_02_used"}}}` | 25:Out → 17:In; 17:False → 18:In |
| `mq016_01_freezer.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#q101_tr_return_landfill"},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq016_cryofreezer"}}}]}}` | 7:Out → 24:In; 24:Out → 25:In |
| `mq016_01_freezer.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 25:Out → 17:In; 24:Out → 25:In |
| `mq016_01_freezer.questphase / h12 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_dbg_test_def"}}}` | 0:Out → 10:In; 10:False → 7:In; 10:True → 11:In |
| `mq016_02_afterlife.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq016_tr_afterlife_entrance"},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ws_nix_default"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}]}}` | 2:Out1 → 12:In; 12:Out → 3:in; 12:Out → 10:Active |
| `mq016_02_afterlife.questphase / h12 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_dbg_afterlife"}}}` | 4:False → 1:In; 10:Out → 4:In; 8:False → 4:In; 4:True → 5:In |
| `mq016_02_afterlife.questphase / h12 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_dbg_test_def"}}}` | 8:False → 4:In; 12:Out → 8:In; 8:True → 10:In |
| `mq016_01_freezer.scene / scene / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq016_bartmoss_cyberdeck"}}}}` | 68:0:0 → 174:0:0; 523:0:0 → 68:0:1 |
| `mq016_01_freezer.scene / scene / 104` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nix_old_school_expert","value":1}}}` | 98:0:0 → 104:0:1; 101:0:0 → 104:0:1; 104:0:0 → 106:0:0; 104:0:1 → 108:0:0 |
| `mq016_01_freezer.scene / scene / 113` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_05_rude_to_nix","value":1,"comparisonType":"GreaterOrEqual"}}}` | 106:0:0 → 113:0:1; 113:0:0 → 116:0:0; 113:0:1 → 620:0:0 |
| `mq016_01_freezer.scene / scene / 404` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq016_tr_freezer"}}` | 294:0:0 → 404:0:1; 404:0:0 → 2:0:0; 404:0:0 → 428:0:0; 404:0:0 → 557:0:0 |
| `mq016_01_freezer.scene / scene / 542` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_recognized_bartmoss","value":1,"comparisonType":"GreaterOrEqual"}}}` | 272:2:0 → 542:0:1; 542:0:0 → 98:0:0; 542:0:1 → 101:0:0 |
| `mq016_01_freezer.scene / scene / 566` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq016_tr_freezer"}}` | 277:666:6 → 566:0:1; 566:0:0 → 557:0:0; 566:0:1 → 564:0:0 |
| `mq016_01_freezer.scene / scene / 581` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questVisionMode_ConditionType","visionModeType":"FocusMode"}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq016_cryofreezer"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}]}}` | 171:666:0 → 581:0:1; 581:0:0 → 174:0:1 |
| `mq016_01_freezer.scene / scene / 591` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq016_01_freezer_johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 590:0:0 → 591:0:1; 591:0:0 → 30:0:1; 591:0:0 → 318:0:1 |
| `mq016_02_afterlife.scene / scene / 290` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_05_rude_to_nix"}}}` | 290:0:0 → 299:0:0; 290:0:1 → 922:0:0; 1002:0:0 → 290:0:1 |
| `mq016_02_afterlife.scene / scene / 354` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_hacked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 354:0:0 → 356:0:0; 354:0:1 → 358:0:0; 963:0:0 → 354:0:1 |
| `mq016_02_afterlife.scene / scene / 408` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq016_tr_door_closed"}}` | 408:0:0 → 323:0:0; 471:1:0 → 408:0:0; 471:1:0 → 408:1026:0; 965:0:0 → 408:0:1 |
| `mq016_02_afterlife.scene / scene / 413` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq016_dvc_nix_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"WashackingMinigameFailed"}}}` | 413:0:0 → 331:0:0; 471:1:0 → 413:0:0; 471:1:0 → 413:1026:0; 507:0:0 → 413:0:1 |
| `mq016_02_afterlife.scene / scene / 481` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq016_dvc_electric_box","eventType":"Executed"}}}` | 471:1:0 → 481:0:0; 471:1:0 → 481:1026:0; 481:0:0 → 321:0:0; 481:0:0 → 1090:0:0; 654:0:0 → 481:0:1 |
| `mq016_02_afterlife.scene / scene / 507` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq016_dvc_nix_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 471:1:0 → 507:0:0; 471:1:0 → 507:1026:0; 507:0:0 → 413:0:1; 507:0:0 → 641:0:1; 507:0:0 → 785:0:1; 965:0:0 → 507:0:1 |
| `mq016_02_afterlife.scene / scene / 570` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0},"comparisonType":"GreaterOrEqual"}}}` | 570:0:0 → 667:0:1; 1107:0:0 → 570:0:1 |
| `mq016_02_afterlife.scene / scene / 641` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq016_dvc_nix_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"WasHackingMinigameSucceeded"}}}` | 471:1:0 → 641:0:0; 471:1:0 → 641:1026:0; 507:0:0 → 641:0:1; 641:0:0 → 93:0:0; 641:0:0 → 1090:0:0 |
| `mq016_02_afterlife.scene / scene / 646` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq016_02_afterlife_johnny"},"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 93:0:0 → 646:0:1; 646:0:0 → 780:0:1 |
| `mq016_02_afterlife.scene / scene / 650` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq016_02_afterlife_johnny"},"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 650:0:0 → 777:0:1; 1040:0:0 → 650:0:1 |
| `mq016_02_afterlife.scene / scene / 914` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questBuild_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"Build_ScriptConditionType","buildId":"95189197130","difficulty":"MEDIUM","comparisonType":"CO_GreaterEq"}}}}` | 914:0:0 → 916:0:0; 914:0:1 → 983:0:1; 965:0:0 → 914:0:1 |
| `mq016_02_afterlife.scene / scene / 983` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq016_dvc_nix_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsInDirectInteractionRange"}}}` | 471:1:0 → 983:0:0; 471:1:0 → 983:1026:0; 914:0:1 → 983:0:1; 983:0:0 → 981:0:0 |
| `mq016_02_afterlife.scene / scene / 1058` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq016_tr_nix_crib"}}` | 1058:0:0 → 1103:0:1; 1097:0:0 → 1058:0:1 |
| `mq016_02_afterlife.scene / scene / 1065` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq016_tr_nix_crib"}}` | 1:0:0 → 1065:0:1; 1065:0:0 → 1048:0:1; 1070:0:0 → 1065:0:1 |
| `mq016_02_afterlife.scene / scene / 1107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq016_tr_nix_crib"}}` | 465:0:0 → 1107:0:1; 1107:0:0 → 570:0:1 |
| `mq016_02_afterlife.scene / scene / 1114` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"Level","value":30.0,"comparisonType":"LessOrEqual"}}}` | 1114:0:0 → 1136:0:1; 1114:0:1 → 1142:0:1; 1115:0:1 → 1114:0:1 |
| `mq016_02_afterlife.scene / scene / 1115` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"Level","value":22.0,"comparisonType":"LessOrEqual"}}}` | 375:2:0 → 1115:0:1; 1115:0:0 → 1133:0:1; 1115:0:1 → 1114:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq016_01_freezer.scene / scene / 591 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | mq016_02_afterlife.scene / scene / 1014; mq016_02_afterlife.scene / scene / 1019; mq016_02_afterlife.scene / scene / 1026; mq016_02_afterlife.scene / scene / 995; +2 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq016_01_freezer.scene / scene / 287; mq016_01_freezer.scene / scene / 331; mq016_01_freezer.scene / scene / 40; mq016_01_freezer.scene / scene / 461; +10 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | mq016_00_shard.questphase / h44 / 11; mq016_01_freezer.questphase / h0 / 17; mq016_01_freezer.questphase / h12 / 10; mq016_01_freezer.scene / scene / 104; +7 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq016_02_afterlife.scene / scene / 1048; mq016_02_afterlife.scene / scene / 1056; mq016_02_afterlife.scene / scene / 1061; mq016_bartmoss.questphase / h83 / 4; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq016_01_freezer.scene / scene / 511; mq016_01_freezer.scene / scene / 527; mq016_01_freezer.scene / scene / 631; mq016_bartmoss.questphase / h83 / 10 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq016_01_freezer.scene / scene / 585; mq016_02_afterlife.questphase / h12 / 10; mq016_02_afterlife.scene / scene / 418; mq016_02_afterlife.scene / scene / 420; +7 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq016_02_afterlife.scene / scene / 413; mq016_02_afterlife.scene / scene / 507; mq016_02_afterlife.scene / scene / 641; mq016_02_afterlife.scene / scene / 983 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `journal_read` | mq016_00_shard.questphase / h0 / 3 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | mq016_00_shard.questphase / h0 / 8; mq016_01_freezer.questphase / h0 / 13; mq016_01_freezer.questphase / h0 / 15; mq016_01_freezer.questphase / h0 / 7; +30 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | mq016_01_freezer.questphase / h0 / 16; mq016_01_freezer.questphase / h0 / 18; mq016_01_freezer.scene / scene / 539; mq016_01_freezer.scene / scene / 654; +13 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq016_01_freezer.questphase / h0 / 25 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | mq016_bartmoss.questphase / h0 / 9 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | mq016_01_freezer.questphase / h0 / 24; mq016_01_freezer.questphase / h0 / 5; mq016_01_freezer.scene / scene / 68 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq016_01_freezer.questphase / h0 / 4; mq016_02_afterlife.questphase / h0 / 3 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq016_01_freezer.questphase / h0 / 24; mq016_01_freezer.questphase / h0 / 5; mq016_01_freezer.scene / scene / 404; mq016_01_freezer.scene / scene / 566; +6 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `weather_scope` | mq016_bartmoss.questphase / h83 / 7 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | mq016_01_freezer.scene / scene / 252; mq016_01_freezer.scene / scene / 274; mq016_01_freezer.scene / scene / 318; mq016_01_freezer.scene / scene / 602; +14 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` | content candidate; journal anchor | `base-mq016` |
| `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` | content candidate; journal anchor | `base-mq016` |
| `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` | content candidate; journal anchor | `base-mq016` |
| `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` | content candidate; journal anchor | `base-mq016` |
| `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` | content candidate; journal anchor | `base-mq016` |
| `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` | content candidate; journal anchor | `base-mq016` |

Evidence shards for this dossier (including parent context): [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

173 repeated typed/socket path signatures in this selected graph context; 29 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `40aa0dddb5f517500320` | `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` / h12 / 12 -> 8 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; False -> In |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 297 -> 302 -> 304 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `276aca4a2dc348a877d5` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 747 -> 64 -> 698 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `016828d499c85128303c` | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 98 -> 104 -> 106 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `1fa539921730278ef7fb` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 302 -> 304 -> 23 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `6b1fcb4c46676ba8a912` | `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 8 -> 13 -> 5 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `38efa89ea367b077425d` | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 90 -> 638 -> 636 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; 0:0 -> 0:3; 0:0 -> 0:1 |
| `7ff0eae411231e617b77` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 368 -> 375 -> 383 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `4dba958d33dae15616f5` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 364 -> 372 -> 375 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `d18fd8da12f6125e7cd7` | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 747 -> 64 -> 1076 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `ebdaafaddefbc1080fe8` | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 88 -> 90 -> 252 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `f2ad97c516e351909a37` | `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 13 -> 5 -> 9 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questRewardManagerNodeDefinition[questGiveReward_NodeType]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 3 | `h22` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 11 | `h68` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` / h0 / 29 | `h83` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` / h0 / 10 | `h44` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | base\quest\minor_quests\mq016\mq016_bartmoss.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\main_characters\johnny\johnny__facial_idle_poses.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_lie_netrunner_chair__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_netrunner_chair__2h_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_table_lean180__rh_cigarette_lh_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__2h_on_sides__aggressive__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_cigarette__aggressive__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q101\06c_memories_p2\q101_06c_memories_p2__player_ma_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq016\mq016_02_afterlife__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq016\scenes\lipsync\en\mq016_01_freezer\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq016\scenes\lipsync\en\mq016_01_freezer\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq016\scenes\lipsync\en\mq016_02_afterlife\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq016\scenes\lipsync\en\mq016_02_afterlife\nix.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq016\scenes\lipsync\en\mq016_02_afterlife\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\table\generic__stand_table_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\ground\johnny__walk_ground_cigarette__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\netrunner_den\netrunner_chair\generic__lie_netrunner_chair__netrun__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\netrunner_den\netrunner_chair\generic__sit_netrunner_chair__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\minor_quests\mq016\mq016__generic__lie_netrunner_chair__braindance__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `codex_nix` | base\quest\bugfixing\minor_quests\mq015\mq015_quest_bugfixes.questphase / h88 / 5; base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase / h0 / 62; ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h83 / 118; 3 total source locations in compressed evidence |
| `mq015_05_rude_to_nix` | base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene / scene / 163; 1 total source locations in compressed evidence |
| `mq016_active` | base\quest\minor_quests\minorquests.questphase / h0 / 135; 1 total source locations in compressed evidence |
| `mq016_dbg_afterlife` | base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene / scene / 9; 1 total source locations in compressed evidence |
| `mq016_dbg_shard` | base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene / scene / 41; 1 total source locations in compressed evidence |
| `mq016_dbg_test_def` | base\quest\minor_quests\mq016\mq016_bartmoss.quest / h0 / 10; 1 total source locations in compressed evidence |
| `mq016_done` | ep1\quest\main_quests\q301\test\q301_chicken_test.scene / scene / 436; ep1\quest\main_quests\q301\test\q301_chicken_test.scene / scene / 454; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 283; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 298; 7 total source locations in compressed evidence |
| `mq016_saved_life` | ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 281; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 296; ep1\quest\test\ep1_chicken_test.scene / scene / 203; ep1\quest\test\ep1_chicken_test.scene / scene / 218; 5 total source locations in compressed evidence |
| `nix_default_on` | base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene / scene / 101; base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene / scene / 104; base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene / scene / 108; base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene / scene / 179; 11 total source locations in compressed evidence |
| `nix_old_school_expert` | base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene / scene / 97; base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene / scene / 83; base\quest\tertiary_characters\default_dialogues\nix_default.scene / scene / 22; 3 total source locations in compressed evidence |
| `q305_haunted_weapon_random_whisper_02` | base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase / h0 / 76; base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene / scene / 3745; ep1\quest\minor_quests\mq305\scenes\mq305_04_bunker.scene / scene / 5138; ep1\quest\main_quests\q305\phases\q305_12_haunted_weapon.questphase / h19 / 52; 6 total source locations in compressed evidence |
| `q305_haunted_weapon_random_whisper_02_used` | ep1\quest\main_quests\q305\scenes\q305_16_haunted_weapons_reactions.scene / scene / 164; 1 total source locations in compressed evidence |

NodeRef uses: 111; TweakDB binding uses: 64. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` | 14 / 84 | scnDialogLineEvent: 26; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 7; scnOverridePhantomParamsEvent: 1; scnPlaySkAnimEvent: 32; scnUnmountEvent: 1; scneventsEquipItemToPerformer: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 8; scneventsVFXEvent: 4 |
| `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` | 28 / 144 | scnDialogLineEvent: 65; scnLookAtEvent: 15; scnPlaySkAnimEvent: 38; scneventsAttachPropToNode: 3; scneventsAttachPropToPerformer: 1; scneventsEquipItemToPerformer: 1; scneventsSocket: 11; scneventsUnequipItemFromPerformer: 1; scneventsVFXEvent: 9 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
