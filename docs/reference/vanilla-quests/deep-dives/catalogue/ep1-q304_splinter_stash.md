# Voodoo Treasure

Journal: `ep1/quests/minor_quest/q304_splinter_stash` · `MinorQuest` · hash `1660496179`.

**Coverage: journal-linked.** 4 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

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
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |

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

| Fact | Writers in context | Readers/conditions in context |
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
| `device_action` | q304_slider_stash.questphase / h0 / 18; q304_slider_stash.questphase / h0 / 21; q304_slider_stash.questphase / h0 / 4 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q304_slider_stash.questphase / h0 / 3 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | q304_slider_stash.questphase / h0 / 6 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `realtime_delay` | q304_slider_stash.questphase / h0 / 13 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_slider_stash.questphase` | content candidate; journal anchor | `ep1-q304` |

Evidence shards for this dossier (including parent context): [ep1-q304](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-q304.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
