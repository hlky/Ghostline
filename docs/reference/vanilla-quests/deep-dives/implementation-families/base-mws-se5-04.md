# base-mws-se5-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 15 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 12 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 12 |
| `questCutControlNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questLogicalAndNodeDefinition` | 13 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 12 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterGroupAttitude_CondtionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 17 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterMount_ConditionType,questComparisonParam,questLogicalCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 24 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 9 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 34 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 12 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 24 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 5 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5eeaca537d10d9625e7e` | 12 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 90 -> 188 -> 187 |
| `daa7a0feb5c3d47c40c5` | 12 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 206 -> 111 -> 112 |
| `e6f885d9c020ece66128` | 12 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 90 -> 188 -> 89 |
| `c1c385a57acb2ff1373d` | 10 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 0 -> 9 -> 2 |
| `e0a3824015009f070156` | 10 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h1760 / 0 -> 14 -> 3 |
| `08d9a8938bfc07555aa9` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 31 -> 8 -> 4 |
| `14e5f3bd901fbecd3e03` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 59 -> 8 -> 4 |
| `43777feef47568a586f5` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 6 -> 5 -> 129 |
| `49c892ff861d479f1c1a` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 129 -> 67 -> 90 |
| `4a269d313d396200872d` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h697 / 131 -> 67 -> 90 |
| `4e4b0b0c06b141374035` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 20 -> 8 -> 4 |
| `4ff3abfc2e95448213b9` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 8 -> 32 -> 34 |
| `53143ae72ba696a385fd` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 56 -> 8 -> 4 |
| `55fff47f5da71f34f536` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 64 -> 8 -> 4 |
| `62989a0fbb1eeadecd1b` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 28 -> 8 -> 4 |
| `74956eb3c6f9b007bea9` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 66 -> 8 -> 4 |
| `7972eb9627beccb2111b` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 82 -> 8 -> 4 |
| `82a9643bae17b90ed0b6` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 13 -> 8 -> 4 |
| `834997c83e8ee1b6960b` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h131 / 90 -> 8 -> 4 |
| `843ee5c7d9c366c5c085` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_04\mws_se5_04.questphase` / h1760 / 30 -> 19 -> 7 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
