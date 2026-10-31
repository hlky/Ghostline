# base-sts-std-rcr-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\community\sts_std_rcr_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\community\sts_std_rcr_04_com_combat.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_combat.questphase; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_combat.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_chats.scene |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_main_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` | content candidate | 8 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_prebrief.scene; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_johnny.scene |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_chats.scene` | content candidate | 0 / 10 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_johnny.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\sts_std_rcr_04_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\sts_std_rcr_04_nc_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\sts_std_rcr_04_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/rcr_04/brief`
- `contacts/muamar_el_capitan_reyes/rcr_04/sts_std_rcr_04_holocall_debriefs`
- `points_of_interest/street_stories/sts_std_rcr_04`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/briefing`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/access_miss_rose_garage`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/destroy_server`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/destroy_server/server`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/enter_garage_area`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/leave_area`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04/sts_std_rcr_04/look_for_garage_66`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEventManagerNodeDefinition` | 18 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 29 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 17 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 29 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 15 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMiscAICommandNode` | 7 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 16 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 14 |
| `questPhaseNodeDefinition` | 15 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f3af3a0144803102e434` | 11 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` / h83 / 124 -> 87 -> 77 |
| `9380dda43f90ecd62efb` | 9 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` / h83 / 87 -> 100 -> 133 |
| `0ae0c4c8f4de2e085375` | 7 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` / h83 / 77 -> 127 -> 145 |
| `d9b2ab6619cc26411970` | 6 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` / h433 / 0 -> 10 -> 4 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 264 -> 267 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 283 -> 285 -> 287 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 66 -> 283 -> 285 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 16 -> 65 -> 67 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 267 -> 61 -> 64 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 264 -> 267 -> 61 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 65 -> 67 -> 62 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 61 -> 64 -> 16 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 1 -> 281 -> 66 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 66 -> 60 -> 264 |
| `340d028e5d410aaca2ca` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04.questphase` / h0 / 22 -> 5 -> 0 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_openworld.questphase` / h83 / 114 -> 116 -> 113 |
| `44e16681fbad62c8e945` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_chats.scene` / scene / 54 -> 15 -> 32 |
| `5c76d3bf7160f29b884f` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\phases\sts_std_rcr_04_bugfixing.questphase` / h14 / 3 -> 2 -> 18 |
| `69a2aad2f79abb156101` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene` / scene / 60 -> 264 -> 267 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
