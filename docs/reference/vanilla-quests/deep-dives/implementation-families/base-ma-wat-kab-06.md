# base-ma-wat-kab-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\communities\ma_wat_kab_06.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\communities\ma_wat_kab_06_npc.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\communities\ma_wat_kab_06_smugglers.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_06/onscreens/ma_wat_kab_06_onscreen_01`
- `points_of_interest/minor_activities/ma_wat_kab_06`
- `quests/minor_quest/mq026_conspiracy`
- `quests/minor_quest/mq026_conspiracy/stash/01_01_find_stash`
- `quests/minor_quest/mq026_conspiracy/stash/01_03_loot_corpse`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_AssignSquad,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 17 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1221d0145d6fae0c9b2b` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 83 -> 131 -> 115 |
| `2c20201f171f754c99e0` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 116 -> 117 -> 118 |
| `39f76984d43788d3b105` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 115 -> 116 -> 85 |
| `3ba86c71a70bfb0620a5` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 115 -> 116 -> 117 |
| `bb22066fe4d716a3a642` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 131 -> 115 -> 116 |
| `cd362676c46d8f6c7955` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 131 -> 117 -> 118 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 32 -> 109 -> 68 |
| `20a77143a898bc753a26` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 11 -> 94 -> 95 |
| `4c248e76044b89e90a29` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 131 -> 26 -> 86 |
| `fce35a96110f22bba65e` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 83 -> 131 -> 26 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 150 -> 147 -> 146 |
| `1196b65ec43cf9530eeb` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 113 -> 114 -> 60 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 2 -> 11 -> 94 |
| `19613c7a8c26709b74ad` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 140 -> 38 -> 40 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 2 -> 32 -> 109 |
| `1d4d0120091ddc729836` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 53 -> 52 -> 133 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 133 -> 132 -> 113 |
| `202e7b729f3d8385079e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 141 -> 14 -> 85 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 48 -> 49 -> 64 |
| `215d586765fc154ea611` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_06\ma_wat_kab_06_phase.questphase` / h0 / 2 -> 83 -> 131 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
