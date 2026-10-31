# base-ma-wat-nid-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\community\ma_wat_nid_15.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15_phase.questphase; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\test\ma_wat_nid_15_chicken.scene; base\quest\additional_game_elements.questphase; base\quest\bugfixing\minor_quests\ma_wat_nid_15\ma_wat_nid_15_quest_bugfixes.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_01_briefing.scene; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene; base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene; base\quest\side_quests\sq025\scenes\sq025_05_scan.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_01_briefing.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` | content candidate | 0 / 381 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\test\ma_wat_nid_15_chicken.scene` | test/debug | 0 / 4 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_nid_15\ma_wat_nid_15_quest_bugfixes.questphase` | repair | 6 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_nid_15/00_msg_intro`
- `contacts/regina_jones/ma_wat_nid_15/00_msg_start`
- `contacts/regina_jones/ma_wat_nid_15/01_ch_info`
- `contacts/regina_jones/ma_wat_nid_15/02_msg_regina`
- `contacts/regina_jones/ma_wat_nid_15/03a_ch_alive`
- `contacts/regina_jones/ma_wat_nid_15/03a_ch_alive/03a_ch_alive`
- `contacts/regina_jones/ma_wat_nid_15/03b_ch_dead`
- `contacts/regina_jones/ma_wat_nid_15/03b_ch_dead/03b_ch_dead`
- `contacts/regina_jones/ma_wat_nid_15/05_msg_conclusion_alive`
- `contacts/regina_jones/ma_wat_nid_15/05b_msg_conclusion_dead`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_15/onscreens/ma_wat_nid_15_shard_mls`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_15/onscreens/ma_wat_nid_15_shard_psycho`
- `onscreens/tutorials_new/encrypted_shard`
- `points_of_interest/minor_quests/ma_wat_nid_15`
- `quests/minor_quest/ma_wat_nid_15`
- `quests/minor_quest/ma_wat_nid_15/description`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/check_shard`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/check_shard_psycho`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/find_ritual`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/hack_shard_mls`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/kill_psycho`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/kill_psycho/area`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/kill_psycho/psycho`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/look_survivors`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/loot_corpse`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/loot_psycho`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/search_clues`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/search_clues/johnny`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/send_info`
- `quests/minor_quest/ma_wat_nid_15/ma_wat_nid_15/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 22 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 6 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 24 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 13 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 47 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 10 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 11 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 31 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 4 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 26 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 35 |
| `questPauseConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 10 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 18 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questShowPopup_NodeSubType,questTutorial_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 21 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 14 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnscreenplayItemId]` | 12 |
| `scnCutControlNode[scnNodeId]` | 10 |
| `scnDeletionMarkerNode[scnNodeId]` | 8 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 25 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 13 |
| `scnStartNode[scnNodeId]` | 4 |
| `scnXorNode[scnNodeId]` | 20 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2be70c555d6a95de2942` | 6 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 3943 -> 3876 -> 41 |
| `a573a324098f51248364` | 6 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 3943 -> 3876 -> 41 |
| `2281ce80c08463c13782` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2240 -> 2233 -> 2573 |
| `229190bc9802d8c207db` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 207 -> 208 -> 2467 |
| `373bad7f7ac9c4868f51` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 37 -> 2458 -> 246 |
| `40fc39f63460775163d2` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2964 -> 2542 -> 3108 |
| `453933c9298365b8abff` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2685 -> 2964 -> 2542 |
| `7ec1c828d8a3ad9b4116` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 14 -> 15 -> 2536 |
| `aa437964546ea2bf479a` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 246 -> 16 -> 200 |
| `c049a2177e6409440132` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2540 -> 2685 -> 2964 |
| `d10727aa04b4965aa867` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2510 -> 2531 -> 2511 |
| `d4b0d93c1fc1901f304f` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2467 -> 241 -> 237 |
| `dbd22cde487220090cc9` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2685 -> 2964 -> 2558 |
| `de91973144400bd7daef` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 246 -> 199 -> 200 |
| `f16f84348e8bf9459245` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2467 -> 241 -> 236 |
| `fdef3a295bce1c3e02c1` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 3108 -> 3471 -> 3431 |
| `fe71b603ec9df6303745` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 199 -> 200 -> 2693 |
| `064485326507b906fa89` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 3943 -> 3876 -> 40 |
| `16bd6948eebbc5a6d14c` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2716 -> 2375 -> 2719 |
| `a30296c7b99c80fb830b` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene` / scene / 2375 -> 2719 -> 2380 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
