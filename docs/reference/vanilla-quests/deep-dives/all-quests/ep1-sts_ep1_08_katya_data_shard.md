# Am I Demon?

Journal: `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard` · `MainQuest` · hash `1878048165`.

**Coverage: journal-linked.** 5 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Send Mr. Hands a message regarding Katya's shard. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/contact_mr_hands` |
| Crack the shard's security. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/crack_the_shard` |
| Sell the shard's data to Mr. Hands. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/sell_the_shard` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wst_ep1_22.questphase / h0 / 2` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/contact_mr_hands` | 41:Out → 2:Active; 2:Out → 3:Active |
| `wst_ep1_22.questphase / h0 / 35` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/contact_mr_hands` | 34:Out → 35:Succeeded; 35:Out → 36:Succeeded |
| `wst_ep1_22.questphase / h0 / 36` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard` | 35:Out → 36:Succeeded |
| `wst_ep1_22.questphase / h0 / 40` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/crack_the_shard` | 40:Out → 1:In; 43:Out → 40:Active |
| `wst_ep1_22.questphase / h0 / 41` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/crack_the_shard` | 1:Out → 41:Succeeded; 41:Out → 2:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| No resolved parent call in indexed scope | — | Global entry eligibility remains unproven |

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
| `sts_ep1_08_katya_data_cracked` | Producer outside selected context | wst_ep1_22.questphase / h0 / 1 |
| `sts_ep1_08_katya_data_obtained` | wst_ep1_22.questphase / h0 / 23 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>10 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wst_ep1_22.questphase / h0 / 1` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_katya_data_cracked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 40:Out → 1:In; 1:Out → 41:Succeeded |
| `wst_ep1_22.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data/wst_ep1_22_wanna_sell_data","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 3:Out → 4:In; 4:Out → 6:Active |
| `wst_ep1_22.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_followup/wst_ep1_22_how_much_worth","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 8:Out → 9:In; 9:Out → 13:Active |
| `wst_ep1_22.questphase / h0 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_followup/wst_ep1_22_sending_data","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 8:Out → 11:In; 11:Out → 10:Active |
| `wst_ep1_22.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_negotiate/wst_ep1_22_trust_you","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 14:Out → 15:In; 15:Out → 18:Active |
| `wst_ep1_22.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_negotiate/wst_ep1_22_v_gives_price","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 14:Out → 17:In; 17:Out → 16:Active |
| `wst_ep1_22.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sending_data/wst_ep1_22_sending_data","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 19:Out → 22:In; 22:Out → 20:Active |
| `wst_ep1_22.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#player"},"itemID":"117389262916","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 43:In; 43:Out → 40:Active |
| `wst_ep1_22.questphase / h0 / 44` | `questLogicalXorNodeDefinition` `{}` | 10:Out → 44:In1; 18:Out → 44:In2; 44:Out1 → 38:In |
| `wst_ep1_22.questphase / h0 / 45` | `questLogicalXorNodeDefinition` `{}` | 45:Out1 → 23:In; 37:Out → 45:In2; 38:Out → 45:In1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | wst_ep1_22.questphase / h0 / 1 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `item_state` | wst_ep1_22.questphase / h0 / 43 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | wst_ep1_22.questphase / h0 / 10; wst_ep1_22.questphase / h0 / 13; wst_ep1_22.questphase / h0 / 14; wst_ep1_22.questphase / h0 / 16; +11 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | wst_ep1_22.questphase / h0 / 33; wst_ep1_22.questphase / h0 / 34 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `persistent_decision` | wst_ep1_22.questphase / h0 / 23 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | wst_ep1_22.questphase / h0 / 44; wst_ep1_22.questphase / h0 / 45 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `reward_commit` | wst_ep1_22.questphase / h0 / 37; wst_ep1_22.questphase / h0 / 38 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` | content candidate; journal anchor | `ep1-wst-ep1-22` |

Evidence shards for this dossier (including parent context): [ep1-wst-ep1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-22.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

16 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `1a9b8893087e174a603f` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 40 -> 1 -> 41 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `235ed1f97cea566186b0` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 1 -> 41 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `451d99bb702265cce046` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 41 -> 2 -> 3 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> Active; Out -> Active |
| `694dcc3f01ba46e3e166` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 8 -> 11 -> 10 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> In; Out -> Active |
| `c6360c30becfcd41253a` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 13 -> 14 -> 17 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `1db42ef0f28084012290` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 9 -> 13 -> 14 | questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> Active; Out -> Active |
| `a60f36d3ae7b5b129c7e` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 11 -> 10 -> 44 | questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questLogicalXorNodeDefinition; Out -> Active; Out -> In1 |
| `73ea3b649aa5d8d484f7` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 38 -> 45 -> 23 | questRewardManagerNodeDefinition[questGiveReward_NodeType] -> questLogicalXorNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In1; Out1 -> In |
| `6a7927685d70d4902dc9` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 18 -> 44 -> 38 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questLogicalXorNodeDefinition -> questRewardManagerNodeDefinition[questGiveReward_NodeType]; Out -> In2; Out1 -> In |
| `cffc3a11a09d8fc3b1de` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 20 -> 37 -> 45 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questRewardManagerNodeDefinition[questGiveReward_NodeType] -> questLogicalXorNodeDefinition; Out -> In; Out -> In2 |
| `d3fa3ff235b25c371f60` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 2 -> 3 -> 4 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `f136c4c9119325c3cd94` | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 0 -> 43 -> 40 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| No direct launch-definition reference to this resolved context | Unresolved activation ownership | — |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| No external graph writer located | External engine/device/script production remains possible |

NodeRef uses: 1; TweakDB binding uses: 7. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
