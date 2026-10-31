# base-ma-wat-kab-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\community\ma_wat_kab_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\community\ma_wat_kab_01_com_civ.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_01/onscreens/ma_wat_kab_01_onscreen_02`
- `points_of_interest/minor_activities/ma_wat_kab_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `79ff30ab7464b071eda5` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 41 -> 42 -> 43 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 11 -> 44 -> 30 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 21 -> 33 -> 38 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 95 -> 92 -> 91 |
| `08365c0c973ed23713c1` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 86 -> 88 -> 90 |
| `177509bec033f4e05c92` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 66 -> 79 -> 26 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 1 -> 0 -> 35 |
| `1d4d0120091ddc729836` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 21 -> 77 -> 68 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 68 -> 67 -> 65 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 19 -> 20 -> 2 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 11 -> 44 -> 17 |
| `24f561c88cc16114d08b` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 40 -> 41 -> 42 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 95 -> 94 -> 91 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 0 -> 35 -> 15 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 18 -> 95 -> 94 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 92 -> 91 -> 13 |
| `3e212261b77dc5a08d93` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 77 -> 68 -> 67 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h0 / 91 -> 13 -> 16 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h251 / 11 -> 10 -> 5 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_01\ma_wat_kab_01_phase.questphase` / h251 / 0 -> 6 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
