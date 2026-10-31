# ep1-sa-ep1-139

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` | content candidate | 6 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_41`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 35 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 10 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 113 -> 112 -> 116 |
| `20a77143a898bc753a26` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 167 -> 166 -> 171 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 106 -> 102 -> 105 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 84 -> 85 -> 80 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 104 -> 105 -> 128 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 102 -> 105 -> 128 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 191 -> 177 -> 176 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 169 -> 167 -> 166 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 106 -> 104 -> 105 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 41 -> 106 -> 104 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 168 -> 175 -> 191 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 20 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 20 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h341 / 41 -> 106 -> 102 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 85 -> 80 -> 99 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 74 -> 37 -> 47 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 116 -> 115 -> 37 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_139\sa_ep1_139.questphase` / h0 / 39 -> 12 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
