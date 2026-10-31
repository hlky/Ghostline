# base-mws-wat-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.quest` | content candidate | 2 / 0 | base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 5 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 9 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 5 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 16 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 7 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 10 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1c385a57acb2ff1373d` | 6 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 6 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h972 / 0 -> 2 -> 7 |
| `5eeaca537d10d9625e7e` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 60 -> 71 -> 70 |
| `daa7a0feb5c3d47c40c5` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 79 -> 16 -> 17 |
| `e6f885d9c020ece66128` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 60 -> 71 -> 58 |
| `146d03d186468f0e231d` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 25 -> 26 -> 30 |
| `43777feef47568a586f5` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 8 -> 7 -> 13 |
| `4757508be048eca14a5f` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 9 -> 2 -> 12 |
| `4a269d313d396200872d` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 14 -> 44 -> 24 |
| `4e4b0b0c06b141374035` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 20 -> 8 -> 3 |
| `4ff3abfc2e95448213b9` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 8 -> 23 -> 24 |
| `6f042f60b3c51702d68b` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 38 -> 8 -> 3 |
| `747b7bfbfb564b635fcd` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 36 -> 8 -> 3 |
| `7972eb9627beccb2111b` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 40 -> 8 -> 3 |
| `82a9643bae17b90ed0b6` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 13 -> 8 -> 3 |
| `8df562f11f6992956703` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h451 / 41 -> 44 -> 24 |
| `b1b55612587e803d1c24` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 21 -> 8 -> 3 |
| `c0e13b65402b413c39d8` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 33 -> 8 -> 3 |
| `d30bb1214ae0ae464bdf` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 21 -> 8 -> 3 |
| `d8ef39870626a261efb0` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_06\mws_wat_06.questphase` / h163 / 12 -> 8 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
