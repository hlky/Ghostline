# ep1-sa-ep1-155

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_57`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 9 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 39 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 35 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 44 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 16 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 8 -> 20 -> 21 |
| `2e1ee5a1324dbeeb9071` | 14 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 161 -> 160 -> 164 |
| `4c86e9d12122e122fabf` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 85 -> 15 -> 83 |
| `593e17bd1c9a456e6bde` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 284 -> 285 -> 297 |
| `5c61b1557cd30faef53c` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 270 -> 285 -> 297 |
| `95098b5ad8804e28c8c4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 292 -> 278 -> 277 |
| `ec56186049f4b470a01a` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 286 -> 284 -> 285 |
| `30d6d5448c2b24a092f4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 268 -> 286 -> 284 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 137 -> 138 -> 133 |
| `8bdf0da350d602cbf970` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 268 -> 276 -> 292 |
| `c9170fb2e5c18a121162` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 21 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 78 -> 24 -> 23 |
| `f36b4271f8b5e18f5d45` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h338 / 268 -> 286 -> 270 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 138 -> 133 -> 152 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 128 -> 92 -> 102 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 81 -> 128 -> 92 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_155\sa_ep1_155.questphase` / h0 / 78 -> 64 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
