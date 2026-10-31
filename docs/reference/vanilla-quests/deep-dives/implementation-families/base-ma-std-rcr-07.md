# base-ma-std-rcr-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\community\ma_std_rcr_07_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\community\ma_std_rcr_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` | content candidate | 3 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\phases\ma_std_rcr_07_bugfixing.questphase` | repair | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_07/onscreens/ma_std_rcr_07_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 4 -> 0 -> 1 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h48 / 10 -> 6 -> 5 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h48 / 10 -> 6 -> 8 |
| `0dc09c13342eae2c9896` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\phases\ma_std_rcr_07_bugfixing.questphase` / h0 / 5 -> 8 -> 7 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 25 -> 41 -> 9 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h48 / 10 -> 6 -> 7 |
| `27aa719598304363c84e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 45 -> 47 -> 44 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\phases\ma_std_rcr_07_bugfixing.questphase` / h0 / 7 -> 6 -> 1 |
| `37a0764f953c91e596dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 47 -> 44 -> 28 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 44 -> 16 -> 25 |
| `414179f27318cfb189d5` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 14 -> 40 -> 33 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h210 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h210 / 0 -> 4 -> 1 |
| `48ef5781867fbe61b8b0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 43 -> 44 -> 16 |
| `4c603d486c6ba569afa7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 40 -> 45 -> 47 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 40 -> 33 -> 45 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 1 -> 5 -> 7 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 33 -> 45 -> 43 |
| `5506424829d3f5f3a244` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h0 / 4 -> 14 -> 27 |
| `60faf7d04cb945080042` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_07\ma_std_rcr_07_phase.questphase` / h210 / 17 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
