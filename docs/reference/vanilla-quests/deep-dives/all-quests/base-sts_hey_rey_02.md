# Gig: Sr. Ladrillo's Private Collection

Journal: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` · `StreetStory` · hash `3578660365`.

Journal premise: Gig type: Thievery\nObjective: Steal data from a computer\nLocation: Dicky Twister, corner of Congress and Pajaro St.\nDetails:\n\nSaint Augustine once wrote: When one has a healthy sense of smell, he will immediately recognize the stench of sin. Well, even anyone with a sinus infection in this city can smell the fuckfests over at Dicky Twister. This gay strip club is full of chicos with glazed, dead eyes who will do anything you desire for an extra eddie tucked into their thongs.\n\nThe stench coming from that place finally wafted into NCPD command. My little rats tell me they plan to kick down the door any day now. That's bad news. The owner of Dicky Twister, a pimp called Sr. Ladrillo, is no gonk – and a fanatic for recordkeeping. He has a computer full of data thanks to spying tech in his VIP rooms. We're talking politicians, suits, crime bosses, celebrities (maybe even the cops themselves)... If the boys in blue get their hands on these recordings, Ladrillo's geniusly built house of cards collapses, leaving the whole district in chaos. And chaos isn't in our best interest at the moment.\n\nKlep those recordings at the Dicky Twister before the cops do. Thankfully, the Lord has blessed us – Ladrillo is currently out of town. But better to make haste, for ignoring divine assistance is a sin in its own right.

**Coverage: journal-linked.** 27 exact journal-linked nodes in 5 resources; 8 resources in the inspected dependency context.

Resource roles in that context: 7 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Deposit the compromising material in the Drop Point. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/drop` |
| Get out of Dicky Twister. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape` |
| Get to Sr. Ladrillo's office. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room` |
| Go to Dicky Twister. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` |
| Steal the compromising material from within Dicky Twister. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_hey_rey_02_gameplay.questphase / h341 / 26` (PauseCondition: IsSystemInCombat) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 0:Out → 26:In; 26:Out → 32:In; 26:Out → 40:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 3` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 58:False → 3:Active; 3:Out → 57:In2 |
| `sts_hey_rey_02_open_world.questphase / h587 / 7` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room` | 6:Out → 7:Active; 7:Out → 8:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 10` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room` | 8:Out → 10:Succeeded; 10:Out → 93:Active |
| `sts_hey_rey_02_open_world.questphase / h587 / 15` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 102:Out → 15:Succeeded; 15:Out → 42:Active; 15:Out → 94:In; 15:Out → 95:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 6` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 6:Out → 7:Active; 53:Out → 6:Succeeded |
| `sts_hey_rey_02_open_world.questphase / h587 / 41` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` | 49:Out → 41:Succeeded; 41:Out → 118:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 42` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape` | 15:Out → 42:Active; 42:Out → 46:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 49` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape` | 49:Out → 41:Succeeded; 46:Out → 49:Succeeded |
| `sts_hey_rey_02_open_world.questphase / h587 / 60` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 60:Out → 57:In1; 58:True → 60:Active |
| `sts_hey_rey_02_open_world.questphase / h587 / 67` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/brief` | 74:Out → 67:Active |
| `sts_hey_rey_02_open_world.questphase / h587 / 93` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 10:Out → 93:Active; 93:Out → 100:In |
| `sts_hey_rey_02_gangers.scene / scene / 239` (PauseCondition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 222:0:0 → 239:0:1; 239:0:0 → 218:0:0; input mappings: 0:0=CutDestination, 0:1=In |
| `sts_hey_vista_del_rey.questphase / h5686 / 26` (PauseCondition: IsSystemInCombat) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 0:Out → 26:In; 26:Out → 32:In; 26:Out → 40:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 3` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 58:False → 3:Active; 3:Out → 57:In2 |
| `sts_hey_vista_del_rey.questphase / h6436 / 7` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room` | 6:Out → 7:Active; 7:Out → 8:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 10` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room` | 8:Out → 10:Succeeded; 10:Out → 93:Active |
| `sts_hey_vista_del_rey.questphase / h6436 / 15` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 102:Out → 15:Succeeded; 15:Out → 42:Active; 15:Out → 94:In; 15:Out → 95:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 6` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 6:Out → 7:Active; 53:Out → 6:Succeeded |
| `sts_hey_vista_del_rey.questphase / h6436 / 41` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` | 49:Out → 41:Succeeded; 41:Out → 118:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 42` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape` | 15:Out → 42:Active; 42:Out → 46:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 49` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape` | 49:Out → 41:Succeeded; 46:Out → 49:Succeeded |
| `sts_hey_vista_del_rey.questphase / h6436 / 60` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club` | 60:Out → 57:In1; 58:True → 60:Active |
| `sts_hey_vista_del_rey.questphase / h6436 / 67` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/brief` | 74:Out → 67:Active |
| `sts_hey_vista_del_rey.questphase / h6436 / 93` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad` | 10:Out → 93:Active; 93:Out → 100:In |
| `open_world_bugfixing.questphase / h1127 / 25` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` | 24:True → 25:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 25` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02` | 24:True → 25:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_hey_rey_02_gameplay.questphase / h277 / 22` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene`; `#sts_sm_hey_rey_02_gangers` | 26:Out → 22:rey_02_ganger_chat_001_start |
| `sts_hey_rey_02_gameplay.questphase / h277 / 24` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene`; `#sts_sm_hey_rey_02_gangers` | 28:Out → 24:rey_02_stippers_chat_001_start |
| `sts_hey_rey_02_open_world.questphase / h214 / 8` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene`; `#sts_sm_hey_rey_02_civilians` | 13:Out → 8:rey_02_civilians_chat_001_start |
| `sts_hey_rey_02_open_world.questphase / h214 / 9` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene`; `#sts_sm_hey_rey_02_civilians` | 14:Out → 9:rey_02_civilians_chat_002_start |
| `sts_hey_rey_02_open_world.questphase / h214 / 11` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene`; `#sts_sm_hey_rey_02_civilians` | 15:Out → 11:rey_02_civilians_chat_004_start |
| `sts_hey_rey_02_open_world.questphase / h281 / 64` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene`; `#sts_sm_hey_rey_02_holocall_debriefs` | 64:End 0 → 52:In; 85:False → 64:Start 0; 64:rejected_out → 86:Active; 64:Holocall INT → 66:In; 64:Holocall RET → 65:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 103` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene`; `#sts_sm_hey_rey_02_holocall_prebrief` | 103:End 0 → 86:Active; 103:rejected_out → 86:Active; 105:True → 103:Start 0; 103:Holocall INT → 108:In; 103:Holocall RET → 107:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase` / h0 / 9 | `sts_hey_rey_02_gameplay.questphase` | 0: Input; 0:Out → 9:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h9065 / 9 | `sts_hey_rey_02_gameplay.questphase` | 0: Input; 0:Out → 9:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase` / h0 / 10 | `sts_hey_rey_02_open_world.questphase` | 0: Input; 0:Out → 10:In1; 10:Out1 → 1:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h9065 / 10 | `sts_hey_rey_02_open_world.questphase` | 0: Input; 0:Out → 10:In1; 10:Out1 → 1:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h214 / 8 | `sts_hey_rey_02_civilians.scene` | 13: PauseCondition: #rey_02_tr_chat_001; 13:Out → 8:rey_02_civilians_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h214 / 9 | `sts_hey_rey_02_civilians.scene` | 14: PauseCondition: #rey_02_tr_chat_002; 14:Out → 9:rey_02_civilians_chat_002_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h214 / 11 | `sts_hey_rey_02_civilians.scene` | 15: PauseCondition: #rey_02_tr_chat_004; 15:Out → 11:rey_02_civilians_chat_004_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h6063 / 8 | `sts_hey_rey_02_civilians.scene` | 13: PauseCondition: #rey_02_tr_chat_001; 13:Out → 8:rey_02_civilians_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h6063 / 9 | `sts_hey_rey_02_civilians.scene` | 14: PauseCondition: #rey_02_tr_chat_002; 14:Out → 9:rey_02_civilians_chat_002_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h6063 / 11 | `sts_hey_rey_02_civilians.scene` | 15: PauseCondition: #rey_02_tr_chat_004; 15:Out → 11:rey_02_civilians_chat_004_start |
| `base\open_world\community\heywood\vista_del_rey\phases\hey_rey_phase.questphase` / h57 / 3 | `sts_hey_rey_02_gangers.scene` | 7: PauseCondition: #rey_02_tr_ganger_doors; 7:Out → 3:rey_02_entrence_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h277 / 22 | `sts_hey_rey_02_gangers.scene` | 26: PauseCondition: #rey_02_tr_up_patrol_start; 26:Out → 22:rey_02_ganger_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h277 / 24 | `sts_hey_rey_02_gangers.scene` | 28: PauseCondition: {"seconds": 2}; 28:Out → 24:rey_02_stippers_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h5622 / 22 | `sts_hey_rey_02_gangers.scene` | 26: PauseCondition: #rey_02_tr_up_patrol_start; 26:Out → 22:rey_02_ganger_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h5622 / 24 | `sts_hey_rey_02_gangers.scene` | 28: PauseCondition: {"seconds": 2}; 28:Out → 24:rey_02_stippers_chat_001_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h281 / 64 | `sts_hey_rey_02_holocall_debriefs.scene` | 85: Condition; 64:End 0 → 52:In; 85:False → 64:Start 0; 64:rejected_out → 86:Active; 64:Holocall INT → 66:In; 64:Holocall RET → 65:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h6130 / 64 | `sts_hey_rey_02_holocall_debriefs.scene` | 85: Condition; 64:End 0 → 52:In; 85:False → 64:Start 0; 64:rejected_out → 86:Active; 64:Holocall INT → 66:In; 64:Holocall RET → 65:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h587 / 103 | `sts_hey_rey_02_holocall_prebrief.scene` | 105: Condition; 103:End 0 → 86:Active; 103:rejected_out → 86:Active; 105:True → 103:Start 0; 103:Holocall INT → 108:In; 103:Holocall RET → 107:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h6436 / 103 | `sts_hey_rey_02_holocall_prebrief.scene` | 105: Condition; 103:End 0 → 86:Active; 103:rejected_out → 86:Active; 105:True → 103:Start 0; 103:Holocall INT → 108:In; 103:Holocall RET → 107:In |
| `base\open_world\street_stories\heywood\sts_heywood.questphase` / h0 / 3 | `sts_hey_vista_del_rey.questphase` | 0: Input; 5: Input; 0:Out → 3:In1; 5:Out → 3:sts_hey_rey_02_bugfixing |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` / h0 / 1 | `sts_hey_rey_02.questphase` | 3: FactsDBManager: rey_02_journal_test; 3:Out → 1:In1; 1:Out1 → 2:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h0 / 6 | `sts_hey_rey_02.questphase` | 37: Journal; 45: Journal; 62: Input; 37:Out → 6:In1; 45:Out → 6:In1; 62:Out → 6:In1 |
| `base\open_world\community\global_phase\open_world_global_commuinity_phase.questphase` / h0 / 15 | `hey_rey_phase.questphase` | 0: Input; 0:Out → 15:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 4 | `sts_heywood.questphase` | 0: Input; 21: Input; 0:Out → 4:In1; 21:Out → 4:sts_hey_rey_02_bugfixing |
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
| `base\open_world\community\global_phase\open_world_global_community_quest.quest` / h0 / 0 | `open_world_global_commuinity_phase.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 1 | `open_world_global_commuinity_phase.questphase` | 0: Input; 122: Input; 0:Out → 1:In1; 122:Out → 1:In1 |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\sts_cct_dtn_03_quest.quest` / h0 / 10 | `open_world_global_commuinity_phase.questphase` | 7: FactsDBManager: dtn_03_test_definition; 7:Out → 10:In1 |
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
| `sts_hey_rey_02_civilians.scene` | rey_02_distract_holograms_start, rey_02_civilians_chat_004_start, rey_02_civilians_chat_001_start, rey_02_civilians_chat_002_start → rey_02_civilians_chat_001_end, rey_02_civilians_chat_002_end, rey_02_civilians_chat_004_end, rey_02_distract_holograms_end | civilian_talk_001; civilian_talk_002; civilian_talk_004; civilian_talk_005; 18 nodes / 18 edges |
| `sts_hey_rey_02_gangers.scene` | rey_02_entrence_start, rey_02_ganger_chat_001_start, rey_02_stippers_chat_001_start → rey_02_entrence_end, rey_02_ganger_chat_001_end, rey_02_stippers_chat_001_end | ganger_001; ganger_003; ganger_005; prostitute_001; prostitute_002; V; 29 nodes / 32 edges |
| `sts_hey_rey_02_holocall_debriefs.scene` | Start 0 → End 0, rejected_out | Padre; Player; 23 nodes / 30 edges |
| `sts_hey_rey_02_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | Padre; Player; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_hey_rey_02_gangers.scene / n30 / 0` | Here you go. (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentFixedAmount_ConditionType", "scriptCondition": {"$type": "PaymentFixedAmount_ScriptConditionType", "payAmount": 100}}}} | 0:0 → 12:0:0 |
| `sts_hey_rey_02_gangers.scene / n30 / 1` | Came to fix your sound system. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "buildId": "85601791440", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 26:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_valentinos` | sts_hey_rey_02_open_world.questphase / h587 / 74; sts_hey_vista_del_rey.questphase / h6436 / 74 | No reader in selected context |
| `hey_achievement` | sts_hey_rey_02_open_world.questphase / h281 / 49 | sts_hey_rey_02_open_world.questphase / h281 / 73 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_hey_rey_02_holocall_prebrief.scene / scene / 279 |
| `holo_padre_calls_v_end_activate` | sts_hey_rey_02_holocall_debriefs.scene / scene / 63; sts_hey_rey_02_holocall_prebrief.scene / scene / 64; sts_hey_rey_02_open_world.questphase / h281 / 66; sts_hey_rey_02_open_world.questphase / h587 / 108 | No reader in selected context |
| `holo_padre_calls_v_end_done` | sts_hey_rey_02_holocall_debriefs.scene / scene / 59; sts_hey_rey_02_holocall_prebrief.scene / scene / 60 | sts_hey_rey_02_holocall_debriefs.scene / scene / 58; sts_hey_rey_02_holocall_prebrief.scene / scene / 59 |
| `holo_padre_calls_v_rejectable` | sts_hey_rey_02_holocall_debriefs.scene / scene / 290; sts_hey_rey_02_holocall_prebrief.scene / scene / 254; sts_hey_rey_02_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_padre_calls_v_rejected` | sts_hey_rey_02_holocall_debriefs.scene / scene / 295; sts_hey_rey_02_holocall_prebrief.scene / scene / 258 | sts_hey_rey_02_holocall_debriefs.scene / scene / 293; sts_hey_rey_02_holocall_prebrief.scene / scene / 256 |
| `holo_padre_calls_v_start_activate` | sts_hey_rey_02_holocall_debriefs.scene / scene / 284; sts_hey_rey_02_holocall_debriefs.scene / scene / 62; sts_hey_rey_02_holocall_prebrief.scene / scene / 283; sts_hey_rey_02_holocall_prebrief.scene / scene / 63; sts_hey_rey_02_open_world.questphase / h281 / 65; sts_hey_rey_02_open_world.questphase / h587 / 107 | sts_hey_rey_02_holocall_debriefs.scene / scene / 257 |
| `holo_padre_calls_v_start_done` | sts_hey_rey_02_holocall_debriefs.scene / scene / 57; sts_hey_rey_02_holocall_prebrief.scene / scene / 58 | sts_hey_rey_02_holocall_debriefs.scene / scene / 249; sts_hey_rey_02_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_hey_rey_02_holocall_debriefs.scene / scene / 257; sts_hey_rey_02_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_hey_rey_02_holocall_debriefs.scene / scene / 257; sts_hey_rey_02_holocall_prebrief.scene / scene / 279 |
| `rey_02_authorized` | Producer outside selected context | sts_hey_rey_02_open_world.questphase / h587 / 62 |
| `rey_02_finished` | sts_hey_rey_02_open_world.questphase / h281 / 51 | open_world_bugfixing.questphase / h1127 / 24; open_world_bugfixing.questphase / h2262 / 24 |
| `rey_02_gang_chase` | sts_hey_rey_02_open_world.questphase / h281 / 90 | No reader in selected context |
| `rey_02_gang_retaliation` | sts_hey_rey_02_gameplay.questphase / h12 / 18 | sts_hey_rey_02_open_world.questphase / h281 / 87 |
| `rey_02_ganger_005_patrol` | sts_hey_rey_02_gangers.scene / scene / 126 | sts_hey_rey_02_gameplay.questphase / h28 / 44 |
| `rey_02_journal_test` | Producer outside selected context | sts_hey_rey_02_open_world.questphase / h587 / 58; sts_hey_vista_del_rey.questphase / h6436 / 58 |
| `rey_02_start` | sts_hey_rey_02_open_world.questphase / h587 / 59 | No reader in selected context |
| `rey_08_finished` | Producer outside selected context | sts_hey_rey_02_open_world.questphase / h587 / 88 |
| `sts_valentinos_retaliation` | sts_hey_rey_02_open_world.questphase / h281 / 88 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>87 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_hey_rey_02_gameplay.questphase / h12 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 14:In; 14:Out → 18:In |
| `sts_hey_rey_02_gameplay.questphase / h28 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_strip_club_enter"}}` | 0:Out → 25:In; 25:Out → 24:In1; 25:Out → 30:In1 |
| `sts_hey_rey_02_gameplay.questphase / h28 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_up_patrol_start"}}` | 0:Out → 26:In |
| `sts_hey_rey_02_gameplay.questphase / h28 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_stripper_patrol_start"}}` | 0:Out → 38:In; 38:Out → 20:In1 |
| `sts_hey_rey_02_gameplay.questphase / h28 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":1}}}` | 39:Out1 → 42:In; 42:Out → 40:In1 |
| `sts_hey_rey_02_gameplay.questphase / h28 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":1}}}` | 39:Out2 → 43:In; 43:Out → 41:In1 |
| `sts_hey_rey_02_gameplay.questphase / h28 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_ganger_005_patrol"}}}` | 0:Out → 44:In; 44:Out → 8:In1 |
| `sts_hey_rey_02_gameplay.questphase / h62 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":3}}}` | 0:Out → 7:In; 7:Out → 6:In |
| `sts_hey_rey_02_gameplay.questphase / h143 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_patrol_ganger_007"}}` | 0:Out → 4:In; 4:Out → 6:In1 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_door_demo_001","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 5:In; 5:Out → 6:In2 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 6` | `questLogicalXorNodeDefinition` `{"inputSocketCount":5}` | 6:Out1 → 1:In; 4:Out → 6:In1; 5:Out → 6:In2; 7:Out → 6:In3; 8:Out → 6:In4; 9:Out → 6:In5 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_door_generic_001","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 7:In; 7:Out → 6:In3 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_door_generic_002","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 8:In; 8:Out → 6:In4 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_door_generic_003","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 9:In; 9:Out → 6:In5 |
| `sts_hey_rey_02_gameplay.questphase / h143 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_patrol_ganger_007_B"}}` | 0:Out → 10:In; 10:Out → 2:In |
| `sts_hey_rey_02_gameplay.questphase / h233 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_007"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 8:Out → 5:In; 6:Out → 8:In |
| `sts_hey_rey_02_gameplay.questphase / h277 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_up_patrol_start"}}` | 0:Out → 26:In; 26:Out → 22:rey_02_ganger_chat_001_start |
| `sts_hey_rey_02_gameplay.questphase / h277 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_stripper_patrol_start"}}` | 0:Out → 27:In; 27:Out → 28:In |
| `sts_hey_rey_02_gameplay.questphase / h277 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 28:Out → 24:rey_02_stippers_chat_001_start; 27:Out → 28:In |
| `sts_hey_rey_02_gameplay.questphase / h341 / 9` | `questLogicalAndNodeDefinition` `{}` | 5:Out → 9:In2; 9:Out1 → 8:In; 24:Out → 9:In1 |
| `sts_hey_rey_02_gameplay.questphase / h341 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_strip_club_enter"}]}}` | 0:Out → 26:In; 26:Out → 32:In; 26:Out → 40:In |
| `sts_hey_rey_02_gameplay.questphase / h341 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_reinforcement"},"isPlayer":false,"inverted":true}}}` | 8:Success → 27:In; 27:Out → 28:In; 27:Out → 29:In |
| `sts_hey_rey_02_gameplay.questphase / h341 / 31` | `questLogicalAndNodeDefinition` `{}` | 31:Out1 → 1:In; 28:Work Started → 31:In1; 29:Work Started → 31:In2 |
| `sts_hey_rey_02_gameplay.questphase / h341 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_006","ganger_007"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false,"unconscious":false,"defeated":false}}}` | 26:Out → 32:In; 32:True → 33:In; 32:False → 36:In; 32:False → 37:In |
| `sts_hey_rey_02_gameplay.questphase / h341 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_006"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false,"unconscious":false,"defeated":false}}}` | 32:False → 36:In; 36:Out → 39:In |
| `sts_hey_rey_02_gameplay.questphase / h341 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_007"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false,"unconscious":false,"defeated":false}}}` | 32:False → 37:In; 37:Out → 38:In |
| `sts_hey_rey_02_gameplay.questphase / h481 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 26:Out → 1:In; 27:Out → 26:In |
| `sts_hey_rey_02_open_world.questphase / h12 / 52` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 70:Out → 52:In1; 32:Out → 52:In2; 61:Out → 52:In3; 52:Out1 → 63:In |
| `sts_hey_rey_02_open_world.questphase / h12 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_sts_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 65:Out → 64:In; 64:Out → 75:In |
| `sts_hey_rey_02_open_world.questphase / h214 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_chat_001"}}` | 0:Out → 13:In; 13:Out → 8:rey_02_civilians_chat_001_start |
| `sts_hey_rey_02_open_world.questphase / h214 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_chat_002"}}` | 0:Out → 14:In; 14:Out → 9:rey_02_civilians_chat_002_start |
| `sts_hey_rey_02_open_world.questphase / h214 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_chat_004"}}` | 0:Out → 15:In; 15:Out → 11:rey_02_civilians_chat_004_start |
| `sts_hey_rey_02_open_world.questphase / h281 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_02_tr_sts_clean_up"}}` | 71:Out → 46:In; 72:Out → 71:In; 71:Out → 78:In |
| `sts_hey_rey_02_open_world.questphase / h281 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 74:Out → 72:In; 75:Out → 74:In |
| `sts_hey_rey_02_open_world.questphase / h281 / 85` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 85:False → 64:Start 0; 84:Out → 85:In; 85:True → 86:Active |
| `sts_hey_rey_02_open_world.questphase / h281 / 87` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 87:False → 48:In; 51:Out → 87:In; 87:True → 90:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_office_room"}}` | 7:Out → 8:In; 8:Out → 10:Succeeded |
| `sts_hey_rey_02_open_world.questphase / h587 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_02_tr_strip_club_exit"}}` | 42:Out → 46:In; 46:Out → 49:Succeeded |
| `sts_hey_rey_02_open_world.questphase / h587 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_strip_club_enter"}}` | 53:Out → 6:Succeeded; 57:Out1 → 53:In; 53:Out → 77:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 57` | `questLogicalXorNodeDefinition` `{}` | 3:Out → 57:In2; 57:Out1 → 53:In; 60:Out → 57:In1 |
| `sts_hey_rey_02_open_world.questphase / h587 / 58` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_journal_test"}}}` | 58:False → 3:Active; 74:Out → 58:In; 58:True → 60:Active |
| `sts_hey_rey_02_open_world.questphase / h587 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_authorized"}}}` | 0:Out → 62:In; 62:Out → 63:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_sts_start"}}` | 82:Out → 79:In; 86:Out → 79:In; 79:Out → 81:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_02_tr_sts_start"}}` | 81:Out → 80:In; 80:Out → 82:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 84` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_007"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 84:In; 84:Out → 85:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_08_finished"}}}` | 0:Out → 88:In; 88:Out → 92:In; 88:Out → 90:In; 88:Out → 91:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_ps_fluff_car_001"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 97:In; 97:Out → 99:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_computer_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 93:Out → 100:In; 100:Out → 101:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 105` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 105:False → 86:Active; 105:True → 103:Start 0; 119:False → 105:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 118` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 118:Out → 1:In; 41:Out → 118:In |
| `sts_hey_rey_02_open_world.questphase / h587 / 119` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 119:True → 86:Active; 87:Out → 119:In; 119:False → 105:In |
| `sts_hey_rey_02_open_world.questphase / h684 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#rey_02_dvc_button","eventType":"Executed"}}}` | 2:Out → 6:In; 6:Out → 3:In; 6:Out → 10:In |
| `sts_hey_rey_02_civilians.scene / scene / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_hologram_module","deviceControllerClass":"GenericDeviceControllerPS","deviceConditionFunction":"WasQuickHacked"}}}` | 1:0:0 → 54:0:1; 54:0:0 → 81:0:1; 54:0:0 → 90:0:1 |
| `sts_hey_rey_02_civilians.scene / scene / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 54:0:0 → 81:0:1; 81:0:0 → 79:0:0 |
| `sts_hey_rey_02_civilians.scene / scene / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 54:0:0 → 90:0:1; 90:0:0 → 12:0:0 |
| `sts_hey_rey_02_civilians.scene / scene / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 13:0:0 → 93:0:1; 93:0:0 → 41:0:0 |
| `sts_hey_rey_02_civilians.scene / scene / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 14:0:0 → 96:0:1; 96:0:0 → 42:0:0 |
| `sts_hey_rey_02_civilians.scene / scene / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 22:0:0 → 99:0:1; 99:0:0 → 44:0:0 |
| `sts_hey_rey_02_gangers.scene / scene / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 132:0:0 → 218:0:1; 222:0:0 → 132:0:1 |
| `sts_hey_rey_02_gangers.scene / scene / 142` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_gangers.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 89:0:0 → 142:0:1; 142:0:0 → 126:0:1 |
| `sts_hey_rey_02_gangers.scene / scene / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_gangers.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 98:0:0 → 146:0:1; 146:0:0 → 99:0:0 |
| `sts_hey_rey_02_gangers.scene / scene / 214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_001"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 214:0:0 → 218:0:2; 222:0:0 → 214:0:1 |
| `sts_hey_rey_02_gangers.scene / scene / 239` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 222:0:0 → 239:0:1; 239:0:0 → 218:0:0 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 58:0:0 → 59:0:1; 63:0:0 → 58:0:1 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 56:666:0 → 249:0:1; 249:0:0 → 254:0:0 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":400}}}` | 56:666:0 → 251:0:1; 251:0:0 → 257:0:1; 254:1:0 → 251:0:0; 254:1:0 → 251:1026:0; 281:0:0 → 251:0:1 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 257` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 251:0:0 → 257:0:1; 254:1:0 → 257:0:0; 254:1:0 → 257:1026:0; 257:0:0 → 265:0:1 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":400}}}` | 254:1:0 → 265:0:0; 254:1:0 → 265:1026:0; 257:0:0 → 265:0:1; 265:0:0 → 279:0:1 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 265:0:0 → 279:0:1; 279:0:0 → 284:0:1; 279:0:1 → 281:0:0 |
| `sts_hey_rey_02_holocall_debriefs.scene / scene / 293` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 62:0:0 → 293:0:1; 293:0:0 → 295:0:1 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 59:0:0 → 60:0:1; 64:0:0 → 59:0:1 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 63:0:0 → 256:0:1; 256:0:0 → 258:0:1 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 57:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 57:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_hey_rey_02_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_hey_vista_del_rey.questphase / h5686 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_strip_club_enter"}]}}` | 0:Out → 26:In; 26:Out → 32:In; 26:Out → 40:In |
| `sts_hey_vista_del_rey.questphase / h5686 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_02_com_enemies","names":["ganger_006","ganger_007"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false,"unconscious":false,"defeated":false}}}` | 26:Out → 32:In; 32:True → 33:In; 32:False → 36:In; 32:False → 37:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_office_room"}}` | 7:Out → 8:In; 8:Out → 10:Succeeded |
| `sts_hey_vista_del_rey.questphase / h6436 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_02_tr_strip_club_exit"}}` | 42:Out → 46:In; 46:Out → 49:Succeeded |
| `sts_hey_vista_del_rey.questphase / h6436 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_02_tr_strip_club_enter"}}` | 53:Out → 6:Succeeded; 57:Out1 → 53:In; 53:Out → 77:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 57` | `questLogicalXorNodeDefinition` `{}` | 3:Out → 57:In2; 57:Out1 → 53:In; 60:Out → 57:In1 |
| `sts_hey_vista_del_rey.questphase / h6436 / 58` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_journal_test"}}}` | 58:False → 3:Active; 74:Out → 58:In; 58:True → 60:Active |
| `sts_hey_vista_del_rey.questphase / h6436 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_02_dvc_computer_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 93:Out → 100:In; 100:Out → 101:In |
| `sts_hey_vista_del_rey.questphase / h6436 / 118` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_02\\scenes\\sts_hey_rey_02_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 118:Out → 1:In; 41:Out → 118:In |
| `open_world_bugfixing.questphase / h1127 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_finished"}}}` | 0:Out → 24:In; 24:True → 25:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_02_finished"}}}` | 0:Out → 24:In; 24:True → 25:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_hey_rey_02_gameplay.questphase / h233 / 8; sts_hey_rey_02_gameplay.questphase / h481 / 26; sts_hey_rey_02_open_world.questphase / h587 / 84; sts_hey_rey_02_open_world.questphase / h587 / 97 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_hey_rey_02_open_world.questphase / h281 / 50; sts_hey_rey_02_open_world.questphase / h587 / 87 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_hey_rey_02_gangers.scene / scene / 30 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | sts_hey_rey_02_gameplay.questphase / h341 / 8 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_hey_rey_02_gameplay.questphase / h341 / 24; sts_hey_rey_02_open_world.questphase / h12 / 70; sts_hey_rey_02_open_world.questphase / h281 / 58 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1127 / 24; open_world_bugfixing.questphase / h2262 / 24; sts_hey_rey_02_gameplay.questphase / h28 / 44; sts_hey_rey_02_holocall_debriefs.scene / scene / 249; +12 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_hey_rey_02_open_world.questphase / h281 / 48; sts_hey_rey_02_open_world.questphase / h281 / 52; sts_hey_rey_02_open_world.questphase / h281 / 76; sts_hey_rey_02_open_world.questphase / h587 / 81; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_hey_rey_02_open_world.questphase / h12 / 59; sts_hey_rey_02_open_world.questphase / h12 / 60; sts_hey_rey_02_open_world.questphase / h281 / 59; sts_hey_rey_02_open_world.questphase / h281 / 60; +5 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_hey_rey_02_gangers.scene / scene / 114; sts_hey_rey_02_gangers.scene / scene / 115; sts_hey_rey_02_gangers.scene / scene / 116; sts_hey_rey_02_open_world.questphase / h12 / 40; +27 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_hey_rey_02_civilians.scene / scene / 54; sts_hey_rey_02_gameplay.questphase / h12 / 14; sts_hey_rey_02_gameplay.questphase / h143 / 5; sts_hey_rey_02_gameplay.questphase / h143 / 7; +7 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_hey_rey_02_gameplay.questphase / h28 / 42; sts_hey_rey_02_gameplay.questphase / h28 / 43; sts_hey_rey_02_gameplay.questphase / h62 / 7; sts_hey_rey_02_open_world.questphase / h281 / 74 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1127 / 25; open_world_bugfixing.questphase / h2262 / 25; sts_hey_rey_02_open_world.questphase / h12 / 54; sts_hey_rey_02_open_world.questphase / h281 / 86; +25 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | sts_hey_rey_02_open_world.questphase / h587 / 85 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `parallel_join` | sts_hey_rey_02_gameplay.questphase / h341 / 31; sts_hey_rey_02_gameplay.questphase / h341 / 9; sts_hey_rey_02_open_world.questphase / h12 / 52 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_hey_rey_02_gameplay.questphase / h12 / 18; sts_hey_rey_02_gangers.scene / scene / 126; sts_hey_rey_02_holocall_debriefs.scene / scene / 284; sts_hey_rey_02_holocall_debriefs.scene / scene / 290; +24 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_hey_rey_02_gameplay.questphase / h143 / 6; sts_hey_rey_02_open_world.questphase / h587 / 57; sts_hey_vista_del_rey.questphase / h6436 / 57 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_hey_rey_02_civilians.scene / scene / 81; sts_hey_rey_02_gameplay.questphase / h277 / 28; sts_hey_rey_02_holocall_debriefs.scene / scene / 251; sts_hey_rey_02_holocall_debriefs.scene / scene / 265; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_hey_rey_02_open_world.questphase / h281 / 25 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_hey_rey_02_gameplay.questphase / h277 / 22; sts_hey_rey_02_gameplay.questphase / h277 / 24; sts_hey_rey_02_open_world.questphase / h214 / 11; sts_hey_rey_02_open_world.questphase / h214 / 8; +3 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_hey_rey_02_gameplay.questphase / h143 / 10; sts_hey_rey_02_gameplay.questphase / h143 / 4; sts_hey_rey_02_gameplay.questphase / h277 / 26; sts_hey_rey_02_gameplay.questphase / h277 / 27; +18 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_hey_rey_02_gameplay.questphase / h341 / 26; sts_hey_rey_02_gameplay.questphase / h341 / 32; sts_hey_rey_02_gameplay.questphase / h341 / 36; sts_hey_rey_02_gameplay.questphase / h341 / 37; +3 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sts_hey_rey_02_gameplay.questphase / h341 / 40; sts_hey_rey_02_open_world.questphase / h587 / 99; sts_hey_vista_del_rey.questphase / h5686 / 40 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weighted_branch` | sts_hey_rey_02_gameplay.questphase / h341 / 33 | ordered output weights + explicit route bindings → one authored weighted output. Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates. |
| `workspot_performance` | sts_hey_rey_02_gameplay.questphase / h341 / 28; sts_hey_rey_02_gameplay.questphase / h341 / 29; sts_hey_rey_02_gangers.scene / scene / 174; sts_hey_rey_02_gangers.scene / scene / 176; +1 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_hey_rey_02_open_world.questphase / h12 / 57; sts_hey_rey_02_open_world.questphase / h281 / 56 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` | content candidate; journal anchor | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` | content candidate; journal anchor | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` | content candidate; forward dependency | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene` | content candidate; journal anchor | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-hey-rey-02` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-cct-dtn-03.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

216 repeated typed/socket path signatures in this selected graph context; 40 distinct direct resource identities; 19 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 62 -> 293 -> 295 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 61 -> 63 -> 58 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 293 -> 295 -> 297 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 57 -> 60 -> 33 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 33 -> 61 -> 63 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` / scene / 13 -> 23 -> 41 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 290 -> 62 -> 293 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `6497920d6ce0ac894daa` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h281 / 51 -> 87 -> 90 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 1 -> 290 -> 62 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h587 / 8 -> 10 -> 93 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 249 -> 254 -> 251 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` / scene / 285 -> 283 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h12 / 9 | `h28` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 8 | `h45` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 20 | `h62` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 24 | `h86` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 30 | `h112` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 37 | `h126` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 39 | `h143` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":2,"socketName":"Out2"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 40 | `h216` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 41 | `h233` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h12 / 12 | `h277` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h0 / 4 | `h341` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h0 / 5 | `h481` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h0 / 3 | `h207` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h207 / 8 | `h214` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h0 / 4 | `h281` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h0 / 5 | `h587` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h587 / 36 | `h684` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

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
| `base\open_world\community\global_phase\open_world_global_community.gamedef` | content candidate | base\open_world\community\global_phase\open_world_global_community_quest.quest |
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
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\sts_cct_dtn_03_nc_def.gamedef` | content candidate | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\sts_cct_dtn_03_quest.quest |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\sts_cct_dtn_03_test_def.gamedef` | content candidate | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\sts_cct_dtn_03_quest.quest |
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
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_bar_lean0__2h_on_bar_wide__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__stand_bar_lean0__2h_on_bar_wide__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_civilians\civ_low_m_09_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_civilians\civ_low_m_107_bra_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_civilians\civ_low_m_113_car_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_civilians\civ_low_m_34_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\civ_prst_m_01_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\civ_prst_m_02_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\gang_val_m_04_mex_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\gang_val_m_10_mex_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\gang_val_m_15_mex_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_gangers\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_holocall_debriefs\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_holocall_prebrief\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\lipsync\en\sts_hey_rey_02_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\bar\bar\generic__stand_bar__work__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_valentinos` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 45; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h294 / 69; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6919 / 161; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h10479 / 71; 12 total source locations in compressed evidence |
| `hey_achievement` | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase / h0 / 42; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase / h0 / 34; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase / h89 / 8; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase / h0 / 40; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_padre_calls_v_end_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 54; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 148; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 145; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 146; 77 total source locations in compressed evidence |
| `holo_padre_calls_v_end_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 144; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 213; base\quest\holocalls\padre\padre_holocall.scene / scene / 42; base\quest\holocalls\padre\padre_holocall.scene / scene / 541; 24 total source locations in compressed evidence |
| `holo_padre_calls_v_rejectable` | base\quest\holocalls\padre\padre_holocall.scene / scene / 664; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 283; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 269; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 308; 30 total source locations in compressed evidence |
| `holo_padre_calls_v_rejected` | base\quest\holocalls\padre\padre_holocall.scene / scene / 672; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 287; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 273; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene / scene / 289; 20 total source locations in compressed evidence |
| `holo_padre_calls_v_start_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 53; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 147; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 141; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 143; 93 total source locations in compressed evidence |
| `holo_padre_calls_v_start_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 142; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 212; base\quest\holocalls\padre\padre_holocall.scene / scene / 41; base\quest\holocalls\padre\padre_holocall.scene / scene / 527; 24 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `rey_02_finished` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6130 / 51; 1 total source locations in compressed evidence |
| `rey_02_gang_chase` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6130 / 90; 1 total source locations in compressed evidence |
| `rey_02_gang_retaliation` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h5357 / 18; 1 total source locations in compressed evidence |
| `rey_02_journal_test` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest / h0 / 3; 1 total source locations in compressed evidence |
| `rey_02_start` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6436 / 59; 1 total source locations in compressed evidence |
| `rey_08_finished` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h11872 / 5; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08_openworld.questphase / h1395 / 5; 2 total source locations in compressed evidence |
| `sts_valentinos_retaliation` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h932 / 65; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6130 / 88; base\open_world\street_stories\street_stories_gang_retaliation.questphase / h1431 / 23; base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase / h520 / 65; 4 total source locations in compressed evidence |

NodeRef uses: 206; TweakDB binding uses: 12. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` | 4 / 6 | scnDialogLineEvent: 4; scnLookAtEvent: 2 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene` | 5 / 34 | scnChangeIdleAnimEvent: 3; scnDialogLineEvent: 10; scnLookAtEvent: 5; scnPlaySkAnimEvent: 11; scneventsSocket: 3; scneventsVFXEvent: 2 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
