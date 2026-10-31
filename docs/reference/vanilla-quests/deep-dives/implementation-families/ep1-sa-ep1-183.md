# ep1-sa-ep1-183

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_82`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 11 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 43 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 15 |
| `questLogicalXorNodeDefinition` | 11 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 9 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 41 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 14 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 106 -> 105 -> 109 |
| `20a77143a898bc753a26` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 168 -> 167 -> 172 |
| `4c86e9d12122e122fabf` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 85 -> 15 -> 83 |
| `593e17bd1c9a456e6bde` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 185 -> 186 -> 198 |
| `5c61b1557cd30faef53c` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 171 -> 186 -> 198 |
| `95098b5ad8804e28c8c4` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 193 -> 179 -> 178 |
| `e6a74d0120b15ec0f02c` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 170 -> 168 -> 167 |
| `ec56186049f4b470a01a` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 187 -> 185 -> 186 |
| `30d6d5448c2b24a092f4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 169 -> 187 -> 185 |
| `8bdf0da350d602cbf970` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 169 -> 177 -> 193 |
| `c9170fb2e5c18a121162` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 21 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h338 / 169 -> 187 -> 171 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 82 -> 83 -> 78 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 83 -> 78 -> 97 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 75 -> 35 -> 45 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 109 -> 108 -> 35 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_183\sa_ep1_183.questphase` / h0 / 37 -> 12 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
