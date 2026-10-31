# base-mq050

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\minor_quests\mq050\mq050.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq050\mq050.quest` | content candidate | 1 / 0 | base\quest\minor_quests\mq050\mq050.questphase |
| `base\quest\minor_quests\mq050\mq050.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene |
| `base\quest\minor_quests\mq050\mq050_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` | content candidate | 0 / 16 |  |

## Journal paths observed in these resources

- `quests/minor_quest/mq050_ken_block_tribute`
- `quests/minor_quest/mq050_ken_block_tribute/mq050_description`
- `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car`
- `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 3 |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForcePhysicsWakeUp_NodeType]` | 2 |
| `questVehicleNodeDefinition[questRepair_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetCanVehicleBeRemoteControlled_NodeType]` | 4 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 6 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 4 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 19 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f50899ee7351d64ed051` | 5 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 26 -> 27 -> 10 |
| `a5f6ff0df46f7043f2b5` | 3 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 36 -> 35 -> 9 |
| `0236274376628b1bf905` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 35 -> 9 -> 13 |
| `21edbf08a25eeafcb062` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 76 -> 77 -> 70 |
| `50a7164e510434acfb41` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 77 -> 70 -> 74 |
| `70d6bfbf84959e7aa5b9` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 70 -> 74 -> 12 |
| `91211ba5c56418b352b6` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 8 -> 36 -> 35 |
| `b657f7f2f003f1ad3883` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 75 -> 76 -> 77 |
| `c637cddf0876303a6557` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 11 -> 8 -> 36 |
| `f02f666e581fbb392116` | 2 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 78 -> 75 -> 76 |
| `01aef8a7bf5ca1c6236a` | 1 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 29 -> 30 -> 43 |
| `072d2b517c1640f6b4a0` | 1 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 40 -> 29 -> 30 |
| `0781ef00ea04c05ee418` | 1 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 23 -> 24 -> 81 |
| `081b254dd90304017f86` | 1 | `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` / scene / 79 -> 52 -> 69 |
| `0c25c88a6ebd18b75c37` | 1 | `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` / scene / 65 -> 15 -> 79 |
| `0eeb0071595e8f50895a` | 1 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 81 -> 87 -> 84 |
| `0fdad4c8a8b4964c866f` | 1 | `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` / scene / 69 -> 17 -> 19 |
| `11d868e716a778724f9f` | 1 | `base\quest\minor_quests\mq050\mq050_bugfixing.questphase` / h14 / 2 -> 4 -> 17 |
| `150a62977587b991a257` | 1 | `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` / scene / 15 -> 79 -> 52 |
| `2a18d536739310eb7e61` | 1 | `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 84 -> 26 -> 27 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
