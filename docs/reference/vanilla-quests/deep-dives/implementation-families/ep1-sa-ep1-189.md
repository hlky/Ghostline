# ep1-sa-ep1-189

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_88`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition` | 18 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 37 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 39 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 42 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6c02e94c30ce1078be32` | 36 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h1161 / 36 -> 80 -> 81 |
| `20a77143a898bc753a26` | 14 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 168 -> 167 -> 172 |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h0 / 28 -> 25 -> 30 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 121 -> 11 -> 9 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h0 / 82 -> 83 -> 78 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 185 -> 186 -> 198 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 171 -> 186 -> 198 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 193 -> 179 -> 178 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 170 -> 168 -> 167 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 187 -> 185 -> 186 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 169 -> 187 -> 185 |
| `39b72397ccc95032470d` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h1161 / 4 -> 35 -> 36 |
| `578f127ea08598833e6a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h1161 / 34 -> 35 -> 36 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 169 -> 177 -> 193 |
| `9ca89b2eecc2e9859a5d` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h1161 / 33 -> 35 -> 36 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 21 -> 10 -> 85 |
| `f2e8e66d552068335e40` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h1161 / 84 -> 100 -> 85 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_189\sa_ep1_189.questphase` / h327 / 21 -> 10 -> 49 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
