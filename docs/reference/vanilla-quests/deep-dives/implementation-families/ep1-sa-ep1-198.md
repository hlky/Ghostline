# ep1-sa-ep1-198

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_100`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition` | 12 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 28 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 30 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 8 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 31 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h0 / 27 -> 26 -> 31 |
| `20a77143a898bc753a26` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 300 -> 299 -> 304 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h0 / 82 -> 83 -> 78 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 118 -> 16 -> 14 |
| `3406cae6ba1ac9d4e144` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h1113 / 13 -> 69 -> 37 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h0 / 83 -> 78 -> 97 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 309 -> 325 -> 311 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 325 -> 311 -> 310 |
| `e6a74d0120b15ec0f02c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 302 -> 300 -> 299 |
| `2d298b805ff1e7433a38` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h837 / 10 -> 11 -> 22 |
| `30d6d5448c2b24a092f4` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 301 -> 319 -> 317 |
| `35398687ac04ff110ad0` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 319 -> 303 -> 318 |
| `593e17bd1c9a456e6bde` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 317 -> 318 -> 330 |
| `7c781f52e78dc0d251df` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 303 -> 318 -> 330 |
| `8bdf0da350d602cbf970` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 301 -> 309 -> 325 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h0 / 37 -> 12 -> 23 |
| `c9170fb2e5c18a121162` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 305 -> 301 -> 319 |
| `ec56186049f4b470a01a` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 319 -> 317 -> 318 |
| `f36b4271f8b5e18f5d45` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 305 -> 301 -> 309 |
| `fe740361380ffc128c81` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_198\sa_ep1_198.questphase` / h244 / 301 -> 319 -> 303 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
