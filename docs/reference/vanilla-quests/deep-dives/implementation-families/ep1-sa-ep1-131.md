# ep1-sa-ep1-131

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_33`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 39 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 44 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 37 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 133 -> 132 -> 136 |
| `20a77143a898bc753a26` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 135 -> 134 -> 139 |
| `4c86e9d12122e122fabf` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 121 -> 11 -> 9 |
| `30d6d5448c2b24a092f4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 136 -> 154 -> 152 |
| `35398687ac04ff110ad0` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 154 -> 138 -> 153 |
| `593e17bd1c9a456e6bde` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 152 -> 153 -> 165 |
| `5c61b1557cd30faef53c` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 138 -> 153 -> 165 |
| `8bdf0da350d602cbf970` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 136 -> 144 -> 160 |
| `95098b5ad8804e28c8c4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 160 -> 146 -> 145 |
| `c9170fb2e5c18a121162` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 21 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 137 -> 135 -> 134 |
| `ec56186049f4b470a01a` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 154 -> 152 -> 153 |
| `f36b4271f8b5e18f5d45` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h338 / 136 -> 154 -> 138 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 108 -> 109 -> 104 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 109 -> 104 -> 123 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 100 -> 39 -> 49 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 34 -> 100 -> 39 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_131\sa_ep1_131.questphase` / h0 / 41 -> 14 -> 25 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
