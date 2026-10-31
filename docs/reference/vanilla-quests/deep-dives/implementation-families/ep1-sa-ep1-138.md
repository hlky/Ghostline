# ep1-sa-ep1-138

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` | content candidate | 10 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_40`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 18 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 18 |
| `questEventManagerNodeDefinition` | 31 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 35 |
| `questFlowControlNodeDefinition` | 7 |
| `questInputNodeDefinition` | 16 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 13 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 32 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 17 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 36 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 9 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 18 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h0 / 29 -> 26 -> 31 |
| `20a77143a898bc753a26` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 135 -> 134 -> 139 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h0 / 79 -> 83 -> 84 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 121 -> 11 -> 9 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 41 -> 106 -> 104 |
| `35398687ac04ff110ad0` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 106 -> 102 -> 105 |
| `3cb0b0a4fbbf5a758151` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1156 / 28 -> 34 -> 35 |
| `51a42480954b5ab725e6` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1156 / 5 -> 15 -> 16 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 104 -> 105 -> 128 |
| `59ca34c075e76518a325` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1096 / 66 -> 64 -> 69 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 49 -> 112 -> 51 |
| `5c96133f23f1794db973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1156 / 11 -> 28 -> 34 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 102 -> 105 -> 128 |
| `86206bcc5a5682b9448a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1156 / 27 -> 38 -> 40 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 136 -> 143 -> 159 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 159 -> 145 -> 144 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 20 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 137 -> 135 -> 134 |
| `e6c034452fb22e1aa2ae` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h1156 / 26 -> 7 -> 2 |
| `ec56186049f4b470a01a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_138\sa_ep1_138.questphase` / h326 / 106 -> 104 -> 105 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
