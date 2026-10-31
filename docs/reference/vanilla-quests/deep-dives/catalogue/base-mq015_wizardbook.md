# Spellbound

Journal: `quests/minor_quest/mq015_wizardbook` · `MinorQuest` · hash `2430424393`.

**Coverage: journal-linked.** 49 exact journal-linked nodes in 10 resources; 11 resources in the inspected dependency context.

Resource roles in that context: 10 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| A job from Nix? Should be interesting. Guy's got a rep for being an expert on antique tech, pre-Krash hardware. Decks, mag disks, yada yada yada. Some people'll tell you it's all as useful as a typewriter, a record player, a pile of dried cat shit. But me... I wouldn't be so sure about that. (Primary) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` |
| Wait for Nix's message. (Primary) | `quests/minor_quest/mq015_wizardbook/01_hook/01a_message_from_nix` |
| Check the ad on the illegal domain. (Primary) | `quests/minor_quest/mq015_wizardbook/01_hook/02_check_website` |
| Call R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller` |
| Go to the coordinates in the ad. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates` |
| Go to the coordinates given by R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1` |
| Talk to R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` |
| Defeat R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller` |
| Steal data from R3n0's computer. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/03_check_computer` |
| Steal data from R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data` |
| Wait for the stash coordinates from R3n0. (Primary) | `quests/minor_quest/mq015_wizardbook/02_restaurant/05_wait_for_contact` |
| Collect the goods from the stash. (Primary) | `quests/minor_quest/mq015_wizardbook/03_stash/01_go_to_coordinates` |
| Use your scanner to find the stash. (Primary) | `quests/minor_quest/mq015_wizardbook/03_stash/02_find_stash` |
| Open your Shards menu and decrypt the Book of Spells. (Optional) | `quests/minor_quest/mq015_wizardbook/03_stash/04_examine_tablet` |
| Open the stash. (Primary) | `quests/minor_quest/mq015_wizardbook/03_stash/03_open_stash` |
| Take the Book of Spells. (Primary) | `quests/minor_quest/mq015_wizardbook/03_stash/04_take_wizardbook` |
| Talk to Johnny. (Primary) | `quests/minor_quest/mq015_wizardbook/03_stash/05_talk_johnny` |
| Return to Nix. (Primary) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix` |
| Ask Nix about the book of spells. (Primary) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq015_quest_bugfixes.questphase / h37 / 3` (Condition) | `quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller` | 3:False → 1:In; 2:Out → 3:In; 3:True → 9:In |
| `mq015_01_hook.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller` | 17:False → 9:Active; 18:Out → 9:Active; 9:Out → 24:In; 9:Out → 59:Active |
| `mq015_01_hook.questphase / h0 / 17` (Condition) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 17:False → 9:Active; 53:Out → 17:In; 17:True → 18:Inactive |
| `mq015_01_hook.questphase / h0 / 18` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 18:Out → 9:Active; 17:True → 18:Inactive |
| `mq015_01_hook.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller` | 32:Out1 → 19:Succeeded; 19:Out → 26:In |
| `mq015_01_hook.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix/description` | 50:Out → 7:In; 50:Out → 8:in; 51:Out → 50:Active |
| `mq015_01_hook.questphase / h0 / 59` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller/contact` | 9:Out → 59:Active |
| `mq015_02_restaurant.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 51:Out → 2:Active; 2:Out → 13:In; 2:Out → 55:In; 2:Out → 64:In; 2:Out → 7:in |
| `mq015_02_restaurant.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1` | 3:Out1 → 4:Active; 4:Out → 14:In |
| `mq015_02_restaurant.questphase / h0 / 5` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1` | 14:Out → 5:Succeeded; 5:Out → 51:In |
| `mq015_02_restaurant.questphase / h0 / 6` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 7:out → 6:Succeeded; 6:Out → 17:In |
| `mq015_02_restaurant.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/03_check_computer` | 65:Out → 8:Active; 8:Out → 32:In |
| `mq015_02_restaurant.questphase / h0 / 12` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/03_check_computer` | 32:Out → 12:Succeeded; 12:Out → 37:In; 12:Out → 61:Succeeded |
| `mq015_02_restaurant.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 7:out_failed → 19:Failed; 19:Out → 27:Active |
| `mq015_02_restaurant.questphase / h0 / 27` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data` | 19:Out → 27:Active |
| `mq015_02_restaurant.questphase / h0 / 61` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data` | 12:Out → 61:Succeeded |
| `mq015_02_restaurant.questphase / h0 / 65` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 65:Out → 8:Active; 16:Out → 65:Succeeded |
| `mq015_02_restaurant_combat.questphase / h0 / 7` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 14:True → 7:Inactive; 7:Out → 19:In |
| `mq015_02_restaurant_combat.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller` | 19:False → 8:Active; 18:Out → 8:Active; 8:Out → 9:In |
| `mq015_02_restaurant_combat.questphase / h0 / 10` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller` | 9:Out → 10:Succeeded; 10:Out → 21:In |
| `mq015_02_restaurant_combat.questphase / h0 / 14` (Condition) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 14:True → 7:Inactive; 29:Out → 14:In; 27:False → 14:In; 14:False → 19:In |
| `mq015_02_restaurant_combat.questphase / h0 / 18` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data` | 18:Out → 8:Active; 19:True → 18:Inactive |
| `mq015_02_restaurant_combat.questphase / h0 / 19` (Condition) | `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data` | 7:Out → 19:In; 19:False → 8:Active; 14:False → 19:In; 19:True → 18:Inactive |
| `mq015_02_restaurant_combat.questphase / h0 / 27` (Condition) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1` | 11:Out1 → 27:In; 27:False → 14:In; 27:True → 29:Inactive |
| `mq015_02_restaurant_combat.questphase / h0 / 29` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1` | 29:Out → 14:In; 27:True → 29:Inactive |
| `mq015_02_restaurant_combat.questphase / h0 / 31` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/03_check_computer` | 22:Out → 31:Active |
| `mq015_03_stash.questphase / h0 / 3` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/01_go_to_coordinates` | 2:Out1 → 3:Active; 3:Out → 5:In |
| `mq015_03_stash.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/01_go_to_coordinates` | 21:Out → 4:Succeeded; 4:Out → 12:in |
| `mq015_04_afterlife.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq015_wizardbook` | 4:out → 8:Succeeded; 8:Out → 32:In |
| `mq015_04_afterlife.questphase / h9 / 2` (Condition) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 8:Out → 2:In; 2:True → 5:Active; 2:False → 6:Active |
| `mq015_04_afterlife.questphase / h9 / 5` (Journal) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix` | 5:Out → 1:In; 2:True → 5:Active |
| `mq015_04_afterlife.questphase / h9 / 6` (Journal) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix` | 6:Out → 1:In; 2:False → 6:Active |
| `mq015_04_afterlife.questphase / h128 / 2` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/04_examine_tablet` | 0:Out → 2:Active; 2:Out → 8:In |
| `mq015_04_afterlife.questphase / h128 / 3` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/04_examine_tablet` | 13:Out → 3:Succeeded; 3:Out → 11:In |
| `mq015_04_afterlife.questphase / h128 / 12` (Journal) | `quests/minor_quest/mq015_wizardbook` | 12:Out → 9:In; 11:True → 12:Succeeded |
| `mq015_01_hook.scene / scene / 8` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 8:0:0 → 10:0:0; 84:0:0 → 8:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_01_hook.scene / scene / 12` (Journal) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 12:0:0 → 162:0:1; 18:0:0 → 12:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_03_restaurant.scene / scene / 369` (Journal) | `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller` | 222:0:0 → 369:0:3; 369:0:0 → 2:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 35` (Condition) | `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix` | 35:0:0 → 67:0:3; 35:0:1 → 76:0:1; 287:0:0 → 35:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq015_04_stash.scene / scene / 64` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/05_talk_johnny` | 64:0:0 → 21:0:1; 64:0:0 → 259:0:1; 123:0:0 → 64:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 67` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/05_talk_johnny` | 35:0:0 → 67:0:3; 67:0:0 → 119:0:1; 67:0:0 → 163:0:1; 83:0:0 → 67:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 122` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/03_open_stash` | 1:0:0 → 122:0:1; 122:0:0 → 188:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 123` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/03_open_stash` | 123:0:0 → 64:0:1; 123:0:0 → 204:0:1; 181:0:0 → 123:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 149` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/04_take_wizardbook` | 149:0:0 → 192:0:0; 204:0:0 → 149:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_04_stash.scene / scene / 156` (Journal) | `quests/minor_quest/mq015_wizardbook/03_stash/04_take_wizardbook` | 156:0:0 → 326:0:0; 341:0:0 → 156:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_05_afterlife.scene / scene / 6` (scnChoiceNode) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix`; `quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix` | 6:0:0 → 4:0:0; 6:0:1 → 58:0:0; 266:0:0 → 6:0:0 |
| `mq015_05_afterlife.scene / scene / 137` (Journal) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix` | 137:0:0 → 2:0:0; 137:0:0 → 263:0:1; 146:0:1 → 137:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq015_05_afterlife.scene / scene / 146` (Condition) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix` | 146:0:0 → 152:0:3; 146:0:1 → 137:0:3; 208:0:0 → 146:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq015_05_afterlife.scene / scene / 152` (Journal) | `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix` | 146:0:0 → 152:0:3; 152:0:0 → 2:0:0; 152:0:0 → 263:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq015_01_hook.questphase / h0 / 8` | `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene`; `#mq015_01_sm_hook` | 12:CutSource → 8:CutDestination; 50:Out → 8:in; 8:out → 31:In |
| `mq015_01_hook.questphase / h152 / 2` | `base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene`; `#mq015_02_sm_seller_holocall` | 4:Out → 2:Start 0; 2:End 0 → 10:In; 2:Holocall INT → 15:In; 2:Holocall RET → 14:In |
| `mq015_02_restaurant.questphase / h0 / 7` | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene`; `#mq015_03_sm_restaurant` | 2:Out → 7:in; 7:out → 6:Succeeded; 16:CutSource → 7:CutDestination; 34:CutSource → 7:CutDestination; 28:CutSource → 7:CutDestination; 57:CutSource → 7:CutDestination; 7:out_failed → 19:Failed |
| `mq015_02_restaurant.questphase / h0 / 9` | `base\quest\minor_quests\mq015\phases\mq015_02_restaurant_combat.questphase` | 3:Out1 → 9:In1 |
| `mq015_02_restaurant.questphase / h0 / 29` | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene`; `#mq015_03_sm_restaurant` | 28:Out → 29:in_stealing_reaction |
| `mq015_02_restaurant.questphase / h0 / 35` | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene`; `#mq015_03_sm_restaurant` | 34:Out → 35:in_hit_reaction |
| `mq015_02_restaurant.questphase / h0 / 60` | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene`; `#mq015_03_sm_restaurant` | 57:Out → 60:in_grapple_reaction |
| `mq015_03_stash.questphase / h0 / 12` | `base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene`; `#mq015_04_sm_stash` | 4:Out → 12:in; 12:out → 16:In |
| `mq015_04_afterlife.questphase / h0 / 4` | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene`; `#mq015_05_sm_afterlife` | 42:Out → 4:in; 4:out → 8:Succeeded |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq015\mq015_wizardbook.questphase` / h0 / 5 | `mq015_01_hook.questphase` | 0: Input; 0:Out → 5:In1; 5:Out1 → 6:In1 |
| `base\quest\minor_quests\mq015\mq015_wizardbook.questphase` / h0 / 6 | `mq015_02_restaurant.questphase` | 2: Input; 5: Phase: mq015_01_hook.questphase; 2:Out → 6:In1; 5:Out1 → 6:In1; 6:Out1 → 7:In1 |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 9 | `mq015_02_restaurant_combat.questphase` | 3: Phase; 3:Out1 → 9:In1 |
| `base\quest\minor_quests\mq015\mq015_wizardbook.questphase` / h0 / 7 | `mq015_03_stash.questphase` | 3: Input; 6: Phase: mq015_02_restaurant.questphase; 3:Out → 7:In1; 6:Out1 → 7:In1; 7:Out1 → 8:In1 |
| `base\quest\minor_quests\mq015\mq015_wizardbook.questphase` / h0 / 8 | `mq015_04_afterlife.questphase` | 4: Input; 7: Phase: mq015_03_stash.questphase; 8:Out1 → 1:In; 4:Out → 8:In1; 7:Out1 → 8:In1 |
| `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` / h0 / 8 | `mq015_01_hook.scene` | 12: CutControl; 50: Journal; 12:CutSource → 8:CutDestination; 50:Out → 8:in; 8:out → 31:In |
| `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` / h152 / 2 | `mq015_02_seller_holocall.scene` | 4: PauseCondition; 4:Out → 2:Start 0; 2:End 0 → 10:In; 2:Holocall INT → 15:In; 2:Holocall RET → 14:In |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 7 | `mq015_03_restaurant.scene` | 2: Journal; 16: CutControl; 34: CutControl; 28: CutControl; 57: CutControl; 2:Out → 7:in; 7:out → 6:Succeeded; 16:CutSource → 7:CutDestination; 34:CutSource → 7:CutDestination; 28:CutSource → 7:CutDestination; 57:CutSource → 7:CutDestination; 7:out_failed → 19:Failed |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 29 | `mq015_03_restaurant.scene` | 28: CutControl; 28:Out → 29:in_stealing_reaction |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 35 | `mq015_03_restaurant.scene` | 34: CutControl; 34:Out → 35:in_hit_reaction |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 60 | `mq015_03_restaurant.scene` | 57: CutControl; 57:Out → 60:in_grapple_reaction |
| `base\quest\minor_quests\mq015\phases\mq015_03_stash.questphase` / h0 / 12 | `mq015_04_stash.scene` | 4: Journal; 4:Out → 12:in; 12:out → 16:In |
| `base\quest\minor_quests\mq015\phases\mq015_04_afterlife.questphase` / h0 / 4 | `mq015_05_afterlife.scene` | 42: Checkpoint; 42:Out → 4:in; 4:out → 8:Succeeded |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 36 | `mq015_wizardbook.questphase` | 134: FactsDBManager: mq015_active; 134:Out → 36:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq015_01_hook.scene` | in, Start 1 → out, out_clean | Nix; Player; 61 nodes / 71 edges |
| `mq015_02_seller_holocall.scene` | Start1, Start 0 → End 0 | Seller; Player; 17 nodes / 16 edges |
| `mq015_03_restaurant.scene` | in, in_stealing_reaction, in_hit_reaction, in_grapple_reaction → out, out_combat, out_failed | Seller; Player; 110 nodes / 142 edges |
| `mq015_04_stash.scene` | in → out, out_clean_up | Johnny; Player; 40 nodes / 46 edges |
| `mq015_05_afterlife.scene` | in → out, out_done | nix; Player; 78 nodes / 94 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq015_01_hook.scene / n10 / 0` | Indeed. (`whats`) | No option-level predicate stored | 0:0 → 101:0:1; 0:0 → 134:0:0 |
| `mq015_01_hook.scene / n10 / 1` | Not just yet. (`not_now`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq015_01_maybe_later", "comparisonType": "Equal"}}} | 0:1 → 29:0:0 |
| `mq015_01_hook.scene / n16 / 0` | Can do. Will do. (`agree`) | No option-level predicate stored | 0:0 → 18:0:0 |
| `mq015_01_hook.scene / n16 / 1` | Gonna give it a think. (`later`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq015_01_player_hesitates", "comparisonType": "Equal"}}} | 0:1 → 20:0:0 |
| `mq015_01_hook.scene / n16 / 2` | Can't you get it? (`wizardbook`) | No option-level predicate stored | 0:2 → 22:0:0 |
| `mq015_02_seller_holocall.scene / n7 / 0` | That's right. (`buy`) | No option-level predicate stored | 0:0 → 8:0:0 |
| `mq015_02_seller_holocall.scene / n7 / 1` | Call you later. (`later`) | No option-level predicate stored | 0:1 → 44:0:0 |
| `mq015_03_restaurant.scene / n6 / 0` | Here for the spell book. (`about_book`) | No option-level predicate stored | 0:0 → 4:0:0; 0:0 → 133:0:0; 0:0 → 339:0:1 |
| `mq015_03_restaurant.scene / n6 / 1` | Whatever. (`later`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq015_03_annoyed_seller", "comparisonType": "Equal"}}} | 0:1 → 39:0:0 |
| `mq015_03_restaurant.scene / n49 / 0` | [Pay] Fine. (`Agree`) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "141574774051"}}}} | 0:0 → 11:0:0 |
| `mq015_03_restaurant.scene / n49 / 1` | This your attempt at a con? (`Fuck with me`) | No option-level predicate stored | 0:1 → 52:0:0 |
| `mq015_03_restaurant.scene / n49 / 2` | Wow, service here at Hard Wire's shit these days… (`Corpo hit`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:2 → 12:0:0 |
| `mq015_03_restaurant.scene / n49 / 3` | No deal. Keep it. (`no_deal`) | No option-level predicate stored | 0:3 → 56:0:0 |
| `mq015_03_restaurant.scene / n54 / 0` | [Pay] So be it. Take you at your word. (`trust`) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "141574774051"}}}} | 0:0 → 11:0:0 |
| `mq015_03_restaurant.scene / n54 / 1` | Conversation's over. (`no_deal`) | No option-level predicate stored | 0:1 → 56:0:0 |
| `mq015_03_restaurant.scene / n54 / 2` | Wow, service here at Hard Wire's shit these days… (`Corpo hit`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:2 → 12:0:0 |
| `mq015_03_restaurant.scene / n62 / 0` | [Pay] Want you to not do anything stupid. (`will pay `) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "141574774051"}}}} | 0:0 → 64:0:0 |
| `mq015_03_restaurant.scene / n62 / 1` | [Negotiate] Discounts. Huge discounts. (`discount`) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "179229746243"}}}} | 0:1 → 67:0:0 |
| `mq015_04_stash.scene / n179 / 0` | [Open] (`open`) | No option-level predicate stored | 0:0 → 181:0:1 |
| `mq015_04_stash.scene / n192 / 0` | [Take] (`take`) | No option-level predicate stored | 0:0 → 195:0:1 |
| `mq015_05_afterlife.scene / n6 / 0` | Bought the book. (`started_nix`) | {"questCondition": {"$type": "questJournalCondition", "type": {"$type": "questJournalEntry_ConditionType", "path": {"$type": "gameJournalPath", "realPath": "quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix", "fileEntryIndex": 2, "className": "gameJournalQuestObjective"}, "state": "Active"}}} | 0:0 → 4:0:0 |
| `mq015_05_afterlife.scene / n6 / 1` | Got something interesting here... (`started_website`) | {"questCondition": {"$type": "questJournalCondition", "type": {"$type": "questJournalEntry_ConditionType", "path": {"$type": "gameJournalPath", "realPath": "quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix", "fileEntryIndex": 2, "className": "gameJournalQuestObjective"}, "state": "Active"}}} | 0:1 → 58:0:0 |
| `mq015_05_afterlife.scene / n11 / 0` | All yours. (`sell`) | No option-level predicate stored | 0:0 → 23:0:0 |
| `mq015_05_afterlife.scene / n11 / 1` | That's not nice. (`netrunnersavvy`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 33:0:0 |
| `mq015_05_afterlife.scene / n11 / 2` | Not sellin' at that price. Need more. (`not enough`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125088650329", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 36:0:0 |
| `mq015_05_afterlife.scene / n40 / 0` | Thanks. (`Noob`) | No option-level predicate stored | 0:0 → 42:0:0 |
| `mq015_05_afterlife.scene / n40 / 1` | Tablet's worth heaps more. You know it, I know it. (`Netrunner`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125088650329", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 45:0:0 |
| `mq015_05_afterlife.scene / n61 / 0` | Sounds right. (`Sell`) | No option-level predicate stored | 0:0 → 63:0:0 |
| `mq015_05_afterlife.scene / n61 / 1` | Fuck you. (`Dont sell`) | No option-level predicate stored | 0:1 → 66:0:0 |
| `mq015_05_afterlife.scene / n68 / 0` | Suits me just fine. (`Sell again`) | No option-level predicate stored | 0:0 → 63:0:0 |
| `mq015_05_afterlife.scene / n68 / 1` | Pay me triple and it's yours... (`Moremore`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125088650329", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 71:0:0 |
| `mq015_05_afterlife.scene / n68 / 2` | Gonna keep it. (`Nope`) | No option-level predicate stored | 0:2 → 78:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-49043` | mq015_quest_bugfixes.questphase / h88 / 3 | mq015_quest_bugfixes.questphase / h88 / 2 |
| `CYB-12345` | mq015_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-587177` | mq015_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `audio_v_calls_r3no_end_activate` | mq015_01_hook.questphase / h152 / 15; mq015_02_seller_holocall.scene / scene / 724 | No reader in selected context |
| `audio_v_calls_r3no_end_done` | mq015_02_seller_holocall.scene / scene / 714 | mq015_02_seller_holocall.scene / scene / 712 |
| `audio_v_calls_r3no_start_activate` | mq015_01_hook.questphase / h152 / 14; mq015_02_seller_holocall.scene / scene / 722 | No reader in selected context |
| `audio_v_calls_r3no_start_done` | mq015_02_seller_holocall.scene / scene / 710 | mq015_02_seller_holocall.scene / scene / 708 |
| `codex_nix` | mq015_01_hook.questphase / h0 / 62; mq015_quest_bugfixes.questphase / h88 / 5 | No reader in selected context |
| `mq015_01_maybe_later` | mq015_01_hook.scene / scene / 172; mq015_01_hook.scene / scene / 31 | mq015_01_hook.scene / scene / 10; mq015_01_hook.scene / scene / 33 |
| `mq015_01_player_hesitates` | mq015_01_hook.scene / scene / 49 | mq015_01_hook.scene / scene / 16 |
| `mq015_02_coordinates` | mq015_02_seller_holocall.scene / scene / 72 | mq015_01_hook.questphase / h152 / 10 |
| `mq015_03_annoyed_seller` | mq015_03_restaurant.scene / scene / 89 | mq015_03_restaurant.scene / scene / 43; mq015_03_restaurant.scene / scene / 6 |
| `mq015_03_combat_start` | mq015_03_restaurant.scene / scene / 29 | mq015_02_restaurant_combat.questphase / h0 / 13 |
| `mq015_05_rude_to_nix` | mq015_05_afterlife.scene / scene / 163 | mq015_04_afterlife.questphase / h0 / 29 |
| `mq015_active` | mq015_04_afterlife.questphase / h0 / 32 | mq015_quest_bugfixes.questphase / h88 / 4 |
| `mq015_coordinates_stash` | Producer outside selected context | mq015_02_restaurant.questphase / h0 / 32 |
| `mq015_dbg_restaurant` | Producer outside selected context | mq015_02_restaurant.questphase / h33 / 4 |
| `mq015_dbg_start` | Producer outside selected context | mq015_01_hook.questphase / h90 / 4; mq015_04_afterlife.questphase / h9 / 9 |
| `mq015_dbg_stash` | Producer outside selected context | mq015_03_stash.questphase / h12 / 2 |
| `mq015_decrypted_wizardbook` | Producer outside selected context | mq015_04_afterlife.questphase / h128 / 8 |
| `mq015_done` | mq015_04_afterlife.questphase / h0 / 7 | mq015_04_afterlife.questphase / h128 / 11; mq015_quest_bugfixes.questphase / h88 / 4 |
| `mq015_tablet_sold` | mq015_05_afterlife.scene / scene / 160 | No reader in selected context |
| `mq016_done` | Producer outside selected context | mq015_quest_bugfixes.questphase / h88 / 4 |
| `mq016_saved_life` | Producer outside selected context | mq015_05_afterlife.scene / scene / 168; mq015_quest_bugfixes.questphase / h88 / 4 |
| `nix_default_on` | mq015_01_hook.scene / scene / 101; mq015_01_hook.scene / scene / 104; mq015_01_hook.scene / scene / 108; mq015_05_afterlife.scene / scene / 179; mq015_05_afterlife.scene / scene / 368 | No reader in selected context |
| `nix_old_school_expert` | mq015_01_hook.scene / scene / 97; mq015_04_stash.scene / scene / 83 | mq015_04_stash.scene / scene / 76 |
| `sq015_sellar_keepalive` | mq015_03_restaurant.scene / scene / 1014; mq015_03_restaurant.scene / scene / 1016; mq015_03_restaurant.scene / scene / 1090; mq015_03_restaurant.scene / scene / 1092; mq015_03_restaurant.scene / scene / 1121; mq015_03_restaurant.scene / scene / 1130; mq015_03_restaurant.scene / scene / 1132; mq015_03_restaurant.scene / scene / 1139; mq015_03_restaurant.scene / scene / 1142 | mq015_03_restaurant.scene / scene / 1012; mq015_03_restaurant.scene / scene / 1018; mq015_03_restaurant.scene / scene / 1101 |
| `travelling_merchant_lives` | Producer outside selected context | mq015_quest_bugfixes.questphase / h0 / 16 |
| `web_smugglers_cache_treasures` | Producer outside selected context | mq015_01_hook.questphase / h0 / 7 |

## Exact gates, joins and cancellation

<details><summary>86 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq015_quest_bugfixes.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 17:Out → 16:In |
| `mq015_quest_bugfixes.questphase / h37 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:False → 1:In; 2:Out → 3:In; 3:True → 9:In |
| `mq015_quest_bugfixes.questphase / h37 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq015_com_seller"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":20.0},"comparisonType":"LessOrEqual"}}}` | 9:False → 1:In; 3:True → 9:In; 9:True → 5:In |
| `mq015_quest_bugfixes.questphase / h88 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-49043"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq015_quest_bugfixes.questphase / h88 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_done"}},{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_saved_life"}}]}]}}` | 3:Out → 4:In; 4:True → 5:In |
| `mq015_01_hook.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"web_smugglers_cache_treasures"}}}` | 31:CutSource → 7:CutDestination; 50:Out → 7:In; 7:Out → 12:In |
| `mq015_01_hook.questphase / h0 / 12` | `questCutControlNodeDefinition` `{}` | 7:Out → 12:In; 12:CutSource → 8:CutDestination; 12:Out → 44:In2 |
| `mq015_01_hook.questphase / h0 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 17:False → 9:Active; 53:Out → 17:In; 17:True → 18:Inactive |
| `mq015_01_hook.questphase / h0 / 31` | `questCutControlNodeDefinition` `{}` | 31:CutSource → 7:CutDestination; 8:out → 31:In; 31:Out → 44:In1 |
| `mq015_01_hook.questphase / h0 / 44` | `questLogicalXorNodeDefinition` `{}` | 12:Out → 44:In2; 31:Out → 44:In1; 44:Out1 → 53:Inactive |
| `mq015_01_hook.questphase / h90 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nix"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 7:In |
| `mq015_01_hook.questphase / h90 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_dbg_start"}}}` | 0:Out → 4:In; 4:False → 2:In; 4:True → 6:In |
| `mq015_01_hook.questphase / h152 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhone_ConditionType","caller":{"$type":"gameJournalPath","realPath":"contacts/player","fileEntryIndex":1,"className":"gameJournalContact"},"addressee":{"$type":"gameJournalPath","realPath":"contacts/seller","fileEntryIndex":1,"className":"gameJournalContact"}}}}` | 4:Out → 2:Start 0; 6:Out → 4:In; 9:Out → 4:In |
| `mq015_01_hook.questphase / h152 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 9:Out → 4:In; 10:False → 9:In |
| `mq015_01_hook.questphase / h152 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_02_coordinates"}}}` | 10:True → 1:In; 2:End 0 → 10:In; 10:False → 9:In |
| `mq015_02_restaurant.questphase / h0 / 10` | `questLogicalXorNodeDefinition` `{}` | 44:Out → 10:In1; 37:Out → 10:In2; 10:Out1 → 18:In; 10:Out1 → 38:In1 |
| `mq015_02_restaurant.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:Out → 13:In; 17:CutSource → 13:CutDestination; 13:Out → 46:In |
| `mq015_02_restaurant.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_restaurant"}}` | 4:Out → 14:In; 14:Out → 5:Succeeded |
| `mq015_02_restaurant.questphase / h0 / 16` | `questCutControlNodeDefinition` `{"permanent":true}` | 16:CutSource → 7:CutDestination; 46:Out → 16:In; 16:Out → 65:Succeeded; 16:CutSource → 25:CutDestination; 16:CutSource → 33:CutDestination |
| `mq015_02_restaurant.questphase / h0 / 17` | `questCutControlNodeDefinition` `{"permanent":true}` | 6:Out → 17:In; 17:CutSource → 13:CutDestination; 17:Out → 45:Active; 17:CutSource → 33:CutDestination; 17:CutSource → 25:CutDestination |
| `mq015_02_restaurant.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq015_dvc_seller_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"WasQuickHackAttempt"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq015_dvc_seller_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"HackingPerformed"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq015_dvc_seller_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq015_dvc_seller_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"WasQuickHacked"}},{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq015_dvc_seller_laptop","eventType":"Executed"}},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_dvc_seller_laptop"},"eventType":"Finished"}}]}}` | 16:CutSource → 25:CutDestination; 17:CutSource → 25:CutDestination; 54:Out → 25:In; 25:Out → 47:In |
| `mq015_02_restaurant.questphase / h0 / 28` | `questCutControlNodeDefinition` `{"permanent":true}` | 28:CutSource → 7:CutDestination; 47:Out → 28:In; 28:Out → 29:in_stealing_reaction |
| `mq015_02_restaurant.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_coordinates_stash"}}}` | 8:Out → 32:In; 32:Out → 12:Succeeded |
| `mq015_02_restaurant.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"includeHitTypes":["Bullet","Explosion","Melee","Other"]}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false,"unconscious":false,"defeated":false}}]},{"$type":"questCharacterCondition","type":{"$type":"questCharacterAim_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHacked_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["seller"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHackUploadBegin_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["seller"]}}}]}}` | 16:CutSource → 33:CutDestination; 17:CutSource → 33:CutDestination; 54:Out → 33:In; 33:Out → 34:In |
| `mq015_02_restaurant.questphase / h0 / 34` | `questCutControlNodeDefinition` `{"permanent":true}` | 34:CutSource → 7:CutDestination; 33:Out → 34:In; 34:Out → 35:in_hit_reaction |
| `mq015_02_restaurant.questphase / h0 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"statusEffectID":"BaseStatusEffect.Grappled"}}]}}` | 54:Out → 56:In; 56:Out → 57:In |
| `mq015_02_restaurant.questphase / h0 / 57` | `questCutControlNodeDefinition` `{"permanent":true}` | 57:CutSource → 7:CutDestination; 56:Out → 57:In; 57:Out → 60:in_grapple_reaction |
| `mq015_02_restaurant.questphase / h0 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#mq015_tr_restaurant"}}` | 2:Out → 64:In; 64:Out → 63:In |
| `mq015_02_restaurant.questphase / h33 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_dbg_restaurant"}}}` | 4:False → 1:In; 7:Out → 4:In; 4:True → 5:In |
| `mq015_02_restaurant.questphase / h310 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 2:Out → 3:In; 3:Out → 7:In |
| `mq015_02_restaurant.questphase / h310 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 0:Out → 6:In; 6:Out → 2:In |
| `mq015_02_restaurant.questphase / h351 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_restaurant"}}` | 4:Out → 6:In; 6:Out → 21:In |
| `mq015_02_restaurant.questphase / h351 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/seller/mq015/03_ch_got_it/03a_ch_got_it","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/seller/mq015/03_ch_got_it/03b_ch_no_games","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}]}}` | 18:False → 5:Inactive; 21:False → 18:In; 18:True → 19:In1 |
| `mq015_02_restaurant.questphase / h351 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}]}}` | 21:True → 1:In; 6:Out → 21:In; 21:False → 18:In |
| `mq015_02_restaurant_combat.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 8:Out → 9:In; 9:Out → 10:Succeeded |
| `mq015_02_restaurant_combat.questphase / h0 / 11` | `questLogicalXorNodeDefinition` `{}` | 11:Out1 → 3:In; 13:Out → 11:In1; 12:Out → 11:In2; 11:Out1 → 24:In; 11:Out1 → 26:In; 11:Out1 → 27:In |
| `mq015_02_restaurant_combat.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]}}}}` | 0:Out → 12:In; 12:Out → 11:In2 |
| `mq015_02_restaurant_combat.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_03_combat_start"}}}` | 0:Out → 13:In; 13:Out → 11:In1 |
| `mq015_02_restaurant_combat.questphase / h0 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 14:True → 7:Inactive; 29:Out → 14:In; 27:False → 14:In; 14:False → 19:In |
| `mq015_02_restaurant_combat.questphase / h0 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 7:Out → 19:In; 19:False → 8:Active; 14:False → 19:In; 19:True → 18:Inactive |
| `mq015_02_restaurant_combat.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq015_dvc_seller_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}}}` | 11:Out1 → 24:In; 24:False → 15:In; 24:False → 16:In |
| `mq015_02_restaurant_combat.questphase / h0 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 11:Out1 → 27:In; 27:False → 14:In; 27:True → 29:Inactive |
| `mq015_03_stash.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_stash"}}` | 3:Out → 5:In; 5:Out → 21:In |
| `mq015_03_stash.questphase / h12 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_dbg_stash"}}}` | 0:Out → 2:In; 2:False → 1:In; 2:True → 3:In |
| `mq015_04_afterlife.questphase / h0 / 29` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_05_rude_to_nix"}}}` | 33:Out → 29:In; 29:True → 31:Active; 29:False → 30:Active |
| `mq015_04_afterlife.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","minutes":30}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0}}}]}}` | 9:Out → 33:In; 33:Out → 29:In |
| `mq015_04_afterlife.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_afterlife_entrance"}}` | 3:Out1 → 36:In; 36:Out → 42:In |
| `mq015_04_afterlife.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#afterlife_interior_area_inside"}}` | 10:Out → 43:In; 43:Out → 34:In |
| `mq015_04_afterlife.questphase / h9 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 8:Out → 2:In; 2:True → 5:Active; 2:False → 6:Active |
| `mq015_04_afterlife.questphase / h9 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_dbg_start"}}}` | 0:Out → 9:In; 9:False → 3:In; 9:True → 10:In |
| `mq015_04_afterlife.questphase / h128 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_decrypted_wizardbook"}}}` | 2:Out → 8:In; 8:Out → 13:In |
| `mq015_04_afterlife.questphase / h128 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_done"}}}` | 3:Out → 11:In; 11:False → 9:In; 11:True → 12:Succeeded |
| `mq015_01_hook.scene / scene / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_01_maybe_later","value":1}}}` | 33:0:0 → 36:0:0; 33:0:1 → 6:0:0; 160:0:0 → 33:0:1 |
| `mq015_01_hook.scene / scene / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questBuild_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"Build_ScriptConditionType","buildId":"95189197130","difficulty":"EASY","comparisonType":"CO_Greater"}}}}` | 39:0:0 → 41:0:0; 39:0:1 → 43:0:0; 97:0:0 → 39:0:1 |
| `mq015_01_hook.scene / scene / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":7.0},"comparisonType":"GreaterOrEqual"}}}` | 78:0:0 → 67:666:1; 84:0:0 → 78:0:1; 134:1:0 → 78:0:0; 134:1:0 → 78:1026:0; 135:0:0 → 78:0:1 |
| `mq015_01_hook.scene / scene / 219` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":7.0}}}}` | 18:0:0 → 219:0:1; 219:0:0 → 108:0:1 |
| `mq015_01_hook.scene / scene / 252` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_netrunners_den"}}` | 67:666:0 → 252:0:1; 252:0:0 → 254:0:1; 259:0:0 → 252:0:1 |
| `mq015_01_hook.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq015_tr_netrunners_den"}}` | 254:0:0 → 256:0:1; 256:0:0 → 259:0:1 |
| `mq015_01_hook.scene / scene / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]},"angleTolerance":60.0}}]}}` | 67:666:0 → 269:0:1; 134:1:0 → 269:0:0; 134:1:0 → 269:1026:0; 269:0:0 → 160:0:1 |
| `mq015_02_seller_holocall.scene / scene / 708` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"audio_v_calls_r3no_start_done"}}}` | 708:0:0 → 710:0:1; 722:0:0 → 708:0:1 |
| `mq015_02_seller_holocall.scene / scene / 712` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"audio_v_calls_r3no_end_done"}}}` | 712:0:0 → 714:0:1; 724:0:0 → 712:0:1 |
| `mq015_03_restaurant.scene / scene / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq015_03_annoyed_seller","value":2}}}` | 43:0:0 → 921:0:0; 43:0:1 → 37:0:0; 1014:0:0 → 43:0:1 |
| `mq015_03_restaurant.scene / scene / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]},"timeInterval":3.0,"angleTolerance":60.0}}]}}` | 72:0:0 → 210:0:1; 133:1:0 → 72:0:0; 133:1:0 → 72:1026:0; 1016:0:0 → 72:0:1 |
| `mq015_03_restaurant.scene / scene / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 78:0:0 → 89:0:1; 133:1:0 → 78:0:0; 133:1:0 → 78:1026:0; 173:0:0 → 78:0:1 |
| `mq015_03_restaurant.scene / scene / 339` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 6:0:0 → 339:0:1; 339:0:0 → 341:0:0 |
| `mq015_03_restaurant.scene / scene / 382` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","statusEffectID":"BaseStatusEffect.Grappled"}}]}}` | 120:0:0 → 382:0:1; 382:0:0 → 384:0:0 |
| `mq015_03_restaurant.scene / scene / 968` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq015_com_seller","names":["Seller"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"Less"}}}` | 968:0:0 → 1067:0:0; 1012:0:0 → 968:0:1 |
| `mq015_03_restaurant.scene / scene / 998` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 996:0:0 → 998:0:1; 998:0:0 → 1004:0:0 |
| `mq015_03_restaurant.scene / scene / 1000` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 996:0:1 → 1000:0:1; 1000:0:0 → 1004:0:0 |
| `mq015_03_restaurant.scene / scene / 1002` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 996:0:2 → 1002:0:1; 1002:0:0 → 1004:0:0 |
| `mq015_03_restaurant.scene / scene / 1012` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq015_sellar_keepalive","value":1,"comparisonType":"Equal"}}}` | 1010:0:0 → 1012:0:1; 1012:0:0 → 968:0:1; 1012:0:1 → 1018:0:1; 1020:0:1 → 1012:0:1 |
| `mq015_03_restaurant.scene / scene / 1018` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq015_sellar_keepalive","value":1,"comparisonType":"Equal"}}}` | 1012:0:1 → 1018:0:1; 1018:0:0 → 1103:0:0; 1099:0:0 → 1018:0:1 |
| `mq015_03_restaurant.scene / scene / 1101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq015_sellar_keepalive","comparisonType":"Equal"}}}` | 1101:0:0 → 1099:0:0; 1103:0:1 → 1101:0:1 |
| `mq015_03_restaurant.scene / scene / 1105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":255}}}` | 1099:1:0 → 1105:0:0; 1103:0:0 → 1105:0:1; 1105:0:0 → 1067:0:1 |
| `mq015_04_stash.scene / scene / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questBuild_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"Build_ScriptConditionType","buildId":"95189197130","difficulty":"MEDIUM","comparisonType":"CO_Greater"}}}}` | 21:0:0 → 20:0:0; 21:0:1 → 14:0:0; 64:0:0 → 21:0:1 |
| `mq015_04_stash.scene / scene / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 35:0:0 → 67:0:3; 35:0:1 → 76:0:1; 287:0:0 → 35:0:1 |
| `mq015_04_stash.scene / scene / 76` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nix_old_school_expert","value":1,"comparisonType":"GreaterOrEqual"}}}` | 35:0:1 → 76:0:1; 76:0:0 → 86:0:0; 76:0:1 → 26:0:0 |
| `mq015_04_stash.scene / scene / 119` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq015_04_stash_Johnny"},"timeInterval":0.0,"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 67:0:0 → 119:0:1; 119:0:0 → 213:0:1 |
| `mq015_04_stash.scene / scene / 204` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 123:0:0 → 204:0:1; 204:0:0 → 149:0:1 |
| `mq015_04_stash.scene / scene / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 64:0:0 → 259:0:1; 259:0:0 → 269:0:0 |
| `mq015_05_afterlife.scene / scene / 146` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 146:0:0 → 152:0:3; 146:0:1 → 137:0:3; 208:0:0 → 146:0:1 |
| `mq015_05_afterlife.scene / scene / 168` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq016_saved_life","value":1,"comparisonType":"GreaterOrEqual"}}}` | 66:0:0 → 168:0:1; 78:0:0 → 168:0:1; 168:0:0 → 172:0:0; 168:0:1 → 128:0:0 |
| `mq015_05_afterlife.scene / scene / 322` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#nix","names":["nix"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0}}}}` | 208:0:0 → 322:0:1; 322:0:0 → 183:0:0 |
| `mq015_05_afterlife.scene / scene / 337` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_afterlife_nix"}}` | 335:0:0 → 337:0:1; 337:0:0 → 188:0:0 |
| `mq015_05_afterlife.scene / scene / 372` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq015_tr_netrunners_den"}}` | 335:0:0 → 372:0:1; 372:0:0 → 374:0:1; 378:0:0 → 372:0:1 |
| `mq015_05_afterlife.scene / scene / 376` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq015_tr_netrunners_den"}}` | 374:0:0 → 376:0:1; 376:0:0 → 378:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq015_01_hook.questphase / h90 / 3; mq015_02_restaurant.questphase / h310 / 3 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | mq015_01_hook.questphase / h152 / 6; mq015_04_afterlife.questphase / h0 / 37 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | mq015_01_hook.scene / scene / 10; mq015_01_hook.scene / scene / 16; mq015_02_seller_holocall.scene / scene / 7; mq015_03_restaurant.scene / scene / 49; +10 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mq015_02_restaurant.questphase / h310 / 2; mq015_02_restaurant.questphase / h33 / 2; mq015_02_restaurant_combat.questphase / h0 / 3 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq015_01_hook.questphase / h0 / 7; mq015_01_hook.questphase / h152 / 10; mq015_01_hook.questphase / h90 / 4; mq015_01_hook.scene / scene / 10; +22 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq015_01_hook.scene / scene / 254; mq015_01_hook.scene / scene / 259; mq015_01_hook.scene / scene / 263; mq015_04_afterlife.questphase / h0 / 28; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_action` | mq015_01_hook.questphase / h90 / 6; mq015_01_hook.questphase / h90 / 7; mq015_02_restaurant_combat.questphase / h0 / 15; mq015_02_restaurant_combat.questphase / h0 / 16; +3 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq015_02_restaurant.questphase / h0 / 25; mq015_02_restaurant_combat.questphase / h0 / 24 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | mq015_04_afterlife.questphase / h0 / 33 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `persistent_decision` | mq015_01_hook.questphase / h0 / 62; mq015_01_hook.questphase / h152 / 14; mq015_01_hook.questphase / h152 / 15; mq015_01_hook.scene / scene / 101; +33 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq015_01_hook.questphase / h0 / 44; mq015_02_restaurant.questphase / h0 / 10; mq015_02_restaurant_combat.questphase / h0 / 11 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq015_01_hook.questphase / h152 / 9; mq015_03_restaurant.scene / scene / 1000; mq015_03_restaurant.scene / scene / 1002; mq015_03_restaurant.scene / scene / 1105; +5 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq015_01_hook.questphase / h0 / 12; mq015_01_hook.questphase / h0 / 31; mq015_02_restaurant.questphase / h0 / 16; mq015_02_restaurant.questphase / h0 / 17; +3 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq015_02_restaurant.questphase / h0 / 37; mq015_02_restaurant_combat.questphase / h0 / 21; mq015_03_stash.questphase / h0 / 16; mq015_04_afterlife.questphase / h0 / 10; +3 locations in catalogue.json | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | mq015_02_restaurant.questphase / h0 / 25 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq015_01_hook.questphase / h0 / 8; mq015_01_hook.questphase / h152 / 2; mq015_02_restaurant.questphase / h0 / 29; mq015_02_restaurant.questphase / h0 / 35; +4 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq015_02_restaurant.questphase / h0 / 13; mq015_02_restaurant.questphase / h0 / 33; mq015_02_restaurant.questphase / h351 / 21; mq015_02_restaurant_combat.questphase / h0 / 9 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq015_01_hook.scene / scene / 164; mq015_01_hook.scene / scene / 165; mq015_01_hook.scene / scene / 230; mq015_01_hook.scene / scene / 231; +58 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq015_02_restaurant.questphase / h33 / 7; mq015_04_stash.scene / scene / 341 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq015\mq015_quest_bugfixes.questphase` | repair; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant_combat.questphase` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\phases\mq015_03_stash.questphase` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\phases\mq015_04_afterlife.questphase` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene` | content candidate; forward dependency | `base-mq015` |
| `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene` | content candidate; journal anchor | `base-mq015` |
| `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` | content candidate; journal anchor | `base-mq015` |

Evidence shards for this dossier (including parent context): [base-mq015](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq015.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
