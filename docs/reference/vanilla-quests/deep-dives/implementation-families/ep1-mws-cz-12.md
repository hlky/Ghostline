# ep1-mws-cz-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` | content candidate | 15 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 17 |
| `questLogicalAndNodeDefinition` | 9 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 2 |
| `questOutputNodeDefinition` | 20 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterMount_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterMount_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 13 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
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
| `1efd1b36fe587f3de557` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h271 / 13 -> 19 -> 8 |
| `4abd3c5d2a5837407003` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h271 / 21 -> 13 -> 19 |
| `4cc4f28014e968ad6a08` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 124 -> 6 -> 5 |
| `96e544b4ea3b00e80c9e` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h271 / 21 -> 13 -> 20 |
| `c1c385a57acb2ff1373d` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h91 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h889 / 0 -> 14 -> 33 |
| `f29c08d36717c505c731` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 122 -> 6 -> 5 |
| `55f63c388f553509dee2` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h271 / 21 -> 22 -> 14 |
| `0ae8d28797e6e43caea9` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h204 / 0 -> 4 -> 2 |
| `0d88efa02aeee82ab489` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h204 / 3 -> 2 -> 1 |
| `1cfa47eb6d677e74c588` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h399 / 0 -> 32 -> 31 |
| `215ca95d939006973a7d` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h399 / 44 -> 45 -> 1 |
| `2f43bc55ad55580f4f99` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 5 -> 183 -> 191 |
| `32669ef2d03b444a525e` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h1370 / 6 -> 8 -> 19 |
| `33325fdca4866e13a05b` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 6 -> 5 -> 183 |
| `34734bea267da26f4309` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 174 -> 173 -> 105 |
| `375d2e7ca500c03f0f7a` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h608 / 0 -> 7 -> 2 |
| `39a864e002b9de7ab425` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 5 -> 131 -> 185 |
| `40ca0a6aeff908ebeb9d` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h1202 / 0 -> 2 -> 4 |
| `43777feef47568a586f5` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_12\mws_cz_12.questphase` / h452 / 6 -> 5 -> 132 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
