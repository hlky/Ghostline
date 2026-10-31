# ep1-sa-ep1-140

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_distance_ignore.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_progress_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_hack_completed.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_42`
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
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawnAll_NodeType]` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 37 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 16 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 10 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMappinManagerNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questUIManagerNodeDefinition[questProximityProgressBar_NodeType]` | 2 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 6 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 14 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `46f6e677d95f49d38652` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 326 -> 327 -> 328 |
| `844196b6c9c48c869bed` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 468 -> 488 -> 157 |
| `f44dd2c3030f3f0cc7ad` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 507 -> 499 -> 498 |
| `9af8a87f20a910659fa8` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h0 / 92 -> 81 -> 82 |
| `adb1674e3d3173d5b06e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 522 -> 157 -> 196 |
| `b63d63d4851418db7779` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 468 -> 488 -> 266 |
| `d44e80a9c8bcf095fe60` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h0 / 141 -> 142 -> 140 |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h0 / 125 -> 115 -> 97 |
| `01749efafbb7386754ee` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 412 -> 515 -> 519 |
| `0eb504601d2220420a7a` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 488 -> 266 -> 168 |
| `23456c22048a301a4981` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 465 -> 441 -> 404 |
| `2d298b805ff1e7433a38` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 134 -> 162 -> 213 |
| `2e1ee5a1324dbeeb9071` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 135 -> 134 -> 162 |
| `34e2d96a43c285550e2b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 448 -> 464 -> 449 |
| `35fc9c9ed3035dd850a8` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 169 -> 171 -> 166 |
| `3b4cf03bd7ab76f88e15` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 533 -> 545 -> 547 |
| `3ed84eaba8f44fc4f398` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 541 -> 547 -> 538 |
| `488ec456cde7467dee6b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h1535 / 2 -> 4 -> 6 |
| `6518e513211213704654` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 543 -> 533 -> 541 |
| `65ba99b38c9ba0bb9d2b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_140\sa_ep1_140.questphase` / h12 / 421 -> 533 -> 541 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
