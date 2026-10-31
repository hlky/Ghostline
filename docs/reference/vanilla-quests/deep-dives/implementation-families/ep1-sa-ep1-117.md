# ep1-sa-ep1-117

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_18`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition` | 18 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 28 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 41 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 8 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMiscAICommandNode` | 6 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 6 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 8 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 30 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 8 -> 20 -> 21 |
| `2e1ee5a1324dbeeb9071` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h0 / 4 -> 3 -> 29 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h0 / 115 -> 116 -> 111 |
| `3406cae6ba1ac9d4e144` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h1051 / 13 -> 69 -> 37 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 96 -> 11 -> 9 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h0 / 116 -> 111 -> 130 |
| `5c61b1557cd30faef53c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 49 -> 83 -> 51 |
| `95098b5ad8804e28c8c4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 83 -> 51 -> 50 |
| `e6a74d0120b15ec0f02c` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 78 -> 24 -> 23 |
| `0a3c1367ab5953f38973` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 10 -> 15 -> 88 |
| `593e17bd1c9a456e6bde` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 87 -> 88 -> 103 |
| `7c781f52e78dc0d251df` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 15 -> 88 -> 103 |
| `8bdf0da350d602cbf970` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 10 -> 49 -> 83 |
| `8d10896873df5c62014e` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 21 -> 10 -> 15 |
| `972e7afc1f9fcd8bb438` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 10 -> 87 -> 88 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h0 / 79 -> 13 -> 25 |
| `aba3ecf25c2ddde8f28b` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 21 -> 10 -> 87 |
| `f36b4271f8b5e18f5d45` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h238 / 21 -> 10 -> 49 |
| `0847cc3d98df51e47132` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h0 / 106 -> 61 -> 81 |
| `115d8a1b79379ecc48b1` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_117\sa_ep1_117.questphase` / h815 / 30 -> 48 -> 49 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
