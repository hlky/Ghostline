# ep1-mws-cz-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` | content candidate | 16 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 22 |
| `questCombatNodeDefinition` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 4 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 15 |
| `questInputNodeDefinition` | 18 |
| `questLogicalAndNodeDefinition` | 16 |
| `questLogicalHubNodeDefinition` | 28 |
| `questLogicalXorNodeDefinition` | 10 |
| `questMiscAICommandNode` | 10 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 4 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 7 |
| `questOutputNodeDefinition` | 21 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 5 |
| `questPhaseNodeDefinition` | 15 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 44 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 14 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 4 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e0a3824015009f070156` | 10 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h1247 / 0 -> 14 -> 3 |
| `c1c385a57acb2ff1373d` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 0 -> 9 -> 2 |
| `5b3c8c1da2f06b2a4afa` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 235 -> 192 -> 195 |
| `a54f3ec841c1b20d61bb` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 192 -> 80 -> 105 |
| `b95e0068710ebce7a7dc` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 235 -> 192 -> 80 |
| `c31dc2737914da8bef9e` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 235 -> 192 -> 174 |
| `ca4d34b4c6649a45372a` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 6 -> 197 -> 230 |
| `d50ccd8263a80adff19b` | 7 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 235 -> 192 -> 105 |
| `08d9a8938bfc07555aa9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 31 -> 8 -> 4 |
| `0d0f6e69eb1c5ad4bee9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 30 -> 8 -> 4 |
| `14e5f3bd901fbecd3e03` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 61 -> 8 -> 4 |
| `375d2e7ca500c03f0f7a` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h637 / 0 -> 21 -> 2 |
| `43777feef47568a586f5` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h104 / 6 -> 5 -> 108 |
| `4e4b0b0c06b141374035` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 20 -> 8 -> 4 |
| `4ff3abfc2e95448213b9` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 22 -> 8 -> 4 |
| `62989a0fbb1eeadecd1b` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 28 -> 8 -> 4 |
| `82a9643bae17b90ed0b6` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 13 -> 8 -> 4 |
| `a36102ceee6fef729c5f` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h2284 / 15 -> 8 -> 4 |
| `a362449474a4c83a958c` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_08\mws_cz_08.questphase` / h637 / 18 -> 21 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
