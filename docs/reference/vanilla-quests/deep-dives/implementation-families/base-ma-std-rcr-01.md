# base-ma-std-rcr-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\community\ma_std_rcr_01_civilians_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\community\ma_std_rcr_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_01/onscreens/ma_std_rcr_01_onscreen_03`
- `points_of_interest/minor_activities/ma_std_rcr_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 1 -> 90 -> 96 |
| `178360ac35259ce804ee` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 1 -> 83 -> 47 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h126 / 20 -> 6 -> 11 |
| `c3a8b811b8c7c7ee308f` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 83 -> 115 -> 116 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h126 / 20 -> 6 -> 13 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 49 -> 50 -> 114 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 90 -> 124 -> 107 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h126 / 6 -> 17 -> 18 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 94 -> 125 -> 2 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 1 -> 90 -> 124 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 90 -> 124 -> 130 |
| `27989a991fbce5b0fc5c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 113 -> 82 -> 92 |
| `27aa719598304363c84e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 130 -> 129 -> 133 |
| `37a0764f953c91e596dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 129 -> 133 -> 97 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 133 -> 81 -> 94 |
| `4139243029a8673a5ce0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 1 -> 83 -> 110 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h297 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h297 / 0 -> 4 -> 1 |
| `4522103ef86d4d94d84a` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 83 -> 110 -> 113 |
| `48ef5781867fbe61b8b0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_01\ma_std_rcr_01_phase.questphase` / h0 / 128 -> 133 -> 81 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
