# ep1-sa-ep1-199

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` | content candidate | 13 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_101`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 24 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 21 |
| `questEventManagerNodeDefinition` | 31 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 35 |
| `questFlowControlNodeDefinition` | 7 |
| `questInputNodeDefinition` | 19 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 13 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 41 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 20 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 35 |
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
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h0 / 28 -> 25 -> 30 |
| `42be946ac78d38ae4123` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1090 / 23 -> 30 -> 126 |
| `1410f618821ed9c47f01` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1090 / 30 -> 131 -> 45 |
| `59ca34c075e76518a325` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1090 / 127 -> 125 -> 130 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h0 / 78 -> 82 -> 83 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 121 -> 11 -> 9 |
| `f36b4271f8b5e18f5d45` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 20 -> 10 -> 49 |
| `1fa560baaa4d791a2127` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1567 / 17 -> 16 -> 25 |
| `20a77143a898bc753a26` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 397 -> 396 -> 401 |
| `20f3923ab22637d7b9bb` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1567 / 22 -> 17 -> 16 |
| `22b04b1160e0b3e361b7` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1567 / 0 -> 18 -> 17 |
| `2cdc7dbc400acc1f7e09` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1090 / 30 -> 126 -> 131 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 398 -> 415 -> 413 |
| `34734bea267da26f4309` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1090 / 139 -> 140 -> 126 |
| `35398687ac04ff110ad0` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 85 -> 15 -> 83 |
| `3cb0b0a4fbbf5a758151` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1162 / 36 -> 47 -> 48 |
| `3fc10e65bb55905c4457` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1567 / 16 -> 25 -> 26 |
| `51a42480954b5ab725e6` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1162 / 5 -> 15 -> 16 |
| `52e00b4ce025b0038016` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h1567 / 18 -> 17 -> 16 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_199\sa_ep1_199.questphase` / h326 / 413 -> 414 -> 426 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
