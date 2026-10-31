# ep1-sa-ep1-118

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` | content candidate | 4 / 0 | ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_intro_cleanup_check.questphase; ep1\openworld\sandbox_activities\courier_spot\introduction_quest\sa_ep1_courier_introduction_spot_logic.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_19`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 9 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_SecondaryWeapon]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 30 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 14 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 30 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 141 -> 140 -> 144 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 116 -> 117 -> 112 |
| `0a3c1367ab5953f38973` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 131 -> 132 -> 140 |
| `4c86e9d12122e122fabf` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 97 -> 11 -> 9 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 139 -> 140 -> 142 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 133 -> 138 -> 135 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 132 -> 140 -> 142 |
| `8d10896873df5c62014e` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 21 -> 10 -> 15 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 138 -> 135 -> 134 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 137 -> 130 -> 129 |
| `20a77143a898bc753a26` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 8 -> 20 -> 21 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 117 -> 112 -> 131 |
| `8bdf0da350d602cbf970` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 131 -> 133 -> 138 |
| `972e7afc1f9fcd8bb438` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 131 -> 139 -> 140 |
| `aba3ecf25c2ddde8f28b` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 21 -> 10 -> 86 |
| `f36b4271f8b5e18f5d45` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h249 / 21 -> 10 -> 49 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 79 -> 13 -> 25 |
| `d2905bd38d9fe6a52800` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 3 -> 58 -> 62 |
| `0847cc3d98df51e47132` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h0 / 107 -> 61 -> 81 |
| `7b44344c01ad5161d3ff` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_118\sa_ep1_118.questphase` / h819 / 80 -> 74 -> 63 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
