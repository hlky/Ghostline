# ep1-wst-ep1-22

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_accepts_v_price`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data/wst_ep1_22_wanna_sell_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_followup`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_followup/wst_ep1_22_how_much_worth`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_followup/wst_ep1_22_sending_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_negotiate`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_negotiate/wst_ep1_22_trust_you`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sell_data_negotiate/wst_ep1_22_v_gives_price`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sending_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_ch_sending_data/wst_ep1_22_sending_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_interested_in_buying_data`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_not_sure_how_much`
- `contacts/mr_hands/wst_ep1_22_katya_data/wst_ep1_22_thanks_sends_money`
- `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard`
- `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/contact_mr_hands`
- `ep1/quests/minor_quest/sts_ep1_08_katya_data_shard/contacts/crack_the_shard`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 10 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 5 |
| `questLogicalXorNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `694dcc3f01ba46e3e166` | 6 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 8 -> 11 -> 10 |
| `c6360c30becfcd41253a` | 5 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 13 -> 14 -> 17 |
| `1db42ef0f28084012290` | 3 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 9 -> 13 -> 14 |
| `1a9b8893087e174a603f` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 40 -> 1 -> 41 |
| `235ed1f97cea566186b0` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 1 -> 41 -> 2 |
| `451d99bb702265cce046` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 41 -> 2 -> 3 |
| `5f17e3165c265747c715` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 15 -> 18 -> 44 |
| `6a7927685d70d4902dc9` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 18 -> 44 -> 38 |
| `73ea3b649aa5d8d484f7` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 38 -> 45 -> 23 |
| `95a75fe41e0e1c494128` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 23 -> 30 -> 31 |
| `97aa687fd8298cd27fb3` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 10 -> 44 -> 38 |
| `9c1637db27a2c7be374d` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 37 -> 45 -> 23 |
| `a60f36d3ae7b5b129c7e` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 11 -> 10 -> 44 |
| `cffc3a11a09d8fc3b1de` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 20 -> 37 -> 45 |
| `d3fa3ff235b25c371f60` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 2 -> 3 -> 4 |
| `f136c4c9119325c3cd94` | 1 | `ep1\openworld\world_stories\wst_ep1_22\wst_ep1_22.questphase` / h0 / 0 -> 43 -> 40 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
