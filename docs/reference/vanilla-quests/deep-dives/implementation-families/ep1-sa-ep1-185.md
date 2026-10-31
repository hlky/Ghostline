# ep1-sa-ep1-185

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_84`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 10 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 44 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questGatherTriggerCondition,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 15 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 24 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 50 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 3 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 4 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 9 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 22 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 168 -> 167 -> 172 |
| `2e1ee5a1324dbeeb9071` | 14 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h0 / 61 -> 60 -> 81 |
| `20e74db83226e46cc202` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 100 -> 101 -> 34 |
| `6bade9a6171d604fd6d8` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 101 -> 34 -> 37 |
| `7214221ab5d271ce1333` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 100 -> 101 -> 37 |
| `7b44344c01ad5161d3ff` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 35 -> 34 -> 37 |
| `42d456f68cbe3d8345c3` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 34 -> 37 -> 36 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 121 -> 11 -> 9 |
| `56c53a847765e20a971f` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h1157 / 101 -> 37 -> 36 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 85 -> 15 -> 83 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h0 / 140 -> 141 -> 136 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 185 -> 186 -> 198 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 49 -> 112 -> 51 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 171 -> 186 -> 198 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 193 -> 179 -> 178 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 170 -> 168 -> 167 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 187 -> 185 -> 186 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 169 -> 187 -> 185 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 169 -> 177 -> 193 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_185\sa_ep1_185.questphase` / h327 / 21 -> 10 -> 85 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
