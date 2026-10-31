# ep1-sa-ep1-204

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_108`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 8 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 47 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 9 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 13 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 55 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 17 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 168 -> 167 -> 172 |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h0 / 28 -> 25 -> 30 |
| `35398687ac04ff110ad0` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h0 / 82 -> 83 -> 78 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 121 -> 11 -> 9 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 185 -> 186 -> 198 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 171 -> 186 -> 198 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 193 -> 179 -> 178 |
| `a05aa3e655dc3a79b896` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h1158 / 58 -> 59 -> 66 |
| `d5be13e2c5c0364eca3b` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h1158 / 57 -> 58 -> 59 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 187 -> 185 -> 186 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 169 -> 187 -> 185 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 169 -> 177 -> 193 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 20 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 170 -> 168 -> 167 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 20 -> 10 -> 49 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h335 / 169 -> 187 -> 171 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h0 / 83 -> 78 -> 97 |
| `de3411f47771811a9ec5` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_204\sa_ep1_204.questphase` / h1158 / 25 -> 45 -> 43 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
