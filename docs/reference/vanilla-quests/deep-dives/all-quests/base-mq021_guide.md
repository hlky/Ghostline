# Fortunate Son

Journal: `quests/minor_quest/mq021_guide` · `MinorQuest` · hash `3933167984`.

**Coverage: journal-linked.** 56 exact journal-linked nodes in 7 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\quest\minor_quests\mq021\mq021.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Kidney failure. In the city, nothing that a stack of eddies and a few minutes won't solve. But in the Badlands… a death sentence. That is, unless a gentle soul somewhere feels like playin' guardian angel. Someone that'll get him the implant he needs before it's too late. Well, V? Think there's anyone out there like that? (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/04_meeting` |
| Meet with the hospital employee. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting` |
| Defeat the police. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/06_defend` |
| Take the briefcase with the implant. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/07_2_get_suitcase` |
| Confront the hospital employee. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` |
| Return to the Aldecaldos camp. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` |
| Kill the hospital employee. (Optional) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` |
| Talk to Bob. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` |
| Return to the camp in eight hours' time, when the operation is complete. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/10_ending_wait` |
| Read Bob's message. (Primary) | `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq021_quest_bugfixes.questphase / h37 / 16` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description`; `quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description` | 16:True → 1:In; 16:False → 7:Active; 11:False → 16:In |
| `mq021_quest_bugfixes.questphase / h131 / 4` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 0:Out → 4:In; 4:False → 1:In; 4:True → 7:In |
| `mq021_quest_bugfixes.questphase / h229 / 12` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/06_defend` | 6:False → 12:In; 12:True → 9:In |
| `mq021.questphase / h0 / 100` (Condition) | `quests/minor_quest/mq021_guide` | 114:Out → 100:In; 100:True → 101:Failed; 100:False → 111:In1 |
| `mq021.questphase / h0 / 101` (Journal) | `quests/minor_quest/mq021_guide` | 100:True → 101:Failed; 101:Out → 111:In1 |
| `mq021_combat_hospital.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/06_defend` | 27:Out → 4:Active; 4:Out → 26:In; 4:Out → 49:In; 4:Out → 45:In; 4:Out → 44:In; 4:Out → 53:In; 4:Out → 64:In |
| `mq021_combat_hospital.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/06_defend` | 42:Out → 13:Succeeded; 13:Out → 65:In |
| `mq021_combat_hospital.questphase / h0 / 27` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 0:Out → 27:Inactive; 27:Out → 4:Active |
| `mq021_hospital_meeting.questphase / h0 / 24` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/04_meeting` | 0:Out → 24:Active; 24:Out → 46:Active |
| `mq021_hospital_meeting.questphase / h0 / 28` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/04_meeting` | 31:Out → 28:Succeeded; 28:Out → 32:Active |
| `mq021_hospital_meeting.questphase / h0 / 32` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting` | 28:Out → 32:Active; 32:Out → 37:mq021_meeting |
| `mq021_hospital_meeting.questphase / h0 / 46` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description` | 46:Out → 6:In; 24:Out → 46:Active |
| `mq021_hospital_meeting.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 52:Out → 50:Active |
| `mq021_hospital_meeting.questphase / h0 / 52` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting` | 37:mq021_meeting_out → 52:Succeeded; 52:Out → 50:Active |
| `mq021_outcome.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 49:Out → 2:Active; 2:Out → 83:In; 2:Out → 103:In |
| `mq021_outcome.questphase / h0 / 33` (Journal) | `quests/minor_quest/mq021_guide` | 48:outcome_out → 33:Succeeded; 33:Out → 102:In |
| `mq021_outcome.questphase / h0 / 43` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` | 32:End1 → 43:Succeeded; 43:Out → 51:In |
| `mq021_outcome.questphase / h0 / 44` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` | 47:Out → 44:Active |
| `mq021_outcome.questphase / h0 / 45` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/10_ending_wait` | 51:Out → 45:Active; 45:Out → 81:In |
| `mq021_outcome.questphase / h0 / 47` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read` | 47:Out → 44:Active; 66:Out → 47:Succeeded |
| `mq021_outcome.questphase / h0 / 67` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/10_ending_wait` | 65:Out → 67:Succeeded; 67:Out → 68:Active |
| `mq021_outcome.questphase / h0 / 68` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read` | 68:Out → 66:In; 67:Out → 68:Active |
| `mq021_outcome.questphase / h0 / 115` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 115:Out → 106:In1; 116:Out → 115:Active |
| `mq021_outcome.questphase / h0 / 116` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/06_defend` | 116:Out → 115:Active; 117:Out → 116:Failed |
| `mq021_outcome.questphase / h386 / 3` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 0:Out → 3:In; 3:True → 4:Succeeded; 3:False → 5:In |
| `mq021_outcome.questphase / h386 / 4` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 3:True → 4:Succeeded; 4:Out → 5:In |
| `mq021_outcome.questphase / h386 / 5` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 3:False → 5:In; 4:Out → 5:In; 5:False → 6:Active |
| `mq021_outcome.questphase / h386 / 6` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 5:False → 6:Active |
| `mq021_02_hospital_meeting.scene / scene / 93` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 93:0:0 → 99:666:1; 93:0:0 → 105:0:1; 93:0:0 → 463:0:0; 94:0:0 → 93:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 94` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 40:0:0 → 94:0:3; 94:0:0 → 93:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 101` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 550:0:0 → 101:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 108` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 113:0:0 → 108:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 118` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 118:0:0 → 124:0:1; 118:0:0 → 466:0:0; 119:0:0 → 118:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 119` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 71:0:0 → 119:0:3; 119:0:0 → 118:0:1; 119:0:0 → 269:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 122` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 556:0:0 → 122:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 125` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor` | 126:0:0 → 125:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 139` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 35:0:0 → 139:0:3; 139:0:0 → 265:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 144` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 55:0:0 → 144:0:3; 144:0:0 → 273:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 250` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting` | 9:0:0 → 250:0:2; 250:0:0 → 253:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 253` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_2_get_suitcase` | 250:0:0 → 253:0:1; 253:0:0 → 256:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 254` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_2_get_suitcase` | 254:0:0 → 280:0:1; 255:0:0 → 254:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 261` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 261:0:0 → 61:0:0; 463:0:0 → 261:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 265` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 139:0:0 → 265:0:1; 265:0:0 → 346:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 269` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 119:0:0 → 269:0:1; 269:0:0 → 61:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 273` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 144:0:0 → 273:0:1; 273:0:0 → 61:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 280` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting` | 254:0:0 → 280:0:1; 280:0:0 → 249:0:0; 280:0:0 → 531:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 349` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 328:2:0 → 349:0:2; 349:0:0 → 351:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 351` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 349:0:0 → 351:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 355` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor` | 42:0:0 → 355:0:3; 355:0:0 → 356:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_02_hospital_meeting.scene / scene / 356` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 355:0:0 → 356:0:1; 356:0:0 → 61:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_03_ending.scene / scene / 35` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/08_outcome` | 35:0:0 → 36:0:1; 53:0:1 → 35:0:3; 54:0:0 → 35:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_03_ending.scene / scene / 36` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` | 35:0:0 → 36:0:1; 36:0:0 → 99:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_03_ending.scene / scene / 39` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` | 45:0:0 → 39:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_03_ending.scene / scene / 40` (Journal) | `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read` | 40:0:0 → 45:0:1; 41:0:0 → 40:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq021_03_ending.scene / scene / 41` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read` | 6:0:0 → 41:0:1; 41:0:0 → 40:0:2; 41:0:1 → 45:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq021_03_ending.scene / scene / 45` (Condition) | `quests/minor_quest/mq021_guide/mq021_guide/09_ending` | 40:0:0 → 45:0:1; 41:0:1 → 45:0:1; 45:0:0 → 39:0:1; input mappings: 0:0=CutDestination, 0:1=In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq021.questphase / h0 / 96` | `base\quest\minor_quests\mq021\phases\mq021_briefing.questphase` | 96:sq027_failed → 114:Inactive; 115:False → 96:In1; 96:Out1 → 103:In |
| `mq021.questphase / h0 / 97` | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` | 103:Out → 97:In1; 107:Out → 97:In1; 97:Out1 → 98:In1 |
| `mq021.questphase / h0 / 98` | `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` | 97:Out1 → 98:In1; 98:combat_escaped → 99:Skip_combat; 98:Out1 → 99:In1 |
| `mq021.questphase / h0 / 99` | `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` | 98:combat_escaped → 99:Skip_combat; 98:Out1 → 99:In1; 99:Out1 → 110:In; 108:Out → 99:In1; 109:Out → 99:ending_in |
| `mq021_briefing.questphase / h0 / 6` | `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene`; `#mq021_01_sm_briefing` | 27:Out → 6:mq021_01_mood; 6:mq_yes → 12:In; 6:mq_yes → 21:In |
| `mq021_combat_hospital.questphase / h0 / 2` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`; `#mq021_02_sm_hospital_meeting` | 26:Out → 2:combat_comment |
| `mq021_hospital_meeting.questphase / h0 / 37` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`; `#mq021_02_sm_hospital_meeting` | 37:mq021_meeting_out → 8:In; 32:Out → 37:mq021_meeting; 37:mq021_meeting_out → 52:Succeeded; 37:mq021_meeting_out → 65:In; 37:mq021_meeting_out_term → 60:In1 |
| `mq021_hospital_meeting.questphase / h0 / 39` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`; `#mq021_02_sm_hospital_meeting` | 51:Out → 39:mq021_meeting_interrupted |
| `mq021_outcome.questphase / h0 / 8` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`; `#mq021_02_sm_hospital_meeting` | 85:Out → 8:mq021_confrontation; 8:scene_cut → 106:In2; 8:scene_cut → 129:In; 8:mq021_confrontation_out → 106:In3 |
| `mq021_outcome.questphase / h0 / 32` | `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene`; `#mq021_03_sm_ending` | 91:Out → 32:Start1; 32:End1 → 43:Succeeded |
| `mq021_outcome.questphase / h0 / 48` | `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene`; `#mq021_03_sm_ending` | 48:outcome_out → 33:Succeeded; 92:Out → 48:outcome |
| `mq021_outcome.questphase / h386 / 2` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`; `#mq021_02_sm_hospital_meeting` | 0:Out → 2:mq021_hospital_done_comment |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 40 | `mq021_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 40:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 8 | `mq021.questphase` | 56: PauseCondition: sq027_done; 56:Out → 8:In1 |
| `base\quest\minor_quests\mq021\mq021.quest` / h0 / 6 | `mq021.questphase` | 21: UIManager; 14: Phase; 14: Phase; 14: Phase; 6:Out1 → 3:In; 21:Out → 6:In1; 14:hospital_out → 6:hospital_in; 14:post_combat_out → 6:post_combat_in; 14:ending_out → 6:ending_in |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 96 | `mq021_briefing.questphase` | 115: Condition: sq027_camp_abandoned; 96:sq027_failed → 114:Inactive; 115:False → 96:In1; 96:Out1 → 103:In |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 98 | `mq021_combat_hospital.questphase` | 97: Phase: mq021_hospital_meeting.questphase; 97:Out1 → 98:In1; 98:combat_escaped → 99:Skip_combat; 98:Out1 → 99:In1 |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 97 | `mq021_hospital_meeting.questphase` | 103: FactsDBManager: mq021_active; 107: Input; 103:Out → 97:In1; 107:Out → 97:In1; 97:Out1 → 98:In1 |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 99 | `mq021_outcome.questphase` | 98: Phase: mq021_combat_hospital.questphase; 98: Phase: mq021_combat_hospital.questphase; 108: Input; 109: Input; 98:combat_escaped → 99:Skip_combat; 98:Out1 → 99:In1; 99:Out1 → 110:In; 108:Out → 99:In1; 109:Out → 99:ending_in |
| `base\quest\minor_quests\mq021\phases\mq021_briefing.questphase` / h0 / 6 | `mq021_01_briefing.scene` | 27: PauseCondition: #mq021_tr_hook; 27:Out → 6:mq021_01_mood; 6:mq_yes → 12:In; 6:mq_yes → 21:In |
| `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` / h0 / 2 | `mq021_02_hospital_meeting.scene` | 26: PauseCondition: {"seconds": 2}; 26:Out → 2:combat_comment |
| `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 37 | `mq021_02_hospital_meeting.scene` | 32: Journal; 37:mq021_meeting_out → 8:In; 32:Out → 37:mq021_meeting; 37:mq021_meeting_out → 52:Succeeded; 37:mq021_meeting_out → 65:In; 37:mq021_meeting_out_term → 60:In1 |
| `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 39 | `mq021_02_hospital_meeting.scene` | 51: PauseCondition: {"seconds": 2}; 51:Out → 39:mq021_meeting_interrupted |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` / h0 / 8 | `mq021_02_hospital_meeting.scene` | 85: PauseCondition; 85:Out → 8:mq021_confrontation; 8:scene_cut → 106:In2; 8:scene_cut → 129:In; 8:mq021_confrontation_out → 106:In3 |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` / h386 / 2 | `mq021_02_hospital_meeting.scene` | 0: Input; 0:Out → 2:mq021_hospital_done_comment |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` / h0 / 32 | `mq021_03_ending.scene` | 91: PauseCondition: #mq021_tr_ending_scene; 91:Out → 32:Start1; 32:End1 → 43:Succeeded |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` / h0 / 48 | `mq021_03_ending.scene` | 92: PauseCondition: #mq021_tr_hook; 48:outcome_out → 33:Succeeded; 92:Out → 48:outcome |
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
| `mq021_01_briefing.scene` | mq021_01_mood → mq_yes | Bob; Wife; Scooter; Player; 23 nodes / 25 edges |
| `mq021_02_hospital_meeting.scene` | mq021_meeting, combat_comment, mq021_meeting_interrupted, mq021_confrontation, mq021_hospital_done_comment → mq021_meeting_out, combat_comment_out, mq021_meeting_interrupted_out, mq021_confrontation_out, mq021_meeting_out_term, scene_cut, mq021_hospital_done_comment_out | Doctor; Security_01; van; Player; 119 nodes / 127 edges |
| `mq021_03_ending.scene` | outcome, Start1 → outcome_out, End2, End1 | Bob; Player; 31 nodes / 33 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq021_01_briefing.scene / n4 / 0` | What's going on? (``) | No option-level predicate stored | 0:0 → 11:0:0; 0:0 → 74:0:0 |
| `mq021_01_briefing.scene / n13 / 0` | I'm sure you can find one in the city. (``) | No option-level predicate stored | 0:0 → 18:0:0 |
| `mq021_01_briefing.scene / n13 / 1` | Did Raffen Shiv shoot him? (``) | No option-level predicate stored | 0:1 → 20:0:0 |
| `mq021_01_briefing.scene / n23 / 0` | You can count on me. (``) | No option-level predicate stored | 0:0 → 25:0:0 |
| `mq021_01_briefing.scene / n23 / 1` | I'm sorry, but I can't. (``) | No option-level predicate stored | 0:1 → 26:0:0 |
| `mq021_01_briefing.scene / n34 / 0` | I'll help Jake. (``) | No option-level predicate stored | 0:0 → 40:0:0 |
| `mq021_02_hospital_meeting.scene / n33 / 0` | Won't let you get away with this. (`let_kill`) | No option-level predicate stored | 0:0 → 301:0:1 |
| `mq021_02_hospital_meeting.scene / n33 / 1` | I'll spare you this time. (`dont_kill`) | No option-level predicate stored | 0:1 → 35:0:0 |
| `mq021_02_hospital_meeting.scene / n33 / 2` | Did anyone tamper with the implant? (`net`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125420028803", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 44:0:0 |
| `mq021_02_hospital_meeting.scene / n49 / 0` | You'll pay for this, motherfucker. (`kill`) | No option-level predicate stored | 0:0 → 304:0:1 |
| `mq021_02_hospital_meeting.scene / n49 / 1` | Get out of my sight. (`dont`) | No option-level predicate stored | 0:1 → 55:0:0 |
| `mq021_02_hospital_meeting.scene / n80 / 0` | [Take shard without a word] (`silent`) | No option-level predicate stored | 0:0 → 78:0:0 |
| `mq021_02_hospital_meeting.scene / n80 / 1` | [Take shard] Thanks for your honesty. (`thanks`) | No option-level predicate stored | 0:1 → 84:0:0 |
| `mq021_02_hospital_meeting.scene / n244 / 0` | [Take shard] (`get_chip`) | No option-level predicate stored | 0:0 → 246:0:0 |
| `mq021_02_hospital_meeting.scene / n293 / 0` | Sure did. (`hello`) | No option-level predicate stored | 0:0 → 9:0:0 |
| `mq021_02_hospital_meeting.scene / n319 / 0` | Why shouldn't I? Talk. Now. (`start`) | No option-level predicate stored | 0:0 → 29:0:0 |
| `mq021_03_ending.scene / n6 / 0` | How's Jake doing? (``) | No option-level predicate stored | 0:0 → 28:0:0; 0:0 → 41:0:1; 0:0 → 51:0:1 |
| `mq021_03_ending.scene / n18 / 0` | [Set down] I've got the implant. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq021_happy_ending", "comparisonType": "Equal"}}} | 0:0 → 20:0:0 |
| `mq021_03_ending.scene / n18 / 1` | [Set down] I've got the implant... but it's infected. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq021_happy_ending"}}} | 0:1 → 25:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CP77-64809` | mq021_quest_bugfixes.questphase / h229 / 5 | mq021_quest_bugfixes.questphase / h229 / 4 |
| `CYB-12345` | mq021_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-643886` | mq021_quest_bugfixes.questphase / h37 / 4 | mq021_quest_bugfixes.questphase / h37 / 2 |
| `CYB-658203` | mq021_quest_bugfixes.questphase / h174 / 2 | mq021_quest_bugfixes.questphase / h174 / 3 |
| `bob_default_on` | mq021.questphase / h98 / 7; mq021_briefing.questphase / h0 / 14 | No reader in selected context |
| `mq021_active` | mq021.questphase / h0 / 103; mq021.questphase / h0 / 104 | No reader in selected context |
| `mq021_bob_ending_approached` | mq021_03_ending.scene / scene / 51 | mq021_outcome.questphase / h0 / 80 |
| `mq021_done` | mq021.questphase / h0 / 105 | mq021_quest_bugfixes.questphase / h174 / 5; mq021_quest_bugfixes.questphase / h229 / 6 |
| `mq021_happy_ending` | mq021_02_hospital_meeting.scene / scene / 42; mq021_02_hospital_meeting.scene / scene / 45 | mq021_03_ending.scene / scene / 18; mq021_03_ending.scene / scene / 4; mq021_03_ending.scene / scene / 53; mq021_outcome.questphase / h0 / 62 |
| `mq021_hospital_done` | mq021_02_hospital_meeting.scene / scene / 501 | mq021_02_hospital_meeting.scene / scene / 505 |
| `mq021_unlocked` | mq021_01_briefing.scene / scene / 8 | No reader in selected context |
| `q115_point_of_no_return` | Producer outside selected context | mq021.questphase / h0 / 95; mq021_quest_bugfixes.questphase / h37 / 19 |
| `sq027_active` | Producer outside selected context | mq021.questphase / h0 / 90 |
| `sq027_camp_abandoned` | Producer outside selected context | mq021.questphase / h0 / 115; mq021_briefing.questphase / h0 / 25; mq021_quest_bugfixes.questphase / h37 / 11 |
| `sq027_done` | Producer outside selected context | mq021_quest_bugfixes.questphase / h37 / 17 |
| `travelling_merchant_lives` | Producer outside selected context | mq021_quest_bugfixes.questphase / h0 / 23 |

## Exact gates, joins and cancellation

<details><summary>67 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq021_quest_bugfixes.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 24:Out → 23:In |
| `mq021_quest_bugfixes.questphase / h37 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-643886"}}}` | 0:Out → 2:In; 2:True → 1:In; 2:False → 4:In |
| `mq021_quest_bugfixes.questphase / h37 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"points_of_interest/minor_quests/mq021_guide","fileEntryIndex":1,"className":"gameJournalPointOfInterestMappin"},"state":"Active"}}}` | 8:True → 1:In; 17:False → 8:In; 8:False → 11:In |
| `mq021_quest_bugfixes.questphase / h37 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned"}}}` | 11:True → 1:In; 8:False → 11:In; 11:False → 16:In |
| `mq021_quest_bugfixes.questphase / h37 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Succeeded"}}]}}` | 16:True → 1:In; 16:False → 7:Active; 11:False → 16:In |
| `mq021_quest_bugfixes.questphase / h37 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_done","comparisonType":"Equal"}}}` | 17:True → 1:In; 17:False → 8:In; 19:False → 17:In |
| `mq021_quest_bugfixes.questphase / h37 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 19:True → 1:In; 4:Out → 19:In; 19:False → 17:In |
| `mq021_quest_bugfixes.questphase / h131 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/08_outcome","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 4:In; 4:False → 1:In; 4:True → 7:In |
| `mq021_quest_bugfixes.questphase / h174 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-658203"}}}` | 3:True → 1:In; 2:Out → 3:In; 3:False → 5:In |
| `mq021_quest_bugfixes.questphase / h174 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_done"}}}` | 5:False → 1:In; 3:False → 5:In; 5:True → 7:In |
| `mq021_quest_bugfixes.questphase / h174 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/bob/mq021/mq021_ending_message","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 7:True → 1:In; 5:True → 7:In; 7:False → 9:Inactive |
| `mq021_quest_bugfixes.questphase / h229 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-64809"}}}` | 0:Out → 4:In; 4:False → 5:In |
| `mq021_quest_bugfixes.questphase / h229 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_done"}}}` | 6:True → 2:In; 5:Out → 6:In; 6:False → 12:In |
| `mq021_quest_bugfixes.questphase / h229 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_hospital_escape_area"}}` | 9:Out → 2:In; 12:True → 9:In |
| `mq021_quest_bugfixes.questphase / h229 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/06_defend","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 6:False → 12:In; 12:True → 9:In |
| `mq021.questphase / h0 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_active","comparisonType":"Equal"}}}` | 2:Out → 90:In; 90:Out → 115:In |
| `mq021.questphase / h0 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 2:Out → 95:In; 95:Out → 114:Inactive |
| `mq021.questphase / h0 / 100` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 114:Out → 100:In; 100:True → 101:Failed; 100:False → 111:In1 |
| `mq021.questphase / h0 / 115` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned"}}}` | 90:Out → 115:In; 115:False → 96:In1; 115:True → 114:Inactive |
| `mq021.questphase / h98 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#bob"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 8:Out → 6:In; 6:Out → 11:In |
| `mq021.questphase / h202 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#bob"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 6:Out → 4:In; 10:Out → 6:In |
| `mq021_briefing.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_nomads"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 4:Out → 3:In; 3:Out → 5:In |
| `mq021_briefing.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#bob"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 5:In; 5:Out → 28:In |
| `mq021_briefing.questphase / h0 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_nomad_camp_big"}}` | 6:mq_yes → 21:In; 21:Out → 19:In |
| `mq021_briefing.questphase / h0 / 25` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq027_camp_abandoned"}}}` | 25:True → 24:In; 28:Out → 25:In |
| `mq021_briefing.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_hook"}}` | 27:Out → 6:mq021_01_mood; 28:Out → 27:In |
| `mq021_combat_hospital.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_security","names":["sec_01","sec_02","sec_03","sec_04","sec_05","sec_06","sec_07"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 64:Out → 12:In; 12:Out → 42:In |
| `mq021_combat_hospital.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 26:Out → 2:combat_comment; 4:Out → 26:In; 26:Out → 41:In |
| `mq021_combat_hospital.questphase / h0 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 26:Out → 41:In; 41:Out → 43:In |
| `mq021_combat_hospital.questphase / h0 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 49:In; 49:Out → 23:In; 49:Out → 29:In; 49:Out → 30:In; 49:Out → 31:In; 49:Out → 32:In |
| `mq021_combat_hospital.questphase / h0 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_hospital_escape_area"}}` | 4:Out → 53:In; 53:Out → 54:In |
| `mq021_hospital_meeting.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 6:Out → 26:In; 26:Out → 47:In; 26:Out → 67:In; 26:Out → 72:In |
| `mq021_hospital_meeting.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_meeting_reached"}}` | 27:Out → 31:In; 31:Out → 28:Succeeded; 31:Out → 55:In; 31:Out → 69:In |
| `mq021_hospital_meeting.questphase / h0 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 51:Out → 39:mq021_meeting_interrupted; 68:Out → 51:In |
| `mq021_hospital_meeting.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_hospital_enemy_area"}}` | 31:Out → 55:In; 58:Out → 55:In; 55:Out → 57:In |
| `mq021_hospital_meeting.questphase / h0 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_hospital_enemy_area"}}` | 57:Out → 56:In; 56:Out → 58:In |
| `mq021_hospital_meeting.questphase / h0 / 61` | `questLogicalAndNodeDefinition` `{}` | 61:Out1 → 54:In; 59:Out → 61:In1; 60:Out1 → 61:In2 |
| `mq021_outcome.questphase / h0 / 62` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_happy_ending"}}}` | 74:Out → 62:In; 62:True → 88:In; 62:False → 63:In |
| `mq021_outcome.questphase / h0 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/bob/mq021/mq021_ending_message","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 66:Out → 47:Succeeded; 79:CutSource → 66:CutDestination; 68:Out → 66:In |
| `mq021_outcome.questphase / h0 / 79` | `questCutControlNodeDefinition` `{}` | 79:CutSource → 66:CutDestination; 108:Out → 79:In |
| `mq021_outcome.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_bob_ending_approached"}}}` | 65:Out → 80:In; 80:Out → 108:Inactive |
| `mq021_outcome.questphase / h0 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 85:Out → 8:mq021_confrontation; 90:Out → 85:In |
| `mq021_outcome.questphase / h0 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_ending_scene"}}` | 91:Out → 32:Start1; 73:Out → 91:In |
| `mq021_outcome.questphase / h0 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_hook"}}` | 92:Out → 48:outcome; 65:Out → 92:In |
| `mq021_outcome.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":8}}}` | 81:Out → 93:In; 93:Out → 105:In |
| `mq021_outcome.questphase / h0 / 94` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq021_tr_hospital_enemy_area"}}` | 49:Out → 94:In; 97:Out → 94:In; 94:Out → 96:In |
| `mq021_outcome.questphase / h0 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_hospital_enemy_area"}}` | 96:Out → 95:In; 95:Out → 97:In |
| `mq021_outcome.questphase / h0 / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_nomad_camp_big"}}` | 104:Out → 75:In; 105:Out → 104:In |
| `mq021_outcome.questphase / h0 / 106` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 8:scene_cut → 106:In2; 8:mq021_confrontation_out → 106:In3; 106:Out1 → 50:In; 115:Out → 106:In1 |
| `mq021_outcome.questphase / h0 / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_hospital_escape_area"}}` | 50:Out → 132:In; 132:Out → 131:In |
| `mq021_outcome.questphase / h386 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 3:In; 3:True → 4:Succeeded; 3:False → 5:In |
| `mq021_outcome.questphase / h386 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:False → 5:In; 4:Out → 5:In; 5:False → 6:Active |
| `mq021_01_briefing.scene / scene / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 26:0:0 → 43:0:1; 43:0:0 → 34:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 93:0:0 → 105:0:1; 105:0:0 → 149:0:0; 550:0:0 → 105:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 118:0:0 → 124:0:1; 124:0:0 → 154:0:0; 556:0:0 → 124:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 257` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134799360879","comparisonType":"Greater"}}}` | 256:0:0 → 257:0:1; 257:0:0 → 255:0:1 |
| `mq021_02_hospital_meeting.scene / scene / 346` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0}}}}` | 265:0:0 → 346:0:1; 346:0:0 → 328:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 505` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_hospital_done"}}}` | 481:0:0 → 505:0:1; 505:0:1 → 480:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 531` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 280:0:0 → 531:0:1; 531:0:0 → 8:0:0 |
| `mq021_02_hospital_meeting.scene / scene / 543` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.InvulnerableFinisherWorkspot"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.Grappled"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterReaction_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"isAnyReaction":true}}]}}` | 27:0:0 → 543:0:1; 543:0:0 → 547:0:1 |
| `mq021_02_hospital_meeting.scene / scene / 550` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.InvulnerableFinisherWorkspot"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.Grappled"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterReaction_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"isAnyReaction":true}}]}}` | 99:666:0 → 550:0:1; 113:1:0 → 550:0:0; 550:0:0 → 101:0:3; 550:0:0 → 105:0:0; 550:0:0 → 149:1:0 |
| `mq021_02_hospital_meeting.scene / scene / 556` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.InvulnerableFinisherWorkspot"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"statusEffectID":"BaseStatusEffect.Grappled"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterReaction_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#mq021_com_doctor","names":["doctor"]},"isAnyReaction":true}}]}}` | 121:666:0 → 556:0:1; 126:1:0 → 556:0:0; 556:0:0 → 122:0:3; 556:0:0 → 124:0:0; 556:0:0 → 154:1:0 |
| `mq021_03_ending.scene / scene / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_happy_ending"}}}` | 4:0:0 → 59:0:1; 4:0:1 → 12:0:0; 28:0:0 → 4:0:1 |
| `mq021_03_ending.scene / scene / 41` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/11_ending_read","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 6:0:0 → 41:0:1; 41:0:0 → 40:0:2; 41:0:1 → 45:0:1 |
| `mq021_03_ending.scene / scene / 45` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq021_guide/mq021_guide/09_ending","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 40:0:0 → 45:0:1; 41:0:1 → 45:0:1; 45:0:0 → 39:0:1 |
| `mq021_03_ending.scene / scene / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq021_happy_ending"}}}` | 33:666:0 → 53:0:1; 53:0:0 → 54:0:1; 53:0:1 → 35:0:3 |
| `mq021_03_ending.scene / scene / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq021_tr_nomad_camp_big"}}` | 22:0:0 → 103:0:1; 103:0:0 → 104:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq021_briefing.questphase / h0 / 3; mq021_briefing.questphase / h0 / 5; mq021_hospital_meeting.questphase / h0 / 26 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq021_02_hospital_meeting.scene / scene / 513 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq021_outcome.questphase / h0 / 65 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | mq021.questphase / h0 / 112; mq021_briefing.questphase / h0 / 12; mq021_hospital_meeting.questphase / h0 / 69; mq021_hospital_meeting.questphase / h0 / 70; +4 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq021_01_briefing.scene / scene / 13; mq021_01_briefing.scene / scene / 23; mq021_01_briefing.scene / scene / 34; mq021_01_briefing.scene / scene / 4; +8 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq021_combat_hospital.questphase / h0 / 23; mq021_combat_hospital.questphase / h0 / 29; mq021_combat_hospital.questphase / h0 / 30; mq021_combat_hospital.questphase / h0 / 31; +3 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq021.questphase / h202 / 2; mq021.questphase / h202 / 3; mq021.questphase / h202 / 4; mq021.questphase / h202 / 9; +20 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq021.questphase / h0 / 115; mq021.questphase / h0 / 90; mq021.questphase / h0 / 95; mq021_02_hospital_meeting.scene / scene / 505; +15 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq021.questphase / h0 / 113; mq021_hospital_meeting.questphase / h0 / 57; mq021_hospital_meeting.questphase / h0 / 58; mq021_hospital_meeting.questphase / h0 / 59; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq021_combat_hospital.questphase / h0 / 61; mq021_combat_hospital.questphase / h0 / 67; mq021_hospital_meeting.questphase / h0 / 72; mq021_outcome.questphase / h0 / 130 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `elapsed_time` | mq021_outcome.questphase / h0 / 93 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq021_02_hospital_meeting.scene / scene / 257 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | mq021_outcome.questphase / h0 / 66; mq021_quest_bugfixes.questphase / h174 / 7 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | mq021.questphase / h0 / 101; mq021.questphase / h0 / 114; mq021_01_briefing.scene / scene / 82; mq021_02_hospital_meeting.scene / scene / 101; +50 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq021_hospital_meeting.questphase / h0 / 61 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq021.questphase / h0 / 103; mq021.questphase / h0 / 104; mq021.questphase / h0 / 105; mq021.questphase / h98 / 7; +10 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq021_outcome.questphase / h0 / 106 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq021_01_briefing.scene / scene / 43; mq021_02_hospital_meeting.scene / scene / 105; mq021_02_hospital_meeting.scene / scene / 124; mq021_02_hospital_meeting.scene / scene / 531; +4 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq021_outcome.questphase / h0 / 79 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq021.questphase / h0 / 110 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq021_briefing.questphase / h0 / 6; mq021_combat_hospital.questphase / h0 / 2; mq021_hospital_meeting.questphase / h0 / 37; mq021_hospital_meeting.questphase / h0 / 39; +4 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq021_03_ending.scene / scene / 103; mq021_briefing.questphase / h0 / 21; mq021_briefing.questphase / h0 / 27; mq021_combat_hospital.questphase / h0 / 53; +10 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq021_02_hospital_meeting.scene / scene / 543; mq021_02_hospital_meeting.scene / scene / 550; mq021_02_hospital_meeting.scene / scene / 556; mq021_combat_hospital.questphase / h0 / 12 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq021_combat_hospital.questphase / h0 / 44; mq021_combat_hospital.questphase / h0 / 45; mq021_combat_hospital.questphase / h0 / 46; mq021_combat_hospital.questphase / h0 / 47; +2 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq021_01_briefing.scene / scene / 49; mq021_01_briefing.scene / scene / 51; mq021_01_briefing.scene / scene / 53; mq021_01_briefing.scene / scene / 55; +26 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq021.questphase / h202 / 10; mq021.questphase / h202 / 8; mq021.questphase / h98 / 10; mq021_briefing.questphase / h0 / 18; +2 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` | repair; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\mq021.questphase` | content candidate; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\phases\mq021_briefing.questphase` | content candidate; forward dependency | `base-mq021` |
| `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` | content candidate; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` | content candidate; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` | content candidate; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` | content candidate; forward dependency | `base-mq021` |
| `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` | content candidate; journal anchor | `base-mq021` |
| `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene` | content candidate; journal anchor | `base-mq021` |

Evidence shards for this dossier (including parent context): [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

226 repeated typed/socket path signatures in this selected graph context; 45 distinct direct resource identities; 8 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 20 -> 11 -> 21 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `c8705a8da51824b73252` | `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h174 / 0 -> 2 -> 3 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 4 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 31 -> 28 -> 32 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `40aa0dddb5f517500320` | `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h37 / 4 -> 19 -> 17 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; False -> In |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 19 -> 24 -> 23 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `a53561b4c002bc02b58a` | `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` / h0 / 27 -> 4 -> 53 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> Active; Out -> In |
| `f1e68c36026b90dd9a9b` | `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` / h0 / 57 -> 61 -> 67 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questEventManagerNodeDefinition -> questEventManagerNodeDefinition; Out -> In; Out -> In |
| `3fe0ae98a8cf5496b004` | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 58 -> 55 -> 57 | questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]; Out -> In; Out -> In |
| `eb252b7e42db30cea85d` | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 55 -> 57 -> 56 | questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `178ff9eba50354aed786` | `base\quest\minor_quests\mq021\mq021.questphase` / h98 / 0 -> 2 -> 3 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 320 -> 319 -> 29 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 14 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 17 | `h131` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 20 | `h174` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` / h0 / 22 | `h229` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 102 | `h98` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq021\mq021.questphase` / h0 / 111 | `h202` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` / h0 / 125 | `h386` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | base\quest\minor_quests\mq021\mq021.quest |
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
| `base\animations\npc\gameplay\man_average\gang\unarmed\ma_gang_unarmed_locomotion_combat.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male__sit_chair_lean270__rh_on_knee__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_up__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_on_chin__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_up__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__kneel__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_fat\interactive_scene\generic_male_fat__lie_bed_0__sleep__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq021\body\mq021__player_female__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq021\body\mq021__player_male__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\synced__passing_item_to_player__male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\synced__passing_item_to_player__player.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq021\phases\mq021_briefing.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_01_briefing\bob.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_01_briefing\gang_ald_f_02_nat_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_01_briefing\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_02_hospital_meeting\civ_high_m_16_chn_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_02_hospital_meeting\civ_mid_m_30_enus_50.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_02_hospital_meeting\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_03_ending\bob.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\lipsync\en\mq021_03_ending\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair__sit_around__06.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__kneel_ground__cry__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__scared__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__06.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_arms_crossed__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_item__give__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\player\bed\player__lie_bed_lean_back__sleep__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `bob_default_on` | base\quest\main_quests\part1\q114\phases\debug\q114_debug_setup.questphase / h75 / 5; base\quest\main_quests\part1\q114\phases\q114_new_camp.questphase / h201 / 5; base\quest\side_quests\sq004\phases\sq004_05_farm.questphase / h122 / 64; base\quest\side_quests\sq004\sq004_riders_on_the_storm.questphase / h1164 / 3; 18 total source locations in compressed evidence |
| `mq021_happy_ending` | base\quest\minor_quests\mq021\test\mq021_00_chicken.scene / scene / 51; base\quest\main_quests\part1\q114\scenes\test\q114_00_setup.scene / scene / 769; base\quest\main_quests\part1\q114\scenes\test\q114_00_setup.scene / scene / 873; 3 total source locations in compressed evidence |
| `q115_point_of_no_return` | base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase / h1024 / 46; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 239; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.questphase / h0 / 139; base\quest\main_quests\epilogue\q204\q204_reborn.quest / h0 / 7; 19 total source locations in compressed evidence |
| `sq027_active` | base\quest\side_quests\sq027\phases\sq027_01_nomad_camp.questphase / h0 / 85; base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest / h0 / 44; base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h173 / 77; 3 total source locations in compressed evidence |
| `sq027_camp_abandoned` | base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h491 / 4; base\quest\side_quests\sq027\sq027_queen_of_the_highway.questphase / h578 / 4; 2 total source locations in compressed evidence |
| `sq027_done` | base\quest\minor_quests\mq021\mq021.quest / h70 / 11; base\quest\minor_quests\mq026\test\mq026_00_chickentest.scene / scene / 239; base\quest\main_quests\part1\q115\test\q115_00_chickentest.scene / scene / 577; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 185; 6 total source locations in compressed evidence |

NodeRef uses: 191; TweakDB binding uses: 42. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` | 7 / 50 | scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 24; scnLookAtEvent: 6; scnPlaySkAnimEvent: 13; scneventsSocket: 6 |
| `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` | 20 / 140 | scnChangeIdleAnimEvent: 4; scnDialogLineEvent: 37; scnGameplayTransitionEvent: 4; scnIKEvent: 8; scnLookAtEvent: 6; scnPlaySkAnimEvent: 33; scnUnmountEvent: 4; scneventsAttachPropToNode: 3; scneventsAttachPropToPerformer: 5; scneventsEquipItemToPerformer: 1; scneventsSetAnimFeatureEvent: 4; scneventsSocket: 30; scneventsUnequipItemFromPerformerByItem: 1 |
| `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene` | 6 / 39 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 2; scnDialogLineEvent: 14; scnLookAtEvent: 6; scnPlaySkAnimEvent: 10; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 2; scneventsSocket: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
