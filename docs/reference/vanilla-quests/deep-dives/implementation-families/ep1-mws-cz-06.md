# ep1-mws-cz-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` | content candidate | 15 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 16 |
| `questCombatNodeDefinition` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 19 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 5 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questInputNodeDefinition` | 17 |
| `questLogicalAndNodeDefinition` | 16 |
| `questLogicalHubNodeDefinition` | 26 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 5 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 5 |
| `questOutputNodeDefinition` | 20 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 13 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 32 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 5 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 10 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 3 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `4f40a37fcba932bb0247` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h1945 / 6 -> 2 -> 17 |
| `5b35423dc4f059f3a7d7` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h1945 / 3 -> 2 -> 17 |
| `1df17639e0b6112a6ec4` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 182 -> 181 -> 183 |
| `2f43bc55ad55580f4f99` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 70 -> 155 -> 186 |
| `47f4f5fc3fc7eb31bd46` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 181 -> 183 -> 160 |
| `5a03b95327fca2d78080` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 181 -> 183 -> 176 |
| `5b3c8c1da2f06b2a4afa` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 188 -> 151 -> 153 |
| `5eeaca537d10d9625e7e` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 59 -> 131 -> 132 |
| `bf21ee8d571801576f26` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 180 -> 20 -> 138 |
| `d50ccd8263a80adff19b` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 188 -> 151 -> 17 |
| `daa7a0feb5c3d47c40c5` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 138 -> 31 -> 32 |
| `e0a3824015009f070156` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h767 / 0 -> 2 -> 21 |
| `e6f885d9c020ece66128` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 59 -> 131 -> 60 |
| `0bbbee1d16cced30ebe7` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 69 -> 17 -> 101 |
| `1efd1b36fe587f3de557` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h430 / 13 -> 19 -> 8 |
| `2140037116ca1ae0087b` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 96 -> 71 -> 70 |
| `2b9abb5adc87f8e63b9e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 151 -> 17 -> 101 |
| `2d9cc1f3cfcae916dbfc` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 96 -> 71 -> 70 |
| `33325fdca4866e13a05b` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h994 / 71 -> 70 -> 155 |
| `4abd3c5d2a5837407003` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_06\mws_cz_06.questphase` / h430 / 21 -> 13 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
