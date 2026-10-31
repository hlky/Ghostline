# base-mws-wbr-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_01\community\mws_wbr_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` | content candidate | 6 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` | content candidate | 0 / 101 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAsCrowdObstacle,questSetAsCrowdObstacle_NodeTypeParams]` | 9 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 8 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questLogicalHubNodeDefinition` | 7 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 10 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 7 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questGatherTriggerCondition,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 32 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 14 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 30 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnHubNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 27 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1f19ca77b00b3e5851f2` | 9 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1009 -> 1012 -> 1016 |
| `3a97f251b240e87051e6` | 9 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h526 / 0 -> 11 -> 2 |
| `20a77143a898bc753a26` | 8 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h456 / 4 -> 10 -> 5 |
| `3f452ac572b5ec564143` | 6 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 544 -> 1213 -> 425 |
| `42f5a4bd6fb7ac77e501` | 6 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h67 / 36 -> 51 -> 41 |
| `820c61dc6db2829126d7` | 6 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1213 -> 1021 -> 1050 |
| `767695cd3492264e6dd4` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1021 -> 1031 -> 1206 |
| `7d61d62ef7aa74a75c88` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1213 -> 1021 -> 1031 |
| `e394afad8fa723bd4087` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1021 -> 1031 -> 1053 |
| `145293552c6182ec258e` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h67 / 63 -> 61 -> 62 |
| `591e67eb044d6379bbfa` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h67 / 0 -> 63 -> 61 |
| `2179acd57cd33a158da3` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1425 -> 1374 -> 1377 |
| `3ac6d8c77268170a54e7` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1213 -> 1425 -> 1374 |
| `5a1eaf3d395cb512f5b1` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h667 / 0 -> 74 -> 75 |
| `74c9344e577682ba75e7` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 909 -> 1009 -> 1012 |
| `970882595212a1b63cac` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1425 -> 1374 -> 1378 |
| `97161d2ba073224f206d` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h67 / 51 -> 15 -> 24 |
| `b94d90be83fb692c0f6f` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 544 -> 1213 -> 1425 |
| `f088adb4ae3897bfd308` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\scenes\mws_wbr_01.scene` / scene / 1228 -> 1095 -> 691 |
| `39002dc30b8c6761724f` | 2 | `base\open_world\mini_world_stories\westbrook\mws_wbr_01\mws_wbr_01.questphase` / h20 / 426 -> 386 -> 384 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
