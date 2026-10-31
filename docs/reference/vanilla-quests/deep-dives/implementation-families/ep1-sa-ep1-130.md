# ep1-sa-ep1-130

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` | content candidate | 12 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_32`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 21 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 21 |
| `questEventManagerNodeDefinition` | 28 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 7 |
| `questInputNodeDefinition` | 18 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 13 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 17 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 40 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 19 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 35 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 9 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 25 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 11 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h0 / 31 -> 28 -> 33 |
| `42be946ac78d38ae4123` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1020 / 23 -> 30 -> 6 |
| `20a77143a898bc753a26` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 136 -> 135 -> 139 |
| `1410f618821ed9c47f01` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1020 / 30 -> 6 -> 45 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h0 / 102 -> 104 -> 88 |
| `35398687ac04ff110ad0` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 85 -> 15 -> 83 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 121 -> 11 -> 9 |
| `51a42480954b5ab725e6` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1139 / 5 -> 15 -> 16 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 99 -> 100 -> 129 |
| `59ca34c075e76518a325` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1534 / 52 -> 50 -> 55 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 49 -> 112 -> 51 |
| `62b5a9d7951df6c2a048` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1020 / 23 -> 30 -> 45 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 97 -> 100 -> 129 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 161 -> 146 -> 145 |
| `e6c034452fb22e1aa2ae` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1139 / 26 -> 7 -> 2 |
| `ec56186049f4b470a01a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 155 -> 153 -> 154 |
| `1fa560baaa4d791a2127` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1437 / 7 -> 5 -> 25 |
| `20f3923ab22637d7b9bb` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1437 / 8 -> 7 -> 5 |
| `30d6d5448c2b24a092f4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h273 / 36 -> 101 -> 99 |
| `34734bea267da26f4309` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_130\sa_ep1_130.questphase` / h1020 / 46 -> 47 -> 6 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
