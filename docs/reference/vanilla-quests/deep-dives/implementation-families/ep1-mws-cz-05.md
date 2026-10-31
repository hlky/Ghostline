# ep1-mws-cz-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\chase_token_system.questphase` | content candidate | 4 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\community\mws_cz_05_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` | content candidate | 15 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 9 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 12 |
| `questCombatNodeDefinition` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 4 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 17 |
| `questInputNodeDefinition` | 21 |
| `questLogicalAndNodeDefinition` | 16 |
| `questLogicalHubNodeDefinition` | 23 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 2 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 4 |
| `questOutputNodeDefinition` | 24 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 16 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 19 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 2 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e2bd4b986fcf2a83f7a6` | 11 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\chase_token_system.questphase` / h107 / 0 -> 14 -> 3 |
| `375d2e7ca500c03f0f7a` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h1132 / 0 -> 15 -> 2 |
| `4f40a37fcba932bb0247` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h1560 / 6 -> 4 -> 7 |
| `591e67eb044d6379bbfa` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h642 / 0 -> 30 -> 3 |
| `5b35423dc4f059f3a7d7` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h1560 / 5 -> 4 -> 7 |
| `829956d9e119d2c5d69e` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h642 / 30 -> 13 -> 16 |
| `a362449474a4c83a958c` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h1132 / 14 -> 15 -> 2 |
| `4cc4f28014e968ad6a08` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 78 -> 71 -> 70 |
| `a553462757d78f7423f6` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 80 -> 71 -> 70 |
| `ea8ea9f40087d567a333` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 81 -> 71 -> 70 |
| `f29c08d36717c505c731` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 79 -> 71 -> 70 |
| `01d898597b49a509b8c9` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 200 -> 103 -> 153 |
| `1df17639e0b6112a6ec4` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 177 -> 210 -> 212 |
| `1efd1b36fe587f3de557` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h334 / 13 -> 19 -> 8 |
| `1fd7777f1542cb243368` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 103 -> 153 -> 110 |
| `22208713ab4429419a4a` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h171 / 52 -> 54 -> 39 |
| `2f43bc55ad55580f4f99` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 70 -> 177 -> 210 |
| `315511ddb9054f123c54` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 202 -> 200 -> 99 |
| `32669ef2d03b444a525e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h1784 / 3 -> 8 -> 10 |
| `43777feef47568a586f5` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_05\mws_cz_05.questphase` / h796 / 71 -> 70 -> 85 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
