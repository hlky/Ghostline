# Gig: Family Matters

Journal: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` · `StreetStory` · hash `3432934147`.

Journal premise: Gig type: Search and Recover\nObjective: Retrieve the Zetatech data Juliet Horrigan owes El Capitán\nLocation: House on Gibson St.\nDetails:\n\nI like everyone to know I'm patient, understanding. I realize there's a time for work and a time for family. Without a good work-life balance we'd all blast our brains out. I get it, I do. But... disappearing for 2 weeks cuz of "family issues?" That how Juliet thinks of me? How much she respects me? I love her cuz she's ripped so much nova data outta Zetatech for me, but man she's starting to hurt my feelings, you know?\n\nGo to her place, see what her deal is. But remember – #1 priority is that data she still owes me. Juliet's nova and all, but if she's got a problem with that, well... like I said, data is prio #1.

**Coverage: journal-linked.** 43 exact journal-linked nodes in 4 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Deposit the datashard in the Drop Point. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` |
| Find a way to open the safe. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` |
| Get the chip from Juliet's home. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/get_datachip` |
| Go to Juliet's home. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` |
| Look for the chip. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house` |
| Exit the building. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/leave_house` |
| Take the chip from the safe. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/loot_datachip` |
| Open the safe. (Primary) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` |
| Find out what happened to Juliet. (Optional) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_std_rancho_corronado.questphase / h543 / 4` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 44:False → 4:Active; 4:Out → 57:In1 |
| `sts_std_rancho_corronado.questphase / h543 / 6` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 43:Out1 → 6:Succeeded; 6:Out → 31:Active; 6:Out → 7:Active |
| `sts_std_rancho_corronado.questphase / h543 / 7` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house` | 6:Out → 7:Active; 7:Out → 8:In; 7:Out → 16:In |
| `sts_std_rancho_corronado.questphase / h543 / 9` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 59:True → 9:Succeeded; 9:Out → 39:In |
| `sts_std_rancho_corronado.questphase / h543 / 10` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` | 39:False → 10:Active; 41:Out → 10:Active; 10:Out → 53:In |
| `sts_std_rancho_corronado.questphase / h543 / 13` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` | 53:Out → 13:Succeeded; 13:Out → 14:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 14` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` | 13:Out → 14:Succeeded; 14:Out → 88:In |
| `sts_std_rancho_corronado.questphase / h543 / 18` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 16:Out → 18:Active; 18:Out → 20:In |
| `sts_std_rancho_corronado.questphase / h543 / 22` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 20:Out → 22:Succeeded; 22:Out → 26:Active |
| `sts_std_rancho_corronado.questphase / h543 / 26` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 22:Out → 26:Active |
| `sts_std_rancho_corronado.questphase / h543 / 31` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 6:Out → 31:Active; 31:Out → 63:In; 31:Out → 86:In; 31:Out → 87:In |
| `sts_std_rancho_corronado.questphase / h543 / 38` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 65:Out1 → 38:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 39` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 9:Out → 39:In; 39:False → 10:Active; 59:False → 39:In; 39:True → 41:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 41` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 41:Out → 10:Active; 39:True → 41:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 45` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 44:True → 45:Active; 45:Out → 57:In1 |
| `sts_std_rancho_corronado.questphase / h543 / 49` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/briefing` | 0:Out → 49:Active |
| `sts_std_rancho_corronado.questphase / h543 / 58` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house` | 8:Out → 58:Succeeded; 58:Out → 76:In |
| `sts_std_rancho_corronado.questphase / h543 / 59` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 59:True → 9:Succeeded; 59:False → 39:In; 61:False → 59:In; 62:Out → 59:In |
| `sts_std_rancho_corronado.questphase / h543 / 61` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 11:Out → 61:In; 61:False → 59:In; 61:True → 62:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 62` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 62:Out → 59:In; 61:True → 62:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 4` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 44:False → 4:Active; 4:Out → 57:In1 |
| `sts_std_rcr_05_openworld.questphase / h128 / 6` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 43:Out1 → 6:Succeeded; 6:Out → 31:Active; 6:Out → 7:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 7` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house` | 6:Out → 7:Active; 7:Out → 8:In; 7:Out → 16:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 9` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 59:True → 9:Succeeded; 9:Out → 39:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 10` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` | 39:False → 10:Active; 41:Out → 10:Active; 10:Out → 53:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 13` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` | 53:Out → 13:Succeeded; 13:Out → 14:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 14` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` | 13:Out → 14:Succeeded; 14:Out → 88:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 18` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 16:Out → 18:Active; 18:Out → 20:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 22` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 20:Out → 22:Succeeded; 22:Out → 26:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 26` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 22:Out → 26:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 31` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 6:Out → 31:Active; 31:Out → 63:In; 31:Out → 86:In; 31:Out → 87:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 38` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 65:Out1 → 38:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 39` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 9:Out → 39:In; 39:False → 10:Active; 59:False → 39:In; 39:True → 41:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 41` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate` | 41:Out → 10:Active; 39:True → 41:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 45` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house` | 44:True → 45:Active; 45:Out → 57:In1 |
| `sts_std_rcr_05_openworld.questphase / h128 / 49` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/briefing` | 0:Out → 49:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 58` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house` | 8:Out → 58:Succeeded; 58:Out → 76:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 59` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe` | 59:True → 9:Succeeded; 59:False → 39:In; 61:False → 59:In; 62:Out → 59:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 61` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 11:Out → 61:In; 61:False → 59:In; 61:True → 62:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 62` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe` | 62:Out → 59:In; 61:True → 62:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 211` (Condition) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver` | 210:False → 211:In; 217:Out → 211:In; 211:True → 212:In; 211:False → 223:In |
| `open_world_bugfixing.questphase / h864 / 17` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` | 16:True → 17:Succeeded |
| `open_world_bugfixing.questphase / h1999 / 17` (Journal) | `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05` | 16:True → 17:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_std_rcr_05_openworld.questphase / h128 / 79` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene`; `#sts_sm_std_rcr_05_holocall_prebrief` | 79:End 0 → 78:Active; 79:rejected_out → 78:Active; 89:False → 79:Start 0; 79:Holocall INT → 82:In; 79:Holocall RET → 81:In |
| `sts_std_rcr_05_openworld.questphase / h566 / 11` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene`; `#sts_sm_std_rcr_05_holocall_debriefs` | 11:End 0 → 5:In; 26:False → 11:Start 0; 11:rejected_out → 27:Active; 11:Holocall INT → 13:In; 11:Holocall RET → 12:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 15` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 96:Out → 15:sedatives |
| `sts_std_rcr_05_openworld.questphase / h736 / 20` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 98:Out → 20:painting |
| `sts_std_rcr_05_openworld.questphase / h736 / 24` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 98:Out → 24:safe |
| `sts_std_rcr_05_openworld.questphase / h736 / 49` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 89:False → 49:found_out |
| `sts_std_rcr_05_openworld.questphase / h736 / 56` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 96:Out → 56:blood |
| `sts_std_rcr_05_openworld.questphase / h736 / 62` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 96:Out → 62:medkit |
| `sts_std_rcr_05_openworld.questphase / h736 / 68` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`; `#sts_sm_std_rcr_05_clues` | 97:False → 68:rose_room |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\sts_santo_domingo.questphase` / h0 / 3 | `sts_std_rancho_corronado.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h4011 / 10 | `sts_std_rcr_05_openworld.questphase` | 14: Condition: rcr_05_finished; 10:Out1 → 1:In; 14:False → 10:In1 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05.questphase` / h0 / 10 | `sts_std_rcr_05_openworld.questphase` | 14: Condition: rcr_05_finished; 10:Out1 → 1:In; 14:False → 10:In1 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 15 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 15:sedatives |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 20 | `sts_std_rcr_05_clues.scene` | 98: PauseCondition: #rcr_05_tr_ground_floor; 98:Out → 20:painting |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 24 | `sts_std_rcr_05_clues.scene` | 98: PauseCondition: #rcr_05_tr_ground_floor; 98:Out → 24:safe |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 49 | `sts_std_rcr_05_clues.scene` | 89: Condition: rcr_05_johnny_scene_active; 89:False → 49:found_out |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 56 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 56:blood |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 62 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 62:medkit |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h1151 / 68 | `sts_std_rcr_05_clues.scene` | 97: Condition: rcr_05_johnny_scene_active; 97:False → 68:rose_room |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 15 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 15:sedatives |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 20 | `sts_std_rcr_05_clues.scene` | 98: PauseCondition: #rcr_05_tr_ground_floor; 98:Out → 20:painting |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 24 | `sts_std_rcr_05_clues.scene` | 98: PauseCondition: #rcr_05_tr_ground_floor; 98:Out → 24:safe |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 49 | `sts_std_rcr_05_clues.scene` | 89: Condition: rcr_05_johnny_scene_active; 89:False → 49:found_out |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 56 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 56:blood |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 62 | `sts_std_rcr_05_clues.scene` | 96: PauseCondition: #rcr_05_tr_first_floor; 96:Out → 62:medkit |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h736 / 68 | `sts_std_rcr_05_clues.scene` | 97: Condition: rcr_05_johnny_scene_active; 97:False → 68:rose_room |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h981 / 11 | `sts_std_rcr_05_holocall_debriefs.scene` | 26: Condition; 11:End 0 → 5:In; 26:False → 11:Start 0; 11:rejected_out → 27:Active; 11:Holocall INT → 13:In; 11:Holocall RET → 12:In |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h566 / 11 | `sts_std_rcr_05_holocall_debriefs.scene` | 26: Condition; 11:End 0 → 5:In; 26:False → 11:Start 0; 11:rejected_out → 27:Active; 11:Holocall INT → 13:In; 11:Holocall RET → 12:In |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h543 / 79 | `sts_std_rcr_05_holocall_prebrief.scene` | 89: Condition; 79:End 0 → 78:Active; 79:rejected_out → 78:Active; 89:False → 79:Start 0; 79:Holocall INT → 82:In; 79:Holocall RET → 81:In |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h128 / 79 | `sts_std_rcr_05_holocall_prebrief.scene` | 89: Condition; 79:End 0 → 78:Active; 79:rejected_out → 78:Active; 89:False → 79:Start 0; 79:Holocall INT → 82:In; 79:Holocall RET → 81:In |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 6 | `sts_santo_domingo.questphase` | 0: Input; 0:Out → 6:In1 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` / h0 / 10 | `sts_std_rcr_05.questphase` | 53: Journal; 65: Journal; 53:Out → 10:In1; 65:Out → 10:In1 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest` / h0 / 0 | `sts_std_rcr_05.questphase` | 4: PauseCondition: {"seconds": 5}; 4:Out → 0:In1; 0:Out1 → 2:In |
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
| `sts_std_rcr_05_clues.scene` | safe, sedatives, photo, painting, sedatives_no_johnny, painting_no_johnny, found_out, blood, medkit, rose_room, blood_no_johnny, medkit_no_johnny → safe_end, sedatives_end, painting_end, photo_end, found_out_end, blood_end, medkit_end, rose_room_end | johnny; Player; 89 nodes / 83 edges |
| `sts_std_rcr_05_holocall_debriefs.scene` | Start 0 → End 0, rejected_out | fixer; Player; 23 nodes / 30 edges |
| `sts_std_rcr_05_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; Player; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_std_rcr_05_clues.scene / n277 / 0` | Zestaw medyczny. (``) | No option-level predicate stored | 0:0 → 145:0:1 |
| `sts_std_rcr_05_clues.scene / n280 / 0` | O cholera... (``) | No option-level predicate stored | 0:0 → 132:0:1 |
| `sts_std_rcr_05_clues.scene / n285 / 0` | Co my tu mamy... (``) | No option-level predicate stored | 0:0 → 89:0:1 |
| `sts_std_rcr_05_clues.scene / n292 / 0` | Ciekawe. (``) | No option-level predicate stored | 0:0 → 104:0:1 |
| `sts_std_rcr_05_clues.scene / n295 / 0` | Zamknięte. (``) | No option-level predicate stored | 0:0 → 72:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_zetatech` | sts_std_rcr_05_openworld.questphase / h12 / 10 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_std_rcr_05_holocall_prebrief.scene / scene / 279 |
| `holo_muamar_calls_v_end_activate` | sts_std_rcr_05_holocall_debriefs.scene / scene / 67; sts_std_rcr_05_holocall_prebrief.scene / scene / 65; sts_std_rcr_05_openworld.questphase / h128 / 82; sts_std_rcr_05_openworld.questphase / h566 / 13 | No reader in selected context |
| `holo_muamar_calls_v_end_done` | sts_std_rcr_05_holocall_debriefs.scene / scene / 63; sts_std_rcr_05_holocall_prebrief.scene / scene / 61 | sts_std_rcr_05_holocall_debriefs.scene / scene / 62; sts_std_rcr_05_holocall_prebrief.scene / scene / 60 |
| `holo_muamar_calls_v_rejectable` | sts_std_rcr_05_holocall_debriefs.scene / scene / 279; sts_std_rcr_05_holocall_prebrief.scene / scene / 254; sts_std_rcr_05_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_muamar_calls_v_rejected` | sts_std_rcr_05_holocall_debriefs.scene / scene / 281; sts_std_rcr_05_holocall_prebrief.scene / scene / 256 | sts_std_rcr_05_holocall_debriefs.scene / scene / 283; sts_std_rcr_05_holocall_prebrief.scene / scene / 258 |
| `holo_muamar_calls_v_start_activate` | sts_std_rcr_05_holocall_debriefs.scene / scene / 262; sts_std_rcr_05_holocall_debriefs.scene / scene / 66; sts_std_rcr_05_holocall_prebrief.scene / scene / 283; sts_std_rcr_05_holocall_prebrief.scene / scene / 64; sts_std_rcr_05_openworld.questphase / h128 / 81; sts_std_rcr_05_openworld.questphase / h566 / 12 | sts_std_rcr_05_holocall_debriefs.scene / scene / 254 |
| `holo_muamar_calls_v_start_done` | sts_std_rcr_05_holocall_debriefs.scene / scene / 61; sts_std_rcr_05_holocall_prebrief.scene / scene / 59 | sts_std_rcr_05_holocall_debriefs.scene / scene / 249; sts_std_rcr_05_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_std_rcr_05_holocall_debriefs.scene / scene / 254; sts_std_rcr_05_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_std_rcr_05_holocall_debriefs.scene / scene / 254; sts_std_rcr_05_holocall_prebrief.scene / scene / 279 |
| `rcr_05_achievement_added` | Producer outside selected context | sts_std_rcr_05_openworld.questphase / h566 / 32 |
| `rcr_05_blood_conclusion` | sts_std_rcr_05_clues.scene / scene / 45 | No reader in selected context |
| `rcr_05_finished` | sts_std_rcr_05_openworld.questphase / h566 / 7 | open_world_bugfixing.questphase / h1999 / 16; open_world_bugfixing.questphase / h864 / 16 |
| `rcr_05_have_datachip` | sts_std_rancho_corronado.questphase / h543 / 11; sts_std_rcr_05_openworld.questphase / h128 / 11 | No reader in selected context |
| `rcr_05_johnny_scene_active` | sts_std_rcr_05_clues.scene / scene / 104; sts_std_rcr_05_clues.scene / scene / 122; sts_std_rcr_05_clues.scene / scene / 125; sts_std_rcr_05_clues.scene / scene / 132; sts_std_rcr_05_clues.scene / scene / 145; sts_std_rcr_05_clues.scene / scene / 152; sts_std_rcr_05_clues.scene / scene / 163; sts_std_rcr_05_clues.scene / scene / 167; sts_std_rcr_05_clues.scene / scene / 254; sts_std_rcr_05_clues.scene / scene / 263; sts_std_rcr_05_clues.scene / scene / 289; sts_std_rcr_05_clues.scene / scene / 72; sts_std_rcr_05_clues.scene / scene / 75; sts_std_rcr_05_clues.scene / scene / 89 | sts_std_rcr_05_openworld.questphase / h736 / 89; sts_std_rcr_05_openworld.questphase / h736 / 97 |
| `rcr_05_mail_01_read` | Producer outside selected context | sts_std_rcr_05_openworld.questphase / h736 / 46 |
| `rcr_05_mail_02_read` | Producer outside selected context | sts_std_rcr_05_openworld.questphase / h736 / 47 |
| `rcr_05_medkit_conclusion` | sts_std_rcr_05_clues.scene / scene / 48 | No reader in selected context |
| `rcr_05_painting_conclusion` | sts_std_rcr_05_clues.scene / scene / 51 | No reader in selected context |
| `rcr_05_pointed_to_safe` | sts_std_rcr_05_clues.scene / scene / 273 | sts_std_rancho_corronado.questphase / h543 / 16; sts_std_rcr_05_openworld.questphase / h128 / 16 |
| `rcr_05_sedatives_conclusion` | sts_std_rcr_05_clues.scene / scene / 57 | No reader in selected context |
| `rcr_05_start` | sts_std_rcr_05_openworld.questphase / h12 / 12 | No reader in selected context |
| `rcr_05_testdef` | Producer outside selected context | sts_std_rancho_corronado.questphase / h543 / 44; sts_std_rcr_05_openworld.questphase / h128 / 44 |
| `std_achievement` | sts_std_rcr_05_openworld.questphase / h566 / 10 | sts_std_rcr_05_openworld.questphase / h566 / 18 |
| `sts_std_rcr_05_datachip` | Producer outside selected context | sts_std_rancho_corronado.questphase / h543 / 53; sts_std_rcr_05_openworld.questphase / h128 / 53 |

## Exact gates, joins and cancellation

<details><summary>81 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_std_rancho_corronado.questphase / h543 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"127433217442","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 8:In; 8:Out → 54:In; 8:Out → 60:In; 8:Out → 77:In; 8:Out → 58:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_pointed_to_safe","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 16:In; 60:CutSource → 16:CutDestination; 16:Out → 18:Active |
| `sts_std_rancho_corronado.questphase / h543 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"121326050879","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 18:Out → 20:In; 60:CutSource → 20:CutDestination; 20:Out → 22:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:Out → 39:In; 39:False → 10:Active; 59:False → 39:In; 39:True → 41:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 43` | `questLogicalXorNodeDefinition` `{}` | 5:Out → 43:In1; 43:Out1 → 6:Succeeded; 42:Out → 43:In2 |
| `sts_std_rancho_corronado.questphase / h543 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_testdef"}}}` | 0:Out → 44:In; 44:False → 4:Active; 44:True → 45:Active |
| `sts_std_rancho_corronado.questphase / h543 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_std_rcr_05_datachip"}}}` | 10:Out → 53:In; 53:Out → 13:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 59` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 59:True → 9:Succeeded; 59:False → 39:In; 61:False → 59:In; 62:Out → 59:In |
| `sts_std_rancho_corronado.questphase / h543 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 11:Out → 61:In; 61:False → 59:In; 61:True → 62:Succeeded |
| `sts_std_rancho_corronado.questphase / h543 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rcr_05_dead_body"},"eventType":"Finished"}}}` | 31:Out → 63:In; 60:CutSource → 63:CutDestination; 63:Out → 65:In1 |
| `sts_std_rancho_corronado.questphase / h543 / 65` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 65:Out1 → 38:Succeeded; 63:Out → 65:In1; 85:Out → 65:In2; 87:Out → 65:In3 |
| `sts_std_rancho_corronado.questphase / h543 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rcr_05_dead_body"},"onScreenTest":true}}}` | 31:Out → 87:In; 60:CutSource → 87:CutDestination; 87:Out → 65:In3 |
| `sts_std_rancho_corronado.questphase / h543 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\rancho_corronado\\sts_std_rcr_05\\scenes\\sts_std_rcr_05_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 14:Out → 88:In; 88:Out → 70:In |
| `sts_std_rcr_05_openworld.questphase / h12 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 19:Out → 14:In; 23:Out → 19:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_ground_floor"}}` | 57:Out1 → 5:In; 5:Out → 43:In1 |
| `sts_std_rcr_05_openworld.questphase / h128 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"127433217442","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 8:In; 8:Out → 54:In; 8:Out → 60:In; 8:Out → 77:In; 8:Out → 58:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_pointed_to_safe","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 16:In; 60:CutSource → 16:CutDestination; 16:Out → 18:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"121326050879","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 18:Out → 20:In; 60:CutSource → 20:CutDestination; 20:Out → 22:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:Out → 39:In; 39:False → 10:Active; 59:False → 39:In; 39:True → 41:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_first_floor"}}` | 57:Out1 → 42:In; 42:Out → 43:In2 |
| `sts_std_rcr_05_openworld.questphase / h128 / 43` | `questLogicalXorNodeDefinition` `{}` | 5:Out → 43:In1; 43:Out1 → 6:Succeeded; 42:Out → 43:In2 |
| `sts_std_rcr_05_openworld.questphase / h128 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_testdef"}}}` | 0:Out → 44:In; 44:False → 4:Active; 44:True → 45:Active |
| `sts_std_rcr_05_openworld.questphase / h128 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_std_rcr_05_datachip"}}}` | 10:Out → 53:In; 53:Out → 13:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 59` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 59:True → 9:Succeeded; 59:False → 39:In; 61:False → 59:In; 62:Out → 59:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 60` | `questCutControlNodeDefinition` `{}` | 8:Out → 60:In; 60:CutSource → 16:CutDestination; 60:CutSource → 20:CutDestination; 60:CutSource → 63:CutDestination; 60:CutSource → 85:CutDestination; 60:CutSource → 87:CutDestination |
| `sts_std_rcr_05_openworld.questphase / h128 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 11:Out → 61:In; 61:False → 59:In; 61:True → 62:Succeeded |
| `sts_std_rcr_05_openworld.questphase / h128 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rcr_05_dead_body"},"eventType":"Finished"}}}` | 31:Out → 63:In; 60:CutSource → 63:CutDestination; 63:Out → 65:In1 |
| `sts_std_rcr_05_openworld.questphase / h128 / 65` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 65:Out1 → 38:Succeeded; 63:Out → 65:In1; 85:Out → 65:In2; 87:Out → 65:In3 |
| `sts_std_rcr_05_openworld.questphase / h128 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_block_tokens"}}` | 69:Out → 66:In; 78:Out → 66:In; 66:Out → 68:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_block_tokens"}}` | 68:Out → 67:In; 67:Out → 69:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 80` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 80:In; 80:False → 78:Active; 80:True → 89:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#rcr_05_dead_body","eventType":"Entered"}}}` | 60:CutSource → 85:CutDestination; 85:Out → 65:In2; 86:Out → 85:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rcr_05_dead_body"},"onScreenTest":true}}}` | 31:Out → 87:In; 60:CutSource → 87:CutDestination; 87:Out → 65:In3 |
| `sts_std_rcr_05_openworld.questphase / h128 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\santo_domingo\\rancho_corronado\\sts_std_rcr_05\\scenes\\sts_std_rcr_05_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 14:Out → 88:In; 88:Out → 70:In |
| `sts_std_rcr_05_openworld.questphase / h128 / 89` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 89:True → 78:Active; 89:False → 79:Start 0; 80:True → 89:In |
| `sts_std_rcr_05_openworld.questphase / h566 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 23:Out → 22:In; 22:Out → 24:In |
| `sts_std_rcr_05_openworld.questphase / h566 / 26` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 26:False → 11:Start 0; 24:Out → 26:In; 26:True → 27:Active |
| `sts_std_rcr_05_openworld.questphase / h566 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_achievement_added"}}}` | 32:False → 10:In; 32:True → 15:In; 9:Out → 32:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_mail_01_read"}}}` | 0:Out → 46:In; 46:Out → 54:In1 |
| `sts_std_rcr_05_openworld.questphase / h736 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_mail_02_read"}}}` | 0:Out → 47:In; 47:Out → 54:In2 |
| `sts_std_rcr_05_openworld.questphase / h736 / 54` | `questLogicalAndNodeDefinition` `{}` | 46:Out → 54:In1; 47:Out → 54:In2; 54:Out1 → 89:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"127433217442","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 80:Out → 75:In; 77:Out → 80:In; 80:Out → 81:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"121326050879","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 78:Out → 82:In; 82:Out → 84:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 89` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_johnny_scene_active"}}}` | 89:False → 49:found_out; 54:Out1 → 89:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_first_floor"}}` | 0:Out → 96:In; 96:Out → 15:sedatives; 96:Out → 56:blood; 96:Out → 62:medkit; 96:Out → 67:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_rose_room"}}` | 96:Out → 67:In; 67:Out → 97:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 97` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_johnny_scene_active"}}}` | 97:False → 68:rose_room; 67:Out → 97:In |
| `sts_std_rcr_05_openworld.questphase / h736 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rcr_05_tr_ground_floor"}}` | 0:Out → 98:In; 98:Out → 20:painting; 98:Out → 24:safe |
| `sts_std_rcr_05_clues.scene / scene / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_std_rcr_05_clues_johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 97:0:0 → 96:0:1; 289:0:0 → 97:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_ground_floor"}}` | 125:0:0 → 127:0:1; 127:0:0 → 126:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_rose_room"}}` | 140:0:0 → 139:0:1; 254:0:0 → 140:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 154` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_rose_room"}}` | 152:0:0 → 154:0:1; 154:0:0 → 153:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 169` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_rose_room"}}` | 167:0:0 → 169:0:1; 169:0:0 → 168:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 260` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_ground_floor"}}` | 260:0:0 → 110:0:1; 263:0:0 → 260:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rcr_05_tr_ground_floor"}}` | 75:0:0 → 267:0:1; 267:0:0 → 81:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 301` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 299:0:0 → 301:0:1; 301:0:0 → 93:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 311` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 309:0:0 → 311:0:1; 311:0:0 → 78:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 316:0:0 → 318:0:1; 318:0:0 → 105:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 325` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 323:0:0 → 325:0:1; 325:0:0 → 133:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 332` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 330:0:0 → 332:0:1; 332:0:0 → 147:0:1 |
| `sts_std_rcr_05_clues.scene / scene / 337` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"121326050879","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 337:0:1; 337:0:0 → 2:0:0 |
| `sts_std_rcr_05_clues.scene / scene / 340` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"121326050879","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 8:0:0 → 340:0:1; 340:0:0 → 9:0:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_end_done"}}}` | 62:0:0 → 63:0:1; 67:0:0 → 62:0:1 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_done"}}}` | 60:666:0 → 249:0:1; 249:0:0 → 272:0:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 252` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":100}}}` | 60:666:0 → 252:0:1; 252:0:0 → 254:0:1; 260:0:0 → 252:0:1; 272:1:0 → 252:0:0; 272:1:0 → 252:1026:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 252:0:0 → 254:0:1; 254:0:0 → 256:0:1; 272:1:0 → 254:0:0; 272:1:0 → 254:1026:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":100}}}` | 254:0:0 → 256:0:1; 256:0:0 → 258:0:1; 272:1:0 → 256:0:0; 272:1:0 → 256:1026:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 258` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 256:0:0 → 258:0:1; 258:0:0 → 262:0:1; 258:0:1 → 260:0:0 |
| `sts_std_rcr_05_holocall_debriefs.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_rejected"}}}` | 66:0:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_end_done"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_rejected"}}}` | 64:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_muamar_calls_v_start_done"}}}` | 58:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 58:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_std_rcr_05_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `mq036_quest_bugfixes.questphase / h870 / 210` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 210:True → 208:In; 308:Out → 210:In; 304:False → 210:In; 210:False → 211:In |
| `mq036_quest_bugfixes.questphase / h870 / 211` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 210:False → 211:In; 217:Out → 211:In; 211:True → 212:In; 211:False → 223:In |
| `mq036_quest_bugfixes.questphase / h870 / 212` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"127433217442","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 211:True → 212:In; 212:True → 218:In; 212:False → 213:In |
| `mq036_quest_bugfixes.questphase / h870 / 223` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 211:False → 223:In; 218:Out → 223:In; 223:True → 224:In; 223:False → 228:In |
| `open_world_bugfixing.questphase / h864 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_finished"}}}` | 0:Out → 16:In; 16:True → 17:Succeeded |
| `open_world_bugfixing.questphase / h1999 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rcr_05_finished"}}}` | 0:Out → 16:In; 16:True → 17:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | sts_std_rcr_05_openworld.questphase / h12 / 14; sts_std_rcr_05_openworld.questphase / h566 / 6 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_std_rcr_05_clues.scene / scene / 277; sts_std_rcr_05_clues.scene / scene / 280; sts_std_rcr_05_clues.scene / scene / 285; sts_std_rcr_05_clues.scene / scene / 292; +1 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_std_rcr_05_openworld.questphase / h566 / 8 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1999 / 16; open_world_bugfixing.questphase / h864 / 16; sts_std_rancho_corronado.questphase / h543 / 16; sts_std_rancho_corronado.questphase / h543 / 44; +17 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_std_rcr_05_openworld.questphase / h128 / 68; sts_std_rcr_05_openworld.questphase / h128 / 69; sts_std_rcr_05_openworld.questphase / h128 / 70; sts_std_rcr_05_openworld.questphase / h566 / 19; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 217; sts_std_rcr_05_clues.scene / scene / 60; sts_std_rcr_05_clues.scene / scene / 63; sts_std_rcr_05_clues.scene / scene / 66; +6 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_std_rcr_05_openworld.questphase / h12 / 22; sts_std_rcr_05_openworld.questphase / h12 / 23; sts_std_rcr_05_openworld.questphase / h12 / 25; sts_std_rcr_05_openworld.questphase / h12 / 26; +2 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 212; sts_std_rancho_corronado.questphase / h543 / 20; sts_std_rancho_corronado.questphase / h543 / 8; sts_std_rcr_05_clues.scene / scene / 337; +5 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1999 / 17; open_world_bugfixing.questphase / h864 / 17; sts_std_rancho_corronado.questphase / h543 / 10; sts_std_rancho_corronado.questphase / h543 / 13; +37 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_std_rcr_05_openworld.questphase / h736 / 54 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_std_rancho_corronado.questphase / h543 / 11; sts_std_rcr_05_clues.scene / scene / 104; sts_std_rcr_05_clues.scene / scene / 122; sts_std_rcr_05_clues.scene / scene / 125; +40 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_std_rancho_corronado.questphase / h543 / 43; sts_std_rancho_corronado.questphase / h543 / 65; sts_std_rcr_05_openworld.questphase / h128 / 43; sts_std_rcr_05_openworld.questphase / h128 / 65 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_std_rcr_05_clues.scene / scene / 301; sts_std_rcr_05_clues.scene / scene / 311; sts_std_rcr_05_clues.scene / scene / 318; sts_std_rcr_05_clues.scene / scene / 325; +6 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_std_rcr_05_openworld.questphase / h128 / 60 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_std_rcr_05_openworld.questphase / h566 / 5 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_std_rancho_corronado.questphase / h543 / 63; sts_std_rcr_05_openworld.questphase / h128 / 63 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_std_rcr_05_openworld.questphase / h128 / 79; sts_std_rcr_05_openworld.questphase / h566 / 11; sts_std_rcr_05_openworld.questphase / h736 / 15; sts_std_rcr_05_openworld.questphase / h736 / 20; +5 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_std_rcr_05_clues.scene / scene / 127; sts_std_rcr_05_clues.scene / scene / 140; sts_std_rcr_05_clues.scene / scene / 154; sts_std_rcr_05_clues.scene / scene / 169; +10 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `workspot_performance` | sts_std_rcr_05_clues.scene / scene / 105; sts_std_rcr_05_clues.scene / scene / 110; sts_std_rcr_05_clues.scene / scene / 118; sts_std_rcr_05_clues.scene / scene / 126; +10 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_std_rcr_05_openworld.questphase / h12 / 21; sts_std_rcr_05_openworld.questphase / h12 / 24; sts_std_rcr_05_openworld.questphase / h566 / 17 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` | content candidate; journal anchor | `base-sts-std-rcr-05` |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` | content candidate; forward dependency | `base-sts-std-rcr-05` |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-std-rcr-05` |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-std-rcr-05` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-std-rcr-05](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-std-rcr-05.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

179 repeated typed/socket path signatures in this selected graph context; 25 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 66 -> 283 -> 281 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 65 -> 67 -> 62 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 61 -> 64 -> 27 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 27 -> 65 -> 67 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 6 -> 13 -> 15 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 279 -> 66 -> 283 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 1 -> 279 -> 66 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 249 -> 272 -> 252 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` / scene / 285 -> 283 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `fe9d2c1bdd2cebf30eb2` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 64 -> 27 -> 65 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `3fe0ae98a8cf5496b004` | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h128 / 69 -> 66 -> 68 | questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h0 / 3 | `h122` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h0 / 4 | `h128` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h0 / 5 | `h566` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h0 / 6 | `h721` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h721 / 5 | `h730` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h721 / 6 | `h736` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

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
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.gamedef` | content candidate | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05_nc.gamedef` | content candidate | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05_test.gamedef` | content candidate | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest |
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
| `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\phases\sts_pac_wwd_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\phases\sts_pac_wwd_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\phases\sts_pac_wwd_05_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_01\phases\sts_std_rcr_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_01\phases\sts_std_rcr_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_01\phases\sts_std_rcr_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\phases\sts_std_rcr_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\phases\sts_std_rcr_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\phases\sts_std_rcr_03_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\phases\sts_std_rcr_03_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_clues\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_clues\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_holocall_debriefs\muamar_capitan_reyes.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_holocall_prebrief\muamar_capitan_reyes.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\lipsync\en\sts_std_rcr_05_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_zetatech` | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h427 / 10; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\phases\sts_std_arr_12_ow.questphase / h324 / 218; 2 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_muamar_calls_v_end_activate` | base\open_world\fixers\el_capitan\phases\el_capitan.questphase / h0 / 58; base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 83; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 283; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 285; 89 total source locations in compressed evidence |
| `holo_muamar_calls_v_end_done` | base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 79; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 193; base\quest\holocalls\muamar\muamar_holocall.scene / scene / 42; base\quest\holocalls\muamar\muamar_holocall.scene / scene / 556; 37 total source locations in compressed evidence |
| `holo_muamar_calls_v_rejectable` | base\quest\holocalls\muamar\muamar_holocall.scene / scene / 635; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 314; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 327; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene / scene / 254; 34 total source locations in compressed evidence |
| `holo_muamar_calls_v_rejected` | base\quest\holocalls\muamar\muamar_holocall.scene / scene / 643; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 316; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene / scene / 329; base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene / scene / 256; 23 total source locations in compressed evidence |
| `holo_muamar_calls_v_start_activate` | base\open_world\fixers\el_capitan\phases\el_capitan.questphase / h0 / 57; base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 82; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 282; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h1567 / 284; 108 total source locations in compressed evidence |
| `holo_muamar_calls_v_start_done` | base\open_world\fixers\el_capitan\scenes\muamar_reyes_default.scene / scene / 77; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h7953 / 6; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h8314 / 6; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 192; 37 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `rcr_05_achievement_added` | base\open_world\bugfixing\fixers\muamar_bugfixing.questphase / h22 / 42; 1 total source locations in compressed evidence |
| `rcr_05_finished` | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h981 / 7; 1 total source locations in compressed evidence |
| `rcr_05_start` | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rancho_corronado.questphase / h427 / 12; 1 total source locations in compressed evidence |
| `rcr_05_testdef` | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest / h0 / 3; 1 total source locations in compressed evidence |
| `std_achievement` | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase / h0 / 28; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase / h0 / 77; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase / h0 / 97; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase / h65 / 23; 80 total source locations in compressed evidence |

NodeRef uses: 88; TweakDB binding uses: 26. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` | 8 / 17 | scnDialogLineEvent: 17 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
