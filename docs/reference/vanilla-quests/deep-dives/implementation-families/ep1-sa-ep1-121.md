# ep1-sa-ep1-121

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_23`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 34 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 43 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 11 |
| `questMovePuppetNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 11 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h0 / 69 -> 68 -> 71 |
| `20a77143a898bc753a26` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 167 -> 166 -> 171 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 121 -> 11 -> 9 |
| `c9170fb2e5c18a121162` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 21 -> 10 -> 85 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 106 -> 102 -> 105 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h0 / 104 -> 105 -> 100 |
| `42d456f68cbe3d8345c3` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h1303 / 10 -> 11 -> 12 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 104 -> 105 -> 128 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 49 -> 112 -> 51 |
| `7b44344c01ad5161d3ff` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h1303 / 9 -> 10 -> 11 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 102 -> 105 -> 128 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 192 -> 178 -> 177 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 169 -> 167 -> 166 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 106 -> 104 -> 105 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 41 -> 106 -> 104 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 168 -> 176 -> 192 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h280 / 41 -> 106 -> 102 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h0 / 105 -> 100 -> 119 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_121\sa_ep1_121.questphase` / h0 / 58 -> 11 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
