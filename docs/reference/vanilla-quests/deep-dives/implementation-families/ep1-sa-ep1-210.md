# ep1-sa-ep1-210

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_distance_ignore.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_hacking_progress_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_hack_completed.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_210`
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
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 7 |
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
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 17 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 10 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 3 |
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
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
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
| `46f6e677d95f49d38652` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 326 -> 327 -> 328 |
| `844196b6c9c48c869bed` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 483 -> 489 -> 157 |
| `f44dd2c3030f3f0cc7ad` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 534 -> 518 -> 517 |
| `9af8a87f20a910659fa8` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h0 / 45 -> 35 -> 36 |
| `adb1674e3d3173d5b06e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 550 -> 157 -> 196 |
| `d44e80a9c8bcf095fe60` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h0 / 53 -> 54 -> 51 |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h0 / 65 -> 64 -> 49 |
| `01749efafbb7386754ee` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 412 -> 543 -> 547 |
| `23456c22048a301a4981` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 474 -> 437 -> 404 |
| `2e1ee5a1324dbeeb9071` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 135 -> 134 -> 162 |
| `34e2d96a43c285550e2b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 490 -> 506 -> 491 |
| `35fc9c9ed3035dd850a8` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 169 -> 171 -> 166 |
| `3b4cf03bd7ab76f88e15` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 566 -> 576 -> 583 |
| `3ed84eaba8f44fc4f398` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 575 -> 579 -> 561 |
| `488ec456cde7467dee6b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h1526 / 2 -> 4 -> 6 |
| `6518e513211213704654` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 578 -> 565 -> 575 |
| `65ba99b38c9ba0bb9d2b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 421 -> 565 -> 575 |
| `7605d08f9e177b1b3c35` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 577 -> 579 -> 561 |
| `7c7062e6c1de3aafaf9d` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 168 -> 259 -> 169 |
| `874f244bd7a185c32851` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_210\sa_ep1_210.questphase` / h12 / 334 -> 335 -> 336 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
