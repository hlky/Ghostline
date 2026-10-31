# ep1-sa-ep1-187

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_86`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 10 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 35 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 36 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 6 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 168 -> 167 -> 172 |
| `2e1ee5a1324dbeeb9071` | 12 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h0 / 28 -> 25 -> 30 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 118 -> 16 -> 14 |
| `35398687ac04ff110ad0` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 187 -> 171 -> 186 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h0 / 82 -> 83 -> 78 |
| `593e17bd1c9a456e6bde` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 185 -> 186 -> 198 |
| `5c61b1557cd30faef53c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 177 -> 193 -> 179 |
| `7c781f52e78dc0d251df` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 171 -> 186 -> 198 |
| `95098b5ad8804e28c8c4` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 193 -> 179 -> 178 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 170 -> 168 -> 167 |
| `ec56186049f4b470a01a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 187 -> 185 -> 186 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 169 -> 187 -> 185 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 169 -> 177 -> 193 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 173 -> 169 -> 187 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 173 -> 169 -> 177 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h327 / 169 -> 187 -> 171 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h0 / 83 -> 78 -> 97 |
| `de1ad3c25c5260707c77` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h1160 / 38 -> 54 -> 39 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h0 / 37 -> 12 -> 23 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_187\sa_ep1_187.questphase` / h0 / 75 -> 35 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
