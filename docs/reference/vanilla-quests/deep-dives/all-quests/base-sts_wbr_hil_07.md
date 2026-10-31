# Gig: Tyger and Vulture

Journal: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` · `StreetStory` · hash `277336735`.

Journal premise: Gig type: Thievery\nObjective: Steal Vortex's credchip\nLocation: Tyger Claws' casino on Longshore South\nDetails:\n\nThe vulture is the wisest bird. While others lose strength in the pursuit of prey, the vulture waits patiently – it only spreads its wings when it smells blood on the air.\n\nYou will be my vulture, V. I heard a Tyger Claws casino has been robbed by one of their own – a dealer. The girl had an alias, Vortex, and she managed the casino's machines. She programmed them to skim a small percentage so a drop from each win landed in her bucket. It took years for the Tygers to realize how they were being cheated. You can imagine they were not pleased. But their ferocity extended too far. Vortex died during the interrogation before revealing where she stored the stolen money. A vulture is wiser than a Tyger, V. You will find it.\n\nI will send you the Vortex's last known location. Don't let me down.

**Coverage: journal-linked.** 38 exact journal-linked nodes in 5 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate, 3 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Take Vortex's credchip. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer` |
| Deposit Vortex's credchip in the Drop Point. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` |
| Enter the casino. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` |
| Search the casino office. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` |
| Find Vortex's credchip. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den` |
| Find the office on the second floor. (Primary) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wbr_charter_hill.questphase / h4544 / 123` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 169:True → 123:Active; 123:Out → 171:In1 |
| `sts_wbr_charter_hill.questphase / h4544 / 128` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 210:Out1 → 128:Succeeded; 128:Out → 129:Active |
| `sts_wbr_charter_hill.questphase / h4544 / 129` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 128:Out → 129:Active; 129:Out → 131:In; 129:Out → 133:In |
| `sts_wbr_charter_hill.questphase / h4544 / 132` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 131:Out → 132:Succeeded; 132:Out → 141:Active |
| `sts_wbr_charter_hill.questphase / h4544 / 141` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` | 132:Out → 141:Active; 141:Out → 133:In |
| `sts_wbr_charter_hill.questphase / h4544 / 142` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` | 133:Out → 142:Succeeded; 142:Out → 196:Active |
| `sts_wbr_charter_hill.questphase / h4544 / 146` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer` | 197:Out → 146:Active; 146:Out → 217:In |
| `sts_wbr_charter_hill.questphase / h4544 / 151` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` | 175:Out → 151:Active; 151:Out → 203:In |
| `sts_wbr_charter_hill.questphase / h4544 / 159` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` | 213:Out → 159:Succeeded; 159:Out → 162:Succeeded |
| `sts_wbr_charter_hill.questphase / h4544 / 160` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/brief` | 169:True → 160:Active; 169:False → 160:Active |
| `sts_wbr_charter_hill.questphase / h4544 / 162` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` | 159:Out → 162:Succeeded; 162:Out → 176:In |
| `sts_wbr_charter_hill.questphase / h4544 / 163` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 133:Out → 163:Inactive |
| `sts_wbr_charter_hill.questphase / h4544 / 172` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 169:False → 172:Active; 172:Out → 171:In2 |
| `sts_wbr_charter_hill.questphase / h4544 / 192` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den/vortex_shard` | 191:Out → 192:In |
| `sts_wbr_charter_hill.questphase / h4544 / 195` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer` | 195:Out → 175:In; 217:Out → 195:Succeeded |
| `sts_wbr_charter_hill.questphase / h4544 / 196` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den` | 142:Out → 196:Active; 196:Out → 149:In; 196:Out → 194:In |
| `sts_wbr_charter_hill.questphase / h4544 / 197` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den` | 197:Out → 146:Active; 216:Out1 → 197:Succeeded |
| `sts_wbr_hil_07_bugfixing.questphase / h120 / 4` (Condition) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` | 3:Out → 4:In; 4:True → 5:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 123` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 169:True → 123:Active; 123:Out → 171:In1 |
| `sts_wbr_hil_07_ow.questphase / h169 / 128` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 210:Out1 → 128:Succeeded; 128:Out → 129:Active |
| `sts_wbr_hil_07_ow.questphase / h169 / 129` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 128:Out → 129:Active; 129:Out → 131:In; 129:Out → 133:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 132` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 131:Out → 132:Succeeded; 132:Out → 141:Active |
| `sts_wbr_hil_07_ow.questphase / h169 / 141` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` | 132:Out → 141:Active; 141:Out → 133:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 142` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan` | 133:Out → 142:Succeeded; 142:Out → 196:Active |
| `sts_wbr_hil_07_ow.questphase / h169 / 146` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer` | 197:Out → 146:Active; 146:Out → 217:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 151` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` | 175:Out → 151:Active; 151:Out → 203:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 159` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` | 213:Out → 159:Succeeded; 159:Out → 162:Succeeded |
| `sts_wbr_hil_07_ow.questphase / h169 / 160` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/brief` | 169:True → 160:Active; 169:False → 160:Active |
| `sts_wbr_hil_07_ow.questphase / h169 / 162` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` | 159:Out → 162:Succeeded; 162:Out → 176:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 163` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers` | 133:Out → 163:Inactive |
| `sts_wbr_hil_07_ow.questphase / h169 / 172` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in` | 169:False → 172:Active; 172:Out → 171:In2 |
| `sts_wbr_hil_07_ow.questphase / h169 / 192` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den/vortex_shard` | 191:Out → 192:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 195` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer` | 195:Out → 175:In; 217:Out → 195:Succeeded |
| `sts_wbr_hil_07_ow.questphase / h169 / 196` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den` | 142:Out → 196:Active; 196:Out → 149:In; 196:Out → 194:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 197` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den` | 197:Out → 146:Active; 216:Out1 → 197:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 228` (Condition) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet` | 223:False → 228:In; 227:Out → 228:In; 228:True → 229:In; 228:False → 235:In |
| `open_world_bugfixing.questphase / h674 / 29` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` | 28:True → 29:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 29` (Journal) | `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07` | 28:True → 29:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wbr_hil_07_ow.questphase / h169 / 200` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene`; `#sts_sm_wbr_hil_07_holocall_prebrief` | 200:End1 → 188:Active; 200:rejected_out → 188:Active; 221:False → 200:Start1; 200:Holocall INT → 206:In; 200:Holocall RET → 205:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 11` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene`; `#sts_sm_wbr_hil_07_holocall_debrief` | 41:False → 11:Start1; 11:rejected_out → 42:Active; 11:End1 → 12:In; 11:Holocall INT → 14:In; 11:Holocall RET → 13:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\sts_westbrook.questphase` / h0 / 2 | `sts_wbr_charter_hill.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\open_world\bugfixing\sts\sts_charter_hill_bugfixing.questphase` / h0 / 7 | `sts_wbr_hil_07_bugfixing.questphase` | 10: DeletionMarker; 10:Out → 7:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h2524 / 11 | `sts_wbr_hil_07_ow.questphase` | 0: Input; 0:Out → 11:In1; 11:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07.questphase` / h0 / 11 | `sts_wbr_hil_07_ow.questphase` | 0: Input; 0:Out → 11:In1; 11:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h4977 / 11 | `sts_wbr_hil_07_holocall_debrief.scene` | 41: Condition; 41:False → 11:Start1; 11:rejected_out → 42:Active; 11:End1 → 12:In; 11:Holocall INT → 14:In; 11:Holocall RET → 13:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h602 / 11 | `sts_wbr_hil_07_holocall_debrief.scene` | 41: Condition; 41:False → 11:Start1; 11:rejected_out → 42:Active; 11:End1 → 12:In; 11:Holocall INT → 14:In; 11:Holocall RET → 13:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h4544 / 200 | `sts_wbr_hil_07_holocall_prebrief.scene` | 221: Condition; 200:End1 → 188:Active; 200:rejected_out → 188:Active; 221:False → 200:Start1; 200:Holocall INT → 206:In; 200:Holocall RET → 205:In |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 200 | `sts_wbr_hil_07_holocall_prebrief.scene` | 221: Condition; 200:End1 → 188:Active; 200:rejected_out → 188:Active; 221:False → 200:Start1; 200:Holocall INT → 206:In; 200:Holocall RET → 205:In |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 8 | `sts_westbrook.questphase` | 0: Input; 0:Out → 8:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 38 | `sts_charter_hill_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 38:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h0 / 11 | `sts_wbr_hil_07.questphase` | 45: Journal; 45:Out → 11:In1 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.quest` / h0 / 2 | `sts_wbr_hil_07.questphase` | 3: FactsDBManager: hil_07_track; 2:Out1 → 1:In; 3:Out → 2:In1 |
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
| `sts_wbr_hil_07_holocall_debrief.scene` | Start1 → rejected_out, End1 | fixer; 23 nodes / 30 edges |
| `sts_wbr_hil_07_holocall_prebrief.scene` | Start1 → End1, rejected_out | fixer; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-622569` | sts_wbr_hil_07_bugfixing.questphase / h120 / 3 | sts_wbr_hil_07_bugfixing.questphase / h120 / 2 |
| `CYB-622577` | sts_wbr_hil_07_bugfixing.questphase / h10 / 3 | sts_wbr_hil_07_bugfixing.questphase / h10 / 2 |
| `glossary_tc` | sts_wbr_hil_07_ow.questphase / h169 / 179 | No reader in selected context |
| `hil_07_after_holocall` | sts_wbr_hil_07_ow.questphase / h602 / 45 | No reader in selected context |
| `hil_07_backdoor` | Producer outside selected context | sts_wbr_hil_07_ow.questphase / h169 / 165 |
| `hil_07_comabt` | Producer outside selected context | sts_wbr_hil_07_ow.questphase / h602 / 7 |
| `hil_07_finished` | sts_wbr_charter_hill.questphase / h4544 / 176; sts_wbr_hil_07_ow.questphase / h169 / 176 | open_world_bugfixing.questphase / h1792 / 28; open_world_bugfixing.questphase / h674 / 28; sts_wbr_hil_07_bugfixing.questphase / h10 / 11 |
| `hil_07_gang_retaliation` | Producer outside selected context | sts_wbr_hil_07_ow.questphase / h602 / 46 |
| `hil_07_second_flor` | Producer outside selected context | sts_wbr_charter_hill.questphase / h4544 / 131; sts_wbr_hil_07_ow.questphase / h169 / 131 |
| `hil_07_spawned` | sts_wbr_hil_07_ow.questphase / h12 / 41 | No reader in selected context |
| `hil_07_start` | sts_wbr_hil_07_ow.questphase / h169 / 87 | No reader in selected context |
| `hil_07_track` | Producer outside selected context | sts_wbr_charter_hill.questphase / h4544 / 169; sts_wbr_hil_07_ow.questphase / h169 / 169 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wbr_hil_07_holocall_prebrief.scene / scene / 279 |
| `holo_setup_active` | Producer outside selected context | sts_wbr_hil_07_holocall_debrief.scene / scene / 251; sts_wbr_hil_07_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wbr_hil_07_holocall_debrief.scene / scene / 251; sts_wbr_hil_07_holocall_prebrief.scene / scene / 279 |
| `holo_wakako_calls_v_end_activate` | sts_wbr_hil_07_holocall_debrief.scene / scene / 65; sts_wbr_hil_07_holocall_prebrief.scene / scene / 67; sts_wbr_hil_07_ow.questphase / h169 / 206; sts_wbr_hil_07_ow.questphase / h602 / 14 | No reader in selected context |
| `holo_wakako_calls_v_end_done` | sts_wbr_hil_07_holocall_debrief.scene / scene / 61; sts_wbr_hil_07_holocall_prebrief.scene / scene / 63 | sts_wbr_hil_07_holocall_debrief.scene / scene / 60; sts_wbr_hil_07_holocall_prebrief.scene / scene / 62 |
| `holo_wakako_calls_v_rejectable` | sts_wbr_hil_07_holocall_debrief.scene / scene / 279; sts_wbr_hil_07_holocall_prebrief.scene / scene / 254; sts_wbr_hil_07_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_wakako_calls_v_rejected` | sts_wbr_hil_07_holocall_debrief.scene / scene / 281; sts_wbr_hil_07_holocall_prebrief.scene / scene / 256 | sts_wbr_hil_07_holocall_debrief.scene / scene / 283; sts_wbr_hil_07_holocall_prebrief.scene / scene / 258 |
| `holo_wakako_calls_v_start_activate` | sts_wbr_hil_07_holocall_debrief.scene / scene / 259; sts_wbr_hil_07_holocall_debrief.scene / scene / 64; sts_wbr_hil_07_holocall_prebrief.scene / scene / 283; sts_wbr_hil_07_holocall_prebrief.scene / scene / 66; sts_wbr_hil_07_ow.questphase / h169 / 205; sts_wbr_hil_07_ow.questphase / h602 / 13 | sts_wbr_hil_07_holocall_debrief.scene / scene / 251 |
| `holo_wakako_calls_v_start_done` | sts_wbr_hil_07_holocall_debrief.scene / scene / 59; sts_wbr_hil_07_holocall_prebrief.scene / scene / 61 | sts_wbr_hil_07_holocall_debrief.scene / scene / 273; sts_wbr_hil_07_holocall_prebrief.scene / scene / 267 |
| `sts_tygerclaws_retaliation` | sts_wbr_hil_07_ow.questphase / h602 / 47 | No reader in selected context |
| `sts_wbr_hil_07_cleanup_fix` | sts_wbr_hil_07_ow.questphase / h602 / 38 | sts_wbr_hil_07_bugfixing.questphase / h10 / 10 |
| `sts_wbr_hil_07_shard` | Producer outside selected context | sts_wbr_charter_hill.questphase / h4544 / 213; sts_wbr_hil_07_ow.questphase / h169 / 213 |
| `travelling_merchant_lives` | Producer outside selected context | sts_wbr_hil_07_bugfixing.questphase / h0 / 8 |
| `wbr_achievement` | sts_wbr_hil_07_ow.questphase / h602 / 4 | sts_wbr_hil_07_ow.questphase / h602 / 16 |

## Exact gates, joins and cancellation

<details><summary>69 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wbr_charter_hill.questphase / h4544 / 131` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_second_flor"}}}` | 129:Out → 131:In; 131:Out → 132:Succeeded |
| `sts_wbr_charter_hill.questphase / h4544 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_den_trigger_001"}}` | 129:Out → 133:In; 141:Out → 133:In; 133:Out → 142:Succeeded; 133:Out → 163:Inactive |
| `sts_wbr_charter_hill.questphase / h4544 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115159699771","comparisonType":"Greater"}}}` | 196:Out → 149:In; 149:Out → 216:In2 |
| `sts_wbr_charter_hill.questphase / h4544 / 169` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_track"}}}` | 78:Out → 169:In; 169:True → 123:Active; 169:True → 160:Active; 169:False → 160:Active; 169:False → 172:Active |
| `sts_wbr_charter_hill.questphase / h4544 / 171` | `questLogicalXorNodeDefinition` `{}` | 123:Out → 171:In1; 171:Out1 → 127:In; 172:Out → 171:In2; 171:Out1 → 211:In |
| `sts_wbr_charter_hill.questphase / h4544 / 191` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_token_quest"}}}}` | 0:Out → 191:In; 191:Out → 192:In |
| `sts_wbr_charter_hill.questphase / h4544 / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_objective_loot"},"timeInterval":2.0}}}` | 196:Out → 194:In; 194:Out → 216:In1 |
| `sts_wbr_charter_hill.questphase / h4544 / 203` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_07_tr_casino"}}` | 151:Out → 203:In; 203:Out → 186:In |
| `sts_wbr_charter_hill.questphase / h4544 / 210` | `questLogicalXorNodeDefinition` `{}` | 127:Out → 210:In2; 210:Out1 → 128:Succeeded; 211:Out → 210:In1 |
| `sts_wbr_charter_hill.questphase / h4544 / 213` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_hil_07_shard"}}}` | 213:Out → 159:Succeeded; 186:Out → 213:In |
| `sts_wbr_charter_hill.questphase / h4544 / 216` | `questLogicalXorNodeDefinition` `{}` | 149:Out → 216:In2; 194:Out → 216:In1; 216:Out1 → 197:Succeeded |
| `sts_wbr_charter_hill.questphase / h4544 / 217` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115159699771","comparisonType":"Greater"}}}` | 146:Out → 217:In; 217:Out → 193:In; 217:Out → 195:Succeeded; 217:Out → 199:In |
| `sts_wbr_hil_07_bugfixing.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 9:Out → 8:In |
| `sts_wbr_hil_07_bugfixing.questphase / h10 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-622577","value":1,"comparisonType":"Equal"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wbr_hil_07_bugfixing.questphase / h10 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_hil_07_cleanup_fix","value":1,"comparisonType":"Equal"}}}` | 3:Out → 10:In; 10:False → 11:In |
| `sts_wbr_hil_07_bugfixing.questphase / h10 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_finished","value":1,"comparisonType":"Equal"}}}` | 10:False → 11:In; 11:True → 12:In |
| `sts_wbr_hil_07_bugfixing.questphase / h10 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_07_tr_quest"},{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}]}}` | 12:Out → 4:In; 11:True → 12:In |
| `sts_wbr_hil_07_bugfixing.questphase / h120 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-622569","value":1,"comparisonType":"Equal"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_wbr_hil_07_bugfixing.questphase / h120 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 5:In |
| `sts_wbr_hil_07_ow.questphase / h12 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_com_civs"},"comparisonParams":{"$type":"questComparisonParam","count":23,"comparisonType":"GreaterOrEqual"}}}}` | 42:Out → 23:In; 23:Out → 62:In2 |
| `sts_wbr_hil_07_ow.questphase / h12 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#wbr_hil_foodshop_02"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 43:Out → 44:In; 44:Out → 62:In3 |
| `sts_wbr_hil_07_ow.questphase / h12 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_com_enemies"},"comparisonParams":{"$type":"questComparisonParam","count":23,"comparisonType":"GreaterOrEqual"}}}}` | 48:Out → 47:In; 47:Out → 62:In1 |
| `sts_wbr_hil_07_ow.questphase / h12 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_quest"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 68:Out → 67:In; 67:Out → 69:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_casino_inside_02"}}` | 171:Out1 → 127:In; 127:Out → 210:In2 |
| `sts_wbr_hil_07_ow.questphase / h169 / 131` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_second_flor"}}}` | 129:Out → 131:In; 131:Out → 132:Succeeded |
| `sts_wbr_hil_07_ow.questphase / h169 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_den_trigger_001"}}` | 129:Out → 133:In; 141:Out → 133:In; 133:Out → 142:Succeeded; 133:Out → 163:Inactive |
| `sts_wbr_hil_07_ow.questphase / h169 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115159699771","comparisonType":"Greater"}}}` | 196:Out → 149:In; 149:Out → 216:In2 |
| `sts_wbr_hil_07_ow.questphase / h169 / 165` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_backdoor"}}}` | 0:Out → 165:In; 165:Out → 164:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 169` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_track"}}}` | 78:Out → 169:In; 169:True → 123:Active; 169:True → 160:Active; 169:False → 160:Active; 169:False → 172:Active |
| `sts_wbr_hil_07_ow.questphase / h169 / 171` | `questLogicalXorNodeDefinition` `{}` | 123:Out → 171:In1; 171:Out1 → 127:In; 172:Out → 171:In2; 171:Out1 → 211:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_casino"}}` | 183:Out → 182:In; 185:Out → 183:In; 188:Out → 183:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_07_tr_casino"}}` | 182:Out → 184:In; 184:Out → 185:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 191` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_token_quest"}}}}` | 0:Out → 191:In; 191:Out → 192:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#hil_07_objective_loot"},"timeInterval":2.0}}}` | 196:Out → 194:In; 194:Out → 216:In1 |
| `sts_wbr_hil_07_ow.questphase / h169 / 203` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_07_tr_casino"}}` | 151:Out → 203:In; 203:Out → 186:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 204` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 204:In; 204:False → 188:Active; 204:True → 221:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 210` | `questLogicalXorNodeDefinition` `{}` | 127:Out → 210:In2; 210:Out1 → 128:Succeeded; 211:Out → 210:In1 |
| `sts_wbr_hil_07_ow.questphase / h169 / 211` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#hil_07_tr_casino_inside_01"}}` | 171:Out1 → 211:In; 211:Out → 210:In1 |
| `sts_wbr_hil_07_ow.questphase / h169 / 213` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_hil_07_shard"}}}` | 213:Out → 159:Succeeded; 186:Out → 213:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 216` | `questLogicalXorNodeDefinition` `{}` | 149:Out → 216:In2; 194:Out → 216:In1; 216:Out1 → 197:Succeeded |
| `sts_wbr_hil_07_ow.questphase / h169 / 217` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115159699771","comparisonType":"Greater"}}}` | 146:Out → 217:In; 217:Out → 193:In; 217:Out → 195:Succeeded; 217:Out → 199:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 219` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_07\\scenes\\sts_wbr_hil_07_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 219:Out → 173:In; 201:Out → 219:In |
| `sts_wbr_hil_07_ow.questphase / h169 / 221` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 221:True → 188:Active; 221:False → 200:Start1; 204:True → 221:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_comabt"}}}` | 7:True → 5:In1; 7:False → 6:In1; 48:Out → 7:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 22:Out → 20:In; 40:Out → 22:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\charter_hill\\sts_wbr_hil_07\\scenes\\sts_wbr_hil_07_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 39:Out → 1:In; 38:Out → 39:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 41` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 41:False → 11:Start1; 20:Out → 41:In; 41:True → 42:Active |
| `sts_wbr_hil_07_ow.questphase / h602 / 46` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 46:False → 18:In; 45:Out → 46:In; 46:True → 47:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#hil_07_inside_location_area"}}` | 48:Out → 7:In; 48:Out → 15:In; 51:Out → 48:In |
| `sts_wbr_hil_07_ow.questphase / h602 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":4}}}` | 51:Out → 48:In; 49:Out → 51:In |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":800}}}` | 58:666:0 → 249:0:1; 249:0:0 → 251:0:1; 257:0:0 → 249:0:1; 261:1:0 → 249:0:0; 261:1:0 → 249:1026:0 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 251:0:1; 251:0:0 → 253:0:1; 261:1:0 → 251:0:0; 261:1:0 → 251:1026:0 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":800}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 261:1:0 → 253:0:0; 261:1:0 → 253:1026:0 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 255` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 253:0:0 → 255:0:1; 255:0:0 → 259:0:1; 255:0:1 → 257:0:0 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 58:666:0 → 273:0:1; 273:0:0 → 261:0:0 |
| `sts_wbr_hil_07_holocall_debrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 64:0:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 62:0:0 → 63:0:1; 67:0:0 → 62:0:1 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 66:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 60:666:0 → 267:0:1; 267:0:0 → 269:0:0 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 60:666:0 → 273:0:1; 269:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wbr_hil_07_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 269:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `mq036_quest_bugfixes.questphase / h870 / 223` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 211:False → 223:In; 218:Out → 223:In; 223:True → 224:In; 223:False → 228:In |
| `mq036_quest_bugfixes.questphase / h870 / 228` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 223:False → 228:In; 227:Out → 228:In; 228:True → 229:In; 228:False → 235:In |
| `mq036_quest_bugfixes.questphase / h870 / 229` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115159699771","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 228:True → 229:In; 229:True → 234:In; 229:False → 230:In |
| `mq036_quest_bugfixes.questphase / h870 / 235` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 228:False → 235:In; 234:Out → 235:In; 235:True → 236:In; 235:False → 240:In |
| `open_world_bugfixing.questphase / h674 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_finished"}}}` | 0:Out → 28:In; 28:True → 29:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hil_07_finished"}}}` | 0:Out → 28:In; 28:True → 29:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wbr_hil_07_ow.questphase / h12 / 23; sts_wbr_hil_07_ow.questphase / h12 / 44; sts_wbr_hil_07_ow.questphase / h12 / 47 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_wbr_hil_07_ow.questphase / h12 / 59; sts_wbr_hil_07_ow.questphase / h169 / 201; sts_wbr_hil_07_ow.questphase / h169 / 78 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_wbr_hil_07_bugfixing.questphase / h10 / 6; sts_wbr_hil_07_bugfixing.questphase / h10 / 7; sts_wbr_hil_07_bugfixing.questphase / h10 / 8; sts_wbr_hil_07_ow.questphase / h12 / 42; +8 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1792 / 28; open_world_bugfixing.questphase / h674 / 28; sts_wbr_charter_hill.questphase / h4544 / 131; sts_wbr_charter_hill.questphase / h4544 / 169; +20 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wbr_hil_07_ow.questphase / h169 / 182; sts_wbr_hil_07_ow.questphase / h169 / 185; sts_wbr_hil_07_ow.questphase / h169 / 186; sts_wbr_hil_07_ow.questphase / h602 / 20; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 227; sts_wbr_charter_hill.questphase / h4544 / 175; sts_wbr_hil_07_ow.questphase / h169 / 175 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wbr_hil_07_bugfixing.questphase / h10 / 4; sts_wbr_hil_07_bugfixing.questphase / h10 / 5; sts_wbr_hil_07_bugfixing.questphase / h120 / 5; sts_wbr_hil_07_ow.questphase / h12 / 54; +6 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | sts_wbr_hil_07_bugfixing.questphase / h10 / 12; sts_wbr_hil_07_ow.questphase / h602 / 51 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 229; sts_wbr_charter_hill.questphase / h4544 / 149; sts_wbr_charter_hill.questphase / h4544 / 217; sts_wbr_hil_07_ow.questphase / h169 / 149; +1 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1792 / 29; open_world_bugfixing.questphase / h674 / 29; sts_wbr_charter_hill.questphase / h4544 / 123; sts_wbr_charter_hill.questphase / h4544 / 128; +36 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | sts_wbr_charter_hill.questphase / h4544 / 176; sts_wbr_hil_07_bugfixing.questphase / h10 / 3; sts_wbr_hil_07_bugfixing.questphase / h120 / 3; sts_wbr_hil_07_holocall_debrief.scene / scene / 259; +26 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wbr_charter_hill.questphase / h4544 / 171; sts_wbr_charter_hill.questphase / h4544 / 210; sts_wbr_charter_hill.questphase / h4544 / 216; sts_wbr_hil_07_ow.questphase / h169 / 171; +2 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wbr_hil_07_holocall_debrief.scene / scene / 249; sts_wbr_hil_07_holocall_debrief.scene / scene / 253; sts_wbr_hil_07_holocall_prebrief.scene / scene / 273; sts_wbr_hil_07_holocall_prebrief.scene / scene / 281; +1 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_wbr_hil_07_ow.questphase / h602 / 12 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_wbr_charter_hill.questphase / h4544 / 191; sts_wbr_hil_07_ow.questphase / h169 / 191 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_wbr_hil_07_ow.questphase / h169 / 200; sts_wbr_hil_07_ow.questphase / h602 / 11 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wbr_charter_hill.questphase / h4544 / 133; sts_wbr_charter_hill.questphase / h4544 / 203; sts_wbr_hil_07_bugfixing.questphase / h10 / 12; sts_wbr_hil_07_ow.questphase / h12 / 67; +7 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` | repair; journal anchor | `base-sts-wbr-hil-07` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` | content candidate; journal anchor | `base-sts-wbr-hil-07` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wbr-hil-07` |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wbr-hil-07` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wbr-hil-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wbr-hil-07.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

166 repeated typed/socket path signatures in this selected graph context; 14 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 64 -> 283 -> 281 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h602 / 49 -> 51 -> 48 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 63 -> 65 -> 60 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 59 -> 62 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 29 -> 63 -> 65 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 279 -> 64 -> 283 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `6497920d6ce0ac894daa` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h602 / 45 -> 46 -> 47 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 56 -> 279 -> 64 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h10 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase` / h4544 / 133 -> 142 -> 196 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 273 -> 261 -> 249 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h0 / 4 | `h10` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h0 / 10 | `h120` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":2,"socketName":"In2"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Out2"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h0 / 4 | `h169` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":173,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h0 / 5 | `h602` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h602 / 5 | `h630` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h602 / 6 | `h651` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.gamedef` | content candidate | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.quest |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07_test.gamedef` | content candidate | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.quest |
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
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_after_phase.questphase` | phase flow | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\quest_phase\sts_wbr_hil_06_quest_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\lipsync\en\sts_wbr_hil_07_holocall_debrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\lipsync\en\sts_wbr_hil_07_holocall_prebrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_tc` | base\quest\main_quests\part1\q105\scenes\q105_02c_to_dollhouse.scene / scene / 931; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 143; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h4278 / 124; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h4544 / 179; 10 total source locations in compressed evidence |
| `hil_07_after_holocall` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h4977 / 45; 1 total source locations in compressed evidence |
| `hil_07_comabt` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h1407 / 13; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase / h27 / 13; 2 total source locations in compressed evidence |
| `hil_07_gang_retaliation` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h1407 / 22; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase / h27 / 22; 2 total source locations in compressed evidence |
| `hil_07_spawned` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h4387 / 41; 1 total source locations in compressed evidence |
| `hil_07_start` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h4544 / 87; 1 total source locations in compressed evidence |
| `hil_07_track` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.quest / h0 / 3; 1 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 63; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 903; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 199; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 27; 61 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 895; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 293; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 42; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 528; 26 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejectable` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 629; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1206; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 288; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 254; 25 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejected` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 637; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1214; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 290; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 256; 17 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 62; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 901; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 198; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 26; 75 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 891; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 292; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 41; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 575; 25 total source locations in compressed evidence |
| `sts_tygerclaws_retaliation` | base\open_world\street_stories\street_stories_gang_retaliation.questphase / h2439 / 23; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h5350 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h1874 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h3468 / 41; 12 total source locations in compressed evidence |
| `sts_wbr_hil_07_cleanup_fix` | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h4977 / 38; 1 total source locations in compressed evidence |
| `wbr_achievement` | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase / h0 / 40; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase / h0 / 68; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase / h0 / 51; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase / h0 / 60; 39 total source locations in compressed evidence |

NodeRef uses: 60; TweakDB binding uses: 10. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
