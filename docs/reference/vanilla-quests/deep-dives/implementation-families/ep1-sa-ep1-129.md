# ep1-sa-ep1-129

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_31`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_SecondaryWeapon]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 28 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 7 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 5 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 30 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 27 -> 26 -> 36 |
| `20a77143a898bc753a26` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 29 -> 28 -> 32 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 95 -> 11 -> 9 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 155 -> 156 -> 151 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 78 -> 24 -> 23 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 156 -> 151 -> 170 |
| `593e17bd1c9a456e6bde` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 86 -> 87 -> 102 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 49 -> 82 -> 51 |
| `7c781f52e78dc0d251df` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 15 -> 87 -> 102 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 82 -> 51 -> 50 |
| `0a3c1367ab5953f38973` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 10 -> 15 -> 87 |
| `8bdf0da350d602cbf970` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 10 -> 49 -> 82 |
| `8d10896873df5c62014e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 20 -> 10 -> 15 |
| `972e7afc1f9fcd8bb438` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 10 -> 86 -> 87 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 55 -> 11 -> 23 |
| `aba3ecf25c2ddde8f28b` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 20 -> 10 -> 86 |
| `f36b4271f8b5e18f5d45` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h232 / 20 -> 10 -> 49 |
| `0847cc3d98df51e47132` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 147 -> 37 -> 58 |
| `17676a0598367dd54c9b` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 160 -> 162 -> 151 |
| `3c9c316e33d16167acf9` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_129\sa_ep1_129.questphase` / h0 / 166 -> 159 -> 161 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
