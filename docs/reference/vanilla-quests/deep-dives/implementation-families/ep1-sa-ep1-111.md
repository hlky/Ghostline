# ep1-sa-ep1-111

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111_combat_community.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_22`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 9 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 39 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 46 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 13 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 49 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 17 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 8 -> 20 -> 21 |
| `2e1ee5a1324dbeeb9071` | 13 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 113 -> 112 -> 116 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 101 -> 11 -> 9 |
| `aba3ecf25c2ddde8f28b` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 21 -> 10 -> 88 |
| `f36b4271f8b5e18f5d45` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 21 -> 10 -> 49 |
| `0a3c1367ab5953f38973` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 10 -> 15 -> 89 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 98 -> 100 -> 17 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 88 -> 89 -> 112 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 49 -> 82 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 15 -> 89 -> 112 |
| `8bdf0da350d602cbf970` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 10 -> 49 -> 82 |
| `8d10896873df5c62014e` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 21 -> 10 -> 15 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 82 -> 51 -> 50 |
| `972e7afc1f9fcd8bb438` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 10 -> 88 -> 89 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h333 / 78 -> 24 -> 23 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 90 -> 17 -> 104 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 88 -> 46 -> 55 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 116 -> 115 -> 46 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 54 -> 13 -> 25 |
| `9e53815c35744add4647` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_111\sa_ep1_111.questphase` / h0 / 88 -> 46 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
