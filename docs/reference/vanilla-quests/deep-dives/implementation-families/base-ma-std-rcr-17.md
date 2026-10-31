# base-ma-std-rcr-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\community\ma_std_rcr_17_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\community\ma_std_rcr_17_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_17/onscreens/ma_std_rcr_17_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_17`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 1 -> 12 -> 19 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h39 / 11 -> 8 -> 4 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 1 -> 32 -> 33 |
| `9f3dfa03c86adea5087f` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 46 -> 14 -> 20 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h39 / 11 -> 8 -> 3 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 50 -> 47 -> 46 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 12 -> 36 -> 30 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 17 -> 37 -> 2 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 1 -> 12 -> 36 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 50 -> 49 -> 46 |
| `2e578fd8f85357f1804f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 12 -> 50 -> 48 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 47 -> 46 -> 14 |
| `3492bc562b5f107175fd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_bugfixing.questphase` / h10 / 7 -> 9 -> 10 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 46 -> 14 -> 17 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h218 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h218 / 0 -> 4 -> 1 |
| `479a11033aba2b8c1ef3` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 12 -> 50 -> 47 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h0 / 9 -> 3 -> 7 |
| `5410098bc97efa377076` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_bugfixing.questphase` / h10 / 2 -> 4 -> 6 |
| `60faf7d04cb945080042` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_17\ma_std_rcr_17_phase.questphase` / h218 / 17 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
