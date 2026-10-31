# ep1-sa-ep1-209

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` | content candidate | 12 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_209`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 18 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 21 |
| `questEventManagerNodeDefinition` | 30 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 35 |
| `questFlowControlNodeDefinition` | 7 |
| `questInputNodeDefinition` | 18 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 13 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 38 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 18 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 38 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 9 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 30 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h0 / 3 -> 2 -> 22 |
| `20a77143a898bc753a26` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h255 / 114 -> 113 -> 117 |
| `42be946ac78d38ae4123` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 23 -> 30 -> 53 |
| `59ca34c075e76518a325` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 26 -> 46 -> 47 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h0 / 104 -> 106 -> 90 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h255 / 101 -> 11 -> 9 |
| `0a3c1367ab5953f38973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h255 / 121 -> 125 -> 138 |
| `1410f618821ed9c47f01` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 30 -> 59 -> 45 |
| `1fa560baaa4d791a2127` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1458 / 30 -> 29 -> 34 |
| `22b04b1160e0b3e361b7` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1458 / 27 -> 36 -> 30 |
| `2cdc7dbc400acc1f7e09` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 30 -> 53 -> 59 |
| `34734bea267da26f4309` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 64 -> 65 -> 53 |
| `3cb0b0a4fbbf5a758151` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1077 / 36 -> 29 -> 31 |
| `3fc10e65bb55905c4457` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1458 / 29 -> 34 -> 35 |
| `51a42480954b5ab725e6` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1077 / 5 -> 15 -> 16 |
| `52e00b4ce025b0038016` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1458 / 36 -> 30 -> 29 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h255 / 135 -> 136 -> 142 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h255 / 122 -> 133 -> 124 |
| `5c96133f23f1794db973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1077 / 30 -> 36 -> 29 |
| `62b5a9d7951df6c2a048` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_209\sa_ep1_209.questphase` / h1007 / 23 -> 30 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
