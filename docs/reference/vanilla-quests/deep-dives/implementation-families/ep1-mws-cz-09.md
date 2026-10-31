# ep1-mws-cz-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` | content candidate | 17 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 22 |
| `questCombatNodeDefinition` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 19 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 3 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questInputNodeDefinition` | 19 |
| `questLogicalAndNodeDefinition` | 19 |
| `questLogicalHubNodeDefinition` | 27 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMiscAICommandNode` | 12 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 8 |
| `questOutputNodeDefinition` | 22 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterMount_ConditionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 19 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 5 |
| `questPhaseNodeDefinition` | 16 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 44 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 16 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 3 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2f43bc55ad55580f4f99` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 5 -> 196 -> 225 |
| `375d2e7ca500c03f0f7a` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h1310 / 0 -> 19 -> 2 |
| `5b3c8c1da2f06b2a4afa` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 228 -> 193 -> 202 |
| `98e07870e42ea688f825` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 110 -> 111 -> 112 |
| `a362449474a4c83a958c` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h1310 / 16 -> 19 -> 2 |
| `a54f3ec841c1b20d61bb` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 193 -> 111 -> 112 |
| `b95e0068710ebce7a7dc` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 228 -> 193 -> 80 |
| `c31dc2737914da8bef9e` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 228 -> 193 -> 174 |
| `d50ccd8263a80adff19b` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 228 -> 193 -> 105 |
| `c1c385a57acb2ff1373d` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h1993 / 0 -> 14 -> 3 |
| `6df7f1c8c4e8b818ab5e` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 188 -> 110 -> 111 |
| `08d9a8938bfc07555aa9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 31 -> 8 -> 4 |
| `0d0f6e69eb1c5ad4bee9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 30 -> 8 -> 4 |
| `14e5f3bd901fbecd3e03` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 59 -> 8 -> 4 |
| `43777feef47568a586f5` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h781 / 6 -> 5 -> 129 |
| `4e4b0b0c06b141374035` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 20 -> 8 -> 4 |
| `4ff3abfc2e95448213b9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 56 -> 8 -> 4 |
| `62989a0fbb1eeadecd1b` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_09\mws_cz_09.questphase` / h199 / 28 -> 8 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
