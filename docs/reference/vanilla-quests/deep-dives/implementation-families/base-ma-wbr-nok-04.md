# base-ma-wbr-nok-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\community\ma_wbr_nok_04_com_compound.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\community\ma_wbr_nok_04_com_crashsite.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\community\ma_wbr_nok_04_com_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/north_oak/ma_wbr_nok_04/onscreens/ma_wbr_nok_04_email_01`
- `points_of_interest/minor_activities/ma_wbr_nok_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `ef828624d48b06bf49f2` | 5 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 18 -> 34 -> 42 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 29 -> 56 -> 28 |
| `69349634cfd076f0d02b` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 26 -> 27 -> 6 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 18 -> 34 -> 35 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 67 -> 65 -> 26 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 69 -> 66 -> 65 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 66 -> 65 -> 29 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 65 -> 29 -> 56 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 0 -> 18 -> 47 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h98 / 11 -> 5 -> 7 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 4 -> 57 -> 24 |
| `27989a991fbce5b0fc5c` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 34 -> 42 -> 43 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 63 -> 60 -> 61 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 33 -> 5 -> 69 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 69 -> 68 -> 65 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 18 -> 47 -> 51 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 67 -> 65 -> 29 |
| `3ba86c71a70bfb0620a5` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 62 -> 63 -> 60 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 68 -> 65 -> 29 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_04\ma_wbr_nok_04_phase.questphase` / h0 / 66 -> 65 -> 26 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
