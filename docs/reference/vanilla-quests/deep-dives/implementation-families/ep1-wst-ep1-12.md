# ep1-wst-ep1-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12_scene.scene |
| `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12_media.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12_scene.scene` | content candidate | 0 / 4 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
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
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckAnyoneDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 9 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `10928bf3a09bffffa44f` | 3 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 0 -> 46 -> 26 |
| `79ff30ab7464b071eda5` | 3 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 38 -> 40 -> 41 |
| `a06e5b5697b34a6e84ee` | 2 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 63 -> 24 -> 2 |
| `c9c638cd8df9e272328e` | 2 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 7 -> 63 -> 24 |
| `ff01e9ceea872dacf574` | 2 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 31 -> 32 -> 42 |
| `05d2345367007644492b` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 44 -> 47 -> 13 |
| `26dea6cec66ce8243108` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 4 -> 5 -> 20 |
| `30d34adedee6f73fb995` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 29 -> 21 -> 22 |
| `328c3c837a86e92ca865` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 20 -> 10 -> 9 |
| `3b0f0db2118237a8d8fd` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 26 -> 27 -> 10 |
| `40bab5690f40c0b90015` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 29 -> 49 -> 48 |
| `4afa97c84ce6ea9b6942` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 0 -> 46 -> 7 |
| `6760a1badd9305b8f9bc` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 58 -> 61 -> 62 |
| `6b8783ef27e0338de605` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 5 -> 20 -> 10 |
| `6e05a1219e111bdf4d9d` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 28 -> 29 -> 4 |
| `725d946ed4b2293c3260` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 29 -> 3 -> 5 |
| `7306d4d6f4fb2d1e8f5e` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 52 -> 55 -> 58 |
| `79176cea4efa068d440e` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 10 -> 9 -> 65 |
| `84ce7de7f2f3ea6f970d` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 25 -> 8 -> 31 |
| `8c5fa435e915755bcac6` | 1 | `ep1\openworld\world_stories\wst_ep1_12\wst_ep1_12.questphase` / h0 / 55 -> 58 -> 61 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
