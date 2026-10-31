# ep1-sa-ep1-112

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_12`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 9 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 35 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 4 -> 3 -> 30 |
| `0a3c1367ab5953f38973` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 25 -> 59 -> 91 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 103 -> 104 -> 99 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 100 -> 16 -> 14 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 90 -> 91 -> 111 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 60 -> 83 -> 62 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 59 -> 91 -> 111 |
| `8bdf0da350d602cbf970` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 30 -> 52 -> 84 |
| `8d10896873df5c62014e` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 23 -> 25 -> 59 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 84 -> 54 -> 53 |
| `972e7afc1f9fcd8bb438` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 25 -> 90 -> 91 |
| `aba3ecf25c2ddde8f28b` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 23 -> 25 -> 90 |
| `f36b4271f8b5e18f5d45` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 23 -> 25 -> 60 |
| `20a77143a898bc753a26` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 29 -> 28 -> 32 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h231 / 78 -> 24 -> 23 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 114 -> 103 -> 104 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 44 -> 13 -> 25 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 95 -> 43 -> 68 |
| `8117af53c31372cf542e` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 30 -> 93 -> 43 |
| `9e53815c35744add4647` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_112\sa_ep1_112.questphase` / h0 / 95 -> 43 -> 41 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
