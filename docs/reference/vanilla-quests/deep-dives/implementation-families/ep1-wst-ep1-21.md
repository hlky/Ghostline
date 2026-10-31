# ep1-wst-ep1-21

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` | content candidate | 1 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21_com.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/quests/minor_quest/sts_ep1_08_loot_pickup`
- `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash`
- `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash`
- `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 5 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `3457629da944eac3b4b2` | 2 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 0 -> 3 -> 33 |
| `163b243e32c0bb8c4eb7` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 33 -> 24 -> 23 |
| `1d48bd7cbbaeca8257d2` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 31 -> 30 -> 22 |
| `20e35486dce84a4318f3` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 33 -> 24 -> 36 |
| `328c3c837a86e92ca865` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 35 -> 18 -> 25 |
| `6b1fcb4c46676ba8a912` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 30 -> 22 -> 35 |
| `756574daa5e17821e522` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 27 -> 28 -> 39 |
| `7d1dcb6883e69c76c400` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 41 -> 27 -> 28 |
| `83a3757c3e54bd269e2e` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 24 -> 23 -> 21 |
| `9380dda43f90ecd62efb` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 48 -> 50 -> 51 |
| `a307896b77afd6a7b01d` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 4 -> 29 -> 31 |
| `bc53dd92975e81e3636d` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 22 -> 35 -> 18 |
| `bfe95df47bd1ca67330f` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 3 -> 33 -> 24 |
| `c4cc47f1088342201da5` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 29 -> 31 -> 30 |
| `d9e8ed8a7a6aa1e9faf1` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 24 -> 36 -> 37 |
| `eac7724540229e714b48` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 50 -> 51 -> 4 |
| `f8b67b9861516876423d` | 1 | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 42 -> 48 -> 50 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
