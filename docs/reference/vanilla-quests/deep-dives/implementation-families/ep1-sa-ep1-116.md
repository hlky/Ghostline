# ep1-sa-ep1-116

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_17`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 7 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 30 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 8 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 31 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 4 -> 3 -> 29 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 108 -> 109 -> 104 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 129 -> 104 -> 92 |
| `20a77143a898bc753a26` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 9 -> 8 -> 20 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 111 -> 112 -> 135 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 49 -> 105 -> 51 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 15 -> 112 -> 135 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 106 -> 100 -> 99 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 78 -> 24 -> 23 |
| `0a3c1367ab5953f38973` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 87 -> 102 -> 120 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 109 -> 104 -> 123 |
| `8bdf0da350d602cbf970` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 10 -> 49 -> 105 |
| `8d10896873df5c62014e` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 20 -> 10 -> 15 |
| `972e7afc1f9fcd8bb438` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 10 -> 111 -> 112 |
| `aba3ecf25c2ddde8f28b` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 20 -> 10 -> 111 |
| `f36b4271f8b5e18f5d45` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h247 / 20 -> 10 -> 49 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 81 -> 13 -> 25 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 125 -> 64 -> 83 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 35 -> 124 -> 64 |
| `9e53815c35744add4647` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_116\sa_ep1_116.questphase` / h0 / 125 -> 64 -> 61 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
