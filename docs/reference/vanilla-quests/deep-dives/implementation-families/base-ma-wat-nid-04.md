# base-ma-wat-nid-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\community\ma_wat_nid_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\community\ma_wat_nid_04_com_civ.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_04/onscreens/ma_wat_nid_04_worker`
- `points_of_interest/minor_activities/ma_wat_nid_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 6 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 1 -> 0 -> 65 |
| `04d78f5a272f905e31eb` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 13 -> 69 -> 70 |
| `05368f97c1887d1ef26f` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 99 -> 102 -> 104 |
| `2c20201f171f754c99e0` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 104 -> 103 -> 100 |
| `344a9bb49243e19907c3` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 69 -> 70 -> 72 |
| `3ba86c71a70bfb0620a5` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 102 -> 104 -> 103 |
| `9897663e481a588474c9` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 99 -> 103 -> 100 |
| `f2dd7997ee02125b02f0` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 69 -> 70 -> 73 |
| `f40c0fde6733ba7a3317` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 69 -> 70 -> 74 |
| `bff957bf33a10413a685` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 14 -> 15 -> 16 |
| `02d878a28a675e881f96` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 113 -> 111 -> 12 |
| `45a0059a97ab5b10fb49` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 112 -> 111 -> 12 |
| `9607ff9432ed294370d1` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 114 -> 111 -> 12 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 10 -> 66 -> 60 |
| `50c0101882435d977f36` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 29 -> 110 -> 51 |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 65 -> 2 -> 5 |
| `dceacff78dfb78406240` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 29 -> 110 -> 30 |
| `e7e76532ca5105db2460` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 29 -> 110 -> 35 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 115 -> 112 -> 111 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase` / h0 / 112 -> 111 -> 62 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
