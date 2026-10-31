# Gig: Until Death Do Us Part

Journal: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` · `StreetStory` · hash `885903102`.

Journal premise: Gig type: Thievery\nObjective: Steal the shard with Emilio Gutierrez's depository receipts\nLocation: Apartment on Palm St.\nDetails:\n\nWould you like to hear about my fourth husband? He was very lazy, gullible, and filthy rich. I divorced him as quickly as I could and never made so much money in such a short time. With that said, can I really blame Mrs. Gutierrez for stripping Mr. Gutierrez down to the last enny? Of course not. In fact, I'd like to meet her lawyers.\n\nBut enough about Mrs. Gutierrez. Our client happens to be the injured party, Mr. Gutierrez. He lost his car and luxury penthouse, now the poor fool has barely anything to live in because he left his depository receipts in their old apartment (the locks are already changed). You'll have to retrieve them, because our new divorcee isn't going to give them back out of the kindness of her heart.\n\nThe penthouse is on the last floor of the building. Don't worry, I'm providing you with elevator access.\n\nFor obvious reasons, Mr. Gutierrez is counting on your utmost discretion. If things go quietly, he'll toss in extra.

**Coverage: journal-linked.** 45 exact journal-linked nodes in 5 resources; 8 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Deposit the shard in the Drop Point. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` |
| Escape the building. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape` |
| Find Gutierrez's office. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find` |
| Go to the apartment on Palm Street. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` |
| Go to the top floor. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor` |
| Steal the shard with the depository receipts. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` |
| Remain undetected. (Optional) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wbr_charter_hill.questphase / h2107 / 48` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 106:False → 48:Active; 48:Out → 105:In2 |
| `sts_wbr_charter_hill.questphase / h2107 / 49` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 4:Out → 49:Succeeded; 49:Out → 50:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 50` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor` | 49:Out → 50:Active; 50:Out → 51:In; 50:Out → 142:Inactive |
| `sts_wbr_charter_hill.questphase / h2107 / 52` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor` | 51:Out → 52:Succeeded; 52:Out → 58:Active; 52:Out → 113:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 58` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find` | 52:Out → 58:Active; 58:Out → 111:In |
| `sts_wbr_charter_hill.questphase / h2107 / 59` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find` | 111:Out → 59:Succeeded; 59:Out → 152:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 60` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape` | 60:Out → 26:In; 102:Out → 60:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 61` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape` | 26:Out → 61:Succeeded; 61:Out → 129:In; 61:Out → 131:In; 61:Out → 157:In |
| `sts_wbr_charter_hill.questphase / h2107 / 62` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 162:Out → 62:Succeeded; 62:Out → 87:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 87` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` | 62:Out → 87:Succeeded; 87:Out → 163:In |
| `sts_wbr_charter_hill.questphase / h2107 / 96` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 157:Out → 96:Active; 96:Out → 162:In |
| `sts_wbr_charter_hill.questphase / h2107 / 102` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 102:Out → 60:Active; 128:Out → 102:Succeeded; 102:Out → 153:In; 102:Out → 154:In |
| `sts_wbr_charter_hill.questphase / h2107 / 109` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 109:Out → 105:In1; 106:True → 109:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 113` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 52:Out → 113:Active; 113:Out → 89:In |
| `sts_wbr_charter_hill.questphase / h2107 / 114` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 89:Out → 114:Failed |
| `sts_wbr_charter_hill.questphase / h2107 / 119` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/brief` | 0:Out → 119:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 130` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 129:True → 130:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 152` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 59:Out → 152:Active; 152:Out → 128:In |
| `sts_wbr_charter_hill.questphase / h2107 / 142` (MappinManager) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor/elevator` | 50:Out → 142:Inactive |
| `sts_wbr_charter_hill.questphase / h2541 / 14` (PauseCondition) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 5:Out1 → 14:In; 14:Out → 15:In2 |
| `sts_wbr_charter_hill.questphase / h2666 / 26` (PauseCondition: IsSystemInCombat) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 0:Out → 26:In; 26:Out → 27:In; 26:Out → 33:In; 26:Out → 34:In |
| `sts_wbr_hil_01_gameplay.questphase / h0 / 14` (PauseCondition) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 5:Out1 → 14:In; 14:Out → 15:In2 |
| `sts_wbr_hil_01_gameplay.questphase / h125 / 26` (PauseCondition: IsSystemInCombat) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 0:Out → 26:In; 26:Out → 27:In; 26:Out → 33:In; 26:Out → 34:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 48` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 106:False → 48:Active; 48:Out → 105:In2 |
| `sts_wbr_hil_01_open_world.questphase / h314 / 49` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 4:Out → 49:Succeeded; 49:Out → 50:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 50` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor` | 49:Out → 50:Active; 50:Out → 51:In; 50:Out → 142:Inactive |
| `sts_wbr_hil_01_open_world.questphase / h314 / 52` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor` | 51:Out → 52:Succeeded; 52:Out → 58:Active; 52:Out → 113:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 58` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find` | 52:Out → 58:Active; 58:Out → 111:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 59` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find` | 111:Out → 59:Succeeded; 59:Out → 152:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 60` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape` | 60:Out → 26:In; 102:Out → 60:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 61` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape` | 26:Out → 61:Succeeded; 61:Out → 129:In; 61:Out → 131:In; 61:Out → 157:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 62` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 162:Out → 62:Succeeded; 62:Out → 87:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 87` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` | 62:Out → 87:Succeeded; 87:Out → 163:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 96` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 157:Out → 96:Active; 96:Out → 162:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 102` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 102:Out → 60:Active; 128:Out → 102:Succeeded; 102:Out → 153:In; 102:Out → 154:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 109` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment` | 109:Out → 105:In1; 106:True → 109:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 113` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 52:Out → 113:Active; 113:Out → 89:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 114` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 89:Out → 114:Failed |
| `sts_wbr_hil_01_open_world.questphase / h314 / 119` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/brief` | 0:Out → 119:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 130` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen` | 129:True → 130:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 152` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps` | 59:Out → 152:Active; 152:Out → 128:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 142` (MappinManager) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor/elevator` | 50:Out → 142:Inactive |
| `mq036_quest_bugfixes.questphase / h870 / 223` (Condition) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point` | 211:False → 223:In; 218:Out → 223:In; 223:True → 224:In; 223:False → 228:In |
| `open_world_bugfixing.questphase / h674 / 25` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` | 24:True → 25:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 25` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01` | 24:True → 25:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wbr_hil_01_open_world.questphase / h83 / 28` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene`; `#sts_sm_wbr_hil_01_chats` | 31:Out → 28:hil_01_civlians_chat_001_start |
| `sts_wbr_hil_01_open_world.questphase / h83 / 29` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene`; `#sts_sm_wbr_hil_01_chats` | 30:Out → 29:hil_01_civlians_chat_002_start |
| `sts_wbr_hil_01_open_world.questphase / h122 / 39` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene`; `#sts_sm_wbr_hil_01_holocall_debriefs` | 39:non_optional → 14:In; 39:optional → 16:In; 53:False → 39:Start 0; 39:rejected_out → 54:In; 39:Holocall INT → 42:In; 39:Holocall RET → 41:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 155` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene`; `#sts_sm_wbr_hil_01_holocall_prebrief` | 155:End 0 → 145:Active; 155:rejected_out → 145:Active; 159:True → 155:Start 0; 155:Holocall INT → 161:In; 155:Holocall RET → 160:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\sts_westbrook.questphase` / h0 / 2 | `sts_wbr_charter_hill.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2833 / 14 | `sts_wbr_hil_01_gameplay.questphase` | 21: Condition: hil_01_finished; 21:False → 14:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase` / h0 / 14 | `sts_wbr_hil_01_gameplay.questphase` | 21: Condition: hil_01_finished; 21:False → 14:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2833 / 15 | `sts_wbr_hil_01_open_world.questphase` | 21: Condition: hil_01_finished; 15:Out1 → 13:In; 21:False → 15:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase` / h0 / 15 | `sts_wbr_hil_01_open_world.questphase` | 21: Condition: hil_01_finished; 15:Out1 → 13:In; 21:False → 15:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h1876 / 28 | `sts_wbr_hil_01_chats.scene` | 31: PauseCondition: #hil_01_tr_civilian_chat_002; 31:Out → 28:hil_01_civlians_chat_001_start |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h1876 / 29 | `sts_wbr_hil_01_chats.scene` | 30: PauseCondition: #hil_01_tr_civilian_chat_001; 30:Out → 29:hil_01_civlians_chat_002_start |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h83 / 28 | `sts_wbr_hil_01_chats.scene` | 31: PauseCondition: #hil_01_tr_civilian_chat_002; 31:Out → 28:hil_01_civlians_chat_001_start |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h83 / 29 | `sts_wbr_hil_01_chats.scene` | 30: PauseCondition: #hil_01_tr_civilian_chat_001; 30:Out → 29:hil_01_civlians_chat_002_start |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h1915 / 39 | `sts_wbr_hil_01_holocall_debriefs.scene` | 53: Condition; 39:non_optional → 14:In; 39:optional → 16:In; 53:False → 39:Start 0; 39:rejected_out → 54:In; 39:Holocall INT → 42:In; 39:Holocall RET → 41:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h122 / 39 | `sts_wbr_hil_01_holocall_debriefs.scene` | 53: Condition; 39:non_optional → 14:In; 39:optional → 16:In; 53:False → 39:Start 0; 39:rejected_out → 54:In; 39:Holocall INT → 42:In; 39:Holocall RET → 41:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2107 / 155 | `sts_wbr_hil_01_holocall_prebrief.scene` | 159: Condition; 155:End 0 → 145:Active; 155:rejected_out → 145:Active; 159:True → 155:Start 0; 155:Holocall INT → 161:In; 155:Holocall RET → 160:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h314 / 155 | `sts_wbr_hil_01_holocall_prebrief.scene` | 159: Condition; 155:End 0 → 145:Active; 155:rejected_out → 145:Active; 159:True → 155:Start 0; 155:Holocall INT → 161:In; 155:Holocall RET → 160:In |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 8 | `sts_westbrook.questphase` | 0: Input; 0:Out → 8:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h0 / 6 | `sts_wbr_hil_01.questphase` | 34: Journal; 34:Out → 6:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.quest` / h0 / 6 | `sts_wbr_hil_01.questphase` | 10: FactsDBManager: hil_01_journal_test; 6:Out1 → 4:In; 10:Out → 6:In1 |
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
| `sts_wbr_hil_01_chats.scene` | hil_01_civlians_chat_001_start, hil_01_civlians_chat_002_start → hil_01_civlians_chat_001_end, hil_01_civlians_chat_002_end | civilian_001; civilian_002; civilian_003; civilian_004; 8 nodes / 8 edges |
| `sts_wbr_hil_01_holocall_debriefs.scene` | Start 0 → optional, rejected_out, non_optional | Wakako; Player; 28 nodes / 38 edges |
| `sts_wbr_hil_01_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | Wakako; Player; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `hil_01_combat` | sts_wbr_hil_01_open_world.questphase / h314 / 115 | sts_wbr_charter_hill.questphase / h2107 / 129; sts_wbr_hil_01_holocall_debriefs.scene / scene / 65; sts_wbr_hil_01_open_world.questphase / h122 / 54; sts_wbr_hil_01_open_world.questphase / h314 / 129 |
| `hil_01_finished` | sts_wbr_hil_01_open_world.questphase / h122 / 30 | open_world_bugfixing.questphase / h1792 / 24; open_world_bugfixing.questphase / h674 / 24 |
| `hil_01_journal_test` | Producer outside selected context | sts_wbr_charter_hill.questphase / h2107 / 106; sts_wbr_hil_01_open_world.questphase / h314 / 106 |
| `hil_01_start` | sts_wbr_hil_01_open_world.questphase / h314 / 107 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wbr_hil_01_holocall_prebrief.scene / scene / 279 |
| `holo_setup_active` | Producer outside selected context | sts_wbr_hil_01_holocall_debriefs.scene / scene / 253; sts_wbr_hil_01_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wbr_hil_01_holocall_debriefs.scene / scene / 253; sts_wbr_hil_01_holocall_prebrief.scene / scene / 279 |
| `holo_wakako_calls_v_end_activate` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 88; sts_wbr_hil_01_holocall_prebrief.scene / scene / 65; sts_wbr_hil_01_open_world.questphase / h122 / 42; sts_wbr_hil_01_open_world.questphase / h314 / 161 | No reader in selected context |
| `holo_wakako_calls_v_end_done` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 84; sts_wbr_hil_01_holocall_prebrief.scene / scene / 61 | sts_wbr_hil_01_holocall_debriefs.scene / scene / 83; sts_wbr_hil_01_holocall_prebrief.scene / scene / 60 |
| `holo_wakako_calls_v_rejectable` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 280; sts_wbr_hil_01_holocall_prebrief.scene / scene / 254; sts_wbr_hil_01_holocall_prebrief.scene / scene / 297 | No reader in selected context |
| `holo_wakako_calls_v_rejected` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 284; sts_wbr_hil_01_holocall_prebrief.scene / scene / 258 | sts_wbr_hil_01_holocall_debriefs.scene / scene / 282; sts_wbr_hil_01_holocall_prebrief.scene / scene / 256 |
| `holo_wakako_calls_v_start_activate` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 261; sts_wbr_hil_01_holocall_debriefs.scene / scene / 87; sts_wbr_hil_01_holocall_prebrief.scene / scene / 295; sts_wbr_hil_01_holocall_prebrief.scene / scene / 64; sts_wbr_hil_01_open_world.questphase / h122 / 41; sts_wbr_hil_01_open_world.questphase / h314 / 160 | sts_wbr_hil_01_holocall_debriefs.scene / scene / 253 |
| `holo_wakako_calls_v_start_done` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 82; sts_wbr_hil_01_holocall_prebrief.scene / scene / 59 | sts_wbr_hil_01_holocall_debriefs.scene / scene / 270; sts_wbr_hil_01_holocall_prebrief.scene / scene / 267 |
| `sts_wbr_hil_01_depositary_receipt` | Producer outside selected context | sts_wbr_charter_hill.questphase / h2107 / 162; sts_wbr_hil_01_open_world.questphase / h314 / 162 |
| `wbr_achievement` | sts_wbr_hil_01_open_world.questphase / h122 / 29 | sts_wbr_hil_01_open_world.questphase / h122 / 47 |

## Exact gates, joins and cancellation

<details><summary>80 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wbr_charter_hill.questphase / h2107 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_building"}}` | 105:Out1 → 4:In; 4:Out → 49:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_end"}}` | 60:Out → 26:In; 26:Out → 61:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_up"}}` | 50:Out → 51:In; 51:Out → 52:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 105` | `questLogicalXorNodeDefinition` `{}` | 105:Out1 → 4:In; 48:Out → 105:In2; 109:Out → 105:In1; 105:Out1 → 132:In |
| `sts_wbr_charter_hill.questphase / h2107 / 106` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_journal_test"}}}` | 106:False → 48:Active; 107:Out → 106:In; 106:True → 109:Active |
| `sts_wbr_charter_hill.questphase / h2107 / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_room"}}` | 58:Out → 111:In; 111:Out → 59:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 113:Out → 89:In; 89:Out → 114:Failed; 89:Out → 115:In |
| `sts_wbr_charter_hill.questphase / h2107 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"171618873303","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 128:Out → 102:Succeeded; 152:Out → 128:In; 128:Out → 133:In; 128:Out → 156:In |
| `sts_wbr_charter_hill.questphase / h2107 / 129` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_combat","comparisonType":"Equal"}}}` | 61:Out → 129:In; 129:True → 130:Succeeded |
| `sts_wbr_charter_hill.questphase / h2107 / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_hil_01_depositary_receipt"}}}` | 162:Out → 62:Succeeded; 96:Out → 162:In |
| `sts_wbr_charter_hill.questphase / h2107 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_01\\scenes\\sts_wbr_hil_01_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 163:Out → 1:In; 87:Out → 163:In |
| `sts_wbr_charter_hill.questphase / h2541 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 5:Out1 → 14:In; 14:Out → 15:In2 |
| `sts_wbr_charter_hill.questphase / h2541 / 15` | `questLogicalXorNodeDefinition` `{}` | 8:Out → 15:In1; 15:Out1 → 9:In; 15:Out1 → 10:In; 15:Out1 → 11:In; 14:Out → 15:In2 |
| `sts_wbr_charter_hill.questphase / h2582 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 16:In; 16:Out → 1:In |
| `sts_wbr_charter_hill.questphase / h2596 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_dron_patrols_001"}}` | 0:Out → 12:In; 12:Out → 16:In1 |
| `sts_wbr_charter_hill.questphase / h2596 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_drone","names":["drone_001"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 14:Out → 4:In; 16:Out1 → 14:In |
| `sts_wbr_charter_hill.questphase / h2596 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_drone","names":["drone_002"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 16:Out1 → 15:In; 15:Out → 19:In |
| `sts_wbr_charter_hill.questphase / h2596 / 16` | `questLogicalXorNodeDefinition` `{}` | 12:Out → 16:In1; 16:Out1 → 14:In; 16:Out1 → 15:In; 17:Out → 16:In2 |
| `sts_wbr_charter_hill.questphase / h2596 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_dvc_techie_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 17:In; 17:Out → 16:In2 |
| `sts_wbr_charter_hill.questphase / h2666 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_room"}]}}` | 0:Out → 26:In; 26:Out → 27:In; 26:Out → 33:In; 26:Out → 34:In |
| `sts_wbr_hil_01_gameplay.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_01_sts_start"}}` | 5:Out1 → 8:In; 8:Out → 15:In1 |
| `sts_wbr_hil_01_gameplay.questphase / h0 / 13` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 13:Out1 → 1:In; 9:Out → 13:In1; 10:Out → 13:In2; 11:Out → 13:In3 |
| `sts_wbr_hil_01_gameplay.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 5:Out1 → 14:In; 14:Out → 15:In2 |
| `sts_wbr_hil_01_gameplay.questphase / h0 / 15` | `questLogicalXorNodeDefinition` `{}` | 8:Out → 15:In1; 15:Out1 → 9:In; 15:Out1 → 10:In; 15:Out1 → 11:In; 14:Out → 15:In2 |
| `sts_wbr_hil_01_gameplay.questphase / h12 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_drone"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 20:Out → 1:In; 18:Out → 20:In |
| `sts_wbr_hil_01_gameplay.questphase / h41 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 16:In; 16:Out → 1:In |
| `sts_wbr_hil_01_gameplay.questphase / h55 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_dron_patrols_001"}}` | 0:Out → 12:In; 12:Out → 16:In1 |
| `sts_wbr_hil_01_gameplay.questphase / h55 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_drone","names":["drone_001"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 14:Out → 4:In; 16:Out1 → 14:In |
| `sts_wbr_hil_01_gameplay.questphase / h55 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_drone","names":["drone_002"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 16:Out1 → 15:In; 15:Out → 19:In |
| `sts_wbr_hil_01_gameplay.questphase / h55 / 16` | `questLogicalXorNodeDefinition` `{}` | 12:Out → 16:In1; 16:Out1 → 14:In; 16:Out1 → 15:In; 17:Out → 16:In2 |
| `sts_wbr_hil_01_gameplay.questphase / h55 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_dvc_techie_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 17:In; 17:Out → 16:In2 |
| `sts_wbr_hil_01_gameplay.questphase / h125 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_enemies"},"isPlayer":false,"inverted":true}}}` | 29:Success → 21:In; 21:Out → 32:In; 21:Out → 31:In; 21:Out → 30:In |
| `sts_wbr_hil_01_gameplay.questphase / h125 / 25` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 25:Out1 → 1:In; 30:Out → 25:In1; 31:Out → 25:In2; 32:Out → 25:In3 |
| `sts_wbr_hil_01_gameplay.questphase / h125 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_room"}]}}` | 0:Out → 26:In; 26:Out → 27:In; 26:Out → 33:In; 26:Out → 34:In |
| `sts_wbr_hil_01_gameplay.questphase / h125 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_01_com_enemies"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 27:Out → 28:In; 28:Out → 29:In |
| `sts_wbr_hil_01_gameplay.questphase / h216 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsRestarting"}}}` | 0:Out → 8:In; 8:Out → 11:In; 8:Out → 12:In; 8:Out → 15:In |
| `sts_wbr_hil_01_open_world.questphase / h12 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_sts_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 31:Out → 27:In; 32:Out → 31:In |
| `sts_wbr_hil_01_open_world.questphase / h83 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_civilian_chat_001"}}` | 0:Out → 30:In; 30:Out → 29:hil_01_civlians_chat_002_start |
| `sts_wbr_hil_01_open_world.questphase / h83 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_civilian_chat_002"}}` | 0:Out → 31:In; 31:Out → 28:hil_01_civlians_chat_001_start |
| `sts_wbr_hil_01_open_world.questphase / h122 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_01_sts_clean_up"}}` | 43:Out → 35:In; 44:Out → 43:In |
| `sts_wbr_hil_01_open_world.questphase / h122 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 45:Out → 44:In; 46:Out → 45:In |
| `sts_wbr_hil_01_open_world.questphase / h122 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 53:False → 39:Start 0; 51:Out → 53:In; 53:True → 54:In |
| `sts_wbr_hil_01_open_world.questphase / h122 / 54` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_combat","comparisonType":"Equal"}}}` | 39:rejected_out → 54:In; 54:False → 52:Active; 53:True → 54:In; 54:True → 55:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_building"}}` | 105:Out1 → 4:In; 4:Out → 49:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_end"}}` | 60:Out → 26:In; 26:Out → 61:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_up"}}` | 50:Out → 51:In; 51:Out → 52:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 105` | `questLogicalXorNodeDefinition` `{}` | 105:Out1 → 4:In; 48:Out → 105:In2; 109:Out → 105:In1; 105:Out1 → 132:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 106` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_journal_test"}}}` | 106:False → 48:Active; 107:Out → 106:In; 106:True → 109:Active |
| `sts_wbr_hil_01_open_world.questphase / h314 / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_tr_room"}}` | 58:Out → 111:In; 111:Out → 59:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#hil_01_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 113:Out → 89:In; 89:Out → 114:Failed; 89:Out → 115:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"171618873303","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 128:Out → 102:Succeeded; 152:Out → 128:In; 128:Out → 133:In; 128:Out → 156:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 129` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_combat","comparisonType":"Equal"}}}` | 61:Out → 129:In; 129:True → 130:Succeeded |
| `sts_wbr_hil_01_open_world.questphase / h314 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_01_sts_start"}}` | 137:Out → 134:In; 145:Out → 134:In; 134:Out → 136:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_01_sts_start"}}` | 136:Out → 135:In; 135:Out → 137:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 159` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 159:False → 145:Active; 159:True → 155:Start 0; 165:False → 159:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_hil_01_depositary_receipt"}}}` | 162:Out → 62:Succeeded; 96:Out → 162:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_01\\scenes\\sts_wbr_hil_01_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 163:Out → 1:In; 87:Out → 163:In |
| `sts_wbr_hil_01_open_world.questphase / h314 / 165` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 144:Out → 165:In; 165:True → 145:Active; 165:False → 159:In |
| `sts_wbr_hil_01_chats.scene / scene / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_01\\scenes\\sts_wbr_hil_01_chats.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 4:0:0 → 19:0:1; 19:0:0 → 5:0:0 |
| `sts_wbr_hil_01_chats.scene / scene / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_01\\scenes\\sts_wbr_hil_01_chats.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 6:0:0 → 25:0:1; 25:0:0 → 7:0:0 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 65` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_combat","comparisonType":"Equal"}}}` | 65:0:0 → 4:0:0; 65:0:1 → 55:0:0; 85:0:0 → 65:0:1 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 83:0:0 → 84:0:1; 88:0:0 → 83:0:1 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":600}}}` | 81:666:0 → 249:0:1; 249:0:0 → 253:0:1; 251:1:0 → 249:0:0; 251:1:0 → 249:1026:0; 259:0:0 → 249:0:1 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 253:0:1; 251:1:0 → 253:0:0; 251:1:0 → 253:1026:0; 253:0:0 → 255:0:1 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":600}}}` | 251:1:0 → 255:0:0; 251:1:0 → 255:1026:0; 253:0:0 → 255:0:1; 255:0:0 → 257:0:1 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 257` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 255:0:0 → 257:0:1; 257:0:0 → 261:0:1; 257:0:1 → 259:0:0 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 270` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 81:666:0 → 270:0:1; 270:0:0 → 251:0:0 |
| `sts_wbr_hil_01_holocall_debriefs.scene / scene / 282` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 87:0:0 → 282:0:1; 282:0:0 → 284:0:1 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 64:0:0 → 256:0:1; 256:0:0 → 258:0:1 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 58:666:0 → 267:0:1; 267:0:0 → 269:0:0 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 58:666:0 → 273:0:1; 269:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 297:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wbr_hil_01_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 269:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `mq036_quest_bugfixes.questphase / h870 / 211` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 210:False → 211:In; 217:Out → 211:In; 211:True → 212:In; 211:False → 223:In |
| `mq036_quest_bugfixes.questphase / h870 / 223` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 211:False → 223:In; 218:Out → 223:In; 223:True → 224:In; 223:False → 228:In |
| `mq036_quest_bugfixes.questphase / h870 / 224` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"171618873303","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 223:True → 224:In; 224:True → 227:In; 224:False → 225:In |
| `mq036_quest_bugfixes.questphase / h870 / 228` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 223:False → 228:In; 227:Out → 228:In; 228:True → 229:In; 228:False → 235:In |
| `open_world_bugfixing.questphase / h674 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_finished"}}}` | 0:Out → 24:In; 24:True → 25:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_01_finished"}}}` | 0:Out → 24:In; 24:True → 25:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wbr_charter_hill.questphase / h2596 / 14; sts_wbr_charter_hill.questphase / h2596 / 15; sts_wbr_hil_01_gameplay.questphase / h12 / 20; sts_wbr_hil_01_gameplay.questphase / h125 / 28; +2 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_wbr_hil_01_open_world.questphase / h122 / 31; sts_wbr_hil_01_open_world.questphase / h314 / 144 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | sts_wbr_hil_01_gameplay.questphase / h125 / 29 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_wbr_charter_hill.questphase / h2666 / 27; sts_wbr_hil_01_gameplay.questphase / h12 / 18; sts_wbr_hil_01_gameplay.questphase / h125 / 27; sts_wbr_hil_01_gameplay.questphase / h125 / 30; +5 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1792 / 24; open_world_bugfixing.questphase / h674 / 24; sts_wbr_charter_hill.questphase / h2107 / 106; sts_wbr_charter_hill.questphase / h2107 / 129; +14 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wbr_charter_hill.questphase / h2107 / 157; sts_wbr_hil_01_open_world.questphase / h122 / 28; sts_wbr_hil_01_open_world.questphase / h122 / 40; sts_wbr_hil_01_open_world.questphase / h314 / 136; +2 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 218; sts_wbr_hil_01_open_world.questphase / h122 / 24; sts_wbr_hil_01_open_world.questphase / h314 / 132; sts_wbr_hil_01_open_world.questphase / h314 / 133; +1 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wbr_charter_hill.questphase / h2107 / 131; sts_wbr_hil_01_open_world.questphase / h12 / 22; sts_wbr_hil_01_open_world.questphase / h122 / 38; sts_wbr_hil_01_open_world.questphase / h314 / 131; +1 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_wbr_charter_hill.questphase / h2107 / 89; sts_wbr_charter_hill.questphase / h2582 / 16; sts_wbr_charter_hill.questphase / h2596 / 17; sts_wbr_charter_hill.questphase / h2666 / 26; +5 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_wbr_hil_01_open_world.questphase / h122 / 45 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 224; sts_wbr_charter_hill.questphase / h2107 / 128; sts_wbr_hil_01_open_world.questphase / h314 / 128 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1792 / 25; open_world_bugfixing.questphase / h674 / 25; sts_wbr_charter_hill.questphase / h2107 / 102; sts_wbr_charter_hill.questphase / h2107 / 109; +40 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_wbr_hil_01_gameplay.questphase / h0 / 13; sts_wbr_hil_01_gameplay.questphase / h125 / 25 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 261; sts_wbr_hil_01_holocall_debriefs.scene / scene / 280; sts_wbr_hil_01_holocall_debriefs.scene / scene / 284; sts_wbr_hil_01_holocall_debriefs.scene / scene / 82; +19 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wbr_charter_hill.questphase / h2107 / 105; sts_wbr_charter_hill.questphase / h2541 / 15; sts_wbr_charter_hill.questphase / h2596 / 16; sts_wbr_hil_01_gameplay.questphase / h0 / 15; +2 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wbr_hil_01_holocall_debriefs.scene / scene / 249; sts_wbr_hil_01_holocall_debriefs.scene / scene / 255; sts_wbr_hil_01_holocall_prebrief.scene / scene / 273; sts_wbr_hil_01_holocall_prebrief.scene / scene / 281 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_wbr_hil_01_open_world.questphase / h122 / 14; sts_wbr_hil_01_open_world.questphase / h122 / 16 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_wbr_hil_01_open_world.questphase / h122 / 39; sts_wbr_hil_01_open_world.questphase / h314 / 155; sts_wbr_hil_01_open_world.questphase / h83 / 28; sts_wbr_hil_01_open_world.questphase / h83 / 29 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wbr_charter_hill.questphase / h2107 / 111; sts_wbr_charter_hill.questphase / h2107 / 26; sts_wbr_charter_hill.questphase / h2107 / 4; sts_wbr_charter_hill.questphase / h2107 / 51; +15 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | sts_wbr_charter_hill.questphase / h2666 / 33; sts_wbr_charter_hill.questphase / h2666 / 34; sts_wbr_hil_01_gameplay.questphase / h125 / 33; sts_wbr_hil_01_gameplay.questphase / h125 / 34 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` | content candidate; journal anchor | `base-sts-wbr-hil-01` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` | content candidate; journal anchor | `base-sts-wbr-hil-01` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene` | content candidate; forward dependency | `base-sts-wbr-hil-01` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-wbr-hil-01` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wbr-hil-01` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wbr-hil-01](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wbr-hil-01.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

180 repeated typed/socket path signatures in this selected graph context; 21 distinct direct resource identities; 12 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h12 / 0 -> 18 -> 20 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 87 -> 282 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 86 -> 88 -> 83 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` / scene / 59 -> 62 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 4 -> 86 -> 88 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene` / scene / 6 -> 11 -> 7 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `c8705a8da51824b73252` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h314 / 0 -> 107 -> 106 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 280 -> 87 -> 282 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 1 -> 280 -> 87 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2107 / 4 -> 49 -> 50 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 270 -> 251 -> 249 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2541 / 5 | `h2582` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2582 / 13 | `h2596` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 4 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 5 | `h41` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h41 / 13 | `h55` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 6 | `h125` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 7 | `h216` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h0 / 4 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h0 / 5 | `h76` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h76 / 4 | `h83` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h0 / 6 | `h122` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h0 / 7 | `h314` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.gamedef` | content candidate | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.quest |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01_test.gamedef` | content candidate | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.quest |
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
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_chats\civ_high_f_02_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_chats\civ_high_f_18_jap_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_chats\civ_high_m_01_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_chats\civ_high_m_09_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_holocall_debriefs\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\lipsync\en\sts_wbr_hil_01_holocall_prebrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_after_phase.questphase` | phase flow | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_quest_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `hil_01_combat` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h2107 / 115; 1 total source locations in compressed evidence |
| `hil_01_finished` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h1915 / 30; 1 total source locations in compressed evidence |
| `hil_01_journal_test` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.quest / h0 / 10; 1 total source locations in compressed evidence |
| `hil_01_start` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h2107 / 107; 1 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 63; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 903; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 199; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 27; 61 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 895; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 293; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 42; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 528; 26 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejectable` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 629; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1206; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 288; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 254; 25 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejected` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 637; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1214; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 290; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 256; 17 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 62; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 901; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 198; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 26; 75 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 891; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 292; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 41; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 575; 25 total source locations in compressed evidence |
| `wbr_achievement` | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase / h0 / 40; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase / h0 / 68; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase / h0 / 51; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase / h0 / 60; 39 total source locations in compressed evidence |

NodeRef uses: 99; TweakDB binding uses: 12. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene` | 2 / 19 | scnDialogLineEvent: 11; scnLookAtEvent: 8 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` | 2 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` | 1 / 4 | scnDialogLineEvent: 4 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
