# ep1-wst-ep1-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `bfe95df47bd1ca67330f` | 2 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 3 -> 11 -> 19 |
| `3457629da944eac3b4b2` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 0 -> 2 -> 3 |
| `481bb61cd41815a09fdf` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 4 -> 17 -> 10 |
| `bd3b2cde4bab8d271c84` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 10 -> 6 -> 12 |
| `c17ba4ca3671fae59af4` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 17 -> 10 -> 6 |
| `c8dd86e59dcccf53ce1a` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 19 -> 4 -> 17 |
| `e7f4dab64cf88a718cc9` | 1 | `ep1\openworld\world_stories\wst_ep1_14\wst_ep1_14.questphase` / h0 / 11 -> 19 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
