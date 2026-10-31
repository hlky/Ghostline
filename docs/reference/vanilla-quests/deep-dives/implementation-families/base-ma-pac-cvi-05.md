# base-ma-pac-cvi-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\community\ma_pac_cvi_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\community\ma_pac_cvi_05_com_reinforcement.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\community\ma_pac_cvi_05_valentinos_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_05/onscreens/ma_pac_cvi_05`
- `points_of_interest/minor_activities/ma_pac_cvi_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 8 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 5 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `502eb41b7f76d4723b4d` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 101 -> 16 -> 49 |
| `808c42396a9735fe3a65` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 0 -> 16 -> 49 |
| `d30dec206567a53c3ede` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 16 -> 49 -> 45 |
| `12b102391853a0e26cba` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 96 -> 97 -> 102 |
| `56c53a847765e20a971f` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 61 -> 54 -> 53 |
| `7214221ab5d271ce1333` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 59 -> 61 -> 54 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 0 -> 2 -> 3 |
| `c979dc8cc7db14abf187` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 49 -> 45 -> 57 |
| `d45e4c43b6d7299f8f46` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 101 -> 2 -> 3 |
| `037e1a1a92454febf234` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_bugfixing.questphase` / h19 / 9 -> 10 -> 1 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 112 -> 108 -> 107 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 44 -> 69 -> 43 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 97 -> 102 -> 104 |
| `0e8d31c8de5feb590e36` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h54 / 4 -> 26 -> 1 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 33 -> 40 -> 44 |
| `159599f19533cfcfe918` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 100 -> 99 -> 38 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 39 -> 68 -> 95 |
| `1e78cf05f701e41dff72` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h0 / 95 -> 103 -> 96 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_phase.questphase` / h54 / 16 -> 15 -> 14 |
| `237687944a84dd96b7b5` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_05\ma_pac_cvi_05_bugfixing.questphase` / h19 / 0 -> 3 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
