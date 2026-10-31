# ep1-sa-ep1-107

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_5`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 27 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 30 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 6 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 4 -> 3 -> 30 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 17 -> 176 -> 179 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 127 -> 11 -> 9 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 180 -> 17 -> 176 |
| `593e17bd1c9a456e6bde` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 104 -> 105 -> 138 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 52 -> 117 -> 72 |
| `7c781f52e78dc0d251df` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 82 -> 105 -> 138 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 119 -> 55 -> 59 |
| `e6a74d0120b15ec0f02c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 62 -> 25 -> 24 |
| `0a3c1367ab5953f38973` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 42 -> 78 -> 109 |
| `8bdf0da350d602cbf970` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 31 -> 54 -> 119 |
| `8d10896873df5c62014e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 24 -> 26 -> 84 |
| `972e7afc1f9fcd8bb438` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 31 -> 104 -> 105 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 52 -> 13 -> 25 |
| `aba3ecf25c2ddde8f28b` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 24 -> 26 -> 94 |
| `f36b4271f8b5e18f5d45` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h396 / 24 -> 26 -> 63 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 206 -> 50 -> 149 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 30 -> 206 -> 50 |
| `9e53815c35744add4647` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 206 -> 50 -> 47 |
| `c1052e80e86bb337f516` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_107\sa_ep1_107.questphase` / h0 / 4 -> 3 -> 47 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
