# base-mws-arr-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` | content candidate | 0 / 26 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 4 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 2 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnNodeId,scnSceneTime]` | 4 |
| `scnStartNode[scnNodeId]` | 1 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `291ed487080e604d017d` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 94 -> 49 -> 44 |
| `48dba4758f4dbcf0c72d` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase` / h12 / 4 -> 3 -> 1 |
| `58497b405887dd561f38` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 32 -> 30 -> 44 |
| `666e2e47265326bbe943` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 67 -> 75 -> 72 |
| `761c35cc851ddc8b7864` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase` / h0 / 5 -> 6 -> 1 |
| `921032b020c2f554cc64` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 6 -> 8 -> 18 |
| `a6e0defbd51d9a3b02a8` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 6 -> 8 -> 26 |
| `ab8de32c06175fbbfba2` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 1 -> 6 -> 8 |
| `ce02fe3459b5db226604` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 10 -> 39 -> 23 |
| `eba9dba27b27079fe9c4` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase` / h0 / 0 -> 2 -> 3 |
| `ebebf7dbc4ffad7f2362` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\scenes\mws_arr_01.scene` / scene / 39 -> 23 -> 32 |
| `efd665b185f42738b702` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_01\mws_arr_01.questphase` / h0 / 8 -> 5 -> 6 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
