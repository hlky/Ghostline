# base-mq044

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq044\mq044_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq044\comunities\mq044_quest_vehicle.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq044\comunities\mq044_scavs.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq044\comunities\mq044_workers.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq044\mq044.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq044\mq044.quest` | content candidate | 1 / 0 | base\quest\minor_quests\mq044\phases\mq044.questphase |
| `base\quest\minor_quests\mq044\phases\mq044.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq044\phases\mq044_main.questphase |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `contacts/jake_estevez/mq044/debrief`
- `contacts/jake_estevez/mq044/vehicle`
- `contacts/muamar_el_capitan_reyes/mq044/debrief`
- `contacts/muamar_el_capitan_reyes/mq044/vehicle_info`
- `quests/minor_quest/mq044_jakes_vehicle`
- `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage`
- `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage/brief`
- `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car`
- `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/04_leave_area`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 11 |
| `questInputNodeDefinition` | 11 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 16 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 8 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2d61756ead564fdbaa1f` | 2 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h14 / 48 -> 65 -> 64 |
| `7c4dc126c0905525e7f8` | 2 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h14 / 48 -> 65 -> 47 |
| `7e7dbbc930b3717fd790` | 2 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 10 -> 8 -> 11 |
| `80c436c3f41257230312` | 2 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 7 -> 6 -> 10 |
| `b96dfb35271b09a85825` | 2 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 7 -> 6 -> 9 |
| `bf30f8ccc3b1e052921e` | 2 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h231 / 26 -> 21 -> 39 |
| `c8705a8da51824b73252` | 2 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 5 |
| `0432d866cd213edc1e99` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h14 / 65 -> 64 -> 42 |
| `086411c97d02f439ba7e` | 1 | `base\quest\minor_quests\mq044\phases\mq044.questphase` / h0 / 4 -> 2 -> 1 |
| `0ae0c4c8f4de2e085375` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 7 -> 4 -> 3 |
| `0b1d0ba8f59ded166064` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 4 -> 3 -> 8 |
| `175232f3c06d599235ca` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 8 -> 9 -> 1 |
| `1a3d0ec08c9c011c8d4e` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 3 -> 8 -> 9 |
| `1babdc0b5a7b4ffc9377` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h231 / 28 -> 27 -> 21 |
| `223048580b7b66384a57` | 1 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 6 -> 10 -> 8 |
| `237687944a84dd96b7b5` | 1 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h130 / 0 -> 3 -> 7 |
| `23ae0d4630e5c2a0331c` | 1 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 8 -> 11 -> 1 |
| `2ba36a4d242febe076b4` | 1 | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h130 / 2 -> 4 -> 5 |
| `2cb6a780f07f49d4270b` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h14 / 37 -> 38 -> 1 |
| `31f9c50ec95457335977` | 1 | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h231 / 2 -> 12 -> 17 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
