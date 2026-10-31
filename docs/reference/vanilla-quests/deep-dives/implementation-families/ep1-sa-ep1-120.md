# ep1-sa-ep1-120

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` | content candidate | 9 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_21`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 16 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 16 |
| `questEventManagerNodeDefinition` | 22 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questFlowControlNodeDefinition` | 5 |
| `questInputNodeDefinition` | 13 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 7 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 29 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 14 |
| `questRandomizerNodeDefinition` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 26 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 20 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h0 / 27 -> 26 -> 39 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h0 / 102 -> 104 -> 88 |
| `20a77143a898bc753a26` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 8 -> 20 -> 21 |
| `42be946ac78d38ae4123` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h777 / 23 -> 30 -> 68 |
| `59ca34c075e76518a325` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h777 / 26 -> 64 -> 65 |
| `4c86e9d12122e122fabf` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 121 -> 11 -> 9 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h0 / 92 -> 102 -> 104 |
| `1410f618821ed9c47f01` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h777 / 30 -> 73 -> 45 |
| `1fa560baaa4d791a2127` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h1259 / 30 -> 29 -> 31 |
| `22b04b1160e0b3e361b7` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h1259 / 0 -> 27 -> 7 |
| `2cdc7dbc400acc1f7e09` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h777 / 30 -> 68 -> 73 |
| `30d6d5448c2b24a092f4` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 202 -> 220 -> 218 |
| `34734bea267da26f4309` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h777 / 78 -> 79 -> 68 |
| `35398687ac04ff110ad0` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 85 -> 15 -> 83 |
| `3cb0b0a4fbbf5a758151` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h847 / 36 -> 37 -> 38 |
| `3fc10e65bb55905c4457` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h1259 / 5 -> 25 -> 26 |
| `51a42480954b5ab725e6` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h847 / 5 -> 15 -> 16 |
| `52e00b4ce025b0038016` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h1259 / 27 -> 30 -> 29 |
| `593e17bd1c9a456e6bde` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 218 -> 219 -> 231 |
| `5c61b1557cd30faef53c` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_120\sa_ep1_120.questphase` / h227 / 49 -> 112 -> 51 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
