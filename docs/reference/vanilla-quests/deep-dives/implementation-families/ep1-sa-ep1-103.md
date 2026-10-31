# ep1-sa-ep1-103

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` | content candidate | 3 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103_combat_community.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_2`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 26 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 6 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 4 |
| `questRandomizerNodeDefinition` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 24 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 114 -> 113 -> 117 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 99 -> 101 -> 86 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 99 -> 11 -> 9 |
| `0a3c1367ab5953f38973` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 119 -> 120 -> 127 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 91 -> 86 -> 105 |
| `593e17bd1c9a456e6bde` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 126 -> 127 -> 130 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 121 -> 128 -> 123 |
| `7c781f52e78dc0d251df` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 120 -> 127 -> 130 |
| `8bdf0da350d602cbf970` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 119 -> 121 -> 128 |
| `8d10896873df5c62014e` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 21 -> 10 -> 15 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 128 -> 123 -> 122 |
| `972e7afc1f9fcd8bb438` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 119 -> 126 -> 127 |
| `aba3ecf25c2ddde8f28b` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 21 -> 10 -> 86 |
| `e6a74d0120b15ec0f02c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 125 -> 118 -> 117 |
| `f36b4271f8b5e18f5d45` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 21 -> 10 -> 49 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 81 -> 40 -> 59 |
| `20a77143a898bc753a26` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h268 / 8 -> 20 -> 21 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 34 -> 106 -> 40 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 48 -> 14 -> 26 |
| `9e53815c35744add4647` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_103\sa_ep1_103.questphase` / h0 / 81 -> 40 -> 37 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
