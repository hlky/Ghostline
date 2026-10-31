# base-sts-cct-dtn-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\community\sts_cct_dtn_05.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\community\sts_cct_dtn_05_default_state.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\community\sts_cct_dtn_05_flathead.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\community\sts_cct_dtn_05_johnny.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\community\sts_cct_dtn_05_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.quest` | content candidate | 1 / 0 | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.questphase |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase |
| `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\sts_cct_dtn_05_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/dino_dinovic/sts_cct_dtn_05/sts_cct_dtn_05_brief`
- `contacts/dino_dinovic/sts_cct_dtn_05/sts_cct_dtn_05_data_recived`
- `contacts/dino_dinovic/sts_cct_dtn_05/sts_cct_dtn_05_debrief`
- `contacts/dino_dinovic/sts_cct_dtn_05/sts_cct_dtn_05_debrief_notperfect`
- `contacts/dino_dinovic/sts_cct_dtn_05/sts_cct_dtn_05_debrief_perfect`
- `points_of_interest/street_stories/sts_cct_dtn_05`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/des`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/escape_from_docks`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/extra_reward`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/get_to_donsk_control_room`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/go_to_the_docks`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/stealth`
- `quests/street_stories/city_center/downtown/sts_cct_dtn_05/sts_cct_dtn_05/take_or_hack_disc`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 32 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 17 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 9 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 7 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 14 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 11 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 9 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 6 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `480a010388ce3a487ffb` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h256 / 21 -> 25 -> 26 |
| `4c068ae78925bce2e854` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h256 / 54 -> 55 -> 47 |
| `4ff3abfc2e95448213b9` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h256 / 25 -> 26 -> 30 |
| `9380dda43f90ecd62efb` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h243 / 27 -> 25 -> 29 |
| `a36102ceee6fef729c5f` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h256 / 24 -> 25 -> 26 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 249 -> 270 -> 254 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 286 -> 284 -> 288 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 76 -> 286 -> 284 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 24 -> 75 -> 77 |
| `4365cb473b16f3e76999` | 3 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h243 / 73 -> 47 -> 56 |
| `b769ade732d21ee6cf4f` | 3 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h243 / 73 -> 47 -> 55 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 270 -> 71 -> 74 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 249 -> 270 -> 71 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene` / scene / 275 -> 271 -> 280 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h614 / 128 -> 129 -> 130 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 75 -> 77 -> 72 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 1 -> 282 -> 76 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene` / scene / 76 -> 70 -> 249 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_openworld.questphase` / h614 / 188 -> 185 -> 184 |
| `4061ed5f9fcb52c86679` | 2 | `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\phases\sts_cct_dtn_05_combat.questphase` / h0 / 11 -> 19 -> 20 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
