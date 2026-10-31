# ep1-sa-ep1-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_03\community\sa_ep1_03_combat_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\courier_spot\courier_spot.questphase; ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase; ep1\openworld\sandbox_activities\sa_ep1_03\scenes\sa_ep1_03_chicken_test.scene |
| `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` | content candidate | 6 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_03\scenes\sa_ep1_03_chicken_test.scene` | test/debug | 0 / 4 |  |

## Journal paths observed in these resources

- `ep1/quests/sandbox_activities/sa_ep1_03`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/convey`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/eliminate_enemies`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/find_shard`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/get_into`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/get_out`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/go_to_parking`
- `ep1/quests/sandbox_activities/sa_ep1_03/sa_ep1_03/if_fail`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 26 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questDestruction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 7 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `808c42396a9735fe3a65` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 0 -> 2 -> 20 |
| `1df95a39b365f9f60e15` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 113 -> 114 -> 115 |
| `3b6a1bfe5272b3ca2c22` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 113 -> 115 -> 116 |
| `d30dec206567a53c3ede` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 3 -> 28 -> 48 |
| `dbbeb65ae81a06c8c460` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 114 -> 115 -> 116 |
| `2be296de9cd6ded33fbd` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 114 -> 115 -> 117 |
| `33bea240e50436a67941` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 6 -> 12 -> 14 |
| `480a010388ce3a487ffb` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 8 -> 11 -> 4 |
| `4ff3abfc2e95448213b9` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 23 -> 16 -> 18 |
| `6e2d70f713e339a6c137` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 12 -> 14 -> 29 |
| `a36102ceee6fef729c5f` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 9 -> 11 -> 4 |
| `abbf46d00a7c0ae464b9` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 113 -> 115 -> 117 |
| `b2c8497272de963cb50b` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 7 -> 12 -> 14 |
| `d8ef39870626a261efb0` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 10 -> 11 -> 4 |
| `0e147d9e68a4074ab8c6` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 25 -> 24 -> 26 |
| `4757508be048eca14a5f` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 4 -> 27 -> 39 |
| `5db090327cb2f56e5c66` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h27 / 23 -> 25 -> 24 |
| `045316bbf4dc2ccf8aca` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 17 -> 19 -> 24 |
| `0ae3f096e347e308a9c4` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 28 -> 30 -> 31 |
| `146d03d186468f0e231d` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_03\sa_ep1_03.questphase` / h891 / 16 -> 18 -> 24 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
