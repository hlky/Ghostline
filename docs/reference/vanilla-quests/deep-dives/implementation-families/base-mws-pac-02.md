# base-mws-pac-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\pacifica\mws_pac_02\community\mws_pac_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase |
| `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 6 |
| `questCutControlNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 6 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 11 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 8 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 12 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5eeaca537d10d9625e7e` | 6 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 97 -> 146 -> 150 |
| `daa7a0feb5c3d47c40c5` | 6 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 151 -> 101 -> 106 |
| `e0a3824015009f070156` | 6 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h635 / 0 -> 13 -> 16 |
| `e6f885d9c020ece66128` | 6 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 97 -> 146 -> 96 |
| `045316bbf4dc2ccf8aca` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 40 -> 45 -> 43 |
| `146d03d186468f0e231d` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 39 -> 44 -> 43 |
| `14e5f3bd901fbecd3e03` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 57 -> 54 -> 39 |
| `43777feef47568a586f5` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 71 -> 70 -> 85 |
| `480a010388ce3a487ffb` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 48 -> 54 -> 39 |
| `4a269d313d396200872d` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 85 -> 72 -> 97 |
| `4ff3abfc2e95448213b9` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 54 -> 39 -> 44 |
| `53143ae72ba696a385fd` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 51 -> 54 -> 39 |
| `808c42396a9735fe3a65` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 0 -> 33 -> 48 |
| `82a9643bae17b90ed0b6` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 50 -> 54 -> 39 |
| `8df562f11f6992956703` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h809 / 84 -> 72 -> 97 |
| `97518b3d83f2e456db90` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 71 -> 54 -> 39 |
| `a36102ceee6fef729c5f` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 49 -> 54 -> 39 |
| `ac31b5fb2ea24ca43895` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 76 -> 54 -> 39 |
| `aea7f6f1090aed0a6593` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 78 -> 54 -> 39 |
| `b5fcd626cddf62c816af` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_02\mws_pac_02.questphase` / h103 / 57 -> 54 -> 39 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
