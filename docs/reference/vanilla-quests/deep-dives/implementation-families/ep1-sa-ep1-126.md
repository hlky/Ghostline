# ep1-sa-ep1-126

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_28`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 34 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 43 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 11 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 64 -> 63 -> 65 |
| `20a77143a898bc753a26` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 8 -> 20 -> 21 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 107 -> 109 -> 94 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 449 -> 450 -> 462 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 435 -> 450 -> 462 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 457 -> 443 -> 442 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 78 -> 24 -> 23 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 451 -> 449 -> 450 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 433 -> 451 -> 449 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 433 -> 441 -> 457 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 21 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h280 / 433 -> 451 -> 435 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 113 -> 107 -> 109 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 55 -> 11 -> 23 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 91 -> 37 -> 56 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_126\sa_ep1_126.questphase` / h0 / 65 -> 89 -> 37 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
