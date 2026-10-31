# The Gig

Journal: `quests/side_quest/sq_q001_wakako` · `SideQuest` · hash `3861473594`.

**Coverage: journal-linked.** 9 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Whenever we go see Wakako and walk into that pachinko salon of hers, I get this weird, like, tingling feeling on the back of my neck. I dunno, V, she's all kinds of weird. Anyway, she promised a special reward for this job with Sandra Dorsett. All we have to do is go see her on Jig-Jig Street. (Primary) | `quests/side_quest/sq_q001_wakako/wakako/00_reward` |
| Collect your reward from Wakako. (Primary) | `quests/side_quest/sq_q001_wakako/wakako/01_reward` |
| Collect your free reward from Cassius Ryder's ripperdoc shop inventory. (Primary) | `quests/side_quest/sq_q001_wakako/wakako/02_reward` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q101_wakako_reward.questphase / h0 / 2` (Journal) | `quests/side_quest/sq_q001_wakako` | 25:Out → 2:Active; 2:Out → 8:Active |
| `q101_wakako_reward.questphase / h0 / 4` (Journal) | `quests/side_quest/sq_q001_wakako` | 18:Out → 4:Succeeded; 4:Out → 26:In |
| `q101_wakako_reward.questphase / h0 / 5` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/01_reward` | 5:Out → 3:In; 9:Out → 5:Active |
| `q101_wakako_reward.questphase / h0 / 6` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/01_reward` | 11:Out → 6:Succeeded; 6:Out → 12:Active |
| `q101_wakako_reward.questphase / h0 / 8` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/00_reward` | 2:Out → 8:Active; 8:Out → 10:Active |
| `q101_wakako_reward.questphase / h0 / 9` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/00_reward` | 9:Out → 5:Active; 7:Out → 9:Succeeded |
| `q101_wakako_reward.questphase / h0 / 10` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/00_reward/description` | 10:Out → 7:In; 8:Out → 10:Active |
| `q101_wakako_reward.questphase / h0 / 15` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/02_reward` | 13:Out → 15:Active; 15:Out → 30:In |
| `q101_wakako_reward.questphase / h0 / 18` (Journal) | `quests/side_quest/sq_q001_wakako/wakako/02_reward` | 18:Out → 4:Succeeded; 29:Out → 18:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\persistent_content.questphase` / h1469 / 5 | `q101_wakako_reward.questphase` | 7: LogicalXor; 7:Out1 → 5:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |

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
| `q001_wakako_reward_given` | Producer outside selected context | q101_wakako_reward.questphase / h0 / 3 |
| `q101_enable_side_content` | Producer outside selected context | q101_wakako_reward.questphase / h0 / 7 |
| `sq_q001_active` | q101_wakako_reward.questphase / h0 / 25; q101_wakako_reward.questphase / h0 / 26 | No reader in selected context |
| `sq_q001_add_reward` | q101_wakako_reward.questphase / h0 / 28 | No reader in selected context |
| `sq_q001_done` | q101_wakako_reward.questphase / h0 / 27 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>3 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q101_wakako_reward.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_wakako_reward_given"}}}` | 5:Out → 3:In; 3:Out → 11:In |
| `q101_wakako_reward.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 10:Out → 7:In; 7:Out → 9:Succeeded |
| `q101_wakako_reward.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"77728680530","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"112450385958","quantity":1,"comparisonType":"GreaterOrEqual"}}]}}` | 29:Out → 18:Succeeded; 28:Out → 29:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | q101_wakako_reward.questphase / h0 / 3; q101_wakako_reward.questphase / h0 / 7 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `item_state` | q101_wakako_reward.questphase / h0 / 29 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `persistent_decision` | q101_wakako_reward.questphase / h0 / 25; q101_wakako_reward.questphase / h0 / 26; q101_wakako_reward.questphase / h0 / 27; q101_wakako_reward.questphase / h0 / 28 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `reward_commit` | q101_wakako_reward.questphase / h0 / 11 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\main_quests\prologue\q001\phases\q101_wakako_reward.questphase` | content candidate; journal anchor | `base-q001` |

Evidence shards for this dossier (including parent context): [base-q001](../../../../../reference/quests/deep-dives/catalogue/evidence/base-q001.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
