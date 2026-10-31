# base-ma-wbr-nok-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\communities\ma_wbr_nok_01_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\communities\ma_wbr_nok_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01/onscreens/ma_wbr_nok_01_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_nok_01`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01/description`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01/ma_wbr_nok_01`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01/ma_wbr_nok_01/go_to_spot`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_01/ma_wbr_nok_01/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 4 -> 74 -> 22 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h247 / 11 -> 4 -> 12 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 50 -> 51 -> 52 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 12 -> 13 -> 80 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 82 -> 76 -> 26 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 83 -> 82 -> 76 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 76 -> 26 -> 75 |
| `1618785f459ae761ab44` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 23 -> 64 -> 6 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 68 -> 69 -> 11 |
| `19a35d27ae1aaa1f92ef` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 28 -> 14 -> 71 |
| `1aa63d67ec6fd9c2fb32` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 7 -> 41 -> 68 |
| `1d9811f383855222e9bf` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 27 -> 28 -> 14 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 4 -> 74 -> 20 |
| `25aae51001db85d5b1fb` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h247 / 4 -> 12 -> 9 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 80 -> 79 -> 76 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 6 -> 70 -> 7 |
| `3df44c2e05455d8969e0` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 49 -> 43 -> 44 |
| `4061ed5f9fcb52c86679` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 65 -> 48 -> 49 |
| `41ac80573b63288ff2f4` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 44 -> 45 -> 46 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_01\ma_wbr_nok_01_phase.questphase` / h0 / 79 -> 76 -> 26 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
