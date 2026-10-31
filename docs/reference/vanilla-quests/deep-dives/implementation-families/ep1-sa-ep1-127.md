# ep1-sa-ep1-127

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_29`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 11 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 34 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 44 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 34 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 118 -> 117 -> 127 |
| `20a77143a898bc753a26` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 8 -> 20 -> 21 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 100 -> 101 -> 96 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 349 -> 350 -> 362 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 335 -> 350 -> 362 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 357 -> 343 -> 342 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 78 -> 24 -> 23 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 351 -> 349 -> 350 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 333 -> 351 -> 349 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 333 -> 341 -> 357 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 21 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h291 / 333 -> 351 -> 335 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 111 -> 100 -> 101 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 93 -> 37 -> 58 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 127 -> 120 -> 37 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_127\sa_ep1_127.questphase` / h0 / 57 -> 11 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
