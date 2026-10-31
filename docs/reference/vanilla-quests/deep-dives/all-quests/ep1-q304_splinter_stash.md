# Voodoo Treasure

Journal: `ep1/quests/minor_quest/q304_splinter_stash` · `MinorQuest` · hash `1660496179`.

Journal premise: Well, well! That eavesdroppin' yielded more than just a satisfied curiosity. A little info for the FIA, a little bonus for V…\n\nBetter make for the Needle and pocket Slider's secret stash o' cash. He sure ain't gonna miss it.

**Coverage: journal-linked.** 4 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Find Slider's stash beneath the Needle and open it with the code 941229. (Primary) | `ep1/quests/minor_quest/q304_splinter_stash/01_stash/01_find_stash` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q304_slider_stash.questphase / h0 / 10` (Condition) | `ep1/quests/minor_quest/q304_splinter_stash` | 3:Out → 10:In; 10:True → 11:Succeeded; 10:False → 12:In2 |
| `q304_slider_stash.questphase / h0 / 11` (Journal) | `ep1/quests/minor_quest/q304_splinter_stash` | 10:True → 11:Succeeded; 11:Out → 12:In1 |
| `q304_slider_stash.questphase / h0 / 15` (Journal) | `ep1/quests/minor_quest/q304_splinter_stash/01_stash/01_find_stash` | 14:Out → 15:Active; 15:Out → 17:Active |
| `q304_slider_stash.questphase / h0 / 17` (Journal) | `ep1/quests/minor_quest/q304_splinter_stash/desc` | 15:Out → 17:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\quest\ep1_persistent_content.questphase` / h388 / 4 | `q304_slider_stash.questphase` | 19: LogicalHub; 19:Out3 → 4:In1 |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 2 | `ep1_persistent_content.questphase` | 0: Input; 15: Input; 0:Out → 2:In1; 15:Out → 2:growl |
| `ep1\openworld\ep1_open_world.quest` / h0 / 26 | `ep1_additional_game_elements.questphase` | 2: PauseCondition: {"seconds": 1}; 2:Out → 26:In1 |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 10 | `ep1_additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 10:In1 |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 16 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 16:In1 |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest` / h0 / 20 | `ep1_additional_game_elements.questphase` | 0: Start; 0:Out → 20:In1 |
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |
| `ep1\quest\main_quests\q301\q301.quest` / h0 / 13 | `ep1_additional_game_elements.questphase` | 4: CharacterManager; 4:Out → 13:In1 |
| `ep1\quest\main_quests\q302\q302.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\main_quests\q303\q303.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 5:In1 |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q306\q306.quest` / h354 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 2:In1; 10:CutSource → 2:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 2:In1 |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| No resolved scene dependency in this scope | This does not prove the quest has no dialogue | — |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `q304_05_slider_stash_info_downloaded` | Producer outside selected context | q304_slider_stash.questphase / h0 / 14 |

## Exact gates, joins and cancellation

<details><summary>6 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q304_slider_stash.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q304_dvc_slider_stash_door"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `q304_slider_stash.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q304_dvc_slider_stash_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 2:Out → 3:In; 3:Out → 10:In |
| `q304_slider_stash.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q304_slider_stash_loot"},"isPlayer":false}}}` | 6:Out → 1:In; 13:Out → 6:In |
| `q304_slider_stash.questphase / h0 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/q304_splinter_stash","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 3:Out → 10:In; 10:True → 11:Succeeded; 10:False → 12:In2 |
| `q304_slider_stash.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 5:Out → 13:In; 13:Out → 6:In |
| `q304_slider_stash.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q304_05_slider_stash_info_downloaded","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 14:In; 14:Out → 15:Active |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | q304_slider_stash.questphase / h0 / 14 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | q304_slider_stash.questphase / h0 / 20 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | q304_slider_stash.questphase / h0 / 18; q304_slider_stash.questphase / h0 / 21; q304_slider_stash.questphase / h0 / 4 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q304_slider_stash.questphase / h0 / 3 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | q304_slider_stash.questphase / h0 / 6 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | q304_slider_stash.questphase / h0 / 11; q304_slider_stash.questphase / h0 / 15; q304_slider_stash.questphase / h0 / 17 | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | q304_slider_stash.questphase / h0 / 22 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `realtime_delay` | q304_slider_stash.questphase / h0 / 13 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` | content candidate; journal anchor | `ep1-q304` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

9 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `660cfd1a96de4dcf75ec` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 0 -> 14 -> 15 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |
| `95c9f0f66f2831e4be4d` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 12 -> 4 -> 21 | questLogicalHubNodeDefinition -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out1 -> In; Out -> In |
| `f5fe843ab54d103f9baa` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 10 -> 11 -> 12 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questLogicalHubNodeDefinition; True -> Succeeded; Out -> In1 |
| `877ad108ad9e586098d9` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 14 -> 15 -> 17 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `8a40b6c45cd82e315141` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 12 -> 20 -> 18 | questLogicalHubNodeDefinition -> questEventManagerNodeDefinition -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out1 -> In; Out -> In |
| `c6df32c8e8c65b9a48f0` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 11 -> 12 -> 20 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questLogicalHubNodeDefinition -> questEventManagerNodeDefinition; Out -> In1; Out1 -> In |
| `2482f0f11bab0abddc11` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 3 -> 10 -> 11 | questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Succeeded |
| `050d20bede13a57863c1` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 3 -> 10 -> 12 | questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questLogicalHubNodeDefinition; Out -> In; False -> In2 |
| `7ae7495c535f66879e7a` | `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` / h0 / 10 -> 12 -> 20 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questLogicalHubNodeDefinition -> questEventManagerNodeDefinition; False -> In2; Out1 -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q301\q301.gamedef` | content candidate | ep1\quest\main_quests\q301\q301.quest |
| `ep1\quest\main_quests\q302\q302.gamedef` | content candidate | ep1\quest\main_quests\q302\q302.quest |
| `ep1\quest\main_quests\q303\q303.gamedef` | content candidate | ep1\quest\main_quests\q303\q303.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\openworld\ep1_open_world.gamedef` | content candidate | ep1\openworld\ep1_open_world.quest |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity_test.gamedef` | content candidate | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `q304_05_slider_stash_info_downloaded` | ep1\quest\main_quests\q304\scenes\q304_05_garage.scene / scene / 3496; 1 total source locations in compressed evidence |

NodeRef uses: 12; TweakDB binding uses: 3. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
