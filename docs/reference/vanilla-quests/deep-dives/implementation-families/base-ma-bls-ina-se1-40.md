# base-ma-bls-ina-se1-40

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_40/onscreens/ma_bls_ina_se1_40_onscreen_01`
- `points_of_interest/minor_quests/mq046_cave_vehicle`
- `quests/minor_quest/mq046_cave_vehicle`
- `quests/minor_quest/mq046_cave_vehicle/mq046_container/get_inside_car`
- `quests/minor_quest/mq046_cave_vehicle/mq046_container/investigate`
- `quests/minor_quest/mq046_cave_vehicle/mq046_desc`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questStatsCondition,questStreetCredTier_ConditionType,questUniversalRef]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 8 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f50899ee7351d64ed051` | 5 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 80 -> 81 -> 42 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 2 -> 20 -> 11 |
| `1a1ebf1d736ae3feaa64` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 32 -> 36 -> 37 |
| `01aef8a7bf5ca1c6236a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 88 -> 89 -> 87 |
| `0236274376628b1bf905` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 102 -> 41 -> 46 |
| `05da58ffa41a47aeb533` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 112 -> 75 -> 76 |
| `072d2b517c1640f6b4a0` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 117 -> 88 -> 89 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 4 -> 8 -> 1 |
| `2252a132cf17333b3476` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 3 -> 4 -> 8 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 2 -> 20 -> 6 |
| `313f1b6d65d6d4b38ebe` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 89 -> 87 -> 1 |
| `34501bbf9fd86720979f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 120 -> 119 -> 117 |
| `34b48742c4257a2c4ed9` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 7 -> 3 -> 10 |
| `3b64c83a3256f94318cd` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 46 -> 74 -> 45 |
| `3bc58cd9dee0aa510d26` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 45 -> 67 -> 68 |
| `3c2d3d76cbc21af939f6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 0 -> 30 -> 31 |
| `4581d020e90cab36873b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 37 -> 44 -> 39 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 20 -> 11 -> 6 |
| `4d6a34d4f440a16559f5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 6 -> 7 -> 3 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_40\ma_bls_ina_se1_40_phase.questphase` / h0 / 20 -> 6 -> 7 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
