# base-ma-std-rcr-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\community\ma_std_rcr_04_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\community\ma_std_rcr_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_04/onscreens/ma_std_rcr_04_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEventManagerNodeDefinition` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 2 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 0 -> 37 -> 38 |
| `d864a6aee629e2bd85fa` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 95 -> 97 -> 100 |
| `e2f4a84af8e0c503880f` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 37 -> 95 -> 96 |
| `5506424829d3f5f3a244` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 0 -> 61 -> 71 |
| `7585a7d9dd9f1c5c3f92` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 37 -> 38 -> 84 |
| `9467f6661252ed56b5e1` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h347 / 0 -> 14 -> 17 |
| `b47b718b67278cee759d` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h347 / 0 -> 6 -> 17 |
| `ed12ad2a881e4e7643f7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 37 -> 91 -> 106 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 82 -> 119 -> 117 |
| `01ca7c0b518607c1d995` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h347 / 37 -> 36 -> 26 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h41 / 19 -> 17 -> 11 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 117 -> 115 -> 72 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 13 -> 39 -> 90 |
| `076f338100bee6b3f46a` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h347 / 15 -> 30 -> 29 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 119 -> 116 -> 115 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h41 / 17 -> 13 -> 15 |
| `0f841c4f8501e3ca5b7b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h347 / 30 -> 29 -> 20 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 104 -> 119 -> 117 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h0 / 69 -> 105 -> 1 |
| `16bbbbb5b786ec4e4789` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_04\ma_std_rcr_04_phase.questphase` / h481 / 0 -> 3 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
