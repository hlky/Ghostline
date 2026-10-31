# base-mws-hey-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 4 |
| `questCutControlNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 6 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 4 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 14 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 8 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5eeaca537d10d9625e7e` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 57 -> 79 -> 78 |
| `c1c385a57acb2ff1373d` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h199 / 0 -> 9 -> 2 |
| `daa7a0feb5c3d47c40c5` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 83 -> 16 -> 17 |
| `e0a3824015009f070156` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h946 / 0 -> 2 -> 7 |
| `e6f885d9c020ece66128` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 57 -> 79 -> 18 |
| `22b8ff11e7e49798423b` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h1117 / 0 -> 36 -> 42 |
| `31341098211086462e6b` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 58 -> 26 -> 21 |
| `52e256c57c21a40b4b08` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h199 / 7 -> 14 -> 32 |
| `780e7777eda96886e6b1` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h1117 / 36 -> 40 -> 44 |
| `b015ff991ad4ab5968a3` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h199 / 14 -> 32 -> 33 |
| `b1cf29259939278c4ac6` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 82 -> 26 -> 21 |
| `b7f8a78fd96d5b3ca452` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h946 / 25 -> 26 -> 31 |
| `cb6ba8fe3946177c6ee2` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 17 -> 26 -> 21 |
| `cfdc4d160cbda67f5eb4` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 0 -> 67 -> 68 |
| `e74b6f5cccd8dea44533` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 7 -> 40 -> 41 |
| `f1dfc330e8111460c52b` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 8 -> 7 -> 40 |
| `019e8b5537945e91f923` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 62 -> 63 -> 26 |
| `0bbbee1d16cced30ebe7` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h458 / 16 -> 17 -> 26 |
| `14e5f3bd901fbecd3e03` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h199 / 25 -> 8 -> 3 |
| `227037b5e7f2d6d4ed0d` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_05\mws_hey_05.questphase` / h199 / 17 -> 21 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
