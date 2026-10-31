# ep1-wst-ep1-100

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_100.questphase` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_100\wst_ep1_101\wst_ep1_101.questphase; ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase |
| `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_101\wst_ep1_101.questphase` | content candidate | 1 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0a44294d973ee0c8afcd` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_101\wst_ep1_101.questphase` / h0 / 6 -> 7 -> 8 |
| `2179483c4d9ed5db29c9` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 0 -> 6 -> 7 |
| `4947cc5bd61f76664b84` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 7 -> 8 -> 9 |
| `4fe64daeff05e511ddfb` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 9 -> 5 -> 10 |
| `579e034397d549f39f8a` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 6 -> 7 -> 8 |
| `85d7311426e632fa016e` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 8 -> 9 -> 5 |
| `85f4bdeeacbf141e610a` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 8 -> 9 -> 12 |
| `a3e5f861a4b71433135a` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 5 -> 10 -> 1 |
| `b3205573f616e5f366a7` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_102\wst_ep1_102.questphase` / h0 / 12 -> 13 -> 14 |
| `eb7ff9b2d44adc239222` | 1 | `ep1\openworld\world_stories\wst_ep1_100\wst_ep1_101\wst_ep1_101.questphase` / h0 / 0 -> 6 -> 7 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
