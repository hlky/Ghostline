# base-mws-joker

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `contacts/jim/hunt/00_hello`
- `contacts/jim/hunt/00_hello2`
- `contacts/jim/hunt/00_start`
- `contacts/jim/hunt/00_start_ch_01`
- `contacts/jim/hunt/00_start_ch_01/01_yes`
- `contacts/jim/hunt/00_start_ch_01/02_no`
- `contacts/jim/hunt/00_start_ch_restart`
- `contacts/jim/hunt/00_start_ch_restart/01_yes`
- `contacts/jim/hunt/00_start_no2_response`
- `contacts/jim/hunt/00_start_no_response`
- `contacts/jim/hunt/00_start_yes_response`
- `contacts/jim/hunt/01_ride`
- `contacts/jim/hunt/01_ride_ch`
- `contacts/jim/hunt/01_ride_ch/01_what`
- `contacts/jim/hunt/01_ride_ch/02_letsgo`
- `contacts/jim/hunt/01_ride_reaction1`
- `contacts/jim/hunt/01_ride_reaction2`
- `contacts/jim/hunt/01_ride_reaction3`
- `contacts/jim/hunt/02_golden`
- `contacts/jim/hunt/03_lucky`
- `contacts/jim/hunt/04_driver`
- `contacts/jim/hunt/05_splash`
- `contacts/jim/hunt/06_spare`
- `contacts/jim/hunt/07_hologram`
- `contacts/jim/hunt/08_sixth`
- `contacts/jim/hunt/09_lusty`
- `contacts/jim/hunt/10_ramen`
- `contacts/jim/hunt/aced`
- `contacts/jim/hunt/bet`
- `contacts/jim/hunt/bluff`
- `contacts/jim/hunt/chips`
- `contacts/jim/hunt/congratulations`
- `contacts/jim/hunt/congratulations_2`
- `contacts/jim/hunt/congratulations_ch`
- `contacts/jim/hunt/congratulations_ch/ch_01`
- `contacts/jim/hunt/congratulations_ch/ch_02`
- `contacts/jim/hunt/congratulations_ch2`
- `contacts/jim/hunt/congratulations_ch2/ch_01`
- `contacts/jim/hunt/disconnect`
- `contacts/jim/hunt/new_1`
- `contacts/jim/hunt/new_2`
- `contacts/jim/hunt/new_3`
- `contacts/jim/hunt/taught`
- `contacts/jim/hunt/well`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/driver`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/golden`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/hologram`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/lucky`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/lusty`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/ramen`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/ride`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/sixth`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/spare`
- `onscreens/emails/quests/mini_world_stories/mws_jim/shards/splash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questCharacterBodyType_CondtionType,questCharacterCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 38 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 34 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 10 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 10 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 30 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 23 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c6360c30becfcd41253a` | 15 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 27 -> 26 -> 29 |
| `f14a5c2b2bdffcab95a6` | 10 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 161 -> 108 -> 73 |
| `037ff8285be6830a8e6e` | 9 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 220 -> 222 -> 221 |
| `38fa6f831b5b88215432` | 9 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 219 -> 220 -> 222 |
| `a2ac242fd7b5bc709605` | 9 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 53 -> 54 -> 60 |
| `694dcc3f01ba46e3e166` | 6 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 100 -> 101 -> 102 |
| `9e39e99ae07a5aebaed8` | 4 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 24 -> 25 -> 27 |
| `1ae94ee872986dd79c0d` | 2 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 0 -> 218 -> 219 |
| `1db42ef0f28084012290` | 2 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 33 -> 35 -> 36 |
| `019ca5040cb89c9c2e75` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 238 -> 237 -> 239 |
| `09662b8399cee5dabacb` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 95 -> 191 -> 96 |
| `11f0785eddebebd8eaba` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 39 -> 40 -> 34 |
| `1c031892b19c6c01a822` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 40 -> 34 -> 49 |
| `1e5f42fc79549003c3a6` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 215 -> 53 -> 54 |
| `273dd0472b807ce0ad20` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 0 -> 94 -> 190 |
| `27a2dcbd75ce1e863830` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 40 -> 34 -> 42 |
| `411185aaa2517a4701fb` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 215 -> 217 -> 216 |
| `45b38da7d34c0e173d61` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 190 -> 95 -> 191 |
| `4f4fcf135cec9c9d0882` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 153 -> 215 -> 217 |
| `5f17e3165c265747c715` | 1 | `base\open_world\mini_world_stories\mws_joker\mws_jim.questphase` / h0 / 38 -> 39 -> 40 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
