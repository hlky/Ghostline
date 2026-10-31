# Gig: The Frolics of Councilwoman Cole

Journal: `quests/street_stories/city_center/downtown/sts_cct_dtn_05` · `StreetStory` · hash `4125561827`.

Journal premise: Gig type: Thievery\nObjective: Steal recordings of Eva Cole\nLocation: Marina, Cannery Row\nDetails:\n\nSo there's this Councilwoman, Eva Cole. By day, she's a living nightmare for greedy corpos, pointin' the finger on abuse, digging up problematic witnesses, dishin' out fees and penalties and whatever. And by night – she fucks. Like a fuckin' cat in heat, with whoever lands on the deck of her yacht docked down at the marina. I'd act more surprised, but I ain't – I mean you gotta let out all that stress somehow, right? So anyway, one of these corpos that got its toes stomped on wants footage of these wet-n-wild orgy fuckfests. They got in mind a joint screening with the councilwoman will help her see the light of a more... pro-business attitude.\n\nI send you the yacht name and coords, you fetch the footage. Oh... and I wouldn't sit on any of the furniture if I was you.\n\nOne last thing – there's more €$ to be made if you do this on the quiet.

**Coverage: journal-linked.** 42 exact journal-linked nodes in 5 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 7 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Escape the docks. (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` |
| Remain undetected. (Optional) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` |
| Collect your bonus from the Drop Point. (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward` |
| Get inside the docks' security room. (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room` |
| Go to the docks. (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` |
| Recording (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/main` |
| Download the incriminating recordings and send them to the fixer. (Primary) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_downtown_bugfixing.questphase / h40 / 4` (PauseCondition) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/des` | 11:Out1 → 4:In; 4:Out → 16:In; 4:Out → 17:In; 4:Out → 18:In; 4:Out → 19:In |
| `sts_downtown_bugfixing.questphase / h40 / 19` (PauseCondition) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` | 4:Out → 19:In; 19:Out → 12:In |
| `sts_cct_downtown.questphase / h4373 / 58` (PauseCondition) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 0:Out → 58:In; 58:Out → 59:In |
| `sts_cct_downtown.questphase / h6769 / 38` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 42:Out → 38:Succeeded; 38:Out → 39:In |
| `sts_cct_downtown.questphase / h6769 / 51` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward` | 44:Out → 51:Succeeded; 51:Out → 52:Succeeded |
| `sts_cct_downtown.questphase / h6769 / 52` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 52:Out → 41:In; 51:Out → 52:Succeeded |
| `sts_cct_downtown.questphase / h6769 / 53` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 40:True → 53:Succeeded; 53:Out → 43:In |
| `sts_cct_downtown.questphase / h7140 / 58` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 62:Out → 58:Succeeded; 58:Out → 194:Active |
| `sts_cct_downtown.questphase / h7140 / 59` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 109:True → 59:Active; 59:Out → 110:In1 |
| `sts_cct_downtown.questphase / h7140 / 108` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 109:False → 108:Active; 108:Out → 110:In2 |
| `sts_cct_downtown.questphase / h7140 / 111` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/des` | 3:Out → 111:Active |
| `sts_cct_downtown.questphase / h7140 / 128` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 190:Out → 128:Active; 128:Out → 129:In |
| `sts_cct_downtown.questphase / h7140 / 130` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 129:Out → 130:Succeeded; 130:Out → 147:In; 130:Out → 179:In1 |
| `sts_cct_downtown.questphase / h7140 / 143` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 143:Out → 62:In; 210:Out → 143:Active; 143:Out → 145:In |
| `sts_cct_downtown.questphase / h7140 / 144` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 145:Out → 144:Failed |
| `sts_cct_downtown.questphase / h7140 / 146` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 147:Out → 146:Succeeded; 146:Out → 177:Active |
| `sts_cct_downtown.questphase / h7140 / 177` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward` | 146:Out → 177:Active; 177:Out → 179:In2 |
| `sts_cct_downtown.questphase / h7140 / 192` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` | 195:Out → 192:Active |
| `sts_cct_downtown.questphase / h7140 / 193` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` | 173:Out → 193:Succeeded |
| `sts_cct_downtown.questphase / h7140 / 194` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room` | 58:Out → 194:Active; 194:Out → 156:In |
| `sts_cct_downtown.questphase / h7140 / 195` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room` | 195:Out → 192:Active; 196:Out → 195:Succeeded |
| `sts_cct_dtn_05_combat.questphase / h256 / 58` (PauseCondition) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 0:Out → 58:In; 58:Out → 59:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 38` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 42:Out → 38:Succeeded; 38:Out → 39:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 51` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward` | 44:Out → 51:Succeeded; 51:Out → 52:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h243 / 52` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 52:Out → 41:In; 51:Out → 52:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h243 / 53` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 40:True → 53:Succeeded; 53:Out → 43:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 58` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 62:Out → 58:Succeeded; 58:Out → 194:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 59` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 109:True → 59:Active; 59:Out → 110:In1 |
| `sts_cct_dtn_05_openworld.questphase / h614 / 108` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks` | 109:False → 108:Active; 108:Out → 110:In2 |
| `sts_cct_dtn_05_openworld.questphase / h614 / 111` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/des` | 3:Out → 111:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 128` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 190:Out → 128:Active; 128:Out → 129:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 130` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks` | 129:Out → 130:Succeeded; 130:Out → 147:In; 130:Out → 179:In1 |
| `sts_cct_dtn_05_openworld.questphase / h614 / 143` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 143:Out → 62:In; 210:Out → 143:Active; 143:Out → 145:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 144` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 145:Out → 144:Failed |
| `sts_cct_dtn_05_openworld.questphase / h614 / 146` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth` | 147:Out → 146:Succeeded; 146:Out → 177:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 177` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward` | 146:Out → 177:Active; 177:Out → 179:In2 |
| `sts_cct_dtn_05_openworld.questphase / h614 / 192` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` | 195:Out → 192:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 193` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc` | 173:Out → 193:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h614 / 194` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room` | 58:Out → 194:Active; 194:Out → 156:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 195` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room` | 195:Out → 192:Active; 196:Out → 195:Succeeded |
| `open_world_bugfixing.questphase / h1425 / 14` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h2561 / 14` (Journal) | `quests/street_stories/city_center/downtown/sts_cct_dtn_05` | 13:True → 14:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_cct_dtn_05_combat.questphase / h176 / 2` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene`; `#sts_sm_cct_dtn_05_guards` | 39:Out → 2:dtn_05_chat_001_start; 2:dtn_05_chat_001_end → 31:In |
| `sts_cct_dtn_05_combat.questphase / h176 / 27` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene`; `#sts_sm_cct_dtn_05_guards` | 38:Out → 27:dtn_05_chat_002_start; 27:dtn_05_chat_002_end → 33:In |
| `sts_cct_dtn_05_openworld.questphase / h218 / 41` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene`; `#sts_sm_cct_dtn_05_johnny` | 41:End 0 → 32:In; 44:Out → 41:Start 0 |
| `sts_cct_dtn_05_openworld.questphase / h243 / 47` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene`; `#sts_sm_cct_dtn_05_holocall_debriefs` | 47:rejected_out → 45:In; 47:End 0 → 45:In; 73:False → 47:Start 0; 47:Holocall INT → 56:In; 47:Holocall RET → 55:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 50` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene`; `#sts_sm_cct_dtn_05_holocall_debriefs` | 71:False → 50:Start 0; 50:End 0 → 54:In; 50:rejected_out → 72:Active; 50:Holocall INT → 58:In; 50:Holocall RET → 57:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 201` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene`; `#sts_sm_cct_dtn_05_holocall_prebrief` | 201:rejected_out → 153:Active; 201:End 0 → 153:Active; 216:False → 201:Start 0; 201:Holocall INT → 212:In; 201:Holocall RET → 211:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 45 | `sts_downtown_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 45:In1 |
| `base\open_world\street_stories\city_center\sts_city_center.questphase` / h0 / 3 | `sts_cct_downtown.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h6457 / 11 | `sts_cct_dtn_05_combat.questphase` | 14: Checkpoint; 14:Out → 11:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.questphase` / h0 / 11 | `sts_cct_dtn_05_combat.questphase` | 14: Checkpoint; 14:Out → 11:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h6457 / 12 | `sts_cct_dtn_05_openworld.questphase` | 14: Checkpoint; 12:Out1 → 1:In; 14:Out → 12:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.questphase` / h0 / 12 | `sts_cct_dtn_05_openworld.questphase` | 14: Checkpoint; 12:Out1 → 1:In; 14:Out → 12:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h4293 / 2 | `sts_cct_dtn_05_guards.scene` | 39: PauseCondition: IsControlledByThePlayer; 39:Out → 2:dtn_05_chat_001_start; 2:dtn_05_chat_001_end → 31:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h4293 / 27 | `sts_cct_dtn_05_guards.scene` | 38: PauseCondition: IsControlledByThePlayer; IsControlledByThePlayer; IsControlledByThePlayer; 38:Out → 27:dtn_05_chat_002_start; 27:dtn_05_chat_002_end → 33:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h176 / 2 | `sts_cct_dtn_05_guards.scene` | 39: PauseCondition: IsControlledByThePlayer; 39:Out → 2:dtn_05_chat_001_start; 2:dtn_05_chat_001_end → 31:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h176 / 27 | `sts_cct_dtn_05_guards.scene` | 38: PauseCondition: IsControlledByThePlayer; IsControlledByThePlayer; IsControlledByThePlayer; 38:Out → 27:dtn_05_chat_002_start; 27:dtn_05_chat_002_end → 33:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h6769 / 47 | `sts_cct_dtn_05_holocall_debriefs.scene` | 73: Condition; 47:rejected_out → 45:In; 47:End 0 → 45:In; 73:False → 47:Start 0; 47:Holocall INT → 56:In; 47:Holocall RET → 55:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h6769 / 50 | `sts_cct_dtn_05_holocall_debriefs.scene` | 71: Condition; 71:False → 50:Start 0; 50:End 0 → 54:In; 50:rejected_out → 72:Active; 50:Holocall INT → 58:In; 50:Holocall RET → 57:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h243 / 47 | `sts_cct_dtn_05_holocall_debriefs.scene` | 73: Condition; 47:rejected_out → 45:In; 47:End 0 → 45:In; 73:False → 47:Start 0; 47:Holocall INT → 56:In; 47:Holocall RET → 55:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h243 / 50 | `sts_cct_dtn_05_holocall_debriefs.scene` | 71: Condition; 71:False → 50:Start 0; 50:End 0 → 54:In; 50:rejected_out → 72:Active; 50:Holocall INT → 58:In; 50:Holocall RET → 57:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h7140 / 201 | `sts_cct_dtn_05_holocall_prebrief.scene` | 216: Condition; 201:rejected_out → 153:Active; 201:End 0 → 153:Active; 216:False → 201:Start 0; 201:Holocall INT → 212:In; 201:Holocall RET → 211:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h614 / 201 | `sts_cct_dtn_05_holocall_prebrief.scene` | 216: Condition; 201:rejected_out → 153:Active; 201:End 0 → 153:Active; 216:False → 201:Start 0; 201:Holocall INT → 212:In; 201:Holocall RET → 211:In |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h6744 / 41 | `sts_cct_dtn_05_johnny.scene` | 44: PauseCondition: #dtn_05_tr_johnny_talk; 41:End 0 → 32:In; 44:Out → 41:Start 0 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h218 / 41 | `sts_cct_dtn_05_johnny.scene` | 44: PauseCondition: #dtn_05_tr_johnny_talk; 41:End 0 → 32:In; 44:Out → 41:Start 0 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 3 | `sts_city_center.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h0 / 9 | `sts_cct_dtn_05.questphase` | 40: Journal; 44: Journal; 40:Out → 9:In1; 44:Out → 9:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.quest` / h0 / 2 | `sts_cct_dtn_05.questphase` | 3: FactsDBManager: dtn_05_journal_test; 2:Out1 → 1:In; 3:Out → 2:In1 |
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
| `sts_cct_dtn_05_guards.scene` | dtn_05_chat_001_start, dtn_05_chat_002_start → dtn_05_chat_001_end, dtn_05_chat_002_end | guard_003; guard_005; guard_006; 6 nodes / 4 edges |
| `sts_cct_dtn_05_holocall_debriefs.scene` | Start 0 → End 0, rejected_out | fixer; player; 25 nodes / 33 edges |
| `sts_cct_dtn_05_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; 22 nodes / 25 edges |
| `sts_cct_dtn_05_johnny.scene` | Start 0 → End 0 | Johnny; Player; 6 nodes / 5 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `cct_achievement` | sts_cct_dtn_05_openworld.questphase / h243 / 19 | sts_cct_dtn_05_openworld.questphase / h243 / 59 |
| `dtn_005_chat_001_end` | sts_cct_dtn_05_combat.questphase / h176 / 31 | sts_cct_dtn_05_combat.questphase / h49 / 34 |
| `dtn_005_chat_002_end` | sts_cct_dtn_05_combat.questphase / h176 / 33 | sts_cct_dtn_05_combat.questphase / h49 / 25 |
| `dtn_05_active` | sts_cct_dtn_05_openworld.questphase / h12 / 87; sts_cct_dtn_05_openworld.questphase / h243 / 36 | No reader in selected context |
| `dtn_05_cleanup` | sts_cct_dtn_05_openworld.questphase / h243 / 35 | No reader in selected context |
| `dtn_05_combat` | sts_cct_dtn_05_combat.questphase / h33 / 28 | sts_cct_downtown.questphase / h6769 / 40; sts_cct_downtown.questphase / h7140 / 145; sts_cct_downtown.questphase / h7140 / 147; sts_cct_dtn_05_holocall_debriefs.scene / scene / 51; sts_cct_dtn_05_openworld.questphase / h243 / 40; sts_cct_dtn_05_openworld.questphase / h614 / 145; sts_cct_dtn_05_openworld.questphase / h614 / 147 |
| `dtn_05_finished` | sts_cct_downtown.questphase / h6769 / 39; sts_cct_dtn_05_openworld.questphase / h243 / 39 | open_world_bugfixing.questphase / h1425 / 13; open_world_bugfixing.questphase / h2561 / 13 |
| `dtn_05_journal_test` | Producer outside selected context | sts_cct_downtown.questphase / h7140 / 109; sts_cct_dtn_05_openworld.questphase / h614 / 109 |
| `dtn_05_reinforcements_active` | sts_cct_dtn_05_combat.questphase / h256 / 65 | sts_cct_dtn_05_combat.questphase / h0 / 8 |
| `dtn_05_start` | sts_cct_dtn_05_openworld.questphase / h12 / 88 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_cct_dtn_05_holocall_prebrief.scene / scene / 280 |
| `holo_dino_calls_v_end_activate` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 77; sts_cct_dtn_05_holocall_prebrief.scene / scene / 71; sts_cct_dtn_05_openworld.questphase / h243 / 56; sts_cct_dtn_05_openworld.questphase / h243 / 58; sts_cct_dtn_05_openworld.questphase / h614 / 212 | No reader in selected context |
| `holo_dino_calls_v_end_done` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 73; sts_cct_dtn_05_holocall_prebrief.scene / scene / 67 | sts_cct_dtn_05_holocall_debriefs.scene / scene / 72; sts_cct_dtn_05_holocall_prebrief.scene / scene / 66 |
| `holo_dino_calls_v_rejectable` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 282; sts_cct_dtn_05_holocall_prebrief.scene / scene / 254; sts_cct_dtn_05_holocall_prebrief.scene / scene / 286 | No reader in selected context |
| `holo_dino_calls_v_rejected` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 284; sts_cct_dtn_05_holocall_prebrief.scene / scene / 256 | sts_cct_dtn_05_holocall_debriefs.scene / scene / 286; sts_cct_dtn_05_holocall_prebrief.scene / scene / 258 |
| `holo_dino_calls_v_start_activate` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 266; sts_cct_dtn_05_holocall_debriefs.scene / scene / 76; sts_cct_dtn_05_holocall_prebrief.scene / scene / 284; sts_cct_dtn_05_holocall_prebrief.scene / scene / 70; sts_cct_dtn_05_openworld.questphase / h243 / 55; sts_cct_dtn_05_openworld.questphase / h243 / 57; sts_cct_dtn_05_openworld.questphase / h614 / 211 | sts_cct_dtn_05_holocall_debriefs.scene / scene / 256 |
| `holo_dino_calls_v_start_done` | sts_cct_dtn_05_holocall_debriefs.scene / scene / 71; sts_cct_dtn_05_holocall_prebrief.scene / scene / 65 | sts_cct_dtn_05_holocall_debriefs.scene / scene / 249; sts_cct_dtn_05_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_cct_dtn_05_holocall_debriefs.scene / scene / 256; sts_cct_dtn_05_holocall_prebrief.scene / scene / 280 |
| `holo_setup_started` | Producer outside selected context | sts_cct_dtn_05_holocall_debriefs.scene / scene / 256; sts_cct_dtn_05_holocall_prebrief.scene / scene / 280 |

## Exact gates, joins and cancellation

<details><summary>87 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_downtown_bugfixing.questphase / h40 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/city_center/downtown/sts_cct_dtn_05/des","fileEntryIndex":4,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 11:Out1 → 4:In; 4:Out → 16:In; 4:Out → 17:In; 4:Out → 18:In; 4:Out → 19:In |
| `sts_downtown_bugfixing.questphase / h40 / 11` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 3:Out → 11:In4; 11:Out1 → 4:In; 5:Out → 11:In1; 6:Out → 11:In2; 7:Out → 11:In3 |
| `sts_downtown_bugfixing.questphase / h40 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded","inverted":true}}}` | 4:Out → 19:In; 19:Out → 12:In |
| `sts_cct_downtown.questphase / h4373 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 58:In; 58:Out → 59:In |
| `sts_cct_downtown.questphase / h4373 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_combat"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5}}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_reinforcements"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"inverted":true}}]}}` | 58:Out → 59:In; 59:Out → 65:In; 59:Out → 66:In1 |
| `sts_cct_downtown.questphase / h6769 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat","comparisonType":"Equal"}}}` | 67:Out → 40:In; 40:True → 53:Succeeded; 40:False → 71:In |
| `sts_cct_downtown.questphase / h6769 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_city_center/downtown/downtown_drop_points_prefabQOBVMZA/drop_point_004_prefabYVOQU5I","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 48:Out → 44:In; 44:Out → 51:Succeeded |
| `sts_cct_downtown.questphase / h7140 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_docks"}}` | 62:Out → 58:Succeeded; 143:Out → 62:In; 62:Out → 196:In |
| `sts_cct_downtown.questphase / h7140 / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_journal_test"}}}` | 3:Out → 109:In; 109:True → 59:Active; 109:False → 108:Active |
| `sts_cct_downtown.questphase / h7140 / 110` | `questLogicalXorNodeDefinition` `{}` | 59:Out → 110:In1; 108:Out → 110:In2; 110:Out1 → 210:In |
| `sts_cct_downtown.questphase / h7140 / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#dtn_05_tr_docks"}}` | 128:Out → 129:In; 129:Out → 130:Succeeded |
| `sts_cct_downtown.questphase / h7140 / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat"}}}` | 143:Out → 145:In; 145:Out → 144:Failed |
| `sts_cct_downtown.questphase / h7140 / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat","comparisonType":"Equal"}}}` | 130:Out → 147:In; 147:Out → 146:Succeeded |
| `sts_cct_downtown.questphase / h7140 / 156` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_computer_003","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 194:Out → 156:In; 156:Out → 161:In |
| `sts_cct_downtown.questphase / h7140 / 179` | `questLogicalXorNodeDefinition` `{}` | 130:Out → 179:In1; 177:Out → 179:In2; 179:Out1 → 199:In |
| `sts_cct_downtown.questphase / h7140 / 196` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_docks_control_room"}}` | 62:Out → 196:In; 196:Out → 195:Succeeded |
| `sts_cct_dtn_05_combat.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_combat"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 6:In; 6:Out → 14:In |
| `sts_cct_dtn_05_combat.questphase / h0 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_reinforcements_active","value":1,"comparisonType":"Equal"}}}` | 14:Out → 8:In; 8:True → 9:In; 8:False → 11:In |
| `sts_cct_dtn_05_combat.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 8:True → 9:In; 9:Out → 12:In |
| `sts_cct_dtn_05_combat.questphase / h0 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 8:False → 11:In; 11:Out → 19:In |
| `sts_cct_dtn_05_combat.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 9:Out → 12:In; 12:Out → 19:In |
| `sts_cct_dtn_05_combat.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_ceiling_turret_001","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsOFF"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_ceiling_turret_001","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsDisabled"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_ceiling_turret_001","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsUnpowered"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_ceiling_turret_001","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_ceiling_turret_001","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsAuthorizationModuleOn"}}]}}` | 6:Out → 14:In; 14:Out → 8:In |
| `sts_cct_dtn_05_combat.questphase / h33 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 25:In; 25:Out → 28:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_005_chat_002_end"}}}` | 0:Out → 25:In; 25:Out → 45:In; 25:Out → 48:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"$/03_night_city/#c_city_center/downtown/loc_sts_cct_dtn_05_luxury_yacht_prefabNYWJWMA/#sts_cct_dtn_05_luxury_yacht_openworld/#sts_cct_dtn_05_streetstory/dtn_05_tr_guard_002_patrol"}}` | 0:Out → 30:In; 30:Out → 29:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"$/03_night_city/#c_city_center/downtown/loc_sts_cct_dtn_05_luxury_yacht_prefabNYWJWMA/#sts_cct_dtn_05_luxury_yacht_openworld/#sts_cct_dtn_05_streetstory/dtn_05_tr_guard_004_patrol"}}` | 0:Out → 32:In; 32:Out → 22:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_005_chat_001_end"}}}` | 0:Out → 34:In; 34:Out → 21:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_guard_008_patrol"}}` | 0:Out → 37:In; 37:Out → 43:In |
| `sts_cct_dtn_05_combat.questphase / h49 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 25:Out → 45:In; 45:Out → 27:In; 45:Out → 46:In |
| `sts_cct_dtn_05_combat.questphase / h176 / 34` | `questLogicalAndNodeDefinition` `{}` | 34:Out1 → 1:In; 31:Out → 34:In1; 33:Out → 34:In2 |
| `sts_cct_dtn_05_combat.questphase / h176 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_guard_talk_002"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_camera_marina_004","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_camera_marina_001","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_camera_marina_005","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}}]}}` | 0:Out → 38:In; 38:Out → 27:dtn_05_chat_002_start |
| `sts_cct_dtn_05_combat.questphase / h176 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_guard_talk_001"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_camera_marina_002","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}}]}}` | 0:Out → 39:In; 39:Out → 2:dtn_05_chat_001_start |
| `sts_cct_dtn_05_combat.questphase / h256 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements"},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 22:Out → 21:In; 21:Out → 25:In1 |
| `sts_cct_dtn_05_combat.questphase / h256 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 20:Out → 24:In; 24:Out → 25:In2 |
| `sts_cct_dtn_05_combat.questphase / h256 / 25` | `questLogicalAndNodeDefinition` `{}` | 21:Out → 25:In1; 24:Out → 25:In2; 25:Out1 → 26:In; 25:Out1 → 27:In; 25:Out1 → 28:In; 25:Out1 → 29:In |
| `sts_cct_dtn_05_combat.questphase / h256 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"childRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements","names":["reinforcments_001"]}}}}` | 26:Out → 30:In; 30:Out → 54:In1 |
| `sts_cct_dtn_05_combat.questphase / h256 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"childRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements","names":["reinforcments_002"]}}}}` | 27:Out → 31:In; 31:Out → 54:In2 |
| `sts_cct_dtn_05_combat.questphase / h256 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"childRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements","names":["reinforcments_003"]}}}}` | 28:Out → 32:In; 32:Out → 54:In3 |
| `sts_cct_dtn_05_combat.questphase / h256 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"childRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_reinforcements","names":["reinforcments_004"]}}}}` | 29:Out → 33:In; 33:Out → 54:In4 |
| `sts_cct_dtn_05_combat.questphase / h256 / 54` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 30:Out → 54:In1; 31:Out → 54:In2; 32:Out → 54:In3; 33:Out → 54:In4; 54:Out1 → 55:In |
| `sts_cct_dtn_05_combat.questphase / h256 / 56` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 56:Out1 → 37:In; 47:Out → 56:In2; 49:Out → 56:In1; 51:Out → 56:In3; 52:Out → 56:In4 |
| `sts_cct_dtn_05_combat.questphase / h256 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 58:In; 58:Out → 59:In |
| `sts_cct_dtn_05_combat.questphase / h256 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_com_combat"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5}}},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_reinforcements"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_reinforcments_002"},"inverted":true}}]}}` | 58:Out → 59:In; 59:Out → 65:In; 59:Out → 66:In1 |
| `sts_cct_dtn_05_openworld.questphase / h12 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_sts_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 44:Out → 96:In; 96:Out → 73:In |
| `sts_cct_dtn_05_openworld.questphase / h218 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_johnny_talk"}}` | 0:Out → 44:In; 44:Out → 41:Start 0 |
| `sts_cct_dtn_05_openworld.questphase / h243 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#dtn_05_tr_cleanup"}]}}` | 59:Out → 16:In; 16:Out → 35:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat","comparisonType":"Equal"}}}` | 67:Out → 40:In; 40:True → 53:Succeeded; 40:False → 71:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/#c_city_center/downtown/downtown_drop_points_prefabQOBVMZA/drop_point_004_prefabYVOQU5I","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 48:Out → 44:In; 44:Out → 51:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h243 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 46:Out → 18:In; 39:Out → 46:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 45:Out → 49:In; 49:Out → 48:Active |
| `sts_cct_dtn_05_openworld.questphase / h243 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\city_center\\downtown\\sts_cct_dtn_05\\scenes\\sts_cct_dtn_05_holocall_debriefs.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 64:Out → 1:In; 36:Out → 64:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 67:Out → 40:In; 65:Out → 67:In |
| `sts_cct_dtn_05_openworld.questphase / h243 / 71` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 40:False → 71:In; 71:False → 50:Start 0; 71:True → 72:Active |
| `sts_cct_dtn_05_openworld.questphase / h243 / 73` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 43:Out → 73:In; 73:False → 47:Start 0; 73:True → 74:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_docks"}}` | 62:Out → 58:Succeeded; 143:Out → 62:In; 62:Out → 196:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_011"},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 3:Out → 100:In; 100:Out → 99:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_journal_test"}}}` | 3:Out → 109:In; 109:True → 59:Active; 109:False → 108:Active |
| `sts_cct_dtn_05_openworld.questphase / h614 / 110` | `questLogicalXorNodeDefinition` `{}` | 59:Out → 110:In1; 108:Out → 110:In2; 110:Out1 → 210:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_05_ps_car_006"},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 3:Out → 114:In; 114:Out → 113:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#dtn_05_tr_docks"}}` | 128:Out → 129:In; 129:Out → 130:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h614 / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat"}}}` | 143:Out → 145:In; 145:Out → 144:Failed |
| `sts_cct_dtn_05_openworld.questphase / h614 / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat","comparisonType":"Equal"}}}` | 130:Out → 147:In; 147:Out → 146:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h614 / 156` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#dtn_05_dvc_computer_003","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 194:Out → 156:In; 156:Out → 161:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 179` | `questLogicalXorNodeDefinition` `{}` | 130:Out → 179:In1; 177:Out → 179:In2; 179:Out1 → 199:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 185` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_tr_sts_content_block"}}` | 153:Out → 185:In; 185:Out → 184:In; 188:Out → 185:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#dtn_05_tr_sts_content_block"}}` | 184:Out → 187:In; 187:Out → 188:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 196` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#dtn_05_docks_control_room"}}` | 62:Out → 196:In; 196:Out → 195:Succeeded |
| `sts_cct_dtn_05_openworld.questphase / h614 / 209` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 3:Out → 209:In; 209:False → 153:Active; 209:True → 216:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\city_center\\downtown\\sts_cct_dtn_05\\scenes\\sts_cct_dtn_05_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 215:Out → 1:In; 199:Out → 215:In |
| `sts_cct_dtn_05_openworld.questphase / h614 / 216` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 216:True → 153:Active; 216:False → 201:Start 0; 209:True → 216:In |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 51` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_combat","comparisonType":"Equal"}}}` | 51:0:0 → 24:0:0; 51:0:1 → 48:0:0; 74:0:0 → 51:0:1 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_end_done"}}}` | 72:0:0 → 73:0:1; 77:0:0 → 72:0:1 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_done"}}}` | 70:666:0 → 249:0:1; 249:0:0 → 270:0:0 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":300}}}` | 70:666:0 → 254:0:1; 254:0:0 → 256:0:1; 263:0:0 → 254:0:1; 270:1:0 → 254:0:0; 270:1:0 → 254:1026:0 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 254:0:0 → 256:0:1; 256:0:0 → 258:0:1; 270:1:0 → 256:0:0; 270:1:0 → 256:1026:0 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":300}}}` | 256:0:0 → 258:0:1; 258:0:0 → 261:0:1; 270:1:0 → 258:0:0; 270:1:0 → 258:1026:0 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 261` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 258:0:0 → 261:0:1; 261:0:0 → 266:0:1; 261:0:1 → 263:0:0 |
| `sts_cct_dtn_05_holocall_debriefs.scene / scene / 286` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_rejected"}}}` | 76:0:0 → 286:0:1; 286:0:0 → 284:0:1 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_end_done"}}}` | 66:0:0 → 67:0:1; 71:0:0 → 66:0:1 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_rejected"}}}` | 70:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_done"}}}` | 64:666:0 → 267:0:1; 267:0:0 → 275:0:0 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 271` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 64:666:0 → 271:0:1; 271:0:0 → 280:0:1; 275:1:0 → 271:0:0 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 280` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 271:0:0 → 280:0:1; 280:0:0 → 286:0:1; 280:0:1 → 282:0:1; 282:0:0 → 280:0:1 |
| `sts_cct_dtn_05_holocall_prebrief.scene / scene / 282` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 275:1:0 → 282:0:0; 280:0:1 → 282:0:1; 282:0:0 → 280:0:1 |
| `sts_cct_dtn_05_johnny.scene / scene / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 4:0:0 → 22:0:1; 22:0:0 → 25:0:1 |
| `open_world_bugfixing.questphase / h1425 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h2561 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"dtn_05_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_cct_dtn_05_combat.questphase / h256 / 21; sts_cct_dtn_05_combat.questphase / h256 / 24; sts_cct_dtn_05_openworld.questphase / h614 / 100; sts_cct_dtn_05_openworld.questphase / h614 / 114 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_cct_downtown.questphase / h7140 / 210; sts_cct_dtn_05_openworld.questphase / h12 / 73; sts_cct_dtn_05_openworld.questphase / h614 / 210 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | sts_cct_dtn_05_combat.questphase / h256 / 37 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_cct_dtn_05_combat.questphase / h256 / 22; sts_cct_dtn_05_combat.questphase / h49 / 43; sts_cct_dtn_05_combat.questphase / h49 / 46; sts_cct_dtn_05_combat.questphase / h49 / 47; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1425 / 13; open_world_bugfixing.questphase / h2561 / 13; sts_cct_downtown.questphase / h6769 / 40; sts_cct_downtown.questphase / h7140 / 109; +18 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_cct_dtn_05_openworld.questphase / h243 / 18; sts_cct_dtn_05_openworld.questphase / h243 / 45; sts_cct_dtn_05_openworld.questphase / h243 / 54; sts_cct_dtn_05_openworld.questphase / h614 / 184; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_cct_downtown.questphase / h6769 / 43; sts_cct_downtown.questphase / h7140 / 173; sts_cct_dtn_05_combat.questphase / h0 / 19; sts_cct_dtn_05_combat.questphase / h0 / 20; +7 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_cct_dtn_05_openworld.questphase / h12 / 64; sts_cct_dtn_05_openworld.questphase / h12 / 67; sts_cct_dtn_05_openworld.questphase / h243 / 25; sts_cct_dtn_05_openworld.questphase / h243 / 27; +8 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_cct_downtown.questphase / h4373 / 59; sts_cct_downtown.questphase / h6769 / 44; sts_cct_downtown.questphase / h7140 / 156; sts_cct_dtn_05_combat.questphase / h0 / 14; +6 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_cct_dtn_05_openworld.questphase / h243 / 16 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1425 / 14; open_world_bugfixing.questphase / h2561 / 14; sts_cct_downtown.questphase / h6769 / 38; sts_cct_downtown.questphase / h6769 / 51; +42 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | sts_cct_dtn_05_combat.questphase / h256 / 30; sts_cct_dtn_05_combat.questphase / h256 / 31; sts_cct_dtn_05_combat.questphase / h256 / 32; sts_cct_dtn_05_combat.questphase / h256 / 33 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | sts_cct_dtn_05_combat.questphase / h176 / 34; sts_cct_dtn_05_combat.questphase / h256 / 25; sts_cct_dtn_05_combat.questphase / h256 / 54; sts_cct_dtn_05_combat.questphase / h256 / 56; +1 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_cct_downtown.questphase / h6769 / 39; sts_cct_dtn_05_combat.questphase / h176 / 31; sts_cct_dtn_05_combat.questphase / h176 / 33; sts_cct_dtn_05_combat.questphase / h256 / 65; +28 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_cct_downtown.questphase / h7140 / 110; sts_cct_downtown.questphase / h7140 / 179; sts_cct_dtn_05_openworld.questphase / h614 / 110; sts_cct_dtn_05_openworld.questphase / h614 / 179 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_cct_dtn_05_combat.questphase / h0 / 11; sts_cct_dtn_05_combat.questphase / h0 / 12; sts_cct_dtn_05_combat.questphase / h49 / 45; sts_cct_dtn_05_holocall_debriefs.scene / scene / 254; +6 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_cct_downtown.questphase / h6769 / 41; sts_cct_downtown.questphase / h6769 / 42; sts_cct_dtn_05_openworld.questphase / h243 / 41; sts_cct_dtn_05_openworld.questphase / h243 / 42 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_cct_dtn_05_combat.questphase / h176 / 2; sts_cct_dtn_05_combat.questphase / h176 / 27; sts_cct_dtn_05_openworld.questphase / h218 / 41; sts_cct_dtn_05_openworld.questphase / h243 / 47; +2 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_cct_downtown.questphase / h4373 / 59; sts_cct_downtown.questphase / h7140 / 129; sts_cct_downtown.questphase / h7140 / 196; sts_cct_downtown.questphase / h7140 / 62; +14 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_cct_downtown.questphase / h4373 / 59; sts_cct_dtn_05_combat.questphase / h0 / 6; sts_cct_dtn_05_combat.questphase / h0 / 9; sts_cct_dtn_05_combat.questphase / h256 / 59 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sts_cct_dtn_05_combat.questphase / h256 / 26; sts_cct_dtn_05_combat.questphase / h256 / 27; sts_cct_dtn_05_combat.questphase / h256 / 28; sts_cct_dtn_05_combat.questphase / h256 / 29; +11 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sts_cct_dtn_05_combat.questphase / h49 / 48; sts_cct_dtn_05_johnny.scene / scene / 25; sts_cct_dtn_05_johnny.scene / scene / 35 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_cct_dtn_05_openworld.questphase / h12 / 63; sts_cct_dtn_05_openworld.questphase / h12 / 95; sts_cct_dtn_05_openworld.questphase / h243 / 15; sts_cct_dtn_05_openworld.questphase / h67 / 2; +5 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_downtown_bugfixing.questphase` | repair; journal anchor | `base-shared` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` | content candidate; journal anchor | `base-sts-cct-dtn-05` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` | content candidate; journal anchor | `base-sts-cct-dtn-05` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene` | content candidate; forward dependency | `base-sts-cct-dtn-05` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-cct-dtn-05` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-cct-dtn-05` |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene` | content candidate; forward dependency | `base-sts-cct-dtn-05` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-cct-dtn-05](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-cct-dtn-05.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

218 repeated typed/socket path signatures in this selected graph context; 24 distinct direct resource identities; 12 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 76 -> 286 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 75 -> 77 -> 72 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 286 -> 284 -> 288 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` / scene / 65 -> 68 -> 26 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 24 -> 75 -> 77 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene` / scene / 1 -> 4 -> 3 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 282 -> 76 -> 286 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 1 -> 282 -> 76 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase` / h7140 / 196 -> 195 -> 192 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 249 -> 270 -> 254 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` / scene / 286 -> 284 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `10de5d2a81ab97879de5` | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h176 / 33 -> 34 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out -> In2; Out1 -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h0 / 2 | `h9` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h0 / 3 | `h33` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h33 / 17 | `h49` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h33 / 21 | `h176` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h0 / 4 | `h256` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h256 / 66 | `h450` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h12 / 66 | `h67` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h0 / 3 | `h211` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h211 / 11 | `h218` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":32,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h0 / 4 | `h243` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h0 / 5 | `h614` | [{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":3,"socketName":"In1"}] |

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
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.gamedef` | content candidate | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.quest |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05_test.gamedef` | content candidate | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.quest |
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
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\phases\sts_cct_dtn_02_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\phases\sts_cct_dtn_02_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\phases\sts_cct_dtn_02_questphase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\phases\sts_cct_dtn_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\phases\sts_cct_dtn_03_main_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\phases\sts_cct_dtn_03_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\phases\sts_cct_dtn_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\phases\sts_cct_dtn_04_av_disposal.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\phases\sts_cct_dtn_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\phases\sts_cct_dtn_04_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_guards\sec_high_m_01_enus_30_big.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_guards\sec_high_m_03_afam_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_holocall_debriefs\dino_dyno_dinovic.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_holocall_prebrief\dino_dyno_dinovic.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_johnny\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\lipsync\en\sts_cct_dtn_05_johnny\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `cct_achievement` | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase / h0 / 22; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase / h0 / 30; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase / h0 / 24; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase / h0 / 44; 16 total source locations in compressed evidence |
| `dtn_005_chat_001_end` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h4293 / 31; 1 total source locations in compressed evidence |
| `dtn_005_chat_002_end` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h4293 / 33; 1 total source locations in compressed evidence |
| `dtn_05_active` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h6538 / 87; base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h6769 / 36; 2 total source locations in compressed evidence |
| `dtn_05_cleanup` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h6769 / 35; 1 total source locations in compressed evidence |
| `dtn_05_combat` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h4150 / 28; 1 total source locations in compressed evidence |
| `dtn_05_journal_test` | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.quest / h0 / 3; 1 total source locations in compressed evidence |
| `dtn_05_reinforcements_active` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h4373 / 65; 1 total source locations in compressed evidence |
| `dtn_05_start` | base\open_world\street_stories\city_center\downtown\sts_cct_downtown.questphase / h6538 / 88; 1 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_dino_calls_v_end_activate` | base\open_world\fixers\dyno\phases\dyno.questphase / h0 / 44; base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 220; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h228 / 79; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h629 / 68; 41 total source locations in compressed evidence |
| `holo_dino_calls_v_end_done` | base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 216; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 99; base\quest\holocalls\dino\dino_holocall.scene / scene / 42; base\quest\holocalls\dino\dino_holocall.scene / scene / 553; 14 total source locations in compressed evidence |
| `holo_dino_calls_v_rejectable` | base\quest\holocalls\dino\dino_holocall.scene / scene / 636; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene / scene / 280; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene / scene / 262; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene / scene / 304; 14 total source locations in compressed evidence |
| `holo_dino_calls_v_rejected` | base\quest\holocalls\dino\dino_holocall.scene / scene / 644; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene / scene / 282; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene / scene / 264; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_debriefs.scene / scene / 285; 10 total source locations in compressed evidence |
| `holo_dino_calls_v_start_activate` | base\open_world\fixers\dyno\phases\dyno.questphase / h0 / 43; base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 219; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h228 / 78; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h629 / 67; 50 total source locations in compressed evidence |
| `holo_dino_calls_v_start_done` | base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 214; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 98; base\quest\holocalls\dino\dino_holocall.scene / scene / 41; base\quest\holocalls\dino\dino_holocall.scene / scene / 580; 14 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |

NodeRef uses: 186; TweakDB binding uses: 13. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene` | 2 / 6 | scnDialogLineEvent: 6 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` | 2 / 4 | scnDialogLineEvent: 4 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene` | 1 / 4 | scnDialogLineEvent: 4 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
