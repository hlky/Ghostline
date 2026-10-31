# ep1-wst-ep1-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_01\wst_ep1_01.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0d0f1617f4485c1b2bba` | 1 | `ep1\openworld\world_stories\wst_ep1_01\wst_ep1_01.questphase` / h0 / 15 -> 28 -> 27 |
| `9555178c9f24c6404fbe` | 1 | `ep1\openworld\world_stories\wst_ep1_01\wst_ep1_01.questphase` / h0 / 14 -> 15 -> 28 |
| `ea4cb15199b9b3fa8e63` | 1 | `ep1\openworld\world_stories\wst_ep1_01\wst_ep1_01.questphase` / h0 / 12 -> 14 -> 15 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
