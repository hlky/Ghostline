# ep1-sa-ep1-168

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_70`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 40 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 49 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 16 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 8 -> 20 -> 21 |
| `2e1ee5a1324dbeeb9071` | 11 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h0 / 28 -> 25 -> 30 |
| `4c86e9d12122e122fabf` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 121 -> 11 -> 9 |
| `de3411f47771811a9ec5` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h1034 / 24 -> 39 -> 37 |
| `e6a74d0120b15ec0f02c` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 236 -> 234 -> 233 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h0 / 98 -> 100 -> 85 |
| `a05aa3e655dc3a79b896` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h1034 / 61 -> 62 -> 77 |
| `d5be13e2c5c0364eca3b` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h1034 / 60 -> 61 -> 62 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 251 -> 252 -> 264 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 237 -> 252 -> 264 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 259 -> 245 -> 244 |
| `ec56186049f4b470a01a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 253 -> 251 -> 252 |
| `30d6d5448c2b24a092f4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 235 -> 253 -> 251 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h0 / 90 -> 85 -> 104 |
| `8bdf0da350d602cbf970` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 235 -> 243 -> 259 |
| `c9170fb2e5c18a121162` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 21 -> 10 -> 85 |
| `f36b4271f8b5e18f5d45` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_168\sa_ep1_168.questphase` / h327 / 235 -> 253 -> 237 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
