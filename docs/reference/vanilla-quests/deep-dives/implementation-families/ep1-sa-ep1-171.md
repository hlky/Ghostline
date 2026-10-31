# ep1-sa-ep1-171

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_distance_ignore.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_progress_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_hack_completed.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_73`
- `ep1/quests/sandbox_activities/courier_test`
- `ep1/quests/sandbox_activities/courier_test/test`
- `ep1/quests/sandbox_activities/courier_test/test/after_hack_take_car`
- `ep1/quests/sandbox_activities/courier_test/test/chase_and_hack`
- `ep1/quests/sandbox_activities/courier_test/test/chase_and_hack/car_no_specific`
- `ep1/quests/sandbox_activities/courier_test/test/hacking_gototarget`
- `ep1/quests/sandbox_activities/courier_test/test/hacking_starting`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questCharacterManagerNodeDefinition` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawnAll_NodeType]` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 37 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 16 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 12 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMappinManagerNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 13 |
| `questUIManagerNodeDefinition[questProximityProgressBar_NodeType]` | 2 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 6 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 14 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `46f6e677d95f49d38652` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 326 -> 327 -> 328 |
| `844196b6c9c48c869bed` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 466 -> 464 -> 157 |
| `9af8a87f20a910659fa8` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h0 / 16 -> 15 -> 4 |
| `adb1674e3d3173d5b06e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 502 -> 157 -> 196 |
| `d44e80a9c8bcf095fe60` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h0 / 23 -> 24 -> 21 |
| `f44dd2c3030f3f0cc7ad` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 487 -> 478 -> 479 |
| `01749efafbb7386754ee` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 412 -> 495 -> 499 |
| `20a77143a898bc753a26` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h0 / 44 -> 35 -> 19 |
| `23456c22048a301a4981` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 461 -> 437 -> 404 |
| `2d298b805ff1e7433a38` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 134 -> 162 -> 213 |
| `2e1ee5a1324dbeeb9071` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 135 -> 134 -> 162 |
| `34e2d96a43c285550e2b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 444 -> 460 -> 445 |
| `488ec456cde7467dee6b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h1428 / 2 -> 4 -> 6 |
| `874f244bd7a185c32851` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 334 -> 335 -> 336 |
| `8a530f1abe574ef376a2` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 499 -> 466 -> 464 |
| `8ba2f1ff405051c02e75` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 464 -> 501 -> 502 |
| `9f968dd33569c459f4d6` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 464 -> 502 -> 157 |
| `b63d63d4851418db7779` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 466 -> 464 -> 266 |
| `bc1bbe870a5807c6d53c` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 384 -> 476 -> 475 |
| `bf07b4aa5b0c33bd4617` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_171\sa_ep1_171.questphase` / h12 / 472 -> 474 -> 470 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
