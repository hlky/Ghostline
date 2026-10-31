# Gig: Greed Never Pays

Journal: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` · `StreetStory` · hash `2542047576`.

Journal premise: Gig type: Search and Recovery\nObjective: Retrieve Leah Gladen's lockbreaker device\nLocation: Building on the corner of Holly and Floyd St, door code 2137\nDetails:\n\nA great treasure can turn out to be a great curse. Remember that, V.\n\nOne of the fences in my territory, Leah Gladen, came into possession of some highly valuable equipment – a lockbreak device capable of jailbreaking corp cyberware (some call it a CorpCracker). This tech opens doors for suits who want out but don't want to lose function of corp-issued chrome or are looking to make an extra eddie by selling secondhand.\n\nLeah wasn't born yesterday. She knows what the tech is worth. She and I went back and forth, long price negotiations. We were close to reaching a deal when all contact was lost.\n\nYour job is to find out what happened to Leah – but more importantly to get that skeleton key for me. Don't bother reporting back until you have it. Don't waste time.

**Coverage: journal-linked.** 64 exact journal-linked nodes in 6 resources; 8 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Get out of Wired Head. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape` |
| Reach the hidden room. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` |
| Go to Leah Gladen's apartment block. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` |
| Deposit the equipment at the Drop Point. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` |
| Enter code 2137. (Optional) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` |
| Go to Leah Gladen's apartment. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment` |
| Go to the braindance club Wired Head. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples` |
| Go to the braindance club Wired Head. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/go_to_bd_bar` |
| Take Leah Gladen's equipment. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker` |
| Search Leah Gladen's apartment. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` |
| Search the hidden room. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room` |
| Search Wired Head. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wbr_japantown.questphase / h5450 / 24` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 90:True → 24:Active; 24:Out → 105:In1 |
| `sts_wbr_japantown.questphase / h5450 / 26` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 25:Out → 26:Succeeded; 26:Out → 97:Active; 26:Out → 114:In1 |
| `sts_wbr_japantown.questphase / h5450 / 27` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 99:Out → 27:Active; 27:Out → 127:In; 27:Out → 154:In |
| `sts_wbr_japantown.questphase / h5450 / 29` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room` | 28:Out → 29:Succeeded; 29:Out → 147:In |
| `sts_wbr_japantown.questphase / h5450 / 30` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples` | 147:Out → 30:Active; 30:Out → 93:In |
| `sts_wbr_japantown.questphase / h5450 / 91` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 90:False → 91:Active; 91:Out → 105:In2 |
| `sts_wbr_japantown.questphase / h5450 / 97` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment` | 26:Out → 97:Active; 97:Out → 98:In |
| `sts_wbr_japantown.questphase / h5450 / 99` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment` | 99:Out → 27:Active; 98:Out → 99:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 106` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/brief` | 150:Out → 106:Active |
| `sts_wbr_japantown.questphase / h5450 / 108` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker/corpo_cracker` | 105:Out1 → 108:Inactive |
| `sts_wbr_japantown.questphase / h5450 / 116` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 114:Out2 → 116:Inactive |
| `sts_wbr_japantown.questphase / h5450 / 131` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 135:Out → 131:Active |
| `sts_wbr_japantown.questphase / h5450 / 132` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 133:True → 132:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 133` (Condition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 133:True → 132:Succeeded; 134:Out → 133:In |
| `sts_wbr_japantown.questphase / h5450 / 135` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 127:Out → 135:Succeeded; 135:Out → 131:Active |
| `sts_wbr_japantown.questphase / h5450 / 136` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 137:True → 136:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 137` (Condition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 134:Out → 137:In; 137:True → 136:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 138` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room` | 138:Out → 28:In; 134:Out → 138:Active |
| `sts_wbr_japantown.questphase / h5642 / 4` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 13:Out → 4:Active; 4:Out → 7:In; 4:Out → 8:In |
| `sts_wbr_japantown.questphase / h5642 / 9` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 9:Out → 1:In; 7:Out → 9:Succeeded; 8:Out → 9:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 3` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar` | 103:Out → 3:Active; 3:Out → 71:In1 |
| `sts_wbr_japantown.questphase / h6048 / 10` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar` | 100:Out → 10:Succeeded; 10:Out → 98:Active |
| `sts_wbr_japantown.questphase / h6048 / 11` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` | 67:Out → 11:Active; 11:Out → 102:In |
| `sts_wbr_japantown.questphase / h6048 / 40` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | 50:Out → 40:Succeeded; 40:Out → 47:In |
| `sts_wbr_japantown.questphase / h6048 / 50` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` | 50:Out → 40:Succeeded; 102:Out → 50:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 64` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape` | 78:Out → 64:Active; 64:Out → 66:In |
| `sts_wbr_japantown.questphase / h6048 / 67` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape` | 67:Out → 11:Active; 92:Out → 67:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 98` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker` | 10:Out → 98:Active; 98:Out → 78:In |
| `sts_wbr_japantown.questphase / h6048 / 99` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker` | 78:Out → 99:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 103` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples` | 103:Out → 3:Active; 73:Out → 103:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 24` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 90:True → 24:Active; 24:Out → 105:In1 |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 26` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 25:Out → 26:Succeeded; 26:Out → 97:Active; 26:Out → 114:In1 |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 27` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 99:Out → 27:Active; 27:Out → 127:In; 27:Out → 154:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 29` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room` | 28:Out → 29:Succeeded; 29:Out → 147:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 30` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples` | 147:Out → 30:Active; 30:Out → 93:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 91` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_apartment_block` | 90:False → 91:Active; 91:Out → 105:In2 |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 97` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment` | 26:Out → 97:Active; 97:Out → 98:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 99` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_into_ozzies_apartment` | 99:Out → 27:Active; 98:Out → 99:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 106` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/brief` | 150:Out → 106:Active |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 108` (MappinManager) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker/corpo_cracker` | 105:Out1 → 108:Inactive |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 116` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 114:Out2 → 116:Inactive |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 131` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 135:Out → 131:Active |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 132` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 133:True → 132:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 133` (Condition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way` | 133:True → 132:Succeeded; 134:Out → 133:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 135` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 127:Out → 135:Succeeded; 135:Out → 131:Active |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 136` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 137:True → 136:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 137` (Condition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence` | 134:Out → 137:In; 137:True → 136:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 138` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_secret_room` | 138:Out → 28:In; 134:Out → 138:Active |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 4` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 13:Out → 4:Active; 4:Out → 7:In; 4:Out → 8:In |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 9` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/use_code` | 9:Out → 1:In; 7:Out → 9:Succeeded; 8:Out → 9:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 3` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar` | 103:Out → 3:Active; 3:Out → 71:In1 |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 10` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/secure_evidence_in_bd_bar` | 100:Out → 10:Succeeded; 10:Out → 98:Active |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 11` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` | 67:Out → 11:Active; 11:Out → 102:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 40` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | 50:Out → 40:Succeeded; 40:Out → 47:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 50` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` | 50:Out → 40:Succeeded; 102:Out → 50:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 64` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape` | 78:Out → 64:Active; 64:Out → 66:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 67` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/escape` | 67:Out → 11:Active; 92:Out → 67:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 98` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker` | 10:Out → 98:Active; 98:Out → 78:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 99` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/retrive_corpo_cracker` | 78:Out → 99:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 103` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/get_to_the_comples` | 103:Out → 3:Active; 73:Out → 103:Succeeded |
| `sts_wbr_jpn_12_silverhand.scene / scene / 214` (PauseCondition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | 46:0:0 → 214:0:1; 214:0:0 → 216:0:0; input mappings: 0:0=CutDestination, 0:1=In |
| `mq036_quest_bugfixes.questphase / h870 / 235` (Condition) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint` | 228:False → 235:In; 234:Out → 235:In; 235:True → 236:In; 235:False → 240:In |
| `open_world_bugfixing.questphase / h674 / 18` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | 17:True → 18:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 18` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12` | 17:True → 18:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wbr_jpn_12_openworld.questphase / h75 / 53` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene`; `#sts_sm_wbr_jpn_12_silverhand` | 57:Out → 53:silverhand_first_location_start |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 148` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene`; `#sts_sm_wat_jpn_12_holocall_prebrief` | 148:rejected_out → 126:Active; 148:End1 → 126:Active; 164:False → 148:Start1; 148:Holocall INT → 152:In; 148:Holocall RET → 151:In |
| `sts_wbr_jpn_12b_openworld.questphase / h74 / 4` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene`; `#sts_sm_wbr_jpn_12_silverhand` | 0:Out → 4:silverhand_second_location_start |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 30` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene`; `#sts_sm_wat_jpn_12_holocall_debrief` | 30:End1 → 15:In; 30:Holocall RET → 31:In; 30:Holocall INT → 32:In; 43:False → 30:Start1; 30:rejected_out → 44:Active |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\sts_westbrook.questphase` / h0 / 3 | `sts_wbr_japantown.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h6450 / 3 | `sts_wbr_jpn_12_openworld.questphase` | 0: Input; 0:Out → 3:In1; 3:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12a.questphase` / h0 / 3 | `sts_wbr_jpn_12_openworld.questphase` | 0: Input; 0:Out → 3:In1; 3:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h1691 / 3 | `sts_wbr_jpn_12b_openworld.questphase` | 0: Input; 0:Out → 3:In1; 3:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b.questphase` / h0 / 3 | `sts_wbr_jpn_12b_openworld.questphase` | 0: Input; 0:Out → 3:In1; 3:Out1 → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h6262 / 30 | `sts_wat_jpn_12_holocall_debrief.scene` | 43: Condition; 30:End1 → 15:In; 30:Holocall RET → 31:In; 30:Holocall INT → 32:In; 43:False → 30:Start1; 30:rejected_out → 44:Active |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h305 / 30 | `sts_wat_jpn_12_holocall_debrief.scene` | 43: Condition; 30:End1 → 15:In; 30:Holocall RET → 31:In; 30:Holocall INT → 32:In; 43:False → 30:Start1; 30:rejected_out → 44:Active |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h5450 / 148 | `sts_wat_jpn_12_holocall_prebrief.scene` | 164: Condition; 148:rejected_out → 126:Active; 148:End1 → 126:Active; 164:False → 148:Start1; 148:Holocall INT → 152:In; 148:Holocall RET → 151:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h104 / 148 | `sts_wat_jpn_12_holocall_prebrief.scene` | 164: Condition; 148:rejected_out → 126:Active; 148:End1 → 126:Active; 164:False → 148:Start1; 148:Holocall INT → 152:In; 148:Holocall RET → 151:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h5421 / 53 | `sts_wbr_jpn_12_silverhand.scene` | 57: PauseCondition: q101_done; 57:Out → 53:silverhand_first_location_start |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h6031 / 4 | `sts_wbr_jpn_12_silverhand.scene` | 0: Input; 0:Out → 4:silverhand_second_location_start |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h75 / 53 | `sts_wbr_jpn_12_silverhand.scene` | 57: PauseCondition: q101_done; 57:Out → 53:silverhand_first_location_start |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h74 / 4 | `sts_wbr_jpn_12_silverhand.scene` | 0: Input; 0:Out → 4:silverhand_second_location_start |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 8 | `sts_westbrook.questphase` | 0: Input; 0:Out → 8:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h1612 / 15 | `sts_wbr_jpn_12a.questphase` | 0: Input; 0:Out → 15:In1; 15:Out1 → 16:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_main_phase.questphase` / h0 / 15 | `sts_wbr_jpn_12a.questphase` | 0: Input; 0:Out → 15:In1; 15:Out1 → 16:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\quests\sts_wbr_jpn_12b_quest.quest` / h0 / 16 | `sts_wbr_jpn_12a.questphase` | 16:Out1 → 17:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h1612 / 16 | `sts_wbr_jpn_12b.questphase` | 15: Phase: sts_wbr_jpn_12a.questphase; 21: PauseCondition: jpn_12_second_location_active; 16:Out1 → 14:In; 15:Out1 → 16:In1; 21:Out → 16:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_main_phase.questphase` / h0 / 16 | `sts_wbr_jpn_12b.questphase` | 15: Phase: sts_wbr_jpn_12a.questphase; 21: PauseCondition: jpn_12_second_location_active; 16:Out1 → 14:In; 15:Out1 → 16:In1; 21:Out → 16:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\quests\sts_wbr_jpn_12b_quest.quest` / h0 / 17 | `sts_wbr_jpn_12b.questphase` | 0: Start; 16: Phase: sts_wbr_jpn_12a.questphase; 0:Out → 17:In1; 16:Out1 → 17:In1 |
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
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h0 / 13 | `sts_wbr_jpn_12_main_phase.questphase` | 57: Journal; 57:Out → 13:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_quest.quest` / h0 / 18 | `sts_wbr_jpn_12_main_phase.questphase` | 19: FactsDBManager: jpn_12_test_definition; 19:Out → 18:In1; 18:Out1 → 21:In |
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
| `sts_wat_jpn_12_holocall_debrief.scene` | Start1 → rejected_out, End1 | fixer; 23 nodes / 30 edges |
| `sts_wat_jpn_12_holocall_prebrief.scene` | Start1 → End1, rejected_out | fixer; 22 nodes / 25 edges |
| `sts_wbr_jpn_12_silverhand.scene` | silverhand_first_location_start, silverhand_second_location_start → silverhand_second_location_end, silverhand_first_location_end | Silverhand; Player; 72 nodes / 80 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_wbr_jpn_12_silverhand.scene / n422 / 0` | Proszę, proszę. (``) | No option-level predicate stored | 0:0 → 425:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `#jpn_12_mail_read` | Producer outside selected context | sts_wbr_japantown.questphase / h5450 / 28; sts_wbr_jpn_12_openworld.questphase / h104 / 28; sts_wbr_jpn_12_silverhand.scene / scene / 169 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wat_jpn_12_holocall_prebrief.scene / scene / 279 |
| `holo_setup_active` | Producer outside selected context | sts_wat_jpn_12_holocall_debrief.scene / scene / 251; sts_wat_jpn_12_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wat_jpn_12_holocall_debrief.scene / scene / 251; sts_wat_jpn_12_holocall_prebrief.scene / scene / 279 |
| `holo_wakako_calls_v_end_activate` | sts_wat_jpn_12_holocall_debrief.scene / scene / 65; sts_wat_jpn_12_holocall_prebrief.scene / scene / 65; sts_wbr_jpn_12_openworld.questphase / h104 / 152; sts_wbr_jpn_12b_openworld.questphase / h305 / 32 | No reader in selected context |
| `holo_wakako_calls_v_end_done` | sts_wat_jpn_12_holocall_debrief.scene / scene / 61; sts_wat_jpn_12_holocall_prebrief.scene / scene / 61 | sts_wat_jpn_12_holocall_debrief.scene / scene / 60; sts_wat_jpn_12_holocall_prebrief.scene / scene / 60 |
| `holo_wakako_calls_v_rejectable` | sts_wat_jpn_12_holocall_debrief.scene / scene / 279; sts_wat_jpn_12_holocall_prebrief.scene / scene / 254; sts_wat_jpn_12_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_wakako_calls_v_rejected` | sts_wat_jpn_12_holocall_debrief.scene / scene / 281; sts_wat_jpn_12_holocall_prebrief.scene / scene / 256 | sts_wat_jpn_12_holocall_debrief.scene / scene / 283; sts_wat_jpn_12_holocall_prebrief.scene / scene / 258 |
| `holo_wakako_calls_v_start_activate` | sts_wat_jpn_12_holocall_debrief.scene / scene / 259; sts_wat_jpn_12_holocall_debrief.scene / scene / 64; sts_wat_jpn_12_holocall_prebrief.scene / scene / 283; sts_wat_jpn_12_holocall_prebrief.scene / scene / 64; sts_wbr_jpn_12_openworld.questphase / h104 / 151; sts_wbr_jpn_12b_openworld.questphase / h305 / 31 | sts_wat_jpn_12_holocall_debrief.scene / scene / 251 |
| `holo_wakako_calls_v_start_done` | sts_wat_jpn_12_holocall_debrief.scene / scene / 59; sts_wat_jpn_12_holocall_prebrief.scene / scene / 59 | sts_wat_jpn_12_holocall_debrief.scene / scene / 273; sts_wat_jpn_12_holocall_prebrief.scene / scene / 267 |
| `jpn_12_after_holocall` | sts_wbr_jpn_12b_openworld.questphase / h305 / 45 | No reader in selected context |
| `jpn_12_button_clicked` | sts_wbr_jpn_12_silverhand.scene / scene / 157 | sts_wbr_jpn_12_silverhand.scene / scene / 129 |
| `jpn_12_finished` | sts_wbr_jpn_12b_openworld.questphase / h91 / 54 | open_world_bugfixing.questphase / h1792 / 17; open_world_bugfixing.questphase / h674 / 17 |
| `jpn_12_gang_retaliation` | Producer outside selected context | sts_wbr_jpn_12b_openworld.questphase / h305 / 46 |
| `jpn_12_johnny_clue` | sts_wbr_jpn_12_silverhand.scene / scene / 151 | No reader in selected context |
| `jpn_12_movable_object_scanned` | sts_wbr_jpn_12_silverhand.scene / scene / 131 | sts_wbr_japantown.questphase / h5450 / 127; sts_wbr_jpn_12_openworld.questphase / h104 / 127; sts_wbr_jpn_12_silverhand.scene / scene / 38 |
| `jpn_12_optional_code` | sts_wbr_jpn_12_silverhand.scene / scene / 141 | sts_wbr_japantown.questphase / h5642 / 13; sts_wbr_jpn_12_openworld.questphase / h296 / 13 |
| `jpn_12_test_definition` | Producer outside selected context | sts_wbr_japantown.questphase / h5450 / 90; sts_wbr_jpn_12_openworld.questphase / h104 / 90 |
| `jpn_12a_finished` | sts_wbr_japantown.questphase / h5450 / 93; sts_wbr_jpn_12_openworld.questphase / h104 / 93 | No reader in selected context |
| `jpn_12a_start` | sts_wbr_jpn_12_openworld.questphase / h104 / 94 | No reader in selected context |
| `jpn_12b_finished` | sts_wbr_japantown.questphase / h6048 / 47; sts_wbr_jpn_12b_openworld.questphase / h91 / 47 | No reader in selected context |
| `jpn_12b_start` | sts_wbr_jpn_12b_openworld.questphase / h91 / 46 | No reader in selected context |
| `q101_done` | Producer outside selected context | sts_wbr_jpn_12_openworld.questphase / h75 / 57 |
| `sts_tygerclaws_retaliation` | sts_wbr_jpn_12b_openworld.questphase / h305 / 47 | No reader in selected context |
| `sts_wbr_jpn_12_corpo_cracker` | Producer outside selected context | sts_wbr_japantown.questphase / h6048 / 102; sts_wbr_jpn_12b_openworld.questphase / h91 / 102 |
| `wbr_achievement` | sts_wbr_jpn_12b_openworld.questphase / h305 / 19 | sts_wbr_jpn_12b_openworld.questphase / h305 / 33 |

## Exact gates, joins and cancellation

<details><summary>109 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wbr_japantown.questphase / h5450 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_galden_building"}}` | 105:Out1 → 25:In; 25:Out → 26:Succeeded; 25:Out → 155:In |
| `sts_wbr_japantown.questphase / h5450 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#jpn_12_mail_read","value":1,"comparisonType":"GreaterOrEqual"}}}` | 138:Out → 28:In; 28:Out → 29:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 90` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_test_definition","value":1,"comparisonType":"GreaterOrEqual"}}}` | 90:True → 24:Active; 94:Out → 90:In; 90:False → 91:Active |
| `sts_wbr_japantown.questphase / h5450 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_inside_ozzies_apartment"}}` | 97:Out → 98:In; 98:Out → 99:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 105` | `questLogicalXorNodeDefinition` `{}` | 24:Out → 105:In1; 105:Out1 → 25:In; 91:Out → 105:In2; 105:Out1 → 108:Inactive; 105:Out1 → 119:In; 105:Out1 → 120:In; 105:Out1 → 121:In; 105:Out1 → 118:In; 105:Out1 → 125:In; 105:Out1 → 141:In; 105:Out1 → 150:In |
| `sts_wbr_japantown.questphase / h5450 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_movable_object_scanned"}}}` | 27:Out → 127:In; 134:CutSource → 127:CutDestination; 127:Out → 135:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 133` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 133:True → 132:Succeeded; 134:Out → 133:In |
| `sts_wbr_japantown.questphase / h5450 / 134` | `questCutControlNodeDefinition` `{}` | 134:CutSource → 127:CutDestination; 134:Out → 133:In; 154:Out → 134:In; 134:Out → 137:In; 134:Out → 138:Active |
| `sts_wbr_japantown.questphase / h5450 / 137` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 134:Out → 137:In; 137:True → 136:Succeeded |
| `sts_wbr_japantown.questphase / h5450 / 154` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#jpn_12_dvc_movable_fridge_activator","eventType":"Executed"}}}` | 27:Out → 154:In; 154:Out → 134:In |
| `sts_wbr_japantown.questphase / h5642 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_inside_ozzies_apartment"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `sts_wbr_japantown.questphase / h5642 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/collective_ps_test_world_002/area/loc_sts_wbr_jpn_12_prefabEFJ2WSA/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 4:Out → 7:In; 7:Out → 9:Succeeded |
| `sts_wbr_japantown.questphase / h5642 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_westbrook/japan_town/loc_sts_wbr_jpn_12_prefabVPQQKEI/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 4:Out → 8:In; 8:Out → 9:Succeeded |
| `sts_wbr_japantown.questphase / h5642 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_optional_code"}}}` | 0:Out → 13:In; 13:Out → 4:Active |
| `sts_wbr_japantown.questphase / h6048 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_12b_tr_wired_head_inside"}}` | 64:Out → 66:In; 66:Out → 92:In |
| `sts_wbr_japantown.questphase / h6048 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_wired_head_inside"}}` | 46:Out → 73:In; 73:Out → 103:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"146850840587","quantity":1}}}` | 78:Out → 64:Active; 98:Out → 78:In; 78:Out → 87:In; 78:Out → 99:Succeeded |
| `sts_wbr_japantown.questphase / h6048 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_device_close"}}` | 100:Out → 10:Succeeded; 71:Out1 → 100:In |
| `sts_wbr_japantown.questphase / h6048 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_jpn_12_corpo_cracker"}}}` | 11:Out → 102:In; 102:Out → 50:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h12 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12a_tr_activator"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 8:Out → 3:In; 9:Out → 8:In |
| `sts_wbr_jpn_12_openworld.questphase / h75 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done"}}}` | 57:Out → 53:silverhand_first_location_start; 58:Out → 57:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_galden_building"}}` | 105:Out1 → 25:In; 25:Out → 26:Succeeded; 25:Out → 155:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#jpn_12_mail_read","value":1,"comparisonType":"GreaterOrEqual"}}}` | 138:Out → 28:In; 28:Out → 29:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 90` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_test_definition","value":1,"comparisonType":"GreaterOrEqual"}}}` | 90:True → 24:Active; 94:Out → 90:In; 90:False → 91:Active |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_inside_ozzies_apartment"}}` | 97:Out → 98:In; 98:Out → 99:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 105` | `questLogicalXorNodeDefinition` `{}` | 24:Out → 105:In1; 105:Out1 → 25:In; 91:Out → 105:In2; 105:Out1 → 108:Inactive; 105:Out1 → 119:In; 105:Out1 → 120:In; 105:Out1 → 121:In; 105:Out1 → 118:In; 105:Out1 → 125:In; 105:Out1 → 141:In; 105:Out1 → 150:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_movable_object_scanned"}}}` | 27:Out → 127:In; 134:CutSource → 127:CutDestination; 127:Out → 135:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 133` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/find_the_way","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 133:True → 132:Succeeded; 134:Out → 133:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 134` | `questCutControlNodeDefinition` `{}` | 134:CutSource → 127:CutDestination; 134:Out → 133:In; 154:Out → 134:In; 134:Out → 137:In; 134:Out → 138:Active |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 137` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/search_the_apartment_for_evidence","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 134:Out → 137:In; 137:True → 136:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 143` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_galden_building"}}` | 126:Out → 143:In; 143:Out → 142:In; 145:Out → 143:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 144` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_12_tr_galden_building"}}` | 142:Out → 144:In; 144:Out → 145:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 149` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 149:In; 149:False → 126:Active; 149:True → 164:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 154` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#jpn_12_dvc_movable_fridge_activator","eventType":"Executed"}}}` | 27:Out → 154:In; 154:Out → 134:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 157` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_12_movable_fridge"},"eventType":"Finished"}}}` | 119:Out → 157:In; 157:Out → 158:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 158` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 158:Out → 156:In; 157:Out → 158:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#jpn_12_dvc_movable_fridge_activator","eventType":"Executed"}}}` | 120:Out → 159:In; 159:Out → 161:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 162:Out → 92:In; 93:Out → 162:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_12\\scenes\\sts_wat_jpn_12_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 163:Out → 1:In; 146:Out → 163:In |
| `sts_wbr_jpn_12_openworld.questphase / h104 / 164` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 164:True → 126:Active; 164:False → 148:Start1; 149:True → 164:In |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_inside_ozzies_apartment"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/collective_ps_test_world_002/area/loc_sts_wbr_jpn_12_prefabEFJ2WSA/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 4:Out → 7:In; 7:Out → 9:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_westbrook/japan_town/loc_sts_wbr_jpn_12_prefabVPQQKEI/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 4:Out → 8:In; 8:Out → 9:Succeeded |
| `sts_wbr_jpn_12_openworld.questphase / h296 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_optional_code"}}}` | 0:Out → 13:In; 13:Out → 4:Active |
| `sts_wbr_jpn_12b_openworld.questphase / h12 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#jpn_12b_com_galden"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 4:Out → 5:In; 5:Out → 9:In |
| `sts_wbr_jpn_12b_openworld.questphase / h12 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_activator"}]}}` | 9:Out → 6:In; 6:Out → 7:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_12b_tr_wired_head_inside"}}` | 64:Out → 66:In; 66:Out → 92:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_wired_head_inside"}}` | 46:Out → 73:In; 73:Out → 103:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"146850840587","quantity":1}}}` | 78:Out → 64:Active; 98:Out → 78:In; 78:Out → 87:In; 78:Out → 99:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_content_lock"}}` | 0:Out → 89:In; 89:Out → 88:In; 91:Out → 89:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_12b_tr_content_lock"}}` | 88:Out → 90:In; 90:Out → 91:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_device_close"}}` | 100:Out → 10:Succeeded; 71:Out1 → 100:In |
| `sts_wbr_jpn_12b_openworld.questphase / h91 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wbr_jpn_12_corpo_cracker"}}}` | 11:Out → 102:In; 102:Out → 50:Succeeded |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 42:Out → 36:In; 36:Out → 43:In |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_12\\scenes\\sts_wat_jpn_12_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 40:Out → 1:In; 41:Out → 40:In |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 26:Out → 41:In; 41:Out → 40:In |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 36:Out → 43:In; 43:False → 30:Start1; 43:True → 44:Active |
| `sts_wbr_jpn_12b_openworld.questphase / h305 / 46` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 46:False → 28:In; 45:Out → 46:In; 46:True → 47:In |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 58:666:0 → 249:0:1; 249:0:0 → 251:0:1; 257:0:0 → 249:0:1; 261:1:0 → 249:0:0; 261:1:0 → 249:1026:0 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 251:0:1; 251:0:0 → 253:0:1; 261:1:0 → 251:0:0; 261:1:0 → 251:1026:0 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 261:1:0 → 253:0:0; 261:1:0 → 253:1026:0 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 255` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 253:0:0 → 255:0:1; 255:0:0 → 259:0:1; 255:0:1 → 257:0:0 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 58:666:0 → 273:0:1; 273:0:0 → 261:0:0 |
| `sts_wat_jpn_12_holocall_debrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 64:0:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 64:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 58:666:0 → 267:0:1; 267:0:0 → 269:0:0 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 58:666:0 → 273:0:1; 269:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_jpn_12_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 269:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 38` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_movable_object_scanned","value":1,"comparisonType":"GreaterOrEqual"}}}` | 38:0:0 → 22:0:0; 38:0:1 → 41:0:0; 303:0:1 → 38:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 47:0:0 → 49:0:0; 319:0:1 → 47:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 55:0:0 → 57:0:0; 326:0:1 → 55:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 61:0:0 → 63:0:0; 327:0:1 → 61:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_silverhand_doors"}}` | 1:0:0 → 80:0:1; 80:0:0 → 263:0:1; 99:1:0 → 80:0:0; 107:1:0 → 80:0:0 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 86` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/collective_ps_test_world_002/area/loc_sts_wbr_jpn_12_prefabEFJ2WSA/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 1:0:0 → 86:0:1; 86:0:0 → 88:0:0; 107:1:0 → 86:0:0 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_westbrook/japan_town/loc_sts_wbr_jpn_12_prefabVPQQKEI/loc_sts_wbr_jpn_12_gameplay_prefabI3CDVXA/loc_sts_wbr_jpn_12_devices_prefabSB2BL6Q/d_scav_b_t_1_eng_prefabAZ4NZIA/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 1:0:0 → 87:0:1; 87:0:0 → 88:0:1; 107:1:0 → 87:0:0 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12_tr_silverhand_inside_window"}}` | 1:0:0 → 104:0:1; 99:1:0 → 104:0:0; 104:0:0 → 107:0:0 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 129` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_button_clicked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 129:0:0 → 455:0:0; 129:0:1 → 294:0:1; 131:0:0 → 129:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:0:0 → 140:0:1; 140:0:0 → 233:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 12:0:0 → 146:0:1; 146:0:0 → 287:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 155` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#jpn_12_dvc_movable_fridge_activator","eventType":"Executed"}}}` | 1:0:0 → 155:0:1; 155:0:0 → 157:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 165` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 22:0:0 → 165:0:1; 41:0:0 → 165:0:1; 165:0:0 → 254:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 169` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#jpn_12_mail_read","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 169:0:1; 169:0:0 → 312:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 27:0:0 → 177:0:1; 177:0:0 → 260:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 189` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 49:0:0 → 189:0:1; 189:0:0 → 340:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_device"}}` | 46:0:0 → 192:0:1; 192:0:0 → 319:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 57:0:0 → 199:0:1; 199:0:0 → 343:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 203` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_tr_ozzie_found"}}` | 46:0:0 → 203:0:1; 203:0:0 → 326:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 206` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 63:0:0 → 206:0:1; 206:0:0 → 346:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12","fileEntryIndex":4,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 46:0:0 → 214:0:1; 214:0:0 → 216:0:0 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 233` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 140:0:0 → 233:0:1; 233:0:0 → 264:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 248` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 17:0:0 → 248:0:1; 248:0:0 → 298:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 165:0:0 → 254:0:1; 254:0:0 → 307:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 260` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 177:0:0 → 260:0:1; 260:0:0 → 316:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 287` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 146:0:0 → 287:0:1; 287:0:0 → 285:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 340` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 189:0:0 → 340:0:1; 340:0:0 → 320:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 343` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 199:0:0 → 343:0:1; 343:0:0 → 321:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 346` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_wbr_jpn_12_silverhand_Silverhand"},"timeInterval":2.0,"angleTolerance":90.0,"inverted":true}}}` | 206:0:0 → 346:0:1; 346:0:0 → 322:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 440` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 425:0:0 → 440:0:1; 440:0:0 → 131:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 449` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_12b_front_entrance_johnny"}}` | 46:0:0 → 449:0:1; 449:0:0 → 327:0:1 |
| `sts_wbr_jpn_12_silverhand.scene / scene / 458` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_12b_tr_wired_head_inside"}}` | 320:0:0 → 458:0:1; 458:0:0 → 216:0:0 |
| `mq036_quest_bugfixes.questphase / h870 / 228` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 223:False → 228:In; 227:Out → 228:In; 228:True → 229:In; 228:False → 235:In |
| `mq036_quest_bugfixes.questphase / h870 / 235` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 228:False → 235:In; 234:Out → 235:In; 235:True → 236:In; 235:False → 240:In |
| `mq036_quest_bugfixes.questphase / h870 / 236` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"146850840587","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 235:True → 236:In; 236:True → 239:In; 236:False → 237:In |
| `mq036_quest_bugfixes.questphase / h870 / 240` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 235:False → 240:In; 239:Out → 240:In; 240:True → 241:In; 240:False → 253:In |
| `open_world_bugfixing.questphase / h674 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_finished"}}}` | 0:Out → 17:In; 17:True → 18:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_12_finished"}}}` | 0:Out → 17:In; 17:True → 18:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_wbr_jpn_12_silverhand.scene / scene / 47; sts_wbr_jpn_12_silverhand.scene / scene / 55; sts_wbr_jpn_12_silverhand.scene / scene / 61; sts_wbr_jpn_12b_openworld.questphase / h12 / 5 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_wbr_japantown.questphase / h5450 / 150; sts_wbr_jpn_12_openworld.questphase / h104 / 150; sts_wbr_jpn_12_openworld.questphase / h104 / 92; sts_wbr_jpn_12_openworld.questphase / h12 / 5; +2 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_wbr_jpn_12_silverhand.scene / scene / 422 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_wbr_jpn_12b_openworld.questphase / h12 / 4; sts_wbr_jpn_12b_openworld.questphase / h305 / 24; sts_wbr_jpn_12b_openworld.questphase / h305 / 25; sts_wbr_jpn_12b_openworld.questphase / h305 / 26; +1 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1792 / 17; open_world_bugfixing.questphase / h674 / 17; sts_wat_jpn_12_holocall_debrief.scene / scene / 251; sts_wat_jpn_12_holocall_debrief.scene / scene / 273; +21 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wbr_japantown.questphase / h6048 / 92; sts_wbr_jpn_12_openworld.questphase / h104 / 142; sts_wbr_jpn_12_openworld.questphase / h104 / 145; sts_wbr_jpn_12_openworld.questphase / h104 / 146; +5 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 234; sts_wbr_jpn_12_openworld.questphase / h104 / 119; sts_wbr_jpn_12_openworld.questphase / h104 / 120; sts_wbr_jpn_12_openworld.questphase / h104 / 121; +6 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wbr_jpn_12b_openworld.questphase / h12 / 8; sts_wbr_jpn_12b_openworld.questphase / h305 / 22; sts_wbr_jpn_12b_openworld.questphase / h305 / 23; sts_wbr_jpn_12b_openworld.questphase / h305 / 29 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_wbr_japantown.questphase / h5642 / 7; sts_wbr_japantown.questphase / h5642 / 8; sts_wbr_jpn_12_openworld.questphase / h296 / 7; sts_wbr_jpn_12_openworld.questphase / h296 / 8; +2 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 236; sts_wbr_japantown.questphase / h6048 / 78; sts_wbr_jpn_12b_openworld.questphase / h91 / 78 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1792 / 18; open_world_bugfixing.questphase / h674 / 18; sts_wbr_japantown.questphase / h5450 / 106; sts_wbr_japantown.questphase / h5450 / 116; +57 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | sts_wat_jpn_12_holocall_debrief.scene / scene / 259; sts_wat_jpn_12_holocall_debrief.scene / scene / 279; sts_wat_jpn_12_holocall_debrief.scene / scene / 281; sts_wat_jpn_12_holocall_debrief.scene / scene / 59; +29 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wbr_japantown.questphase / h5450 / 105; sts_wbr_jpn_12_openworld.questphase / h104 / 105 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wat_jpn_12_holocall_debrief.scene / scene / 249; sts_wat_jpn_12_holocall_debrief.scene / scene / 253; sts_wat_jpn_12_holocall_prebrief.scene / scene / 273; sts_wat_jpn_12_holocall_prebrief.scene / scene / 281; +12 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_wbr_japantown.questphase / h5450 / 134; sts_wbr_jpn_12_openworld.questphase / h104 / 134 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_wbr_jpn_12b_openworld.questphase / h305 / 15 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_wbr_jpn_12_openworld.questphase / h104 / 157 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_wbr_jpn_12_openworld.questphase / h104 / 148; sts_wbr_jpn_12_openworld.questphase / h75 / 53; sts_wbr_jpn_12b_openworld.questphase / h305 / 30; sts_wbr_jpn_12b_openworld.questphase / h74 / 4 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wbr_japantown.questphase / h5450 / 25; sts_wbr_japantown.questphase / h5450 / 98; sts_wbr_japantown.questphase / h5642 / 2; sts_wbr_japantown.questphase / h6048 / 100; +20 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `workspot_performance` | sts_wbr_jpn_12_silverhand.scene / scene / 263; sts_wbr_jpn_12_silverhand.scene / scene / 264; sts_wbr_jpn_12_silverhand.scene / scene / 274; sts_wbr_jpn_12_silverhand.scene / scene / 281; +13 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` | content candidate; journal anchor | `base-sts-wbr-jpn-12` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` | content candidate; journal anchor | `base-sts-wbr-jpn-12` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wbr-jpn-12` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wbr-jpn-12` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene` | content candidate; journal anchor | `base-sts-wbr-jpn-12` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wbr-jpn-12](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wbr-jpn-12.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

207 repeated typed/socket path signatures in this selected graph context; 32 distinct direct resource identities; 11 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `215ca95d939006973a7d` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h91 / 47 -> 54 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `20a77143a898bc753a26` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h305 / 24 -> 25 -> 27 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 64 -> 283 -> 281 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 63 -> 65 -> 60 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 59 -> 62 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 29 -> 63 -> 65 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `c8705a8da51824b73252` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h104 / 0 -> 94 -> 90 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 279 -> 64 -> 283 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `6497920d6ce0ac894daa` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h305 / 45 -> 46 -> 47 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` / scene / 56 -> 279 -> 64 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h5450 / 25 -> 26 -> 97 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h5450 / 114 | `h5642` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Out2"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h0 / 3 | `h68` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h68 / 2 | `h75` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h0 / 4 | `h104` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` / h104 / 114 | `h296` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Out2"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h0 / 3 | `h67` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h67 / 3 | `h74` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h0 / 4 | `h91` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` / h0 / 5 | `h305` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_def.gamedef` | content candidate | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_quest.quest |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_nc.gamedef` | content candidate | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_quest.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01b_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01b_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_main_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12a.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\lipsync\en\sts_wat_jpn_12_holocall_debrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\lipsync\en\sts_wat_jpn_12_holocall_prebrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\lipsync\en\sts_wbr_jpn_12_silverhand\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\lipsync\en\sts_wbr_jpn_12_silverhand\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 63; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 903; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 199; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 27; 61 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 895; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 293; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 42; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 528; 26 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejectable` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 629; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1206; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 288; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 254; 25 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejected` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 637; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1214; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 290; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 256; 17 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 62; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 901; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 198; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 26; 75 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 891; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 292; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 41; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 575; 25 total source locations in compressed evidence |
| `jpn_12_after_holocall` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h6262 / 45; 1 total source locations in compressed evidence |
| `jpn_12_finished` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h6048 / 54; 1 total source locations in compressed evidence |
| `jpn_12_gang_retaliation` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h1460 / 28; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_combat.questphase / h34 / 28; 2 total source locations in compressed evidence |
| `jpn_12_test_definition` | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\sts_wbr_jpn_12_quest.quest / h0 / 19; 1 total source locations in compressed evidence |
| `jpn_12a_start` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h5450 / 94; 1 total source locations in compressed evidence |
| `jpn_12b_start` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h6048 / 46; 1 total source locations in compressed evidence |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `sts_tygerclaws_retaliation` | base\open_world\street_stories\street_stories_gang_retaliation.questphase / h2439 / 23; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h5350 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h1874 / 56; base\open_world\street_stories\watson\little_china\sts_wat_little_china.questphase / h3468 / 41; 12 total source locations in compressed evidence |
| `wbr_achievement` | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase / h0 / 40; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase / h0 / 68; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase / h0 / 51; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase / h0 / 60; 39 total source locations in compressed evidence |

NodeRef uses: 92; TweakDB binding uses: 11. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene` | 1 / 1 | scnDialogLineEvent: 1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene` | 9 / 24 | scnDialogLineEvent: 24 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
