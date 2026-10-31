# base-mws-wat-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 8 |
| `questCutControlNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 11 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 8 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterMount_ConditionType,questComparisonParam,questLogicalCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 16 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 5 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 22 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 8 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 16 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5eeaca537d10d9625e7e` | 8 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 90 -> 162 -> 161 |
| `daa7a0feb5c3d47c40c5` | 8 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 176 -> 111 -> 112 |
| `e6f885d9c020ece66128` | 8 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 90 -> 162 -> 89 |
| `c1c385a57acb2ff1373d` | 7 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 7 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h1253 / 0 -> 14 -> 3 |
| `08d9a8938bfc07555aa9` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 31 -> 8 -> 4 |
| `14e5f3bd901fbecd3e03` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 59 -> 8 -> 4 |
| `43777feef47568a586f5` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 6 -> 5 -> 129 |
| `49c892ff861d479f1c1a` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 129 -> 67 -> 90 |
| `4a269d313d396200872d` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 131 -> 67 -> 90 |
| `4e4b0b0c06b141374035` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 20 -> 8 -> 4 |
| `4ff3abfc2e95448213b9` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 56 -> 8 -> 4 |
| `62989a0fbb1eeadecd1b` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 28 -> 8 -> 4 |
| `7972eb9627beccb2111b` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 71 -> 8 -> 4 |
| `82a9643bae17b90ed0b6` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 13 -> 8 -> 4 |
| `834997c83e8ee1b6960b` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 67 -> 8 -> 4 |
| `8df562f11f6992956703` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h512 / 130 -> 67 -> 90 |
| `a36102ceee6fef729c5f` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 15 -> 8 -> 4 |
| `b1b55612587e803d1c24` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_05\mws_wat_05.questphase` / h129 / 59 -> 8 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
