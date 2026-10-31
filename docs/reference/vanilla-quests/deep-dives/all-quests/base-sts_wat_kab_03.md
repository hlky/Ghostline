# Gig: Backs Against the Wall

Journal: `quests/street_stories/watson/kabuki/sts_wat_kab_03` · `StreetStory` · hash `1197270346`.

Journal premise: Gig type: Search and Recover\nObjective: Recovered stolen medicine\nLocation: Housing block on Columbus St.\nDetails:\n\nA few years back I scrolled a little feature called "How Affordable is Health?" It turns out not very. My numbers showed only 3 percent of Night Citizens could afford healthcare. A lot has changed since. For the worse. Some people are declaring open war on rippers, breaking into clinics, klepping meds and chems. No surprise there. And no surprise these rippers want to protect what's theirs.\n\nThey want you to recover a pack of stolen meds. Thanks to the GPS tracer hidden inside, we know exactly where to look.

**Coverage: journal-linked.** 51 exact journal-linked nodes in 5 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 3 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`; `base\quest\demos\handson_2020\handson_2020_kabuki.quest`; `base\quest\demos\handson_2020\handson_2020_speed_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go to the indicated residence. (Primary) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` |
| Find the stolen medicine. (Primary) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` |
| Deposit the medicine in the Drop Point. (Primary) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` |
| Retrieve the stolen medicine. (Primary) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve_stolen_meds` |
| Retrieve the stolen medicine. (Primary) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 30` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 69:True → 30:Succeeded; 30:Out → 43:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 32` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 52:Out → 32:Active; 32:Out → 33:In; 32:Out → 50:In; 32:Out → 56:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 34` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 42:False → 34:Succeeded; 34:Out → 36:Active |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 35` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | 37:Out → 35:Succeeded; 35:Out → 49:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 36` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 34:Out → 36:Active; 41:Out → 36:Active; 36:Out → 51:In; 36:Out → 64:In; 36:Out → 63:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 37` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 37:Out → 35:Succeeded; 55:Out → 37:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 40` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 47:Out → 40:Active |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 41` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 41:Out → 36:Active; 67:Out → 41:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 47` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 39:False → 47:Succeeded; 47:Out → 40:Active; 56:Out → 47:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 59` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 42:False → 59:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 65` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 62:True → 65:In; 65:True → 66:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 66` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 65:True → 66:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 67` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 67:Out → 41:Succeeded; 42:True → 67:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 69` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 69:True → 30:Succeeded; 69:True → 48:In; 72:Out → 69:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 4` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 3:Out → 4:In; 4:True → 7:In1; 4:False → 6:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 6` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 4:False → 6:In; 6:True → 7:In2 |
| `sts_wat_kab_03_openworld.questphase / h79 / 8` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 9:Out → 8:Succeeded; 8:Out → 57:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 10` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 79:Out → 10:Active; 10:Out → 14:In; 10:Out → 76:In; 10:Out → 102:In; 10:Out → 124:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 15` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 47:False → 15:Succeeded; 15:Out → 26:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 16` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | 27:Out → 16:Succeeded; 16:Out → 73:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 26` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 15:Out → 26:Active; 46:Out → 26:Active; 26:Out → 78:In; 26:Out → 134:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 27` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 27:Out → 16:Succeeded; 101:Out → 27:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 45` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 70:Out → 45:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 46` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 46:Out → 26:Active; 138:Out → 46:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 52` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 52:Out → 9:In; 66:False → 52:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 64` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/brief` | 109:Out → 64:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 67` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 67:Out → 9:In; 66:True → 67:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 70` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 44:False → 70:Succeeded; 70:Out → 45:Active; 102:Out → 70:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 121` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 47:False → 121:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 136` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 131:True → 136:In; 136:True → 137:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 137` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 136:True → 137:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 138` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 138:Out → 46:Succeeded; 47:True → 138:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 8` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 9:Out → 8:Succeeded; 8:Out → 57:In |
| `sts_wat_kabuki.questphase / h9073 / 10` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 79:Out → 10:Active; 10:Out → 14:In; 10:Out → 76:In; 10:Out → 102:In; 10:Out → 124:In |
| `sts_wat_kabuki.questphase / h9073 / 15` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 47:False → 15:Succeeded; 15:Out → 26:Active |
| `sts_wat_kabuki.questphase / h9073 / 16` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | 27:Out → 16:Succeeded; 16:Out → 73:In |
| `sts_wat_kabuki.questphase / h9073 / 26` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 15:Out → 26:Active; 46:Out → 26:Active; 26:Out → 78:In; 26:Out → 134:In |
| `sts_wat_kabuki.questphase / h9073 / 27` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 27:Out → 16:Succeeded; 101:Out → 27:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 45` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 70:Out → 45:Active |
| `sts_wat_kabuki.questphase / h9073 / 46` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 46:Out → 26:Active; 138:Out → 46:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 52` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 52:Out → 9:In; 66:False → 52:Active |
| `sts_wat_kabuki.questphase / h9073 / 64` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/brief` | 109:Out → 64:Active |
| `sts_wat_kabuki.questphase / h9073 / 67` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house` | 67:Out → 9:In; 66:True → 67:Active |
| `sts_wat_kabuki.questphase / h9073 / 70` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 44:False → 70:Succeeded; 70:Out → 45:Active; 102:Out → 70:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 121` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 47:False → 121:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 136` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 131:True → 136:In; 136:True → 137:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 137` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds` | 136:True → 137:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 138` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds` | 138:Out → 46:Succeeded; 47:True → 138:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 311` (Condition) | `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve` | 200:False → 311:In; 311:False → 202:In; 214:Out → 311:In; 311:True → 310:In |
| `open_world_bugfixing.questphase / h116 / 76` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | 33:True → 76:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 76` (Journal) | `quests/street_stories/watson/kabuki/sts_wat_kab_03` | 33:True → 76:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 7` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene`; `#sts_sm_wat_kab_03_holocall_debrief` | 37:CutSource → 7:CutDestination; 15:Out → 7:Start1; 7:End1 → 8:In; 7:Holocall INT → 10:In; 7:Holocall RET → 9:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 105` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene`; `#sts_sm_wat_kab_03_holocall_prebrief` | 105:rejected_out → 83:Active; 105:End1 → 83:Active; 140:False → 105:Start1; 105:End1 → 113:In; 105:Holocall INT → 111:In; 105:Holocall RET → 110:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 4` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene`; `#sts_wat_kab_03_scene_sm` | 3:Out → 4:neighbours |
| `sts_wat_kab_03_openworld.questphase / h680 / 10` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene`; `#sts_sm_wat_kab_03_johnny` | 22:Out → 10:Start 0; 10:End 0 → 13:In |
| `sts_wat_kab_03_openworld.questphase / h760 / 7` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene`; `#sts_sm_wat_kab_03_holocall_debrief` | 37:False → 7:Start1; 7:rejected_out → 38:Active; 7:End1 → 8:In; 7:Holocall INT → 10:In; 7:Holocall RET → 9:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_kabuki_bugfixing.questphase` / h0 / 29 | `sts_wat_kab_03_bugfixing.questphase` | 31: DeletionMarker; 31:Out → 29:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase` / h0 / 25 | `sts_wat_kab_03_openworld.questphase` | 0: Input; 0:Out → 25:In1; 25:Out1 → 1:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h20161 / 25 | `sts_wat_kab_03_openworld.questphase` | 0: Input; 0:Out → 25:In1; 25:Out1 → 1:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h361 / 7 | `sts_wat_kab_03_holocall_debrief.scene` | 37: CutControl; 15: GameManager; 37:CutSource → 7:CutDestination; 15:Out → 7:Start1; 7:End1 → 8:In; 7:Holocall INT → 10:In; 7:Holocall RET → 9:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h760 / 7 | `sts_wat_kab_03_holocall_debrief.scene` | 37: Condition; 37:False → 7:Start1; 7:rejected_out → 38:Active; 7:End1 → 8:In; 7:Holocall INT → 10:In; 7:Holocall RET → 9:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h9754 / 7 | `sts_wat_kab_03_holocall_debrief.scene` | 37: Condition; 37:False → 7:Start1; 7:rejected_out → 38:Active; 7:End1 → 8:In; 7:Holocall INT → 10:In; 7:Holocall RET → 9:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h79 / 105 | `sts_wat_kab_03_holocall_prebrief.scene` | 140: Condition; 105:rejected_out → 83:Active; 105:End1 → 83:Active; 140:False → 105:Start1; 105:End1 → 113:In; 105:Holocall INT → 111:In; 105:Holocall RET → 110:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h9073 / 105 | `sts_wat_kab_03_holocall_prebrief.scene` | 140: Condition; 105:rejected_out → 83:Active; 105:End1 → 83:Active; 140:False → 105:Start1; 105:End1 → 113:In; 105:Holocall INT → 111:In; 105:Holocall RET → 110:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h680 / 10 | `sts_wat_kab_03_johnny.scene` | 22: PauseCondition: {"seconds": 1}; 22:Out → 10:Start 0; 10:End 0 → 13:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h9674 / 10 | `sts_wat_kab_03_johnny.scene` | 22: PauseCondition: {"seconds": 1}; 22:Out → 10:Start 0; 10:End 0 → 13:In |
| `base\quest\main_quests\prologue\q003\phases\q003_stout.questphase` / h575 / 8 | `sts_wat_kab_03_johnny.scene` | 15: CutControl; 9: PauseCondition: q003_johnny_comment_cat_flat; 15:CutSource → 8:CutDestination; 9:Out → 8:q003_cat_flat_reaction_in; 8:q003_cat_flat_reaction_out → 10:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase` / h25 / 63 | `sts_wat_kab_03_scene.scene` | 105: CutControl; 102: PauseCondition: #sts_wat_kab_03_tr_apartment; 105:CutSource → 63:CutDestination; 102:Out → 63:solo; 63:combat → 115:In; 63:combat → 106:In; 63:peaceful → 103:In; 63:dont move → 79:In1; 63:BeforeSuicide → 96:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h680 / 4 | `sts_wat_kab_03_scene.scene` | 3: PauseCondition: #kab_03_tr_fluff_chat; 3:Out → 4:neighbours |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h9674 / 4 | `sts_wat_kab_03_scene.scene` | 3: PauseCondition: #kab_03_tr_fluff_chat; 3:Out → 4:neighbours |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h20218 / 63 | `sts_wat_kab_03_scene.scene` | 105: CutControl; 102: PauseCondition: #sts_wat_kab_03_tr_apartment; 105:CutSource → 63:CutDestination; 102:Out → 63:solo; 63:combat → 115:In; 63:combat → 106:In; 63:peaceful → 103:In; 63:dont move → 79:In1; 63:BeforeSuicide → 96:In |
| `base\open_world\street_stories\watson\sts_watson.questphase` / h0 / 2 | `sts_wat_kabuki.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 4 | `sts_wat_kabuki.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h15 / 5 | `sts_wat_kabuki.questphase` | 0: Input; 0:Out → 5:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 33 | `sts_kabuki_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 33:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_quest.quest` / h0 / 8 | `sts_wat_kab_03_phase.questphase` | 13: FactsDBManager: sts_wat_kab_03_test; 8:Out1 → 1:In; 13:Out → 8:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h0 / 8 | `sts_wat_kab_03_phase.questphase` | 119: Journal; 119:Out → 8:In1 |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 28 | `q003_stout.questphase` |  |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 14 | `q003_stout.questphase` |  |
| `base\quest\persistent_content.questphase` / h2254 / 2 | `q003_stout.questphase` | 8: PauseCondition: q003_done; 8:Out → 2:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase` / h0 / 26 | `sts_wat_kab_03_combat.questphase` | 0: Input; 0:Out → 26:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h20161 / 26 | `sts_wat_kab_03_combat.questphase` | 0: Input; 0:Out → 26:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 7 | `sts_watson.questphase` | 0: Input; 0:Out → 7:In1 |
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
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_wat_kab_03_holocall_debrief.scene` | Start1 → rejected_out, End1 | fixer; 25 nodes / 29 edges |
| `sts_wat_kab_03_holocall_prebrief.scene` | Start1 → End1, rejected_out | fixer; 22 nodes / 25 edges |
| `sts_wat_kab_03_johnny.scene` | Start 0, q003_cat_flat_reaction_in → End 0, q003_cat_flat_reaction_out | johnny; johnny_spawnset_cat; Player; 34 nodes / 43 edges |
| `sts_wat_kab_03_scene.scene` | solo, interrupt, neighbours → peaceful, combat, interrupt_default, interrupt_o, neighbours_o, dont move | solo; neighbour_001; neighbour_002; johnny; player; 103 nodes / 134 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_wat_kab_03_johnny.scene / n8 / 0` | We can't help him. (``) | No option-level predicate stored | 0:0 → 14:0:0 |
| `sts_wat_kab_03_johnny.scene / n8 / 1` | He's not alone. (``) | No option-level predicate stored | 0:1 → 20:0:0 |
| `sts_wat_kab_03_johnny.scene / n8 / 2` | Sympathizing with a Militech soldier? (``) | No option-level predicate stored | 0:2 → 10:0:0 |
| `sts_wat_kab_03_scene.scene / n557 / 0` | Fixer sent me. (`fixer`) | No option-level predicate stored | 0:0 → 554:0:0 |
| `sts_wat_kab_03_scene.scene / n557 / 1` | GPS signal. (`gps`) | No option-level predicate stored | 0:1 → 601:0:0 |
| `sts_wat_kab_03_scene.scene / n557 / 2` | Let's just fight. (`fight`) | No option-level predicate stored | 0:2 → 720:0:0 |
| `sts_wat_kab_03_scene.scene / n701 / 0` | If it doesn't work, give it to me. (`dont need them`) | No option-level predicate stored | 0:0 → 705:0:0 |
| `sts_wat_kab_03_scene.scene / n701 / 1` | Give it, or I call MaxTac. (`maxtac`) | No option-level predicate stored | 0:1 → 703:0:0 |
| `sts_wat_kab_03_scene.scene / n712 / 0` | His death would change nothing. (`without_change`) | No option-level predicate stored | 0:0 → 753:0:0 |
| `sts_wat_kab_03_scene.scene / n712 / 1` | Do what you want, but give me the drugs. (`whatever`) | No option-level predicate stored | 0:1 → 714:0:0 |
| `sts_wat_kab_03_scene.scene / n712 / 2` | You're a soldier, not a terrorist. (`solo`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "164696763007", "buildId": "75476658533", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 1372:0:0 |
| `sts_wat_kab_03_scene.scene / n712 / 3` | I see we're past talking. (`enough_is_enough`) | No option-level predicate stored | 0:3 → 718:0:0 |
| `sts_wat_kab_03_scene.scene / n727 / 0` | I understand your anger. (`i_understand`) | No option-level predicate stored | 0:0 → 1375:0:0; 0:0 → 1466:0:0 |
| `sts_wat_kab_03_scene.scene / n727 / 1` | Where did you serve? (`where`) | No option-level predicate stored | 0:1 → 729:0:0 |
| `sts_wat_kab_03_scene.scene / n751 / 0` | Other poltician's will make use of his death. (`holt_death`) | No option-level predicate stored | 0:0 → 778:0:1; 0:0 → 1391:0:0; 0:0 → 1466:0:0 |
| `sts_wat_kab_03_scene.scene / n751 / 1` | They'll say you're a psycho. (`cyberpsycho`) | No option-level predicate stored | 0:1 → 757:0:0; 0:1 → 778:0:1; 0:1 → 1466:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-640311` | sts_wat_kab_03_bugfixing.questphase / h17 / 3 | sts_wat_kab_03_bugfixing.questphase / h17 / 2 |
| `CYB-645884` | sts_wat_kab_03_bugfixing.questphase / h580 / 3 | sts_wat_kab_03_bugfixing.questphase / h580 / 2 |
| `CYB-645885` | sts_wat_kab_03_bugfixing.questphase / h503 / 3 | sts_wat_kab_03_bugfixing.questphase / h503 / 2 |
| `CYB-668458` | sts_wat_kab_03_bugfixing.questphase / h640 / 3 | sts_wat_kab_03_bugfixing.questphase / h640 / 2 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wat_kab_03_holocall_prebrief.scene / scene / 279 |
| `holo_reggie_calls_v_end_activate` | sts_wat_kab_03_bugfixing.questphase / h361 / 10; sts_wat_kab_03_holocall_debrief.scene / scene / 68; sts_wat_kab_03_holocall_prebrief.scene / scene / 87; sts_wat_kab_03_openworld.questphase / h760 / 10; sts_wat_kab_03_openworld.questphase / h79 / 111 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | sts_wat_kab_03_holocall_debrief.scene / scene / 64; sts_wat_kab_03_holocall_prebrief.scene / scene / 83 | sts_wat_kab_03_holocall_debrief.scene / scene / 63; sts_wat_kab_03_holocall_prebrief.scene / scene / 82 |
| `holo_reggie_calls_v_rejectable` | sts_wat_kab_03_holocall_debrief.scene / scene / 295; sts_wat_kab_03_holocall_prebrief.scene / scene / 254; sts_wat_kab_03_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | sts_wat_kab_03_holocall_debrief.scene / scene / 297; sts_wat_kab_03_holocall_prebrief.scene / scene / 256 | sts_wat_kab_03_holocall_debrief.scene / scene / 299; sts_wat_kab_03_holocall_prebrief.scene / scene / 258 |
| `holo_reggie_calls_v_start_activate` | sts_wat_kab_03_bugfixing.questphase / h361 / 9; sts_wat_kab_03_holocall_debrief.scene / scene / 265; sts_wat_kab_03_holocall_debrief.scene / scene / 67; sts_wat_kab_03_holocall_prebrief.scene / scene / 283; sts_wat_kab_03_holocall_prebrief.scene / scene / 86; sts_wat_kab_03_openworld.questphase / h760 / 9; sts_wat_kab_03_openworld.questphase / h79 / 110 | sts_wat_kab_03_bugfixing.questphase / h361 / 39; sts_wat_kab_03_holocall_debrief.scene / scene / 263 |
| `holo_reggie_calls_v_start_done` | sts_wat_kab_03_holocall_debrief.scene / scene / 62; sts_wat_kab_03_holocall_prebrief.scene / scene / 81 | sts_wat_kab_03_holocall_debrief.scene / scene / 277; sts_wat_kab_03_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_wat_kab_03_holocall_debrief.scene / scene / 263; sts_wat_kab_03_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wat_kab_03_holocall_debrief.scene / scene / 263; sts_wat_kab_03_holocall_prebrief.scene / scene / 279 |
| `kab_03_finished` | sts_wat_kab_03_bugfixing.questphase / h17 / 38; sts_wat_kab_03_openworld.questphase / h79 / 42 | open_world_bugfixing.questphase / h116 / 33; open_world_bugfixing.questphase / h2878 / 33; sts_wat_kab_03_bugfixing.questphase / h17 / 39; sts_wat_kab_03_openworld.questphase / h79 / 44; sts_wat_kabuki.questphase / h9073 / 44 |
| `kab_03_gun_shot` | sts_wat_kab_03_bugfixing.questphase / h17 / 54; sts_wat_kab_03_johnny.scene / scene / 116; sts_wat_kab_03_openworld.questphase / h79 / 94; sts_wat_kab_03_scene.scene / scene / 1187 | sts_wat_kab_03_scene.scene / scene / 797 |
| `kab_03_interrupt` | Producer outside selected context | sts_wat_kab_03_scene.scene / scene / 1124 |
| `kab_03_johnny` | sts_wat_kab_03_scene.scene / scene / 1388 | sts_wat_kab_03_bugfixing.questphase / h17 / 60; sts_wat_kab_03_openworld.questphase / h680 / 8; sts_wat_kab_03_openworld.questphase / h79 / 123 |
| `kab_03_peace` | sts_wat_kab_03_openworld.questphase / h79 / 91; sts_wat_kab_03_scene.scene / scene / 778 | sts_wat_kab_03_bugfixing.questphase / h17 / 42; sts_wat_kab_03_openworld.questphase / h79 / 116; sts_wat_kab_03_openworld.questphase / h79 / 47; sts_wat_kab_03_scene.scene / scene / 895; sts_wat_kabuki.questphase / h9073 / 47 |
| `kab_03_start` | sts_wat_kab_03_openworld.questphase / h79 / 41 | sts_wat_kab_03_bugfixing.questphase / h640 / 7 |
| `q101_done` | Producer outside selected context | sts_wat_kab_03_openworld.questphase / h680 / 21; sts_wat_kab_03_scene.scene / scene / 1188 |
| `sts_wat_kab_03_meds` | Producer outside selected context | sts_wat_kab_03_bugfixing.questphase / h17 / 58; sts_wat_kab_03_openworld.questphase / h79 / 112 |
| `sts_wat_kab_03_ready_1` | sts_wat_kab_03_scene.scene / scene / 1435 | sts_wat_kab_03_scene.scene / scene / 1437 |
| `sts_wat_kab_03_test` | Producer outside selected context | sts_wat_kab_03_openworld.questphase / h79 / 66; sts_wat_kabuki.questphase / h9073 / 66 |
| `travelling_merchant_lives` | Producer outside selected context | sts_wat_kab_03_bugfixing.questphase / h0 / 14 |
| `wat_achievement` | sts_wat_kab_03_bugfixing.questphase / h361 / 5; sts_wat_kab_03_openworld.questphase / h760 / 5 | sts_wat_kab_03_bugfixing.questphase / h361 / 14; sts_wat_kab_03_openworld.questphase / h760 / 14 |
| `welcome_holocall_skipped` | sts_wat_kab_03_openworld.questphase / h79 / 113 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>141 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wat_kab_03_bugfixing.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 15:Out → 14:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-640311","value":1,"comparisonType":"Equal"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_start_loop"},{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_entrance_window"}]}}` | 3:Out → 31:In; 31:Out → 72:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 32:Out → 33:In; 33:Out → 68:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_finished"}}}` | 50:Out → 39:In; 60:Out → 39:In; 39:False → 47:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_peace"}}}` | 42:False → 34:Succeeded; 68:Out → 42:In; 42:True → 54:In; 42:True → 67:Succeeded; 42:False → 59:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 45:Out → 46:In; 46:Out → 61:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 32:Out → 50:In; 50:Out → 39:In; 68:CutSource → 50:CutDestination |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 32:Out → 56:In; 56:Out → 47:Succeeded; 68:CutSource → 56:CutDestination |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_kab_03_meds"}}}` | 53:Out → 58:In; 58:Out → 55:In; 58:Out → 57:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_johnny"}}}` | 60:Out → 39:In; 68:CutSource → 60:CutDestination |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\kabuki\\sts_wat_kab_03\\scenes\\sts_wat_kab_03_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 46:Out → 61:In; 61:Out → 28:In1 |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 62` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 64:Out → 62:In; 62:True → 65:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 36:Out → 63:In; 63:Out → 53:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 36:Out → 64:In; 64:Out → 62:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 65` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 62:True → 65:In; 65:True → 66:Succeeded |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 68` | `questCutControlNodeDefinition` `{}` | 33:Out → 68:In; 68:Out → 42:In; 68:CutSource → 50:CutDestination; 68:CutSource → 56:CutDestination; 68:CutSource → 60:CutDestination |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 69` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 69:True → 30:Succeeded; 69:True → 48:In; 72:Out → 69:In |
| `sts_wat_kab_03_bugfixing.questphase / h17 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 31:Out → 72:In; 72:Out → 69:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_start"},{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}]}}` | 12:Out → 2:In; 13:Out → 12:In; 12:Out → 35:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 31:Out → 15:In; 36:Out → 31:In; 31:Out → 40:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\kabuki\\sts_wat_kab_03\\scenes\\sts_wat_kab_03_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 34:Out → 1:In; 3:Out → 34:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 37` | `questCutControlNodeDefinition` `{"permanent":true}` | 37:CutSource → 7:CutDestination; 39:True → 37:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_activate"}}}` | 39:True → 37:In; 40:Out → 39:In |
| `sts_wat_kab_03_bugfixing.questphase / h361 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 31:Out → 40:In; 40:Out → 39:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-645885","value":1,"comparisonType":"Equal"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 7:In1; 4:False → 6:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHacked_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]}}}}` | 7:Out1 → 5:In; 5:Out → 8:In |
| `sts_wat_kab_03_bugfixing.questphase / h503 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:False → 6:In; 6:True → 7:In2 |
| `sts_wat_kab_03_bugfixing.questphase / h580 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-645884","value":1,"comparisonType":"Equal"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wat_kab_03_bugfixing.questphase / h580 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_start"}}` | 3:Out → 9:In; 9:Out → 10:In |
| `sts_wat_kab_03_bugfixing.questphase / h580 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 9:Out → 10:In; 10:False → 13:In |
| `sts_wat_kab_03_bugfixing.questphase / h640 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-668458"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wat_kab_03_bugfixing.questphase / h640 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_start"}}}` | 3:Out → 7:In; 7:Out → 14:In |
| `sts_wat_kab_03_bugfixing.questphase / h640 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 7:Out → 14:In; 14:Out → 15:In |
| `sts_wat_kab_03_bugfixing.questphase / h640 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_entrance_window"}}` | 15:Out → 9:In; 14:Out → 15:In |
| `sts_wat_kab_03_openworld.questphase / h2 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 29:Out → 17:In; 30:Out → 29:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_start_loop"},{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_entrance_window"}]}}` | 9:Out → 8:Succeeded; 52:Out → 9:In; 67:Out → 9:In; 9:Out → 72:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 10:Out → 14:In; 14:Out → 139:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_finished"}}}` | 76:Out → 44:In; 123:Out → 44:In; 44:False → 70:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_peace"}}}` | 47:False → 15:Succeeded; 139:Out → 47:In; 47:True → 94:In; 47:True → 138:Succeeded; 47:False → 121:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 109:Out → 65:In; 65:Out → 66:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_kab_03_test"}}}` | 66:False → 52:Active; 65:Out → 66:In; 66:True → 67:Active |
| `sts_wat_kab_03_openworld.questphase / h79 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 10:Out → 76:In; 76:Out → 44:In; 139:CutSource → 76:CutDestination |
| `sts_wat_kab_03_openworld.questphase / h79 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 0:Out → 80:In; 141:Out → 80:In; 80:Out → 81:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 86` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 83:Out → 86:In; 86:Out → 85:In; 88:Out → 86:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 85:Out → 87:In; 87:Out → 88:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 90:In; 90:Out → 91:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_ruined_apartment"}}` | 97:Out → 99:In; 99:Out → 98:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_ruined_apartment"}}` | 100:Out → 97:In; 126:CutSource → 100:CutDestination; 98:Out → 100:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 10:Out → 102:In; 102:Out → 70:Succeeded; 139:CutSource → 102:CutDestination |
| `sts_wat_kab_03_openworld.questphase / h79 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 61:Out → 69:In; 69:Out → 130:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 108` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 108:In; 108:False → 83:Active; 108:True → 140:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_kab_03_meds"}}}` | 89:Out → 112:In; 112:Out → 101:In; 112:Out → 104:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 115` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 115:In; 115:Out → 118:In1 |
| `sts_wat_kab_03_openworld.questphase / h79 / 116` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_peace"}}}` | 0:Out → 116:In; 116:Out → 118:In2 |
| `sts_wat_kab_03_openworld.questphase / h79 / 118` | `questLogicalXorNodeDefinition` `{}` | 118:Out1 → 114:In; 115:Out → 118:In1; 116:Out → 118:In2 |
| `sts_wat_kab_03_openworld.questphase / h79 / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 81:Out → 120:In; 120:Out → 119:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 123` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_johnny"}}}` | 123:Out → 44:In; 139:CutSource → 123:CutDestination; 124:Out → 123:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 126` | `questCutControlNodeDefinition` `{"permanent":true}` | 126:CutSource → 100:CutDestination; 128:Out → 126:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"isPlayer":false}}}` | 0:Out → 128:In; 128:Out → 126:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 130` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\kabuki\\sts_wat_kab_03\\scenes\\sts_wat_kab_03_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 130:Out → 1:In; 69:Out → 130:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 131` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 135:Out → 131:In; 131:True → 136:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_content_lock"}}` | 133:Out → 89:In; 134:Out → 133:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 135:Out → 131:In; 134:Out → 135:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 136` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 131:True → 136:In; 136:True → 137:Succeeded |
| `sts_wat_kab_03_openworld.questphase / h79 / 139` | `questCutControlNodeDefinition` `{}` | 14:Out → 139:In; 139:Out → 47:In; 139:CutSource → 76:CutDestination; 139:CutSource → 102:CutDestination; 139:CutSource → 123:CutDestination |
| `sts_wat_kab_03_openworld.questphase / h79 / 140` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 140:True → 83:Active; 140:False → 105:Start1; 108:True → 140:In |
| `sts_wat_kab_03_openworld.questphase / h79 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 141:Out → 80:In; 119:Out → 141:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_fluff_chat"}}` | 0:Out → 3:In; 3:Out → 4:neighbours |
| `sts_wat_kab_03_openworld.questphase / h680 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_suicide"}}` | 8:Out → 7:In; 7:Out → 21:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_johnny"}}}` | 0:Out → 8:In; 8:Out → 7:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_johnny_dead_body"}}` | 13:Out → 1:In; 10:End 0 → 13:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done"}}}` | 7:Out → 21:In; 21:True → 22:In |
| `sts_wat_kab_03_openworld.questphase / h680 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 22:Out → 10:Start 0; 21:True → 22:In |
| `sts_wat_kab_03_openworld.questphase / h760 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_start"},{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}]}}` | 12:Out → 2:In; 13:Out → 12:In; 12:Out → 35:In |
| `sts_wat_kab_03_openworld.questphase / h760 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 31:Out → 15:In; 36:Out → 31:In |
| `sts_wat_kab_03_openworld.questphase / h760 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\kabuki\\sts_wat_kab_03\\scenes\\sts_wat_kab_03_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 34:Out → 1:In; 3:Out → 34:In |
| `sts_wat_kab_03_openworld.questphase / h760 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 37:False → 7:Start1; 15:Out → 37:In; 37:True → 38:Active |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 63:0:0 → 64:0:1; 68:0:0 → 63:0:1 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 261` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":200}}}` | 61:666:0 → 261:0:1; 261:0:0 → 263:0:1; 267:0:0 → 261:0:1; 280:1:0 → 261:0:0 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 261:0:0 → 263:0:1; 263:0:0 → 269:0:1; 280:1:0 → 263:0:0 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":200}}}` | 263:0:0 → 269:0:1; 269:0:0 → 290:0:1; 280:1:0 → 269:0:0 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 277` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 61:666:0 → 277:0:1; 277:0:0 → 280:0:0 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 290` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 269:0:0 → 290:0:1; 290:0:0 → 265:0:1; 290:0:1 → 267:0:0 |
| `sts_wat_kab_03_holocall_debrief.scene / scene / 299` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 67:0:0 → 299:0:1; 299:0:0 → 297:0:1 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 82:0:0 → 83:0:1; 87:0:0 → 82:0:1 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 86:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 80:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 80:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_kab_03_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wat_kab_03_johnny_johnny"},"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 91:0:0 → 2:0:0; 130:0:0 → 91:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 4:0:0 → 117:0:1; 117:0:0 → 110:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 166` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_wat_kab_03_tr_apartment"}}` | 166:0:0 → 130:0:1; 195:0:0 → 166:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 179` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 1:0:0 → 179:0:1; 179:0:0 → 209:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_wat_kab_03_tr_solo_room"}}` | 116:0:0 → 183:0:1; 183:0:0 → 205:0:1; 183:0:0 → 214:0:0 |
| `sts_wat_kab_03_johnny.scene / scene / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_wat_kab_03_tr_solo_room"}}` | 162:0:1 → 192:0:1; 192:0:0 → 195:0:0 |
| `sts_wat_kab_03_johnny.scene / scene / 205` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 183:0:0 → 205:0:1; 205:0:0 → 222:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wat_kab_03_johnny_johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 179:0:0 → 209:0:1; 209:0:0 → 4:0:0 |
| `sts_wat_kab_03_johnny.scene / scene / 222` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wat_kab_03_johnny_johnny"},"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 205:0:0 → 222:0:1; 222:0:0 → 162:0:1 |
| `sts_wat_kab_03_johnny.scene / scene / 237` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 199:0:0 → 237:0:1; 237:0:0 → 231:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 790` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#kab_03_tr_fluff_chat"}}` | 769:0:0 → 790:0:1; 790:0:0 → 768:1:0 |
| `sts_wat_kab_03_scene.scene / scene / 797` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_gun_shot"}}}` | 797:0:0 → 1458:0:1; 1215:0:0 → 797:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 819` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"observedTargetRef":{"$type":"gameEntityReference","reference":"#player"}}}}` | 819:0:0 → 874:0:1; 887:0:1 → 819:0:1; 894:1:0 → 819:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 874` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 819:0:0 → 874:0:1; 874:0:0 → 882:0:1; 894:1:0 → 874:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 882` | `questConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"observedTargetRef":{"$type":"gameEntityReference","reference":"#player"}}}}` | 874:0:0 → 882:0:1; 882:0:0 → 887:0:1; 882:0:1 → 830:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 887` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":8.0}}}}` | 882:0:0 → 887:0:1; 887:0:0 → 830:0:0; 887:0:1 → 819:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 895` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_peace","value":1,"comparisonType":"Equal"}}}` | 27:0:0 → 895:0:1; 895:0:0 → 894:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1116` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","quantity":1}}}` | 757:0:0 → 1116:0:1; 1116:0:0 → 778:0:1; 1116:0:0 → 1147:0:0; 1116:0:0 → 1445:0:1; 1116:0:1 → 748:0:0; 1116:0:1 → 778:0:1; 1116:0:1 → 1445:0:1; 1375:0:0 → 1116:0:1; 1391:0:0 → 1116:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_interrupt"}}}` | 27:0:0 → 1124:0:1; 1124:0:0 → 826:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1161` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sts_wat_kab_03_kitchen_doors","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 27:0:0 → 1161:0:1; 1161:0:0 → 551:0:0; 1161:0:0 → 1177:1:0 |
| `sts_wat_kab_03_scene.scene / scene / 1166` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]}}}}` | 27:0:0 → 1166:0:1; 1166:0:0 → 1168:0:0; 1182:1:0 → 1166:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1188` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done"}}}` | 748:2:0 → 1188:0:1; 1147:2:0 → 1188:0:1; 1188:0:1 → 1190:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1190` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 1188:0:1 → 1190:0:1; 1190:0:0 → 1437:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 1194:0:0 → 1187:0:1; 1437:0:0 → 1194:0:1; 1440:0:0 → 1194:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1201` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"timeInterval":0.0,"onScreenTest":true,"inverted":true}}}` | 748:2:0 → 1201:0:1; 1147:2:0 → 1201:0:1; 1201:0:0 → 1203:0:0; 1201:0:0 → 1227:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1402` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 551:0:0 → 1402:0:1; 1402:0:0 → 557:1:0; 1402:0:0 → 1405:0:0; 1411:1:0 → 1402:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1414` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 553:0:0 → 1414:0:1; 1414:0:0 → 1405:0:1; 1415:1:0 → 1414:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1420` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 709:0:0 → 1420:0:1; 1420:0:0 → 1405:0:2; 1421:1:0 → 1420:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1437` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_kab_03_ready_1"}}}` | 1190:0:0 → 1437:0:1; 1437:0:0 → 1194:0:1; 1437:0:1 → 1440:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1440` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_wat_kab_03_tr_solo_room"}}` | 1437:0:1 → 1440:0:1; 1440:0:0 → 1194:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1452` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]},"timeInterval":2.5999999046325684,"inverted":true}}}` | 1452:0:0 → 1476:0:1; 1458:0:0 → 1452:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1458` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_wat_kab_03_tr_solo_room"}}` | 797:0:0 → 1458:0:1; 1458:0:0 → 1452:0:1 |
| `sts_wat_kab_03_scene.scene / scene / 1462` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#sts_wat_kab_03_drugs","eventType":"Executed"}}}` | 27:0:0 → 1462:0:1; 1462:0:0 → 716:0:0; 1466:1:0 → 1462:0:0 |
| `sts_wat_kab_03_scene.scene / scene / 1502` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHacked_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kab_03_com_ar","names":["solo"]}}}}` | 27:0:0 → 1502:0:1; 1502:0:0 → 716:0:0 |
| `sts_wat_kabuki.questphase / h9073 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_start_loop"},{"$type":"questTriggerCondition","triggerAreaRef":"#kab_03_tr_entrance_window"}]}}` | 9:Out → 8:Succeeded; 52:Out → 9:In; 67:Out → 9:In; 9:Out → 72:In |
| `sts_wat_kabuki.questphase / h9073 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 10:Out → 14:In; 14:Out → 139:In |
| `sts_wat_kabuki.questphase / h9073 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_finished"}}}` | 76:Out → 44:In; 123:Out → 44:In; 44:False → 70:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_peace"}}}` | 47:False → 15:Succeeded; 139:Out → 47:In; 47:True → 94:In; 47:True → 138:Succeeded; 47:False → 121:Succeeded |
| `sts_wat_kabuki.questphase / h9073 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_kab_03_test"}}}` | 66:False → 52:Active; 65:Out → 66:In; 66:True → 67:Active |
| `sts_wat_kabuki.questphase / h9073 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 10:Out → 76:In; 76:Out → 44:In; 139:CutSource → 76:CutDestination |
| `sts_wat_kabuki.questphase / h9073 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_kab_03_drugs"}}}}` | 10:Out → 102:In; 102:Out → 70:Succeeded; 139:CutSource → 102:CutDestination |
| `sts_wat_kabuki.questphase / h9073 / 131` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","itemTag":"Items.sts_wat_kab_03_meds","comparisonType":"Greater"}}}` | 135:Out → 131:In; 131:True → 136:In |
| `sts_wat_kabuki.questphase / h9073 / 136` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 131:True → 136:In; 136:True → 137:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 200` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/deliver_shard","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 193:True → 200:In; 194:True → 200:In; 195:True → 200:In; 200:True → 199:In; 329:Out → 200:In; 200:False → 311:In |
| `mq036_quest_bugfixes.questphase / h870 / 202` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/drop","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 313:Out → 202:In; 311:False → 202:In; 202:True → 203:In; 202:False → 205:In |
| `mq036_quest_bugfixes.questphase / h870 / 310` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"110954123004","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 310:False → 309:In; 311:True → 310:In; 310:True → 313:In |
| `mq036_quest_bugfixes.questphase / h870 / 311` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 200:False → 311:In; 311:False → 202:In; 214:Out → 311:In; 311:True → 310:In |
| `open_world_bugfixing.questphase / h116 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_finished"}}}` | 0:Out → 33:In; 33:True → 76:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_03_finished"}}}` | 0:Out → 33:In; 33:True → 76:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wat_kab_03_bugfixing.questphase / h640 / 14; sts_wat_kab_03_johnny.scene / scene / 209 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sts_wat_kab_03_scene.scene / scene / 1213 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sts_wat_kab_03_bugfixing.questphase / h17 / 45; sts_wat_kab_03_openworld.questphase / h2 / 24; sts_wat_kab_03_openworld.questphase / h79 / 109; sts_wat_kab_03_openworld.questphase / h79 / 61; +1 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_wat_kab_03_johnny.scene / scene / 8; sts_wat_kab_03_scene.scene / scene / 557; sts_wat_kab_03_scene.scene / scene / 701; sts_wat_kab_03_scene.scene / scene / 712; +2 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_wat_kab_03_bugfixing.questphase / h361 / 35; sts_wat_kab_03_openworld.questphase / h2 / 22; sts_wat_kab_03_openworld.questphase / h760 / 35 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h116 / 33; open_world_bugfixing.questphase / h2878 / 33; sts_wat_kab_03_bugfixing.questphase / h0 / 14; sts_wat_kab_03_bugfixing.questphase / h17 / 2; +33 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wat_kab_03_bugfixing.questphase / h17 / 44; sts_wat_kab_03_bugfixing.questphase / h17 / 53; sts_wat_kab_03_bugfixing.questphase / h361 / 15; sts_wat_kab_03_openworld.questphase / h760 / 15; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 214; sts_wat_kab_03_bugfixing.questphase / h17 / 43; sts_wat_kab_03_bugfixing.questphase / h17 / 51; sts_wat_kab_03_bugfixing.questphase / h503 / 8; +6 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_state` | sts_wat_kab_03_scene.scene / scene / 1161 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_wat_kab_03_bugfixing.questphase / h361 / 12; sts_wat_kab_03_openworld.questphase / h760 / 12 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 310; sts_wat_kab_03_bugfixing.questphase / h17 / 33; sts_wat_kab_03_bugfixing.questphase / h17 / 62; sts_wat_kab_03_johnny.scene / scene / 117; +6 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h116 / 76; open_world_bugfixing.questphase / h2878 / 76; sts_wat_kab_03_bugfixing.questphase / h17 / 30; sts_wat_kab_03_bugfixing.questphase / h17 / 32; +52 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | sts_wat_kab_03_bugfixing.questphase / h17 / 3; sts_wat_kab_03_bugfixing.questphase / h17 / 38; sts_wat_kab_03_bugfixing.questphase / h17 / 54; sts_wat_kab_03_bugfixing.questphase / h361 / 10; +35 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wat_kab_03_openworld.questphase / h79 / 118 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wat_kab_03_bugfixing.questphase / h17 / 46; sts_wat_kab_03_bugfixing.questphase / h17 / 64; sts_wat_kab_03_bugfixing.questphase / h17 / 72; sts_wat_kab_03_bugfixing.questphase / h361 / 31; +19 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_wat_kab_03_bugfixing.questphase / h17 / 68; sts_wat_kab_03_bugfixing.questphase / h361 / 37; sts_wat_kab_03_openworld.questphase / h79 / 126; sts_wat_kab_03_openworld.questphase / h79 / 139 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_wat_kab_03_bugfixing.questphase / h361 / 8; sts_wat_kab_03_openworld.questphase / h760 / 8 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_wat_kab_03_bugfixing.questphase / h361 / 7; sts_wat_kab_03_openworld.questphase / h680 / 10; sts_wat_kab_03_openworld.questphase / h680 / 4; sts_wat_kab_03_openworld.questphase / h760 / 7; +1 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wat_kab_03_bugfixing.questphase / h17 / 31; sts_wat_kab_03_bugfixing.questphase / h17 / 63; sts_wat_kab_03_bugfixing.questphase / h361 / 12; sts_wat_kab_03_bugfixing.questphase / h580 / 9; +20 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_wat_kab_03_bugfixing.questphase / h580 / 10; sts_wat_kab_03_openworld.questphase / h79 / 115; sts_wat_kab_03_openworld.questphase / h79 / 90 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_wat_kab_03_johnny.scene / scene / 101; sts_wat_kab_03_johnny.scene / scene / 162; sts_wat_kab_03_johnny.scene / scene / 226; sts_wat_kab_03_johnny.scene / scene / 95; +19 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_wat_kab_03_bugfixing.questphase / h361 / 2; sts_wat_kab_03_bugfixing.questphase / h361 / 3; sts_wat_kab_03_openworld.questphase / h2 / 18; sts_wat_kab_03_openworld.questphase / h2 / 19; +3 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` | repair; journal anchor | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` | content candidate; journal anchor | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` | content candidate; forward dependency | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` | content candidate; forward dependency | `base-sts-wat-kab-03` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wat-kab-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wat-kab-03.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

297 repeated typed/socket path signatures in this selected graph context; 63 distinct direct resource identities; 9 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 67 -> 299 -> 297 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 252 -> 68 -> 63 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 299 -> 297 -> 301 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` / scene / 81 -> 84 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` / scene / 29 -> 85 -> 87 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` / scene / 769 -> 768 -> 771 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 295 -> 67 -> 299 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 59 -> 295 -> 67 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 277 -> 280 -> 261 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` / scene / 285 -> 283 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `fe9d2c1bdd2cebf30eb2` | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` / scene / 84 -> 29 -> 85 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h0 / 6 | `h17` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 28 | `h361` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h0 / 8 | `h503` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h0 / 13 | `h580` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h0 / 16 | `h640` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h0 / 1 | `h2` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h0 / 5 | `h79` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h0 / 16 | `h680` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` / h0 / 18 | `h760` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\quest\minor_quests\mq025\batty\batty_definition.gamedef` | content candidate | base\quest\minor_quests\mq025\batty\batty_quest.quest |
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
| `base\quest\main_quests\part1\q108\q108_johnny.gamedef` | content candidate | base\quest\main_quests\part1\q108\q108_johnny.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.gamedef` | content candidate | base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest |
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
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
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
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_definition.gamedef` | content candidate | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_quest.quest |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_testworld_def.gamedef` | content candidate | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_quest.quest |
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
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_folded__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_stand_2h_rifle_aim.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_stand__rh_shotgun.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__sit_chair_lean0__2h_elbow_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\open_world\generic_male_big_work__dead_bodies__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\sts_quests\sts_wat_kab_03\sts_wab_kab_03__male_big.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_holocall_debrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_holocall_prebrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_johnny\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_johnny\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_scene\civ_low_m_107_bra_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_scene\civ_low_m_93_chn_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_scene\corporal_hare.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_scene\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\lipsync\en\sts_wat_kab_03_scene\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_back__dead__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front__nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_riffle__aim__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\sts_quests\sts_wat_kab_03\sts_wat_kab_03_rifle.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\sts_quests\sts_wat_kab_03\sts_wat_kab_03_shotgun.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\sts_quests\sts_wat_kab_03__mb_gang__rifle_aim__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 186; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 379; 193 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 375; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; 74 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 395; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 412; 102 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 403; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; 63 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 185; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 378; 252 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 373; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; 69 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `kab_03_finished` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h9073 / 42; 1 total source locations in compressed evidence |
| `kab_03_gun_shot` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h9073 / 94; 1 total source locations in compressed evidence |
| `kab_03_interrupt` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h20265 / 7; base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase / h72 / 7; 2 total source locations in compressed evidence |
| `kab_03_peace` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h9073 / 91; 1 total source locations in compressed evidence |
| `kab_03_start` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h9073 / 41; 1 total source locations in compressed evidence |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `sts_wat_kab_03_test` | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_quest.quest / h0 / 13; 1 total source locations in compressed evidence |
| `wat_achievement` | base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase / h0 / 81; base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase / h0 / 89; base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase / h0 / 50; base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase / h0 / 66; 66 total source locations in compressed evidence |
| `welcome_holocall_skipped` | base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h1701 / 275; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h3924 / 125; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h4664 / 232; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h5754 / 195; 41 total source locations in compressed evidence |

NodeRef uses: 141; TweakDB binding uses: 43. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` | 1 / 1 | scnDialogLineEvent: 1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` | 7 / 36 | scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 15; scnLookAtEvent: 7; scnPlaySkAnimEvent: 7; scneventsSocket: 6 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` | 26 / 139 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 5; scnDialogLineEvent: 71; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 10; scnPlaySkAnimEvent: 24; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 22 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
