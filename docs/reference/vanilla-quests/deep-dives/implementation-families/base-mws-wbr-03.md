# base-mws-wbr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` | content candidate | 7 / 0 |  |

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
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 4 |
| `questCutControlNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 4 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
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
| `e0a3824015009f070156` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h606 / 0 -> 2 -> 21 |
| `5eeaca537d10d9625e7e` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 59 -> 145 -> 144 |
| `daa7a0feb5c3d47c40c5` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 149 -> 31 -> 32 |
| `e6f885d9c020ece66128` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 59 -> 145 -> 60 |
| `0bbbee1d16cced30ebe7` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 69 -> 17 -> 101 |
| `22b8ff11e7e49798423b` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h367 / 0 -> 9 -> 30 |
| `4a269d313d396200872d` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 86 -> 114 -> 20 |
| `52e256c57c21a40b4b08` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 15 -> 23 -> 51 |
| `598de76db428cdd3df4a` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 145 -> 144 -> 68 |
| `780e7777eda96886e6b1` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h367 / 9 -> 28 -> 32 |
| `808c42396a9735fe3a65` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 0 -> 19 -> 27 |
| `80dc5e4d799234ebd745` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 21 -> 12 -> 13 |
| `8df562f11f6992956703` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 88 -> 114 -> 20 |
| `b015ff991ad4ab5968a3` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 30 -> 49 -> 50 |
| `d4361c3162ef542168ac` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 29 -> 21 -> 3 |
| `d8f074f901df9fb245c9` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 70 -> 105 -> 85 |
| `e74b6f5cccd8dea44533` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 70 -> 116 -> 117 |
| `f1dfc330e8111460c52b` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 71 -> 70 -> 116 |
| `f271ae592045f39514cb` | 3 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h773 / 114 -> 20 -> 149 |
| `146d03d186468f0e231d` | 2 | `base\open_world\mini_world_stories\westbrook\mws_wbr_03\mws_wbr_03.questphase` / h97 / 3 -> 6 -> 5 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
