# base-mws-arr-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCombatNodeDefinition` | 18 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 5 |
| `questLogicalAndNodeDefinition` | 12 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 8 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVehicleCollision_ConditionType,questVehicleCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 19 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 5 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 14 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `53d5208b81f6b90ddebd` | 6 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 92 -> 98 -> 95 |
| `66596649ae1619fb6b47` | 6 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 183 -> 63 -> 77 |
| `9397c898bb35317853b5` | 6 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 62 -> 72 -> 69 |
| `9c55b1f63a76f8a1defc` | 6 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 98 -> 101 -> 100 |
| `2212917ffb7f6de4a3dc` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h12 / 17 -> 9 -> 2 |
| `348b0837d1f7a5bdaf87` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 50 -> 59 -> 133 |
| `352c142407be97159275` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 74 -> 180 -> 182 |
| `372ef4268e5f96884795` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 74 -> 180 -> 64 |
| `450daf207136bdbb1e64` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 73 -> 69 -> 196 |
| `47edeb25f1fe5f37b009` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h12 / 11 -> 18 -> 2 |
| `4827f08cc2deba01aad6` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 13 -> 14 -> 23 |
| `4f74af1e52ea0d2b13d5` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 72 -> 69 -> 196 |
| `5bd1ffd1ddb27d04ed2d` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h12 / 11 -> 18 -> 2 |
| `5c9dba7306f15898d131` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 13 -> 14 -> 110 |
| `65c8e6a94d2911009994` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 163 -> 166 -> 167 |
| `756c2ce04a33c8466010` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 32 -> 57 -> 129 |
| `8b3405243df5673ad7e3` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 22 -> 31 -> 27 |
| `940c540fff25a96a935d` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 161 -> 163 -> 165 |
| `a699e14e9b7a10c6a6d1` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h124 / 72 -> 166 -> 167 |
| `b5930fbdb4eec0166e25` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_02\mws_arr_02.questphase` / h12 / 11 -> 18 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
