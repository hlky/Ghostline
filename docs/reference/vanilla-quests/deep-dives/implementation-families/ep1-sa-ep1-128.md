# ep1-sa-ep1-128

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_30`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 12 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 42 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 44 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 11 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 16 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 9 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 46 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 16 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 123 -> 122 -> 126 |
| `20a77143a898bc753a26` | 14 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 8 -> 20 -> 21 |
| `4c86e9d12122e122fabf` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 121 -> 11 -> 9 |
| `593e17bd1c9a456e6bde` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 383 -> 384 -> 396 |
| `5c61b1557cd30faef53c` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 369 -> 384 -> 396 |
| `95098b5ad8804e28c8c4` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 391 -> 377 -> 376 |
| `e6a74d0120b15ec0f02c` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 78 -> 24 -> 23 |
| `35398687ac04ff110ad0` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 85 -> 15 -> 83 |
| `8bdf0da350d602cbf970` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 367 -> 375 -> 391 |
| `ec56186049f4b470a01a` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 385 -> 383 -> 384 |
| `f36b4271f8b5e18f5d45` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 21 -> 10 -> 49 |
| `30d6d5448c2b24a092f4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 367 -> 385 -> 383 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 99 -> 100 -> 95 |
| `c9170fb2e5c18a121162` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 21 -> 10 -> 85 |
| `fe740361380ffc128c81` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h283 / 367 -> 385 -> 369 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 114 -> 108 -> 110 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 89 -> 37 -> 56 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 126 -> 125 -> 37 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_128\sa_ep1_128.questphase` / h0 / 55 -> 11 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
