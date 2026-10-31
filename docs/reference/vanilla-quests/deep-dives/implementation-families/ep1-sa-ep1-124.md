# ep1-sa-ep1-124

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_26`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 14 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 34 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 13 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 21 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 42 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 16 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 8 -> 20 -> 21 |
| `2e1ee5a1324dbeeb9071` | 13 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h0 / 105 -> 104 -> 122 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h0 / 83 -> 102 -> 87 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 349 -> 350 -> 362 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 335 -> 350 -> 362 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 78 -> 24 -> 23 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 351 -> 349 -> 350 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 333 -> 351 -> 349 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 49 -> 112 -> 51 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 333 -> 341 -> 357 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 357 -> 343 -> 342 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 21 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h291 / 333 -> 351 -> 335 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h0 / 88 -> 83 -> 102 |
| `7b44344c01ad5161d3ff` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h1497 / 32 -> 10 -> 11 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h0 / 111 -> 37 -> 57 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_124\sa_ep1_124.questphase` / h0 / 55 -> 11 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
