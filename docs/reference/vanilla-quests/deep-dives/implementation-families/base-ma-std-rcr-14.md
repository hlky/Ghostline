# base-ma-std-rcr-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\community\ma_std_rcr_14_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\community\ma_std_rcr_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_14/onscreens/ma_std_rcr_14_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 0 -> 50 -> 62 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h50 / 14 -> 7 -> 8 |
| `bff957bf33a10413a685` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 81 -> 80 -> 82 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h50 / 14 -> 7 -> 10 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 101 -> 97 -> 96 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 50 -> 89 -> 75 |
| `13455132e6fe4cc4bf73` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h50 / 14 -> 7 -> 16 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 0 -> 50 -> 89 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 101 -> 100 -> 96 |
| `2e578fd8f85357f1804f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 50 -> 101 -> 98 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 97 -> 96 -> 52 |
| `390915d4be7a3df08eff` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 95 -> 94 -> 85 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 96 -> 52 -> 60 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h238 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h238 / 0 -> 4 -> 1 |
| `479a11033aba2b8c1ef3` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 50 -> 101 -> 97 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 3 -> 4 -> 5 |
| `60faf7d04cb945080042` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h238 / 17 -> 2 -> 3 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h50 / 14 -> 7 -> 9 |
| `69ac42d59aa43099e19c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_14\ma_std_rcr_14_phase.questphase` / h0 / 60 -> 90 -> 76 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
