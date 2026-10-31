# base-sts-wbr-hil-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\community\hil_07_com_after.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\community\sts_wbr_hil_07_civs.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\community\sts_wbr_hil_07_com_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\community\sts_wbr_hil_07_corpses.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_gameplay.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07.scene; base\open_world\vendors\westbrook\charter_hill\wbr_hil_foodshop_02\wbr_hil_foodshop_02.scene |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07.scene` | content candidate | 0 / 21 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07.quest` | content candidate | 1 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07.questphase |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\sts_wbr_hil_07_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/wakako_okada/sts_wbr_hil_07/sts_wbr_hil_07_brief`
- `contacts/wakako_okada/sts_wbr_hil_07/sts_wbr_hil_07_holocall_debrief`
- `points_of_interest/service_points/wbr_hil_foodshop_02`
- `points_of_interest/street_stories/sts_wbr_hil_07`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/brief`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/call_fixer`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_in`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_drainage_serwers`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/get_to_vortex_den/vortex_shard`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/scan`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 36 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 19 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 11 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 17 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 4 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType,questLogicalCondition,questSensesCondition,questVision_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 16 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 5 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questPaymentBalanced_ConditionType,questPaymentCondition,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `d1f111c26d5b25a439ba` | 8 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h10 / 4 -> 5 -> 6 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 273 -> 261 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 64 -> 283 -> 281 |
| `05654a41a34dbd7ac8c5` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h10 / 5 -> 8 -> 9 |
| `087ee7415a18b2106b7a` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h10 / 5 -> 6 -> 9 |
| `0bc8f68e59c0b883af0d` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 221 -> 200 -> 205 |
| `0c03b966286e3ac022cb` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 78 -> 169 -> 160 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 29 -> 63 -> 65 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 261 -> 59 -> 62 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 273 -> 261 -> 59 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_prebrief.scene` / scene / 269 -> 273 -> 279 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 129 -> 133 -> 142 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 63 -> 65 -> 60 |
| `22adbd10519df5772f7c` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 221 -> 200 -> 206 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 59 -> 62 -> 29 |
| `279d49ced382bf8957df` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_bugfixing.questphase` / h10 / 5 -> 7 -> 9 |
| `2a18d536739310eb7e61` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\phase\sts_wbr_hil_07_ow.questphase` / h169 / 210 -> 128 -> 129 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 56 -> 279 -> 64 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_07\scenes\sts_wbr_hil_07_holocall_debrief.scene` / scene / 64 -> 58 -> 273 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
