# ep1-sa-ep1-102

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` | content candidate | 3 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102_combat_community.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_102`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 30 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 7 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 26 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 2 -> 22 -> 26 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 74 -> 72 -> 119 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 103 -> 104 -> 99 |
| `0a3c1367ab5953f38973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 10 -> 15 -> 82 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 81 -> 82 -> 111 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 55 -> 100 -> 57 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 15 -> 82 -> 111 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 10 -> 49 -> 83 |
| `8d10896873df5c62014e` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 21 -> 10 -> 15 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 83 -> 51 -> 50 |
| `972e7afc1f9fcd8bb438` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 10 -> 81 -> 82 |
| `aba3ecf25c2ddde8f28b` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 21 -> 10 -> 81 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 80 -> 24 -> 23 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 21 -> 10 -> 49 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 114 -> 103 -> 104 |
| `20a77143a898bc753a26` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h267 / 8 -> 20 -> 21 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 47 -> 11 -> 25 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 94 -> 45 -> 70 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 36 -> 94 -> 45 |
| `9e53815c35744add4647` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_102\sa_ep1_102.questphase` / h0 / 94 -> 45 -> 42 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
