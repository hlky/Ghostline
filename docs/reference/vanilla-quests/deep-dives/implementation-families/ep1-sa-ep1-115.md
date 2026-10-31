# ep1-sa-ep1-115

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_16`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 26 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 41 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 8 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 23 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 61 -> 60 -> 62 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 122 -> 123 -> 118 |
| `4c86e9d12122e122fabf` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 97 -> 11 -> 9 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 123 -> 118 -> 137 |
| `593e17bd1c9a456e6bde` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 86 -> 87 -> 99 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 49 -> 82 -> 51 |
| `7c781f52e78dc0d251df` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 15 -> 87 -> 99 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 82 -> 51 -> 50 |
| `0a3c1367ab5953f38973` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 10 -> 15 -> 87 |
| `8bdf0da350d602cbf970` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 10 -> 49 -> 82 |
| `8d10896873df5c62014e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 20 -> 10 -> 15 |
| `972e7afc1f9fcd8bb438` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 10 -> 86 -> 87 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 86 -> 13 -> 25 |
| `aba3ecf25c2ddde8f28b` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 20 -> 10 -> 86 |
| `e6a74d0120b15ec0f02c` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 78 -> 24 -> 23 |
| `f36b4271f8b5e18f5d45` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 20 -> 10 -> 49 |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h238 / 29 -> 28 -> 32 |
| `0847cc3d98df51e47132` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 115 -> 57 -> 88 |
| `17676a0598367dd54c9b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h0 / 127 -> 129 -> 118 |
| `22725fd3b57fe8a30b1b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_115\sa_ep1_115.questphase` / h803 / 4 -> 26 -> 10 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
