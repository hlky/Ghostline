# base-ma-wat-kab-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\communities\ma_wat_kab_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\communities\ma_wat_kab_03_com_worker.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_03/onscreens/ma_wat_kab_03_onscreen_02`
- `points_of_interest/minor_activities/ma_wat_kab_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 34 -> 70 -> 53 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 3 -> 44 -> 45 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 4 -> 3 -> 44 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 84 -> 51 -> 59 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 95 -> 92 -> 91 |
| `1196b65ec43cf9530eeb` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 83 -> 84 -> 51 |
| `11d01d01a3598fe0b256` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 68 -> 69 -> 66 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 4 -> 34 -> 70 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 86 -> 85 -> 83 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 41 -> 42 -> 5 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 34 -> 70 -> 39 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 73 -> 74 -> 75 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 95 -> 94 -> 91 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 40 -> 95 -> 94 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 92 -> 91 -> 33 |
| `39f76984d43788d3b105` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 72 -> 73 -> 75 |
| `3ba86c71a70bfb0620a5` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 72 -> 73 -> 74 |
| `3e212261b77dc5a08d93` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 90 -> 86 -> 85 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 91 -> 33 -> 37 |
| `46832392e10cc5a581d6` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_03\ma_wat_kab_03_phase.questphase` / h0 / 59 -> 61 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
