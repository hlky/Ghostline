# ep1-mws-cz-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` | content candidate | 17 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 12 |
| `questCombatNodeDefinition` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 19 |
| `questLogicalAndNodeDefinition` | 15 |
| `questLogicalHubNodeDefinition` | 19 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMiscAICommandNode` | 4 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 4 |
| `questOutputNodeDefinition` | 22 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterMount_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 15 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 24 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 5 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 2 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1c385a57acb2ff1373d` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 0 -> 9 -> 2 |
| `ca4d34b4c6649a45372a` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 6 -> 172 -> 166 |
| `e0a3824015009f070156` | 6 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h1287 / 0 -> 14 -> 33 |
| `1efd1b36fe587f3de557` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h373 / 13 -> 19 -> 8 |
| `22208713ab4429419a4a` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 29 -> 8 -> 4 |
| `375d2e7ca500c03f0f7a` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h815 / 0 -> 9 -> 2 |
| `43777feef47568a586f5` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 6 -> 5 -> 132 |
| `4757508be048eca14a5f` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 9 -> 2 -> 12 |
| `4abd3c5d2a5837407003` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h373 / 21 -> 13 -> 19 |
| `4cc4f28014e968ad6a08` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 124 -> 6 -> 5 |
| `4fd58750800eef2bd6eb` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h910 / 0 -> 4 -> 2 |
| `4ff3abfc2e95448213b9` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 28 -> 8 -> 4 |
| `6276bb29e49f92f12f57` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 190 -> 203 -> 192 |
| `6df7f1c8c4e8b818ab5e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 173 -> 81 -> 80 |
| `82a9643bae17b90ed0b6` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 31 -> 8 -> 4 |
| `93c1898ee0554f0c33a9` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 198 -> 173 -> 81 |
| `96e544b4ea3b00e80c9e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h373 / 21 -> 13 -> 20 |
| `98e07870e42ea688f825` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h543 / 81 -> 80 -> 105 |
| `a36102ceee6fef729c5f` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_11\mws_cz_11.questphase` / h98 / 15 -> 8 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
