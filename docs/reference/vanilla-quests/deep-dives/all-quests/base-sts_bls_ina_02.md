# Gig: Big Pete's Got Big Problems

Journal: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` · `StreetStory` · hash `4224564162`.

Journal premise: Gig type: Gun for Hire\nObjective: Get rid of Big Pete – a mechanic with the Wraiths.\nDetails:\n\nBig Pete runs a garage out here in the Badlands, fixes up clunkers for the Raffen Shiv. Before that he was hustling as a techie in Night City. Now, Pete's not your definition of a nice guy. Soon enough he made some powerful enemies and had to skip town.\nJust so happens Pete's enemies are my friends and I owe said friends a favor. You make Big Pete eat dust – I get one less favor to owe.\n\nIt's not hard to find him. Just try any of the Wraith's garages.

**Coverage: journal-linked.** 44 exact journal-linked nodes in 5 resources; 8 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Carry out the hit on Big Pete. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/complete_the_hit_on_big_pete` |
| Neutralize Big Pete. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` |
| Find Big Pete. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` |
| Get inside Big Pete's garage. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` |
| Leave the area. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_02_bugfixing.questphase / h111 / 4` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 4:False → 1:In; 3:Out → 4:In; 4:True → 5:In |
| `sts_bls_ina_02_bugfixing.questphase / h223 / 6` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 5:True → 6:In; 6:True → 7:In; 6:False → 8:In |
| `sts_bls_ina_02_bugfixing.questphase / h304 / 4` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 3:Out → 4:In; 4:True → 5:In |
| `sts_bls_ina_02_ow.questphase / h543 / 56` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 72:Out → 56:Active; 56:Out → 57:In; 56:Out → 93:In; 56:Out → 133:In |
| `sts_bls_ina_02_ow.questphase / h543 / 58` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 94:Out1 → 58:Succeeded; 58:Out → 59:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 59` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 58:Out → 59:Active; 59:Out → 61:In; 59:Out → 140:In |
| `sts_bls_ina_02_ow.questphase / h543 / 62` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 146:Out → 62:Succeeded; 62:Out → 66:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 65` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 64:Out → 65:Succeeded; 65:Out → 147:In |
| `sts_bls_ina_02_ow.questphase / h543 / 66` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 62:Out → 66:Active; 66:Out → 64:In |
| `sts_bls_ina_02_ow.questphase / h543 / 67` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | 148:Out → 67:Succeeded; 67:Out → 91:In |
| `sts_bls_ina_02_ow.questphase / h543 / 72` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 72:Out → 56:Active; 135:Out1 → 72:Succeeded |
| `sts_bls_ina_02_ow.questphase / h543 / 85` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | No connected edge in indexed graph |
| `sts_bls_ina_02_ow.questphase / h543 / 110` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 109:Out → 110:In; 110:True → 111:Inactive; 110:False → 112:In |
| `sts_bls_ina_02_ow.questphase / h543 / 111` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 110:True → 111:Inactive; 111:Out → 112:In |
| `sts_bls_ina_02_ow.questphase / h543 / 112` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 110:False → 112:In; 111:Out → 112:In; 112:True → 113:Inactive; 112:False → 114:Succeeded |
| `sts_bls_ina_02_ow.questphase / h543 / 113` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 112:True → 113:Inactive; 113:Out → 114:Succeeded |
| `sts_bls_ina_02_ow.questphase / h543 / 114` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 112:False → 114:Succeeded; 113:Out → 114:Succeeded; 114:Out → 116:In |
| `sts_bls_ina_02_ow.questphase / h543 / 117` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 117:Out → 64:In; 116:True → 117:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 149` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 79:True → 149:Active; 149:Out → 151:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 150` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 0:Out → 150:Active; 150:Out → 68:In; 79:False → 150:Active; 150:Out → 134:In; 150:Out → 152:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 151` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | 151:Out → 68:In; 151:Out → 134:In; 149:Out → 151:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 152` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | 152:Out → 68:In; 152:Out → 134:In; 150:Out → 152:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 56` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 72:Out → 56:Active; 56:Out → 57:In; 56:Out → 93:In; 56:Out → 133:In |
| `sts_bls_inland_avenue.questphase / h18378 / 58` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 94:Out1 → 58:Succeeded; 58:Out → 59:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 59` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 58:Out → 59:Active; 59:Out → 61:In; 59:Out → 140:In |
| `sts_bls_inland_avenue.questphase / h18378 / 62` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 146:Out → 62:Succeeded; 62:Out → 66:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 65` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 64:Out → 65:Succeeded; 65:Out → 147:In |
| `sts_bls_inland_avenue.questphase / h18378 / 66` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 62:Out → 66:Active; 66:Out → 64:In |
| `sts_bls_inland_avenue.questphase / h18378 / 67` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | 148:Out → 67:Succeeded; 67:Out → 91:In |
| `sts_bls_inland_avenue.questphase / h18378 / 72` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 72:Out → 56:Active; 135:Out1 → 72:Succeeded |
| `sts_bls_inland_avenue.questphase / h18378 / 85` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | No connected edge in indexed graph |
| `sts_bls_inland_avenue.questphase / h18378 / 110` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 109:Out → 110:In; 110:True → 111:Inactive; 110:False → 112:In |
| `sts_bls_inland_avenue.questphase / h18378 / 111` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 110:True → 111:Inactive; 111:Out → 112:In |
| `sts_bls_inland_avenue.questphase / h18378 / 112` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 110:False → 112:In; 111:Out → 112:In; 112:True → 113:Inactive; 112:False → 114:Succeeded |
| `sts_bls_inland_avenue.questphase / h18378 / 113` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete` | 112:True → 113:Inactive; 113:Out → 114:Succeeded |
| `sts_bls_inland_avenue.questphase / h18378 / 114` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete` | 112:False → 114:Succeeded; 113:Out → 114:Succeeded; 114:Out → 116:In |
| `sts_bls_inland_avenue.questphase / h18378 / 117` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave` | 117:Out → 64:In; 116:True → 117:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 149` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 79:True → 149:Active; 149:Out → 151:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 150` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in` | 0:Out → 150:Active; 150:Out → 68:In; 79:False → 150:Active; 150:Out → 134:In; 150:Out → 152:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 151` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | 151:Out → 68:In; 151:Out → 134:In; 149:Out → 151:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 152` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing` | 152:Out → 68:In; 152:Out → 134:In; 150:Out → 152:Active |
| `sts_badlands.questphase / h11 / 2` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | 0:Out → 2:In; 2:Out → 12:In1 |
| `open_world_bugfixing.questphase / h1543 / 8` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | 7:True → 8:Succeeded |
| `open_world_bugfixing.questphase / h2679 / 8` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02` | 7:True → 8:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_02_ow.questphase / h11 / 2` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene`; `#sts_sm_bls_ina_02_big_pete_scene` | 8:Out → 2:big_pete_door; 2:big_pete_spared → 80:In; 2:big_pete_spared → 83:In |
| `sts_bls_ina_02_ow.questphase / h543 / 129` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene`; `#sts_sm_bls_ina_02_holocall_prebrief` | 129:End 0 → 95:Active; 129:rejected_out → 95:Active; 130:True → 129:Start 0; 129:Holocall INT → 132:In; 129:Holocall RET → 131:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 84` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene`; `#sts_sm_bls_ina_02_holocall_debriefs` | 84:End 0 → 23:In; 108:False → 84:Start 0; 84:rejected_out → 109:In; 84:Holocall INT → 93:In; 84:Holocall RET → 92:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_ina_south_bugfixing.questphase` / h0 / 8 | `sts_bls_ina_02_bugfixing.questphase` | 14: DeletionMarker; 14:Out → 8:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_phase.questphase` / h0 / 2 | `sts_bls_ina_02_ow.questphase` | 0: Input; 0:Out → 2:In1; 2:Out2 → 7:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h10779 / 2 | `sts_bls_ina_02_ow.questphase` | 0: Input; 0:Out → 2:In1; 2:Out2 → 7:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h11 / 2 | `sts_bls_ina_02_big_pete_scene.scene` | 8: CutControl; 8:Out → 2:big_pete_door; 2:big_pete_spared → 80:In; 2:big_pete_spared → 83:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h17846 / 2 | `sts_bls_ina_02_big_pete_scene.scene` | 8: CutControl; 8:Out → 2:big_pete_door; 2:big_pete_spared → 80:In; 2:big_pete_spared → 83:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h1017 / 84 | `sts_bls_ina_02_holocall_debriefs.scene` | 108: Condition; 84:End 0 → 23:In; 108:False → 84:Start 0; 84:rejected_out → 109:In; 84:Holocall INT → 93:In; 84:Holocall RET → 92:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h18852 / 84 | `sts_bls_ina_02_holocall_debriefs.scene` | 108: Condition; 84:End 0 → 23:In; 108:False → 84:Start 0; 84:rejected_out → 109:In; 84:Holocall INT → 93:In; 84:Holocall RET → 92:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h543 / 129 | `sts_bls_ina_02_holocall_prebrief.scene` | 130: Condition; 129:End 0 → 95:Active; 129:rejected_out → 95:Active; 130:True → 129:Start 0; 129:Holocall INT → 132:In; 129:Holocall RET → 131:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h18378 / 129 | `sts_bls_ina_02_holocall_prebrief.scene` | 130: Condition; 129:End 0 → 95:Active; 129:rejected_out → 95:Active; 130:True → 129:Start 0; 129:Holocall INT → 132:In; 129:Holocall RET → 131:In |
| `base\open_world\street_stories\badlands\sts_badlands.questphase` / h0 / 2 | `sts_bls_inland_avenue.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 2 | `sts_badlands.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 49 | `sts_ina_south_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 49:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.quest` / h0 / 6 | `sts_bls_ina_02_phase.questphase` | 16: FactsDBManager: ina_02_test_def; 6:Out1 → 1:In; 16:Out → 6:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h0 / 2 | `sts_bls_ina_02_phase.questphase` | 41: Journal; 41:Out → 2:In1 |
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
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

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_bls_ina_02_big_pete_scene.scene` | big_pete_door → big_pete_spared | big_pete; Player; 47 nodes / 51 edges |
| `sts_bls_ina_02_holocall_debriefs.scene` | Start 0 → rejected_out, End 0 | dakota; 25 nodes / 33 edges |
| `sts_bls_ina_02_holocall_prebrief.scene` | Start 0 → rejected_out, End 0 | dakota; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_bls_ina_02_big_pete_scene.scene / n21 / 0` | No can do. (`Disagree`) | No option-level predicate stored | 0:0 → 36:0:0 |
| `sts_bls_ina_02_big_pete_scene.scene / n21 / 1` | Fine, but I don't want your money. (`Agree`) | No option-level predicate stored | 0:1 → 431:0:1 |
| `sts_bls_ina_02_big_pete_scene.scene / n21 / 2` | Deal. (`bribe`) | No option-level predicate stored | 0:2 → 435:0:1 |
| `sts_bls_ina_02_big_pete_scene.scene / n21 / 3` | I know you're broke. (`no_money`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "ina_02_found_email", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:3 → 302:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `#ina_02_combat_triggered` | Producer outside selected context | sts_bls_ina_02_big_pete_scene.scene / scene / 409; sts_bls_ina_02_ow.questphase / h133 / 13 |
| `#ina_02_pete_found` | sts_bls_ina_02_big_pete_scene.scene / scene / 105 | sts_bls_ina_02_ow.questphase / h543 / 57; sts_bls_inland_avenue.questphase / h18378 / 57 |
| `CYB-566436` | sts_bls_ina_02_bugfixing.questphase / h14 / 9 | sts_bls_ina_02_bugfixing.questphase / h14 / 8 |
| `CYB-625945` | sts_bls_ina_02_bugfixing.questphase / h111 / 3 | sts_bls_ina_02_bugfixing.questphase / h111 / 2 |
| `CYB-627009` | sts_bls_ina_02_bugfixing.questphase / h177 / 3 | sts_bls_ina_02_bugfixing.questphase / h177 / 2 |
| `CYB-646285` | sts_bls_ina_02_bugfixing.questphase / h223 / 3 | sts_bls_ina_02_bugfixing.questphase / h223 / 2 |
| `CYB-654476` | sts_bls_ina_02_bugfixing.questphase / h304 / 3 | sts_bls_ina_02_bugfixing.questphase / h304 / 2 |
| `bls_achievement` | sts_bls_ina_02_ow.questphase / h1017 / 22 | sts_bls_ina_02_ow.questphase / h1017 / 94 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_bls_ina_02_holocall_prebrief.scene / scene / 297 |
| `holo_dakota_calls_v_end_activate` | sts_bls_ina_02_holocall_debriefs.scene / scene / 99; sts_bls_ina_02_holocall_prebrief.scene / scene / 83; sts_bls_ina_02_ow.questphase / h1017 / 93; sts_bls_ina_02_ow.questphase / h543 / 132 | No reader in selected context |
| `holo_dakota_calls_v_end_done` | sts_bls_ina_02_holocall_debriefs.scene / scene / 95; sts_bls_ina_02_holocall_prebrief.scene / scene / 79 | sts_bls_ina_02_holocall_debriefs.scene / scene / 94; sts_bls_ina_02_holocall_prebrief.scene / scene / 78 |
| `holo_dakota_calls_v_rejectable` | sts_bls_ina_02_holocall_debriefs.scene / scene / 280; sts_bls_ina_02_holocall_prebrief.scene / scene / 254; sts_bls_ina_02_holocall_prebrief.scene / scene / 292 | No reader in selected context |
| `holo_dakota_calls_v_rejected` | sts_bls_ina_02_holocall_debriefs.scene / scene / 284; sts_bls_ina_02_holocall_prebrief.scene / scene / 266 | sts_bls_ina_02_holocall_debriefs.scene / scene / 282; sts_bls_ina_02_holocall_prebrief.scene / scene / 262 |
| `holo_dakota_calls_v_start_activate` | sts_bls_ina_02_holocall_debriefs.scene / scene / 267; sts_bls_ina_02_holocall_debriefs.scene / scene / 98; sts_bls_ina_02_holocall_prebrief.scene / scene / 290; sts_bls_ina_02_holocall_prebrief.scene / scene / 82; sts_bls_ina_02_ow.questphase / h1017 / 92; sts_bls_ina_02_ow.questphase / h543 / 131 | sts_bls_ina_02_holocall_debriefs.scene / scene / 256 |
| `holo_dakota_calls_v_start_done` | sts_bls_ina_02_holocall_debriefs.scene / scene / 93; sts_bls_ina_02_holocall_prebrief.scene / scene / 77 | sts_bls_ina_02_holocall_debriefs.scene / scene / 249; sts_bls_ina_02_holocall_prebrief.scene / scene / 273 |
| `holo_setup_active` | Producer outside selected context | sts_bls_ina_02_holocall_debriefs.scene / scene / 256; sts_bls_ina_02_holocall_prebrief.scene / scene / 297 |
| `holo_setup_started` | Producer outside selected context | sts_bls_ina_02_holocall_debriefs.scene / scene / 256; sts_bls_ina_02_holocall_prebrief.scene / scene / 297 |
| `ina_02_after_holocall` | sts_bls_ina_02_ow.questphase / h1017 / 113 | No reader in selected context |
| `ina_02_big_pete_dead` | sts_bls_ina_02_ow.questphase / h2 / 14 | sts_bls_ina_02_holocall_debriefs.scene / scene / 71; sts_bls_ina_02_ow.questphase / h1017 / 109 |
| `ina_02_big_pete_spared` | sts_bls_ina_02_big_pete_scene.scene / scene / 26; sts_bls_ina_02_big_pete_scene.scene / scene / 431; sts_bls_ina_02_big_pete_scene.scene / scene / 435; sts_bls_ina_02_bugfixing.questphase / h304 / 10 | sts_bls_ina_02_bugfixing.questphase / h304 / 5; sts_bls_ina_02_ow.questphase / h11 / 102; sts_bls_ina_02_ow.questphase / h543 / 61; sts_bls_inland_avenue.questphase / h18378 / 61 |
| `ina_02_bp_attack` | sts_bls_ina_02_big_pete_scene.scene / scene / 220 | sts_bls_ina_02_ow.questphase / h11 / 33 |
| `ina_02_finished` | sts_bls_ina_02_ow.questphase / h543 / 91; sts_bls_inland_avenue.questphase / h18378 / 91 | open_world_bugfixing.questphase / h1543 / 7; open_world_bugfixing.questphase / h2679 / 7; sts_bls_ina_02_bugfixing.questphase / h223 / 7 |
| `ina_02_found_email` | Producer outside selected context | sts_bls_ina_02_big_pete_scene.scene / scene / 21 |
| `ina_02_gang_retaliation` | Producer outside selected context | sts_bls_ina_02_ow.questphase / h1017 / 114 |
| `ina_02_impossible_fact` | Producer outside selected context | sts_bls_ina_02_ow.questphase / h1017 / 85 |
| `ina_02_no_combat_fix` | Producer outside selected context | sts_bls_ina_02_ow.questphase / h133 / 12 |
| `ina_02_pete_afraid` | sts_bls_ina_02_ow.questphase / h133 / 7 | No reader in selected context |
| `ina_02_post_community` | sts_bls_ina_02_ow.questphase / h1017 / 18 | sts_bls_ina_02_bugfixing.questphase / h14 / 11; sts_bls_ina_02_bugfixing.questphase / h14 / 12 |
| `ina_02_ready` | sts_bls_ina_02_ow.questphase / h1425 / 15 | No reader in selected context |
| `ina_02_scene_started` | sts_bls_ina_02_big_pete_scene.scene / scene / 281 | sts_bls_ina_02_ow.questphase / h133 / 5 |
| `ina_02_start` | sts_bls_ina_02_ow.questphase / h1425 / 28 | sts_bls_ina_02_bugfixing.questphase / h14 / 10 |
| `ina_02_test_def` | Producer outside selected context | sts_bls_ina_02_ow.questphase / h543 / 79; sts_bls_inland_avenue.questphase / h18378 / 79 |
| `kab_01_done` | Producer outside selected context | sts_bls_ina_02_big_pete_scene.scene / scene / 155 |
| `sts_bls_ina_tier_2` | Producer outside selected context | sts_bls_ina_02_bugfixing.questphase / h223 / 5 |
| `sts_wraiths_retaliation` | sts_bls_ina_02_ow.questphase / h1017 / 115 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sts_bls_ina_02_bugfixing.questphase / h0 / 18 |

## Exact gates, joins and cancellation

<details><summary>131 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_02_bugfixing.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 21:Out1 → 18:In |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["guard_01","guard_02","guard_03","guard_04","guard_05","guard_06","guard_07","guard_10","guard_11"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":9,"comparisonType":"GreaterOrEqual"}}}}` | 11:False → 2:In; 2:Out → 4:In2 |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ina_02_turret_roof","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsUnpowered"}}}` | 11:False → 3:In; 3:Out → 4:In1 |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 4` | `questLogicalAndNodeDefinition` `{}` | 2:Out → 4:In2; 3:Out → 4:In1; 4:Out1 → 6:In |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-566436"}}}` | 0:Out → 8:In; 8:False → 9:In |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_start"}}}` | 10:False → 1:In; 9:Out → 10:In; 10:True → 11:In |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_post_community"}}}` | 11:False → 2:In; 11:False → 3:In; 10:True → 11:In; 11:False → 12:In |
| `sts_bls_ina_02_bugfixing.questphase / h14 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_post_community"}}}` | 12:Out → 6:In; 11:False → 12:In |
| `sts_bls_ina_02_bugfixing.questphase / h111 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-625945"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_02_bugfixing.questphase / h111 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:False → 1:In; 3:Out → 4:In; 4:True → 5:In |
| `sts_bls_ina_02_bugfixing.questphase / h111 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 4:True → 5:In; 5:True → 7:In |
| `sts_bls_ina_02_bugfixing.questphase / h111 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 5:True → 7:In; 7:Out → 6:In |
| `sts_bls_ina_02_bugfixing.questphase / h177 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-627009"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_02_bugfixing.questphase / h177 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_content_lock"}}` | 3:Out → 11:In; 11:True → 9:In |
| `sts_bls_ina_02_bugfixing.questphase / h223 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-646285"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_02_bugfixing.questphase / h223 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_bls_ina_tier_2"}}}` | 3:Out → 5:In; 5:True → 6:In; 5:False → 8:In |
| `sts_bls_ina_02_bugfixing.questphase / h223 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 5:True → 6:In; 6:True → 7:In; 6:False → 8:In |
| `sts_bls_ina_02_bugfixing.questphase / h223 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_finished"}}}` | 7:False → 1:In; 6:True → 7:In; 7:True → 8:In |
| `sts_bls_ina_02_bugfixing.questphase / h304 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-654476"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_02_bugfixing.questphase / h304 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 5:In |
| `sts_bls_ina_02_bugfixing.questphase / h304 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_spared"}}}` | 4:True → 5:In; 5:True → 7:In |
| `sts_bls_ina_02_ow.questphase / h2 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 19:Out → 14:In; 20:Out → 19:In |
| `sts_bls_ina_02_ow.questphase / h11 / 8` | `questCutControlNodeDefinition` `{}` | 8:Out → 2:big_pete_door; 111:Out → 8:In; 8:Out → 108:In; 8:CutSource → 58:CutDestination |
| `sts_bls_ina_02_ow.questphase / h11 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]}}}}` | 0:Out → 11:In; 11:Out → 23:In1 |
| `sts_bls_ina_02_ow.questphase / h11 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"isPlayer":false}}}` | 0:Out → 13:In; 13:Out → 23:In4 |
| `sts_bls_ina_02_ow.questphase / h11 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 0:Out → 22:In; 22:Out → 23:In2 |
| `sts_bls_ina_02_ow.questphase / h11 / 23` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 11:Out → 23:In1; 13:Out → 23:In4; 22:Out → 23:In2; 33:Out → 23:In3; 23:Out1 → 102:In |
| `sts_bls_ina_02_ow.questphase / h11 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 46:Out → 27:In; 27:Out → 65:In |
| `sts_bls_ina_02_ow.questphase / h11 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_bp_attack"}}}` | 0:Out → 33:In; 33:Out → 23:In3 |
| `sts_bls_ina_02_ow.questphase / h11 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 85:Out1 → 67:In; 75:Out → 67:In; 67:Out → 68:In |
| `sts_bls_ina_02_ow.questphase / h11 / 68` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_petes_basement"}}` | 67:Out → 68:In; 68:True → 73:In |
| `sts_bls_ina_02_ow.questphase / h11 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 80:Out → 79:In; 79:Out → 87:In |
| `sts_bls_ina_02_ow.questphase / h11 / 83` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers"},"isPlayerActivator":false}}` | 2:big_pete_spared → 83:In; 83:False → 81:In1; 83:True → 98:In1 |
| `sts_bls_ina_02_ow.questphase / h11 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_01"]},"isPlayerActivator":false}}` | 98:Out1 → 88:In; 88:Out → 97:In1 |
| `sts_bls_ina_02_ow.questphase / h11 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_02"]},"isPlayerActivator":false}}` | 98:Out1 → 89:In; 89:Out → 97:In2 |
| `sts_bls_ina_02_ow.questphase / h11 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_03"]},"isPlayerActivator":false}}` | 98:Out1 → 90:In; 90:Out → 97:In3 |
| `sts_bls_ina_02_ow.questphase / h11 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_04"]},"isPlayerActivator":false}}` | 98:Out1 → 91:In; 91:Out → 97:In4 |
| `sts_bls_ina_02_ow.questphase / h11 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_05"]},"isPlayerActivator":false}}` | 98:Out1 → 92:In; 92:Out → 97:In5 |
| `sts_bls_ina_02_ow.questphase / h11 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_06"]},"isPlayerActivator":false}}` | 98:Out1 → 93:In; 93:Out → 97:In6 |
| `sts_bls_ina_02_ow.questphase / h11 / 94` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_07"]},"isPlayerActivator":false}}` | 98:Out1 → 94:In; 94:Out → 97:In7 |
| `sts_bls_ina_02_ow.questphase / h11 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_10"]},"isPlayerActivator":false}}` | 98:Out1 → 95:In; 95:Out → 97:In8 |
| `sts_bls_ina_02_ow.questphase / h11 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_11"]},"isPlayerActivator":false}}` | 98:Out1 → 96:In; 96:Out → 97:In9 |
| `sts_bls_ina_02_ow.questphase / h11 / 97` | `questLogicalAndNodeDefinition` `{"inputSocketCount":9}` | 97:Out1 → 81:In1; 88:Out → 97:In1; 89:Out → 97:In2; 90:Out → 97:In3; 91:Out → 97:In4; 92:Out → 97:In5; 93:Out → 97:In6; 94:Out → 97:In7; 95:Out → 97:In8; 96:Out → 97:In9 |
| `sts_bls_ina_02_ow.questphase / h11 / 102` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_spared"}}}` | 23:Out1 → 102:In; 102:False → 101:In |
| `sts_bls_ina_02_ow.questphase / h11 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ina_02_big_petes_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 112:Out → 111:In; 114:Out → 112:In |
| `sts_bls_ina_02_ow.questphase / h133 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"onScreenTest":true,"inverted":true}}}` | 4:True → 3:In; 3:Out → 6:In |
| `sts_bls_ina_02_ow.questphase / h133 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"onScreenTest":true}}}` | 4:True → 3:In; 13:Out → 4:In; 4:False → 6:In |
| `sts_bls_ina_02_ow.questphase / h133 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_scene_started"}}}` | 0:Out → 5:In; 5:Out → 1:In |
| `sts_bls_ina_02_ow.questphase / h133 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_no_combat_fix","value":1,"comparisonType":"GreaterOrEqual"}}}` | 14:Out → 12:In; 12:Out → 13:In |
| `sts_bls_ina_02_ow.questphase / h133 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#ina_02_combat_triggered"}}}` | 13:Out → 4:In; 12:Out → 13:In |
| `sts_bls_ina_02_ow.questphase / h273 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_01"]},"isPlayerActivator":false}}` | 0:Out → 3:In; 3:Out → 13:In1 |
| `sts_bls_ina_02_ow.questphase / h273 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_02"]},"isPlayerActivator":false}}` | 0:Out → 5:In; 5:Out → 13:In2 |
| `sts_bls_ina_02_ow.questphase / h273 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_03"]},"isPlayerActivator":false}}` | 0:Out → 6:In; 6:Out → 13:In3 |
| `sts_bls_ina_02_ow.questphase / h273 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_04"]},"isPlayerActivator":false}}` | 0:Out → 7:In |
| `sts_bls_ina_02_ow.questphase / h273 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_05"]},"isPlayerActivator":false}}` | 0:Out → 8:In; 8:Out → 13:In4 |
| `sts_bls_ina_02_ow.questphase / h273 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_06"]},"isPlayerActivator":false}}` | 0:Out → 9:In; 9:Out → 13:In5 |
| `sts_bls_ina_02_ow.questphase / h273 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_07"]},"isPlayerActivator":false}}` | 0:Out → 10:In; 10:Out → 13:In6 |
| `sts_bls_ina_02_ow.questphase / h273 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_10"]},"isPlayerActivator":false}}` | 0:Out → 11:In; 11:Out → 13:In7 |
| `sts_bls_ina_02_ow.questphase / h273 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_basement","activatorRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers","names":["ganger_11"]},"isPlayerActivator":false}}` | 0:Out → 12:In; 12:Out → 13:In8 |
| `sts_bls_ina_02_ow.questphase / h273 / 13` | `questLogicalXorNodeDefinition` `{"inputSocketCount":8}` | 3:Out → 13:In1; 13:Out1 → 4:In; 5:Out → 13:In2; 6:Out → 13:In3; 8:Out → 13:In4; 9:Out → 13:In5; 10:Out → 13:In6; 11:Out → 13:In7; 12:Out → 13:In8 |
| `sts_bls_ina_02_ow.questphase / h543 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#ina_02_pete_found"}}}` | 56:Out → 57:In; 57:Out → 94:In2 |
| `sts_bls_ina_02_ow.questphase / h543 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_spared","value":1,"comparisonType":"GreaterOrEqual"}}}` | 59:Out → 61:In; 61:Out → 63:In2 |
| `sts_bls_ina_02_ow.questphase / h543 / 63` | `questLogicalXorNodeDefinition` `{}` | 61:Out → 63:In2; 139:Out → 63:In1; 63:Out1 → 146:In |
| `sts_bls_ina_02_ow.questphase / h543 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_leave_workshop"}}` | 66:Out → 64:In; 117:Out → 64:In; 64:Out → 65:Succeeded |
| `sts_bls_ina_02_ow.questphase / h543 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_area_upper_floor"}}` | 151:Out → 68:In; 152:Out → 68:In; 150:Out → 68:In; 68:Out → 135:In1 |
| `sts_bls_ina_02_ow.questphase / h543 / 79` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_test_def"}}}` | 79:True → 149:Active; 79:False → 150:Active |
| `sts_bls_ina_02_ow.questphase / h543 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ina_02_dvc_old_camera_002","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsQuestTargetSpotted"}}}` | 93:Out → 92:In; 92:Out → 94:In1 |
| `sts_bls_ina_02_ow.questphase / h543 / 94` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 57:Out → 94:In2; 94:Out1 → 58:Succeeded; 92:Out → 94:In1; 133:Out → 94:In3 |
| `sts_bls_ina_02_ow.questphase / h543 / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 121:CutSource → 109:CutDestination; 119:Out1 → 109:In; 109:Out → 110:In |
| `sts_bls_ina_02_ow.questphase / h543 / 110` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 109:Out → 110:In; 110:True → 111:Inactive; 110:False → 112:In |
| `sts_bls_ina_02_ow.questphase / h543 / 112` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 110:False → 112:In; 111:Out → 112:In; 112:True → 113:Inactive; 112:False → 114:Succeeded |
| `sts_bls_ina_02_ow.questphase / h543 / 116` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_leave_workshop"}}` | 114:Out → 116:In; 116:True → 117:Active; 116:False → 147:In |
| `sts_bls_ina_02_ow.questphase / h543 / 118` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ina_02_dvc_old_camera_002","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsQuestTargetSpotted"}}}` | 119:Out1 → 118:In; 118:Out → 121:In |
| `sts_bls_ina_02_ow.questphase / h543 / 121` | `questCutControlNodeDefinition` `{}` | 121:CutSource → 109:CutDestination; 118:Out → 121:In |
| `sts_bls_ina_02_ow.questphase / h543 / 130` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 130:False → 95:Active; 130:True → 129:Start 0; 153:False → 130:In |
| `sts_bls_ina_02_ow.questphase / h543 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"onScreenTest":true}}}` | 56:Out → 133:In; 133:Out → 94:In3 |
| `sts_bls_ina_02_ow.questphase / h543 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_area_ground_floor"}}` | 151:Out → 134:In; 152:Out → 134:In; 150:Out → 134:In; 134:Out → 135:In2 |
| `sts_bls_ina_02_ow.questphase / h543 / 135` | `questLogicalXorNodeDefinition` `{}` | 68:Out → 135:In1; 135:Out1 → 72:Succeeded; 134:Out → 135:In2 |
| `sts_bls_ina_02_ow.questphase / h543 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 139:Out → 63:In1; 140:Out → 139:In |
| `sts_bls_ina_02_ow.questphase / h543 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_content_lock"}}` | 141:Out → 125:In; 142:Out → 141:In |
| `sts_bls_ina_02_ow.questphase / h543 / 143` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_content_lock"}}` | 143:Out → 126:In; 144:Out → 143:In |
| `sts_bls_ina_02_ow.questphase / h543 / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_02\\scenes\\sts_bls_ina_02_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 145:Out → 1:In; 128:Out → 145:In |
| `sts_bls_ina_02_ow.questphase / h543 / 153` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 153:In; 153:True → 95:Active; 153:False → 130:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_away"}}` | 94:Out → 2:In; 2:Out → 50:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_away"}}` | 96:Out → 34:In; 34:Out → 51:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 85` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_impossible_fact"}}}` | 85:False → 69:In; 85:True → 73:In; 82:Out → 85:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 96:Out → 34:In; 95:Out → 96:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_02\\scenes\\sts_bls_ina_02_holocall_debriefs.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 101:Out → 1:In; 18:Out → 101:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 102:Out → 103:In; 103:Out → 108:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 108` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 108:False → 84:Start 0; 103:Out → 108:In; 108:True → 109:In |
| `sts_bls_ina_02_ow.questphase / h1017 / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_dead"}}}` | 84:rejected_out → 109:In; 108:True → 109:In; 109:True → 110:Active; 109:False → 111:Active |
| `sts_bls_ina_02_ow.questphase / h1017 / 114` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 114:False → 22:In; 113:Out → 114:In; 114:True → 115:In |
| `sts_bls_ina_02_ow.questphase / h1425 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 25:Out → 13:In; 13:Out → 15:In |
| `sts_bls_ina_02_ow.questphase / h1425 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 25:Out → 13:In; 66:Out → 25:In |
| `sts_bls_ina_02_ow.questphase / h1425 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 72:Out → 28:In; 73:Out → 72:In |
| `sts_bls_ina_02_big_pete_scene.scene / scene / 155` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_01_done"}}}` | 17:0:0 → 155:0:1; 155:0:0 → 164:0:0; 155:0:1 → 160:0:0 |
| `sts_bls_ina_02_big_pete_scene.scene / scene / 302` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_02\\scenes\\sts_bls_ina_02_big_pete_scene.scene","Flags":"Soft"},"sectionName":"sts_bls_ina_02_no_money","type":"IsOutside"}}}` | 21:0:3 → 302:0:1; 302:0:0 → 176:0:0 |
| `sts_bls_ina_02_big_pete_scene.scene / scene / 336` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 1:0:0 → 336:0:1; 336:0:0 → 334:0:0 |
| `sts_bls_ina_02_big_pete_scene.scene / scene / 353` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"timeInterval":0.10000000149011612}}}` | 1:0:0 → 353:0:1; 353:0:0 → 105:0:1 |
| `sts_bls_ina_02_big_pete_scene.scene / scene / 409` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#ina_02_combat_triggered"}}}` | 1:0:0 → 409:0:1; 409:0:0 → 9:0:0; 409:0:1 → 9:0:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 71` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_dead"}}}` | 71:0:0 → 66:0:0; 71:0:1 → 74:0:0; 96:0:0 → 71:0:1 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 94` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_end_done"}}}` | 94:0:0 → 95:0:1; 99:0:0 → 94:0:1 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_done"}}}` | 92:666:0 → 249:0:1; 249:0:0 → 271:0:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 92:666:0 → 253:0:1; 253:0:0 → 256:0:1; 265:0:0 → 253:0:1; 271:1:0 → 253:0:0; 271:1:0 → 253:1026:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 253:0:0 → 256:0:1; 256:0:0 → 259:0:1; 271:1:0 → 256:0:0; 271:1:0 → 256:1026:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 256:0:0 → 259:0:1; 259:0:0 → 262:0:1; 271:1:0 → 259:0:0; 271:1:0 → 259:1026:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 262` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 259:0:0 → 262:0:1; 262:0:0 → 267:0:1; 262:0:1 → 265:0:0 |
| `sts_bls_ina_02_holocall_debriefs.scene / scene / 282` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_rejected"}}}` | 98:0:0 → 282:0:1; 282:0:0 → 284:0:1 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_end_done"}}}` | 78:0:0 → 79:0:1; 83:0:0 → 78:0:1 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 262` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_rejected"}}}` | 82:0:0 → 262:0:1; 262:0:0 → 266:0:1 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_done"}}}` | 76:666:0 → 273:0:1; 273:0:0 → 281:0:0 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 76:666:0 → 284:0:1; 281:1:0 → 284:0:0; 284:0:0 → 297:0:1 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 297` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 284:0:0 → 297:0:1; 297:0:0 → 292:0:1; 297:0:1 → 302:0:1; 302:0:0 → 297:0:1 |
| `sts_bls_ina_02_holocall_prebrief.scene / scene / 302` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 281:1:0 → 302:0:0; 297:0:1 → 302:0:1; 302:0:0 → 297:0:1 |
| `sts_bls_inland_avenue.questphase / h18378 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#ina_02_pete_found"}}}` | 56:Out → 57:In; 57:Out → 94:In2 |
| `sts_bls_inland_avenue.questphase / h18378 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_big_pete_spared","value":1,"comparisonType":"GreaterOrEqual"}}}` | 59:Out → 61:In; 61:Out → 63:In2 |
| `sts_bls_inland_avenue.questphase / h18378 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_02_tr_leave_workshop"}}` | 66:Out → 64:In; 117:Out → 64:In; 64:Out → 65:Succeeded |
| `sts_bls_inland_avenue.questphase / h18378 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_area_upper_floor"}}` | 151:Out → 68:In; 152:Out → 68:In; 150:Out → 68:In; 68:Out → 135:In1 |
| `sts_bls_inland_avenue.questphase / h18378 / 79` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_test_def"}}}` | 79:True → 149:Active; 79:False → 150:Active |
| `sts_bls_inland_avenue.questphase / h18378 / 94` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 57:Out → 94:In2; 94:Out1 → 58:Succeeded; 92:Out → 94:In1; 133:Out → 94:In3 |
| `sts_bls_inland_avenue.questphase / h18378 / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 121:CutSource → 109:CutDestination; 119:Out1 → 109:In; 109:Out → 110:In |
| `sts_bls_inland_avenue.questphase / h18378 / 110` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 109:Out → 110:In; 110:True → 111:Inactive; 110:False → 112:In |
| `sts_bls_inland_avenue.questphase / h18378 / 112` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 110:False → 112:In; 111:Out → 112:In; 112:True → 113:Inactive; 112:False → 114:Succeeded |
| `sts_bls_inland_avenue.questphase / h18378 / 116` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_leave_workshop"}}` | 114:Out → 116:In; 116:True → 117:Active; 116:False → 147:In |
| `sts_bls_inland_avenue.questphase / h18378 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_02_com_big_pete","names":["big_pete"]},"onScreenTest":true}}}` | 56:Out → 133:In; 133:Out → 94:In3 |
| `sts_bls_inland_avenue.questphase / h18378 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_02_tr_area_ground_floor"}}` | 151:Out → 134:In; 152:Out → 134:In; 150:Out → 134:In; 134:Out → 135:In2 |
| `sts_bls_inland_avenue.questphase / h18378 / 135` | `questLogicalXorNodeDefinition` `{}` | 68:Out → 135:In1; 135:Out1 → 72:Succeeded; 134:Out → 135:In2 |
| `sts_badlands.questphase / h11 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_02","fileEntryIndex":4,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 2:In; 2:Out → 12:In1 |
| `sts_badlands.questphase / h11 / 12` | `questLogicalXorNodeDefinition` `{"inputSocketCount":9}` | 2:Out → 12:In1; 3:Out → 12:In2; 4:Out → 12:In3; 5:Out → 12:In4; 6:Out → 12:In5; 7:Out → 12:In7; 8:Out → 12:In6; 9:Out → 12:In8; 10:Out → 12:In9; 12:Out1 → 13:In |
| `open_world_bugfixing.questphase / h1543 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_finished"}}}` | 0:Out → 7:In; 7:True → 8:Succeeded |
| `open_world_bugfixing.questphase / h2679 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_02_finished"}}}` | 0:Out → 7:In; 7:True → 8:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_bls_ina_02_big_pete_scene.scene / scene / 336; sts_bls_ina_02_bugfixing.questphase / h111 / 7; sts_bls_ina_02_ow.questphase / h1425 / 13; sts_bls_ina_02_ow.questphase / h1425 / 25 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sts_bls_ina_02_big_pete_scene.scene / scene / 392 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sts_bls_ina_02_ow.questphase / h0 / 180; sts_bls_ina_02_ow.questphase / h0 / 182 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_bls_ina_02_big_pete_scene.scene / scene / 21 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | sts_bls_ina_02_ow.questphase / h11 / 42 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_bls_ina_02_big_pete_scene.scene / scene / 380; sts_bls_ina_02_big_pete_scene.scene / scene / 402; sts_bls_ina_02_ow.questphase / h1017 / 50; sts_bls_ina_02_ow.questphase / h1017 / 51; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1543 / 7; open_world_bugfixing.questphase / h2679 / 7; sts_bls_ina_02_big_pete_scene.scene / scene / 155; sts_bls_ina_02_big_pete_scene.scene / scene / 21; +36 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_bls_ina_02_bugfixing.questphase / h177 / 9; sts_bls_ina_02_ow.questphase / h1017 / 21; sts_bls_ina_02_ow.questphase / h1017 / 83; sts_bls_ina_02_ow.questphase / h1017 / 98; +3 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_bls_ina_02_bugfixing.questphase / h14 / 5; sts_bls_ina_02_bugfixing.questphase / h14 / 6; sts_bls_ina_02_bugfixing.questphase / h14 / 7; sts_bls_ina_02_ow.questphase / h1017 / 80; +6 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_bls_ina_02_bugfixing.questphase / h223 / 8; sts_bls_ina_02_ow.questphase / h1017 / 104; sts_bls_ina_02_ow.questphase / h1017 / 105; sts_bls_ina_02_ow.questphase / h1017 / 106; +41 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_bls_ina_02_bugfixing.questphase / h14 / 3; sts_bls_ina_02_ow.questphase / h11 / 112; sts_bls_ina_02_ow.questphase / h543 / 118; sts_bls_ina_02_ow.questphase / h543 / 92 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_bls_ina_02_ow.questphase / h1017 / 96 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1543 / 8; open_world_bugfixing.questphase / h2679 / 8; sts_bls_ina_02_ow.questphase / h0 / 184; sts_bls_ina_02_ow.questphase / h1017 / 110; +37 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_bls_ina_02_bugfixing.questphase / h14 / 4; sts_bls_ina_02_ow.questphase / h11 / 97 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_bls_ina_02_big_pete_scene.scene / scene / 105; sts_bls_ina_02_big_pete_scene.scene / scene / 220; sts_bls_ina_02_big_pete_scene.scene / scene / 26; sts_bls_ina_02_big_pete_scene.scene / scene / 281; +37 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_badlands.questphase / h11 / 12; sts_bls_ina_02_ow.questphase / h11 / 23; sts_bls_ina_02_ow.questphase / h273 / 13; sts_bls_ina_02_ow.questphase / h543 / 135; +4 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_bls_ina_02_holocall_debriefs.scene / scene / 253; sts_bls_ina_02_holocall_debriefs.scene / scene / 259; sts_bls_ina_02_holocall_prebrief.scene / scene / 284; sts_bls_ina_02_holocall_prebrief.scene / scene / 302; +4 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_bls_ina_02_ow.questphase / h11 / 8; sts_bls_ina_02_ow.questphase / h543 / 121 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_bls_ina_02_big_pete_scene.scene / scene / 185; sts_bls_ina_02_ow.questphase / h1017 / 23 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_bls_ina_02_ow.questphase / h1017 / 84; sts_bls_ina_02_ow.questphase / h11 / 2; sts_bls_ina_02_ow.questphase / h543 / 129 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_bls_ina_02_bugfixing.questphase / h177 / 11; sts_bls_ina_02_ow.questphase / h1017 / 2; sts_bls_ina_02_ow.questphase / h1017 / 34; sts_bls_ina_02_ow.questphase / h11 / 68; +30 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_bls_ina_02_bugfixing.questphase / h111 / 5; sts_bls_ina_02_bugfixing.questphase / h14 / 2; sts_bls_ina_02_ow.questphase / h2 / 19; sts_bls_ina_02_ow.questphase / h543 / 109; +2 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sts_bls_ina_02_ow.questphase / h1017 / 107; sts_bls_ina_02_ow.questphase / h1425 / 75 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weighted_branch` | sts_bls_ina_02_ow.questphase / h11 / 73 | ordered output weights + explicit route bindings → one authored weighted output. Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates. |
| `workspot_performance` | sts_bls_ina_02_big_pete_scene.scene / scene / 339; sts_bls_ina_02_big_pete_scene.scene / scene / 341; sts_bls_ina_02_big_pete_scene.scene / scene / 346; sts_bls_ina_02_big_pete_scene.scene / scene / 359; +8 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_bls_ina_02_ow.questphase / h1017 / 89; sts_bls_ina_02_ow.questphase / h273 / 2; sts_bls_ina_02_ow.questphase / h273 / 4 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` | repair; journal anchor | `base-sts-bls-ina-02` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` | content candidate; journal anchor | `base-sts-bls-ina-02` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` | content candidate; forward dependency | `base-sts-bls-ina-02` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-bls-ina-02` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-bls-ina-02` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\badlands\sts_badlands.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-bls-ina-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-bls-ina-02.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

348 repeated typed/socket path signatures in this selected graph context; 45 distinct direct resource identities; 12 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 98 -> 282 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h1017 / 95 -> 96 -> 34 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 97 -> 99 -> 94 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene` / scene / 77 -> 80 -> 45 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 66 -> 97 -> 99 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h133 / 0 -> 5 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 280 -> 98 -> 282 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `6497920d6ce0ac894daa` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h1017 / 113 -> 114 -> 115 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 38 -> 280 -> 98 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h14 / 0 -> 8 -> 9 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 249 -> 271 -> 253 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h0 / 6 | `h14` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h0 / 10 | `h111` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h0 / 13 | `h177` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h0 / 17 | `h223` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h0 / 22 | `h304` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h0 / 71 | `h2` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h2 / 12 | `h11` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h11 / 58 | `h133` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h11 / 81 | `h273` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h0 / 72 | `h543` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h0 / 73 | `h1017` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h0 / 88 | `h1425` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.gamedef` | content candidate | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.quest |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02_testing.gamedef` | content candidate | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.quest |
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
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_up__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__stand_table_lean0__2h_on_keyboard__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q110\q110_08a_agent\q110_08a_agent__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\lipsync\en\sts_bls_ina_02_big_pete_scene\gang_tcl_m_06_jap_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\lipsync\en\sts_bls_ina_02_big_pete_scene\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\lipsync\en\sts_bls_ina_02_holocall_debriefs\dakota_smith.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\lipsync\en\sts_bls_ina_02_holocall_prebrief\dakota_smith.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\phases\sts_bls_ina_05_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\phases\sts_bls_ina_05_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\sts_bls_ina_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\generic__stand_ground__afraid__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__06.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\table\generic__stand_table_lean_front_keyboard__type__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `#ina_02_combat_triggered` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h10410 / 31; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase / h29 / 31; 2 total source locations in compressed evidence |
| `bls_achievement` | base\open_world\bugfixing\fixers\dakota_bugfixing.questphase / h22 / 61; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 3; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 5; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 7; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_dakota_calls_v_end_activate` | base\open_world\fixers\dakota\phases\dakota.questphase / h0 / 63; base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 295; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 346; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1123 / 27; 57 total source locations in compressed evidence |
| `holo_dakota_calls_v_end_done` | base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 291; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 83; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 42; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 555; 21 total source locations in compressed evidence |
| `holo_dakota_calls_v_rejectable` | base\quest\holocalls\dakota\dakota_holocall.scene / scene / 634; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene / scene / 282; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene / scene / 254; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene / scene / 283; 25 total source locations in compressed evidence |
| `holo_dakota_calls_v_rejected` | base\quest\holocalls\dakota\dakota_holocall.scene / scene / 642; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene / scene / 286; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene / scene / 258; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_holocall_debriefs.scene / scene / 285; 17 total source locations in compressed evidence |
| `holo_dakota_calls_v_start_activate` | base\open_world\fixers\dakota\phases\dakota.questphase / h0 / 62; base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 294; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 345; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1123 / 26; 74 total source locations in compressed evidence |
| `holo_dakota_calls_v_start_done` | base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 289; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 82; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 41; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 580; 21 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `ina_02_after_holocall` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h18852 / 113; 1 total source locations in compressed evidence |
| `ina_02_big_pete_dead` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h17837 / 14; 1 total source locations in compressed evidence |
| `ina_02_gang_retaliation` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h10410 / 52; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase / h29 / 52; 2 total source locations in compressed evidence |
| `ina_02_pete_afraid` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h17968 / 7; 1 total source locations in compressed evidence |
| `ina_02_post_community` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h18852 / 18; 1 total source locations in compressed evidence |
| `ina_02_ready` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h19260 / 15; 1 total source locations in compressed evidence |
| `ina_02_start` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h19260 / 28; 1 total source locations in compressed evidence |
| `ina_02_test_def` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.quest / h0 / 16; 1 total source locations in compressed evidence |
| `kab_01_done` | base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\phases\sts_wat_kab_01_openworld.questphase / h214 / 58; base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\phases\sts_wat_kab_01_openworld.questphase / h214 / 111; 2 total source locations in compressed evidence |
| `sts_bls_ina_tier_2` | base\open_world\fixers\dakota\phases\dakota.questphase / h0 / 5; 1 total source locations in compressed evidence |
| `sts_wraiths_retaliation` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h15287 / 54; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h18852 / 115; base\open_world\street_stories\street_stories_gang_retaliation.questphase / h23 / 23; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase / h763 / 54; 4 total source locations in compressed evidence |

NodeRef uses: 214; TweakDB binding uses: 13. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` | 10 / 63 | scnChangeIdleAnimEvent: 2; scnDialogLineEvent: 20; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 3; scnPlaySkAnimEvent: 10; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 21; scneventsVFXEvent: 2 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` | 2 / 4 | scnDialogLineEvent: 4 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
