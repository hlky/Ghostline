# Through Pain to Heaven

Journal: `ep1/quests/main_quest/q306_reed_epilogue` · `MainQuest` · hash `172105197`.

Journal premise: Silence... Finally. Every time I think back to that first meeting with Songbird, I feel like I'm gonna blow chunks. The moment she made me fade out... A feeling worse than death. Believe me, I'm an expert on the subject. But now? Nothing. Not a peep. Not even an echo. As if she's far, far away, or... I dunno. Looks like it's just the two of us again. But for how long now, I wonder.

**Coverage: journal-linked.** 38 exact journal-linked nodes in 6 resources; 12 resources in the inspected dependency context.

Resource roles in that context: 12 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Reed's message. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/0000_read_reed` |
| Reply to Reed's message. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/000_answer_reeds_message` |
| Find something to do until Reed contacts you. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` |
| Answer the holocall. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/01_answer_phone` |
| Talk to Reed. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/02_talk_to_reed` |
| Meet Reed at the CHOOH2 station. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03_meet_reed` |
| Wait for Reed. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03a_wait_for_reed` |
| Talk to Reed. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/04_talk_to_reed` |
| Talk to Johnny. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny` |
|  (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/06_decrypt_shard` |
| Read Reed's message. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_00_read` |
| Reply to Reed's message. (Primary) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_01_respond` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 168` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue` | 185:Out → 168:Failed; 168:Out → 186:In |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 3` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/000_answer_reeds_message` | 51:Out → 3:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 32` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/000_answer_reeds_message` | 29:Out → 32:Succeeded; 32:Out → 46:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 44` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/000_answer_reeds_message` | 43:Out → 44:Succeeded; 44:Out → 52:Succeeded |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 46` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` | 32:Out → 46:Active; 46:Out → 45:In |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 48` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/description` | 48:Out → 2:Active; 49:Out → 48:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 49` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/0000_read_reed` | 24:Out → 49:Active; 49:Out → 48:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 51` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/0000_read_reed` | 51:Out → 3:Active; 50:Out → 51:Succeeded |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 52` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue` | 52:Out → 33:In; 44:Out → 52:Succeeded |
| `q306_06_epilogues.questphase / h0 / 58` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/02_talk_to_reed` | 57:End 0 → 58:Succeeded; 58:Out → 59:Active |
| `q306_06_epilogues.questphase / h0 / 59` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03_meet_reed` | 59:Out → 55:In1; 58:Out → 59:Active; 59:Out → 64:In |
| `q306_06_epilogues.questphase / h0 / 190` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue` | 55:Out1 → 190:Succeeded; 190:Out → 162:In |
| `q306_06_epilogues.questphase / h0 / 191` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue` | 191:Out → 187:In |
| `q306_06_epilogues.questphase / h0 / 229` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` | 150:Out1 → 229:Active; 229:Out → 232:Active |
| `q306_06_epilogues.questphase / h0 / 232` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/description` | 232:Out → 176:In; 229:Out → 232:Active |
| `q306_06_epilogues.questphase / h709 / 41` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_01_respond` | 40:Out → 41:Succeeded; 41:Out → 55:Active |
| `q306_06_epilogues.questphase / h709 / 53` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_01_respond` | 52:Out → 53:Succeeded; 53:Out → 75:Succeeded |
| `q306_06_epilogues.questphase / h709 / 55` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` | 41:Out → 55:Active; 55:Out → 54:In |
| `q306_06_epilogues.questphase / h709 / 61` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/description` | 62:Out → 61:Active; 61:Out → 63:Active |
| `q306_06_epilogues.questphase / h709 / 62` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_00_read` | 62:Out → 61:Active; 76:Out → 62:Active |
| `q306_06_epilogues.questphase / h709 / 64` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_01_respond` | 71:Out → 64:Active |
| `q306_06_epilogues.questphase / h709 / 71` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/no_deal_00_read` | 71:Out → 64:Active; 70:Out → 71:Succeeded |
| `q306_06_epilogues.questphase / h709 / 75` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue` | 75:Out → 42:In; 53:Out → 75:Succeeded |
| `q306_06_epilogues.questphase / h709 / 76` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue` | 39:Out → 76:Active; 76:Out → 62:Active |
| `q306_epilogue_reed.questphase / h0 / 41` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03_meet_reed` | 46:True → 41:Inactive; 41:Out → 42:Active |
| `q306_epilogue_reed.questphase / h0 / 42` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03a_wait_for_reed` | 41:Out → 42:Active; 42:Out → 68:intro_wait |
| `q306_epilogue_reed.questphase / h0 / 43` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03a_wait_for_reed` | 68:intro_wait_out → 43:Succeeded; 43:Out → 44:Active |
| `q306_epilogue_reed.questphase / h0 / 44` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/04_talk_to_reed` | 43:Out → 44:Active |
| `q306_epilogue_reed.questphase / h148 / 9` (PauseCondition) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny` | 0:Out → 9:In; 9:Out → 10:In |
| `q306_12b_holo_reed_call.scene / scene / 13` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/02_talk_to_reed` | 13:0:0 → 159:0:1; 106:0:0 → 13:0:1; 155:0:1 → 13:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_12b_holo_reed_call.scene / scene / 106` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` | 106:0:0 → 13:0:1; 155:0:0 → 106:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_12b_holo_reed_call.scene / scene / 155` (Condition) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed` | 81:0:0 → 155:0:1; 155:0:0 → 106:0:3; 155:0:1 → 13:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `q306_12b_holo_reed_call.scene / scene / 159` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/description` | 13:0:0 → 159:0:1; 159:0:0 → 112:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_13b_epilogue_reed.scene / scene / 158` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/03_meet_reed` | 7:0:0 → 158:0:3; 158:0:0 → 159:0:1; 158:0:0 → 1489:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_13b_epilogue_reed.scene / scene / 159` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/04_talk_to_reed` | 158:0:0 → 159:0:1; 159:0:0 → 811:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_13b_epilogue_reed.scene / scene / 164` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/04_talk_to_reed` | 164:0:0 → 851:0:1; 510:0:0 → 164:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_13b_epilogue_reed.scene / scene / 851` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny` | 164:0:0 → 851:0:1; 851:0:0 → 982:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q306_13b_epilogue_reed.scene / scene / 1261` (Journal) | `ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny` | 857:0:0 → 1261:0:3; 1261:0:0 → 2:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `q306_06_epilogues.questphase / h0 / 15` | `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene`; `#q306_12_sm_holo_alex_call` | 221:True → 15:Start 0; 257:Out → 15:Start 0; 15:End 0 → 24:Succeeded; 15:End 0 → 130:In1; 15:End 0 → 228:In; 15:End 0 → 256:In; 15:Holocall INT → 96:In; 15:Holocall RET → 95:In |
| `q306_06_epilogues.questphase / h0 / 37` | `ep1\quest\main_quests\q306\test\q306_00_chickentest.scene`; `#q306_00_sm_chickentest` | 39:True → 37:Teleport; 37:Yes → 38:In |
| `q306_06_epilogues.questphase / h0 / 53` | `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` | 25:Out → 53:In1; 53:Out1 → 26:Succeeded |
| `q306_06_epilogues.questphase / h0 / 55` | `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` | 59:Out → 55:In1; 55:Out1 → 190:Succeeded |
| `q306_06_epilogues.questphase / h0 / 57` | `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene`; `#q306_12b_sm_holo_reed_call` | 220:True → 57:Start 0; 259:Out → 57:Start 0; 57:End 0 → 58:Succeeded; 57:End 0 → 231:In; 57:End 0 → 261:In; 57:Holocall INT → 90:In; 57:Holocall RET → 89:In |
| `q306_06_epilogues.questphase / h0 / 62` | `ep1\quest\main_quests\q306\test\q306_00_chickentest.scene`; `#q306_00_sm_chickentest` | 64:True → 62:Teleport; 62:Yes → 63:In |
| `q306_06_epilogues.questphase / h0 / 103` | `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene`; `#q306_12a_sm_mission_aftermath` | 105:Out → 103:q306_somi_wrap_in; 103:q306_somi_wrap_out → 149:In1; 103:q306_somi_wrap_out → 160:In; 133:Out1 → 103:Prefetch |
| `q306_06_epilogues.questphase / h0 / 106` | `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene`; `#q306_12a_sm_mission_aftermath` | 104:Out → 106:q306_reed_wrap_in; 106:q306_reed_wrap_out → 148:In2; 106:q306_reed_wrap_out → 160:In; 133:Out1 → 106:Prefetch |
| `q306_06_epilogues.questphase / h0 / 130` | `ep1\quest\main_quests\q306\phases\messages\q306_msg_alex_meeting_reminder.questphase` | 15:End 0 → 130:In1 |
| `q306_06_epilogues.questphase / h0 / 142` | `ep1\quest\main_quests\q306\phases\messages\q306_msg_reed_launchpad_retreated_scenario.questphase` | 141:True → 142:In1; 142:Out1 → 150:In2; 142:Refused_Out → 241:In1 |
| `q306_epilogue_alex.questphase / h0 / 3` | `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene`; `#q306_13_sm_epilogue` | 3:End 0 → 1:In; 15:Out → 3:Start0; 48:Out1 → 3:Start0 |
| `q306_epilogue_alex.questphase / h0 / 5` | `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene`; `#q306_sm_tv_bit` | 30:Out → 5:Start 0; 5:End 0 → 31:In |
| `q306_epilogue_alex.questphase / h0 / 25` | `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene`; `#q306_13_sm_epilogue` | 26:Out → 25:tv_start |
| `q306_epilogue_alex.questphase / h0 / 47` | `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene`; `#q306_13_sm_epilogue` | 36:Out → 47:intro_wait; 47:intro_wait_out → 37:Succeeded; 47:intro_wait_out → 48:In1 |
| `q306_epilogue_reed.questphase / h0 / 2` | `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene`; `#q306_13b_sm_epilogue_reed` | 31:Out → 2:Start 0; 2:End 0 → 37:In; 2:End 0 → 10:In1; 2:reed_leave_out → 23:In |
| `q306_epilogue_reed.questphase / h0 / 68` | `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene`; `#q306_13b_sm_epilogue_reed` | 42:Out → 68:intro_wait; 68:intro_wait_out → 43:Succeeded; 68:intro_wait_out → 70:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.questphase` / h0 / 69 | `q115_00_hanako.questphase` | 62: Phase; 89: Input; 72: Input; 62:Out1 → 69:In1; 69:Out1 → 70:In1; 89:Out → 69:In2; 72:Out → 69:In3 |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 130 | `q306_msg_alex_meeting_reminder.questphase` | 15: Scene: q306_12_holo_alex_call.scene; 15:End 0 → 130:In1 |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 142 | `q306_msg_reed_launchpad_retreated_scenario.questphase` | 141: Condition: q306_launchpad_retreated_scenario; 141:True → 142:In1; 142:Out1 → 150:In2; 142:Refused_Out → 241:In1 |
| `ep1\quest\main_quests\q306\q306.questphase` / h0 / 66 | `q306_06_epilogues.questphase` | 65: Phase: q306_05_launchpad.questphase; 65: Phase: q306_05_launchpad.questphase; 65: Phase: q306_05_launchpad.questphase; 125: LogicalHub; 73: Phase: q306_endingb_debug_setup.questphase; 94: Phase; 66:Out1 → 19:In1; 65:Prefetch → 66:Prefetch_In; 65:SomiReturned → 66:SomiReturned; 65:ReedDead → 66:ReedDead; 125:Out1 → 66:Moth_Scene_In; 73:Out1 → 66:ReedDead; 94:Out1 → 66:SomiReturned; 66:point_of_no_return_out → 126:In1 |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 53 | `q306_epilogue_alex.questphase` | 25: Journal; 25:Out → 53:In1; 53:Out1 → 26:Succeeded |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 55 | `q306_epilogue_reed.questphase` | 59: Journal; 59:Out → 55:In1; 55:Out1 → 190:Succeeded |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 15 | `q306_12_holo_alex_call.scene` | 221: Condition: q306_DEBUG_debugModeOn; 257: GameManager; 221:True → 15:Start 0; 257:Out → 15:Start 0; 15:End 0 → 24:Succeeded; 15:End 0 → 130:In1; 15:End 0 → 228:In; 15:End 0 → 256:In; 15:Holocall INT → 96:In; 15:Holocall RET → 95:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_a.questphase` / h0 / 2 | `q306_12_holo_alex_call.scene` | 0: Input; 0:Out → 2:Start 0; 2:End 0 → 4:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_b.questphase` / h0 / 5 | `q306_12_holo_alex_call.scene` | 0: Input; 0:Out → 5:Start 0; 5:End 0 → 7:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_c.questphase` / h0 / 3 | `q306_12_holo_alex_call.scene` | 0: Input; 0:Out → 3:Start 0; 3:End 0 → 5:In |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 103 | `q306_12a_mission_aftermath.scene` | 105: Checkpoint; 133: LogicalHub; 105:Out → 103:q306_somi_wrap_in; 103:q306_somi_wrap_out → 149:In1; 103:q306_somi_wrap_out → 160:In; 133:Out1 → 103:Prefetch |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 106 | `q306_12a_mission_aftermath.scene` | 104: Checkpoint; 133: LogicalHub; 104:Out → 106:q306_reed_wrap_in; 106:q306_reed_wrap_out → 148:In2; 106:q306_reed_wrap_out → 160:In; 133:Out1 → 106:Prefetch |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 57 | `q306_12b_holo_reed_call.scene` | 220: Condition: q306_DEBUG_debugModeOn; 259: GameManager; 220:True → 57:Start 0; 259:Out → 57:Start 0; 57:End 0 → 58:Succeeded; 57:End 0 → 231:In; 57:End 0 → 261:In; 57:Holocall INT → 90:In; 57:Holocall RET → 89:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_a.questphase` / h0 / 3 | `q306_13_epilogue.scene` | 4: PauseCondition; 3:End 0 → 1:In; 4:Out → 3:q306_13_ending_a |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_b.questphase` / h0 / 6 | `q306_13_epilogue.scene` | 7: PauseCondition; 7:Out → 6:q306_13_ending_b; 6:End 0 → 9:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_epilogue_c.questphase` / h0 / 4 | `q306_13_epilogue.scene` | 5: PauseCondition; 4:End 0 → 1:In; 5:Out → 4:q306_13_ending_c |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` / h0 / 3 | `q306_13_epilogue.scene` | 15: WorldDataManager; 48: LogicalHub; 3:End 0 → 1:In; 15:Out → 3:Start0; 48:Out1 → 3:Start0 |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` / h0 / 25 | `q306_13_epilogue.scene` | 26: PauseCondition: #q306_tr_epilogue_tv_in; 26:Out → 25:tv_start |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` / h0 / 47 | `q306_13_epilogue.scene` | 36: Journal; 36:Out → 47:intro_wait; 47:intro_wait_out → 37:Succeeded; 47:intro_wait_out → 48:In1 |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h0 / 2 | `q306_13b_epilogue_reed.scene` | 31: Vehicle; 31:Out → 2:Start 0; 2:End 0 → 37:In; 2:End 0 → 10:In1; 2:reed_leave_out → 23:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h0 / 68 | `q306_13b_epilogue_reed.scene` | 42: Journal; 42:Out → 68:intro_wait; 68:intro_wait_out → 43:Succeeded; 68:intro_wait_out → 70:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` / h0 / 5 | `q306_tv_bit.scene` | 30: WorldDataManager; 30:Out → 5:Start 0; 5:End 0 → 31:In |
| `base\quest\main_quests\part1\act_1.questphase` / h329 / 4 | `q115_afterlife.questphase` | 0: Input; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 0:Out → 4:In; 4:Out1 → 1:In; 9:Out1 → 4:In; 9:OutRestaurant → 4:InRestaurant; 9:OutElevator → 4:InElevator; 9:OutRipperdoc → 4:InRipperdoc; 4:q114_out → 5:In; 9:OutPills → 4:InPills; 4:q113_out → 6:In; 9:OutRipperRoof → 4:InRipperdocRoof; 4:death_out → 7:In; 9:OutQ114 → 4:InQ114; 4:mikoshi_out → 8:In; 9:OutQ113 → 4:InQ113; 9:OutSolo → 4:InSolo; 9:OutAfterlife → 4:InAfterlife; 9:OutAfterRogue → 4:InAfterSex; 9:OutBeforeAlt → 4:InBeforeAlt; 9:OutAfterAlt → 4:InAfterlifePlan; 9:OutAV → 4:InAfterlifeAV; 9:OutJungle → 4:InJungle; 9:OutAtrium → 4:InAtrium; 9:OutNetrunner → 4:InNetrunner |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 5 | `q115_afterlife.questphase` | 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91:Out1 → 5:In; 5:Out1 → 73:In1; 91:OutRestaurant → 5:InRestaurant; 91:OutElevator → 5:InElevator; 91:OutRipperdoc → 5:InRipperdoc; 5:q114_out → 92:In1; 91:OutPills → 5:InPills; 5:q113_out → 115:In1; 91:OutRipperRoof → 5:InRipperdocRoof; 5:death_out → 116:In1; 91:OutQ114 → 5:InQ114; 5:mikoshi_out → 73:cyberspace_in; 91:OutQ113 → 5:InQ113; 91:OutSolo → 5:InSolo; 91:OutAfterlife → 5:InAfterlife; 91:OutAfterRogue → 5:InAfterSex; 91:OutBeforeAlt → 5:InBeforeAlt; 91:OutAfterAlt → 5:InAfterlifePlan; 91:OutAV → 5:InAfterlifeAV; 91:OutJungle → 5:InJungle; 91:OutAtrium → 5:InAtrium; 91:OutNetrunner → 5:InNetrunner |
| `ep1\quest\main_quests\ep1_main_quests.questphase` / h0 / 7 | `q306.questphase` | 18: Condition: q304_songbirds_path Less 1; 25: Input; 7:Point_of_no_return_out → 43:In1; 7:quest_end → 43:In2; 18:False → 7:00_start; 25:Out → 7:00_start |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 2 | `q306.questphase` | 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 2:quest_end → 1:In; 3:Meeting → 2:00_start; 3:Song → 2:Song; 3:Mid-ride → 2:Mid-ride; 3:Cosmodrome → 2:Cosmodrome; 3:Gate Passed → 2:Gate Passed; 3:Failstate → 2:Failstate; 3:Restricted → 2:Restricted; 3:Roof → 2:Roof; 3:Myers Arrival → 2:Myers Arrival; 3:Public Revisited → 2:Public Revisited; 3:Restricted Revisited → 2:Restricted Revisited; 3:Duty Free → 2:Duty Free; 3:Viewing Gallery → 2:Viewing Gallery; 3:Station Approach → 2:Station Approach; 3:Tower Defense → 2:Tower Defense; 3:Overdrive Scene → 2:Overdrive Scene; 3:Overdrive Gameplay → 2:Overdrive Gameplay; 3:Train → 2:Train; 3:Launchpad → 2:Launchpad; 3:REED dead, SOMI on moon → 2:REED dead, SOMI on moon; 3:REED takes SOMI → 2:REED leaves, SOMI returned; 3:CreditsTest_Out → 2:CreditsTest_In; 3:Reed Epilogue Postcontent → 2:Reed Epilogue Postcontent; 3:Somi Epilogue Postcontent → 2:Somi Epilogue Postcontent |
| `base\quest\cyberpunk2077.questphase` / h0 / 33 | `act_1.questphase` | 32: Phase: prologue.questphase; 82: Phase; 57: Phase; 57: Phase; 57: Phase; 98: Condition: ep1_active Less 1; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 102: PauseCondition: ep1_active GreaterOrEqual 1; 32:Out1 → 33:Q101; 82:CYB-656199_Out → 33:CYB-656199_In; 33:Q201 → 36:Q201; 33:Q202 → 36:Q202; 57:Q101 Out → 33:Q101; 33:Q203 → 36:Q203; 57:Q101 Vroom Out → 33:Q101 Vroom; 33:Q204 → 36:Q204; 57:Q103 Out → 33:Q103; 98:True → 33:Q103; 33:Q115 Final Boards → 91:In1; 57:Q104 Out → 33:Q104; 57:Q105 Out → 33:Q105; 57:Q108 Out → 33:Q108; 57:Q110 Out → 33:Q110; 57:Q112 Out → 33:Q112; 57:Q113 Out → 33:Q113; 57:Q114 Out → 33:Q114; 57:Q115 Out → 33:Q115; 57:Q116 Out → 33:Q116; 57:EP1_Standalone → 33:EP1_Standalone; 102:Out → 33:EP1_Standalone |
| `ep1\quest\ep1.questphase` / h0 / 9 | `ep1_main_quests.questphase` | 22: LogicalHub; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 19: Phase; 86: LogicalHub; 87: LogicalHub; 22:Out1 → 9:Base; 12:q301 → 9:q301; 12:q302 → 9:q302; 12:q303 → 9:q303; 12:q304 → 9:q304; 12:q305 → 9:q305; 12:q306 → 9:q306; 12:q307 → 9:q307; 19:Out1 → 9:Standalone; 86:Out1 → 9:CP77-64292_in; 87:Out1 → 9:CP77-65722_Out |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `q306_12_holo_alex_call.scene` | Start 0 → End 0 | Alex; V; 22 nodes / 24 edges |
| `q306_12a_mission_aftermath.scene` | q306_somi_wrap_in, q306_reed_wrap_in → q306_somi_wrap_out, End1, End2, q306_reed_wrap_out | Johnny; Player; 83 nodes / 95 edges |
| `q306_12b_holo_reed_call.scene` | Start 0 → End 0 | Reed; V; 22 nodes / 24 edges |
| `q306_13_epilogue.scene` | Start0, intro_wait, tv_start → End 0, intro_wait_out, tv_cut | Alex; TV_PERSON; Johnny; V; 207 nodes / 250 edges |
| `q306_13b_epilogue_reed.scene` | Start 0, intro_wait → End 0, intro_wait_out, End2, reed_leave_out | Reed; Johnny; Reed_Car; V; 148 nodes / 209 edges |
| `q306_tv_bit.scene` | Start 0 → End 0 | Journalist; Wawuda; chicken_journalist; chicken_wawuda; 67 nodes / 81 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `q306_12_holo_alex_call.scene / n7 / 0` | Glad you're reaching out. (`joy`) | No option-level predicate stored | 0:0 → 32:0:0 |
| `q306_12_holo_alex_call.scene / n7 / 1` | Didn't expect this, I guess. (`not_sure`) | No option-level predicate stored | 0:1 → 33:0:0 |
| `q306_12_holo_alex_call.scene / n7 / 2` | Just plain good to know you're alive. (`surprise`) | No option-level predicate stored | 0:2 → 95:0:0 |
| `q306_12_holo_alex_call.scene / n49 / 0` | See you there. (`see_you`) | No option-level predicate stored | 0:0 → 52:0:0 |
| `q306_12_holo_alex_call.scene / n49 / 1` | This invite from you or the FIA? (`discreet`) | No option-level predicate stored | 0:1 → 63:0:1 |
| `q306_12a_mission_aftermath.scene / n54 / 0` | We're still together, there's that… (`Me_First`) | No option-level predicate stored | 0:0 → 56:0:0 |
| `q306_12a_mission_aftermath.scene / n54 / 1` | Not about to lie down, give up. (`You_First`) | No option-level predicate stored | 0:1 → 58:0:0 |
| `q306_12a_mission_aftermath.scene / n54 / 2` | We'll see how this game plays out. (`Together`) | No option-level predicate stored | 0:2 → 68:0:0 |
| `q306_12a_mission_aftermath.scene / n84 / 0` | Feelin' sorry for yourself, more like… (`doomed`) | No option-level predicate stored | 0:0 → 86:0:0 |
| `q306_12a_mission_aftermath.scene / n84 / 1` | Forgettin' someone? Like me? (`friend`) | No option-level predicate stored | 0:1 → 88:0:0 |
| `q306_12a_mission_aftermath.scene / n203 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 204:0:0; 0:0 → 443:0:1; 0:0 → 522:0:3; 0:0 → 586:0:1 |
| `q306_12a_mission_aftermath.scene / n224 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 226:0:0; 0:0 → 462:0:0; 0:0 → 522:0:3 |
| `q306_12a_mission_aftermath.scene / n502 / 0` | Myers's got bigger problems than me. (`victim`) | No option-level predicate stored | 0:0 → 505:0:0 |
| `q306_12a_mission_aftermath.scene / n502 / 1` | Myers? Didn't give a lick about Reed. (`egal`) | No option-level predicate stored | 0:1 → 507:0:0 |
| `q306_12a_mission_aftermath.scene / n502 / 2` | Myers was after Song, cared about her exclusively. (`obsessed`) | No option-level predicate stored | 0:2 → 511:0:0 |
| `q306_12b_holo_reed_call.scene / n113 / 0` | Surgery – what's up with that? (`Deal`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q306_finale_deal_done", "value": 1, "comparisonType": "Equal"}}} | 0:0 → 115:0:0 |
| `q306_12b_holo_reed_call.scene / n113 / 1` | You all right? (`alright`) | No option-level predicate stored | 0:1 → 133:0:0 |
| `q306_12b_holo_reed_call.scene / n113 / 2` | Didn't expect to get this call, honestly. (`again`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q306_finale_deal_done", "value": 1, "comparisonType": "NotEqual"}}} | 0:2 → 114:0:0 |
| `q306_13_epilogue.scene / n34 / 0` | Had to come, of course. (`came`) | No option-level predicate stored | 0:0 → 197:0:0 |
| `q306_13_epilogue.scene / n34 / 1` | Was thinkin' of skippin'. (`didnt want`) | No option-level predicate stored | 0:1 → 198:0:0 |
| `q306_13_epilogue.scene / n339 / 0` | I killed him – had no choice. (`admit`) | No option-level predicate stored | 0:0 → 340:0:0 |
| `q306_13_epilogue.scene / n339 / 1` | Stubbornness killed him. (`lie1`) | No option-level predicate stored | 0:1 → 341:0:0 |
| `q306_13_epilogue.scene / n339 / 2` | Myers – she's responsible for his death. (`lie2`) | No option-level predicate stored | 0:2 → 342:0:0 |
| `q306_13_epilogue.scene / n365 / 0` | [Drink] To Reed. (`Go`) | No option-level predicate stored | 0:0 → 1461:0:0 |
| `q306_13_epilogue.scene / n365 / 1` | [Drink] To Jackie. (`Jackie`) | No option-level predicate stored | 0:1 → 372:0:0 |
| `q306_13_epilogue.scene / n365 / 2` | [Drink] To Johnny. (`Johnny`) | No option-level predicate stored | 0:2 → 370:0:0 |
| `q306_13_epilogue.scene / n365 / 3` | [Drink] To T-Bug. (`T-Bug`) | No option-level predicate stored | 0:3 → 368:0:0 |
| `q306_13_epilogue.scene / n365 / 4` | [Drink] To Evelyn. (`Evelyn`) | No option-level predicate stored | 0:4 → 500:0:0 |
| `q306_13_epilogue.scene / n365 / 5` | [Drink] To Takemura. (`Takemura`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q112_takemura_dead", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:5 → 411:0:0 |
| `q306_13_epilogue.scene / n365 / 6` | [Drink] To Scorpion. (`Scorpion`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq001_done", "value": 1, "comparisonType": "GreaterOrEqual"}}, "bluelineCondition": {"$type": "questCharacterCondition", "type": {"$type": "questCharacterLifePath_ConditionType", "lifePathID": "67091901544"}}} | 0:6 → 367:0:0 |
| `q306_13_epilogue.scene / n365 / 7` | Thanks, nothing for me. (`no_alcohol`) | No option-level predicate stored | 0:7 → 747:0:0 |
| `q306_13_epilogue.scene / n512 / 0` | So, within the FIA, was he liked, admired? (`not_sure`) | No option-level predicate stored | 0:0 → 516:0:0 |
| `q306_13_epilogue.scene / n512 / 1` | Gonna miss him? (`myers_too`) | No option-level predicate stored | 0:1 → 517:0:0 |
| `q306_13_epilogue.scene / n540 / 0` | I did. (`honor`) | No option-level predicate stored | 0:0 → 542:0:0 |
| `q306_13_epilogue.scene / n540 / 1` | No, can't say I did. (`and_you`) | No option-level predicate stored | 0:1 → 543:0:0 |
| `q306_13_epilogue.scene / n540 / 2` | Hard to say. (`dont_know`) | No option-level predicate stored | 0:2 → 763:0:0 |
| `q306_13_epilogue.scene / n608 / 0` | Many have tried. (`Try_me`) | No option-level predicate stored | 0:0 → 610:0:0 |
| `q306_13_epilogue.scene / n608 / 1` | Plan to kill me? (`no_fight`) | No option-level predicate stored | 0:1 → 611:0:0 |
| `q306_13_epilogue.scene / n608 / 2` | But you won't… (`sure_fight`) | No option-level predicate stored | 0:2 → 731:0:0 |
| `q306_13_epilogue.scene / n618 / 0` | Thanks, Alex. (`thank`) | No option-level predicate stored | 0:0 → 739:0:0 |
| `q306_13_epilogue.scene / n618 / 1` | Sounds pretty risky. (`Risk`) | No option-level predicate stored | 0:1 → 619:0:0 |
| `q306_13_epilogue.scene / n618 / 2` | Got the feeling you're not telling me everything… (`Why_Here`) | No option-level predicate stored | 0:2 → 620:0:0 |
| `q306_13_epilogue.scene / n618 / 3` | [Return token] Show 'em this as proof. (`coin`) | No option-level predicate stored | 0:3 → 1144:0:0 |
| `q306_13_epilogue.scene / n630 / 0` | What'll you do while you wait for me to die? (`safety`) | No option-level predicate stored | 0:0 → 680:0:1 |
| `q306_13_epilogue.scene / n630 / 1` | You should quit, get outta here. (`what_now`) | No option-level predicate stored | 0:1 → 681:0:1 |
| `q306_13_epilogue.scene / n630 / 2` | None too busy a day. (`no_jukebox`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q304_04e_heart_to_heart_done", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:2 → 1151:0:0 |
| `q306_13_epilogue.scene / n630 / 3` | Never thought I'd live to see the start of a fifth corp war. (`corpowar`) | {"bluelineCondition": {"$type": "questCharacterCondition", "type": {"$type": "questCharacterLifePath_ConditionType", "lifePathID": "83635443133"}}} | 0:3 → 787:0:1 |
| `q306_13_epilogue.scene / n750 / 0` | Died serving Myers. (`myers`) | No option-level predicate stored | 0:0 → 755:0:0 |
| `q306_13_epilogue.scene / n750 / 1` | He was out to save Song. (`so_mi`) | No option-level predicate stored | 0:1 → 752:0:0 |
| `q306_13_epilogue.scene / n750 / 2` | Died for both. (`both`) | No option-level predicate stored | 0:2 → 753:0:0 |
| `q306_13_epilogue.scene / n767 / 0` | [Drink] To those with principles. (`last_drink`) | No option-level predicate stored | 0:0 → 769:0:0 |
| `q306_13_epilogue.scene / n767 / 1` | [Do not drink] To those with principles. (`no_drink`) | No option-level predicate stored | 0:1 → 770:0:0 |
| `q306_13_epilogue.scene / n767 / 2` | [Do not drink] Principles are another excuse. (`deny`) | No option-level predicate stored | 0:2 → 788:0:0 |
| `q306_13_epilogue.scene / n867 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 423:0:0 |
| `q306_13_epilogue.scene / n890 / 0` | [Sit] (`sit`) | No option-level predicate stored | 0:0 → 469:0:3; 0:0 → 892:0:0 |
| `q306_13_epilogue.scene / n1457 / 0` | [Drink] To Reed – and I'm sorry. (`to reed`) | No option-level predicate stored | 0:0 → 1483:0:0 |
| `q306_13_epilogue.scene / n1457 / 1` | [Drink] To Reed – RIP, choom. (`to reed 2`) | No option-level predicate stored | 0:1 → 1465:0:0 |
| `q306_13_epilogue.scene / n1816 / 0` | [Wait] (`wait`) | No option-level predicate stored | 0:0 → 1818:0:0 |
| `q306_13b_epilogue_reed.scene / n12 / 0` | You in a hurry? (`bye`) | No option-level predicate stored | 0:0 → 842:0:0 |
| `q306_13b_epilogue_reed.scene / n12 / 1` | Leavin' for good. Vaya con Dios. (`leave`) | No option-level predicate stored | 0:1 → 19:0:0 |
| `q306_13b_epilogue_reed.scene / n12 / 2` | Medkit in the car stocked? (`head`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q302_reed_interrogation_fail", "value": 1, "comparisonType": "Equal"}}} | 0:2 → 934:0:1 |
| `q306_13b_epilogue_reed.scene / n12 / 3` | "Black Thorton Merrimac." (`tail`) | No option-level predicate stored | 0:3 → 935:0:1 |
| `q306_13b_epilogue_reed.scene / n454 / 0` | Fear. Song was scared you'd give 'er up to Myers. (`myers`) | No option-level predicate stored | 0:0 → 745:0:0 |
| `q306_13b_epilogue_reed.scene / n454 / 1` | Shame – at havin' betrayed you… (`betray`) | No option-level predicate stored | 0:1 → 834:0:0 |
| `q306_13b_epilogue_reed.scene / n454 / 2` | Cunning. Knew she couldn't dupe you, duped me easy. (`cheat`) | No option-level predicate stored | 0:2 → 838:0:0 |
| `q306_13b_epilogue_reed.scene / n454 / 3` | Hope – that I'd understand her… predicament. (`empathy`) | No option-level predicate stored | 0:3 → 840:0:0 |
| `q306_13b_epilogue_reed.scene / n454 / 4` | Practicality – calculated her chances, didn't listen to her heart. (`ouch`) | No option-level predicate stored | 0:4 → 1061:0:0 |
| `q306_13b_epilogue_reed.scene / n789 / 0` | Coulda done it already, long ago. (`bullshit`) | No option-level predicate stored | 0:0 → 792:0:0 |
| `q306_13b_epilogue_reed.scene / n789 / 1` | Stop spewin' crap. (`right`) | No option-level predicate stored | 0:1 → 858:0:0 |
| `q306_13b_epilogue_reed.scene / n789 / 2` | Can't. Promised he'd help me… (`surgery`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q306_finale_deal_done", "value": 1, "comparisonType": "Equal"}}} | 0:2 → 862:0:0 |
| `q306_13b_epilogue_reed.scene / n815 / 0` | I get it – drive'll be a pilgrimage into the depths of Sol Reed. (`pilgrim`) | No option-level predicate stored | 0:0 → 821:0:0 |
| `q306_13b_epilogue_reed.scene / n815 / 1` | Your very own penitential path, this drive? (`penitent`) | No option-level predicate stored | 0:1 → 823:0:0 |
| `q306_13b_epilogue_reed.scene / n815 / 2` | Gonna visit Songbird? (`visit_song`) | No option-level predicate stored | 0:2 → 1138:0:0 |
| `q306_13b_epilogue_reed.scene / n909 / 0` | Hadn't thought to call her any time over that seven-year span. (`silence`) | No option-level predicate stored | 0:0 → 913:0:0 |
| `q306_13b_epilogue_reed.scene / n909 / 1` | Oughta just ask her yourself, really. (`ask_her`) | No option-level predicate stored | 0:1 → 914:0:0 |
| `q306_13b_epilogue_reed.scene / n918 / 0` | This one time, just let it go. (`wishes`) | No option-level predicate stored | 0:0 → 948:0:0; 0:0 → 1276:0:0 |
| `q306_13b_epilogue_reed.scene / n918 / 1` | Got regrets? Learn to live with 'em. (`ice cube`) | No option-level predicate stored | 0:1 → 953:0:0; 0:1 → 1276:0:0 |
| `q306_13b_epilogue_reed.scene / n918 / 2` | Stop thinkin' about Songbird. Doesn't deserve it. (`forget`) | No option-level predicate stored | 0:2 → 1071:0:0 |
| `q306_13b_epilogue_reed.scene / n1225 / 0` | Don't mention it. (`no_prob`) | No option-level predicate stored | 0:0 → 1227:0:0 |
| `q306_13b_epilogue_reed.scene / n1225 / 1` | Bon voyage. (`warm`) | No option-level predicate stored | 0:1 → 1228:0:0 |
| `q306_13b_epilogue_reed.scene / n1654 / 0` | [Wait] (`Lean`) | No option-level predicate stored | 0:0 → 1656:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `cz_con_foodshop_01_default_on` | q306_13_epilogue.scene / scene / 1916; q306_epilogue_alex.questphase / h0 / 10 | No reader in selected context |
| `disable_hidden_gems_tutorial` | q306_06_epilogues.questphase / h0 / 242 | No reader in selected context |
| `holo_alex_calls_v_complete` | q306_06_epilogues.questphase / h0 / 228 | q306_epilogue_alex.questphase / h0 / 45 |
| `holo_alex_calls_v_end_activate` | q306_06_epilogues.questphase / h0 / 96; q306_12_holo_alex_call.scene / scene / 120 | No reader in selected context |
| `holo_alex_calls_v_end_done` | q306_06_epilogues.questphase / h0 / 100; q306_12_holo_alex_call.scene / scene / 112 | q306_06_epilogues.questphase / h0 / 99; q306_12_holo_alex_call.scene / scene / 110 |
| `holo_alex_calls_v_start_activate` | q306_06_epilogues.questphase / h0 / 95; q306_12_holo_alex_call.scene / scene / 118 | No reader in selected context |
| `holo_alex_calls_v_start_done` | q306_06_epilogues.questphase / h0 / 98; q306_12_holo_alex_call.scene / scene / 108 | q306_06_epilogues.questphase / h0 / 97; q306_12_holo_alex_call.scene / scene / 106 |
| `holo_reed_calls_v_complete` | q306_06_epilogues.questphase / h0 / 231 | q306_epilogue_reed.questphase / h0 / 46 |
| `holo_reed_calls_v_end_activate` | q306_06_epilogues.questphase / h0 / 90; q306_12b_holo_reed_call.scene / scene / 87 | No reader in selected context |
| `holo_reed_calls_v_end_done` | q306_06_epilogues.questphase / h0 / 94; q306_12b_holo_reed_call.scene / scene / 79 | q306_06_epilogues.questphase / h0 / 93; q306_12b_holo_reed_call.scene / scene / 77 |
| `holo_reed_calls_v_start_activate` | q306_06_epilogues.questphase / h0 / 89; q306_12b_holo_reed_call.scene / scene / 85 | No reader in selected context |
| `holo_reed_calls_v_start_done` | q306_06_epilogues.questphase / h0 / 92; q306_12b_holo_reed_call.scene / scene / 75 | q306_06_epilogues.questphase / h0 / 91; q306_12b_holo_reed_call.scene / scene / 73 |
| `mq001_done` | Producer outside selected context | q306_13_epilogue.scene / scene / 365 |
| `player_drunk` | q306_13_epilogue.scene / scene / 1511; q306_13_epilogue.scene / scene / 1520 | No reader in selected context |
| `q112_takemura_dead` | Producer outside selected context | q306_13_epilogue.scene / scene / 365 |
| `q115_point_of_no_return` | Producer outside selected context | q306_06_epilogues.questphase / h0 / 202 |
| `q302_reed_interrogation_fail` | Producer outside selected context | q306_13b_epilogue_reed.scene / scene / 12 |
| `q304_04e_heart_to_heart_done` | Producer outside selected context | q306_13_epilogue.scene / scene / 630 |
| `q306_12a_player_stood_up` | q306_12a_mission_aftermath.scene / scene / 480; q306_12a_mission_aftermath.scene / scene / 483 | q306_12a_mission_aftermath.scene / scene / 485; q306_12a_mission_aftermath.scene / scene / 488 |
| `q306_13_epilogue_progressed_pass_tv` | q306_13_epilogue.scene / scene / 1063 | No reader in selected context |
| `q306_13b_johnny_gone` | q306_13b_epilogue_reed.scene / scene / 1258 | q306_06_epilogues.questphase / h0 / 139; q306_epilogue_reed.questphase / h350 / 6 |
| `q306_13b_lookat_loop` | q306_13b_epilogue_reed.scene / scene / 1359; q306_13b_epilogue_reed.scene / scene / 1362; q306_13b_epilogue_reed.scene / scene / 1430; q306_13b_epilogue_reed.scene / scene / 1433 | q306_13b_epilogue_reed.scene / scene / 1381; q306_13b_epilogue_reed.scene / scene / 1441 |
| `q306_DEBUG_debugModeOn` | Producer outside selected context | q306_06_epilogues.questphase / h0 / 110; q306_06_epilogues.questphase / h0 / 220; q306_06_epilogues.questphase / h0 / 221; q306_06_epilogues.questphase / h0 / 39; q306_06_epilogues.questphase / h0 / 64 |
| `q306_alex_coin_given` | q306_13_epilogue.scene / scene / 1937 | No reader in selected context |
| `q306_alex_epilog_tv_done` | q306_13_epilogue.scene / scene / 1306; q306_epilogue_alex.questphase / h0 / 6 | q306_tv_bit.scene / scene / 115 |
| `q306_epilogue_alex_welcomes_v` | q306_13_epilogue.scene / scene / 1609 | q306_tv_bit.scene / scene / 82 |
| `q306_epilogue_johnny_done_a` | q306_13_epilogue.scene / scene / 1611 | q306_tv_bit.scene / scene / 93 |
| `q306_epilogue_johnny_done_b` | q306_13_epilogue.scene / scene / 1618 | q306_tv_bit.scene / scene / 97 |
| `q306_epilogue_reed_scene_done` | q306_epilogue_reed.questphase / h0 / 23 | No reader in selected context |
| `q306_finale_deal_done` | q306_06_epilogues.questphase / h709 / 54; q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 45 | q306_06_epilogues.questphase / h0 / 214; q306_06_epilogues.questphase / h0 / 237; q306_12b_holo_reed_call.scene / scene / 113; q306_13b_epilogue_reed.scene / scene / 789; q306_13b_epilogue_reed.scene / scene / 869 |
| `q306_launchpad_retreated_scenario` | Producer outside selected context | q306_06_epilogues.questphase / h0 / 141 |
| `q306_tv_bit_line_001_done` | q306_tv_bit.scene / scene / 23 | q306_13_epilogue.scene / scene / 1623 |
| `q306_tv_bit_line_002_done` | q306_tv_bit.scene / scene / 25 | q306_13_epilogue.scene / scene / 1255 |
| `q306_tv_bit_line_003_done` | q306_tv_bit.scene / scene / 28 | q306_13_epilogue.scene / scene / 1614 |
| `q306_tv_bit_line_004_done` | q306_tv_bit.scene / scene / 30 | No reader in selected context |
| `q306_tv_bit_line_005_done` | q306_tv_bit.scene / scene / 32 | q306_13_epilogue.scene / scene / 1631 |
| `q306_tv_bit_line_006_done` | q306_tv_bit.scene / scene / 34 | No reader in selected context |
| `q306_tv_bit_line_007_done` | q306_tv_bit.scene / scene / 36 | No reader in selected context |
| `q306_tv_bit_turned_on_tv` | q306_tv_bit.scene / scene / 399; q306_tv_bit.scene / scene / 404 | q306_tv_bit.scene / scene / 397 |
| `wanted_level` | Producer outside selected context | q306_epilogue_reed.questphase / h148 / 5 |

## Exact gates, joins and cancellation

<details><summary>136 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 185` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 167:Out → 185:In; 185:Out → 168:Failed |
| `q115_00_hanako.questphase / h1024 / 186` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 168:Out → 186:In; 186:Out → 169:Failed |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alex/q306_meeting_reminder/q306_meeting_reminder_03_ch_visit/q306_meeting_reminder_03a_coming","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 6:Out → 8:In; 8:Out → 15:Active |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 10` | `questLogicalXorNodeDefinition` `{}` | 15:Out → 10:In1; 17:Out → 10:In2; 10:Out1 → 20:In3 |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1,"hours":23}}}` | 0:Out → 11:In; 11:Out → 3:Active |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alex/q306_meeting_reminder/q306_meeting_reminder_03_ch_visit/q306_meeting_reminder_03b_question","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 6:Out → 13:In; 13:Out → 17:Active |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_phone_off"}}` | 0:Out → 19:In; 19:Out → 22:In |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 20` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 20:Out1 → 1:In; 10:Out1 → 20:In3; 22:True → 20:In1; 21:Out → 20:In2 |
| `q306_msg_alex_meeting_reminder.questphase / h0 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alex/q306_meeting_reminder/q306_meeting_reminder_03_ch_visit/q306_meeting_reminder_03a_coming","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alex/q306_meeting_reminder/q306_meeting_reminder_03_ch_visit/q306_meeting_reminder_03b_question","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}]}}` | 19:Out → 22:In; 22:True → 20:In1; 22:False → 21:Inactive |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/02_v_answer_unexpected/02_v_answer_unexpected_hostile","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 6:Out → 7:In; 7:Out → 10:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/02_v_answer_unexpected/02_v_answer_unexpected_interested","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 6:Out → 8:In; 8:Out → 11:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/05_v_answer_cure_offer/05_v_answer_cure_offer_accept","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 13:Out → 14:In; 14:Out → 39:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/05_v_answer_cure_offer/05_v_answer_cure_offer_refuse","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 13:Out → 15:In; 15:Out → 17:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 0:Out → 24:In; 24:Out → 49:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/06_v_answer_cure_offer_response_refuse/06_v_answer_cure_offer_response_refuse_accept","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 35:In; 35:Out → 39:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/06_v_answer_cure_offer_response_refuse/06_v_answer_cure_offer_response_refuse_reason_001","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 36:In; 36:Out → 40:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/06_v_answer_cure_offer_response_refuse/06_v_answer_cure_offer_response_refuse_reason_002","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 37:In; 37:Out → 41:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/06_v_answer_cure_offer_response_refuse/06_v_answer_cure_offer_response_refuse_reason_003","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 38:In; 38:Out → 42:Active |
| `q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_launchpad_retreated_scenario/01_unexpected","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 2:Out → 50:In; 50:Out → 51:Succeeded |
| `q306_06_epilogues.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 218:Out → 20:In; 20:Out → 108:In1; 20:Out → 107:In2 |
| `q306_06_epilogues.questphase / h0 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 25:Out → 39:In; 39:True → 37:Teleport |
| `q306_06_epilogues.questphase / h0 / 64` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 59:Out → 64:In; 64:True → 62:Teleport |
| `q306_06_epilogues.questphase / h0 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reed_calls_v_start_done"}}}` | 89:Out → 91:In; 91:Out → 92:In |
| `q306_06_epilogues.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reed_calls_v_end_done"}}}` | 90:Out → 93:In; 93:Out → 94:In |
| `q306_06_epilogues.questphase / h0 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_alex_calls_v_start_done"}}}` | 95:Out → 97:In; 97:Out → 98:In |
| `q306_06_epilogues.questphase / h0 / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_alex_calls_v_end_done"}}}` | 96:Out → 99:In; 99:Out → 100:In |
| `q306_06_epilogues.questphase / h0 / 107` | `questLogicalAndNodeDefinition` `{}` | 3:Out → 107:In1; 20:Out → 107:In2; 107:Out1 → 105:In |
| `q306_06_epilogues.questphase / h0 / 108` | `questLogicalAndNodeDefinition` `{}` | 20:Out → 108:In1; 47:Out → 108:In2; 108:Out1 → 104:In |
| `q306_06_epilogues.questphase / h0 / 110` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 104:Out → 110:In; 105:Out → 110:In; 110:False → 109:In; 110:True → 111:In |
| `q306_06_epilogues.questphase / h0 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 112:Out → 109:In; 111:Out → 112:In |
| `q306_06_epilogues.questphase / h0 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_13b_johnny_gone","value":1,"comparisonType":"Equal"}}}` | 162:Out → 139:In; 139:Out → 214:In |
| `q306_06_epilogues.questphase / h0 / 141` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_launchpad_retreated_scenario"}}}` | 237:False → 141:In; 141:True → 142:In1; 141:False → 238:In2 |
| `q306_06_epilogues.questphase / h0 / 148` | `questLogicalAndNodeDefinition` `{}` | 106:q306_reed_wrap_out → 148:In2; 129:Out → 148:In1; 148:Out1 → 184:In; 148:Out1 → 202:In; 148:Out1 → 237:In |
| `q306_06_epilogues.questphase / h0 / 149` | `questLogicalAndNodeDefinition` `{}` | 103:q306_somi_wrap_out → 149:In1; 129:Out → 149:In2; 149:Out1 → 183:In; 149:Out1 → 192:In |
| `q306_06_epilogues.questphase / h0 / 176` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":23}}}` | 232:Out → 176:In; 241:Out1 → 176:In; 176:Out → 216:In |
| `q306_06_epilogues.questphase / h0 / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":11}}}` | 149:Out1 → 192:In; 192:Out → 215:In |
| `q306_06_epilogues.questphase / h0 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 148:Out1 → 202:In; 202:Out → 204:In |
| `q306_06_epilogues.questphase / h0 / 214` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_finale_deal_done"}}}` | 139:Out → 214:In; 214:True → 197:Active; 214:False → 262:In |
| `q306_06_epilogues.questphase / h0 / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_nighthawks_closed"}}` | 192:Out → 215:In; 215:Out → 243:In; 215:Out → 221:In |
| `q306_06_epilogues.questphase / h0 / 216` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_gas_station_area_big"}}` | 176:Out → 216:In; 216:Out → 220:In |
| `q306_06_epilogues.questphase / h0 / 217` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 217:Out → 113:In; 129:Out → 217:In |
| `q306_06_epilogues.questphase / h0 / 220` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 220:True → 57:Start 0; 216:Out → 220:In; 220:False → 254:In |
| `q306_06_epilogues.questphase / h0 / 221` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 221:True → 15:Start 0; 215:Out → 221:In; 221:False → 252:In |
| `q306_06_epilogues.questphase / h0 / 237` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_finale_deal_done"}}}` | 237:False → 141:In; 148:Out1 → 237:In; 237:True → 150:In1 |
| `q306_06_epilogues.questphase / h0 / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 252:Out → 253:In; 253:Out → 257:In |
| `q306_06_epilogues.questphase / h0 / 255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 254:Out → 255:In; 255:Out → 259:In |
| `q306_06_epilogues.questphase / h0 / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 15:End 0 → 256:In; 256:Out → 258:In |
| `q306_06_epilogues.questphase / h0 / 261` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 57:End 0 → 261:In; 261:Out → 260:In |
| `q306_06_epilogues.questphase / h709 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 25:Out → 39:In; 39:Out → 76:Active |
| `q306_06_epilogues.questphase / h709 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_deal_denied/02_ch_v_answers/02_alright","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 65:Out → 66:In; 66:Out → 68:Active |
| `q306_06_epilogues.questphase / h709 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_deal_denied/02_ch_v_answers/02_fuck_off","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 65:Out → 67:In; 67:Out → 69:Active |
| `q306_06_epilogues.questphase / h709 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/reed/q306_deal_denied/01b_reed_cure_offer","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 72:Out → 70:In; 70:Out → 71:Succeeded |
| `q306_epilogue_alex.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior_full"}}` | 45:True → 20:In; 20:Out → 35:Inactive |
| `q306_epilogue_alex.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_epilogue_tv_in"}}` | 15:Out → 26:In; 26:Out → 25:tv_start; 48:Out2 → 26:In; 26:Out → 30:In |
| `q306_epilogue_alex.questphase / h0 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_nighthawks_closed"}}` | 0:Out → 40:In; 40:False → 11:In; 40:True → 45:In |
| `q306_epilogue_alex.questphase / h0 / 45` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_alex_calls_v_complete"}}}` | 45:False → 11:In; 45:True → 20:In; 40:True → 45:In |
| `q306_epilogue_reed.questphase / h0 / 5` | `questLogicalAndNodeDefinition` `{}` | 3:Out → 5:In1; 4:Out → 5:In2; 5:Out1 → 70:In |
| `q306_epilogue_reed.questphase / h0 / 10` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 10:Out1 → 1:In; 2:End 0 → 10:In1; 23:Out → 10:In2; 39:Out1 → 10:In3 |
| `q306_epilogue_reed.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#reed_car"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 13:In; 13:Out → 12:In; 13:Out → 14:In |
| `q306_epilogue_reed.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_area"}}` | 31:Out → 32:In; 32:Out → 35:In |
| `q306_epilogue_reed.questphase / h0 / 46` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reed_calls_v_complete"}}}` | 46:True → 41:Inactive; 46:True → 45:Inactive; 48:True → 46:In; 46:False → 49:In1 |
| `q306_epilogue_reed.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_area_big"}}` | 0:Out → 48:In; 48:True → 46:In; 48:False → 49:In1 |
| `q306_epilogue_reed.questphase / h148 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_toggle_UI_area"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wanted_level","comparisonType":"Equal"}}]}}` | 0:Out → 5:In; 5:Out → 4:In; 10:CutSource → 5:CutDestination; 15:Out → 5:In |
| `q306_epilogue_reed.questphase / h148 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_gas_station_toggle_UI_area"}}` | 10:CutSource → 6:CutDestination; 14:Out → 6:In; 6:Out → 7:In |
| `q306_epilogue_reed.questphase / h148 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/05_talk_to_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 9:In; 9:Out → 10:In |
| `q306_epilogue_reed.questphase / h148 / 10` | `questCutControlNodeDefinition` `{"permanent":true}` | 10:CutSource → 3:CutDestination; 10:CutSource → 4:CutDestination; 10:CutSource → 5:CutDestination; 10:CutSource → 6:CutDestination; 10:CutSource → 7:CutDestination; 10:CutSource → 8:CutDestination; 9:Out → 10:In; 10:Out → 13:In |
| `q306_epilogue_reed.questphase / h148 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 10:Out → 13:In; 13:Out → 11:In |
| `q306_epilogue_reed.questphase / h148 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 3:Out → 14:In; 14:Out → 6:In |
| `q306_epilogue_reed.questphase / h148 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 15:Out → 5:In; 8:Out → 15:In |
| `q306_epilogue_reed.questphase / h350 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_toggle_UI_area"}}` | 0:Out → 2:In; 3:Out → 2:In; 2:Out → 3:In; 2:Out → 4:In |
| `q306_epilogue_reed.questphase / h350 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_gas_station_toggle_UI_area"}}` | 3:Out → 2:In; 2:Out → 3:In; 3:Out → 5:In |
| `q306_epilogue_reed.questphase / h350 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_13b_johnny_gone","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 6:In; 6:Out → 1:In |
| `q306_12_holo_alex_call.scene / scene / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_12_holo_alex_call.scene","Flags":"Soft"},"sectionName":"q306_12_discreet","type":"IsOutside"}}}` | 49:0:1 → 63:0:1; 63:0:0 → 51:0:0 |
| `q306_12_holo_alex_call.scene / scene / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_alex_calls_v_start_done"}}}` | 106:0:0 → 108:0:1; 118:0:0 → 106:0:1 |
| `q306_12_holo_alex_call.scene / scene / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_alex_calls_v_end_done"}}}` | 110:0:0 → 112:0:1; 120:0:0 → 110:0:1 |
| `q306_12a_mission_aftermath.scene / scene / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 108:0:0 → 110:0:1; 110:0:0 → 158:0:1 |
| `q306_12a_mission_aftermath.scene / scene / 115` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 113:0:0 → 115:0:1; 115:0:0 → 157:0:1 |
| `q306_12a_mission_aftermath.scene / scene / 450` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q306_12a_mission_aftermath_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 443:0:0 → 450:0:1; 450:0:0 → 208:0:0 |
| `q306_12a_mission_aftermath.scene / scene / 464` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q306_12a_mission_aftermath_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 462:0:0 → 464:0:1; 464:0:0 → 313:0:0 |
| `q306_12a_mission_aftermath.scene / scene / 485` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_12a_player_stood_up","value":1,"comparisonType":"Equal"}},{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}]}}` | 208:3:0 → 485:0:1; 485:0:0 → 453:0:0 |
| `q306_12a_mission_aftermath.scene / scene / 488` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_12a_player_stood_up","value":1,"comparisonType":"Equal"}},{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}]}}` | 313:3:0 → 488:0:1; 488:0:0 → 469:0:0 |
| `q306_12b_holo_reed_call.scene / scene / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reed_calls_v_start_done"}}}` | 73:0:0 → 75:0:1; 85:0:0 → 73:0:1 |
| `q306_12b_holo_reed_call.scene / scene / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reed_calls_v_end_done"}}}` | 77:0:0 → 79:0:1; 87:0:0 → 77:0:1 |
| `q306_12b_holo_reed_call.scene / scene / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 79:0:0 → 147:0:1; 147:0:0 → 142:0:0 |
| `q306_12b_holo_reed_call.scene / scene / 155` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q306_reed_epilogue/00_epilogue/00_wait_for_call_reed","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 81:0:0 → 155:0:1; 155:0:0 → 106:0:3; 155:0:1 → 13:0:1 |
| `q306_13_epilogue.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior"}}` | 10:0:0 → 254:0:1; 254:0:0 → 13:0:0; 254:0:0 → 465:0:3; 254:0:0 → 1259:0:0 |
| `q306_13_epilogue.scene / scene / 461` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 459:0:0 → 461:0:1; 461:0:0 → 460:0:1 |
| `q306_13_epilogue.scene / scene / 680` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_13_epilogue.scene","Flags":"Soft"},"sectionName":"q306_13_safety","type":"IsOutside"}}}` | 630:0:0 → 680:0:1; 680:0:0 → 631:0:0 |
| `q306_13_epilogue.scene / scene / 681` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_13_epilogue.scene","Flags":"Soft"},"sectionName":"q306_13_what_now","type":"IsOutside"}}}` | 630:0:1 → 681:0:1; 681:0:0 → 632:0:0 |
| `q306_13_epilogue.scene / scene / 787` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_13_epilogue.scene","Flags":"Soft"},"sectionName":"q306_13_corpowar_blueline","type":"IsOutside"}}}` | 630:0:3 → 787:0:1; 787:0:0 → 784:0:0 |
| `q306_13_epilogue.scene / scene / 1255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_tv_bit_line_002_done"}}}` | 1255:0:0 → 1270:0:2; 1266:0:0 → 1255:0:1 |
| `q306_13_epilogue.scene / scene / 1266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 1259:0:0 → 1266:0:1; 1266:0:0 → 355:0:1; 1266:0:0 → 1255:0:1 |
| `q306_13_epilogue.scene / scene / 1546` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior"}}` | 13:0:0 → 1546:0:1; 1546:0:0 → 1623:0:1 |
| `q306_13_epilogue.scene / scene / 1550` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior"}}` | 1270:0:0 → 1550:0:1; 1550:0:0 → 351:0:0 |
| `q306_13_epilogue.scene / scene / 1561` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior"}}` | 351:0:0 → 1561:0:1; 1561:0:0 → 1614:0:1 |
| `q306_13_epilogue.scene / scene / 1568` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior_full"}}` | 1568:0:0 → 1389:0:1; 1655:0:0 → 1568:0:1 |
| `q306_13_epilogue.scene / scene / 1571` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior_full"}}` | 1571:0:0 → 1601:0:1; 1605:0:0 → 1571:0:1 |
| `q306_13_epilogue.scene / scene / 1605` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1388:0:0 → 1605:0:1; 1605:0:0 → 1571:0:1 |
| `q306_13_epilogue.scene / scene / 1614` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_tv_bit_line_003_done"}}}` | 1561:0:0 → 1614:0:1; 1614:0:0 → 1554:0:0 |
| `q306_13_epilogue.scene / scene / 1623` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_tv_bit_line_001_done"}}}` | 1546:0:0 → 1623:0:1; 1623:0:0 → 482:0:0 |
| `q306_13_epilogue.scene / scene / 1631` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_tv_bit_line_005_done"}}}` | 1554:2:0 → 1631:0:1; 1631:0:0 → 1634:0:0 |
| `q306_13_epilogue.scene / scene / 1655` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1574:0:0 → 1655:0:1; 1655:0:0 → 1568:0:1 |
| `q306_13_epilogue.scene / scene / 1828` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":334}}}` | 1828:0:0 → 1824:0:0; 1828:0:0 → 1848:0:1; 1834:0:0 → 1828:0:1 |
| `q306_13_epilogue.scene / scene / 1836` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1832:0:0 → 1836:0:1; 1836:0:0 → 1838:0:1 |
| `q306_13_epilogue.scene / scene / 1848` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":570}}}` | 1828:0:0 → 1848:0:1; 1848:0:0 → 1832:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_area"},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#reed","names":["reed"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#reed","names":["reed"]},"onScreenTest":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true,"condition":"OnUnmount"}}]}}` | 1:0:0 → 7:0:1; 7:0:0 → 158:0:3; 7:0:0 → 1543:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 510` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 91:0:0 → 510:0:1; 510:0:0 → 164:0:3; 882:0:0 → 510:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 869` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_finale_deal_done","value":1,"comparisonType":"Equal"}}}` | 869:0:0 → 1247:0:1; 869:0:1 → 1251:0:1; 1225:4:0 → 869:0:1; 1227:2:0 → 869:0:1; 1228:2:0 → 869:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 934` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_13b_epilogue_reed.scene","Flags":"Soft"},"sectionName":"q306_13b_head_PU","type":"IsOutside"}}}` | 12:0:2 → 934:0:1; 934:0:0 → 895:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 935` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\main_quests\\q306\\scenes\\q306_13b_epilogue_reed.scene","Flags":"Soft"},"sectionName":"q306_13b_tail_PU","type":"IsOutside"}}}` | 12:0:3 → 935:0:1; 935:0:0 → 897:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1219` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 1219:0:0 → 1188:0:1; 1276:2:0 → 1219:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1241` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q306_13b_epilogue_reed_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 857:0:0 → 1241:0:1; 1241:0:0 → 1258:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1351` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 1351:0:0 → 1348:0:0; 1371:0:0 → 1351:0:1; 1378:1:0 → 1351:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1368` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 1368:0:0 → 1348:0:0; 1371:0:1 → 1368:0:1; 1378:1:0 → 1368:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1381` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_13b_lookat_loop","comparisonType":"Equal"}}}` | 454:1:0 → 1381:0:1; 909:1:0 → 1381:0:1; 1381:0:0 → 1378:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1424` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 382:2:0 → 1424:0:1; 811:2:0 → 1424:0:1; 895:2:0 → 1424:0:1; 897:2:0 → 1424:0:1; 1424:0:0 → 1433:0:1; 1430:0:0 → 1424:0:1; 1438:1:0 → 1424:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1441` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_13b_lookat_loop","comparisonType":"Equal"}}}` | 12:1:0 → 1441:0:1; 1441:0:0 → 1438:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1469` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 142:0:0 → 1469:0:1; 1469:0:0 → 1472:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1486` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_gas_station_area_big"}}` | 1:0:0 → 1486:0:1; 1486:0:0 → 996:0:0; 1486:0:0 → 1495:0:1; 1489:1:0 → 1486:0:0; 1495:0:0 → 1486:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1495` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q306_tr_gas_station_area_big"}}` | 1486:0:0 → 1495:0:1; 1489:1:0 → 1495:0:0; 1495:0:0 → 1486:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1553` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q306_13b_epilogue_reed_Johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 1038:2:0 → 1553:0:1; 1553:0:0 → 857:0:0 |
| `q306_13b_epilogue_reed.scene / scene / 1588` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1584:0:0 → 1588:0:1; 1588:0:0 → 1590:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1627` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#reed_car"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1624:0:0 → 1627:0:1; 1627:0:0 → 1626:0:1; 1627:0:0 → 1628:0:1 |
| `q306_13b_epilogue_reed.scene / scene / 1674` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":83}}}` | 1580:0:0 → 1674:0:1; 1674:0:0 → 1702:0:0 |
| `q306_tv_bit.scene / scene / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_epilogue_alex_welcomes_v","value":1,"comparisonType":"Equal"}}}` | 1:0:0 → 82:0:1; 82:0:0 → 250:0:0 |
| `q306_tv_bit.scene / scene / 84` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q306_tr_alex_epilogue_bar_interior"}}` | 23:0:0 → 84:0:1; 84:0:0 → 87:0:0 |
| `q306_tv_bit.scene / scene / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_epilogue_johnny_done_a","value":1,"comparisonType":"Equal"}}}` | 25:0:0 → 93:0:1; 93:0:0 → 137:0:1 |
| `q306_tv_bit.scene / scene / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_epilogue_johnny_done_b","value":1,"comparisonType":"Equal"}}}` | 28:0:0 → 97:0:1; 97:0:0 → 59:0:0; 97:0:0 → 350:0:0 |
| `q306_tv_bit.scene / scene / 115` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_alex_epilog_tv_done","value":1,"comparisonType":"Equal"}}}` | 61:2:2 → 115:0:1; 115:0:0 → 117:0:0 |
| `q306_tv_bit.scene / scene / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q306_com_tv_studio","names":["journalist"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 135:0:0 → 340:0:1; 135:0:0 → 399:0:1; 336:0:0 → 135:0:1 |
| `q306_tv_bit.scene / scene / 137` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q306_com_tv_studio","names":["wawuda"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 93:0:0 → 137:0:1; 137:0:0 → 57:0:0; 137:0:0 → 325:0:0 |
| `q306_tv_bit.scene / scene / 336` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q306_com_tv_studio","names":["journalist_chicken"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 51:0:0 → 336:0:1; 336:0:0 → 135:0:1 |
| `q306_tv_bit.scene / scene / 340` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 135:0:0 → 340:0:1; 340:0:0 → 54:0:0; 340:0:0 → 307:0:0 |
| `q306_tv_bit.scene / scene / 365` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 117:0:0 → 365:0:1; 365:0:0 → 123:0:0 |
| `q306_tv_bit.scene / scene / 394` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 257:0:0 → 394:0:1; 394:0:0 → 397:0:1 |
| `q306_tv_bit.scene / scene / 397` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_tv_bit_turned_on_tv","value":1,"comparisonType":"Equal"}}}` | 394:0:0 → 397:0:1; 397:0:0 → 257:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | q306_13b_epilogue_reed.scene / scene / 1627; q306_epilogue_reed.questphase / h0 / 13; q306_tv_bit.scene / scene / 135; q306_tv_bit.scene / scene / 137; +1 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | q306_13_epilogue.scene / scene / 645 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | q306_06_epilogues.questphase / h0 / 104; q306_06_epilogues.questphase / h0 / 105 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | q306_12_holo_alex_call.scene / scene / 49; q306_12_holo_alex_call.scene / scene / 7; q306_12a_mission_aftermath.scene / scene / 203; q306_12a_mission_aftermath.scene / scene / 224; +26 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | q306_06_epilogues.questphase / h0 / 243; q306_13_epilogue.scene / scene / 1917; q306_epilogue_alex.questphase / h0 / 11; q306_epilogue_alex.questphase / h0 / 64; +5 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | q306_06_epilogues.questphase / h0 / 110; q306_06_epilogues.questphase / h0 / 139; q306_06_epilogues.questphase / h0 / 141; q306_06_epilogues.questphase / h0 / 202; +37 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | q306_06_epilogues.questphase / h0 / 113; q306_06_epilogues.questphase / h0 / 199; q306_06_epilogues.questphase / h0 / 218; q306_06_epilogues.questphase / h0 / 257; +12 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | q306_epilogue_reed.questphase / h0 / 70; q306_epilogue_reed.questphase / h0 / 71; q306_epilogue_reed.questphase / h0 / 72; q306_tv_bit.scene / scene / 257 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | q306_13_epilogue.scene / scene / 1295; q306_13_epilogue.scene / scene / 1388; q306_13_epilogue.scene / scene / 1389; q306_13_epilogue.scene / scene / 1524; +10 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | q306_06_epilogues.questphase / h0 / 176; q306_06_epilogues.questphase / h0 / 192; q306_msg_alex_meeting_reminder.questphase / h0 / 11 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | q306_06_epilogues.questphase / h709 / 70; q306_msg_reed_launchpad_retreated_scenario.questphase / h0 / 50 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | q115_00_hanako.questphase / h1024 / 168; q306_06_epilogues.questphase / h0 / 136; q306_06_epilogues.questphase / h0 / 190; q306_06_epilogues.questphase / h0 / 191; +76 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | q306_13b_epilogue_reed.scene / scene / 7 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | q306_06_epilogues.questphase / h0 / 107; q306_06_epilogues.questphase / h0 / 108; q306_06_epilogues.questphase / h0 / 148; q306_06_epilogues.questphase / h0 / 149; +2 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | q306_06_epilogues.questphase / h0 / 100; q306_06_epilogues.questphase / h0 / 228; q306_06_epilogues.questphase / h0 / 231; q306_06_epilogues.questphase / h0 / 242; +45 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | q306_msg_alex_meeting_reminder.questphase / h0 / 10; q306_msg_alex_meeting_reminder.questphase / h0 / 20 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | q115_00_hanako.questphase / h1024 / 185; q115_00_hanako.questphase / h1024 / 186; q306_06_epilogues.questphase / h0 / 112; q306_06_epilogues.questphase / h0 / 20; +31 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | q306_epilogue_reed.questphase / h148 / 10 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | q306_06_epilogues.questphase / h0 / 160; q306_06_epilogues.questphase / h0 / 161; q306_06_epilogues.questphase / h0 / 162; q306_06_epilogues.questphase / h0 / 187 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | q306_06_epilogues.questphase / h0 / 103; q306_06_epilogues.questphase / h0 / 106; q306_06_epilogues.questphase / h0 / 15; q306_06_epilogues.questphase / h0 / 37; +8 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | q306_06_epilogues.questphase / h0 / 215; q306_06_epilogues.questphase / h0 / 216; q306_13_epilogue.scene / scene / 1546; q306_13_epilogue.scene / scene / 1550; +18 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | q306_06_epilogues.questphase / h0 / 109; q306_06_epilogues.questphase / h0 / 111; q306_13b_epilogue_reed.scene / scene / 1188; q306_13b_epilogue_reed.scene / scene / 1472; +6 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | q306_12a_mission_aftermath.scene / scene / 127; q306_12a_mission_aftermath.scene / scene / 129; q306_12a_mission_aftermath.scene / scene / 135; q306_12a_mission_aftermath.scene / scene / 206; +94 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | q306_12a_mission_aftermath.scene / scene / 324; q306_12a_mission_aftermath.scene / scene / 582; q306_12a_mission_aftermath.scene / scene / 586; q306_13_epilogue.scene / scene / 1933; +6 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase` | content candidate; journal anchor | `base-q115` |
| `ep1\quest\main_quests\q306\phases\messages\q306_msg_alex_meeting_reminder.questphase` | content candidate; forward dependency | `ep1-q306` |
| `ep1\quest\main_quests\q306\phases\messages\q306_msg_reed_launchpad_retreated_scenario.questphase` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` | content candidate; forward dependency | `ep1-q306` |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` | content candidate; forward dependency | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene` | content candidate; forward dependency | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene` | content candidate; forward dependency | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene` | content candidate; forward dependency | `ep1-q306` |

Evidence shards for this dossier (including parent context): [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

565 repeated typed/socket path signatures in this selected graph context; 83 distinct direct resource identities; 3 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` / scene / 118 -> 106 -> 108 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` / scene / 116 -> 120 -> 110 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` / scene / 110 -> 112 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene` / scene / 137 -> 83 -> 87 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h350 / 0 -> 6 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `bbf9efd740881cf31a37` | `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene` / scene / 1381 -> 1378 -> 1351 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `10de5d2a81ab97879de5` | `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h0 / 23 -> 10 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out -> In2; Out1 -> In |
| `19665e3783f6f51a7337` | `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene` / scene / 10 -> 809 -> 912 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `18be198845c90c6bb3c8` | `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 192 -> 215 -> 243 | questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `95d4997362b664c5c23b` | `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene` / scene / 185 -> 502 -> 505 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `276aca4a2dc348a877d5` | `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene` / scene / 58 -> 185 -> 267 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `7e7dbbc930b3717fd790` | `ep1\quest\main_quests\q306\phases\messages\q306_msg_alex_meeting_reminder.questphase` / h0 / 3 -> 4 -> 6 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\quest\main_quests\q306\phases\q306_06_epilogues.questphase` / h0 / 238 | `h709` | [{"$type":"questInputNodeDefinition","id":25,"socketName":"In2"},{"$type":"questOutputNodeDefinition","id":26,"socketName":"Out2"},{"$type":"questOutputNodeDefinition","id":42,"socketName":"Refused_Out"}] |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h0 / 39 | `h148` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` / h0 / 74 | `h350` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest; ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest; ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_bar_lean180__2h_elbow_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_bar_lean90__rh_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\open_world\generic_female_average_work__stand_bar_lean0__2h_on_bar_wide__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_barstool_bar_lean90__rh_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__rh_up__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_table_lean0__2h_on_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__03.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand_wall_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__2h_on_sides__aggressive__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_thorton_mackinaw__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q103\q103_03_rogue\body\q103_03_rogue__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q105\q105_03a_dollhouse_doll_01\q105_03a_dollhouse_doll_01__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q110\q110_04_netrunners_den\q110_04_netrunners_den__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q110\q110_04_netrunners_den\q110_04_netrunners_den__player_woman.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\workspots\bar\bar\generic__stand_bar_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\bar\bar_and_barstool\generic__sit_barstool_bar__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_front__stand_around__07.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_table_lean_front__nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair_table\generic__sit_chair_table_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__stand_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\office\chair\generic__sit_armchair_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\ground\player__stand_ground__idle__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q105\q105_03a_dollhouse_doll_01\player__sit_bed_lean_front__relax__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq031\sq031_01a_smack_afterlife\sq031__johnny__stand__wait_nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `ep1\animations\facial\main_characters\reed\reed_facial_gestures.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_10_eden_call\body\q306_10_eden_call__player_female.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_10_eden_call\body\q306_10_eden_call__player_male.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13_epilogue\body\q306_13_epilogue__alex.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13_epilogue\body\q306_13_epilogue__fpp_female.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13_epilogue\body\q306_13_epilogue__fpp_male.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13_epilogue\body\q306_13_epilogue__johnny.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13b_epilogue_reed\synced\synced__q306_13b_epilogue_reed__male_big.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\main_quests\q306\q306_13b_epilogue_reed\synced\synced__q306_13b_epilogue_reed__thorton_merrimac.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\quest\minor_quests\mq301\mq301_02_initiation\body\mq301_02_initiation__player.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\quest\main_quests\q306\phases\messages\q306_msg_alex_meeting_reminder.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\phases\messages\q306_msg_reed_launchpad_retreated_scenario.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_alex.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\phases\subphases\q306_epilogue_reed.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12_holo_alex_call\alex.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12_holo_alex_call\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12a_mission_aftermath\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12a_mission_aftermath\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12b_holo_reed_call\reed.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_12b_holo_reed_call\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13_epilogue\alex.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13_epilogue\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13_epilogue\tv_sports_commentator.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13_epilogue\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13b_epilogue_reed\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13b_epilogue_reed\reed.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_13b_epilogue_reed\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_tv_bit\civ_high_m_07_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_tv_bit\wawuda.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q306\test\q306_00_chickentest.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\workspots\quest\main_quests\q304\q304_03_songbird_meeting\q304__songbird__stand__arms_crossed_front__01.workspot` | performance binding | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\workspots\quest\main_quests\q306\q306_13_epilogue\ep1__q306__player__sit_barstool_bar_lean_front__sit__01.workspot` | performance binding | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\workspots\quest\main_quests\q306\q306_13b_epilogue_reed\ep1__q306__reed__stand_car__check_engine__01.workspot` | performance binding | ep1/ep1_1_nightcity.archive; index evidence only |
| `ep1\workspots\quest\main_quests\q306\q306_13b_epilogue_reed\ep1__q306__reed__stand_car__check_engine__02.workspot` | performance binding | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\workspots\quest\main_quests\q306\q306_13b_epilogue_reed\ep1__q306__synced__reed__sit_thorton_merrimac__drive__01.workspot` | performance binding | ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `cz_con_foodshop_01_default_on` | ep1\quest\main_quests\q303\phases\q303_02_nighthawks.questphase / h518 / 62; ep1\quest\main_quests\q303\phases\q303_02_nighthawks.questphase / h656 / 62; ep1\quest\main_quests\q303\q303.quest / h11776 / 7; ep1\quest\main_quests\q303\q303.questphase / h158 / 6; 15 total source locations in compressed evidence |
| `disable_hidden_gems_tutorial` | ep1\quest\main_quests\q306\phases\q306_05_launchpad.questphase / h133 / 26; 1 total source locations in compressed evidence |
| `holo_alex_calls_v_end_activate` | ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5727; ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5753; ep1\quest\main_quests\q304\phases\q304_02b_car_rental.questphase / h14 / 73; ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene / scene / 116; 5 total source locations in compressed evidence |
| `holo_alex_calls_v_end_done` | ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5719; ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5751; ep1\quest\main_quests\q304\phases\q304_02b_car_rental.questphase / h14 / 77; ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene / scene / 108; 6 total source locations in compressed evidence |
| `holo_alex_calls_v_start_activate` | ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5725; ep1\quest\main_quests\q304\phases\q304_02b_car_rental.questphase / h14 / 72; ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene / scene / 114; ep1\quest\holocalls\alex\alex_holocall.questphase / h0 / 8; 4 total source locations in compressed evidence |
| `holo_alex_calls_v_start_done` | ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene / scene / 5715; ep1\quest\main_quests\q304\phases\q304_02b_car_rental.questphase / h14 / 75; ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene / scene / 104; ep1\quest\holocalls\alex\alex_holocall.scene / scene / 78; 5 total source locations in compressed evidence |
| `holo_reed_calls_v_end_activate` | ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 13; ep1\quest\main_quests\q302\scenes\q302_08_call.scene / scene / 56; ep1\quest\main_quests\q303\phases\q303_07b_lobby_combat.questphase / h0 / 567; ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene / scene / 9596; 21 total source locations in compressed evidence |
| `holo_reed_calls_v_end_done` | ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 57; ep1\quest\main_quests\q302\scenes\q302_08_call.scene / scene / 48; ep1\quest\main_quests\q303\phases\q303_07b_lobby_combat.questphase / h0 / 571; ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene / scene / 9588; 22 total source locations in compressed evidence |
| `holo_reed_calls_v_start_activate` | ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 12; ep1\quest\main_quests\q302\scenes\q302_08_call.scene / scene / 54; ep1\quest\main_quests\q303\phases\q303_07b_lobby_combat.questphase / h0 / 566; ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene / scene / 9594; 24 total source locations in compressed evidence |
| `holo_reed_calls_v_start_done` | ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 55; ep1\quest\main_quests\q302\scenes\q302_08_call.scene / scene / 44; ep1\quest\main_quests\q303\phases\q303_07b_lobby_combat.questphase / h0 / 569; ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene / scene / 9584; 25 total source locations in compressed evidence |
| `mq001_done` | base\quest\minor_quests\mq001\mq001.questphase / h517 / 11; base\quest\minor_quests\mq001\phases\mq001_cleanup.questphase / h0 / 59; base\quest\minor_quests\mq001\scenes\test\mq001_chicken_test.scene / scene / 88; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 5; 4 total source locations in compressed evidence |
| `player_drunk` | base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene / scene / 4264; base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene / scene / 4267; base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene / scene / 4270; base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene / scene / 4273; 53 total source locations in compressed evidence |
| `q112_takemura_dead` | base\quest\main_quests\part1\q112\scenes\q112_000_setup.scene / scene / 285; base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene / scene / 534; base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene / scene / 1588; base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene / scene / 1615; 13 total source locations in compressed evidence |
| `q115_point_of_no_return` | base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase / h1024 / 46; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 239; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.questphase / h0 / 139; base\quest\main_quests\epilogue\q204\q204_reborn.quest / h0 / 7; 19 total source locations in compressed evidence |
| `q302_reed_interrogation_fail` | ep1\quest\main_quests\q302\scenes\q302_06_basketball.scene / scene / 1008; ep1\quest\main_quests\q302\test\q302_chicken_test.scene / scene / 413; 2 total source locations in compressed evidence |
| `q304_04e_heart_to_heart_done` | ep1\quest\main_quests\q304\scenes\q304_04e_alex_heart_to_heart.scene / scene / 257; 1 total source locations in compressed evidence |
| `q306_DEBUG_debugModeOn` | ep1\quest\main_quests\q306\q306.quest / h99 / 9; ep1\quest\test\q306_spaceport_performance.quest / h11 / 9; 2 total source locations in compressed evidence |
| `q306_finale_deal_done` | ep1\quest\main_quests\q306\scenes\q306_09_monorail.scene / scene / 2061; ep1\quest\main_quests\q306\scenes\q306_10_finale.scene / scene / 3376; ep1\quest\main_quests\q306\scenes\q306_10_finale.scene / scene / 3671; ep1\quest\main_quests\q306\scenes\q306_10_finale.scene / scene / 3949; 4 total source locations in compressed evidence |
| `q306_launchpad_retreated_scenario` | ep1\quest\main_quests\q306\scenes\q306_10_finale.scene / scene / 4287; 1 total source locations in compressed evidence |
| `wanted_level` | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.quest / h44 / 7; 1 total source locations in compressed evidence |

NodeRef uses: 240; TweakDB binding uses: 86. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene` | 7 / 26 | scnChangeIdleAnimEvent: 2; scnDialogLineEvent: 12; scnLookAtEvent: 3; scnPlaySkAnimEvent: 4; scneventsSocket: 5 |
| `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene` | 19 / 172 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 9; scnDialogLineEvent: 34; scnGameplayTransitionEvent: 4; scnIKEvent: 8; scnLookAtEvent: 5; scnOverridePhantomParamsEvent: 1; scnPlaySkAnimEvent: 51; scnUnmountEvent: 4; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 2; scneventsSetAnimFeatureEvent: 4; scneventsSocket: 46 |
| `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene` | 6 / 27 | scnChangeIdleAnimEvent: 5; scnDialogLineEvent: 11; scnLookAtEvent: 5; scnPlaySkAnimEvent: 4; scneventsSocket: 2 |
| `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene` | 68 / 634 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 15; scnDialogLineEvent: 122; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtAdvancedEvent: 13; scnLookAtEvent: 164; scnPlaySkAnimEvent: 112; scnPoseCorrectionEvent: 5; scnUnmountEvent: 3; scneventsAttachPropToPerformer: 33; scneventsAttachPropToWorld: 31; scneventsCameraParamsEvent: 2; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 106; scneventsVFXDurationEvent: 10; scneventsVFXEvent: 4 |
| `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene` | 47 / 312 | scnAudioEvent: 1; scnChangeIdleAnimEvent: 22; scnDialogLineEvent: 71; scnGameplayActionEvent: 2; scnLookAtAdvancedEvent: 6; scnLookAtEvent: 70; scnPlaySkAnimEvent: 77; scneventsCameraParamsEvent: 2; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 58; scneventsVFXEvent: 2 |
| `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene` | 14 / 38 | scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 14; scnPlaySkAnimEvent: 12; scneventsSocket: 11 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
