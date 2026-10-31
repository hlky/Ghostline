# Fortunate Son

Journal: `quests/minor_quest/mq021_guide` · `MinorQuest` · hash `3933167984`.

**Coverage: journal-linked.** 56 exact journal-linked nodes in 7 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

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
| `base\quest\minor_quests\minorquests.questphase` / h0 / 8 | `mq021.questphase` | 56: PauseCondition: sq027_done; 56:Out → 8:In1 |
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
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

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

| Fact | Writers in context | Readers/conditions in context |
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
| `choice_gate` | mq021_01_briefing.scene / scene / 13; mq021_01_briefing.scene / scene / 23; mq021_01_briefing.scene / scene / 34; mq021_01_briefing.scene / scene / 4; +8 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq021_combat_hospital.questphase / h0 / 23; mq021_combat_hospital.questphase / h0 / 29; mq021_combat_hospital.questphase / h0 / 30; mq021_combat_hospital.questphase / h0 / 31; +3 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq021.questphase / h202 / 2; mq021.questphase / h202 / 3; mq021.questphase / h202 / 4; mq021.questphase / h202 / 9; +20 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq021.questphase / h0 / 115; mq021.questphase / h0 / 90; mq021.questphase / h0 / 95; mq021_02_hospital_meeting.scene / scene / 505; +15 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq021.questphase / h0 / 113; mq021_hospital_meeting.questphase / h0 / 57; mq021_hospital_meeting.questphase / h0 / 58; mq021_hospital_meeting.questphase / h0 / 59; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `elapsed_time` | mq021_outcome.questphase / h0 / 93 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq021_02_hospital_meeting.scene / scene / 257 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | mq021_outcome.questphase / h0 / 66; mq021_quest_bugfixes.questphase / h174 / 7 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `parallel_join` | mq021_hospital_meeting.questphase / h0 / 61 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq021.questphase / h0 / 103; mq021.questphase / h0 / 104; mq021.questphase / h0 / 105; mq021.questphase / h98 / 7; +10 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq021_outcome.questphase / h0 / 106 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq021_01_briefing.scene / scene / 43; mq021_02_hospital_meeting.scene / scene / 105; mq021_02_hospital_meeting.scene / scene / 124; mq021_02_hospital_meeting.scene / scene / 531; +4 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq021_outcome.questphase / h0 / 79 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq021.questphase / h0 / 110 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq021_briefing.questphase / h0 / 6; mq021_combat_hospital.questphase / h0 / 2; mq021_hospital_meeting.questphase / h0 / 37; mq021_hospital_meeting.questphase / h0 / 39; +4 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
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

Evidence shards for this dossier (including parent context): [base-mq021](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq021.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
