# base-mws-wbr-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_05\community\mws_wbr_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 5 |
| `questCutControlNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 5 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 8 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 10 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e0a3824015009f070156` | 6 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h602 / 0 -> 13 -> 16 |
| `5eeaca537d10d9625e7e` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 97 -> 149 -> 148 |
| `daa7a0feb5c3d47c40c5` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 151 -> 101 -> 106 |
| `e6f885d9c020ece66128` | 5 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 97 -> 149 -> 96 |
| `142b5b5db9d8fd127640` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 77 -> 54 -> 39 |
| `14e5f3bd901fbecd3e03` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 63 -> 54 -> 39 |
| `43777feef47568a586f5` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 71 -> 70 -> 85 |
| `4757508be048eca14a5f` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 55 -> 33 -> 48 |
| `480a010388ce3a487ffb` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 48 -> 54 -> 39 |
| `4a269d313d396200872d` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 85 -> 72 -> 97 |
| `4ff3abfc2e95448213b9` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 54 -> 39 -> 44 |
| `53143ae72ba696a385fd` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 51 -> 54 -> 39 |
| `82a9643bae17b90ed0b6` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 50 -> 54 -> 39 |
| `8df562f11f6992956703` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h760 / 84 -> 72 -> 97 |
| `a36102ceee6fef729c5f` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 49 -> 54 -> 39 |
| `ac31b5fb2ea24ca43895` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 65 -> 54 -> 39 |
| `aea7f6f1090aed0a6593` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 75 -> 54 -> 39 |
| `b5fcd626cddf62c816af` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 63 -> 54 -> 39 |
| `be837e40b8a894907830` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 77 -> 54 -> 39 |
| `c5e06569ffe3a0a19809` | 4 | `base\open_world\mini_world_stories\westbrook\mws_wbr_05\mws_wbr_05.questphase` / h103 / 63 -> 54 -> 39 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
