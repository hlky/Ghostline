# base-mws-wbr-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 7 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 9 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 7 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 5 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 22 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 10 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 14 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e0a3824015009f070156` | 10 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h1102 / 0 -> 14 -> 3 |
| `c1c385a57acb2ff1373d` | 8 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 0 -> 9 -> 2 |
| `5eeaca537d10d9625e7e` | 7 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 90 -> 166 -> 165 |
| `daa7a0feb5c3d47c40c5` | 7 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 174 -> 80 -> 105 |
| `e6f885d9c020ece66128` | 7 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 90 -> 166 -> 89 |
| `0d0f6e69eb1c5ad4bee9` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 30 -> 8 -> 4 |
| `14e5f3bd901fbecd3e03` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 61 -> 8 -> 4 |
| `43777feef47568a586f5` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 6 -> 5 -> 108 |
| `49c892ff861d479f1c1a` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 109 -> 67 -> 90 |
| `4a269d313d396200872d` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 108 -> 67 -> 90 |
| `4e4b0b0c06b141374035` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 20 -> 8 -> 4 |
| `4ff3abfc2e95448213b9` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 22 -> 8 -> 4 |
| `62989a0fbb1eeadecd1b` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 28 -> 8 -> 4 |
| `82a9643bae17b90ed0b6` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 13 -> 8 -> 4 |
| `8df562f11f6992956703` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h405 / 114 -> 67 -> 90 |
| `97518b3d83f2e456db90` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 66 -> 8 -> 4 |
| `a36102ceee6fef729c5f` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 15 -> 8 -> 4 |
| `b1b55612587e803d1c24` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 61 -> 8 -> 4 |
| `b50d2df4ab802800c61e` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_04\mws_wbr_04.questphase` / h65 / 14 -> 8 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
