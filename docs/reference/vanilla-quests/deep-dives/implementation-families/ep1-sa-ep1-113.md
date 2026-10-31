# ep1-sa-ep1-113

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_13`
- `ep1/quests/sandbox_activities/courier_test/test/end_01/sa_ep1_garage_e5`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 15 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questDistanceCondition,questMappinGPSComparison_ConditionType,questMappinGPSDistance,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 8 |
| `questEventManagerNodeDefinition` | 35 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 43 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 13 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 8 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 36 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 13 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 168 -> 167 -> 169 |
| `20a77143a898bc753a26` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 29 -> 28 -> 32 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 95 -> 11 -> 9 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 144 -> 145 -> 140 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 149 -> 150 -> 152 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 143 -> 148 -> 145 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 142 -> 150 -> 152 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 148 -> 145 -> 144 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 147 -> 140 -> 139 |
| `0a3c1367ab5953f38973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 141 -> 142 -> 150 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 141 -> 143 -> 148 |
| `8d10896873df5c62014e` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 20 -> 10 -> 15 |
| `972e7afc1f9fcd8bb438` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 141 -> 149 -> 150 |
| `aba3ecf25c2ddde8f28b` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 20 -> 10 -> 86 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h258 / 20 -> 10 -> 49 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 145 -> 140 -> 159 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 109 -> 13 -> 25 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 136 -> 67 -> 111 |
| `206ee749ef12fb46b188` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h828 / 28 -> 30 -> 32 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_113\sa_ep1_113.questphase` / h0 / 64 -> 136 -> 67 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
