# ep1-sa-ep1-176

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` | content candidate | 13 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_dynamic_immortality.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_loop_vehicle_damage_check.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_78`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 15 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 21 |
| `questEventManagerNodeDefinition` | 31 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 35 |
| `questFlowControlNodeDefinition` | 7 |
| `questInputNodeDefinition` | 19 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 13 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 38 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 20 |
| `questRandomizerNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 35 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 9 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 15 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h0 / 28 -> 25 -> 30 |
| `1410f618821ed9c47f01` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h1112 / 30 -> 103 -> 102 |
| `42be946ac78d38ae4123` | 9 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h1112 / 23 -> 30 -> 95 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h0 / 102 -> 104 -> 88 |
| `4c86e9d12122e122fabf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 121 -> 11 -> 9 |
| `20a77143a898bc753a26` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 8 -> 20 -> 21 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 268 -> 286 -> 284 |
| `35398687ac04ff110ad0` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 85 -> 15 -> 83 |
| `51a42480954b5ab725e6` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h1181 / 5 -> 15 -> 16 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 284 -> 285 -> 297 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 49 -> 112 -> 51 |
| `62b5a9d7951df6c2a048` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h1112 / 23 -> 30 -> 45 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 270 -> 285 -> 297 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 268 -> 276 -> 292 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 292 -> 278 -> 277 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 21 -> 10 -> 85 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 78 -> 24 -> 23 |
| `e6c034452fb22e1aa2ae` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h1181 / 26 -> 7 -> 28 |
| `ec56186049f4b470a01a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 286 -> 284 -> 285 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_176\sa_ep1_176.questphase` / h326 / 21 -> 10 -> 49 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
