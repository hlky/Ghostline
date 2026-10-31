# Phantom Liberty

Journal: `ep1/quests/main_quest/q300_phantom_liberty` · `MainQuest` · hash `2743273388`.

Journal premise: Sure V, a good edgerunner’s always lookin' to broaden their horizons, run down the unbeaten path. But one wrong move, and suddenly your back’s up against the wall. Believe me, been there. Before you dive too deep into the unknown, wrap up a few loose ends in Night City first. Step by step in this town, OK?

**Coverage: journal-linked.** 10 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Find out more about Evelyn Parker. (Primary) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/find_out_about_evelyn` |
| Find Evelyn's employer in Pacifica. (Primary) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_clues_to_pacifica` |
| Conclude your business with the Voodoo Boys. (Primary) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_placide` |
| Make a name for yourself in Night City. (Primary) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/prologue` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ep1_requirements.questphase / h0 / 8` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/prologue` | 24:Out → 8:Active; 8:Out → 28:Active |
| `ep1_requirements.questphase / h0 / 11` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/prologue` | 9:Out → 11:Succeeded; 11:Out → 12:Active |
| `ep1_requirements.questphase / h0 / 12` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/find_out_about_evelyn` | 11:Out → 12:Active; 12:Out → 14:In |
| `ep1_requirements.questphase / h0 / 18` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/find_out_about_evelyn` | 14:Out → 18:Succeeded; 18:Out → 19:Active |
| `ep1_requirements.questphase / h0 / 19` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_clues_to_pacifica` | 19:Out → 13:In; 18:Out → 19:Active |
| `ep1_requirements.questphase / h0 / 20` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_clues_to_pacifica` | 13:Out → 20:Succeeded; 20:Out → 21:Active |
| `ep1_requirements.questphase / h0 / 21` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_placide` | 21:Out → 3:In; 20:Out → 21:Active |
| `ep1_requirements.questphase / h0 / 22` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/00_unlock_ep1/follow_placide` | 3:Out → 22:Succeeded; 22:Out → 32:Succeeded |
| `ep1_requirements.questphase / h0 / 28` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty/description` | 8:Out → 28:Active; 28:Out → 9:In |
| `ep1_requirements.questphase / h0 / 32` (Journal) | `ep1/quests/main_quest/q300_phantom_liberty` | 22:Out → 32:Succeeded; 32:Out → 26:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\quest\ep1.questphase` / h58 / 12 | `ep1_requirements.questphase` | 15: PauseCondition: ep1_active Equal RED default; ep1_standalone Equal RED default; 15:Out → 12:In1 |
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
| `q101_done` | Producer outside selected context | ep1_requirements.questphase / h0 / 9 |
| `q105_done` | Producer outside selected context | ep1_requirements.questphase / h0 / 14 |
| `q110_butcher_shop_done` | Producer outside selected context | ep1_requirements.questphase / h0 / 13 |
| `q300_active` | ep1_requirements.questphase / h0 / 24; ep1_requirements.questphase / h0 / 26 | No reader in selected context |
| `q301_started` | Producer outside selected context | ep1_requirements.questphase / h0 / 3 |

## Exact gates, joins and cancellation

<details><summary>4 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ep1_requirements.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q301_started","value":1,"comparisonType":"GreaterOrEqual"}}}` | 21:Out → 3:In; 3:Out → 22:Succeeded |
| `ep1_requirements.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 28:Out → 9:In; 9:Out → 11:Succeeded |
| `ep1_requirements.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q110_butcher_shop_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 19:Out → 13:In; 13:Out → 20:Succeeded |
| `ep1_requirements.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:Out → 14:In; 14:Out → 18:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | ep1_requirements.questphase / h0 / 13; ep1_requirements.questphase / h0 / 14; ep1_requirements.questphase / h0 / 3; ep1_requirements.questphase / h0 / 9 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `journal_transition` | ep1_requirements.questphase / h0 / 11; ep1_requirements.questphase / h0 / 12; ep1_requirements.questphase / h0 / 18; ep1_requirements.questphase / h0 / 19; +6 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | ep1_requirements.questphase / h0 / 24; ep1_requirements.questphase / h0 / 26 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\ep1_requirements.questphase` | content candidate; journal anchor | `ep1-shared` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

6 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `1666d7526b9bab74f2e2` | `ep1\quest\ep1_requirements.questphase` / h0 / 11 -> 12 -> 14 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> Active; Out -> In |
| `1d48bd7cbbaeca8257d2` | `ep1\quest\ep1_requirements.questphase` / h0 / 22 -> 32 -> 26 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Succeeded; Out -> In |
| `1a9b8893087e174a603f` | `ep1\quest\ep1_requirements.questphase` / h0 / 19 -> 13 -> 20 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `235ed1f97cea566186b0` | `ep1\quest\ep1_requirements.questphase` / h0 / 9 -> 11 -> 12 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `b7ed287d779868c023f1` | `ep1\quest\ep1_requirements.questphase` / h0 / 24 -> 8 -> 28 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `q105_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 8; base\quest\main_quests\part1\q105\phases\q105_complete.questphase / h0 / 79; base\quest\test\cp77_chicken_test.scene / scene / 789; base\quest\test\cp77_chicken_test.scene / scene / 1375; 8 total source locations in compressed evidence |
| `q110_butcher_shop_done` | base\quest\main_quests\part1\q105\definitions\q105_chicken.scene / scene / 324; base\quest\main_quests\part1\q110\phases\q110_03_butcher_shop.questphase / h0 / 257; 2 total source locations in compressed evidence |
| `q301_started` | base\quest\minor_quests\mq033\scenes\mq033_chicken_test.scene / scene / 22; base\quest\minor_quests\mq033\scenes\mq033_chicken_test.scene / scene / 23; ep1\quest\minor_quests\mq303\test\mq303_chickentest.scene / scene / 408; ep1\quest\main_quests\q301\q301.questphase / h0 / 37; 4 total source locations in compressed evidence |

NodeRef uses: 0; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
