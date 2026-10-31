# ep1-mws-cz-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` | content candidate | 14 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCombatNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 16 |
| `questLogicalAndNodeDefinition` | 9 |
| `questLogicalHubNodeDefinition` | 16 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 2 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 11 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 16 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 2 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1efd1b36fe587f3de557` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h303 / 13 -> 19 -> 8 |
| `375d2e7ca500c03f0f7a` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h659 / 0 -> 15 -> 2 |
| `4abd3c5d2a5837407003` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h303 / 21 -> 13 -> 19 |
| `4cc4f28014e968ad6a08` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h491 / 6 -> 8 -> 7 |
| `4f40a37fcba932bb0247` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h1156 / 4 -> 2 -> 5 |
| `5b35423dc4f059f3a7d7` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h1156 / 3 -> 2 -> 5 |
| `96e544b4ea3b00e80c9e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h303 / 21 -> 13 -> 20 |
| `a362449474a4c83a958c` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h659 / 10 -> 15 -> 2 |
| `c1c385a57acb2ff1373d` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h108 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h925 / 0 -> 10 -> 7 |
| `f29c08d36717c505c731` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h491 / 5 -> 8 -> 7 |
| `0d88efa02aeee82ab489` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h242 / 4 -> 2 -> 1 |
| `55f63c388f553509dee2` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h303 / 21 -> 22 -> 14 |
| `71ec4a8c7b5d3e9b0f09` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h242 / 5 -> 2 -> 1 |
| `86bca07cda2d32c976c3` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h242 / 6 -> 2 -> 1 |
| `943bf0d3613ddcc51523` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h242 / 3 -> 2 -> 1 |
| `0ae8d28797e6e43caea9` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h242 / 0 -> 3 -> 2 |
| `0bbbee1d16cced30ebe7` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h491 / 16 -> 17 -> 26 |
| `2b9abb5adc87f8e63b9e` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h491 / 54 -> 17 -> 26 |
| `2e609f414fc3de5fdece` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_07\mws_cz_07.questphase` / h491 / 17 -> 26 -> 40 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
