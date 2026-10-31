# base-ma-wbr-nok-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\communities\ma_wbr_nok_03.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\communities\ma_wbr_nok_03_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/north_oak/ma_wbr_nok_03/onscreens/ma_wbr_nok_03_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_nok_03`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_03`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_03/description`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_03/ma_wbr_nok_03/go_to_spot`
- `quests/minor_activities/westbrook/north_oak/ma_wbr_nok_03/ma_wbr_nok_03/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 34 -> 66 -> 33 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 24 -> 51 -> 53 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 24 -> 44 -> 45 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h167 / 17 -> 11 -> 9 |
| `fee3756653cd083fb28e` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h167 / 18 -> 17 -> 5 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 17 -> 18 -> 80 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 77 -> 78 -> 34 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 82 -> 77 -> 78 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 78 -> 34 -> 66 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 0 -> 24 -> 51 |
| `19a35d27ae1aaa1f92ef` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 32 -> 19 -> 21 |
| `1d9811f383855222e9bf` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 31 -> 32 -> 19 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 9 -> 67 -> 29 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 74 -> 71 -> 72 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 80 -> 79 -> 78 |
| `2e8b4a64bfc7406e3d35` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 16 -> 47 -> 17 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 11 -> 12 -> 15 |
| `3b5a6e81dfc083dd3d0a` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 56 -> 60 -> 59 |
| `3ba86c71a70bfb0620a5` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 73 -> 74 -> 71 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_03\ma_wbr_nok_03_phase.questphase` / h0 / 79 -> 78 -> 34 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
