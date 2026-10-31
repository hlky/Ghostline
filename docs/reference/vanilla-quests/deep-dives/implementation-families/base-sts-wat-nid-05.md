# base-sts-wat-nid-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\community\sts_wat_nid_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\community\sts_wat_nid_05_com_reinforcement.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_phase.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_regina_call.scene` | content candidate | 0 / 19 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene` | content candidate | 0 / 21 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\sts_wat_nid_05.quest` | content candidate | 3 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_phase.questphase; base\open_world\vendors\watson\northside\northside_vendors.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\sts_wat_nid_05_gamedef.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/player`
- `contacts/regina_jones`
- `contacts/regina_jones/sts_wat_nid_05/brief`
- `contacts/regina_jones/sts_wat_nid_05/debrief`
- `contacts/regina_jones/sts_wat_nid_05/sts_wat_nid_05_debrief`
- `points_of_interest/street_stories/sts_wat_nid_05`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/brief`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/escape_clinic`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/find_recording`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/get_to_clinic`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/steal_recording`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/steal_recording/find_recording_mp`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05/sts_wat_nid_05/steal_recording/steal_recording_mp`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 30 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 18 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 13 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPhaseNodeDefinition` | 12 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questPhoneManagerNodeDefinition[questCallContact_NodeType]` | 3 |
| `questPhoneManagerNodeDefinition[questSetPhoneStatus_NodeType]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 10 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 13 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase` / h12 / 4 -> 5 -> 6 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 249 -> 252 -> 254 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 65 -> 283 -> 281 |
| `3b70bb506b872cadfa43` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene` / scene / 22 -> 309 -> 24 |
| `0f26c46c87ccd874fc3a` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene` / scene / 22 -> 61 -> 21 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 28 -> 64 -> 66 |
| `10ac8cb355f355254ee3` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase` / h184 / 9 -> 38 -> 58 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 252 -> 60 -> 63 |
| `11fb797d6ef6d81c6c15` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene` / scene / 99 -> 298 -> 303 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 249 -> 252 -> 60 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_prebrief.scene` / scene / 270 -> 273 -> 280 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 64 -> 66 -> 61 |
| `2251a3c44ea8a153bc79` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase` / h67 / 0 -> 9 -> 11 |
| `2394003fd7b26c5666e2` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase` / h184 / 55 -> 6 -> 8 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 60 -> 63 -> 28 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 1 -> 279 -> 65 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene` / scene / 65 -> 59 -> 249 |
| `2face0cc90a9b0fee909` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase` / h87 / 82 -> 33 -> 34 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase` / h87 / 99 -> 101 -> 100 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
