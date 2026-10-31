# ep1-sa-ep1-144

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` | content candidate | 7 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_46`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerCombat_SetDeathDirection]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 9 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 11 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 40 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questFlowControlNodeDefinition` | 3 |
| `questInputNodeDefinition` | 11 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 12 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 9 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 40 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 3 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 105 -> 104 -> 108 |
| `20a77143a898bc753a26` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 135 -> 134 -> 139 |
| `4c86e9d12122e122fabf` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 121 -> 11 -> 9 |
| `30d6d5448c2b24a092f4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 41 -> 106 -> 104 |
| `35398687ac04ff110ad0` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 106 -> 102 -> 105 |
| `593e17bd1c9a456e6bde` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 104 -> 105 -> 128 |
| `7c781f52e78dc0d251df` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 102 -> 105 -> 128 |
| `95098b5ad8804e28c8c4` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 160 -> 146 -> 145 |
| `c9170fb2e5c18a121162` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 21 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 137 -> 135 -> 134 |
| `ec56186049f4b470a01a` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 106 -> 104 -> 105 |
| `f36b4271f8b5e18f5d45` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 21 -> 10 -> 49 |
| `fe740361380ffc128c81` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 41 -> 106 -> 102 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 84 -> 85 -> 80 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 49 -> 112 -> 51 |
| `8bdf0da350d602cbf970` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h336 / 136 -> 144 -> 160 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 85 -> 80 -> 99 |
| `0847cc3d98df51e47132` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 76 -> 37 -> 47 |
| `8117af53c31372cf542e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 108 -> 107 -> 37 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_144\sa_ep1_144.questphase` / h0 / 39 -> 12 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
