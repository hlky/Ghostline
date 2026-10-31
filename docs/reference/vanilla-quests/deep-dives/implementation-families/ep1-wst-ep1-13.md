# ep1-wst-ep1-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13_scene.scene |
| `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13_media.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13_scene.scene` | content candidate | 0 / 4 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckAnyoneDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 7 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `10928bf3a09bffffa44f` | 2 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 1 -> 41 -> 20 |
| `5743b77769af998e6baa` | 2 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 1 -> 41 -> 61 |
| `79ff30ab7464b071eda5` | 2 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 23 -> 35 -> 36 |
| `abe697defbff91d17846` | 2 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 3 -> 22 -> 23 |
| `ff01e9ceea872dacf574` | 2 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 22 -> 23 -> 35 |
| `26dea6cec66ce8243108` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 5 -> 6 -> 15 |
| `282fd08593d53394f518` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 61 -> 56 -> 57 |
| `2fa88f8b756d0471ddff` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 41 -> 61 -> 59 |
| `30d34adedee6f73fb995` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 36 -> 13 -> 14 |
| `328c3c837a86e92ca865` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 15 -> 10 -> 19 |
| `3b0f0db2118237a8d8fd` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 20 -> 21 -> 10 |
| `40bab5690f40c0b90015` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 36 -> 40 -> 39 |
| `498a6b7eecd95b64c096` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 41 -> 61 -> 56 |
| `4afa97c84ce6ea9b6942` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 1 -> 41 -> 16 |
| `6760a1badd9305b8f9bc` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 49 -> 50 -> 51 |
| `6a353fd4cdca12b560b7` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 18 -> 42 -> 11 |
| `6b8783ef27e0338de605` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 6 -> 15 -> 10 |
| `6c017a3cbb51268343eb` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 37 -> 38 -> 18 |
| `71509fd9baed518c2fa8` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 81 -> 80 -> 73 |
| `725d946ed4b2293c3260` | 1 | `ep1\openworld\world_stories\wst_ep1_13\wst_ep1_13.questphase` / h0 / 36 -> 4 -> 6 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
