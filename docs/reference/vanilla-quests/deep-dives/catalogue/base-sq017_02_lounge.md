# Off the Leash

Journal: `quests/side_quest/sq017_02_lounge` · `SideQuest` · hash `3513022215`.

**Coverage: journal-linked.** 28 exact journal-linked nodes in 5 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Talk to the bouncer. (Primary) | `quests/side_quest/sq017_02_lounge/pachinko/countersign` |
| Go to the given address. (Primary) | `quests/side_quest/sq017_02_lounge/pachinko/go_pachinko` |
| Look for Kerry. (Primary) | `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry` |
| Answer the phone. (Primary) | `quests/side_quest/sq017_02_lounge/pachinko/phone_call` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq017_02_lounge/party/enjoy` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq017_02_lounge/party/find_kerry` |
| Follow Kerry. (Primary) | `quests/side_quest/sq017_02_lounge/party/follow_kerry` |
| Wait for Kerry. (Primary) | `quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sq017_quest_bugfixes.questphase / h37 / 8` (Condition) | `quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available` | 24:False → 8:In; 8:True → 26:In; 8:False → 10:In |
| `sq017_quest_bugfixes.questphase / h37 / 10` (Condition) | `quests/side_quest/sq017_02_lounge/party/find_kerry` | 8:False → 10:In; 10:True → 26:In; 10:False → 12:In |
| `sq017_quest_bugfixes.questphase / h37 / 12` (Condition) | `quests/side_quest/sq017_02_lounge/party/follow_kerry` | 10:False → 12:In; 12:True → 18:In; 12:False → 15:In |
| `sq017_quest_bugfixes.questphase / h37 / 15` (Condition) | `quests/side_quest/sq017_02_lounge/party/enjoy` | 12:False → 15:In; 15:True → 22:In; 15:False → 27:In |
| `sq017_quest_bugfixes.questphase / h37 / 19` (PauseCondition) | `quests/side_quest/sq017_02_lounge/party/enjoy` | 17:Out → 19:In; 19:Out → 20:In |
| `sq017_quest_bugfixes.questphase / h37 / 24` (Condition) | `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry` | 2:Out → 24:In; 24:False → 8:In; 24:True → 26:In |
| `sq017_quest_bugfixes.questphase / h37 / 27` (Condition) | `quests/side_quest/sq017_02_lounge/party/enjoy` | 27:False → 1:In; 15:False → 27:In; 27:True → 35:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 12` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/go_pachinko` | 35:Out → 12:Active; 12:Out → 40:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 13` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/go_pachinko` | 18:Out → 13:Succeeded; 13:Out → 14:Active |
| `sq017_03a_premiere_pachinko.questphase / h0 / 14` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/countersign` | 14:Out → 10:Start 0; 13:Out → 14:Active |
| `sq017_03a_premiere_pachinko.questphase / h0 / 15` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/countersign` | 10:End 0 → 15:Succeeded; 15:Out → 36:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 44` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/phone_call` | 50:Out → 44:Active; 44:Out → 47:Active |
| `sq017_03a_premiere_pachinko.questphase / h0 / 47` (Journal) | `quests/side_quest/sq017_02_lounge/description` | 47:Out → 4:Start 0; 44:Out → 47:Active |
| `sq017_03b_premiere_concert.questphase / h0 / 38` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry` | 38:Out → 6:In; 8:Out → 38:Active; 68:Out → 38:Active; 38:Out → 58:In |
| `sq017_16_phone_call_3.scene / scene / 86` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/phone_call` | 86:0:0 → 2:0:0; 130:0:0 → 86:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_16_phone_call_3.scene / scene / 272` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/phone_call` | 261:0:0 → 272:0:2; 272:0:0 → 265:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 41` (Journal) | `quests/side_quest/sq017_02_lounge/party/find_kerry` | 41:0:0 → 62:0:1; 42:0:0 → 41:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 42` (Journal) | `quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available` | 19:0:0 → 42:0:3; 42:0:0 → 41:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 49` (Journal) | `quests/side_quest/sq017_02_lounge/party/find_kerry` | 49:0:0 → 50:0:1; 103:0:0 → 49:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 50` (Journal) | `quests/side_quest/sq017_02_lounge/party/follow_kerry` | 49:0:0 → 50:0:1; 50:0:0 → 1642:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 210` (Journal) | `quests/side_quest/sq017_02_lounge/party/follow_kerry` | 202:0:0 → 210:0:3; 210:0:0 → 211:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 211` (Journal) | `quests/side_quest/sq017_02_lounge/party/enjoy` | 210:0:0 → 211:0:1; 211:0:0 → 238:0:1; 2406:0:0 → 211:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 277` (Journal) | `quests/side_quest/sq017_02_lounge/party/follow_kerry` | 280:0:0 → 277:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 280` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry` | 280:0:0 → 277:0:1; 298:0:0 → 280:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 563` (Journal) | `quests/side_quest/sq017_02_lounge/pachinko/meet_kerry` | 1:0:0 → 563:0:3; 563:0:0 → 564:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 564` (Journal) | `quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available` | 563:0:0 → 564:0:1; 564:0:0 → 155:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 4051` (Journal) | `quests/side_quest/sq017_02_lounge` | 4051:0:0 → 1385:0:1; 4052:0:0 → 4051:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq017_18_premiere.scene / scene / 4052` (Journal) | `quests/side_quest/sq017_02_lounge/party/enjoy` | 3800:0:0 → 4052:0:3; 4052:0:0 → 4051:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sq017_03a_premiere_pachinko.questphase / h0 / 4` | `base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene`; `#sq017_16_sm_phone_call_3` | 47:Out → 4:Start 0; 4:End 0 → 35:In; 4:rejected_out → 53:In; 4:Holocall INT → 49:In; 4:Holocall RET → 48:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 10` | `base\quest\side_quests\sq017\scenes\sq017_17_pachinko.scene`; `#sq017_17_sm_pachinko` | 14:Out → 10:Start 0; 10:End 0 → 15:Succeeded |
| `sq017_03b_premiere_concert.questphase / h0 / 7` | `base\quest\side_quests\sq017\scenes\sq017_18_premiere.scene`; `#sq017_18_sm_premiere` | 69:False → 7:Start 0; 61:Out → 7:in_rooftop; 69:True → 7:no_us_cracks_in; 7:End 0 → 86:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\side_quests\sq017\sq017.questphase` / h591 / 2 | `sq017_03a_premiere_pachinko.questphase` | 0: Input; 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `base\quest\side_quests\sq017\sq017.questphase` / h591 / 3 | `sq017_03b_premiere_concert.questphase` | 2: Phase: sq017_03a_premiere_pachinko.questphase; 6: Input; 7: Input; 3:Out1 → 1:In; 2:Out1 → 3:In1; 6:Out → 3:In1; 7:Out → 3:In_rooftop |
| `base\quest\side_quests\sq017\phases\sq017_03a_premiere_pachinko.questphase` / h0 / 4 | `sq017_16_phone_call_3.scene` | 47: Journal; 47:Out → 4:Start 0; 4:End 0 → 35:In; 4:rejected_out → 53:In; 4:Holocall INT → 49:In; 4:Holocall RET → 48:In |
| `base\quest\side_quests\sq017\phases\sq017_03a_premiere_pachinko.questphase` / h0 / 10 | `sq017_17_pachinko.scene` | 14: Journal; 14:Out → 10:Start 0; 10:End 0 → 15:Succeeded |
| `base\quest\side_quests\sq017\phases\sq017_03b_premiere_concert.questphase` / h0 / 7 | `sq017_18_premiere.scene` | 69: Condition: sq017_us_cracks_no_deal GreaterOrEqual 1; 61: Input; 69: Condition: sq017_us_cracks_no_deal GreaterOrEqual 1; 69:False → 7:Start 0; 61:Out → 7:in_rooftop; 69:True → 7:no_us_cracks_in; 7:End 0 → 86:In |
| `base\quest\side_quests\sidequests.questphase` / h0 / 40 | `sq017.questphase` | 115: PauseCondition; 40:End → 175:In; 115:Out → 40:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 5 | `sidequests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:sq026_02_signal → 5:sq026_02_signal; 7:Out1 → 5:In1; 8:Out → 5:In1; 21:Out → 5:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sq017_16_phone_call_3.scene` | Start 0 → End 0, rejected_out | kerry; v; 19 nodes / 19 edges |
| `sq017_17_pachinko.scene` | Start 0 → End 0 | doorman; v; 26 nodes / 26 edges |
| `sq017_18_premiere.scene` | Start 0, Elevator, Start 8, Start1, in_rooftop, no_us_cracks_in, Speech, kiss → End 0 | kerry; purple_force; blue_moon; red_menace; media1; media2; spector_vendor; vip1; vip2; photo1; photo2; photo3; johnny; mrsblocker; mrblocker; v; 496 nodes / 644 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sq017_17_pachinko.scene / n5 / 0` | Got a meet with Kerry. (`password`) | No option-level predicate stored | 0:0 → 7:0:0 |
| `sq017_17_pachinko.scene / n5 / 1` | So why're you here? (`sam nie działasz`) | No option-level predicate stored | 0:1 → 115:0:1 |
| `sq017_18_premiere.scene / n204 / 0` | [Kiss Kerry] Yes. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "censorship_homosexuality", "comparisonType": "Equal"}}} | 0:0 → 462:0:0 |
| `sq017_18_premiere.scene / n204 / 1` | [Kiss Kerry] Shadows'll fade before you. (``) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "kerry_romanceable", "value": 1, "comparisonType": "GreaterOrEqual"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "censorship_homosexuality", "comparisonType": "Equal"}}]}} | 0:1 → 465:0:0 |
| `sq017_18_premiere.scene / n204 / 2` | You'll be fine. Even without me. (``) | No option-level predicate stored | 0:2 → 468:0:0 |
| `sq017_18_premiere.scene / n283 / 0` | [Sit] (``) | No option-level predicate stored | 0:0 → 524:0:0 |
| `sq017_18_premiere.scene / n295 / 0` | [Stand] Later, Spector. (``) | No option-level predicate stored | 0:0 → 298:0:0 |
| `sq017_18_premiere.scene / n316 / 0` | Show me what you got. (``) | No option-level predicate stored | 0:0 → 58:0:0 |
| `sq017_18_premiere.scene / n316 / 1` | OK, we'll talk later. (``) | No option-level predicate stored | 0:1 → 503:0:0 |
| `sq017_18_premiere.scene / n364 / 0` | It's a wild and crazy ride, but I can't complain. (``) | No option-level predicate stored | 0:0 → 366:0:0 |
| `sq017_18_premiere.scene / n364 / 1` | He'd be in jail right now if it wasn't for me. (``) | No option-level predicate stored | 0:1 → 368:0:0 |
| `sq017_18_premiere.scene / n364 / 2` | It's... simply legendary. That's all I got to say. (``) | No option-level predicate stored | 0:2 → 375:0:0 |
| `sq017_18_premiere.scene / n364 / 3` | No comment. (``) | No option-level predicate stored | 0:3 → 370:0:0 |
| `sq017_18_premiere.scene / n378 / 0` | "Love at first sight?" (``) | No option-level predicate stored | 0:0 → 56:0:0 |
| `sq017_18_premiere.scene / n378 / 1` | You look great. (``) | No option-level predicate stored | 0:1 → 381:0:0 |
| `sq017_18_premiere.scene / n378 / 2` | Great tune. (``) | No option-level predicate stored | 0:2 → 383:0:0 |
| `sq017_18_premiere.scene / n378 / 3` | Mighta brought Kerry around, but I remain skeptical. (``) | No option-level predicate stored | 0:3 → 385:0:0 |
| `sq017_18_premiere.scene / n400 / 0` | Maybe it's time you stopped being afraid. (``) | No option-level predicate stored | 0:0 → 404:0:0 |
| `sq017_18_premiere.scene / n400 / 1` | You're at the top. Don't need to prove anything, to anyone. (``) | No option-level predicate stored | 0:1 → 455:0:0 |
| `sq017_18_premiere.scene / n407 / 0` | [Lean] Amazing view. (``) | No option-level predicate stored | 0:0 → 411:0:0 |
| `sq017_18_premiere.scene / n407 / 1` | [Lean] Something's bugging you. (``) | No option-level predicate stored | 0:1 → 413:0:0 |
| `sq017_18_premiere.scene / n407 / 2` | [Lean] Glad we got a moment to ourselves. (``) | No option-level predicate stored | 0:2 → 415:0:0 |
| `sq017_18_premiere.scene / n417 / 0` | Think I get it. (``) | No option-level predicate stored | 0:0 → 434:0:0 |
| `sq017_18_premiere.scene / n417 / 1` | What do you mean? (``) | No option-level predicate stored | 0:1 → 421:0:0 |
| `sq017_18_premiere.scene / n430 / 0` | You can tell me. (``) | No option-level predicate stored | 0:0 → 396:0:0 |
| `sq017_18_premiere.scene / n430 / 1` | Little too heavy for me right now. (``) | No option-level predicate stored | 0:1 → 553:0:0 |
| `sq017_18_premiere.scene / n439 / 0` | But you did make it. (``) | No option-level predicate stored | 0:0 → 444:0:0 |
| `sq017_18_premiere.scene / n439 / 1` | Johnny thought you just chickened out. (``) | No option-level predicate stored | 0:1 → 446:0:0 |
| `sq017_18_premiere.scene / n458 / 0` | [Kiss] Hold you to that. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "censorship_homosexuality", "comparisonType": "Equal"}}} | 0:0 → 471:0:0 |
| `sq017_18_premiere.scene / n458 / 1` | Should probably get back. (``) | No option-level predicate stored | 0:1 → 206:0:0 |
| `sq017_18_premiere.scene / n521 / 0` | Show me what you got. (``) | No option-level predicate stored | 0:0 → 519:0:0 |
| `sq017_18_premiere.scene / n521 / 1` | OK, we'll talk later. (``) | No option-level predicate stored | 0:1 → 526:0:0 |
| `sq017_18_premiere.scene / n555 / 0` | Whatever happens, you'll be fine. (``) | No option-level predicate stored | 0:0 → 558:0:0 |
| `sq017_18_premiere.scene / n555 / 1` | Should probably be getting back. (``) | No option-level predicate stored | 0:1 → 1445:0:0 |
| `sq017_18_premiere.scene / n2177 / 0` | Text join unresolved (``) | No option-level predicate stored | 0:0 → 2173:0:0 |
| `sq017_18_premiere.scene / n2190 / 0` | [Step away] OK. See ya. (``) | No option-level predicate stored | 0:0 → 2191:0:0; 0:0 → 2995:0:1 |
| `sq017_18_premiere.scene / n2254 / 0` | [Step away] Guess I'll see ya. (``) | No option-level predicate stored | 0:0 → 2251:0:0; 0:0 → 2995:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CYB-12345` | sq017_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-586066` | sq017_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `CYB-586429` | sq017_quest_bugfixes.questphase / h235 / 2 | No reader in selected context |
| `CYB-604026` | sq017_quest_bugfixes.questphase / h275 / 2 | No reader in selected context |
| `CYB-624025` | sq017_quest_bugfixes.questphase / h316 / 2 | No reader in selected context |
| `CYB-626638` | sq017_quest_bugfixes.questphase / h377 / 2 | No reader in selected context |
| `CYB-626859` | sq017_quest_bugfixes.questphase / h630 / 2 | No reader in selected context |
| `CYB-628108` | sq017_quest_bugfixes.questphase / h486 / 2 | No reader in selected context |
| `CYB-638485` | sq017_quest_bugfixes.questphase / h540 / 2 | No reader in selected context |
| `CYB-644298` | sq017_quest_bugfixes.questphase / h669 / 2 | No reader in selected context |
| `CYB-646031` | sq017_quest_bugfixes.questphase / h745 / 2 | No reader in selected context |
| `CYB-655330` | sq017_quest_bugfixes.questphase / h807 / 2 | No reader in selected context |
| `censorship_homosexuality` | Producer outside selected context | sq017_18_premiere.scene / scene / 204; sq017_18_premiere.scene / scene / 458 |
| `holo_kerry_calls_v_end_activate` | sq017_03a_premiere_pachinko.questphase / h0 / 49; sq017_16_phone_call_3.scene / scene / 134 | No reader in selected context |
| `holo_kerry_calls_v_end_done` | sq017_16_phone_call_3.scene / scene / 130 | sq017_16_phone_call_3.scene / scene / 129 |
| `holo_kerry_calls_v_rejectable` | sq017_16_phone_call_3.scene / scene / 259 | No reader in selected context |
| `holo_kerry_calls_v_rejected` | sq017_16_phone_call_3.scene / scene / 261 | sq017_16_phone_call_3.scene / scene / 263 |
| `holo_kerry_calls_v_start_activate` | sq017_03a_premiere_pachinko.questphase / h0 / 48; sq017_16_phone_call_3.scene / scene / 133 | No reader in selected context |
| `holo_kerry_calls_v_start_done` | sq017_16_phone_call_3.scene / scene / 128 | sq017_16_phone_call_3.scene / scene / 127 |
| `kerry_default_on` | sq017_03a_premiere_pachinko.questphase / h0 / 37 | No reader in selected context |
| `kerry_romanceable` | Producer outside selected context | sq017_18_premiere.scene / scene / 204; sq017_18_premiere.scene / scene / 474 |
| `mq019_03_active` | Producer outside selected context | sq017_quest_bugfixes.questphase / h377 / 43 |
| `sq017_breathtaking` | sq017_18_premiere.scene / scene / 3817; sq017_18_premiere.scene / scene / 3819 | sq017_18_premiere.scene / scene / 62 |
| `sq017_floor_dof_lock` | sq017_18_premiere.scene / scene / 3873 | sq017_18_premiere.scene / scene / 3864; sq017_18_premiere.scene / scene / 3866 |
| `sq017_janusz_look` | sq017_18_premiere.scene / scene / 2932; sq017_18_premiere.scene / scene / 2934 | sq017_18_premiere.scene / scene / 2937 |
| `sq017_kerry_kiss` | sq017_18_premiere.scene / scene / 208 | No reader in selected context |
| `sq017_kerrys_dialog_3` | sq017_18_premiere.scene / scene / 3956; sq017_18_premiere.scene / scene / 3961 | sq017_18_premiere.scene / scene / 1112; sq017_18_premiere.scene / scene / 1241 |
| `sq017_met_kerry_outside_riot` | Producer outside selected context | sq017_quest_bugfixes.questphase / h275 / 42 |
| `sq017_mq028_start` | Producer outside selected context | sq017_quest_bugfixes.questphase / h37 / 28; sq017_quest_bugfixes.questphase / h37 / 37 |
| `sq017_pachinko_kerry_active` | sq017_03a_premiere_pachinko.questphase / h0 / 40 | No reader in selected context |
| `sq017_riot_sequence_active` | Producer outside selected context | sq017_quest_bugfixes.questphase / h235 / 24; sq017_quest_bugfixes.questphase / h275 / 24; sq017_quest_bugfixes.questphase / h377 / 24; sq017_quest_bugfixes.questphase / h807 / 8 |
| `sq017_roof_dof_lock` | sq017_18_premiere.scene / scene / 2995; sq017_18_premiere.scene / scene / 3875; sq017_18_premiere.scene / scene / 3877 | sq017_18_premiere.scene / scene / 2742; sq017_18_premiere.scene / scene / 2744 |
| `sq017_us_cracks_no_deal` | Producer outside selected context | sq017_03a_premiere_pachinko.questphase / h0 / 53; sq017_03b_premiere_concert.questphase / h0 / 65; sq017_03b_premiere_concert.questphase / h0 / 69; sq017_03b_premiere_concert.questphase / h0 / 96; sq017_16_phone_call_3.scene / scene / 53; sq017_quest_bugfixes.questphase / h37 / 35; sq017_quest_bugfixes.questphase / h630 / 8 |
| `sq17_caliente` | sq017_quest_bugfixes.questphase / h486 / 43; sq017_quest_bugfixes.questphase / h486 / 44 | sq017_18_premiere.scene / scene / 424 |
| `travelling_merchant_lives` | Producer outside selected context | sq017_quest_bugfixes.questphase / h0 / 42 |
| `wbr_jpn_melee_01_default_on` | sq017_03b_premiere_concert.questphase / h0 / 75; sq017_03b_premiere_concert.questphase / h0 / 76 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>116 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sq017_quest_bugfixes.questphase / h0 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 43:Out → 42:In |
| `sq017_quest_bugfixes.questphase / h37 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/wait_until_kerry_is_available","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 24:False → 8:In; 8:True → 26:In; 8:False → 10:In |
| `sq017_quest_bugfixes.questphase / h37 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/find_kerry","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 8:False → 10:In; 10:True → 26:In; 10:False → 12:In |
| `sq017_quest_bugfixes.questphase / h37 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/follow_kerry","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:False → 12:In; 12:True → 18:In; 12:False → 15:In |
| `sq017_quest_bugfixes.questphase / h37 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/enjoy","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 12:False → 15:In; 15:True → 22:In; 15:False → 27:In |
| `sq017_quest_bugfixes.questphase / h37 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#loc_sq017_pachinko_lounge_int_area02"}}` | 12:True → 18:In; 26:Out → 18:In; 18:Out → 22:In |
| `sq017_quest_bugfixes.questphase / h37 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/enjoy","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 17:Out → 19:In; 19:Out → 20:In |
| `sq017_quest_bugfixes.questphase / h37 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/pachinko/meet_kerry","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 24:In; 24:False → 8:In; 24:True → 26:In |
| `sq017_quest_bugfixes.questphase / h37 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_02_lounge/party/enjoy","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 27:False → 1:In; 15:False → 27:In; 27:True → 35:In |
| `sq017_quest_bugfixes.questphase / h37 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_mq028_start","comparisonType":"LessOrEqual"}}}` | 35:False → 28:In; 28:True → 33:In; 28:False → 38:In |
| `sq017_quest_bugfixes.questphase / h37 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_inside_crowd_aft_premiere"}}` | 28:True → 33:In; 33:False → 29:In; 33:True → 32:In |
| `sq017_quest_bugfixes.questphase / h37 / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 27:True → 35:In; 35:False → 28:In; 35:True → 37:In |
| `sq017_quest_bugfixes.questphase / h37 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_mq028_start","comparisonType":"LessOrEqual"}}}` | 37:True → 1:In; 35:True → 37:In; 37:False → 36:In |
| `sq017_quest_bugfixes.questphase / h235 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_riot_sequence_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 24:False → 1:In; 2:Out → 24:In; 24:True → 40:In |
| `sq017_quest_bugfixes.questphase / h275 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_riot_sequence_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 24:False → 1:In; 2:Out → 24:In; 24:True → 42:In |
| `sq017_quest_bugfixes.questphase / h275 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_met_kerry_outside_riot","value":1,"comparisonType":"GreaterOrEqual"}}}` | 42:True → 1:In; 24:True → 42:In; 42:False → 41:In |
| `sq017_quest_bugfixes.questphase / h316 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_01_riot_club/nightclub/go_backstage","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 24:False → 1:In; 2:Out → 24:In; 24:True → 42:In |
| `sq017_quest_bugfixes.questphase / h316 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_backstage_lift_0_floor","activatorRef":{"$type":"gameEntityReference","reference":"#kerry"},"isPlayerActivator":false}}` | 42:False → 1:In; 24:True → 42:In; 42:True → 49:In |
| `sq017_quest_bugfixes.questphase / h377 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_riot_sequence_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 24:True → 1:In; 2:Out → 24:In; 24:False → 43:In |
| `sq017_quest_bugfixes.questphase / h377 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq019_03_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 43:True → 1:In; 24:False → 43:In; 43:False → 45:In |
| `sq017_quest_bugfixes.questphase / h377 / 45` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wat_lch_nightclub_riot_int_area01"}}` | 43:False → 45:In; 45:True → 47:In; 45:False → 52:In |
| `sq017_quest_bugfixes.questphase / h377 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wat_lch_nightclub_riot_int_area01"}}` | 47:Out → 46:In; 46:Out → 48:In |
| `sq017_quest_bugfixes.questphase / h486 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/caliente/follow_kerry","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/caliente/follow_kerry","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 2:Out → 24:In; 24:True → 43:In; 24:False → 44:In |
| `sq017_quest_bugfixes.questphase / h540 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/intro/wait","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 8:In; 8:True → 10:In; 8:False → 9:In |
| `sq017_quest_bugfixes.questphase / h540 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/intro/get_into_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:False → 1:In; 8:False → 9:In; 9:True → 10:In |
| `sq017_quest_bugfixes.questphase / h540 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sq017_com_filipino_barista","names":["sq017_filipino_barista"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 8:True → 10:In; 9:True → 10:In; 10:True → 11:In; 10:False → 12:In |
| `sq017_quest_bugfixes.questphase / h540 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sq017_mp_wait"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 10:False → 12:In; 12:Out → 13:In |
| `sq017_quest_bugfixes.questphase / h540 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/intro/get_into_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 13:True → 1:In; 12:Out → 13:In; 13:False → 14:In |
| `sq017_quest_bugfixes.questphase / h630 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `sq017_quest_bugfixes.questphase / h669 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/highwaymen/set_spike_trap","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 2:Out → 8:In; 8:True → 10:In; 8:False → 12:In |
| `sq017_quest_bugfixes.questphase / h669 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 11:Out → 9:In; 10:Out → 11:In |
| `sq017_quest_bugfixes.questphase / h669 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_01_riot_club","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 8:False → 12:In; 9:Out → 12:In; 12:True → 14:In; 12:False → 13:In |
| `sq017_quest_bugfixes.questphase / h669 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_01_riot_club","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Failed"}}}` | 13:False → 1:In; 12:False → 13:In; 13:True → 14:In |
| `sq017_quest_bugfixes.questphase / h745 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `sq017_quest_bugfixes.questphase / h745 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq017_kerry/intro/get_into_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 9:True → 1:In; 8:True → 9:In; 9:False → 10:In |
| `sq017_quest_bugfixes.questphase / h807 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_riot_sequence_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_pachinko_back"}}` | 18:Out → 13:Succeeded; 40:Out → 18:In |
| `sq017_03a_premiere_pachinko.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 3:Out → 50:In; 50:Out → 44:Active |
| `sq017_03a_premiere_pachinko.questphase / h0 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 4:rejected_out → 53:In; 53:True → 51:Active; 53:False → 52:Active |
| `sq017_03b_premiere_concert.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_entrance"}}` | 38:Out → 6:In; 6:Out → 72:In; 6:Out → 77:In |
| `sq017_03b_premiere_concert.questphase / h0 / 65` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 75:Out → 65:In; 65:True → 90:In; 65:True → 67:In; 65:False → 70:In; 65:False → 84:In |
| `sq017_03b_premiere_concert.questphase / h0 / 69` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 69:False → 7:Start 0; 69:True → 7:no_us_cracks_in; 59:Out → 69:In |
| `sq017_03b_premiere_concert.questphase / h0 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sq017_tr_inside_pachinko_building"}}` | 59:Out → 78:In; 83:Out → 78:In; 78:Out → 79:In |
| `sq017_03b_premiere_concert.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_inside_pachinko_building"}}` | 82:Out → 80:In; 80:Out → 81:In |
| `sq017_03b_premiere_concert.questphase / h0 / 96` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 96:True → 76:In; 96:False → 95:In; 101:Out → 96:In |
| `sq017_16_phone_call_3.scene / scene / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_us_cracks_no_deal"}}}` | 53:0:0 → 56:0:0; 53:0:1 → 3:0:0; 131:0:0 → 53:0:1 |
| `sq017_16_phone_call_3.scene / scene / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_start_done"}}}` | 127:0:0 → 128:0:1; 133:0:0 → 127:0:1 |
| `sq017_16_phone_call_3.scene / scene / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_end_done"}}}` | 129:0:0 → 130:0:1; 134:0:0 → 129:0:1 |
| `sq017_16_phone_call_3.scene / scene / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_rejected"}}}` | 133:0:0 → 263:0:1; 263:0:0 → 261:0:1 |
| `sq017_17_pachinko.scene / scene / 115` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq017\\scenes\\sq017_17_pachinko.scene","Flags":"Soft"},"sectionName":"sq017_17_whythen","type":"IsOutside"}}}` | 5:0:1 → 115:0:1; 115:0:0 → 37:0:0 |
| `sq017_17_pachinko.scene / scene / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sq017_pachinko_lift_street_door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 34:0:0 → 132:0:1; 132:0:0 → 133:0:1 |
| `sq017_17_pachinko.scene / scene / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 132:0:0 → 133:0:1; 133:0:0 → 2:0:0 |
| `sq017_17_pachinko.scene / scene / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sq017_pachinko_lift_street","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsMoving"}}}` | 34:0:0 → 140:0:1; 140:0:0 → 139:0:1 |
| `sq017_18_premiere.scene / scene / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_breathtaking","comparisonType":"Equal"}},{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_interview"}]}}` | 41:0:0 → 62:0:1; 62:0:0 → 63:0:0 |
| `sq017_18_premiere.scene / scene / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":1.5},"comparisonType":"LessOrEqual"}}}` | 47:2:0 → 114:0:1; 114:0:0 → 362:0:0 |
| `sq017_18_premiere.scene / scene / 178` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sq017_pachinko_lift_lounge","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsAtFloor","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"floorNumber","value":{"$type":"Variant","$rawData":"9AAIAAAAAQAAAA=="}}]}}}` | 178:0:0 → 177:0:1; 178:0:0 → 1460:0:1; 178:0:0 → 7133:0:1; 1057:0:0 → 178:0:1 |
| `sq017_18_premiere.scene / scene / 266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_meeting_vendor"}}` | 266:0:0 → 268:0:0; 266:0:0 → 3805:0:1; 1091:0:0 → 266:0:1 |
| `sq017_18_premiere.scene / scene / 270` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 268:0:0 → 270:0:1; 270:0:0 → 284:0:0 |
| `sq017_18_premiere.scene / scene / 346` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_rooftop_view","activatorRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"isPlayerActivator":false}}` | 326:0:0 → 346:0:1; 346:0:0 → 1266:0:1 |
| `sq017_18_premiere.scene / scene / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 344:0:0 → 349:0:1; 349:0:0 → 202:0:0 |
| `sq017_18_premiere.scene / scene / 424` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq17_caliente","value":1,"comparisonType":"GreaterOrEqual"}}}` | 424:0:0 → 419:0:0; 424:0:0 → 2142:0:1; 424:0:1 → 427:0:0; 1462:0:0 → 424:0:1 |
| `sq017_18_premiere.scene / scene / 474` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kerry_romanceable","comparisonType":"Equal"}}}` | 462:2:0 → 474:0:1; 465:2:0 → 474:0:1; 471:2:0 → 474:0:1; 474:0:0 → 205:0:0; 474:0:0 → 1192:0:1; 474:0:1 → 212:0:0 |
| `sq017_18_premiere.scene / scene / 1112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_kerrys_dialog_3","value":1,"comparisonType":"Equal"}}}` | 176:0:0 → 1112:0:1; 1112:0:0 → 1160:0:0 |
| `sq017_18_premiere.scene / scene / 1192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq017_18_premiere_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":90.0,"inverted":true}}}` | 206:0:0 → 1192:0:1; 474:0:0 → 1192:0:1; 1192:0:0 → 2443:0:0 |
| `sq017_18_premiere.scene / scene / 1241` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_kerrys_dialog_3","comparisonType":"Equal"}}}` | 1241:0:0 → 1152:0:0; 1956:0:0 → 1241:0:1 |
| `sq017_18_premiere.scene / scene / 1247` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 574:0:0 → 1247:0:1; 1247:0:0 → 394:0:0 |
| `sq017_18_premiere.scene / scene / 1266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 346:0:0 → 1266:0:1; 1266:0:0 → 344:0:0 |
| `sq017_18_premiere.scene / scene / 1519` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":18}}}` | 1519:0:0 → 19:0:0; 1758:0:0 → 1519:0:1 |
| `sq017_18_premiere.scene / scene / 1614` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":10}}}` | 63:0:0 → 1614:0:1; 1614:0:0 → 47:0:0; 1614:0:0 → 3831:0:0 |
| `sq017_18_premiere.scene / scene / 1642` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_kerry_waits"}}` | 50:0:0 → 1642:0:1; 1642:0:0 → 599:0:0 |
| `sq017_18_premiere.scene / scene / 1758` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_entrance2"}}` | 1482:0:0 → 1758:0:1; 1758:0:0 → 1519:0:1; 1758:0:0 → 4065:0:1 |
| `sq017_18_premiere.scene / scene / 2047` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 362:2:0 → 2047:0:1; 2047:0:0 → 1837:0:0; 2055:1:0 → 2047:0:0 |
| `sq017_18_premiere.scene / scene / 2084` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 2084:0:0 → 326:0:0; 2092:0:0 → 2084:0:1 |
| `sq017_18_premiere.scene / scene / 2092` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_rooftop_view2","activatorRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"isPlayerActivator":false}}` | 1152:0:0 → 2092:0:1; 2092:0:0 → 2084:0:1 |
| `sq017_18_premiere.scene / scene / 2176` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"GreaterOrEqual"}}}` | 2176:0:0 → 2:0:0; 7139:0:0 → 2176:0:1 |
| `sq017_18_premiere.scene / scene / 2244` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 2244:0:0 → 2920:0:0; 2279:1:0 → 2244:0:0; 2916:0:0 → 2244:0:1 |
| `sq017_18_premiere.scene / scene / 2410` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 63:1:0 → 2410:0:0; 2410:0:0 → 2425:0:0; 2414:0:0 → 2410:0:1 |
| `sq017_18_premiere.scene / scene / 2419` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 63:1:0 → 2419:0:0; 2414:0:1 → 2419:0:1; 2419:0:0 → 2425:0:0 |
| `sq017_18_premiere.scene / scene / 2420` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 63:1:0 → 2420:0:0; 2414:0:2 → 2420:0:1; 2420:0:0 → 2425:0:0 |
| `sq017_18_premiere.scene / scene / 2719` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#sq017_pachinko_lift_lounge","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsMoving"}}}` | 1057:0:0 → 2719:0:1; 2719:0:0 → 2722:0:1 |
| `sq017_18_premiere.scene / scene / 2722` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2719:0:0 → 2722:0:1; 2722:0:0 → 2707:0:1 |
| `sq017_18_premiere.scene / scene / 2742` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_roof_dof_lock","comparisonType":"Equal"}}]}}` | 2742:0:0 → 2741:0:0; 2743:0:0 → 2742:0:1; 2745:0:0 → 2742:0:1 |
| `sq017_18_premiere.scene / scene / 2744` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612,"inverted":true}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_roof_dof_lock","comparisonType":"Equal"}}]}}` | 2741:0:0 → 2744:0:1; 2744:0:0 → 2745:0:0 |
| `sq017_18_premiere.scene / scene / 2751` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2751:0:0 → 2757:0:1; 2754:0:0 → 2751:0:1; 2778:1:0 → 2751:0:0 |
| `sq017_18_premiere.scene / scene / 2752` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 2752:0:0 → 2757:0:1; 2754:0:1 → 2752:0:1; 2778:1:0 → 2752:0:0 |
| `sq017_18_premiere.scene / scene / 2753` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 2753:0:0 → 2757:0:1; 2754:0:2 → 2753:0:1; 2778:1:0 → 2753:0:0 |
| `sq017_18_premiere.scene / scene / 2757` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2751:0:0 → 2757:0:1; 2752:0:0 → 2757:0:1; 2753:0:0 → 2757:0:1; 2757:0:0 → 2755:0:0; 2757:0:0 → 2756:0:0; 2778:1:0 → 2757:0:0 |
| `sq017_18_premiere.scene / scene / 2802` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2802:0:0 → 2808:0:1; 2805:0:0 → 2802:0:1; 2809:1:0 → 2802:0:0 |
| `sq017_18_premiere.scene / scene / 2803` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 2803:0:0 → 2808:0:1; 2805:0:1 → 2803:0:1; 2809:1:0 → 2803:0:0 |
| `sq017_18_premiere.scene / scene / 2804` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 2804:0:0 → 2808:0:1; 2805:0:2 → 2804:0:1; 2809:1:0 → 2804:0:0 |
| `sq017_18_premiere.scene / scene / 2808` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2802:0:0 → 2808:0:1; 2803:0:0 → 2808:0:1; 2804:0:0 → 2808:0:1; 2808:0:0 → 2806:0:0; 2808:0:0 → 2807:0:0; 2809:1:0 → 2808:0:0 |
| `sq017_18_premiere.scene / scene / 2825` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2825:0:0 → 2831:0:1; 2828:0:0 → 2825:0:1; 2832:1:0 → 2825:0:0 |
| `sq017_18_premiere.scene / scene / 2826` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 2826:0:0 → 2831:0:1; 2828:0:1 → 2826:0:1; 2832:1:0 → 2826:0:0 |
| `sq017_18_premiere.scene / scene / 2827` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 2827:0:0 → 2831:0:1; 2828:0:2 → 2827:0:1; 2832:1:0 → 2827:0:0 |
| `sq017_18_premiere.scene / scene / 2831` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2825:0:0 → 2831:0:1; 2826:0:0 → 2831:0:1; 2827:0:0 → 2831:0:1; 2831:0:0 → 2829:0:0; 2831:0:0 → 2830:0:0; 2832:1:0 → 2831:0:0 |
| `sq017_18_premiere.scene / scene / 2914` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 2279:1:0 → 2914:0:0; 2914:0:0 → 2920:0:0; 2916:0:1 → 2914:0:1 |
| `sq017_18_premiere.scene / scene / 2915` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 2279:1:0 → 2915:0:0; 2915:0:0 → 2920:0:0; 2916:0:2 → 2915:0:1 |
| `sq017_18_premiere.scene / scene / 2937` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_janusz_look","value":1,"comparisonType":"Equal"}}}` | 2920:0:0 → 2937:0:1; 2937:0:0 → 2942:0:0; 2939:0:0 → 2937:0:1 |
| `sq017_18_premiere.scene / scene / 2964` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 2105:1:0 → 2964:0:0; 2964:0:0 → 2968:0:0; 2967:0:0 → 2964:0:1 |
| `sq017_18_premiere.scene / scene / 2965` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 2105:1:0 → 2965:0:0; 2965:0:0 → 2968:0:0; 2967:0:1 → 2965:0:1 |
| `sq017_18_premiere.scene / scene / 2966` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":12}}}` | 2105:1:0 → 2966:0:0; 2966:0:0 → 2968:0:0; 2967:0:2 → 2966:0:1 |
| `sq017_18_premiere.scene / scene / 3743` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 3741:1:0 → 3743:0:0; 3743:0:0 → 3747:0:0; 3746:0:0 → 3743:0:1 |
| `sq017_18_premiere.scene / scene / 3744` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 3741:1:0 → 3744:0:0; 3744:0:0 → 3747:0:0; 3746:0:1 → 3744:0:1 |
| `sq017_18_premiere.scene / scene / 3745` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":12}}}` | 3741:1:0 → 3745:0:0; 3745:0:0 → 3747:0:0; 3746:0:2 → 3745:0:1 |
| `sq017_18_premiere.scene / scene / 3864` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq017_com_premiere_folks","names":["media_woman1"]},"timeInterval":0.10000000149011612}}]},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_floor_dof_lock","comparisonType":"Equal"}}]}}` | 3864:0:0 → 3865:0:0; 3867:0:0 → 3864:0:1 |
| `sq017_18_premiere.scene / scene / 3866` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq017_com_premiere_folks","names":["media_woman1"]},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}]},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_floor_dof_lock","comparisonType":"Equal"}}]}}` | 362:0:0 → 3866:0:1; 3865:0:0 → 3866:0:1; 3866:0:0 → 3867:0:0 |
| `sq017_18_premiere.scene / scene / 3884` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 568:0:0 → 3884:0:1; 3884:0:0 → 354:0:0 |
| `sq017_18_premiere.scene / scene / 3911` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_elevator"}}` | 3911:0:0 → 3951:0:1; 3911:0:1 → 523:0:0; 4010:0:0 → 3911:0:1 |
| `sq017_18_premiere.scene / scene / 3914` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_elevator"}}` | 3914:0:0 → 3951:0:1; 3914:0:1 → 356:0:0; 4013:0:0 → 3914:0:1 |
| `sq017_18_premiere.scene / scene / 3917` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 298:0:0 → 3917:0:1; 3917:0:0 → 522:0:0 |
| `sq017_18_premiere.scene / scene / 3951` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_elevator"}}` | 356:0:0 → 3951:0:1; 523:0:0 → 3951:0:1; 3911:0:0 → 3951:0:1; 3914:0:0 → 3951:0:1; 3951:0:0 → 3956:0:1 |
| `sq017_18_premiere.scene / scene / 4010` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":10}}}` | 522:0:0 → 4010:0:1; 4010:0:0 → 3911:0:1 |
| `sq017_18_premiere.scene / scene / 4013` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":10}}}` | 354:0:0 → 4013:0:1; 4013:0:0 → 3914:0:1 |
| `sq017_18_premiere.scene / scene / 4042` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"de"}},{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"es"}},{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"fr"}},{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"pl"}},{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"pt"}},{"$type":"questSystemCondition","type":{"$type":"questLanguage_ConditionType","mode":"VoLang","languageCode":"pl"}}]}}` | 61:2:0 → 4042:0:1; 4042:0:1 → 3817:0:1 |
| `sq017_18_premiere.scene / scene / 7126` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq017_tr_lounge_elevator"}}` | 1160:2:0 → 7126:0:1; 7126:0:0 → 7129:0:1 |
| `sq017_18_premiere.scene / scene / 7151` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 19:2:0 → 7151:0:1; 7151:0:0 → 7105:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_route` | sq017_18_premiere.scene / scene / 1659; sq017_18_premiere.scene / scene / 1799; sq017_18_premiere.scene / scene / 1805; sq017_18_premiere.scene / scene / 194; +3 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `choice_gate` | sq017_17_pachinko.scene / scene / 5; sq017_18_premiere.scene / scene / 204; sq017_18_premiere.scene / scene / 2177; sq017_18_premiere.scene / scene / 2190; +14 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sq017_03a_premiere_pachinko.questphase / h0 / 3; sq017_03b_premiere_concert.questphase / h0 / 100; sq017_03b_premiere_concert.questphase / h0 / 84; sq017_03b_premiere_concert.questphase / h0 / 87; +5 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sq017_03a_premiere_pachinko.questphase / h0 / 53; sq017_03b_premiere_concert.questphase / h0 / 65; sq017_03b_premiere_concert.questphase / h0 / 69; sq017_03b_premiere_concert.questphase / h0 / 96; +27 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sq017_03b_premiere_concert.questphase / h0 / 77; sq017_03b_premiere_concert.questphase / h0 / 79; sq017_03b_premiere_concert.questphase / h0 / 81; sq017_quest_bugfixes.questphase / h540 / 11; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_action` | sq017_03b_premiere_concert.questphase / h0 / 72; sq017_03b_premiere_concert.questphase / h0 / 85; sq017_03b_premiere_concert.questphase / h0 / 86; sq017_03b_premiere_concert.questphase / h0 / 98; +19 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sq017_17_pachinko.scene / scene / 132; sq017_17_pachinko.scene / scene / 140; sq017_18_premiere.scene / scene / 178; sq017_18_premiere.scene / scene / 2719 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `persistent_decision` | sq017_03a_premiere_pachinko.questphase / h0 / 37; sq017_03a_premiere_pachinko.questphase / h0 / 40; sq017_03a_premiere_pachinko.questphase / h0 / 48; sq017_03a_premiere_pachinko.questphase / h0 / 49; +33 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sq017_17_pachinko.scene / scene / 133; sq017_18_premiere.scene / scene / 1247; sq017_18_premiere.scene / scene / 1266; sq017_18_premiere.scene / scene / 1519; +35 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sq017_03b_premiere_concert.questphase / h0 / 63 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sq017_03a_premiere_pachinko.questphase / h0 / 10; sq017_03a_premiere_pachinko.questphase / h0 / 4; sq017_03b_premiere_concert.questphase / h0 / 7 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | sq017_quest_bugfixes.questphase / h275 / 41; sq017_quest_bugfixes.questphase / h745 / 10; sq017_quest_bugfixes.questphase / h807 / 10; sq017_quest_bugfixes.questphase / h807 / 9 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sq017_17_pachinko.scene / scene / 105; sq017_17_pachinko.scene / scene / 106; sq017_17_pachinko.scene / scene / 45; sq017_17_pachinko.scene / scene / 46; +162 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sq017_03b_premiere_concert.questphase / h0 / 70; sq017_03b_premiere_concert.questphase / h0 / 71; sq017_03b_premiere_concert.questphase / h0 / 90; sq017_03b_premiere_concert.questphase / h0 / 95; +9 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\sidequests\sq017\sq017_quest_bugfixes.questphase` | repair; journal anchor | `base-sq017` |
| `base\quest\side_quests\sq017\phases\sq017_03a_premiere_pachinko.questphase` | content candidate; journal anchor | `base-sq017` |
| `base\quest\side_quests\sq017\phases\sq017_03b_premiere_concert.questphase` | content candidate; journal anchor | `base-sq017` |
| `base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene` | content candidate; journal anchor | `base-sq017` |
| `base\quest\side_quests\sq017\scenes\sq017_17_pachinko.scene` | content candidate; forward dependency | `base-sq017` |
| `base\quest\side_quests\sq017\scenes\sq017_18_premiere.scene` | content candidate; journal anchor | `base-sq017` |

Evidence shards for this dossier (including parent context): [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/catalogue/evidence/base-sq017.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
